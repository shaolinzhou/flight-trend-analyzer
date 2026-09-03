# Flygprisanalys och avgångstidsoptimering

## 📌 1. Project Overview (Projektöversikt)

This project is an object-oriented Python application designed to analyze historical airline ticket data from Kaggle (`Clean_Dataset.csv` / `Data_Train.csv`). It performs automated data loading, cleaning, statistical aggregation, visualization, and persistent CSV export.

The primary goal is to demonstrate fundamental Python software engineering principles, robust error handling, data processing pipeline development, and documentation practices aligned with AI and data engineering industry standards.

---

## 📌 2. Uppgiftsbeskrivning (Task Scope)

Detta projekt syftar till att genomföra en inledande dataundersökning och förädling av flygbiljettsdata baserat på Kaggle-dataset (`Clean_Dataset.csv` / `Data_Train.csv`). Genom en objektorienterad (OOP) datapipeline analyseras flygpriser och avgångstider för att filtrera fram de mest prisvärda flygresorna.

---

## 🛠️ 3. Pågående arbete (Aktuella uppgifter)

### 1. Inledande dataundersökning (Data Exploration & Ingestion)
- Genomgång och strukturanalys av rådata för flygbiljetter.
- Felhantering vid inladdning samt datatvätt (t.ex. rensning av tomma värden och onödiga indexkolumner).

### 2. Filtrering och optimering av flyginformation (Flight Selection & Filtering)
- **Pris- och frekvensanalys för populära rutter**: Sammanställning av snittpriser och lägsta priser för de vanligaste flygrutterna.
- **Filtrering av optimerade "guld-flyg" (Best-Value Flights)**: Tillämpning av dubbla kvantilfilter (lägsta 20 % av priset samt kortaste 20 % av flygtiden) för att identifiera flyg med högsta prisvärdhet.
- **Tidsfördelningsanalys**: Visualisering av hur de optimerade flygresorna fördelar sig över olika avgångstider (`departure_time`).
- **Datalagring (Data Export)**: Exportering av de filtrerade, optimala flygresorna till en separat rapportfil (`best_value_flights.csv`).

---

## 🌐 4. Datakällor och Utvärdering (Data Sources Evaluation)

För att säkerställa projektets genomförbarhet har följande 4 datahämtningsalternativ utvärderats:

1. **Amadeus Self-Service API**
   - *Beskrivning*: Officiell API-plattform från den globala flyggiganten Amadeus.
   - *Funktioner*: Realtidssökning av flyg och prisprognoser (ca 2 000 fria anrop/månad).
2. **RapidAPI / Skyscanner API**
   - *Beskrivning*: Tredjeparts-API för snabb inläsning av lägsta priser på specifik rutt.
3. **Kaggle Statiskt Dataset (Vald huvudkälla / Chosen Primary Source ⭐⭐⭐⭐⭐)**
   - *Beskrivning*: Historisk databas med över 300 000 flygposteringar (`Clean_Dataset.csv`).
   - *Länk*: [Kaggle Flight Price Prediction Dataset](https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction)
   - *Motivering*: **Noll API-risk (ingen nätverksbegränsning/rate-limiting)**, perfekt anpassat för objektorienterad datatvätt, funktionsextrahering och stabil visualisering.
4. **Mock API / Lokal Genererad Data (Reservalternativ)**
   - *Beskrivning*: Lokal simulering med Python `faker`/`random` för reservtester.

---

## 🚀 5. Arbetsflöde (Pipeline)

`Datainläsning (Ingestion)` ➔ `Datatvätt (Cleaning)` ➔ `Analys & Visualisering (Analysis)` ➔ `Dataexport (Export)`

---

## 📊 6. Kom igång – enkel dataanalys (Quick Start)

Huvudlogiken ligger i `src/flight_logic.py` och anropas från notebooken `flight_analyzer.ipynb`.

```python
from src.flight_logic import KaggleFlightDataLoader

# 1. Läs in CSV från nuvarande arbetskatalog
loader = KaggleFlightDataLoader()
loader.load_data()

# 2. Förhandsvisa de 10 första raderna
print(loader.show_first_rows(10))
```

### Enkel dataöversikt (datamängdens egenskaper)

| Egenskap | Värde |
|---|---|
| Antal rader | 300 153 |
| Antal kolumner | 12 |
| Flygbolag | 6 (SpiceJet, AirAsia, Vistara, GO_FIRST, Indigo, Air_India) |
| Pris – medel / min / max | 20 890 / 1 105 / 123 071 |
| Genomsnittlig flygtid (timmar) | 12,2 |
| Klasser | Economy, Business |
| Avgångstidslottar | 6 (Early_Morning … Late_Night) |

### Exempel: snabb statistik med pandas

```python
import pandas as pd
df = pd.read_csv("Clean_Dataset.csv")

print(df.groupby("airline")["price"].agg(["mean", "min", "max"]))  # pris per flygbolag
print(df.describe())                                               # grundstatistik
```

---

## ✅ 7. Projektstatus (Status)

| # | Steg | Status |
|---|------|--------|
| 1 | Läsa in `Clean_Dataset.csv` och testa utskrift av första raderna | ✅ Klar (2026-09-03) |
| 2 | Datatvätt (hantera `Unnamed: 0`, tomma värden) | ⬜ |
| 3 | Grundstatistik & kolumnöversikt | ⬜ |
| 4 | Analysfunktioner (rutter, priser, avgångstider) | ⬜ |
| 5 | Visualisering av resultat | ⬜ |
| 6 | Export av analyserad data | ⬜ |

Se `dev.log` för detaljerad utvecklingslogg och arkitekturvision.

