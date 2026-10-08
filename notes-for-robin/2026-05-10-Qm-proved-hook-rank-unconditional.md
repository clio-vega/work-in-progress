# (Q_m) proved unconditionally; hook rank formula now closed

**Date:** 2026-05-10 prove session
**Writeup:** `~/projects/proofs/2026-05-10-Q-m-via-strong-image.tex` (8pp)

## The headline

The May-9 writeup reduced the hook rank formula
`rank Π^{S_n}|V_(n-1,1) = ⌈(n-2)/2⌉` to a single open property:
**(Q_m): v_{m-1}^*(K_m) ≠ 0 for all even m ≥ 4**.

Today's writeup proves (Q_m) unconditionally. Combined with May-9,
the hook rank formula is now fully proved for all n ≥ 2.

## The two ingredients

### 1. Strong Image Coefficient Formula (rigorous)

For `w ∈ V_{(n-1,1)}` with `R_n'(w) = y ∈ span(v_2,...,v_{n-2})`,
modulo `ker R_n' = Q(q) v_2`:

```
  w_{v_l} = (y_{v_{l-1}} - γ_{l-2} y_{v_{l-2}}) / (1+q)^{n-2}
                                                  for l = 3, ..., n-1
  w_{v_n} = C_n y_{v_{n-2}}                       (Image Lemma)
```

where `γ_i := β_i p_{i+1}` are explicit Hoefsmit constants.

This generalizes the May-8 evening Image Lemma (which gave only the
top coordinate `w_{v_n}`) to ALL coordinates `w_{v_l}` for `l ≥ 3`.
Each is determined by exactly two consecutive coordinates of `y`.

Proved by direct triangular inversion of `R_{n-1}'' = (T_{n-2}+1)
... (T_1+1)` on `V_{(n-1,1)}` using a closed-form formula
`L_j v_l = (1+q)^j q_{l-1} (v_{l-1} + Σ B_{l,k} v_k + B_{l,j} u_j)`
that I prove by induction on the chain of `(T_k+1)` factors. The
back-substitution produces a beautiful telescoping that collapses
the inverse to two terms.

### 2. Alternating sign induction

Define the slopes:
- `μ_l := ξ^(l)_{v_{l-1}} / ξ^(l)_{v_{l-2}}` for `l` odd (≥5),
- `ν_l := η^(l)_{v_{l-1}} / η^(l)_{v_l}` for `l` even (≥4),

where `ξ^(l), η^(l)` are new generators of `K_l` modulo
`K_{l-2}^embed`. Both are intrinsic (independent of choice of new
generator).

By Strong Image and the recursive structure of K_l (via May-9
nesting + reduction):
```
  μ_l = -γ_{l-3} / (1 - γ_{l-4} ν_{l-3})    [l odd ≥ 7]
  ν_l = (1 - γ_{l-3}/μ_{l-1}) / ((1+q)^{l-2} C_l)   [l even ≥ 6]
```

Bases: `μ_5 = -γ_2`, `ν_4 = -1/γ_2`.

**Key sign theorem:** at any `q ∈ ℝ_{>0}`, `μ_l < 0` and `ν_l < 0`.
Proof by alternating induction:
- All `γ_i > 0`, `β_i > 0`, `p_i > 0`, `β'_i < 0`, `C_l < 0` at q > 0.
- If `ν_{l-3} < 0`, then `1 - γ_{l-4} ν_{l-3} > 0`, so `μ_l < 0`.
- If `μ_{l-1} < 0`, then `1 - γ_{l-3}/μ_{l-1} > 0`, so `ν_l < 0`
  (using `C_l < 0`).

### 3. (Q_m) follows

Apply Strong Image at level m to `w ∈ K_m` lifting `ξ^(m-1)`:
```
  w_{v_{m-1}} = (ξ^(m-1)_{v_{m-2}} - γ_{m-3} ξ^(m-1)_{v_{m-3}}) / (1+q)^{m-2}
              = ξ^(m-1)_{v_{m-3}} (μ_{m-1} - γ_{m-3}) / (1+q)^{m-2}
```

Since `μ_{m-1} < 0 < γ_{m-3}` at every positive real q, the
difference `μ_{m-1} - γ_{m-3}` is strictly negative there, hence
nonzero in Q(q). So `w_{v_{m-1}} ≠ 0`, proving (Q_m).

## What's now closed

The full chain:
- May-7 morning: rank formula reduced to dim formula.
- May-8 morning: D_n structure + iterative image program.
- May-8 evening: Image Lemma + reduction theorem (May-8 evening's
  (R_m) gap closed at n=4,6).
- May-9: nesting rigorous + reduction theorem (R_m → Q_m).
- **May-10: Q_m unconditional → hook rank formula unconditional.**

Hook rank formula `rank Π^{S_n}|V_(n-1,1) = ⌈(n-2)/2⌉` is now
**rigorously proved for all n ≥ 2**.

## Why I'm satisfied

1. The Strong Image formula is a clean, structural identity I
   proved directly from the Hoefsmit matrices.
2. The sign induction is a real proof, not a fudge: it uses a
   genuine positivity property of the Hoefsmit normalization that
   I doubt would hold for arbitrary cellular bases. So the
   inductive structure reflects something specific to the seminormal
   form.
3. The proof did NOT require:
   - Closed-form for μ_l or ν_l.
   - A continued-fraction argument (though the recursion structure
     suggests one).
   - Beyond-(n-1,1) analysis.
4. The base cases are entirely concrete: ν_4 = -1/γ_2, μ_5 = -γ_2,
   both positive-definite at q > 0.

## Open follow-ups (NOT pursued today)

- Closed-form for μ_l, ν_l as continued fractions in γ_i.
- Generalization to V_{(n-r, r)} for r ≥ 2.
- Why does the sign alternation work? Is there a duality / pairing
  that gives a cellular interpretation?

## Computational verification (post-proof)

Verified $(Q_m)$ at $m = 4, 6, 8, 10$ by direct kernel computation.
The "new generator" of $K_m$ has $w_{v_{m-1}}$ given by a palindromic
polynomial in $q$ over a positive denominator:

- $m=6$: $w_{v_5} \propto 2q^2 - q + 2$ (coefficient sum $3$).
- $m=8$: $w_{v_7} \propto 3q^4 - 2q^3 + 4q^2 - 2q + 3$ (sum $6$).
- $m=10$: $w_{v_9} \propto 4q^6 - 3q^5 + 6q^4 - 4q^3 + 6q^2 - 3q + 4$ (sum $10$).

Coefficient sums $3, 6, 10, \ldots$ = triangular numbers
$T_{m/2-1}$. The structural meaning of these polynomials is open —
they encode $\mu_{m-1} - \gamma_{m-3}$ in a normalized form.

## Files

- `~/projects/proofs/2026-05-10-Q-m-via-strong-image.tex` (this writeup, compiled to PDF)
- `~/projects/scratch/2026-05-10-strong-image/verify_strong_image.py`
  (verifies Strong Image at n=4..8, signs at q=2, (Q_m) identity at m=6,8)

## Push status

Still 19 unpushed commits (read-only PAT remains a blocker). The
sequence May-7 → May-8 → May-9 → May-10 is now the longest
sustained structural progress on Π^{S_n}|V_(n-1,1) so far.
