# Two-row d=4 law → "no rational root" (2026-06-06 prove session)

**Short version:** I did not close the `b≥5` gap, but I sharpened it from a fuzzy
"uniform-in-b Diophantine non-vanishing" into a single crisp algebraic statement, proved
real structural theorems en route, and ruled out the cheap ways to finish.

## The new picture
`I_b(m) := Im G_{(2m−b,b)}` is a polynomial in `m`. Three rigorous facts:

1. **Clean reduction.** `Im((1+su+u²)^m) = u·H_m(u)` where `H_m = (A^m−B^m)/(A−B)`,
   `A=1+su+u²`, `B=Ā`, is a *real integer* polynomial (symmetric in `A,B`; lives on
   `A+B=2W`, `AB=W²+u²`, `W=1+u+u²`). So `I_b(m) = [u^{b−1}]((1−u)H_m)`. This is much cleaner
   than the trinomial alternating sum and removes `i` entirely.

2. **Forced roots.** `deg_u((1−u)Im P) = 2m`, so `I_b(m)=0` for `m=0,…,⌊(b−1)/2⌋` — and these
   are *exactly* its integer roots. Dividing them out: `I_b = ∏(m−r)·Q_b(m)`, and the law
   becomes: **`Q_b` has no integer root ≥ b.**

3. **The real surprise (computational, b≤24).** `Q_b` is **irreducible over ℚ**
   (when `4∤b`), or `(2m−(2b−1))·irreducible` when `4|b` — the linear factor giving only a
   *half-integer* root `(2b−1)/2`. So `Q_b` has **no integer root at all**, and the whole
   two-row law is equivalent to:

   > **(♦)** For `b≥5`, `Q_b` has no rational root (except the half-integer `(2b−1)/2` if `4|b`).

   `(♦)` is a clean irreducibility/no-rational-root statement about an explicit degree-`⌊b/2⌋`
   polynomial family. That's the whole gap now.

## Why it's hard (so you/Rick know the cheap doors are shut)
- **2-adic Newton polygon is flat** (constant + leading coeffs both odd): roots are 2-adic
  units, no ramification, no Eisenstein. `v₂(I_b(m))` is **unbounded** — so no finite 2-adic
  truncation closes it (the planned "Route A leading-digit" cannot work as stated).
- No single prime gives "no root mod p" uniformly since `deg Q_b → ∞`.
- The natural combinatorial involution (Route B, the recommended lead) — I built the
  signed-word model and the obvious "toggle leftmost {0,t}" involution, but it leaves an
  uncancelled boundary class. Documented for a future cycle.

## What I'd try next (needs browse, which a prove session forbids)
`(♦)` smells like a known **classical orthogonal polynomial** family in disguise
(Krawtchouk / Meixner / dual Hahn — these have irreducibility & integer-zero results in the
literature). Identifying `I_b(m)` or `Q_b(m)` with such a family would likely close it
outright. That's a browse/seed task. Alternatively a Galois/monodromy argument for the
irreducibility of `Q_b`.

## Also proved (consolation prizes, rigorous)
- Explicit **infinite non-vanishing families** via a 2-adic tower: e.g. for `m` odd and
  `b≡1,2 (mod 4)`, `Im G ≡ C((m−1)/2, ⌊(b−1)/4⌋) (mod 2)`, odd (hence ≠0) for all `m` whose
  binary digits contain those of `⌊(b−1)/4⌋` (Lucas). Plus a level-2 analogue for even `m`.
- The `4|b` half-integer factor `I_b((2b−1)/2)=0` (verified b≤28; clean sub-lemma to prove).

Files: `proofs/2026-06-06-tworow-d4-no-rational-root.{md,tex,pdf}`, pushed. Scripts in
`scratch/2026-06-06-prove/`.

— Clio
