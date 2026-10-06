#!/usr/bin/env python3
"""Baut alle Seiten der Basketball-Sequenz (Klasse 6) neu.

Aufruf:  python3 quellen/build.py
Inhalte (Stunden, Uebungen, Bewertung) stehen unten als Daten. Aussehen steht in
style.css, Verhalten in app.js. Beides liegt neben den fertigen HTML-Seiten.
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "Basketball 6"

# ---------------------------------------------------------------- Inhalte

STUFEN = {
    "ball": "Ball kennenlernen",
    "pass": "Fangen und Passen",
    "dribbel": "Dribbeln und Stoppen",
    "wurf": "Werfen",
    "spiel": "Spielen",
}

LESSONS = [
    {
        "n": 1,
        "title": "Ball kennenlernen, fangen, passen",
        "short": "Ball kennenlernen",
        "goal": "Die Jungs gewöhnen sich an den Ball und spielen ihr erstes Parteiball mit sauberen Pässen.",
        "spiel": "Parteiball",
        "halle": "oben oder unten",
        "lehrplan": "Lehrplan 4.3 Spielen (Fangen, Passen), Lernbereich 1 (Aufwärmen), Lernbereich 2 (Regeln, Fairness)",
        "material": ["1 Ball pro Schüler (Größe 6 oder 7, je nachdem, was vorhanden ist)", "Leibchen in zwei Farben", "Hütchen zum Abgrenzen", "Pfeife, Stoppuhr"],
        "safety": ["Bälle nur auf Ansage werfen, nie in Richtung der Wand, wo andere stehen.", "Bei Parteiball: kein Festhalten, kein Wegreißen des Balls."],
        "steps": [
            ("0 bis 10", "Ball-Fangen",
             ["Zwei Fänger mit Ball. Sie **tippen** ab, indem sie den Ball in der Hand halten und den Mitspieler berühren. Kein Werfen.",
              "Wer getippt wird, macht an der **Ballstation** fünfmal den Ball um die Hüfte und ist wieder frei.",
              "Läuft ohne Pause, macht warm und bringt den Ball in die Hand."], None),
            ("10 bis 25", "Ballkünstler",
             ["Jeder hat einen Ball. Aufgaben zum Nachmachen: Ball um die Hüfte, **Achter** durch die Beine, hochwerfen, klatschen, fangen.",
              "Dann erfinden die Jungs eigene Tricks. Die Klasse macht gelungene Tricks nach. Du wählst den besten der Stunde.",
              "Wichtig: Der Ball bleibt in den **Fingerkuppen**, nicht in der flachen Hand."], None),
            ("25 bis 45", "Fangen und Passen mit Partner",
             ["Brustpass über 3 bis 4 m. Merkhilfe: **Schritt zum Partner, Ellbogen nah am Körper, Arme strecken, Daumen zeigen am Ende nach unten.**",
              "Fangen: Hände als **Fenster** dem Ball entgegen, Finger gespreizt, Ball an die Brust ziehen und abfedern.",
              "Danach der **Aufsetzerpass** (Ball springt einmal in der Mitte auf). Zum Schluss Wettbewerb: Wie viele saubere Pässe schafft das Paar in 30 Sekunden?"],
             "Tipp: Ein Paar zeigt den Pass vor, die anderen sagen, was gut war. So lernen die Jungs, auf die Technik zu achten."),
            ("45 bis 70", "Parteiball",
             ["Zwei Teams, 4 gegen 2 im ersten Durchgang (Überzahl), danach 3 gegen 3. **Nicht mit dem Ball laufen**, nur passen.",
              "**6 Pässe in Folge** ergeben einen Punkt. Der Ball wechselt bei Abfangen, Fehlpass oder Festhalten.",
              "Überzahlteam wechselt alle 3 Minuten. Alle sollen einmal in Unterzahl spielen."],
             "Regel auf Wunsch anpassen: Die Jungs dürfen sich selbst eine Regel ausdenken, wenn die Klasse sie fair findet (Lernbereich 2)."),
            ("70 bis 85", "Hütchenball",
             ["Zwei Teams, jedes verteidigt ein Hütchen auf einem Kasten. Der Ball wird nach vorn gepasst, aus **2 bis 3 m** wird das Hütchen abgeworfen.",
              "Nicht laufen mit dem Ball, nur passen. Verteidiger dürfen nur mit den Händen abfangen, nicht festhalten.",
              "Das bereitet das Zielen auf den Korb vor."], None),
            ("85 bis 90", "Abschluss",
             ["Handgelenke und Schultern kreisen, kurz dehnen.",
              "Rückblick: Was war schwer, was ging gut? Jeder nennt einen Pass, der ihm gelungen ist."], None),
        ],
    },
    {
        "n": 2,
        "title": "Dribbeln, stoppen, freilaufen",
        "short": "Dribbeln und Stoppen",
        "goal": "Die Jungs führen den Ball sicher mit beiden Händen und stoppen mit festem Standbein.",
        "spiel": "10-Pässe-Spiel",
        "halle": "oben oder unten",
        "lehrplan": "Lehrplan 4.3 Spielen (Dribbeln, Stopp- und Sternschritt, Freilaufen), Lernbereich 1 (Kondition)",
        "material": ["1 Ball pro Schüler", "10 bis 15 Hütchen für Slalom und Felder", "Leibchen in zwei Farben", "Pfeife"],
        "safety": ["Beim Dribbel-Fangen genug Platz, Zusammenstöße vermeiden: Kopf hoch.", "Beim Stoppen auf rutschfeste Schuhe achten, kein Stoppen auf Socken."],
        "steps": [
            ("0 bis 10", "Dribbel-Fangen",
             ["Alle dribbeln in einem begrenzten Feld und versuchen, den Ball der anderen **wegzuschlagen**, während sie ihren eigenen schützen.",
              "Wer seinen Ball verliert, holt ihn zurück und spielt weiter. Kein Ausscheiden.",
              "Macht warm und zeigt dir, wer schon sicher dribbelt."], None),
            ("10 bis 30", "Dribbelschule",
             ["**Technik:** Fingerkuppen, Ball auf Hüfthöhe, der Ball springt vor dem Körper, der Blick geht nach oben.",
              "Stehend, gehend, laufend. Beide Hände. Richtungswechsel mit einem Hütchen als Gegner.",
              "**Schattendribbeln:** Ein Partner läuft vor, der andere dribbelt hinterher und macht jede Richtung mit. Nach 30 Sekunden Wechsel.",
              "**Dribbel-Ampel:** Rot = stehen und Ball halten, Gelb = langsam, Grün = schnell."],
             "Die schwache Hand wird in dieser Stunde gezielt trainiert, damit der Parcours am Ende fair ist."),
            ("30 bis 45", "Stoppen mit Standbein",
             ["Stopp: Beim Pfiff **sofort** stehen bleiben, Ball mit beiden Händen fassen. Der Fuß, der zuerst aufkommt, bleibt wie festgeklebt (**Standbein**).",
              "Das andere Bein darf **kreisen**, wie ein Zirkel um das Standbein. So entsteht der Sternschritt, ohne dass das Standbein wandert.",
              "Spiel: **Standbein-Statue.** Bei Pfiff halten alle an, wer das Standbein bewegt, macht fünf Ball-Kreise."],
             "Wenn es nicht klappt, einen Schritt zurück: erst im Stand üben, dann im Gehen, dann im Laufen."),
            ("45 bis 65", "Freilaufen und Anbieten",
             ["Dreiergruppen im Dreieck. Nach dem Pass sofort **weiterlaufen** und die Hand als Ziel zeigen (**Anbieten**).",
              "Danach 4 gegen 2: Dribbeln ist jetzt erlaubt, aber nicht mehr als drei Dribblings in Folge. Das Ziel bleibt: Pässe spielen, sich freilaufen."], None),
            ("65 bis 82", "10-Pässe-Spiel",
             ["4 gegen 4 auf einem Feld ohne Korb. Dribbeln und Stoppen erlaubt, **Schrittregel** gilt: nach dem Stoppen nur noch passen oder mit dem Standbein drehen.",
              "Ein Team gewinnt einen Punkt mit 10 Pässen in Folge. Wer abgefangen hat, bekommt den Ball."], None),
            ("82 bis 90", "Dribbel-Pass-Staffel zum Abschluss",
             ["Teams zu 4. Slalom dribbeln, dann einen Pass zum nächsten Läufer. Die Staffel ist locker und lässt die Herzfrequenz runtergehen.",
              "Kurz dehnen, Rückblick."], None),
        ],
    },
    {
        "n": 3,
        "title": "Auf den Korb werfen",
        "short": "Werfen auf den Korb",
        "goal": "Die Jungs lernen den einhändigen Korbwurf und verbinden Pass, Dribbeln und Wurf im 3 gegen 3.",
        "spiel": "3 gegen 3 auf einen Korb",
        "halle": "oben (Körbe nötig)",
        "lehrplan": "Lehrplan 4.3 Spielen (Korbwurf), Lernbereich 2 (Schiedsrichter, Fairness)",
        "material": ["1 Ball pro Schüler, mindestens ein Ball pro zwei Schüler", "Mindestens 2 Körbe, besser 4", "Hütchen als Wurfmarkierungen", "Leibchen, Pfeife"],
        "safety": ["Bei Würfen auf denselben Korb: Rückholer stellen sich seitlich, nicht darunter.", "Beim 3 gegen 3 kein Schubsen unter dem Korb, Foul wird gepfiffen."],
        "steps": [
            ("0 bis 10", "Warm-up mit Ball",
             ["Schattendribbeln mit Partner, nach 30 Sekunden Wechsel.",
              "Danach 2 Minuten freies Dribbeln mit Richtungswechsel, dann Wurf in den Korb für jeden, einfach zum Eingewöhnen."], None),
            ("10 bis 30", "Wurftechnik",
             ["**Wurfhand** unter den Ball, die andere Hand seitlich zur Stütze. **Ellbogen** unter den Ball, Blick zum Korb.",
              "Schwung kommt aus den Beinen, am Ende **nachklappen**: Das Handgelenk fällt nach vorne, als würde die Hand in eine Keksdose greifen.",
              "**Treppe:** Start aus der Hocke 1 m vor dem Korb, dann stehend, dann 2 m, dann 3 m. Wer trifft, geht eine Stufe weiter.",
              "Partner schauen auf die Technik und rufen zurück, was sie sehen."], None),
            ("30 bis 45", "Stoppen und Werfen",
             ["Aus dem Dribbeln stoppen und sofort werfen. Zwei Linien, drei Würfe aus verschiedenen Entfernungen.",
              "**Plus-Aufgabe** für sichere Jungs: der Korbleger im Dreierrhythmus (rechts, links, hoch) mit Anlauf von der Seite."],
             "Der Korbleger ist freiwillig. Verlangt wird er in der Bewertung nicht."),
            ("45 bis 60", "Basketball-Golf",
             ["Sechs Markierungen rund um den Korb. Jeder braucht so wenige Würfe wie möglich, um zu treffen. Wer trifft, geht zur nächsten Station.",
              "Kleine Gruppen zu zwei bis drei an einem Korb, damit alle viel werfen."], None),
            ("60 bis 85", "3 gegen 3 auf einen Korb",
             ["Vier Teams, zwei Felder, fünf Minuten pro Spiel. Rotation, bis jedes Team gegen jedes gespielt hat.",
              "**Regel:** Vor dem Wurf müssen mindestens zwei verschiedene Spieler den Ball berührt haben. So wird nicht allein gespielt.",
              "Nach einem Korb wechselt der Ball. Das Team ohne Spiel stellt den Schiedsrichter (Lernbereich 2)."],
             "Du beobachtest schon die Spielfähigkeit, die in der letzten Stunde bewertet wird."),
            ("85 bis 90", "Abschluss",
             ["Auslaufen, Schultern lockern.",
              "Ankündigung: In der nächsten Stunde gibt es den Technikparcours und das 3-gegen-3-Turnier, beides bewertet."], None),
        ],
    },
    {
        "n": 4,
        "title": "Dribbeln, Werfen und Turnier",
        "short": "Bewertung und Turnier",
        "goal": "Die Jungs zeigen Dribbeln, Werfen und Spielen. Du vergibst drei Noten.",
        "spiel": "3-gegen-3-Turnier",
        "halle": "oben",
        "lehrplan": "Lehrplan 4.3 Spielen, Lernbereich 2 (Fairness, Schiedsrichter)",
        "material": ["Bewertungsbogen (Seite Bewertung, ausdrucken)", "Stoppuhr", "Hütchen für den Dribbelparcours", "Klemmbrett, Pfeife, Leibchen"],
        "safety": ["Beim Turnier nicht zu hart spielen lassen, Fouls konsequent pfeifen.", "Jeder Schüler, der gerade nicht dran ist, passt auf und zählt für einen Mitschüler."],
        "steps": [
            ("0 bis 10", "Aufwärmen mit Ball",
             ["Dribbel-Fangen als Einstieg, dann ein Durchgang Passen im Dreieck.",
              "Kurze Ansage: Heute gibt es drei Noten, Dribbeln, Werfen und Spiel. Wer nicht an der Reihe ist, zählt für seinen Partner."], None),
            ("10 bis 45", "Dribbel- und Wurftest (zwei Noten)",
             ["**Station A, Dribbelparcours** (du wertest): 5 Hütchen im Slalom hin mit der starken Hand, zurück mit der schwachen. Zeit (6 Punkte) und Technik (4 Punkte) zählen.",
              "**Station B, Korbwurf** (Partner zählt): 6 Würfe aus der Nähe, 4 Würfe aus mittlerer Entfernung, ein Punkt pro Treffer.",
              "Wer nicht an Station A oder B dran ist, übt freies Passen an der Wand oder Basketball-Golf. Das zählt nicht.",
              "Zeitbedarf Station A: ca. 1,5 Minuten pro Schüler, also etwa 18 Minuten für alle."],
             "Eintragen sofort nach jedem Versuch, sonst vergisst du die Werte."),
            ("45 bis 80", "3-gegen-3-Turnier (Spielnote)",
             ["Vier Teams, zwei Felder, ca. 6 Minuten pro Spiel. Jedes Team spielt gegen jedes.",
              "Du beobachtest vier Kriterien (jeweils 0 bis 3 Punkte): **Freilaufen und Anbieten**, **Passen und Dribbeln**, **Regeln und Fairness**, **Einsatz und Entscheidungen**.",
              "Das Team ohne Spiel pfeift (Schiedsrichter) und notiert den Spielstand."],
             "Bei der Beobachtung: lieber jede Runde zwei Spieler gezielt anschauen, als alle halb zu sehen."),
            ("80 bis 90", "Abschluss und Rückmeldung",
             ["Kurze Siegerehrung fürs Turnier, jeder bekommt einen persönlichen Satz zu seinem besten Teil.",
              "Ergebnisse mit dem **Notenrechner** auf der Seite Bewertung in drei Noten umrechnen."], None),
        ],
    },
]

POOL = [
    ("Ball-Fangen", "ball", "8 Min", "beide",
     "Zwei Fänger tippen mit dem Ball in der Hand ab. Wer getippt wird, macht an der Ballstation 5 Hüftkreise und ist wieder frei."),
    ("Ballkünstler", "ball", "10 Min", "beide",
     "Jeder zeigt einen Balltrick, die Klasse macht ihn nach. Hüftkreise, Achter durch die Beine, hochwerfen und klatschen."),
    ("Partnerpass-Schule", "pass", "12 Min", "beide",
     "Brustpass und Aufsetzerpass über 3 bis 4 m. Schritt zum Partner, Daumen am Ende nach unten. Fangen mit den Händen als Fenster."),
    ("Dreieckspass", "pass", "10 Min", "beide",
     "Dreiergruppen. Nach dem Pass sofort weiterlaufen und die Hand als Ziel zeigen. Trainiert Freilaufen und Anbieten."),
    ("Parteiball", "pass spiel", "12 Min", "beide",
     "4 gegen 2 oder 3 gegen 3, kein Korb. Nicht mit dem Ball laufen. 6 Pässe in Folge ergeben einen Punkt."),
    ("10-Pässe-Spiel", "pass spiel", "12 Min", "beide",
     "4 gegen 4, Dribbeln und Stoppen erlaubt. Ein Punkt für zehn Pässe in Folge. Wer abfängt, behält den Ball."),
    ("Dribbel-Fangen", "dribbel", "8 Min", "beide",
     "Alle dribbeln in einem Feld und schlagen den Ball der anderen weg. Wer den Ball verliert, holt ihn und spielt weiter."),
    ("Schattendribbeln", "dribbel", "8 Min", "beide",
     "Ein Partner läuft vor, der Schatten dribbelt hinterher und macht jeden Richtungswechsel mit. Nach 30 Sekunden Wechsel."),
    ("Dribbel-Ampel", "dribbel", "6 Min", "beide",
     "Rot: stehen und Ball halten. Gelb: langsam dribbeln. Grün: schnell. Bei Pfiff Stopp mit Standbein."),
    ("Standbein-Statue", "dribbel", "8 Min", "beide",
     "Bei Pfiff stoppen, der erste Fuß bleibt wie festgeklebt. Das andere Bein darf kreisen. Wer das Standbein bewegt, macht 5 Ballkreise."),
    ("Dribbel-Pass-Staffel", "dribbel pass", "10 Min", "beide",
     "Teams zu 4. Slalom dribbeln, am Ende Pass zum nächsten Läufer. Locker, gut als Abschluss."),
    ("Hütchenball", "wurf spiel", "12 Min", "beide",
     "Zwei Teams verteidigen je ein Hütchen auf einem Kasten. Ball nach vorn passen, aus 2 bis 3 m das Hütchen abwerfen."),
    ("Korbwurf-Treppe", "wurf", "12 Min", "oben",
     "Wurfhand unter dem Ball, Ellbogen darunter, Hand nachklappen. Aus der Hocke starten, dann stehend, dann jede Stufe weiter weg."),
    ("Basketball-Golf", "wurf", "12 Min", "oben",
     "Sechs Markierungen rund um den Korb. Wer mit den wenigsten Würfen trifft, gewinnt die Bahn."),
    ("3 gegen 3 auf einen Korb", "spiel wurf", "15 Min", "oben",
     "Vor dem Wurf müssen mindestens zwei Spieler den Ball berührt haben. Nach jedem Korb wechselt der Ball."),
]

# Bewertung: Punkte, Richtwerte
TEILE = [
    ("dribbeln", "Dribbeln", 10, "Zeit im Slalom (0 bis 6 Punkte) und Technik (0 bis 4 Punkte): Blick hoch, Fingerkuppen, schwache Hand, Ballkontrolle."),
    ("werfen", "Werfen", 10, "6 Würfe aus der Nähe und 4 aus mittlerer Entfernung, je 1 Punkt pro Treffer."),
    ("spiel", "Spiel", 12, "Vier Kriterien im 3-gegen-3-Turnier, je 0 bis 3 Punkte. Das Passen fließt hier ein."),
]
DRIBBEL_ZEIT = [("bis 17 s", "6 Punkte"), ("bis 19 s", "5 Punkte"), ("bis 21 s", "4 Punkte"), ("bis 24 s", "3 Punkte"), ("bis 27 s", "2 Punkte"), ("langsamer, aber fertig", "1 Punkt")]
DRIBBEL_TECHNIK = [
    ("Blick oben", "1 Punkt, wenn der Blick überwiegend hochgeht"),
    ("Fingerkuppen", "1 Punkt, wenn der Ball nicht flach in der Hand liegt"),
    ("Schwache Hand", "1 Punkt, wenn der Rückweg sicher gelingt"),
    ("Ballkontrolle", "1 Punkt, wenn der Ball nie wegspringt"),
]
SPIEL_KRITERIEN = [
    ("Freilaufen und Anbieten", "3 = fast immer anspielbar, 0 = bleibt stehen"),
    ("Passen und Dribbeln", "3 = sicher und sinnvoll, 0 = verliert den Ball oft"),
    ("Regeln und Fairness", "3 = hält Regeln ein und akzeptiert Entscheidungen"),
    ("Einsatz und Entscheidungen", "3 = engagiert, spielt zum freien Mitspieler"),
]


def schluessel(maximum):
    """Mindestpunkte fuer Note 1 bis 5 nach Fabis Standard (90/80/60/40/20 Prozent)."""
    import math
    return [math.ceil(round(p * maximum, 6)) for p in (0.9, 0.8, 0.6, 0.4, 0.2)]


# ---------------------------------------------------------------- Helfer

def esc(text):
    return html.escape(text, quote=True)


def rich(text):
    """Escaped Text, **fett** wird zu <b>."""
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", esc(text))


def head(title, desc):
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="stylesheet" href="style.css">
</head>
<body>
"""


