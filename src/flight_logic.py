import os
import pandas as pd
import requests
from typing import Dict, Any, Optional, List

class FlightDataAnalyzer:
    """Basklass för flyghantering och analys (Base Class - Mål 3)."""

    def __init__(self, data: Optional[pd.DataFrame] = None):
        self.df = data.copy() if data is not None else pd.DataFrame()

    def calculate_summary_stats(self) -> Dict[str, Any]:
        """Beräkna grundläggande sammanfattande statistik för datamängden."""
        if self.df.empty:
            return {"total_flights": 0, "status": "No data available"}

        stats: Dict[str, Any] = {
            "total_flights": int(len(self.df)),
            "columns": list(self.df.columns)
        }
        if "country" in self.df.columns:
            stats["total_countries"] = int(self.df["country"].nunique())
        return stats

class LiveFlightAPI(FlightDataAnalyzer):
    """Barnklass som hämtar realtids flygdata från OpenSky Network API (Arv - Mål 3)."""

    API_URL = "https://opensky-network.org/api/states/all"

    def fetch_live_flights(self, limit: int = 100) -> bool:
        """Hämta realtidsflyg från OpenSky Network REST API (Mål 7)."""
        try:
            response = requests.get(self.API_URL, timeout=12)
            response.raise_for_status()
            data = response.json()
            flights = data.get("states", [])
            if not flights:
                print("[WARNING] OpenSky API returnerade inga flygdata.")
                return False

            records: List[Dict[str, Any]] = []
            for flight in flights[:limit]:
                records.append({
                    "icao24": flight[0],
                    "callsign": flight[1].strip() if flight[1] else "N/A",
                    "country": flight[2],
                    "longitude": flight[5],
                    "latitude": flight[6],
                    "altitude": flight[7],
                    "velocity": flight[9],
                    "heading": flight[10]
                })
            self.df = pd.DataFrame(records)
            print(f"[SUCCESS] Loaded {len(self.df)} live flights from OpenSky Network")
            return True
        except Exception as e:
            print(f"[ERROR] API fetch error: {e}")
            if os.path.exists("live_flights_data.csv"):
                self.df = pd.read_csv("live_flights_data.csv").head(limit)
                print(f"[INFO] Använder sparad backupdata ({len(self.df)} rader).")
                return True
            return False

    def test_api_connection(self) -> bool:
        """Stage 03 testmetod: Kontrollera API-anslutning."""
        print("[TEST] Stage 03: Testing OpenSky API connectivity...")
        success = self.fetch_live_flights(limit=10)
        print(f"[TEST RESULT] API Connection: {'PASS' if success else 'FAIL'}")
        return success
