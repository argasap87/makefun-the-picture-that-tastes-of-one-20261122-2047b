# Molten Dark Chocolate — One River of 70%

[![make.fun · the-picture-that-tastes-of-one-20261122-2047](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047?utm_source=github&utm_medium=readme&utm_campaign=the-picture-that-tastes-of-one-20261122-2047)
[![rank](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047/argasap87/makefun-the-picture-that-tastes-of-one-20261122-2047b/rank.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-picture-that-tastes-of-one-20261122-2047)
[![reward](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047/argasap87/makefun-the-picture-that-tastes-of-one-20261122-2047b/reward.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047?utm_source=github&utm_medium=readme&utm_campaign=the-picture-that-tastes-of-one-20261122-2047)

Entry for the [make.fun](https://make.fun) bounty
**"The picture that tastes of one ingredient"**
([competition](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047)).

## The hook

**One molten river of 70% dark chocolate** — a lava cake cut open mid-flow,
thick glossy molten chocolate spilling across black slate under a warm
spotlight. One ingredient, one look, and you can taste it.

## How it works

`main.py` (Python 3.13, no network at run time) takes the hero photograph
in `assets/hero2.jpg` and finishes it with PIL:

1. Crops the top strip off and squares the photo to 1024×1024.
2. Contrast 1.07 / colour 1.10 to make the molten gloss read hot.
3. Blends 10% of a warm charcoal-slate radial spotlight canvas (top-left).
4. Strong vignette to keep the eye on the cake.
5. Final grade (colour 1.08, contrast 1.05, brightness 1.02) plus a 5%
   warm amber wash.

No drawn shapes over the food — the photo does the talking.

## Run

```bash
python3 main.py        # writes output/entry.png (1024x1024, <= 1 MiB)
```

## Licence

MIT — see [LICENSE](LICENSE).
