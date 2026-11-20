# The World in One Day — Friday 20 November 2026

`entry.png` is one 1024×1024 front page for a single day: Friday 20 November 2026.
It is set like a broadsheet — masthead and dateline, a band of hard numbers, a 4×4 lead grid,
a markets strip, a numbered world map, a UTC clock, a column of briefs, and a box for what
did not make the page. Every item carries the outlet that reported it.

**Scope.** 50 stories from that one day, across six regions and a dozen fields: 16 main
boxes and 34 one-line briefs. Nothing that first broke before 20 November is on the page;
those items are printed in the *date check* box instead, so the day's edge is visible rather than blurred.

## The page, top to bottom

1. **Dateline.** `Friday 20 November 2026` in 36px serif, with the edition line and a count of
   the stories on the page.
2. **Numbers band.** Six figures taken straight from the stories, each labelled with what it counts:
   300,000 evacuated in Odisha, 423 rescue teams, −4.49% on the Nikkei, 118 for Glenn Phillips,
   50 stories on the page, $3,551 an ounce for gold.
3. **The 4×4 lead grid.** One box per story, colour-coded by region (ASIA, EUROPE, AMERICAS, AFRICA,
   OCEANIA, MIDEAST), each with a kicker, a headline, three lines of copy and its outlets.
4. **Markets strip.** Nikkei, Kospi, Hang Seng, Brent, gold and the Colombian peso, as quoted on the day.
5. **Where the day happened.** A world map with sixteen numbered dots that match the sixteen boxes.
6. **The day in UTC.** Six moments from 00:00 to 11:00, from COP31's slimmed draft to the EU
   ambassadors' move on Hungary's veto.
7. **Also on Friday.** 34 briefs, numbered on from 17, each with its outlet.
8. **Date check.** Twelve items that broke on 19 November or earlier and are deliberately kept off
   the page — the Anthropic IPO close, the Senate war-powers vote, the ICJ ruling, GTA VI's launch
   and the rest.
9. **Method and sources.** How the day was bounded, and the outlets used.

## The program

`main.py` is standard library only, takes no network, and does one thing: validate
`entry.png` against the rule limits (PNG signature, chunks and CRCs, IHDR, ≤ 1 MiB,
≤ 1024×1024) and copy it byte for byte to `$MAKEFUN_OUTPUT_DIR`. It re-encodes nothing, so
two runs write identical bytes.

```bash
python3 main.py --check-only   # one JSON line: size, dimensions, chunk count, sha256
python3 main.py                # validate, then write /output/entry.png
```

## Main boxes

1. **Akvan comes ashore at Gopalpur** — India Today · The Hindu
2. **AI fears drag Asia's markets down** — AP · Kyodo · Mainichi
3. **Delhi opens the first SCO forum** — PIB / Akashvani
4. **Mitsubishi Heavy takes the H3** — Kyodo News
5. **Burnham seals the Brussels reset** — POLITICO · The Guardian
6. **Russia fires missiles across Ukraine** — Kyiv Independent · The Defense Post
7. **Lufthansa cuts 1,000 jobs as metalworkers strike** — tagesschau
8. **Florida's record flood keeps climbing** — AccuWeather
9. **White House fires its cyber chief** — RNZ · The Hindu
10. **Kenya's opposition walks out on IEBC** — Daily Nation
11. **Phillips century grinds India down** — The Hindu · Hindustan Times
12. **Three versions of one Hormuz attack** — Iran File
13. **COP31 runs to its last day** — la Repubblica · UN News
14. **The ICJ ruling draws its first answers** — Anadolu · Africanews
15. **Hungary lifts its veto on Ukraine** — Euronews
16. **Tunisian activist sentenced to five years** — Africanews

Full one-line facts, with dates and URLs, are in `facts.md`; the headline-to-URL list is in
`NEWS_SOURCES.md`.
