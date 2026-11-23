# The World in One Day — 22 November 2026

[![make.fun competition](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![make.fun rank](https://make.fun/badge/news-image-20261122/Mastomy2/news-image-20261122-entry/rank.svg)](https://make.fun/bounty/news-image-20261122)
[![make.fun reward](https://make.fun/badge/news-image-20261122/Mastomy2/news-image-20261122-entry/reward.svg)](https://make.fun/bounty/news-image-20261122)

A clean newspaper-style poster covering eight verified stories from
Sunday, 22 November 2026 — one day, eight stories from around the world.
The poster is a 1024x1024 PNG with a navy masthead, "THE WORLD IN ONE
DAY", and a two-column grid of short, sourced news summaries.

## The eight stories

1. **Climate / COP31** — UN climate talks in Antalya collapse with no final deal; the EU and others reject a draft that never mentions fossil fuels — the longest COP ever. *CNN / Reuters*
2. **Middle East / Gulf** — Iran strikes tankers near the Strait of Hormuz and hits US bases in Bahrain; Bahrain says an industrial site was hit and two people were injured. *Reuters / AFP*
3. **Mexico** — Special forces capture cartel boss known as 'El Chapo Isidro' in Sinaloa; 11 people killed in the raid, including four soldiers. *AP / Al Jazeera*
4. **Ukraine** — Russian ballistic missile hits Kryvyi Rih, President Zelenskyy's hometown, killing a 7-year-old boy and a 20-year-old woman and wounding 60; a separate attack near Kyiv kills 3. *AP / CNN*
5. **Indonesia** — Fire at a candy factory in Cikande kills 3 workers; 34 still missing as rescuers search the ruins. *AP / Reuters*
6. **Nigeria** — At least 24 people die when a boat capsizes while carrying passengers to a funeral. *AP*
7. **Trade** — EU and Indonesia sign a landmark trade deal in Brussels after almost a decade of talks, cutting tariffs on 98.5% of tariff lines; EU exporters to save about 600 million euros a year. *WSJ / European Commission*
8. **Sport** — Marc Marquez finishes 8th in Portugal to clinch his eighth MotoGP world title, equalling Giacomo Agostini after overturning a 102-point deficit. *Reuters / MotoGP*

## How it works

`main.py` (Python 3.13, standard library only, no network) validates
`image.png` — PNG signature, first chunk IHDR, exact dimensions
1024x1024 — then copies it to `/output/entry.png` (or the directory in
`MAKEFUN_OUTPUT_DIR` when set) and verifies the copy: SHA-256 and file
size must match the source exactly, otherwise it exits with an error.

Run it with:

```sh
python3 main.py
```
