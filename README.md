# Flight Trend & Optimization Analyzer
---

## 📌 1. Om projektet
Det här är ett Python-program. Programmet är skrivet med objektorientering (OOP). Programmet hämtar **flygdata i realtid** från OpenSky Network API. Sedan rensar programmet datan. Programmet gör också statistik och bilder (grafer).

Projektet är en uppgift i kursen **Utveckling med Python, grund** (40 YH-poäng). Jag har gjort detta:
- Tydlig struktur med klasser
- Bra felhantering för nätverk och filer
- Hela processen med grafer från Matplotlib och export till CSV
- Mer än 10 commits på GitHub
- En analys av branschen, certifikat och en reflektion

## 📦 2. Vad ska lämnas in
1. **Jupyter Notebook (`flight_analyzer.ipynb`)**: En notebook med 21 celler. Det finns text (markdown) som förklarar arbetet. Klasserna `FlightDataAnalyzer` och `LiveFlightAPI` finns i cell 4. Rubriken där heter "FLIGHT LOGIC". Notebooken behöver inga andra filer.
2. **Datafil (`live_flights_data.csv`)**: 500 flygposter. Datan kommer från OpenSky API. Datan är rensad och kontrollerad.
3. **Dokumentation (`README.md`)**: En rapport med mål, metod, resultat, branschanalys, certifikat och reflektion.

---

## 🛠️ 3. Metod och teknik
- **OOP och arv**: Basklassen `FlightDataAnalyzer` har den statistiska logiken. Barnklassen `LiveFlightAPI` hämtar data från API:et. Den rensar också datan.
- **JSON-data och integration**:
  - *Adress och format*: OpenSky Network API (`https://opensky-network.org/api/states/all`) skickar ett **JSON-svar**.
  - *Avkodning*: Metoden `requests.get().json()` gör om JSON till en Python-ordlista. Nyckeln `"states"` har en lista med data om flygplan.
  - *Data från index*: Varje flygning har 17 fält. Fälten har inga namn, bara nummer. Koden hämtar `icao24` (nummer 0), `callsign` (nummer 1), `country` (nummer 2), longitud/latitud (nummer 5/6), höjd (nummer 7) och fart (nummer 9). Datan går till en Pandas DataFrame.
- **Bibliotek**:
  - Standardbibliotek: `os`, `typing` (OBS: `json` används **inte** i notebooken. JSON läses med `response.json()` från `requests` i stället.)
  - Externa bibliotek: `requests` (för API), `pandas` (för analys), `matplotlib` (för grafer)
- **Felhantering**: Try/except skyddar mot nätverksfel (`ConnectionError`, `Timeout`), HTTP-fel och filfel (`IOError`). Om något går fel, använder programmet filen `live_flights_data.csv` i stället.

---

## 📊 4. Resultat och analys
- **Länder**: USA och Indien har flest flygningar. Sedan kommer Tyskland (ibland också Frankrike, Ungern eller Sverige). Topp 5-listan kan ändras. Det beror på vad OpenSky API visar just då.
- **Fart i luften**: De flesta flygplan har en fart mellan 200 och 250 m/s. Höjden är mellan 8 000 och 12 000 meter.
- **Callsigns**: SAS, Lufthansa, Air France och United Airlines var mest aktiva under testet.

---

## 🎓 5. Branschanalys och trender (AI och Data Engineering)
Koden visar de första stegen i en professionell datapipeline. Här är tre exempel:

1. **Analys av flygsituationen just nu**: `fetch_live_flights()` hämtar live-data från OpenSky. `calculate_summary_stats()` och `get_flights_by_country()` visar hur många flygningar det finns per land. De visar också medelfart och medelhöjd. Notebooken visar grafer om de mest aktiva länderna och flygbolagen (efter callsign). Man ser trafiken direkt.

2. **Övervakning av flygrutter**: Varje flygpost har longitud, latitud och `heading`  . Detta är basdata för att följa en flygväg. Metoden `run_final_test()` kontrollerar hela pipelinen. Detta är en bra grund för att övervaka rutter. 

3. **En stabil ETL-pipeline**: Koden gör Extract–Transform–Load. Extract: `requests.get().json()` hämtar data från OpenSky. Transform: koden kopplar data (icao24, callsign, land, position, höjd, fart) till en Pandas DataFrame. Koden rensar med `dropna()` och tar bort dåliga callsigns. Load: `export_cleaned_data()` sparar data som CSV. Om nätverket inte fungerar, använder programmet filen `live_flights_data.csv`. Detta gör pipelinen stabil.

Detta projekt visar det första steget i AI-arbete: **ETL (Extract, Transform, Load)**. Man gör bra träningsdata från rådata.

---

## 💡 6. Reflektion och utvärdering

### Vad gick bra?
- **OOP och struktur**: Koden har tydliga klasser (`FlightDataAnalyzer` är basklass, `LiveFlightAPI` är barnklass). I notebooken ligger klasserna i en egen kodcell. Tidigare låg de i en annan fil. Nu är koden ren och lätt att läsa. Koden följer PEP 8.
- **Versionshantering**: Jag dokumenterade arbetet med 14 commits.
- **Export av data**: CSV-exporten fungerade bra. All data kom med.
- **Att ändra plan**: Jag kunde se ett problem snabbt. Sedan bytte jag till en bättre lösning.

