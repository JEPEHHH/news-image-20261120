# The World in One Day — Friday 20 November 2026

`entry.png` is one 1024×1024 front page for a single day, set like a broadsheet:
masthead and dateline, a band of hard numbers, a 4×4 lead grid, a markets strip,
a numbered world map, a UTC clock, a column of briefs, and a box for what did not
make the page. Every item carries the outlet that reported it.

**Scope.** 50 stories from that one day across six regions — 16 main boxes and 34
one-line briefs. Nothing that first broke before 20 November is on the page; those
items sit in the *date check* box instead, so the edge of the day is visible
rather than blurred.

## The page, top to bottom

1. **Dateline** — `Friday 20 November 2026`, with the edition line and a count of
   the stories on the page.
2. **Numbers band** — six figures taken straight from the stories: 300,000
   evacuated in Odisha, 423 rescue teams, −4.49% on the Nikkei, 118 for Glenn
   Phillips, 50 stories, $3,551 an ounce for gold.
3. **Lead grid** — one box per story, colour-coded by region (Asia, Europe,
   Americas, Africa, Oceania, Mideast), each with a kicker, a headline, three
   lines of copy and its outlets.
4. **Markets strip** — Nikkei, Kospi, Hang Seng, Brent, gold and the Colombian
   peso, as quoted on the day.
5. **Where the day happened** — a world map with sixteen numbered dots matching
   the sixteen boxes.
6. **The day in UTC** — six moments between 00:00 and 11:00, from COP31's slimmed
   draft to the EU ambassadors' move on Hungary's veto.
7. **Also on Friday** — 34 briefs, numbered on from 17, each with its outlet.
8. **Date check** — twelve items that broke on 19 November or earlier and are
   deliberately kept off the page.
9. **Method** — how the day was bounded, and the outlets used.

## The program

`main.py` is standard library only, takes no network, and does one thing: validate
`entry.png` against the intake limits (PNG signature, chunk CRCs, IHDR first,
IEND last, ≤ 1 MiB, ≤ 1024×1024) and copy it byte for byte to
`$MAKEFUN_OUTPUT_DIR`. It re-encodes nothing, so two runs write identical bytes.

```bash
python3 main.py --check-only   # one JSON line: size, dimensions, chunk count, sha256
python3 main.py                # validate, then write output/entry.png
```
