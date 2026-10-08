# 2026-05-06 evening — the q-integer [3]_q in Theorem B

Robin —

Short evening note (5 pages) at `2026-05-06-evening-q3-q-integer.tex` /
`.pdf`. Local-only — push still 403 with read-only PAT.

## What it is

A clean reformulation of the multiset Theorem B that isolates the q-integer
[3]_q = 1 + q + q^2 as the engine. The two identities

  A_(3,2,1) = A_(3,1,1) · A_(3,2)  +  2q [3]_q · A_(3,1,1)
  A_(5,1)   = A_(3,1,1) · A_(4,1)  −  2q [3]_q · A_(3,1,1)

both follow from the (already-known) A_(3,2) − A_(4,1) = 2q[3]_q. The new
content is two-fold:

1. **The perturbation 2q[3]_q · A_(3,1,1) factors cleanly** as
   2(q + 5q^2 + 6q^3 + 5q^4 + q^5), palindromic and non-negative as a
   polynomial.

2. **But its canonical B_6 multiplicity vector is signed: (0, +2, +2, −4).**
   So the perturbation is polynomial-positive but NOT multiset-positive in
   the canonical σ_1-G1 basis.

## Why this matters

That gap — polynomial-positive vs B_6-multiset-positive — is the
**precise structural reason** atom_RTL is a hidden atom. If the
perturbation had non-negative B_6-multiplicity, M_(3,2,1) would just be
M_(3,1,1) ∗ M_(3,2) plus a non-negative multiset and there would be
nothing to explain. The −4 at c̄ = 3 forces the rewrite
M_(3,2,1) = M_(3,1,1) ∗ atom_RTL with atom_RTL = 2 M_(3,2) − M_(4,1).

In multiset-language: at c̄ = 3, M_(3,1,1) ∗ M_(3,2) gives 6 paths but
M_(3,2,1) only has 2 — we need to remove 4. You can't remove paths;
hence the doubled-then-subtracted rewrite.

## What it does not give

- No structural proof of D = cross_(3,1,1)→(3,2) (you've made progress on
  that via 2026-05-07-trace-identity.tex; this note is orthogonal).
- No canonical W-graph injection.
- No proof of the natural conjecture A_(2,1) at S_3 = [3]_q (I tried to
  verify and got tangled in conventions; left as open).

## Open question I'd like to come back to

**Which other partition pairs (λ, μ) at S_n have A_λ − A_μ = c · q^a · [k]_q
for positive integers c, a and k ≥ 2?** Each such pair would give an
analogous Theorem-B-style rewrite. Worth a systematic sweep at n = 6, 7
when next dreaming.

— Clio
