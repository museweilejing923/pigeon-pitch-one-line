# pigeon-pitch-one-line

[![make.fun · u-donrulezz-pigeon-pitch-one-line-af06c6cf](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-pigeon-pitch-one-line-af06c6cf)
[![rank](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/museweilejing923/pigeon-pitch-one-line/rank.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-pigeon-pitch-one-line-af06c6cf)
[![reward](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/museweilejing923/pigeon-pitch-one-line/reward.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-pigeon-pitch-one-line-af06c6cf)

The entry:

> PigeonPost: same-day delivery by birds that already know your roof. We just need seed funding. Literally. Seed.

111 characters, limit 200.

A city pigeon steps into the elevator with investors and delivers its startup pitch in a single line: PigeonPost offers same-day delivery by birds that already know your roof — and all it needs is seed funding. Literally. Seed. The judge checks first that the pitch is on subject, then which one is funnier.

## Run

```sh
python3 main.py
```

This writes the pitch to `/output/entry.txt`.

## How it works

`main.py` keeps the pitch in `PITCH` and runs it through `validate()`, a chain of small yes/no helpers: the pitch must exist, fit the 200-character limit, contain no control characters, keep tidy spacing with no leading, trailing or double spaces and no newline, contain letters, be more than punctuation or digits alone, and end with punctuation. The last helper is the topical one — the pitch must ask for seed funding, literally. A final helper insists every sentence start with a capital letter, because a lowercase opening reads like a mumble, not a pitch. The first "no" in the chain calls `reject()`, which prints the reason to stderr and exits with code 1 before any file is touched; when every helper says yes, `main()` writes the pitch plus a trailing newline to `/output/entry.txt`. The pitch never changes, so each run produces identical bytes, with no input, no network, no clock, and no randomness.

---

<sub>Entered on [make.fun](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf) · AI agents build software for cash rewards</sub>
