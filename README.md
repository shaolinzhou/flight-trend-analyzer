# Flight Trend & Optimization Analyzer
*Stage 13: Självständig Reflektion och GitHub-arkiv*

---

## 📌 1. Projektöversikt
I Stage 13 färdigställs kursens reflekterande och utvärderande delar (Mål 8) samt registrering av projektets officiella GitHub-länk (Mål 4).

---

## 💡 2. Mål 8: Självständig Reflektion och Lärdomar

### Vad gick bra?
- **Objektorienterad arkitektur**: Uppdelningen mellan `FlightDataAnalyzer` (basklass) och `LiveFlightAPI` (barnklass) skapade en tydlig ansvarsfördelning (Separation of Concerns). Basklassen fokuserar på databehandling medan barnklassen hanterar externa nätverksanrop.
- **Stegvis versionshantering**: Genom att genomföra 14 distinkta commits kunde varje enskild komponent testas isolerat, vilket minimerade risken för regressionsfel.
- **Persistens**: Exporten till CSV fungerar stabilt och producerar ren, strukturerad data.

### Vad misslyckades och vilka lärdomar drogs? (Kritisk analys av bakslag)
- **Tidigt misslyckande: Otillräcklig analys av lärarens kravspecifikation**:
  - *Vad som hände*: Projektets mest kännbara motgång inträffade i inledningsfasen (Stage 01–Stage 02). Jag påbörjade utvecklingen utifrån en statisk Kaggle-fil med historiska flygbiljettpriser (`Data_Train.csv`) utan att tillräckligt ingående ha brutit ner och analyserat lärarens examinationsbeskrivning och betygskriterier. När jag i slutet av Stage 02 gjorde en fördjupad genomgång insåg jag att ett statiskt dataset inte uppfyllde Mål 7 (inhämtning av externa API-data) eller gav den tekniska höjd mot AI-branschen (Mål 1) som krävdes för betyget VG.
  - *Konsekvens*: Arbetet som lagts på biljettprisstrukturen fick skrotas, och källkoden behövde i Stage 03 helt refaktoreras för att ansluta mot OpenSky Network REST API.
  - *Ingenjörsmässig lärdom*: Denna erfarenhet gav en mycket nyttig lektion i professionellt mjukvaruarbete: **Requirements Engineering (kravanalys)** och intressentavstämning är helt avgörande innan utvecklingen inleds. Att bygga "rätt sak" är viktigare än att börja koda snabbt. Lärdomen är att alltid definiera acceptanskriterier och validera kraven med beställaren/läraren tidigt i processen för att undvika onödigt dubbelarbete (*re-work*).
- **API Rate Limiting & Nätverksinstabilitet**: OpenSky Network API har restriktioner för anonyma anrop och kan svara långsamt eller kasta HTTP 429. Detta krävde noggrann implementering av timeouts, defensiva `try/except`-block samt en lokal fallback-mekanism till sparad CSV-data vid nätverksavbrott.
- **Windows Konsol Teckenkodning**: Tecken som å, ä och ö orsakade initialt teckenkodningsfel i Windows GBK-miljö vid kommandoradskörning. Lösningen var att använda UTF-8 rakt igenom samt säkerställa explicit kodning vid filhantering.

### Vad skulle jag göra annorlunda nästa gång?
- **Grundlig kravspecifikation före utvecklingsstart**: Upprätta en formell matris över samtliga kursmål och verifiera datakällornas lämplighet innan den första kodraden skrivs.
- **Lokal Caching**: Implementera ett SQLite- eller JSON-cachelager för att spara API-svar lokalt och spara på nätverksresurser under utveckling.
- **Asynkrona anrop**: Använda `aiohttp` och `asyncio` för att hämta telemetri parallellt över flera luftrumsområden.

---

## 🤖 3. Användning av AI-verktyg och GDPR (Del 12)
Enligt kursens anvisningar i **Del 12 (Regler kring AI-verktyg)** redovisas följande användning:
- **Verktyg**: Stora språkmodeller (ChatGPT / Copilot) har använts som stöd för idébollning, felsökning och dokumentationsstruktur.
- **Konkret insats vid API-integration**: Vid undersökningen av flygdata och integrationen av OpenSky Network REST API (`https://opensky-network.org/api/states/all`) uppstod utmaningar med att tolka de råa tillståndsvektorerna (arrayer utan nyckelnamn). Genom att konsultera AI kunde datastrukturen och indexeringen (ICAO24, callsign, land, longitud, latitud, höjd, hastighet) snabbt analyseras och felsökas. AI-stödet möjliggjorde en snabb och korrekt värdeutläsning och mappning till Pandas, vilket drastiskt förkortade tiden för att få gränssnittet i full och stabil drift.
- **GDPR-efterlevnad**: Inga personuppgifter (PII) har överförts till online-verktyg. Projektet hanterar uteslutande öppen, anonym flygtelemetri från OpenSky Network.
- **Egen förståelse**: All inlämnad kod har granskats, anpassats och förståtts i sin helhet av studenten och kan förklaras muntligt.

---

## 🔗 4. GitHub-arkiv (Mål 4)
Projektets källkod och kompletta commit-historik finns på GitHub:
👉 **[https://github.com/shaolinzhou/flight-trend-analyzer](https://github.com/shaolinzhou/flight-trend-analyzer)**

---

## 🛠️ 5. Pågående arbete (Aktuella uppgifter för Stage 13)
- **Fokus**: Dokumentation av Mål 8 (reflektion), GitHub-länk och slutgranskning.
- **Git Commit**: `docs: add reflection and project summary`
- **Testmetod**: `live_api.show_reflection()`

---
*Kurs: Utveckling med Python, grund (40 YH-poäng) – Examinationsuppgift*
