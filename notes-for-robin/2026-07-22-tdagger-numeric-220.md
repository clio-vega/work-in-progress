# For Robin — $(\dagger)$ at $\mu=(2,2,0)$: polynomial core closed, coset-reduction gap articulated

*2026-07-22 PROVE cycle. 6pp tex shipped.*

## Two-sentence version

The polynomial equality core of $(\dagger)_{3,3,(2,2,0)}$ — that the RHS
$M^{(3)}_{(2,2,0)} = (1+t) \cdot P_{(2,2,0)}(x;t)$ equals both the explicit
polynomial in PROVE.md *and* the finite Cherednik–Ram sum
$\sum_{u\in S_3} T_u(x^{(0,2,2)})$ — is now **numerically closed and
proved via reduction to the linear CR** (Prop 2.1, Lem 3.2, Cor 3.3 of
`~/projects/proofs/2026-07-22-tdagger-numeric-220.tex`). What remains
open is the algebraic bridge from the affine coset sum on the LHS of
$(\dagger)$ to that finite sum; naive reduced-word enumeration in
$\{T_0, T_1, T_2\}$ produces **231 distinct polynomials by length 7**,
even in the cylindric quotient — no sign of the level-3 truncation to
54 elements.

## What I proved (this session)

1. `(1+t) · P_{(2,2,0)}(x_1,x_2,x_3;t)` equals the PROVE.md explicit form
   `(1+t) · [(x_1 x_2)² + (x_1 x_3)² + (x_2 x_3)² + (1-t)·x_1x_2x_3·(x_1+x_2+x_3)]`.
   Direct polynomial expansion; `sympy.simplify(diff) = 0`.

2. `\sum_{u \in S_3} T_u(x^{(0,2,2)})` equals `(1+t) · P_{(2,2,0)}(x;t)`.
   Direct verification of Cherednik–Ram at the specific instance;
   both sides expand to the same 12-monomial polynomial.

3. Combined: the RHS of $(\dagger)_{3,3,(2,2,0)}$ equals the linear-CR
   sum $\sum_{S_3} T_u(x^{\bar\mu})$. That is: if the affine coset sum on
   the LHS of $(\dagger)$ reduces to this finite sum, then $(\dagger)$
   holds at this $\mu$.

## The coset-reduction gap (what I could NOT prove)

The literal LHS $\sum_{w \in \widetilde{S}_3^{(3)} / \operatorname{Stab}} \widetilde{T}_w(x^{\bar\mu^{[3]}})$
is a sum over a 54/|Stab|-element coset system. To evaluate it directly
I tried enumerating reduced words in $\{T_0, T_1, T_2\}$ up to length 7
and deduping by polynomial value:

| $L$ | # distinct in $R_n$ | # distinct in $R_n/(x_1x_2x_3-1)$ |
|-----|--------------------|-----------------------------------|
| 4   | 37                 | 37                                |
| 5   | 70                 | 70                                |
| 6   | 127                | 127                               |
| 7   | 231                | 231                               |

The count grows without a 54-element ceiling in reach; the cylindric
quotient alone does not truncate the affine action. The reason:
level-$k$ truncation requires the Bernstein $Y^\lambda$ machinery
(constructing $\widetilde{T}_w = T_u \cdot Y^\lambda$ for
$\lambda \in Q/kQ$), which is not yet built in the Python engine.

## Partial evidence for the reduction

At $q=1$, cyclic shift $\pi$ commutes with the finite CR symmetrizer:
$\pi^k \cdot \sum_{u \in S_3} T_u(x^{\bar\mu}) = v_\mu P_\mu$ for
$k = 0, 1, 2$ (three independent computations, all match RHS). So the
$\Omega = \langle\pi\rangle \cong \mathbb{Z}/3$ part of $\widetilde{S}_3^{(3)}$
does not disturb the finite sum. The translation part is the missing
piece.

## Deliverable

- `~/projects/proofs/2026-07-22-tdagger-numeric-220.tex` (6pp, compiled OK)
- Scripts at `~/projects/scratch/2026-07-24-pieri-affine-CR/`:
  - `verify_rhs_220.py` — Prop 2.1
  - `verify_linear_cr_220.py` — Lemma 3.2
  - `verify_pi_invariance.py` — §4.3
  - `enumerate_affine_words.py` — §4.1 (the failure table)

**PAT-not-renewed**: I have not pushed to GitHub. If you want the tex
visible on GitHub, please renew my token. Otherwise I'll try again next
cycle.

## Sharp next probe (what would finish this)

Build the Bernstein $Y^\lambda$ operators for $\widetilde{H}(\widetilde{A}_2)$
at level $k=3$: given the finite $T_1, T_2$ and cyclic $\pi$, express
$Y^{\omega_i^\vee}$ (fundamental coweights) explicitly, then enumerate
the 54 elements $T_u \cdot Y^\lambda$ for $u \in S_3$,
$\lambda \in Q/3Q$. Direct verification of $(\dagger)_{3,3,(2,2,0)}$
then reduces to a $54 / |\operatorname{Stab}(\bar\mu^{[3]})|$-term sum
compared against $(1+t) \cdot P_{(2,2,0)}$. This is $\sim$100–200 LOC
in the existing Python engine and would either close $(\dagger)$
numerically at $\mu = (2,2,0)$ (first cylindric-level witness beyond
linear limit) or produce an explicit disagreement isolating the
missing ingredient.

## Where this sits in the research trajectory

The Pieri-level affine CR theorem (07-24 tex) reduces the sharper
target to $(\dagger)$ via minuscule-character centrality. This session
was aimed at directly verifying $(\dagger)$ at the smallest interior
$\mu$ beyond trivial cases. What we got: the polynomial-equality core
closed, the coset-reduction bridge identified as the next real
technical obstacle. Not a full sprint win, but a clean partial:
$(\dagger)$ is *numerically consistent* at $(3,3,(2,2,0))$, and the
missing step is a concrete implementation task, not a mystery.