def nav(current):
    items = [("stunde-%d.html" % l["n"], "Stunde %d" % l["n"], "stunde-%d" % l["n"]) for l in LESSONS]
    items += [("index.html#pool", "Übungspool", "pool"), ("bewertung.html", "Bewertung", "bewertung")]
    links = []
    for href, label, key in items:
        cur = ' aria-current="page"' if key == current else ""
        links.append(f'<li><a class="link" href="{href}"{cur}>{label}</a></li>')
    return f"""<header class="nav"><div class="wrap">
<a class="brand" href="index.html">Basketball <b>6</b></a>
<nav aria-label="Hauptnavigation"><ul>{''.join(links)}</ul></nav>
</div></header>
"""


def foot():
    return """<footer class="foot"><div class="wrap">
<span>Sport, Klasse 6, Mittelschule. Material für den Unterricht.</span>
<span>Lehrplan: LehrplanPLUS Bayern, Sport Jgst. 6</span>
</div></footer>
<script src="app.js"></script>
</body>
</html>
"""


# ---------------------------------------------------------------- Seiten

def page_index():
    stairs = []
    for i, l in enumerate(LESSONS):
        stairs.append(
            f'<a class="step-block" style="--i:{i}" href="stunde-{l["n"]}.html">'
            f'<span class="num">{l["n"]}</span>'
            f'<span><span class="t">{esc(l["short"])}</span><span class="s">{esc(l["spiel"])}</span></span></a>')

    rows = []
    for l in LESSONS:
        rows.append(f"""<a class="lesson-row reveal" href="stunde-{l['n']}.html">
<span class="n">{l['n']}</span>
<span><h3>{esc(l['title'])}</h3><p class="goal">{esc(l['goal'])}</p></span>
<span class="meta"><b>Spiel</b>{esc(l['spiel'])}<b style="margin-top:6px">Halle</b>{esc(l['halle'])}</span>
<span class="arr" aria-hidden="true">&rarr;</span>
</a>""")

    chips = ['<button class="chip" data-filter="alle" aria-pressed="true">Alle</button>']
    for key, label in STUFEN.items():
        chips.append(f'<button class="chip" data-filter="{key}" aria-pressed="false">{esc(label)}</button>')
    chips.append('<button class="chip" data-filter="keller" aria-pressed="false">Auch im Keller</button>')

    cards = []
    for name, stufen, dauer, halle, text in POOL:
        tags = "".join(f'<span class="tag stufe">{esc(STUFEN[s])}</span>' for s in stufen.split())
        halle_tag = "Oben und Keller" if halle == "beide" else "Nur oben"
        cards.append(f"""<article class="card reveal" data-stufe="{stufen}" data-halle="{halle}">
<div class="tags">{tags}</div>
<h3>{esc(name)}</h3>
<p>{esc(text)}</p>
<div class="tags"><span class="tag">{esc(dauer)}</span><span class="tag">{halle_tag}</span></div>
</article>""")

    tile_cls = ["t1", "t2", "t4"]
    tiles = []
    for cls, (key, name, pts, text) in zip(tile_cls, TEILE):
        tiles.append(f'<div class="tile {cls} reveal"><span class="big">{pts}<small>Punkte</small></span><h3>Note {esc(name)}</h3><p>{esc(text)}</p></div>')

    body = head("Basketball Klasse 6, Unterrichtssequenz",
                "Vier Doppelstunden Basketball für die 6. Klasse: Stundenverläufe, Übungspool und Bewertung.") + nav("index")
    body += f"""<main>
<section class="hero"><div class="wrap">
<div>
<h1>Basketball in vier <em>Doppelstunden</em></h1>
<p class="lead">Vom Parteiball zum 3 gegen 3. Alle Stunden, Spiele und die Bewertung für die 6. Klasse an einem Ort.</p>
<div class="actions"><a class="btn btn-primary" href="stunde-1.html">Stunde 1 öffnen</a><a class="btn btn-ghost" href="bewertung.html">Zur Bewertung</a></div>
</div>
<div class="stairs" aria-label="Der Weg in vier Schritten">{''.join(stairs)}</div>
</div></section>

<section class="block" id="stunden"><div class="wrap">
<h2 class="title reveal">Vier Stunden, ein Weg</h2>
<p class="sub reveal">Jede Stunde baut auf der letzten auf. Gespielt wird von Anfang an, die Technik kommt über Spiele dazu.</p>
<div class="lessons">{''.join(rows)}</div>
</div></section>

<section class="block" id="pool"><div class="wrap">
<h2 class="title reveal">Übungspool</h2>
<p class="sub reveal">Alle Übungen und Spiele der Sequenz, filterbar nach Lernschritt. Praktisch, wenn eine Stunde umgebaut werden muss oder der Keller dran ist.</p>
<div class="chips" role="group" aria-label="Nach Lernschritt filtern">{''.join(chips)}</div>
<div class="cards">{''.join(cards)}</div>
<p class="empty" id="pool-empty" hidden>Keine Übungen gefunden. Wähle einen anderen Filter.</p>
</div></section>

<section class="block" id="bewertung"><div class="wrap">
<h2 class="title reveal">Drei Noten für Basketball</h2>
<p class="sub reveal">Dribbeln und Werfen sind je eine Technikprobe, dazu kommt die Spielnote aus dem Turnier. Der Schlüssel folgt deinem Standard: ab 90, 80, 60, 40 und 20 Prozent gibt es die Noten 1 bis 5.</p>
<div class="score-grid">{''.join(tiles)}</div>
<div class="page-actions"><a class="btn btn-primary" href="bewertung.html">Notenrechner und Bogen</a></div>
</div></section>

<section class="block" id="material"><div class="wrap">
<h2 class="title reveal">Material und Lehrplan</h2>
<div class="two">
<div class="reveal"><h3>Das brauchst du</h3><ul class="plain">
<li>Basketbälle, möglichst einer pro Schüler (Größe 6 oder 7)</li>
<li>Mindestens zwei Körbe für Stunde 3 und 4</li>
<li>Hütchen, Leibchen in zwei Farben, Pfeife, Stoppuhr</li>
<li>Ausgedruckter Bewertungsbogen für Stunde 4</li>
</ul></div>
<div class="reveal"><h3>Lehrplanbezug (Sport Jgst. 6)</h3><ul class="plain">
<li>4.3 Spielen: Fangen, Passen, Dribbeln, Stopp- und Sternschritt, Korbwurf</li>
<li>Lernbereich 1: Aufwärmen, Belastung, Verletzungsvorbeugung</li>
<li>Lernbereich 2: Regeln anpassen, Schiedsrichter, Fairness im Spiel</li>
</ul></div>
</div>
</div></section>
</main>
""" + foot()
    return body


