# prop:regII is now a theorem about the paper's object, not about a formula

**2026-10-01 c2, Lean session. Sorry-free. Nothing here needs an edit to the paper.**

New file, pushed to `clio-vega/tworow-d4-kernel` (commits `6aae9d0`, `84f9da1`):
<https://github.com/clio-vega/tworow-d4-kernel/blob/main/TworowD4Kernel/Convolution.lean>

Snapshot note (local, not pushed — ask if you want it in a repo):
`projects/proofs/2026-10-01-c2-lean-convolution.md`

## The gap I closed

`prop:regII` of `2026-09-30-c1-cylindric-kostka-logconcavity.tex` is a claim about a
**convolution**: `G(s) = Σ_t (1_[a_t,b_t] * 1_[c_t,d_t])(s)`. When I formalised it on 09-30,
I *defined* `GR` by the trapezoid formula `min(s−ℓ+1, h−s+1, n_t, m_t)_+` and proved `PF₂` for
that. So the sorry-free `GR_PFtwo` was a machine-checked theorem **about a formula**, and the
sentence it was supposed to certify was about something else. I wrote that down at the time, in
a "What is NOT formalised" section — but a comment is not an assertion, so nothing was
checking it, and anything built on top would have inherited the wrong reading.

Now: convolution on `ℤ` is defined (`conv f g s = ∑ᶠ x, f x * g (s−x)`, a `finsum`, so no
window appears in any statement), the trapezoid formula is a **theorem**
(`conv_ind_ind`, your l.394), the paper's `eq:G` is proved **equal** to `GR`
(`sum_conv_eq_GR`), and `sum_conv_PFtwo` is `prop:regII` for the sum of convolutions itself.
All `[propext, Classical.choice, Quot.sound]`.

The formula's proof turned out to be a *count*, not an induction — the summand becomes an
interval indicator, so the value is `#(Icc a b ∩ Icc (s−d) (s−c))` and `Int.card_Icc` plus
`omega` finish it. Pleasingly inevitable: the trapezoid's four edges are just the four ways
that intersection can be pinched.

## A correction to myself that concerns you only because it nearly reached the paper

My session brief told me to record that the paper **cites (P3)** (closure of `PF₂` under
convolution) *in full generality* while using only the interval-indicator case — i.e. a scope
complaint against the write-up, with an edit owed to the `.tex`.

That was wrong, and the registry already knew: node `pf2-convolution` is `trust: proved` —
you prove (P3) from scratch, `T(f*g) = T(f)T(g)` on bi-infinite Toeplitz matrices plus
Cauchy–Binet. **The paper owes no edit.** What is true is narrower and is about *my* side:
a formalised `prop:regI` needs only the weaker *window sum of `PF₂` is `PF₂`*, which is
reachable without Toeplitz matrices. I committed the wrong wording first and corrected it in
`84f9da1`.

The thing I want to flag for its own sake: the mathematics my brief asked for was sound either
way, so the one clause I checked last was the clause that **graded your paper**.

## Still open, stated honestly

- **`prop:regI`.** `conv_ind_left` proves the *reduction* — convolution against an interval
  indicator **is** a sliding window sum of constant width. The *implication* is not proved.
  The obstruction is written into the file: with `α = w(s−1−B)`, `β = w(s−B)`, `γ = w(s−A)`,
  `δ = w(s−A+1)`,
  `W(s)² − W(s−1)W(s+1) = W(s)(β+γ−α−δ) + (α−γ)(β−δ)`.
  This is *not* `omega` plus termwise log-concavity — it needs the monotone-ratio form
  `βγ ≥ αδ` together with `W(s) ≥ β+γ`. At window width 1 it degenerates to exactly
  log-concavity of `w`, which is a check on the identity and **not** evidence for the general
  case; I have been burned by that kind of captive sample before.
- **The `−∞`-extended `lem:trunc`.** Your remark "the same proof applies" is now a stated
  proposition in the Lean file rather than a remark, and I can say why it is genuinely
  separate: the interval-support conjunct in the finite proof comes from `IntConcave.min_le`,
  whose induction `slope_antitone` **walks outside `[p,q]`**. I think the extended claim is
  true — the `−∞` cut makes concavity free at both endpoints — but I did not prove it today.

Two of four regions remain verified, not four. The parent node is still not promoted.
