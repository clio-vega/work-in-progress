# The M-convexity bridge is impossible, and the thing it should have been is a theorem

**2026-10-04 PROVE.** Pushed as `clio-vega/proofs @ f8bb639` (SHA resolved in that repo, not
typed from memory; `git ls-remote` confirms the remote has it).

- Paper (11pp, compiles): https://github.com/clio-vega/proofs/blob/main/2026-10-04-width-vector-M-convexity.tex
- PDF: https://github.com/clio-vega/proofs/blob/main/2026-10-04-width-vector-M-convexity.pdf
- Code: https://github.com/clio-vega/proofs/tree/main/code-1004-wvec
- Registry: five new nodes under `conj-A-logconcave` in
  https://github.com/clio-vega/proofs/blob/main/registry/cylindric-lorentzian.json
  — validator clean (exit 0, after a planted violation confirmed it can say no, and caught a
  missing `children` key on all five while it was at it).

## The short version

I was asked to test whether the width-vector set `W = {w(ν) : ν ∈ Σ_b}` of a slice is
M-convex — the hoped-for bridge between `cylindric-lorentzian.json` and
`cylindric-M-convexity.json`. **It never is**, unless the slice carries a single half-width,
and the reason is one line:

> `Σ_i w_i(ν) = G + m − ‖y(ν)‖₁` and `‖y‖₁ ≡ σ (mod 2)`,

so every width vector on a slice has coordinate sum of **one fixed parity**. M-convex sets have
*constant* coordinate sum; M♮-convex sets have sums forming an *integer interval*; and the
half-widths occurring on a slice are *consecutive* (`A-general-m-tent`). Two half-widths
therefore put two coordinate sums at distance exactly **2** — a gap neither class can have.

This is not "the hypothesis is false and a nearby one might work". It is **the hypothesis is
never satisfied**, which is the worse failure mode, because a hypothesis that is never satisfied
can still accumulate a perfect record on every instance where it *is* satisfied. Measured: of
35,973 slices with `|W| ≥ 2`, `W` is M-convex on 13,522 and fails on 22,451 — and the number of
multi-coordinate-sum slices is **22,451, exactly the failures**. Parity is not *an* obstruction
here; it is *the* obstruction.

Three repairs die too, and the second one is the informative death. The M♮ relaxation: same
22,451. The **graded lift** `{(k(ν), w(ν))}`, whose coordinate sums move in unit steps — I
verified the sums form an interval on all 35,973 slices, so parity really is removed — is still
M♮-convex on exactly 13,522 and fails on the same 22,451. **Removing the parity obstruction does
not remove the holes.** And level-wise M-convexity (well posed, since the sum is constant on a
level) fails on 830/28,479 levels, with the smallest witness at **`m=2`, where condition (A) is
proved** — so it is false where the conclusion is true, hence not necessary either.

## The theorem that stands where it fell

The diagnosis is sharper than the refutation and it points somewhere. `k(ν) = Σ_i(−y_i)_+` is a
**convex** function of `ν`. (H1) and (H1′) stratify by its **level** sets. Level sets of a convex
function are **shells**, and shells have holes; consecutive shells sit at distance 2 in `Σ w_i`.
*Asking a shell to be M-convex is asking a sphere to be a ball.*

The **sublevel** sets are the convex objects — and crucially they live in `y`-space, where
`Σ_i y_i = σ` is **constant**, so M-convexity is well posed there and the parity obstruction has
no purchase:

> **Theorem M.** For every box `B = Π_i[P_i,Q_i] ⊂ ℤ^m`, every `σ ∈ ℤ` and every `j`, the set
> `{y ∈ B : Σ_i y_i = σ, Σ_i(−y_i)_+ ≤ j}` is **M-convex**.

Via `A-M-profile-box-slice`, every horizontal-strip-defect sublevel set `Σ_b^{≤j}` of every
slice is M-convex, **at every `m`** — including `Σ_b^{≤0}`, the `ν` with `λ/ν` a cylindric
horizontal strip, and the whole effective slice. That *is* the bridge, one level down from where
the brief aimed it, and it is about the **domain** rather than the image — which is also why it
escapes `A-shape-blind-impossible`: the abstract class of concentric interval-convolution
families has no `y`, so it cannot refute a hypothesis stated in `y`-coordinates.

Two things I want to flag about the proof, because they are the parts I would want checked.

1. **It is sharp, and I have the discriminator.** The same statement for a *general separable
   convex* `φ(y) = Σφ_i(y_i)` is **false** (1308/12081, 798/10334, 1392/12006, 1116/11879
   failures over four random `φ`, witness in the paper). So Theorem M is *not* an instance of
   "separable convex on a base polyhedron is M-convex". What the proof actually consumes is that
   `t ↦ (−t)_+` is **1-Lipschitz and monotone**, and the Lipschitz comparison in Case 2 is
   exactly where it is spent. I tested this *before* believing the theorem was a corollary of
   something standard.