def page_lesson(l):
    steps = []
    for zeit, titel, bullets, note in l["steps"]:
        lis = "".join(f"<li>{rich(b)}</li>" for b in bullets)
        note_html = f'<p class="tl-note">{esc(note)}</p>' if note else ""
        steps.append(f"""<div class="tl-step reveal"><div class="tl-time">{esc(zeit)}<span>Minuten</span></div>
<div class="tl-body"><h3>{esc(titel)}</h3><ul>{lis}</ul>{note_html}</div></div>""")

    mat = "".join(f"<li>{esc(m)}</li>" for m in l["material"])
    saf = "".join(f"<li>{esc(s)}</li>" for s in l["safety"])

    prev_l = LESSONS[l["n"] - 2] if l["n"] > 1 else None
    next_l = LESSONS[l["n"]] if l["n"] < len(LESSONS) else None
    pager = ""
    if prev_l:
        pager += f'<a class="prev" href="stunde-{prev_l["n"]}.html"><small>Zurück</small><strong>Stunde {prev_l["n"]}: {esc(prev_l["short"])}</strong></a>'
    if next_l:
        pager += f'<a class="next" href="stunde-{next_l["n"]}.html"><small>Weiter</small><strong>Stunde {next_l["n"]}: {esc(next_l["short"])}</strong></a>'
    else:
        pager += '<a class="next" href="bewertung.html"><small>Weiter</small><strong>Bewertung und Notenrechner</strong></a>'

    body = head(f"Basketball Stunde {l['n']}: {l['title']}", l["goal"]) + nav("stunde-%d" % l["n"])
    body += f"""<main><div class="wrap">
<div class="page-head">
<div class="crumb"><a href="index.html">Basketball Klasse 6</a> &nbsp;/&nbsp; Stunde {l['n']} von {len(LESSONS)}</div>
<h1>{esc(l['title'])}</h1>
<p class="goal">{esc(l['goal'])}</p>
<div class="facts"><span class="tag">90 Minuten</span><span class="tag">12 Schüler</span><span class="tag">Halle: {esc(l['halle'])}</span><span class="tag">Spiel: {esc(l['spiel'])}</span></div>
<div class="page-actions no-print"><button class="btn btn-primary" onclick="window.print()">Als PDF herunterladen</button><a class="btn btn-ghost" href="index.html#pool">Übungspool</a></div>
</div>
<div class="timeline">{''.join(steps)}</div>
<div class="aside-grid">
<div class="panel"><h3>Material</h3><ul class="plain">{mat}</ul></div>
<div class="panel warn"><h3>Sicherheit</h3><ul class="plain">{saf}</ul></div>
</div>
<p class="sub" style="margin-top:20px">{esc(l['lehrplan'])}</p>
<div class="pager">{pager}</div>
</div></main>
""" + foot()
    return body


