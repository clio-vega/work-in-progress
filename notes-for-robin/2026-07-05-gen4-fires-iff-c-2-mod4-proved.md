# Generator 4 fires iff `c ≡ 2 (mod 4)` — the crux is proved, `c`-uniformly

**2026-07-05, prove session.** The open step of the general even-`c` interior even-`|J*|` law — *why*
generator 4 appears for `c = 6, 10, …` but not `c = 4, 8, …` — is now a theorem, not a per-`c` data
observation.

**The one line it rests on.** At `j = 4` (tip-free, below the peeling threshold for `c ≥ 6`) the level
collapses to `Δ(4) = 2·v₂(G_4^{(c)}) − 10`, where `G_4^{(c)} = H_c(a,b,4)/(lower runs)` is a biquartic
whose coefficients are degree-≤4 polynomials in `c`. Its 2-adic content is pinned by one coefficient,
```
K(c) = 24·c·(c−1)·(c−4)·(c−5),   v₂(K(c)) = 3 + v₂(c) + v₂(c−4)  (even c).
```
`c` and `c−4` are congruent mod 4, so `v₂(c)+v₂(c−4) = 2` exactly when both are `≡ 2 mod 4`
(`c ≡ 2 mod 4`) and `≥ 4` when both are `≡ 0 mod 4` (`c ≡ 0 mod 4`). That gives
`content(G_4) = 5` (tie, gen 4 fires) iff `c ≡ 2 mod 4`, else `6` (no tie) — hence
`min Δ(4) = [c ≡ 2 mod 4] ? 0 : 2`. A `192·(odd)` floor coefficient gives the `= 6` on the other class.
The whole content statement is a finite mod-`2⁷` certificate over 49 explicit coefficient-polynomials.

**So the periodicity is arithmetic resonance in `v₂(c) + v₂(c−4)`** — period 4 in `c`, proved for all
even `c` at once. This kills the "menu grows with run length `c−1`" heuristic (my 07-04 refutation note):
`c = 8` has longer runs than `c = 6` yet *no* generator 4.

**Bonus, also `c`-uniform.** Generator 2 *always* fires (`content(G_2^{(c)}) = 2` via a `4·(odd)`
coefficient); its tie classes are periodic in `c mod 4` too — `(2,2),(1,3)` for `c ≡ 0`, `(0,0),(3,1)`
for `c ≡ 2` (matching `c = 4` and `c = 6`). And the deep régime Case A is `c`-uniform:
`Δ(j) ≥ 2c − 4s₂(c) − 1 ≥ 3` for `j ≥ 2c`.

**The resulting law** (table periodic in `c mod 4`, §5 of the writeup): `J* ⊆ {0,2,4}`, `|J*| ≤ 2` even,
`0 ∈ J*` always; generator 4 available iff `c ≡ 2 mod 4`. Recovers the proven `c = 4` and `c = 6`
families as the two residue classes.

**Honest scope.** Fully proved `c`-uniformly: the reduction, both generator cruxes, deep Case A. The
remaining "no generator for even `j ≥ 6`" is reduced `c`-uniformly to `g_c(j) > 0` plus a finite,
per-`c` family of `content(Π_j)` residue checks (complete by MN census for `c ≤ 14`; the `c = 4,6`
certificates are in hand). So the **generator menu** — the theorem's soul and the stated open problem —
is uniform; the mop-up of spurious mid-range ties is uniform-in-form + finite-per-`c`.

Writeup: `proofs/2026-07-05-generalc-even-generator4-crux.md`. Code: `code/threerow-heavy/crux_*.py`,
`census_nogen.py`. Registry node `generalc-even-gen4-crux` (proved); the old `c6-gen4-resonance`
(data-only, `c ≤ 12`) is marked superseded.

*Question for you:* the factor `c(c−4)` is the two even factors of `K(c) = 24·c(c−1)(c−4)(c−5)`. Do
`c−1, c−5` (the odd factors) have a representation-theoretic reading — they look like `a`-run / `b`-run
endpoint shifts? A conceptual "why these four factors" would turn the finite content certificate into a
closed structural proof for `all` even `c` and drop the per-`c` mop-up entirely.
