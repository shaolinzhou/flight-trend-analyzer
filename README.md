# Flight Trend & Optimization Analyzer
*Stage 10: Dataexport till CSV (Inlämningskrav)*

---

## 📌 1. Projektöversikt
Ett av de obligatoriska kraven för godkänt (G) i kursen är att programmet kan hantera och spara extern data till en fil (.csv eller .json) som bifogas examinationen.

---

## 💾 2. Datahantering och Persistens (Mål 4 & 7)
- **Metod `export_cleaned_data(output_filepath)`**:
  - Sparar den validerade och rengjorda datamängden till filen `live_flights_data.csv`.
  - Använder UTF-8-kodning och utesluter standardindexet (`index=False`).
  - Innehåller skyddande felhantering (`IOError`) för att förhindra krasch vid filåtkomstproblem.
- **Dataschemat**:
  - `icao24`: Transponder-ID
  - `callsign`: Anropssignal
  - `country`: Ursprungsland
  - `longitude`, `latitude`: Koordinater
  - `altitude`: Barometrisk höjd (m)
  - `velocity`: Hastighet (m/s)
  - `heading`: Riktning i grader

---

## 🛠️ 3. Pågående arbete (Aktuella uppgifter för Stage 10)
- **Fokus**: Implementera och verifiera CSV-exporten.
- **Git Commit**: `feat: implementera CSV-export`
- **Testmetod**: `live_api.show_export_info()`
- **Leverabel**: `live_flights_data.csv` finns nu genererad i mappen.

---

## 📊 4. Kom igång
```python
from src.flight_logic import LiveFlightAPI

live_api = LiveFlightAPI()
live_api.fetch_live_flights(limit=300)
live_api.export_cleaned_data("live_flights_data.csv")
```

---
*Kurs: Utveckling med Python, grund (40 YH-poäng) – Examinationsuppgift*
