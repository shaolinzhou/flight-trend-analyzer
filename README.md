# Flygprisanalys och avgångstidsoptimering

## 📌 1. Project Overview (Projektöversikt)

Detta projekt är ett objektorienterat (OOP) Python-program som hämtar **realtids flygdata** från OpenSky Network API och utför dataanalys med fokus på:
- Landfördelning av aktiva flyg
- Hastighets- och höjdsanalys
- Filtrering och export av data

Målet är att visa grundläggande Python-programmeringsprinciper, felhantering, datapipeline och dokumentation i linje med AI- och dataingenjörsbranschen.

---

## 📌 2. Uppgiftsbeskrivning (Task Scope)

Detta projekt syftar till att hämta och analysera **live flygdata** från OpenSky Network API. Genom en objektorienterad datapipeline analyseras flygfördelning, hastighet och höjd för att identifiera mönster i realtid.

---

## 🛠️ 3. Pågående arbete (Aktuella uppgifter)

### 1. Basklass för dataanalys (Base Class)
- Skapande av `FlightDataAnalyzer` som basklass
- Grundläggande funktioner för datahantering och statistik

---

## 🚀 4. Arbetsflöde (Pipeline)

`Datahämtning (API)` ➔ `Validering & Rengöring` ➔ `Analys & Visualisering` ➔ `Dataexport (CSV)`

---

## 📊 5. Kom igång – Basklass (Quick Start)

Huvudlogiken ligger i `src/flight_logic.py` och anropas från notebooken `flight_analyzer.ipynb`.

```python
from src.flight_logic import FlightDataAnalyzer

# Skapa basklass med testdata
analyzer = FlightDataAnalyzer()

# Hämta grundläggande statistik
stats = analyzer.calculate_summary_stats()
print(stats)
```

### Klassstruktur

```python
class FlightDataAnalyzer:
    """Basklass för flyghantering och analys."""

    def __init__(self, data=None):
        self.df = data if data is not None else pd.DataFrame()

    def calculate_summary_stats(self):
        # Returnerar total_flights, avg_velocity, min/max, etc.
```

---

## ✅ 6. Projektstatus (Status)

| # | Steg | Status |
|---|------|--------|
| 1 | Skapa basklass FlightDataAnalyzer | ✅ Klar |
| 2 | Lägg till API-barnklass | ⬜ |
| 3 | Datavalidering och rengöring | ⬜ |
| 4 | Landfördelningsanalys | ⬜ |
| 5 | Hastighet och höjd analys | ⬜ |
| 6 | For-loop sammanfattning | ⬜ |

---

*Skapad som en del av kursuppgiften Utveckling med Python, grund.*
