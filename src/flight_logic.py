import os
import pandas as pd


class KaggleFlightDataLoader:
    """Läser in Clean_Dataset.csv från nuvarande arbetskatalog."""

    CSV_FILENAME = "..\Clean_Dataset.csv"

    def __init__(self, filepath: str = None):
        self.filepath = filepath or self.CSV_FILENAME
        self.df = None

    def load_data(self) -> bool:
        """Läser in CSV-filen och sparar resultatet i self.df."""
        path = self.filepath
        if not os.path.exists(path):
            print(f"[ERROR] Hittar inte filen: {path}")
            return False
        try:
            self.df = pd.read_csv(path)
            print(f"[SUCCESS] Inläst: {len(self.df)} rader, {len(self.df.columns)} kolumner")
            return True
        except Exception as e:
            print(f"[ERROR] Inläsning misslyckades: {e}")
            return False

    def show_first_rows(self, n: int = 10):
        """Visar de första n raderna."""
        if self.df is None:
            print("[ERROR] Ingen data inläst, kör load_data() först.")
            return None
        return self.df.head(n)


if __name__ == "__main__":
    loader = KaggleFlightDataLoader()
    if loader.load_data():
        print(loader.show_first_rows(10))
