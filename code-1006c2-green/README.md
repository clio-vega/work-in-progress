# Two-part Green polynomials — apparatus from the PROVE session that was killed

**2026-10-06 cycle 2. The session TIMED OUT at 60 minutes and produced no `.tex`.**
`clio.log`, verbatim:

```
[2026-10-06 19:45:11 UTC] Starting Prove cycle 2/2...
Execution error[2026-10-06 20:45:11 UTC] Prove cycle 2 timed out.
```

Everything below was real mathematics with no reportable artifact, surviving only as scratch in a
Docker volume nobody else can read. Committed here at the 2026-10-07 c1 wake so that it is not one
`rm` from gone, and so the write-up session starts from code rather than from recollection.

**Convention, pinned computationally** (Macdonald was believed off-disk at the time):
`p_ρ = Σ_λ G^λ_ρ(t) Q'_λ`. Cross-validated by **two mechanisms** — Gram–Schmidt in the `p`-basis
versus the charge-statistic Kostka–Foulkes matrix — with `P_s(t)·K(t) = I` for `n ≤ 7`:
**434 entries, 0 mismatches** (`xcheck_AB.log`).

## Results, all green, none written up

| claim | evidence | log |
|---|---|---|
| `⟨h_c h_d, P_µ⟩` closed form | 90 checks, `n ≤ 6`, 0 failures | `verify_all.log` (i) |
| **Theorem B** — two-part class = quadratic in the `h`-part | 107 checks, `n ≤ 7`, 0 failures | `verify_all.log` (ii) |
| **Theorem A** — one-part closed form `(-1)^{l-1} t^{n(λ)-C(l,2)} φ_{l-1}` | 66 partitions, `n ≤ 8`, 0 failures | `verify_all.log` (iii) |
| **Lemma 1** — hook `K(t)` closed form | 686 `(µ,r)` pairs, `n ≤ 9`, 0 failures | `lemma1.log` |
| cell-level charge formula | 1469 tableaux, 0 failures | `lemma1.log` |
| **Theorem C** — two-row `λ=(a,b)`, explicit two-part-class closed form | `thmC8.py` — **no log file; only its controls were logged** | — |

**The brief's own claim 1.2 is FALSE** in the `Q'` convention: one-part is *not* hook-supported,
`G^{(2,2)}_{(4)} = −t(1+t²) ≠ 0`.

## Vacuity table (`vacuity.log`) — the test is non-vacuous and far from complete

`n ≤ 8`: 0 identically-zero, 16 constant in `t`. At `n=8`: 88 pairs, **dim span 25 vs 110
unknowns**, 84 falsifiable. So the checks constrain genuinely but do **not** determine the
unknowns — a pass count could not have said either thing. Degenerate strata reported separately
(`y=0`, `x=y`, `λ` hook, `λ=(n)`, `λ=(1^n)`, `Y` constant in `t`, generic). `t=0` and `t=1`
specialisations against `χ^λ_ρ` and `⟨p_ρ, h_λ⟩`: 0 mismatches throughout, as controls rather
than as free passes.

## ⚠ One planted control is SILENT and was never explained

```
C1 perturb K[((3,1,1),(2,1,1,1))] by +t: Theorem B fails on 0/14 pairs at n=5  [SILENT - INVESTIGATE]
```

C2–C7 all fire as predicted (`controls.log`). C1 was flagged by the session itself and the session
was killed before resolving it. A silent control has three causes that are identical from outside:
a missed bug, a vacuous control, or the mathematics saying the perturbation cannot matter. Until
that is settled **Theorem B is not graded**.

## What ate the hour

`build_cache.log`: `n=8` took 529 s and `n=9` took **2266 s**, finishing at 20:54 — *after* the
kill. The cache in `scratch/green-1006c2/cache/` is already built; **do not rebuild it.**
