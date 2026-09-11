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
        return {
            "total_flights": int(len(self.df)),
            "columns": list(self.df.columns),
            "total_countries": int(self.df["country"].nunique()) if "country" in self.df else 0
        }

class LiveFlightAPI(FlightDataAnalyzer):
    """Barnklass med datavalidering, rengöring och landsfiltrering (Mål 3 & 6)."""

    API_URL = "https://opensky-network.org/api/states/all"

    def fetch_live_flights(self, limit: int = 100) -> bool:
        """Hämta och rengör realtidsflygdata."""
        try:
            response = requests.get(self.API_URL, timeout=12)
            response.raise_for_status()
            flights = response.json().get("states", [])
            if not flights:
                return False

            records: List[Dict[str, Any]] = []
            for flight in flights[:limit]:
                callsign = flight[1].strip() if flight[1] else "N/A"
                records.append({
                    "icao24": flight[0],
                    "callsign": callsign,
                    "country": flight[2],
                    "longitude": flight[5],
                    "latitude": flight[6],
                    "altitude": flight[7],
                    "velocity": flight[9],
                    "heading": flight[10]
                })
            raw_df = pd.DataFrame(records)
            # Rengöring: ta bort saknade nödvändiga fält
            self.df = raw_df.dropna(subset=["icao24", "country"]).copy()
            print(f"[SUCCESS] Validated and cleaned {len(self.df)} records.")
            return True
        except Exception as e:
            print(f"[ERROR] API fetch error: {e}")
            if os.path.exists("live_flights_data.csv"):
                self.df = pd.read_csv("live_flights_data.csv").head(limit)
                return True
            return False

    def get_flights_by_country(self, country: str = "United States") -> pd.DataFrame:
        """Filtrera flyg baserat på ursprungsland."""
        if self.df.empty:
            print("[WARNING] Ingen flygdata tillganglig for filtrering.")
            return pd.DataFrame()
        filtered = self.df[self.df["country"] == country]
        print(f"[INFO] {country}: {len(filtered)} aktiva flyg hittades.")
        return filtered

    def show_data_info(self) -> None:
        """Stage 04 testmetod: Visa struktur och validering av hämtad data."""
        if self.df.empty:
            self.fetch_live_flights(limit=100)
        print("[TEST] Stage 04: Data validation & info check:")
        print(f"  Shape: {self.df.shape}")
        print(f"  Missing altitude: {self.df['altitude'].isna().sum() if 'altitude' in self.df else 0}")
        print(f"  Missing velocity: {self.df['velocity'].isna().sum() if 'velocity' in self.df else 0}")