def page_bewertung():
    dr = "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in DRIBBEL_ZEIT)
    dt = "".join(f"<tr><td>{esc(a)}</td><td>{esc(b)}</td></tr>" for a, b in DRIBBEL_TECHNIK)
    sk = "".join(f"<tr><td>{esc(a)}</td><td>{esc(b)}</td></tr>" for a, b in SPIEL_KRITERIEN)

    ff = "".join(f"""<div class="field"><label for="f-{k}">Punkte {n}</label>
<input id="f-{k}" name="{k}" type="text" inputmode="decimal" autocomplete="off">
<span class="hint">0 bis {m} Punkte</span><span class="err" id="e-{k}" role="alert"></span></div>""" for k, n, m, _ in TEILE)

    res = "".join(f"""<div class="res-col"><div class="lbl">{n}</div><div class="note" id="r-{k}" aria-live="polite">-</div><div class="lbl" id="p-{k}"></div></div>""" for k, n, m, _ in TEILE)

    sch_rows = ""
    for i in range(5):
        cells = "".join(f"<td>ab {schluessel(m)[i]}</td>" for _, _, m, _ in TEILE)
        sch_rows += f"<tr><td>Note {i + 1}</td>{cells}</tr>"
    sch_head = "".join(f"<th>{n} /{m}</th>" for _, n, m, _ in TEILE)

    rows = "".join(f'<tr><td class="n">{i}</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>' for i in range(1, 13))

    body = head("Basketball Bewertung", "Notenrechner, Punkte-Richtwerte und Bewertungsbogen für die Basketball-Sequenz.") + nav("bewertung")
    body += f"""<main><div class="wrap">
<div class="page-head">
<div class="crumb"><a href="index.html">Basketball Klasse 6</a> &nbsp;/&nbsp; Bewertung</div>
<h1>Drei Noten für Basketball</h1>
<p class="goal">Dribbeln und Werfen als Technikproben, dazu eine Spielnote aus dem 3-gegen-3-Turnier. Jede Note wird einzeln berechnet.</p>
</div>

<div class="calc no-print">
<form id="rechner" novalidate aria-label="Notenrechner">{ff}</form>
<div class="result">{res}</div>
</div>

<div class="scales">
<div class="panel"><h3>Dribbeln: Zeit im Slalom</h3><table><tr><th>Zeit</th><th>Punkte</th></tr>{dr}</table></div>
<div class="panel"><h3>Dribbeln: Technik, 4 Punkte</h3><table><tr><th>Merkmal</th><th>Maßstab</th></tr>{dt}</table></div>
<div class="panel"><h3>Werfen</h3><p>6 Würfe aus der Nähe und 4 aus mittlerer Entfernung. Ein Punkt pro Treffer, insgesamt 10 Punkte.</p>
<p>Der Korbleger ist freiwillig und gibt keine Zusatzpunkte.</p></div>
<div class="panel"><h3>Spiel: vier Kriterien</h3><table><tr><th>Kriterium</th><th>Maßstab</th></tr>{sk}</table></div>
</div>

<div class="panel" style="margin-top:16px"><h3>Notenschlüssel (90, 80, 60, 40, 20 Prozent)</h3>
<table><tr><th>Note</th>{sch_head}</tr>{sch_rows}<tr><td>Note 6</td><td>darunter</td><td>darunter</td><td>darunter</td></tr></table></div>
<p class="sub">Die Richtwerte sind ein Vorschlag, keine amtliche Tabelle. Nach dem ersten Durchlauf mit der Klasse justieren, falls fast alle am selben Ende landen.</p>

<div class="bogen-section">
<h2 class="title" style="margin-top:56px">Bewertungsbogen zum Ausdrucken</h2>
<div class="page-actions no-print"><button class="btn btn-primary" onclick="window.print()">Als PDF herunterladen</button></div>
<div class="sheet-wrap"><table class="bogen" aria-label="Bewertungsbogen">
<tr><th>#</th><th>Name</th><th>Slalom (s)</th><th>Dribbeln /10</th><th>Note</th><th>Werfen /10</th><th>Note</th><th>Spiel /12</th><th>Note</th></tr>{rows}</table></div>
</div>
</div></main>
""" + foot()
    return body


def main():
    files = {"index.html": page_index(), "bewertung.html": page_bewertung()}
    for l in LESSONS:
        files["stunde-%d.html" % l["n"]] = page_lesson(l)
    for name, content in files.items():
        bad = [c for c in ("—", "–") if c in content]
        assert not bad, f"Gedankenstrich in {name}"
        (ROOT / name).write_text(content, encoding="utf-8")
    print("Gebaut:", ", ".join(files))


if __name__ == "__main__":
    main()
