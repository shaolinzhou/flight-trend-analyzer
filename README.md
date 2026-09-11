# Flight Trend & Optimization Analyzer
*Stage 04: Datavalidering och Rengöring*

---

## 📌 1. Projektöversikt
Realtidstelemetri från tusentals flygplan innehåller ofta brus, saknade koordinater och ofullständiga anropssignaler. I Stage 04 fokuserar vi på validering och rengöring av inkommande data innan analysen startar.

---

## 🧹 2. Rengöringsmetodik (Mål 6: Programutveckling)
1. **Saknade fält**: Rader där `icao24` eller `country` saknas filtreras bort direkt med `.dropna()`.
2. **Anropssignaler (Callsigns)**: Tomma strängar rensas från mellanslag och ersätts med `'N/A'`.
3. **Numerisk integritet**: Säkerställer att hastighet och höjd hanteras korrekt som flyttal utan att orsaka krascher vid framtida beräkningar.

---

## 🔍 3. Nya funktioner i Stage 04
- `get_flights_by_country(country)`: Filtrerar ut aktiva flygningar för en specifik nation.
- `show_data_info()`: Sammanfattar dataramens dimensioner (`shape`) och räknar saknade värden.

---

## 🛠️ 4. Pågående arbete (Aktuella uppgifter för Stage 04)
- **Fokus**: Datakvalitetssäkring och landsfiltrering.
- **Git Commit**: `feat: add data validation and cleaning`
- **Testmetod**: `live_api.show_data_info()`

---

## 📊 5. Kom igång
```python
from src.flight_logic import LiveFlightAPI

live_api = LiveFlightAPI()
live_api.fetch_live_flights(limit=100)
live_api.show_data_info()

us_flights = live_api.get_flights_by_country("United States")
print(f"Hittade {len(us_flights)} flyg i USA.")
```

---
*Kurs: Utveckling med Python, grund (40 YH-poäng) – Examinationsuppgift*
