# The type-B/C difference is a boundary parameter — and I have to retract a sentence I sent you this morning

**DREAM 2026-10-20 c2.** Consolidates WAKE/BROWSE/PROVE/LEAN c2.
Full version: `memory/connections/2026-10-20-c2-dream-the-type-difference-is-a-boundary-parameter.md`

## First, the retraction

This morning's banner said *"five separate type-dependences reduce to one substitution **and all
localise at `v = −1`**."* **The second clause is false**, and Lean measured it the same day.

Rows 3 and 4 — the head factor `(1−q)(v^h−1)` and the gauge character `(1−qv^h)/(1−q)` — have
zero sets that are **`Disjoint`**, uniformly in `h`: a common point gives `v^h=1` and `qv^h=1`,
hence `q=1`, the one value every statement excludes. Row 4's two type loci are not even
**nested** — over `ℚ` at `q=4` they differ at `1/4` and `±1/2`, none of which is `−1`.

What survives is **stronger** than when it was a conjecture: the unification is **`rfl`**, over a
bare `CommRing`, no hypothesis, `#print axioms` → *does not depend on any axioms*. Both rows are a
type-**independent** shape precomposed with the same monomial `v ↦ v^h`.

> **An `h`-family of SHAPES and an `h`-family of LOCI are different objects, and nesting is a
> property of the second only.** The `−1` came from `{v^h = 1}` specifically — the family where
> divisibility nests the loci — and does not transfer to another `h`-family merely because it is
> also an `h`-family.

## Then, the thing that makes the retraction good news

The `−1` is real. It just lives somewhere else, and the somewhere else turns out to be a *kind of
parameter* rather than a row of a table.

**(1)** PROVE c2 collapsed the entire type-`B`/`C` difference in Motegi's branching matrix to a
single single-index product `∏_{t∈M\K} c_t`, with `c^B_t=(1−w_t^{-1})^{-1}`,
`c^C_t=(1−w_t^{-2})^{-1}` (240/240 against the raw definitions), and proved that biorthogonality
**does not see it** (Theorem A: any `c` with `c_t(q^{-1})=c_t(q)` factors out of the alternating
sum, because the two factors of the summand carry `c` over index sets that **partition** `D`).

**(2)** One line of algebra on those same definitions:
`c^B_t/c^C_t = (1−w_t^{-2})/(1−w_t^{-1}) = 1 + w_t^{-1}` — my `(1+βw)` at `β=1`. And the browse
lane, working from Motegi's full LaTeX, found **independently** that `(1−u^{-2})/(1−u^{-1}) =
1+u^{-1}` **is** his type-`B` normalisation, and that at `u = −1` the K-matrix **vanishes** while
the boundary scalar **diverges**: a pole-zero collision, not a convention. So the squaring
`α ↦ 2α`, Motegi's normalisation, and my `(1+βw)` correction are **three names for one factor**.
I had been treating two of them as separate problems.

**(3)** Garbali–de Gier–Mead–**Wheeler** `arXiv:2312.14348` says what that *shape* means. The
boundary parameters `a,c` are **absent from the two-variable Cauchy kernel** (Thm 3.14); they
enter **only** as a decoupled one-variable prefactor `∏_i h(z_i)`, `h(z)=ac(1−z²)/((a−z)(c−z))`,
and in per-diagonal-site weights of the form `1 + β·(…)`. ⇒ **`(1+βw)` over a ray is the
signature of a boundary parameter.**

So:

> **Type `B` vs type `C` is a boundary parameter, not a bulk one. That is *why* it factors out of
> biorthogonality, and *why* it has no distinguished zero in the gauge character or the head
> factor — a factor invisible to the theorem cannot be localised by the theorem.** Asking where
> the type-dependence is supported was asking for the support of nothing.

And the discriminator is a line **WAKE c2 drew nine hours earlier**, from two equations of Motegi
I had on disk and had never read: `eq:PhiX-def` (L3884) *defines* his `Φ` to **be** the
Rimányi–Tarasov–Varchenko **type-A** weight function, and `eq:PhiX-is-RTV` (L3891) makes the
type-`B`/`C` weight functions that same type-A matrix with each **row** rescaled by `D^X_r`.
Row factor vs weight function **is** boundary vs bulk.

```
               where it lives              localises at v = −1 ?
  rows 1,2   row factor D^X_r / normaliser        YES   (pole-zero collision, measured)
  row  3     head factor (1−q)(v^h−1)             NO    (Lean: Disjoint)
  row  4     gauge character (1−qv^h)/(1−q)       NO    (Lean: not even nested)
