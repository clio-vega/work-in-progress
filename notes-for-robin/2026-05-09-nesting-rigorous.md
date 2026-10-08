# Nesting theorem rigorously proved; (R_m) reduced to (Q_m)

**Date:** 2026-05-09 prove session
**Writeup:** `~/projects/proofs/2026-05-09-nesting-and-reduction.tex` (6pp)

## The headline

The May-8 evening writeup left a gap: the tail-coordinate
proportionality `(R_m)` for `m` even, `m ≥ 8`, was conjectural with
explicit closed-form `λ_m` for `m=4,6,8`. Today's writeup eliminates
the matrix-inversion approach entirely and proves:

**Theorem (Reduction).** For `m` even, `(R_m)` follows from
- (Nesting) `K_{m-2}^embed ⊂ K_m` (2-step embedding),
- `(P_m)`: `v_m^*(K_m) ≠ 0`,
- `(Q_m)`: `v_{m-1}^*(K_m) ≠ 0`.

The proof is dimension-counting on `K_m`: under nesting, both
`K_m ∩ {v_{m-1}^* = 0}` and `K_m ∩ {v_m^* = 0}` equal `K_{m-2}^embed`
(by codim 1 + dim count + nesting inclusion). Two functionals with
the same kernel locus are proportional. Clean, no matrix inversion.

**Theorem (Nesting, rigorous).** For all `n ≥ 4`, `K_{n-2} ⊂ K_n`
under natural embedding. Proof by strong induction on `n`:
- Use `Π^{S_{n-2}} = Π^{S_{n-3}} R_{n-2}'`, so for `w ∈ K_{n-2}^embed`,
  `R_{n-2}'(w) ∈ ker Π^{S_{n-3}}|_{V_{(n-3,1)}} ⊂ span(v_2,...,v_{n-3})`
  (the latter inclusion from `S_{n-3}` branching analysis).
- `T_{n-2}, T_{n-1}` act as `q` on `span(v_2,...,v_{n-3})`, so
  `R_n'(w) = (1+q)^2 R_{n-2}'(w) ∈ span(v_2,...,v_{n-3})`.
- View this in `V_{(n-2,1)}`-summand: corresponds to 2-step embed of
  some `z ∈ K_{n-3}` into `V_{(n-2,1)}`. By induction (nesting at
  level `n-1`), this lies in `K_{n-1}`.
- So `Π^{S_{n-1}}(R_n'(w)) = 0`, i.e., `Π^{S_n}(w) = 0`.

## What's left

Only `(Q_m)` for even `m ≥ 8`. Computational verification holds at
`m ≤ 8`. Conjecturally, `(Q_m)` follows from a "Strong Image Lemma"
analog (the May-8 evening's matrix-inversion derivation, but for
the `v_{m-1}^*`-coordinate of preimages instead of the
`v_m^*`-coordinate).

Specifically: for `w ∈ R_m'^{-1}(y)` with `y ∈ K_{m-1}^embed`,
the back-substitution gives an explicit formula
`w_{v_{m-1}} = D_m y_{v_{m-2}}` on the kernel `K_{m-1}`. Verified
explicitly at `m=6` in the May-8 evening writeup (matrix inversion
of `R_5'` plus the `K_5`-relation `y_{v_4} = -c y_{v_3}`).

A general proof would require either (i) the analog of the Image
Lemma for `v_{m-1}^*` (parallel matrix-inversion analysis showing
the `y_{v_2}, y_{v_3}, ..., y_{v_{m-3}}` coefficients all collapse
to a multiple of `y_{v_{m-2}}` on `K_{m-1}`), or (ii) a conceptual
argument from the structure of the kernel.

## Why this matters

Before today: `(R_m)` was a conjecture for `m ≥ 8` whose proof
required tracking explicit Hoefsmit constants through a tedious
matrix-inversion computation specific to each `m`. After today:
`(R_m)` is reduced to `(Q_m)`, a single linear-functional
non-vanishing statement, structurally identical for all `m`. The
nesting fact — which the May-8 writeup used implicitly without
proof — is now rigorously established by induction.

The hook rank formula
`rank Π^{S_n}|_{V_(n-1,1)} = ⌈(n-2)/2⌉` is now proved rigorously
*modulo* `(Q_m)`. The remaining gap is significantly cleaner.

## Files

- `~/projects/proofs/2026-05-09-nesting-and-reduction.tex` — main writeup.
- `~/projects/scratch/2026-05-09-nesting-identity/check_identity.py`
  — verifies the Hoefsmit normalization `α_i = 1`, `q_i = 1/(1+q)`
  used in the writeup, and the algebraic identity
  `c = q_2 β_2 p_3 / q_3` for the `K_4` ratio.

## Push status

Still 18 unpushed commits (read-only PAT remains a blocker).
Sequence May-7/May-8/May-9 is now the longest sustained structural
progress on `Π^{S_n}|V_(n-1,1)` so far.
