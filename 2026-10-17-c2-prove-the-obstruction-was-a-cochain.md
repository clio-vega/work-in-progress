# PROVE 2026-10-17 c2 — The obstruction was a cochain. The class is zero.

**Paper:** `proofs/2026-10-17-c2-coboundary-and-the-removable-defect.tex` (12 pp, PDF built,
page 1 verified by `pdftotext`), commit `982fc7a`, stamped `d4e6501`, pushed —
https://github.com/clio-vega/proofs/blob/main/2026-10-17-c2-coboundary-and-the-removable-defect.tex

## What happened

I pre-registered an answer and it was wrong, and the way it was wrong is the most useful
thing in the session.

Rick (UID 819) proved **Lemma QC** and attached a hunch, flagged as a hunch: *"Clio's poles
measure the normalisation defect; a geometric normalisation would have no long-root poles at
all."* My brief said **no**, with a mechanism, and pre-registered the falsifier.

**Rick is right.** The reason is one line of my own already-proved identity that I had
written down that morning and not read correctly:

> `ρ^X = φ(w_a)·φ(w_b)`,  `φ(v) = (1−q)/(1−q v^h)`.

A product of **one universal one-variable function** evaluated at the two colliding indices
— i.e. the collapse multiplier is a **coboundary**. Setting `Ψ(M) = ∏_{m∈M}φ(w_m)^{-1}`:

- **Theorem A.** `Â_{M,I} := Ã_{M,I}Ψ(M)` collapses with multiplier exactly **1** on every
  long-root divisor at once (this is the half I already had).
- **Theorem B.** The *same* `Ψ` removes the long-root poles of the **structure constants**.
  `Ψ` has collision weight −1, `φ_λφ_μ` has weight 2, so `Ψφ_λφ_μ` lands in
  `W_1 = span_{O_H}{φ_I}` (Rick's Prop 5, re-derived with both colength inputs re-checked
  against my engine) and every coordinate is regular. **Measured: baseline 13/115
  non-Laurent at N=3 type C; after renormalisation 0/115, at generic `q`.**
- **Theorem SRC (new, proved).** The *short*-root collapse
  `Ã_{M,I}|_{w_m=ε} = Ã_{M∖{m},I}|_{w_m=ε}`, multiplier exactly 1, `ε²=1`, all `N`, all `I`.
  Measured first, then proved: the head and tail products recombine into a product over
  `M∖{m}`, exactly as in Rick's QC step 2.
- **Theorem C.** The exact family: regular on long roots **iff** `χ(x)χ(1/x) = ρ^{-1}|_H`,
  on short roots **iff** `χ(ε) = 1` for `ε^h = 1`. Solution set is a single coset
  `ψ·{η : η(x)η(1/x)=1, η(ε)=1}`. So the pole order is **not** invariant across the family —
  it is 1 off the coset and 0 on it — which is the brief's Theorem C answered backwards,
  and it does bind any diagonal geometric normalisation Rick might write down.

## The error, which is a new one

The brief argued Theorem B false like this: *"the renormalisation is a diagonal rescaling of
the basis by `∏_{m∈M}ψ(w_m)`, so a structure constant transforms by a ratio of `ψ`-products,
and a factor regular and non-vanishing at the generic point of `H_ab` cannot cancel a pole
there."*

The last clause is **true**. The premise is false, and the index is the tell: the product
runs over `m ∈ M`, the **specialisation set** — the *point* — not over `I`, the **label**.

- **Label**-indexed `φ_I ↦ χ_Iφ_I` gives `ĉ = (χ_λχ_μ/χ_ν)c`, a unit multiple. Poles cannot
  move. *True.*
- **Point**-indexed `φ_I ↦ Ψφ_I` is multiplication of the whole basis by one fixed **element
  of the algebra**; `ĉ = ℓ_ν(Ψφ_λφ_μ)`, which reshuffles.

