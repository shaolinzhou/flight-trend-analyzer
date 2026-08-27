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

