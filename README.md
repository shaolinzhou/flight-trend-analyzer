# Flight Trend & Optimization Analyzer
*Stage 03: API-integration och Barnklass LiveFlightAPI*

---

## 📌 1. Projektöversikt
I detta stadium utökas det objektorienterade systemet med en barnklass som ansluter till ett offentligt REST API för att hämta globala flyglägen i realtid.

---

## 🔄 2. Projektmålsförändring och API-undersökning (Mål 1 & 7)
I ett tidigt skede av projektet övervägdes en statisk analys av historiska biljettpriser. För att bättre spegla en verklig AI-utvecklarroll och modern datainsamling beslutades dock att **omformulera målet**:
- Istället för statiska CSV-filer fokuserar vi på **strömmande realtidsdata** via externa REST API:er.
- Efter en utvärdering av olika flygdatakällor (såsom FlightAware och OpenSky Network) valdes **OpenSky Network API** tack vare dess öppna akademiska tillgång, tillförlitliga telemetriska tillståndsvektorer och direkta lämplighet för framtida maskininlärningsmodeller.

---

## 🌐 3. Datakälla: OpenSky Network API (Mål 7: Externa API:er)
- **Endpunkt**: `https://opensky-network.org/api/states/all`
- **Format**: JSON-payload innehållande tillståndsvektorer för alla luftburna plan jorden runt.
- **Parametrar**: Varje post innehåller bland annat ICAO24 (unikt transponder-ID), anropssignal (callsign), ursprungsland, longitud, latitud, barometrisk höjd och hastighet.

---

## 🏗️ 4. Objektorienterat Arv (Mål 3: Klasser och Arv)
Vi definierar barnklassen `LiveFlightAPI` som ärver från `FlightDataAnalyzer`:
```python
class LiveFlightAPI(FlightDataAnalyzer):
    # Barnklassen utökar basklassen med nätverks- och API-logik
```
- **Metod `fetch_live_flights(limit=100)`**: Gör HTTP GET-anrop med `requests`, kontrollerar statuskoder och populerar instansvariabeln `self.df`.
- **Testmetod `test_api_connection()`**: Verifierar att API-anslutningen fungerar och returnerar data.

---

## 🛠️ 5. Pågående arbete (Aktuella uppgifter för Stage 03)
- **Fokus**: API-integration via barnklass och nätverksverifiering.
- **Git Commit**: `feat: undersök API och implementera LiveFlightAPI`
- **Testmetod**: `live_api.test_api_connection()`

---

## 📊 6. Kom igång
```python
from src.flight_logic import LiveFlightAPI

live_api = LiveFlightAPI()
if live_api.fetch_live_flights(limit=50):
    print(f"Framgång! Laddade {len(live_api.df)} flygningar.")
```

---
*Kurs: Utveckling med Python, grund (40 YH-poäng) – Examinationsuppgift*