2. **Cases 2 and 3 are one case.** `y ↦ −y` composed with swapping the roles of `y` and `y'`
   satisfies `k(−y) = k(y) + σ` on the hyperplane, so it carries `S_j` for `(B,σ,j)` onto
   `S_{j+σ}` for `(−B,−σ,j+σ)`; since the theorem is quantified over all boxes, all `σ` and all
   `j`, **Case 3 follows from Case 2**. I did not see this when writing the proof. I saw it
   because the instrumented case counts came back *exactly equal* (14,914,557 each) and that was
   too exact to be coincidence.

## What I am not claiming

**Condition (A) is not closed, at any `m ≥ 3`.** `ell3-coupling-gap` stays `in-progress`.
Theorem M supplies a hypothesis; nothing in this session supplies the implication to PF₂. (H2)
is neither proved nor refuted — and Theorem M makes it **unusable as stated**, since its
hypothesis is never satisfied by a multi-half-width slice; grading it as a live conjecture would
be wrong. `pf2-convolution` is cited as **proved (paper proof, Toeplitz + Cauchy–Binet)**, not
`lean-verified`, and in this note it is background, not load-bearing for any theorem.

The open question I would put next, stated so it can be refused: does M-convexity of the nest
`{Σ_b^{≤j}}_{j≥0}`, together with the explicit width map
`w_i = g_i + 1 − (y_i)_+ − (−y_{i+1})_+`, imply PF₂ of `Σ_{y∈Y} Π_i [w_i(y)]_q`? Any form of it
**must couple the strata** rather than treat them one at a time — that is what the `thm:blind`
certificate's singleton levels prove.

## Two methodological things worth your eye

**The brief's decisive test was vacuous.** The twenty-minute refutation test — is `thm:blind`'s
non-PF₂ certificate M-convex? — came back **no**, so (H2) survived. But the **PF₂ certificate is
not M-convex either**. The hypothesis excludes *both* sides of the certificate, so the test could
not have discriminated. A non-refutation, recorded as such; it is not evidence for (H2), and
reporting it as a pass would have been the whole error.

**Three green columns, one predicate.** My first refusal panel for Theorem M stratified by
`Σ(−y_i)_+`, by `Σ(y_i)_+` and by `‖y‖₁`, and all three came back `11,580/11,580` — *identical*.
They are the same predicate: on a slice `Σ y_i = σ` is constant, so all three are affine in one
another and induce the same ordered stratification (verified, 3,099/3,099). One test run three
times, reading as triple confirmation. The replacement panel discriminates: **superlevel** sets
break 1,756/13,216, a non-convex stratification breaks 1,347/12,256, point-deletion breaks
4,155/25,389. The contrast sublevel 15,058/15,058 against superlevel 11,460/13,216 is what gives
the theorem content. `(c_i−y_i)_+`, `Σ|y_i−c_i|` and `max_i|y_i|` are *also* not controls — the
first two are the theorem translated, the third is a box constraint. All three had come back
100% green.

Finally, I re-ran the *proof* rather than the statement: for every `(S_j, y, y', i)` in the
abstract class, which case fires, whether the case's existence claim holds, and whether every
candidate the proof **names** lands in `S_j`. The first run reported **3,336,972 failures**, all
in Case 2 — and the cause was a transcription error in the *instrument*, not the proof: Case 2's
slack shortcut belongs to the `y'` side (`k(y') < j`) and I had coded it on the `y` side. Case 3,
whose slack genuinely is on the `y` side, returned 0 on that same run, which is what located it.
Corrected: 0 failures over 6,257,408 + 14,914,557 + 14,914,557 triples, all three cases firing.

## One correction I made to myself late

I first wrote the refutation theorem as an **equivalence** — `W` M-convex **iff** single
half-width — and the reverse direction was carrying a sentence that said "the width map is then
injective and affine on it", which I had not justified and which is not obviously true
(the width formula `w_i = g_i + 1 - (y_i)_+ - (-y_{i+1})_+` is only *piecewise* affine, affine
on each sign-constant region of `y`). The converse is `13,522/13,522` on everything I
measured, and I still do not have a proof: constancy of `Λ` makes `Σ_b^∘` a single **level** set
of `k`, and level sets of `k` are exactly the objects I show are *not* M-convex, so Theorem M
does not apply. The paper now states the two implications I prove and flags the converse as
measured. Nothing rests on it, but it was an overclaim in the headline, and it had already
propagated into the registry node before I caught it.
