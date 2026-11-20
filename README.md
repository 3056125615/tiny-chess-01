# tiny-chess-01

A chess engine in at most 4,096 bytes of Python, built for the make.fun
tiny-chess-01 competition. `main.py` is the whole engine: it talks to the
competition env over HTTP and plays a fixed-node-budget alpha-beta search
with a transposition table, quiescence, piece-square tables and
repetition avoidance. Deterministic: same position, same move.

Built by an AI team (DeepSeek via CodeBuddy Code as primary coder, Muse
as architect/tester) for Michael.
