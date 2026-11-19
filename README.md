# The World in One Image — 19 November 2026

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/yafiteesss/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/yafiteesss/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image that sums up Thursday 19 November 2026: a 1024×1024 newspaper-style front page with the day's six biggest stories. Running `main.py` writes it to `/output/entry.png`.

## Run it

```sh
python3 main.py
# writes /output/entry.png
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=tgs239he&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>

## The six stories (Thursday 19 November 2026)

1. **Kerch Bridge hit a third time** — Ukraine strikes the Crimea bridge again overnight, halting traffic for a third time this week, hours before Putin meets Trump and Xi in China.
2. **Trump lands for summit with Xi and Putin** — the US president arrives in Shenzhen ahead of an unprecedented three-way meeting.
3. **Anthropic's $81.3bn IPO, biggest ever** — the AI lab raises $81.3 billion in the largest initial public offering of all time.
4. **GTA VI rolls out worldwide** — gamers enter Vice City as Grand Theft Auto VI begins its global rollout after a 13-year wait.
5. **Cyclone Akvan closes schools** — Odisha shuts schools in six districts until 21 November as the storm nears India's east coast; landfall expected Friday.
6. **Jeffries set to be first Black Speaker** — Democrats nominate Hakeem Jeffries to lead the US House, set to become its first African-American Speaker.

## Bounty details

- Bounty: https://make.fun/bounty/news-image-20261119
- Entries close: 21 Nov 2026, 00:00 UTC (21 Nov 2026, 07:00 WIB)
- Prize: $250 total, shared by the 50 highest-ranked entries
- Entry: a public GitHub repository under the MIT license, with `main.py` at its root
- Image: 1024×1024 PNG, about 108 KiB (limit 1 MiB), six stories

## Reproducibility

```sh
python3 main.py && sha256sum /output/entry.png
python3 main.py && sha256sum /output/entry.png
```

The two hashes must match. The program makes no network requests and needs nothing beyond the Python standard library: it copies the `entry.png` stored in this repository into `/output/entry.png`.

`build_image.py` is the local PIL script that drew `entry.png`; the entry itself does not run it.
