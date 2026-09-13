# Flight Trend & Optimization Analyzer
*Stage 07: Explicit For-Loop Summering per Land*

---

## 📌 1. Projektöversikt
Kursens mål 2 och 6 kräver förståelse för grundläggande styrsatser och loopar i Python. I Stage 07 kompletterar vi pandas vektoriserade operationer med explicita `for`-loopar för att skapa formaterade terminalrapporter.

---

## 🔄 2. Programmeringsparadigm: Vektorisering vs Explicita Loopar (Mål 2)
- **Varför både och?** Medan pandas är överlägset för snabb databehandling i minnet, ger explicita loopar full kontroll över detaljerad strängformatering, anpassade utskrifter och logik för varje enskild entitet.
- **Implementation**:
  ```python
  for country, count in country_counts.items():
      subset = live_api.df[live_api.df["country"] == country]
      avg_v = subset["velocity"].mean()
      print(f"Land: {country} | Antal: {count} | Snittfart: {avg_v:.1f} m/s")
  ```

---

## 🛠️ 3. Pågående arbete (Aktuella uppgifter för Stage 07)
- **Fokus**: Konstruktion av loop-baserad summeringsrapport för toppländer.
- **Git Commit**: `feat: for-loop sammanfattning per land`
- **Testmetod**: `live_api.show_for_loop_demo()`

---

## 📊 4. Kom igång
```python
from src.flight_logic import LiveFlightAPI

live_api = LiveFlightAPI()
live_api.fetch_live_flights(limit=150)
live_api.show_for_loop_demo()
```

---
*Kurs: Utveckling med Python, grund (40 YH-poäng) – Examinationsuppgift*
