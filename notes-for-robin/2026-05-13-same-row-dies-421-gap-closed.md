# Same-row dies for (4, 2, 1^q): closing the May-12 evening-3 gap

**Date:** 2026-05-13 (morning-after-tracer-formula prove session)
**Paper:** `2026-05-13-same-row-dies-421.tex` (8 pp, commit `3fcdf38`, **unpushed** — PAT still read-only)
**Status:** dim B = 3 and E_1^- containment for λ = (4, 2, 1^{n-6}) at n ≥ 10 are now unconditional.

## Headline

While re-auditing the May-12 evening-3 paper as background for the
next step in the dim-formula program, I caught a real gap: the
Phase A decomposition

  E_+|_{V_λ} = Φ_A(V_{μ_A}) ⊕ Φ_B(V_{μ_B}) ⊕ Φ_C(V_{μ_C})

claimed for λ = (4, 2, 1^{n-6}) is **incomplete**. The shape has a
same-row pair at row 1 (cells (1,3), (1,4)), and the corresponding
same-row +q-eigenvectors span a non-trivial subspace S of dimension
f^{(2,2,1^{n-6})}. At n = 10, dim S = 20 (vs. dim Φ_A + Φ_B + Φ_C = 120,
dim E_+ = 140). So **without** showing S dies under the iteration,
the upper bound dim ≤ 3 doesn't follow from the May-12 argument.

The same gap was inherited by Cor 4.4 of the May-13 Shift Lemma paper,
which asserts the May-12 evening-3 result is now unconditional via the
hook j-formula at k = 4. That's correct for the Φ_B-piece (μ_B is a
k=4 hook) but it doesn't fill the same-row hole.

**This paper plugs the hole.** It proves R'_{j_0} ... R'_{n-1} S = 0
for every q ≥ 2 via the same Shift Lemma machinery that closed the
hook same-row-dies and the (3,3,1^q) same-row-dies — but with the
sub-shape now ν' = (2, 2, 1^q), which is itself **non-hook** but has
a known j-formula (May-13 paper `2026-05-13-non-hook-22-1n.tex`).

## Proof in one paragraph

The iteration R'_{n-3} R'_{n-2} R'_{n-1} on S (3 R'-factors since
j_0 = n - 3). Shift Lemma rewrites this as

  P_{n-3, n-1} = (T_{n-4}+1)(T_{n-3}+1)(T_{n-2}+1) · P_{ℓ, n-2}

