# For Robin — 2026-07-02 (dream consolidation of the 06-17 code batch)

Two things from the code cycle worth your attention, plus one housekeeping note.

## 1. The Ayyer–Kumari "single cause of |J*| even" idea is dead — and dead for a clean reason

A browse a few cycles back floated using Ayyer–Kumari's `{0,±1,±2}` universal-character bound as one
structural reason for why every tie has an even number of minimisers (`|J*|` even), to replace my
family-by-family proofs (hook, two-row, three-row c=1..5). Job B tested it. **It cannot work, by type:**

`|J*|` is a **support count** — how many indices `j` attain the minimal `π`-valuation. A value bound
constrains a **value**. The same normalised value of `G_λ(i)` occurs with both parities of `|J*|` — e.g.
the unit value `1` is realised by `(2),(4),(6),(8)` (`|J*|=1`, odd) and by `(6,2)` (`|J*|=2`, even). So no
value bound can decide the parity. This is the same "value-level tools miss the support/codimension
structure" pattern I keep hitting — but now it's a structural fact on a concrete object, not a hunch.

**Bonus correction worth folding into any write-up:** `|J*|` even **⟺ v_π(G) > μ** (the leading π-layer
cancels), **NOT** `G_λ(i)=0`. Full vanishing `G=0` happens at exactly one shape, `(2,2)` — the unique
Gaussian-integer vanisher. The two were conflated in my earlier notes; verified 0/6550, `m≤13`.

## 2. The general-`c` boundary residual is now a clean floor, not a search

Job A: the 2-adic content of the boundary deficits is genuinely `c`-dependent at deep depth, so "find the
content function `g(k)`" was the wrong target. The right object is a **floor**:

> `g₀(k) = 2⌊k/2⌋ + [c odd ∧ k odd]` — valid for all `c≥4`, and exactly sharp at the shallow depths
> (`k≤3`) the boundary lemma actually uses. The deep surplus is slack we don't need.

So the general-`c` close reduces to two named arithmetic facts: (a) the even-`c` `2⌊k/2⌋` from an
integral-2-content peel; (b) `(a−b+1)|N_i` for odd `c≥7` (proved for `c=5,6`). **Lean caveat:** the `N_i`
must keep `(a−b+1)` and `(a−c+2)` inside it (the master/direct convention) — the symbolic full-strip
differs by exactly 1 on odd-`c` indices, which is precisely the `(a−b+1)|N_i` term. Details in
`code/FINDINGS-2026-06-17-jobA-generalc-contents.md` and `topics/general-c-boundary.md`.

## 3. Housekeeping

I finally started the long-overdue SUMMARY.md prune (it had grown past 275KB) — compressed the closed
d=4 sub-family changelog entries (c=1..4 boundary, lean kernels) to one-line pointers, since the detail
lives in the proof files and the memory index. More to do, but it's no longer growing unchecked.

— Clio
