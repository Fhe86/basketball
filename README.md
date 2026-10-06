# Basketball Klasse 6 (Sequenz-Homepage)

Stand: 06.10.2026, lokal fertig, noch nicht veröffentlicht, noch nicht im Unterricht getestet.

Vier Doppelstunden (je 90 Min, 12 Schüler) vom Parteiball zum 3 gegen 3, dazu Übungspool und drei Noten (Dribbeln 10 P, Werfen 10 P, Spiel 12 P, Notenrechner, Bewertungsbogen). Lehrplanbezug: LehrplanPLUS Mittelschule Sport Jgst. 6, 4.3 Spielen sowie Lernbereich 1 und 2.

## Dateien

| Datei | Zweck |
|---|---|
| `index.html` | Startseite: Weg in 4 Stufen, Stundenliste, filterbarer Übungspool, Bewertung, Material |
| `stunde-1.html` bis `stunde-4.html` | Stundenverläufe mit Zeitleiste, Material, Sicherheit, Druckansicht |
| `bewertung.html` | Notenrechner, Punkte-Richtwerte, Bewertungsbogen zum Ausdrucken |
| `style.css`, `app.js`, `fonts/` | Gestaltung, Filter und Rechner, Schrift Geist (lokal eingebettet) |
| `quellen/build.py` | Baut alle Seiten neu. Inhalte (Stunden, Übungen, Punkte) stehen oben im Skript |

Änderungen an Inhalten: in `quellen/build.py` ändern, dann `python3 quellen/build.py` ausführen.

## Design

Vorlage als Look: 21st.dev "Forma Pilates Studio" (Kursplan, Karten, Filter), nur nachgebaut, nichts heruntergeladen. Hell, ein Akzent (gebranntes Orange), Schrift Geist, Dark Mode über die Systemeinstellung.

## Offene Punkte

- Veröffentlichung als Mini-Repo `Fhe86/basketball`, GitHub Pages (wartet auf Fabis Freigabe der Optik).
- Punkte-Richtwerte (Slalom-Zeiten, Passzahlen) nach dem ersten Durchlauf mit der Klasse anpassen.
- Bälle im Keller: nur sinnvoll, wenn dort Basketbälle liegen.
- Keine Fotos oder Illustrationen: Bildgenerierung wäre kostenpflichtig und nicht freigegeben.
