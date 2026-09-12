# Flight Trend & Optimization Analyzer
*Stage 05: Landfördelningsanalys och Filtrering*

---

## 📌 1. Projektöversikt
Med validerad data i systemet påbörjas analysen av luftrumsfördelningen. Vilka nationer har flest plan i luften vid mättillfället?

---

## 📈 2. Analysfokus: Global flygaktivitet per land (Mål 2, 6)
- **Frekvensberäkning**: Använder pandas `.value_counts()` på kolumnen `country` för att identifiera de mest trafikerade länderna.
- **Flygbolagsanalys**: Introducerar metoden `get_top_airlines(top_n=10)` som grupperar giltiga anropssignaler (`callsign`) för att kartlägga dominerande aktörer.
- **Insikter**: Ger en överblick över globala trafikmönster, där länder som USA, Frankrike, Kina och Tyskland ofta toppar listan beroende på tid på dygnet.

---

## 🛠️ 3. Pågående arbete (Aktuella uppgifter för Stage 05)
- **Fokus**: Aggregering av landfördelning och flygbolagstopplista.
- **Git Commit**: `feat: analys av landfördelning och filtrering`
- **Testmetod**: `live_api.show_country_stats()`

---

## 📊 4. Kom igång
```python
from src.flight_logic import LiveFlightAPI

live_api = LiveFlightAPI()
live_api.fetch_live_flights(limit=200)

top_countries = live_api.df["country"].value_counts().head(5)
print("Topp 5 länder:")
print(top_countries)
```

---
*Kurs: Utveckling med Python, grund (40 YH-poäng) – Examinationsuppgift*
