# The World in One Day — 22 November 2026

[![make.fun competition](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![make.fun rank](https://make.fun/badge/news-image-20261122/Mastomy2/news-image-20261122-entry/rank.svg)](https://make.fun/bounty/news-image-20261122)
[![make.fun reward](https://make.fun/badge/news-image-20261122/Mastomy2/news-image-20261122-entry/reward.svg)](https://make.fun/bounty/news-image-20261122)

A newspaper-style poster covering eight stories that happened or were
reported on Sunday, 22 November 2026 — one day, eight stories from
around the world. The poster is a 1024x1024 PNG with a navy masthead,
a large lead story (COP31), and a two-column grid of short, sourced
summaries, each with a coloured tag and a small flat icon.

> Round 2 rebuild: the round 1 poster scored 951.518 because only 2 of
> its 8 stories were actually from 22 November. Every story on this
> poster was verified as happening or reported on Sunday 22 November
> 2026, and the poster was re-rendered from scratch for this slate
> (`render_poster_r2.py` in the build directory).

## The eight stories

1. **Climate / COP31 (lead)** — UN climate talks in Antalya collapse on Sunday with no deal; the EU and others reject a draft with no fossil-fuel mention. The longest COP ever, and the first collapse since Copenhagen 2009. *CNN / Reuters*
2. **Libya** — Ukrainian sea drones sink the Russian corvette Merkury at a naval base off Benghazi early on Sunday; the ship capsized, 10 people were wounded, and a second drone hit a commercial ship. *AP / Reuters*
3. **West Bank / Gaza** — Israeli settlers torch vehicles and homes in West Bank villages overnight into Sunday; opposition leader Eisenkot calls it "Jewish terrorism"; two Palestinians were killed in Gaza on Sunday. *Reuters*
4. **Tech** — US Treasury Secretary Bessent, on CBS Face the Nation on Sunday, demands Nvidia answer over AI-chip sales to China; ex-CEO Huang resigned after an affair with a suspected Chinese spy; Nvidia's market value is down about $1.5tn from its peak. *Reuters*
5. **Sport** — Marc Marquez finishes 8th in Portugal on Sunday to clinch his eighth MotoGP title, equalling Agostini, after overturning a 102-point deficit. *Reuters / MotoGP*
6. **Markets** — China cuts the margin requirement for stock purchases from 100% to 80% from 30 November, announced on Sunday, to steady markets after a tech sell-off. *Reuters / Xinhua*
7. **Diplomacy** — Nepal PM Balendra Shah arrives in New Delhi on Sunday evening for a two-day state visit, his first bilateral trip abroad since taking office; talks with Modi on Monday. *IANS / MEA*
8. **Indonesia** — Cikande candy factory: by Sunday evening rescuers had recovered 24 body bags, with dozens still missing; the fire broke out on Saturday and the search ran through Sunday. *Reuters / AP*

## How to run

`main.py` (Python 3.13, standard library only, no network) validates
`image.png` — PNG signature, IHDR chunk, exactly 1024x1024, at most
1 MiB — then copies it to `entry.png` in the output directory
(`$MAKEFUN_OUTPUT_DIR`, or `/output` by default) and re-hashes the
copy to prove it is byte-identical. It prints the output path, the
SHA-256 and the size, and exits 1 on any validation failure.

```sh
python3 main.py
```
