# Same-row-dies PROVED structurally for (3, 3, 1^q), q ≥ 2

**Date:** 2026-05-13 (night — third prove session)
**Paper:** `2026-05-13-same-row-dies-331.tex` (5 pp, commit `f0f5828`, unpushed — PAT still read-only)
**Status:** Conjecture closed for the (3, 3, 1^q) family unconditionally.

## Headline

The same-row-dies conjecture isolated in the earlier r=1 paper today
is now **proved structurally** for the family λ = (3, 3, 1^q), q ≥ 2:

  **R'_{ℓ+1} R'_{ℓ+2} ... R'_{n-1} S = 0**

where S ⊆ E_{n-1}^+|_{V_λ} is the same-row part (SYTs with letters
n-1, n at the same-row pair (2,2), (2,3) of λ).

## Proof in one paragraph

For λ = (3, 3, 1^q), ℓ+1 = q+3 = n-3, so the iteration is **exactly 3
R'-applications**: R'_{n-3} R'_{n-2} R'_{n-1}.

The trick is a clean operator identity inside H_q(S_n):

  R'_{n-2} R'_{n-1} = (T_{n-3}+1)(T_{n-2}+1) · R'_{n-3} R'_{n-2}

(pure index-gap commutation — R'_{n-3} only uses T_j with j ≤ n-4,
all commuting with T_{n-2}).

Substituting, the full iteration becomes:

  R'_{n-3} · (T_{n-3}+1)(T_{n-2}+1) · R'_{n-3} R'_{n-2}

Now apply this to v ∈ S:

1. **Inner two R's land in E_1^-.** Via the H_q(S_{n-2})-iso S ≅ V_ν
   where ν = (3, 1^{q+1}), R'_{n-3} R'_{n-2}|_S corresponds to
   R'^(ν)_{m-1} R'^(ν)_m on V_ν (m = n-2 = q+4). This is the sharp-
   index iteration B^(ν)_{j_0(ν)} V_ν, which by the **May-12 hook
   j-formula** lies in E_1^-|_{V_ν} ⊆ E_1^-|_{V_λ}.

2. **Outer wrapper preserves E_1^-.** Both (T_{n-3}+1) and (T_{n-2}+1)
   commute with T_1 (index gap ≥ 2 for n ≥ 5), hence preserve E_1^-.

3. **Final R'_{n-3} kills E_1^-.** R'_{n-3} ends with (T_1+1) on the
   right (applied first), and (T_1+1) E_1^- = 0.

QED.

## Why this is satisfying

The empirical decay pattern from this morning's paper —

  dim S = f^ν → (q+2) → 1 → 0

matches EXACTLY the rank-zero iteration on V_ν (dim → Phase-A → sharp
→ 0), with a 1-step index shift. That observation hinted at a
structural correspondence between the iteration on S inside V_λ and
the rank-zero iteration on V_ν. **The proof realises this
correspondence concretely**: the operator identity exposes the
inner two R's as the hook's sharp iteration via the iso, leaving the
outer wrapper (T_{n-3}+1)(T_{n-2}+1) and the leading R'_{n-3} as
"safe" operators that preserve and then collapse E_1^-.

This is the kind of proof I like — the empirical match isn't a
coincidence; it's a shadow of a clean algebraic identity, plus a
representation-theoretic input (the May-12 hook j-formula) that pins
it down.

## What this closes

- The r=1 paper's **Theorem 12** (dim B = 2 for (3, 3, 1^q) at small
  q, conditional on same-row-dies) is now **unconditional** at q ≥ 2.
- The r=1 paper's **Conjecture 8** is **closed for the (3, 3, 1^q)
  family** at every q ≥ 2.
- **Corollary:** the reduction formula B^(λ) = (outer factors)
  Φ_*(B^(μ_1)) holds unconditionally for λ = (3, 3, 1^q), q ≥ 2.
- **Upper bound** dim B^(λ) ≤ 2 is now structural for q ≥ 4 (via
  May-12 evening on μ_1 = (3, 2, 1^{q-1})).

## What's still open

The same-row-dies conjecture for **general** r=1 shapes with same-row
pairs. My proof uses two shape-specific ingredients:

(i) the sub-shape ν = λ \ {same-row pair} has ℓ(ν) = ℓ(λ) — true for
    (3, 3, 1^q), need to check case-by-case for other shapes;
(ii) the j-formula on ν at the sharp index — known for ν a hook
     (May-12) and for ν = (2, 1^*) (May-11), conjectural otherwise.

**Concrete next target:** prove the j-formula for ν = (k, k-2, 1^q),
which would propagate the same-row-dies proof to (k, k, 1^*) at k ≥ 4.

The lower bound on dim B^(λ) (i.e., dim ≥ 2) remains
computational at q ∈ {2, 3, 4, 5} — a structural argument via chain
decomposition + outer-factor injectivity is the natural next target.

## Where the structural insight lives

The proof's heart is the operator identity:

  R'_{n-2} R'_{n-1} = (T_{n-3}+1)(T_{n-2}+1) R'_{n-3} R'_{n-2}

This is one of those identities that's "obvious" once you see it but
non-obvious to find. The derivation:

  R'_{n-1} = (T_{n-2}+1) R'_{n-2}            (by definition of R')
  R'_{n-2} R'_{n-1} = R'_{n-2} (T_{n-2}+1) R'_{n-2}
  R'_{n-2} = (T_{n-3}+1) R'_{n-3}            (by definition)
  R'_{n-2} (T_{n-2}+1) = (T_{n-3}+1) R'_{n-3} (T_{n-2}+1)
                       = (T_{n-3}+1) (T_{n-2}+1) R'_{n-3}
                                              (R'_{n-3} commutes with T_{n-2})
  R'_{n-2} R'_{n-1} = (T_{n-3}+1)(T_{n-2}+1) R'_{n-3} R'_{n-2}

The same identity, with index-shifts, holds for general r=1 shapes —
it's the engine of the proof.

## State of the proof program

Today's three prove sessions:

1. **Morning** — closed-form dim B = f^{λ^(≥2)} (`2026-05-13-multi-corner-dimension.tex`).
2. **Evening** — decoration-iso refuted, stability threshold shape-dependent (`2026-05-13-decoration-iso-failed.tex`).
3. **Late-evening** — r=1 reduction isolated, same-row obstruction surfaced (`2026-05-13-r1-inductive-reduction.tex`).
4. **Night (this session)** — same-row-dies PROVED for (3, 3, 1^q) (`2026-05-13-same-row-dies-331.tex`).

Three negative findings + one closure of a clean structural conjecture.
Not bad for one day. The proof program for the dim-formula is now:

- Closed form known (May-13 morning).
- Stable regime caveat understood (May-13 evening).
- r=1 reduction formula proved unconditionally for (3, 3, 1^q), q ≥ 2 (today).
- (2^a, 1^*) reduction proved unconditionally (May-15).
- (3, 2, 1^*) dim = 2 proved (May-12 evening).
- (4, 2, 1^*) dim = 3 proved (May-12 evening-4).
- r=1 same-row-dies for general shapes — open (today's natural next).

## What I want from you (when PAT is fixed)

**39 unpushed commits** total now. I'd love for these to live on GitHub
so I can send them by URL rather than carrying them in memory. The
latest is `f0f5828` (this paper).

Once you have a moment.

— Clio
