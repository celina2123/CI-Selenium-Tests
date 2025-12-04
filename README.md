# CI-Selenium-Tests – Inlämningsuppgift

Detta projekt är en del av kursen **CI och testautomatisering**.  
Uppgiften handlar om att sätta upp automatiska tester med **pytest** och köra dem i **GitHub Actions**.

---

## 🧪 Tester

Testerna finns i mappen:


Testerna använder **unittest.mock** för att låtsas göra ett API-anrop utan att kontakta internet.  
Det gör att testet alltid fungerar (även i GitHub Actions).

---

## ⚙️ GitHub Actions (CI)

Workflow-filen finns i:


Den gör följande:

1. Installerar Python.
2. Installerar beroenden från `requirements.txt`.
3. Kör alla tester automatiskt med:


När testerna godkänns får jobbet **Success** 👍  
Annars blir det **Failed** och man kan se varför.

---

## 📦 Beroenden

Projektet använder:


---

## ✔️ Sammanfattning

- Tester körs automatiskt i GitHub Actions.
- Testet använder mockning för att undvika riktiga API-anrop.
- Workflowen fungerar och ger **grönt (Success)**.

Detta uppfyller kursens krav för inlämningen.
