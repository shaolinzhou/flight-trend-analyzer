# Flight Trend & Optimization Analyzer
*Stage 08: Flygbolagsräkning med For-Loop och Dictionaries*

---

## 📌 1. Projektöversikt
I detta stadium demonstrerar vi algoritmisk databearbetning i Python genom att räkna och sortera flygningar per anropssignal (callsign/flygbolag) med hjälp av en `dict` och en iterativ loop.

---

## 📊 2. Algoritmisk logik: Dictionaries & Sortering (Mål 2, 6)
- **Ackumuleringsmönster**:
  1. Gruppera DataFrame per `callsign`.
  2. Iterera genom grupperna med en `for`-loop.
  3. Bygg en uppslagsbok (`dict`) som mappar flygbolagskod till antal aktiva flyg.
  4. Sortera ordlistan fallande med `sorted()` och lambda-uttryck:
     ```python
     sorted_airlines = dict(sorted(airline_counts.items(), key=lambda x: x[1], reverse=True))
     ```
- Detta belyser hur standardstrukturer i Python samverkar med externa analysbibliotek.

---

## 🛠️ 3. Pågående arbete (Aktuella uppgifter för Stage 08)
- **Fokus**: For-loop baserad uppräkning och sortering av flygbolagstrafik.
- **Git Commit**: `feat: räkna flyg per callsign med for-loop`
- **Testmetod**: `live_api.show_callsign_stats()`

---

## 📊 4. Kom igång
```python
from src.flight_logic import LiveFlightAPI

live_api = LiveFlightAPI()
live_api.fetch_live_flights(limit=200)
live_api.show_callsign_stats()
```

---
*Kurs: Utveckling med Python, grund (40 YH-poäng) – Examinationsuppgift*
