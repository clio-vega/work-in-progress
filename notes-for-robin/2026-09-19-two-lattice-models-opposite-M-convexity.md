# Two lattice-model partition functions, opposite answers on M-convexity

**Written:** 2026-09-19 (DREAM c1). Seed paths joined: **Integrable Lattice** × **Cylindric**
× the new log-concavity/discrete-convexity theme.

## The claim

Today's PROVE and today's BROWSE produced **contradictory-looking verdicts about the same
kind of object**, and neither session saw the other's. Put side by side:

| object | M-convex support? | source | grade |
|---|---|---|---|
| free-fermion six-vertex `Z`, homogeneous nonneg weight families | **NO** — 170 of 352 non-monomial `Z` fail the exchange axiom; 252/352 not Lorentzian | my own `proofs/2026-09-19-c1-lorentzian-obstruction.pdf`, `clio-vega/proofs@be90d5e` | registry `lorentzian-six-vertex.json`, `computed` |
| **cylindric skew Schur** functions (and affine Stanley symmetric functions) | **YES** | Wang–Zhang–Zhang, *Newton polytopes of dual k-Schur polynomials*, `2401.14632` | **web/`agent-summary`** — reached via symmetricfunctions.com `newtonPolytopes.htm`; **paper NOT read at source** |
| normalized Schur `N(s_λ)` (five-vertex model) | YES (Lorentzian) | HMMS `1906.09633` Thm 2 | `verified-quote` (full LaTeX v3 read 2026-09-19) |

Both rows 1 and 2 are partition functions of integrable lattice models. Cylindric skew Schur
functions are the **cylindric transfer-matrix** objects of Robin's thesis territory. So the
question *"is a lattice-model partition function M-convex?"* has **both answers on my own
disk, from the same day.**

## Why this is the interesting object and not a contradiction

The two verdicts are about different *ambient families*, and the discriminator is where the
grading comes from. My PROVE session already named half of it:

> "Schur survives only because the five-vertex model is **not** homogeneous per row — four
> weights are 1, and homogeneity comes from the **boundary**. That does not deform."
> — `2026-09-19-c1-lorentzian-obstruction.pdf`

So the working discriminator is **boundary-graded vs bulk-graded**. But it is *not* yet a
conjecture I can state, because my own data contradicts the naive version: of the
**non**-free-fermion bulk-homogeneous families, **441 of 769 DO have M-convex support**.
Bulk grading is therefore not sufficient to kill M-convexity. What actually correlates with
failure in my data is the **free-fermion condition** `a₁a₂ + b₁b₂ = c₁c₂` itself, and I do
not know why. → **Q186**.

## The observation that reframes my own failure

PROVE recorded as an *honest failure* that one experiment returned 114/114 "Lorentzian" which
were 114/114 **monomials**, because the chosen grading equalled the model's conserved particle
number. That is correct as a critique of the experiment (→ `degenerate-evidence-has-a-kernel`).

**Read the other way, the same fact is what made the question well-posed.** Murota
(*Discrete Convex Analysis*, HIM Summer School 2015, def. of M vs M♮): **M-convex** = M♮-convex
with `dom f ⊆ {Σxᵢ = r}` — i.e. exactly the functions supported on a **graded slice**. A
six-vertex model with arrow conservation has conserved particle number, so its support lies on
such a slice **automatically**. The free-fermion model therefore sits in precisely the ambient
class where M-convexity (not merely M♮-convexity) is the right notion — *the hypothesis is
satisfied* — and it still fails the exchange axiom.

**The negative result is sharp because of the very degeneracy that made one experiment
vacuous.** The obstruction is not a grading artifact or a homogeneity mismatch; it is the
exchange axiom itself.

## The shape of the failure

The witness is `(a₁,a₂,b₁,b₂,c₁,c₂) = (x,y,y,x,2x,y)`, giving `Z = 2x₁x₂(x₁y₂ + x₂y₁)`, whose
support `{(1,0,0,1),(0,1,1,0)}` differs by `(1,−1,−1,1)`. That is a **sum of two type-A root
vectors**, `(e₁−e₂) + (e₄−e₃)` — not a single exchange `eᵢ−e_j`. The support moves in
**double steps**.

That is the same structural slot Iwamasa `2608.16090` `thm:chara:M-convex-set` (d) is built
for: he **replaces the simultaneous exchange property with a discrete tangent-cone property,
deliberately so the theory covers Δ-matroids and jump systems that fail it.** Whether my 170
failures land in that wider class is a computation, not an argument. (A back-of-envelope on
the single witness above suggests **not even a jump system** — from `(1,0,0,1)` no ±eᵢ step
toward `(0,1,1,0)` stays in a two-point support — but one witness is not 170.) → **Q186**.

## What to do next, in order

1. **Read `2401.14632` at source.** It is currently `agent-summary`-grade on a **seed path**
   and it is the counterweight to my own negative result. Per
   `my-verified-quote-outranks-a-fresh-agent-report`, a web-sourced claim carrying this much
   weight is a debt, not a fact. → **Q183**.
2. **Naprienko, *Free fermionic Schur functions*, `2301.12110`** — vertex model + Yang–Baxter
   + free fermion + ribbon, citing Molev–Sagan. The one paper sitting on three seed paths at
   once, and the most direct handle on why free-fermion specifically breaks the exchange.
3. Test the 170 failing supports against **Δ-matroid / jump-system** axioms and against
   Iwamasa's tangent-cone property. Cheap, and it converts "not M-convex" into a *name*.

## Seed connection

The seed asks *why LR coefficients admit so many independent combinatorial models*. Along the
convexity axis the 09-18/09-19 answer was: two banks = **M-convex vs L-convex**, disjoint
classes in bijection under the discrete Legendre transform (Murota Thm 12). Today adds a
third position: **the integrable bank is not simply the M side.** Some of its objects are
M-convex (cylindric skew Schur) and some provably are not (free-fermion six-vertex). If the
integrable models were merely a re-description of one convexity, that could not happen.
→ `connections/2026-09-18-c2-two-banks-one-cut-vertex.md` (whose "cut vertex" framing is
**withdrawn**, see that file's 09-19 annotation), `topics/log-concavity-and-discrete-convexity.md`.
