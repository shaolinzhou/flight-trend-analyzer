import os
import pandas as pd
import requests
from typing import Dict, Any, Optional, List

class FlightDataAnalyzer:
    """Basklass för flyghantering och analys (Base Class - Mål 3)."""

    def __init__(self, data: Optional[pd.DataFrame] = None):
        self.df = data.copy() if data is not None else pd.DataFrame()

    def calculate_summary_stats(self) -> Dict[str, Any]:
        """Beräkna grundläggande sammanfattande statistik."""
        if self.df.empty:
            return {"total_flights": 0, "status": "No data available"}
        return {
            "total_flights": int(len(self.df)),
            "columns": list(self.df.columns),
            "total_countries": int(self.df["country"].nunique()) if "country" in self.df else 0
        }

class LiveFlightAPI(FlightDataAnalyzer):
    """Barnklass med hastighets- och höjdsanalys samt exportfunktion (Mål 3 & 6)."""

    API_URL = "https://opensky-network.org/api/states/all"

    def fetch_live_flights(self, limit: int = 200) -> bool:
        """Hämta och rengör realtidsflygdata."""
        try:
            response = requests.get(self.API_URL, timeout=12)
            response.raise_for_status()
            flights = response.json().get("states", [])
            if not flights:
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
            raw_df = pd.DataFrame(records)
            self.df = raw_df.dropna(subset=["icao24", "country"]).copy()
            return True
        except Exception as e:
            print(f"[ERROR] API fetch error: {e}")
            if os.path.exists("live_flights_data.csv"):
                self.df = pd.read_csv("live_flights_data.csv").head(limit)
                return True
            return False

    def get_flights_by_country(self, country: str = "United States") -> pd.DataFrame:
        """Filtrera flyg baserat på land."""
        if self.df.empty:
            return pd.DataFrame()
        return self.df[self.df["country"] == country]

    def get_top_airlines(self, top_n: int = 10) -> pd.DataFrame:
        """Hämta topp flygbolag baserat på callsign."""
        if self.df.empty:
            return pd.DataFrame()
        valid = self.df[(self.df["callsign"] != "N/A") & (self.df["callsign"].str.strip() != "")]
        stats = valid.groupby("callsign").agg(
            flight_count=("icao24", "count"),
            avg_altitude=("altitude", "mean"),
            avg_velocity=("velocity", "mean")
        ).reset_index()
        return stats.sort_values(by="flight_count", ascending=False).head(top_n)

    def export_cleaned_data(self, output_filepath: str = "live_flights_data.csv") -> bool:
        """Exportera rengjord data till CSV-fil (Mål 4 & 7)."""
        if self.df.empty:
            print("[WARNING] Ingen data att exportera.")
            return False
        try:
            self.df.to_csv(output_filepath, index=False, encoding="utf-8")
            print(f"[SUCCESS] Exporterade {len(self.df)} rader till '{output_filepath}'")
            return True
        except IOError as e:
            print(f"[ERROR] Kunde inte spara CSV-fil: {e}")
            return False

    def show_velocity_stats(self) -> None:
        """Stage 06 testmetod: Visa hastighets- och höjdstatistik."""
        if self.df.empty:
            self.fetch_live_flights(limit=100)
        print("[TEST] Stage 06: Velocity & Altitude stats:")
        if not self.df.empty and "velocity" in self.df:
            print(f"  Medelhastighet: {self.df['velocity'].mean():.2f} m/s")
            print(f"  Maxhastighet:   {self.df['velocity'].max():.2f} m/s")
            print(f"  Medelhojd:      {self.df['altitude'].mean():.2f} m")
