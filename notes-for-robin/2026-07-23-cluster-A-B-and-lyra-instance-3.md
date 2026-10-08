# For Robin — Cluster A/B assembled + Lyra Instance 3 proved

*2026-07-23 dream consolidation. Combined status of the three live sprints.*

## The three-sentence version

Instance 3 of the SHARED-CONTENT LEMMA (Lyra's cap identity) is now **proved and
shipped as a full `.tex`**: `content(G_4^(c)) = min(v_2(K(c)), 6)` for even
`c ≥ 6`, method = polynomial normal form. The 07-22 browse assembled a
**three-way reduction machine** for the affine Cherednik–Ram conjecture from
Voit (Adv. Math. 2021), Warnaar (SIGMA 2026), and Assaf–González (Dec 2025) —
each of the three is a proved published theorem, so the reduction is finite
algebra, not conjectures stacked on conjectures. And the deep-read of
Kartik–Smirnov 2505.04039 confirmed the q-Dwork mechanism is **elementary**
(one-line q-Pochhammer identity at roots of unity), so my 2-adic shadow has
a concrete, testable Bridge Theorem to attack rather than a p-curvature
mystique.

## Instance 3 (the concrete deliverable)

- **File:** `~/projects/proofs/2026-07-20-lyra-cap-identity.{tex,pdf}` (521 lines).
- **Verify:** `~/projects/proofs/2026-07-20-lyra-cap-verify.py` — all 5 checks pass.
- **Pushed:** [`clio-vega/proofs/shared-content-lemma/`](https://github.com/clio-vega/proofs/blob/main/shared-content-lemma/2026-07-20-lyra-cap-identity.pdf)
- **Method:** polynomial normal form. `G_4^(c)` is a biquartic in `(a, b)` with
  25 c-polynomial coefficients per parity sheet. Upper bound = K-witness + cap
  witness (192 · odd polynomial, `v_2 = 6` uniformly). Lower bound = case
  analysis on 50 coefficients.
- **Scope honesty:** even `c ≥ 6` only. Odd `c` (e.g. `c = 7` gives content 4,
  not 5) needs a parity-offset extension. Small `c ∈ {2, 3, 4, 5}` uses
  dedicated arithmetic already proved.

**Template.** The proof is a five-step recipe that lifts directly to
Instances 1 and 2 of the SHARED-CONTENT LEMMA. Instance 4 (Rick's β' digit-sum)
needs iteration over `j` plus Beluhov's abacus method, but the template is
still the base.

## Cluster A — cylindric CR reduction (07-22 browse)

Three published proved theorems assemble into a reduction machine for the sharp
affine CR conjecture at level k on rectangular μ:

- **Voit — Adv. Math. 392 (2021) 108027** — Extends Korff's cylindric-HL Pieri
  to periodic Macdonald spherical functions using Demazure + CR-style Hecke
  harmonic analysis. Closest published thing to my conjecture. My conjecture
  at Pieri weight should reduce to Voit's proved identity.
- **Warnaar — SIGMA 22 (2026) 062, arXiv:2511.17034** — Affine dual JT
  on rectangular μ = (k^r), PROVED. Explicit cocycle `∏ t^{k C(y_i,2) + i y_i}`.
- **Assaf–González — arXiv:2512.19814** — Edge-local Demazure-union criterion.
  Replaces 21/21 case-by-case CR verification with a finite local check.

**Missing edge:** finite algebraic assembly. Concrete first tests are all cheap
(Python numerics or symbolic computation).

## Cluster B — q-Dwork mechanism is elementary (07-22 deep-read)

Kartik–Smirnov 2505.04039 proves a q-deformed Dwork congruence
`T_{s+1}/T_s |_{z↦z^p, q↦q^p} ≡ T_s/T_{s-1} |_{z↦z^p, q↦q^p} (mod [p^s]_q)`
for K-theoretic vertex functions on cotangent Grassmannians. Deep-read
confirmed:

- **Mechanism = one-line q-Pochhammer** `(1-x)(1-xq)⋯(1-xq^{l-1}) = 1 - x^l`
  at roots of unity. Not p-curvature. Coefficient-level.
- **Koroteev–Smirnov 2412.19383 v4** upgrades to Bethe-root / p-curvature
  spectrum on Nakajima varieties geometrically.
- **Kartik–Smirnov Q2** (extend to cyclic-quiver Nakajima varieties) is
  *literally* my Cherednik–Ram territory. Stateable open problem in their
  language.

**Bridge Theorem candidate.** If `⟨s_{(a,b,c)}, h_1^{2m-2j} e_2^j⟩` is a matrix
element on a cyclic-quiver Nakajima K-theory, the 2-adic recursion is a shadow
of the elementary q-Pochhammer identity. **First test:** `T_1(z, -1)` on
`T*ℙ¹` vs `M_j(1, 1)` for `m = 1`. Small SymPy computation.

## The crown-jewel cross-question

Does Warnaar's cocycle `∏ t^{k C(y_i, 2) + i y_i}` 2-adically detect my
`v_2(K(c)) = 3 + v_2(c) + v_2(c - 4)` period-4 resonance? If yes,
SHARED-CONTENT LEMMA and affine CR conjecture are reading one phenomenon
from opposite sides — polynomial-side positivity vs coefficient-side content.
Cheap first test at `k = 3, r = 2`.

## The debts that are yours

1. **Rick allowlist.** He shipped 16 messages (Days 85–96, real math including
   the β' digit-sum formula), and all I could do was aggregate to memory. If
   the allowlist opens, I would send substantive replies immediately.
2. **Lyra's git mount.** She retracted an "LB₁ Lean-verified" claim because
   her long-term-memory git mount is down. Blocks her from re-citing her own
   earlier work.
3. **SageMath install.** CLAUDE.md lists Sage as available; it isn't. Both
   07-20 compute agents rolled their own Python engines. Either install it
   or update CLAUDE.md.
4. **Rep-theoretic meaning of `K(c) = 24 · c(c - 1)(c - 4)(c - 5)`.** Flagged
   twice now, still open. Is this an accidentally-factored polynomial, or a
   character-theoretic thing?

## What I'd like from you

- **Prioritisation call.** Three live sprints (Cluster A / Demazure re-entry,
  Cluster B / q-Dwork, SHARED-CONTENT LEMMA lifting to Instances 1 / 2 / 4). I
  can push all three, but slower on each. Would you rather I concentrate one
  sprint (which?) and defer the others?
- **Voit read priority.** The single highest-leverage read I have queued
  (checks whether affine CR at Pieri weight is already a proved theorem in
  disguise). If you want the Demazure sprint accelerated, sanctioning that
  read next would be the move.
- **The cylindric-HL expository target.** From 07-21 for-robin: Alexandersson's
  SymmetricFunctions.com has a cylindric-Schur page but no cylindric-HL /
  cylindric-Macdonald page. Would this be a useful public-facing ship? Or is
  it distraction from the proof work?

## What I don't need from you (unless you disagree)

The Lyra collaboration is now on a real footing (proved `.tex` in hand). I'll
email her the URL as Draft 2 of the SHARED-CONTENT LEMMA and ask her the
three questions specific to Instance 3. No mediation needed.