where ℓ = n - 4 = q + 2. Restricted to S, the inner factor P_{ℓ, n-2}
corresponds via the same-row iso Ψ: S → V_{ν'} to
P^{(ν')}_{ℓ, n-2} = R'^{(ν')}_{ℓ(ν')} · B^{(ν')}_{j_0(ν')} V_{ν'}.
The May-13 j-formula on (2, 2, 1^q) gives
B^{(ν')}_{j_0(ν')} V_{ν'} ⊆ E_1^-|_{V_{ν'}}, and the trailing (T_1+1)
of R'^{(ν')}_{ℓ(ν')} kills E_1^-. So P^{(ν')}_{ℓ, n-2} V_{ν'} = 0,
P_{ℓ, n-2} S = 0, and P_{n-3, n-1} S = 0.

The argument is structurally identical to the same-row-dies-331 proof
(May-13 night), with the sub-shape promoted from hook (3, 1^{q+1}) to
non-hook (2, 2, 1^q).

## General framework theorem

The proof factors into three ingredients that don't depend on
λ = (4, 2, 1^q). Section 4 isolates them as a general theorem:

**Theorem (General same-row dies).** Let λ ⊢ n with a same-row pair
at row i, λ_i ≥ 3. Set ν_i = λ \ {(i, λ_i-1), (i, λ_i)}, S_i the
same-row part of E_+|_{V_λ} at row i. If the j-formula on ν_i at
sharp index j_0(ν_i) holds (B^{(ν_i)}_{j_0(ν_i)} V_{ν_i} ⊆ E_1^-),
then P_{j_0, n-1} S_i = 0.

This subsumes:
- Hooks (k, 1^{n-k}), k ≥ 3 — done by the Shift Lemma paper.
- (3, 3, 1^q) — done by the same-row-dies-331 paper.
- **(4, 2, 1^q), q ≥ 2** — this paper.
- (k, 2, 1^q), k ≥ 5 — needs j-formula on (k-2, 2, 1^q). Recursive.
- (k, k, 1^q), k ≥ 4 — needs j-formula on (k, k-2, 1^q). Open.

## Why the gap matters

Cor 4.4 of the Shift Lemma paper was relied on for the **refined
recursive rank-corner formula** (May-12 evening-3 Conjecture 12.1) at
the smallest case where it differs from the May-11 formula. With this
fix, the prediction dim B^{(λ)}_{j_0} = dim B^{(μ_A)} + dim B^{(μ_B)}
= 2 + 1 = 3 is end-to-end rigorous for λ = (4, 2, 1^{n-6}).

More broadly, the dim-formula program's "recursive structure" — each
length-pres corner of λ contributes its own dim B^{(μ)} — only holds
when the Phi-pieces span E_+. For shapes with same-row pairs, the
"recursive" formula requires the same-row part to die, which is now a
framework-level theorem (Section 4 of this paper) provided the
sub-shape's j-formula is known.

## Computational verification

Phase A gap (n = 10, 11):
| n  | dim V_λ | Σ dim Φ_X | dim S | dim E_+ |
|----|---------|-----------|-------|---------|
| 10 | 350     | 120       | 20    | 140     |
| 11 | 594     | 189       | 27    | 216     |

Same-row dies (n = 10, 11):
| n  | dim S | after R'_{n-1} | after R'_{n-2} | after R'_{n-3} |
|----|-------|----------------|----------------|----------------|
| 10 | 20    | 5              | 1              | 0              |
| 11 | 27    | 6              | 1              | 0              |

Decay matches the ν' = (2, 2, 1^q)-iteration: 20 → q+1 → 1 → 0.

Scripts: `~/projects/scratch/2026-05-13-same-row-dies/track_S_421.py`.

## Where this fits

- **Closes:** May-12 evening-3 Theorem 1 unconditional (dim = 3),
  Shift Lemma paper Cor 4.4 (rank-zero for (4,2,1^{n-6})).
- **Frames:** Section 4's general framework gives a uniform statement
  covering all proven same-row-dies cases and a clean reduction
  scheme for the next ones.
- **Next target:** j-formula on (k, k-2, 1^q) for k ≥ 4 (to close
  same-row-dies for (k, k, 1^q)) or j-formula on (k-2, 2, 1^q) for
  k ≥ 5 (to extend to (k, 2, 1^q)).

## Honesty

The gap was subtle: the May-12 evening-3 paper cites the May-20 paper's
Lemma 4.4 for the Phase A decomposition. The May-20 paper handles
λ = (3, 2, 1^{n-5}), which has **no** same-row pair, so the
decomposition there is correct. The May-12 evening-3 paper inherits
the statement without re-checking whether the same-row condition is
present for (4, 2, 1^{n-6}). It is.

The lower-bound argument in May-12 evening-3 (Proposition 9, the
explicit construction of F_{A,A}, F_{A,B}, F_B and the
position-of-(n-1) separator) is unaffected — those vectors live in
the Φ_A and Φ_B pieces, and their linear independence is checked
directly. So the dim = 3 result is correct; the upper-bound
justification was just incomplete.

**45 unpushed commits** total on `clio-vega/proofs` now. PAT still
read-only — please fix when you have time, Robin.

## Bonus observation: refined formula extends cleanly to $(5, 2, 1^q)$

After the gap was closed I computed $\dim B^{(\nu)}_{j_0(\nu)}$ for
$\nu = (5, 2, 1^3)$ at $n = 10$ as a sanity check on the next case:

  **dim B = 4** (vs. dim V = 448).

This matches the refined recursive formula
$\dim B^{(\mu_A)} + \dim B^{(\mu_B)} = 3 + 1 = 4$ where
$\mu_A = (4, 2, 1^2)$ (May-12 evening-3 family) and $\mu_B = (5, 1^3)$
(hook). The recursion bottoms cleanly: the C-piece (corner pair
$\{c_1, c_2\} = $ both length-pres) dies via the same leakage
mechanism we saw for $(4, 2, 1^q)$ — the iteration on $\mu_C = (4, 1^4)$
hits the sharp index, then the leading $(T_1+1)$ of $R'^{(\mu_C)}_{q+2}$
annihilates $E_1^-|_{V_{\mu_C}}$. The same-row-at-row-1 part dies via
the general framework theorem (Sec 4 of this paper), using j-formula
on the sub-shape $\nu_1' = (3, 2, 1^q)$ (May-12 today result).

So the next clean structural target is the j-formula on
$\nu = (5, 2, 1^q)$ at $q \ge 5$, with the recursion
$\dim B^{(\nu)} = \dim B^{(4, 2, 1^{q-1})} + 1 = 3 + 1 = 4$ structurally
unconditional. This would close a second test case of the refined
recursive formula at the multi-corner level — the May-12 evening-3
paper's Section 12.1, item (1) next-target.

— Clio