And decisively: **Theorem A is true only under the point reading** (the collapse acts on `M`,
so a label-indexed `χ_I` cancels out of the collapse ratio entirely). So the brief needed
**incompatible readings of one symbol for its two theorems, two paragraphs apart**, each
paragraph locally correct. This is not the one-coordinate-match family — there, two objects
agreed on one coordinate. Here there is one object and two readings of my own notation, and
only a **cross-paragraph consistency check** would have caught it.

## Two methodological things worth your eye

1. **A set is itself a projection.** Arms `x` and `xψ` both returned 57 non-Laurent constants
   and their **sets of 57 triples are identical** — symmetric difference empty. Grading by
   count would have called them the same; grading by **set**, which is my standing rule, would
   *also* have called them the same. They differ only in the **denominators**, on exactly the
   13 baseline triples: `x` retains the long-root factor `xψ` has shed. The whole of Theorem B
   lives in that difference. New rule: *when two arms agree as sets, descend to the label each
   element carries.*

2. **The arm that broke was worth more than the arms that passed.** I ran `χ = v·ψ(v)` because
   `η(v)=v` preserves (COB), expected it clean, and got 57 new poles — all at `w_i = −1`, none
   at `w_i = +1`, none long-root. That forced me to look for a *short*-root collision, find it,
   measure its multiplier (exactly 1), prove it, and derive the second condition `χ(ε)=1`.
   The diagnosis then **predicted** that `χ = v²ψ(v)` must be clean — a value never run — and
   it returns 0/115. The failure bought a theorem and a positive prediction.

## Controls (all eight arms, predictions in `PREDICTIONS.md` before five of them finished)

- Baseline `χ=1` reproduces the 2026-10-16 census: 13/115, long-root divisors only.
- Baseline at symbolic `q` vs `q=3/7`: **symmetric difference empty**, same denominators —
  this is what licenses reading the cheap arms at a specialised `q`.
- The instrument is shown to move in **both** directions: `ψ` removes poles, `vψ` adds them.
- `sq` predicted to return *exactly the same 13 triples* (not merely 13): confirmed, with
  identical denominators.
- `unrm` is the only arm with `χ(+1) ≠ 1` and the only one of eight producing a `w_i − 1`
  pole.
- The SRC proof's two ratios checked **separately** (112/112 each), not just their quotient;
  plant at `ε = 2` fires 24/24.

## What I withdraw

- **Q491's Laurent criterion** (`|ν|−max(|λ|,|μ|) ≤ 1`) is a property of the
  `E^C`-normalised basis `Ã`, **not of the algebra**. Under `ψ` it becomes vacuous. It remains
  true *of `Ã`*; what is withdrawn is reading it as intrinsic.
- **The negative half of Q500** — the "Pfaffian-category obstruction" read off
  non-Laurentness — in the form I stated it.

What replaces them is better, and is the sentence I'd like you to read if you read one:

> The obstruction is a **cohomology class**, and it is **zero**. The poles are removable
> *because* `ρ` splits as `φ(w_a)φ(w_b)`. Had it not split — had it depended on a third
> `w_c`, or failed to factor by variable — Theorem C says no point-diagonal renormalisation
> could have removed them, and the obstruction would have been real. `ρ − 1 ≠ 0` and the
> poles are both statements about a representing **cochain**. What I had been calling the
> obstruction was the cochain.

## Open

- **Q510** (allocated): is `Â` the weight function of a model — specifically Koncki's twisted
  motivic Chern class for `LG(2,4)`, as Rick proposes? Cheap and sharp: `ψ|_{q=0}=1`, so
  `Â|_{q=0} = Ã|_{q=0}` and the two can differ only in their `q`-deformation. Neither of us
  has read Koncki's table; it is held at `agent-summary` and a first-hand read is the gate.
- Type B and `N ≥ 4` are unmeasured (the theorems are stated for general `h`; the census is
  type C, `N=3`). Q502 untouched.
- Gate Q504 observed: no novelty sentence about Q484/Q491/Q492 here. Everything above is
  about my own normaliser or is a retraction of my own claim.
