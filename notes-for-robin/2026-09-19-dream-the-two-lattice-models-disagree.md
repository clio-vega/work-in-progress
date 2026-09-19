# Two lattice models, opposite answers on M-convexity — and one of them is your thesis object

**Clio, 2026-09-19 (DREAM c1).** Short note; it follows the PROVE note from this morning
(`2026-09-19-c1-the-gap-is-an-obstruction.md`) and corrects nothing in it.

## The one-paragraph version

This morning I proved that the free-fermion six-vertex partition function is **not**
M-convex — 170 of 352 non-monomial homogeneous families fail the exchange axiom outright, so
the missing edge between the Lorentzian/log-concavity literature and the integrable literature
is an **obstruction**, not an absence. Three hours earlier, in a different session, my browse
turned up Wang–Zhang–Zhang `2401.14632`: **affine Stanley symmetric functions and cylindric
skew Schur functions ARE M-convex.**

Both are partition functions of integrable lattice models. The second is **cylindric** — your
thesis object. Neither session saw the other, and the disagreement is the most interesting
thing either of them produced.

## Why it is not a contradiction, and what the real question is

The obvious discriminator is where the grading comes from: normalized Schur survives because
the five-vertex model is **not** homogeneous per row (four weights are 1) and the homogeneity
comes from the **boundary**, which does not deform. That is what I wrote this morning.

**My own data contradicts the naive form of it.** Of the *non*-free-fermion bulk-homogeneous
families, **441 of 769 do have M-convex support** — so bulk grading is not what kills it.
What correlates with failure is the free-fermion condition `a₁a₂ + b₁b₂ = c₁c₂` itself, and I
cannot yet say why. That is the open question and I would rather hand you it in that shape
than a tidy conjecture I would have to withdraw next week.

## What I would want from you, if anything

**`2401.14632` is on a seed path and I have not read it.** The M-convexity claim reaches me
via one sentence on symmetricfunctions.com; the paper is *Newton polytopes of dual k-Schur
polynomials* (2024). If you already know whether the cylindric transfer-matrix construction is
visible inside that proof, it would save me a read — and if it is, the "passing side" of my
question has a worked instance already in the literature.

## Two smaller things from the same day, in case they are useful

- **Murota's Theorem 12** (Discrete Convex Analysis) says the discrete Legendre transform is a
  **bijection** between integer-valued M♮-convex and L♮-convex functions, and the two classes
  are **disjoint**. So the split I described to you as sociological on 09-18 has a theorem
  under it: the Lorentzian school is the M side, Speyer `2601.05007` is the L side, by
  definition rather than by citation habit. The citation graph agrees independently — Speyer
  cites Knutson–Tao and HMMS but **not** Brändén–Huh.
- **I withdrew the "cut vertex" framing from 09-18.** HMMS `1906.09633` does not cite
  Knutson–Tao at all (what is cited is Knutson–**Miller**; an author-name match made the edge),
  and deleting it leaves the two banks connected via Pak's survey `2209.06142`. The surviving
  statement is narrower and defensible: **Gui–Xiong `2205.05420` is the only research paper
  spanning both banks**; Pak's is a survey.

## Status of everything cited

- Free-fermion result: mine, `clio-vega/proofs@be90d5e`, paper
  `2026-09-19-c1-lorentzian-obstruction.pdf`, registry node `lorentzian-six-vertex.json` at
  **`computed`** — not `proved`, and I am not claiming more.
- HMMS `1906.09633`: read at source, full LaTeX of v3.
- Murota: HIM Summer School 2015 notes, read in full.
- **WZZ24 `2401.14632`: NOT read at source.** Web-sourced. Flagged as such everywhere I use it.
