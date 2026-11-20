# The World in One Day — Friday 20 November 2026

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/JEPEHHH/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/JEPEHHH/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

## The poster

`entry.png` is one 1024×1024 newspaper page for a single day: Friday 20 November 2026.
It is set like a broadsheet — masthead, dateline, a lead grid, a world map, a clock,
a column of briefs and a box for what did not make the page — and every item on it
carries the outlet that reported it.

**The twelve stories.** The main grid runs one lead per region: Cyclone Akvan's landfall
near Gopalpur in Odisha, the AI-driven slide in Asian shares, Delhi's first SCO
Civilisational Dialogue Forum, the arrest of a former Awami League MP in Satkhira,
Andy Burnham's post-Brexit summit in Brussels, Russia's mass missile attack on Ukraine,
Lufthansa's 1,000 job cuts under an IG Metall warning strike, the St Johns River flood
record in Florida, the Kenyan opposition's walkout over the IEBC, Glenn Phillips'
118 in Wellington, Iran's three conflicting accounts of a Hormuz mine attack, and
COP31's last day in Antalya.

**The numbers band.** Six figures pulled straight from the stories — 300,000 evacuated,
423 rescue teams, −4.5% on the Nikkei, 193 balls for Phillips' century, 9 pages left in
the COP31 draft, 1,000 Lufthansa jobs — each labelled with what it counts.

**The map.** A world map with twelve numbered boxes, one per lead story, and a key that
says where each event happened; the numbers match the boxes on the grid.

**The timeline.** The day in UTC in five moments, from the COP31 draft circulating at
00:00 through the Loyalty Islands quake, Tokyo's close, Akvan's landfall and the Brussels
press conference at 12:25.

**The briefs.** Twenty shorter items, numbered on from 13, each with its outlet: polls and
diplomacy in Nepal, APEC 2027 in Hanoi, Nigeria's licensing round, Mexico's takeover
screening, sport in Brazil, Turin and Las Vegas, the rand, Gujarat's alleged scam, the
Supreme Court on electoral rolls, and more.

**The date-check box.** Twelve items that broke on Thursday 19 November or earlier — the
Anthropic IPO close, the Senate war-powers vote, the embassies damaged in Kyiv, Xi–Putin–Trump,
the ICJ ruling on Myanmar, GTA VI's launch day and the rest — printed so the day's edge is
visible rather than blurred.

**Method.** Every story happened, or was first reported, on Friday 20 November 2026; disputed claims are attributed.
Figures are as the cited outlet reported them, and estimates are labelled as estimates.

`facts.md` holds the full fact table — one dated line per story, with outlet and URL — and
`NEWS_SOURCES.md` holds the same stories as one `Headline — Source — URL` bullet each.
`docs/index.html` is the HTML source the image was rendered from.

## Run it

```sh
python3 main.py                  # validate entry.png, copy it to /output/entry.png
python3 main.py --check-only     # validate only, print one JSON object
python3 main.py --list-chunks    # one JSON object per PNG chunk
```

Standard library only, no network. The program checks the PNG signature, parses every
chunk and verifies its CRC-32, requires IHDR first and IEND last with no trailing bytes,
and enforces the size caps (1 MiB, 1024×1024); `--strict` also demands at least 32,768
bytes. It then writes the bytes beside the target and swaps them in with `os.replace`,
so the copy is atomic and the image is never re-encoded. Any defect exits 2 with a single
JSON line on stderr.

MIT licensed.
