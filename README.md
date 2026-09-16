# Flight Trend & Optimization Analyzer
*Stage 11: Robust Felhantering med try-except*

---

## 📌 1. Projektöversikt
För att nå VG-nivå (Väl godkänd) i Mål 6 och 8 krävs att applikationen uppvisar defensiv programmering och hanterar nätverks- och datafel på ett strukturerat sätt.

---

## 🛡️ 2. Felhanteringsarkitektur (Mål 6: Robust programutveckling)
Vi bygger in specifika `try...except`-block över alla kritiska punkter:
1. **Nätverksfel**:
   - `requests.exceptions.ConnectionError`: Fångar internetavbrott och ger användarvänligt meddelande.
   - `requests.exceptions.Timeout`: Förhindrar att programmet hänger sig vid långsamma API-svar.
   - `requests.exceptions.HTTPError`: Reagerar på HTTP 429 (rate limits) och 5xx serverfel.
2. **Dataparsningsfel**:
   - `KeyError` och `IndexError`: Hanterar eventuella formatändringar i API-svaret.
3. **Filskrivningsfel**:
   - `IOError`: Varnar om målfilen är låst eller saknar skrivbehörighet.

---

## 🛠️ 3. Pågående arbete (Aktuella uppgifter för Stage 11)
- **Fokus**: Ersätta generiska exceptions med specifika felklasser och bygga testfall för tom/ogiltig data.
- **Git Commit**: `feat: förbättra felhantering med try-except`
- **Testmetod**: `live_api.test_error_handling()`

---

## 📊 4. Kom igång
```python
from src.flight_logic import LiveFlightAPI

live_api = LiveFlightAPI()
# Testa felhanteringen vid simulering av felaktiga indata
live_api.test_error_handling()
```

---
*Kurs: Utveckling med Python, grund (40 YH-poäng) – Examinationsuppgift*
