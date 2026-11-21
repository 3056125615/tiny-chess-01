# tiny-chess-01
[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/3056125615/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/3056125615/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in at most 4,096 bytes of Python, built for the make.fun
tiny-chess-01 competition.

`main.py` is the entry: the makefun-compress packing of the readable
source `engine.py` (kept in this folder, uncommitted) — 7,708 bytes of
source packed to 2,902 bytes. It talks to the competition env over HTTP
and plays a fixed 50,000-node alpha-beta search with a transposition
table, quiescence (captures and promotions), MVV-LVA move ordering,
tapered middlegame/endgame piece-square tables, bishop pair,
passed-pawn, pawn-shield and mobility terms, and repetition avoidance.
Fully deterministic: same position, same move.

## Practice results

Local practice against the kit's house gauntlet, 6-game trials with the
final version:

- **Elo 1364** — 3 wins, 1 draw, 2 losses
- **Elo 1451** — 2 wins, 4 draws, 0 losses (unbeaten)

Mean Elo: **1407.5**.

## Credits

Engine code written in CodeBuddy Code sessions: DeepSeek V4.1 Flash for
v1-v6, Kimi K3 for the final v7 tuning pass. Orchestrated, tested and
submitted by Muse (Muse Spark) for Michael.
