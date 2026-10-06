# Migration vertical-step measurements — 2026-10-06 c1

Instruments behind `proofs/2026-10-06-migration-vertical-step-gap.tex`.
They import the 1005c3 apparatus (`../mosaic-migration-1005c3/`), which is
unchanged.

- `vert.py`   — dump every strictly vertical step in full. Finds exactly 2, and
                they share the same hexagon region: `H = R (+) [0,1]u_60`.
- `sizes.py`  — every admissible local move for the canonical nest-A rhombus,
                WITH the hexagon tile count. 15 moves, all 4 tiles, so
                minimality cannot discriminate the two vertical directions.
- `pool.py`   — the one that matters. Measures whether a `dphi = -1` vertical
                candidate was ever AVAILABLE, not merely whether it was chosen.
                The engine's tie-break is constant on vertical candidates, so a
                selection tally cannot distinguish geometry from list order.
                Result: available in 0 of 3111 steps.
- `chosen.py` — coverage check: does the engine take steps the exhaustive
                classification never classified? (3111/3111 chosen hexagons have
                exactly one rhombus and four tiles.) This is how hypothesis (G2)
                was found.
- `p3.py`     — why the half-integer-`dphi` candidates are always rejected. All
                346 have the Prop-3.1-forbidden orientation (120,90) and h/v
                false; both controls return 0.

`FINDINGS.md` is the session record, written before the paper.
