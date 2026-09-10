import os
import pandas as pd
import requests
from typing import Dict, Any, Optional, List


class FlightDataAnalyzer:
    """Basklass for flyghantering och analys."""

    def __init__(self, data: Optional[pd.DataFrame] = None):
        """Initiera med valfri DataFrame."""
        self.df = data if data is not None else pd.DataFrame()

    def calculate_summary_stats(self) -> Dict[str, Any]:
        """Returnera grundläggande statistik om datasetet."""
        if self.df.empty:
            return {}
        try:
            return {
                "total_flights": int(len(self.df)),
                "avg_velocity": round(float(self.df["velocity"].mean()), 2),
                "min_velocity": float(self.df["velocity"].min()),
                "max_velocity": float(self.df["velocity"].max()),
                "avg_altitude": round(float(self.df["altitude"].mean()), 2)
            }
        except KeyError as e:
            print(f"[ERROR] Missing column: {e}")
            return {}

    def get_top_airlines(self, top_n: int = 10) -> pd.DataFrame:
        """Hanta toppflygbolag efter antal flyg."""
        required_cols = {"callsign", "icao24", "altitude", "velocity"}
        if self.df.empty or not required_cols.issubset(self.df.columns):
            print("[WARNING] Missing columns for airline analysis")
            return pd.DataFrame()
        try:
            airline_stats = self.df.groupby("callsign").agg(
                flight_count=("icao24", "count"),
                avg_altitude=("altitude", "mean"),
                avg_velocity=("velocity", "mean")
            ).reset_index()
            airline_stats["avg_altitude"] = airline_stats["avg_altitude"].round(2)
            airline_stats["avg_velocity"] = airline_stats["avg_velocity"].round(2)
            return airline_stats.sort_values(by="flight_count", ascending=False).head(top_n)
        except Exception as e:
            print(f"[ERROR] Airline analysis failed: {e}")
            return pd.DataFrame()


class LiveFlightAPI(FlightDataAnalyzer):
    """Barnklass - hämtar live flygdata fran OpenSky Network API."""

    API_URL = "https://opensky-network.org/api/states/all"

    def fetch_live_flights(self, limit: int = 100) -> bool:
        """Hanta live flygdata fran OpenSky Network API."""
        try:
            response = requests.get(self.API_URL, timeout=15)
            response.raise_for_status()
            data = response.json()

            flights = data.get("states", [])
            if not flights:
                print("[WARNING] API returned empty data")
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

            # Datavalidering: ta bort rader med saknade kritiska falt
            before_clean = len(self.df)
            self.df = self.df.dropna(subset=["velocity", "altitude"])
            after_clean = len(self.df)
            if before_clean != after_clean:
                print(f"[INFO] Cleaned {before_clean - after_clean} rows with missing data")

            print(f"[SUCCESS] Fetched {len(self.df)} valid flights")
            return True

        except requests.exceptions.ConnectionError:
            print("[ERROR] Network connection failed")
            return False
        except requests.exceptions.Timeout:
            print("[ERROR] Request timed out")
            return False
        except requests.exceptions.HTTPError as e:
            print(f"[ERROR] HTTP error: {e}")
            return False
        except (KeyError, IndexError) as e:
            print(f"[ERROR] API data parsing failed: {e}")
            return False
        except Exception as e:
            print(f"[ERROR] Unknown error: {e}")
            return False

    def get_flights_by_country(self, country: str = "United States") -> pd.DataFrame:
        """Filtrera flyg efter land."""
        if self.df.empty:
            print("[WARNING] No flight data available")
            return pd.DataFrame()
        try:
            filtered = self.df[self.df["country"] == country]
            print(f"[INFO] {country}: {len(filtered)} flights")
            return filtered
        except KeyError:
            print("[ERROR] 'country' column not found")
            return pd.DataFrame()

    def export_cleaned_data(self, output_filepath: str) -> bool:
        """Exportera data till CSV."""
        if self.df.empty:
            print("[WARNING] No data to export")
            return False
        try:
            self.df.to_csv(output_filepath, index=False, encoding="utf-8")
            print(f"[SUCCESS] Data exported to: {output_filepath}")
            return True
        except IOError as e:
            print(f"[ERROR] Export failed: {e}")
            return False