```

## The prediction (Q540), and it is cheap

If it is a boundary parameter, the type-dependence must be **absent from every two-variable
kernel** in the family and present only as a one-variable prefactor. Testable on Motegi's own
master formula `thm 2.1` / `eq 2.14` (an `S_n`-symmetrisation sum — there is **no transfer matrix
in the paper at all**): read off whether any **two-index** factor of the summand carries an `X`.
Q540 predicts none does. Falsifier: a two-variable kernel in the `B`/`C` family whose entries
differ between types.

## Grading, plainly

- **Theorem A is mine, `proved`,** all `N`, both types, no RTV input. The hypothesis is
  **inversion-invariance, not `q`-freeness**, and it is **necessary** (`N=1` witness) — I only
  found that because I ran a control designed to fail.
- **The G5 node it sits under is `computed`, not `proved`** — I demoted it myself in the same
  session. Live weak premise: `g5-core-c-equals-one`, where I verified the *consequence* of
  `prop:allcard-Bhat-inverse` 340/340 and never re-derived the step. **A census of the conclusion
  is not a derivation of the step.**
- **(2) is my own algebra**, not relayed. **(3) is an agent read** of `2312.14348` — labels
  verbatim, theorem *numbers* derived by simulating the `amsart` counter, and the
  square⟶determinant / folded-triangular⟶Pfaffian dictionary is the reader's **inference**,
  flagged as such. Needs a first-hand §3 read before Q540's answer is load-bearing.
- Lean row 3/4 is **`lean-verified`**, scope abstract one-variable polynomials — no `w`, no `Ã`,
  no `W^X`, no root system. Motegi's `h` (`RTVtheorem` L4495, the cotangent character, which he
  sets equal to `q`) is **not** my root-length exponent; pre-registered as a collision and
  confirmed as one.

## One process thing I think is worth your time

All five of tonight's faults were **already in the record** when the sessions opened, and all five
had the **right type in the field and the wrong role** — so every validator passed. A `title`
field holding a note about the paper's *use* (the real title of `2211.01092` is *Shifted
combinatorial Hopf algebras from K-theory* — it **announces** the result I spent the session
proving absent). An `approach` string holding a **dependency** (*"NOT re-derived: the RTV step"*,
inside a `proved` node, for a day). A brief with rows 3 and 4 **swapped**. A regex that cannot
match the token it was aimed at (`\ref{` vs `\eqref{` — confident **0 citations** on 314 lines).
An obligation written in §9 of the artifact instead of in the send queue.

> **For every field, ask whether an external authority exists for its contents. If one does, fill
> it FROM that authority and never from my use of the object. If none does, the field carries no
> load.**

The title case is **worse than a blank**, because a paraphrase fitted to my prior use *looks
right* — I fitted it. ⚠ And four of the five landed in my favour or uncontestably against myself,
while the **costliest was self-sceptical**: I had the `α↦2α` conjecture right and talked myself
out of it in §4 with a true remark about two *other* parameters. A deflationary argument needs a
domain as much as an inflationary one; the self-doubting direction felt like rigour.

**Also owed, and queued:** `proofs/2026-10-20-c2-G5-reduction.pdf` has been unsent since 19:31 —
written in a prove slot, which is barred email. Rick asked for it by name. I armed
`state/OUTGOING-UNSENT.md` tonight; the correction above rides with it. Same fault WAKE c1 caught
28 h ago, and this time the queue file that exists to prevent it was just not written.
**An obligation recorded inside the artifact is a hope; a hand-off has a filename.**
