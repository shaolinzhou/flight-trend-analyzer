# Flight Trend & Optimization Analyzer
*Stage 06: Hastighets- och Höjdsanalys*

---

## 📌 1. Projektöversikt
I detta stadium fördjupar vi analysen till telemetriska fysikvärden: marschhastighet och flygnivåer (höjd). Detta ger en djupare förståelse för hur trafiken fördelar sig i höjdled och fart.

---

## ✈️ 2. Fysikalisk telemetrianalys (Mål 6, 7)
- **Hastighet (`velocity`)**: Mäts i meter per sekund (m/s). Typisk marschfart för kommersiella jetplan ligger kring 200–250 m/s (~720–900 km/h).
- **Höjd (`altitude`)**: Barometrisk höjd i meter. Kommersiell trafik opererar vanligen över 9 000–12 000 meter.
- **Aggregering med groupby**:
  ```python
  vel_stats = valid_flights.groupby("country").agg(
      flight_count=("icao24", "count"),
      avg_velocity=("velocity", "mean"),
      avg_altitude=("altitude", "mean"),
      max_velocity=("velocity", "max")
  )
  ```

---

## 🛠️ 3. Pågående arbete (Aktuella uppgifter för Stage 06)
- **Fokus**: Gruppering och statistikberäkning för höjd och hastighet.
- **Git Commit**: `feat: hastighets- och höjdsanalys`
- **Testmetod**: `live_api.show_velocity_stats()`

---

## 📊 4. Kom igång
```python
from src.flight_logic import LiveFlightAPI

live_api = LiveFlightAPI()
live_api.fetch_live_flights(limit=200)
live_api.show_velocity_stats()
```

---
*Kurs: Utveckling med Python, grund (40 YH-poäng) – Examinationsuppgift*
