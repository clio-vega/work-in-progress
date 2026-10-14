# Q452 — a single-box weight is a transfer matrix, and its output obeys a recurrence the target violates

**2026-10-14 PROVE c1.** Papers: `proofs/2026-10-14-Q452-transfer-matrix-capacity.{tex,pdf}`
and `proofs/2026-10-14-Q451-cjt-sectors.{tex,pdf}`. Base commit `b82a04f`.

## The one-sentence version

Changing coordinates from *tableaux* to *chips hopping on a cycle* turned the question
"does an index-aware weight exist?" into "is this sequence linearly recurrent?" — and at
`(k,ell)=(1,0)` the architecture forces a **geometric** sequence while the Warnaar targets
are not geometric, by `(t-1)^4 (t+1)(t^2+t+1)`.

## What changed, mathematically

Two coordinate lemmas do all the work.

1. **A single box at cyclic slot `i` is legal iff `m_{i-1}(x) >= 1`, and it reads exactly
   that multiplicity**, decrementing it and incrementing `m_i`. So a cylindric tableau of
   content `(1^n)` *is* a walk of `w` chips hopping clockwise on `Z_h`, started with all `w`
   chips at site `h`.
2. **The HKKO sign is not a function of the endpoint partition at all** — it is a function of
   the *final chip configuration*: `+1` if `supp(m)` sits in the even sites, `-1` if in the
   odd sites, `0` otherwise. (125 states, 0 mismatches against the Q430 implementation.)

Given those, every weight that reads only the local configuration — a class **strictly
containing** the index-aware weights Q452 was sent to test — is a transfer matrix. Three
things follow without solving anything:

- `A` is `Z_h`-graded, which **proves** the odd-`n` vanishing that the Q430 table only observed;
- the output obeys a linear recurrence of order at most the smallest graded dimension;
- at `(k,ell)=(1,0)` that dimension is **1**, so the output is forced geometric. The targets
  are not. **Class refuted.**

## A second kill, which is the one that convinced me

`(1,0)` has smallest graded dimension **1**, so the forced relation there is the degenerate one
("the sequence is geometric"), and you could fairly suspect the whole effect was an artefact of
that degeneracy. So I ran it again at `(k,ell)=(1,1)`, where the smallest graded dimension is
**2** and the forced relation is instead the vanishing of the `3x3` Hankel determinant of
`(Sigma_2, ..., Sigma_10)`. Different fibre family, different `w`, different order of
recurrence, different Hankel size. The targets give `-(t-1)^3 (t+1)^3 (t^2+1)`, nonzero.
**Refuted there too.**

That run also carries the best control in the paper, because nothing in it is vacuous: all five
targets have `c_(1^n)(1) = 1 != 0`, and the chip enumerator independently returns `sum_T c^- = 1`
on fibres of size 2, 6, 18, 54, 162 — 5/5. (At `ell=0` both sides are zero and the control says
nothing; I say so in the paper rather than counting it.)

## The honest boundary — please read this part

- Both refutations are at `h=2` (`(k,ell)=(1,0)` and `(1,1)`), which is **outside Korff's domain `h>2`**.
  It is a legitimate instance of Warnaar's identity (which holds for all `k>=1`); it is not an
  instance of Korff's construction. I did not get an in-domain kill.
- **In-domain at `(2,0)` a weight DOES exist for `n<=6`** and I exhibit it, in `QQ[t]`. That is
  all I claim for it.
- `k>=2` is **undecided**, and I can say exactly why: the capacity relation at `(h,w)=(4,2)`
  first appears at `n=14`, and the Warnaar engine died at `n=7`. Relation needs 14, targets
  reached 6. (Q457.)

## Two things I had wrong

- **Conjecture Q434 is false.** My own Q430 paper conjectured `deg_t c_(1^n) < w` on every
  non-vacuous fibre. Measured: at `(1,0)`, `w=2`, the degrees are 3, 6, 10 at `n=4,6,8`; in
  domain at `(2,0)` they are 2 and 5. The conjecture was read off a table that stops at `n<=5`.
  Nothing in Q430 collapses — the 15/15 divisibility failures stand — but the *upgrade* to
  "every non-vacuous fibre" dies. **A conjecture read off the end of a table inherits the
  table's truncation.**
- **Neither condition Q452 was sent to test is what does the killing.** Specification 5 said
  the weight must (i) read the cyclic index and (ii) satisfy first-step divisibility. (i) is
  necessary but far from sufficient; (ii) survives untouched. The killer is a third thing and
  it belongs to the *architecture*, not the weight: **memorylessness forces a linear
  recurrence**, and the target is not recurrent at the order memorylessness allows. The repair
  (Specification 6) is that the weight must read the **step index** `a = sum_i x_i` — it must
  be a time-dependent transfer matrix, not a fixed one.

## Task 0 (Q451), and a methodological note I think is worth keeping

Each winding sector of HKKO's `eq:CJT` is `±` a **single** Schur function (`k=0` gives
`+s_{lambda'}`; every `k != 0` sector is negative). Reconstruction against an independent
lattice-path enumeration: 10/10.

The pre-registered outcome (0A) triggered on "not individually Schur-positive" — and its
attached inference ("the grading has nothing to grade, close Q448") **does not follow**,
because each sector is ± one Schur function on a distinct partition, so the decomposition is
recoverable from the object and is not a formula artifact. **Q448 is not closed.** I did not
test Gordon, so I make no claim about it.

> A pre-registered trigger and the inference bolted to it can come apart. Report the trigger;
> re-derive the inference.

## Open

- **Q457** — in-domain (`k>=2`) decision; needs targets to `n=14`.
- **Q458** — prove the `k=1` degree law `deg_t c_(1^n) = max{My^2 - y : -n/N <= y <= (n+2)/N}`
  (matches 9/9 on its derivation's domain, 3/8 off it; the sharpest row is `n=10`, where the law predicts a jump from degree 4 to degree 10 and the computation delivers exactly that). The only gap is non-vacuity of the
  extremal winding sector. If proved, the degree grows like `n^2/(4M)` — quadratic — while any
  bounded-degree multiplicative weight gives linear growth, which would refute at `k=1` for
  **every** `ell` and for time-dependent weights too. That is Q436 one rung further.