### Vad var svårt? Vad gick fel?
- **Problem: Jag förstod inte kraven i början**:
  - *Bakgrund*: Först ville jag använda gamla flygpriser från en Kaggle-fil (`Data_Train.csv`). Jag hade inte läst kursens krav noga. Jag förstod inte vad läraren ville ha, speciellt om extern data och AI.
  - *Ny idé*: I slutet av Stage 02 förstod jag att en statisk CSV-fil inte var bra nog. Den passade inte för ett VG-betyg. I Stage 03 tog jag ett modigt beslut. Jag slutade med den gamla planen. Jag började använda OpenSky Network API för live-data i stället.
  - *Vad jag lärde mig*: I riktiga projekt kan fel förståelse av kraven ge problem och kosta mer tid och pengar. Jag lärde mig att analysera kraven ordentligt innan man börjar koda. Man ska våga byta plan snabbt. Man ska inte fastna i gamla beslut (*sunk cost fallacy*). Detta gjorde projektet mycket bättre.
- **Problem med API och nätverk**: OpenSky API har gränser för anonyma användare. Ibland blir det nätverksfel. Jag behövde noggrann kod med timeouts, felhantering (`requests.exceptions.RequestException`) och en backup-fil om nätverket inte fungerar.
- **Teckenkodning i Windows**: Text i konsolen behövde extra kontroll. Det fanns problem mellan UTF-8 och Windows kodning (GBK/CP1252).

### Vad kan bli bättre nästa gång?
- **Statistik per flygbolag, inte per callsign**: Nu räknar koden statistik efter `callsign` (se `get_top_airlines()`). Detta räknar varje flightsignatur, inte flygbolaget. Nästa steg: ta de tre första bokstäverna i callsignen (till exempel `SAS`, `DLH`, `AFR`, `UAL`). Koppla dessa till ett riktigt flygbolagsnamn med en tabell. Då visar listan "mest aktiva flygbolag" riktiga flygbolag, inte bara enskilda signaturer.
- **Live-övervakning med databas, var 10:e sekund**: Byt CSV mot en databas (till exempel SQLite eller PostgreSQL). Databasen sparar varje avläsning med tid. Ett program (`APScheduler` eller en bakgrundstråd) hämtar data från OpenSky var 10:e sekund. Programmet sparar raderna. En funktion kan hitta konstiga saker: snabb ändring av fart eller höjd, flygplan som inte rör sig, eller callsigns som försvinner eller kommer plötsligt.
- **Ta bort dubbelt arbete och död kod**: `country.value_counts()` räknas tre gånger nu (cell 8, cell 13 och `run_final_test`). Detta bör bli en metod med cache. Också: `get_top_airlines()` finns men används inte i notebooken. Den bör användas eller tas bort.

---

## 🤖 7. AI-verktyg och GDPR
Här ser du hur jag använde AI i projektet:
- **AI som hjälp**: Jag använde AI (ChatGPT / Copilot) som en partner. AI hjälpte mig med:
  1. *Diskussion om arkitektur*: Vi pratade om ansvaret mellan basklass (`FlightDataAnalyzer`) och barnklass (`LiveFlightAPI`).
  2. *Undersökning av API*: Det var svårt att förstå OpenSky Network API:et (`https://opensky-network.org/api/states/all`). Datan har ingen struktur med namn, bara en lista med nummer. AI hjälpte mig att förstå och koppla de 17 fälten (ICAO24, callsign, land, position, höjd, fart) till en Pandas DataFrame. Det gick mycket snabbare med hjälp av AI.
  3. *Felsökning*: AI hjälpte med Pandas-funktioner och stabil felhantering för nätverket (timeouts, felkoder och backup-lösning).
  4. *Struktur för dokumentation*: AI hjälpte med mallar för commit-meddelanden och rapportens struktur.
- **Språkgranskning på svenska**: Jag skrev denna README själv först. Sedan använde jag AI för att förbättra språket (meningar, ord och flyt). Innehållet och tekniska fakta ändrades inte.
- **GDPR och personuppgifter**: Jag har inte gett några personuppgifter till AI-verktyg online. Datan har bara offentlig flyginformation (ICAO24-koder, callsigns, fart och position).

---

## 🔗 8. GitHub och inlämning
- **Repository**: [https://github.com/shaolinzhou/flight-trend-analyzer](https://github.com/shaolinzhou/flight-trend-analyzer)
- **Commits**: 14 commits visar hela arbetet, från start till färdig produkt.

---

## 🚀 9. Installation och körning (Kom igång)
1. Klona repositoryt och gå till mappen:
   ```bash
   git clone https://github.com/shaolinzhou/flight-trend-analyzer.git
   cd flight-trend-analyzer
   ```
2. Skapa och starta en virtuell miljö:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install pandas requests matplotlib 
   ```
3. Starta notebooken:
   ```bash
   jupyter notebook flight_analyzer.ipynb
   ```
---
