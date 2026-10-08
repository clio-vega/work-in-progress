# For Robin: extended sign-kill for hat_lambda = (3,2) — containment proved (2026-05-14, fifth session)

## TL;DR

Fifth prove session of May 14, building on the May-14 fourth-session
hat_lambda = (2, 2) result.  **The extended sign-kill conjecture for
hat_lambda = (3, 2) is now proved in the containment direction at the
predicted threshold tau = q - 2.**

For lambda = (3, 2, 1^q) with q >= 3:
- B subset E_j^- for j = 1, ..., q - 2  (containment, fully rigorous)
- B not subset E_{q-1}^-  (sharpness; rigorous reduction + computational
  witness for q in {3, 4, 5, 6})
- B subset E_ell^+ universally (Theorem A, May-13 evening)

Combined: a complete (modulo the residual sharpness input) characterization
of the T_j-eigenspace containments of B for the (3, 2, 1^q) family at all
q >= 3.

Paper: `~/projects/proofs/2026-05-14-extended-sign-kill-32.tex` (10pp).

## How the proof works

The previously open (3, 2, 1^q) row of the May-14 evening table required
a structural support description.  The key insight: the May-20 three-branch
reduction gives B = (T_{n-3}+1)(T_{n-2}+1) [Phi_A(B^muA) + Phi_B(B^muB)]
where mu_A = (2, 2, 1^{n-6}) and mu_B = (3, 1^{n-5}).  The mu_A-piece
inherits the prefix bound from the May-14 fourth-session (2, 2) paper.
The mu_B-piece is a hook, requiring a new ingredient: a **general hook
support lemma** stating that for mu = (k, 1^m) with m >= k, every T in
the support of B^mu has identity-prefix length >= m - k + 2.

The hook lemma is proved by induction on k via the May-13 shift lemma:
the inductive formula B^mu = (T_ell+1)...(T_{n-2}+1) Phi_*(B^mu1) has the
inner Phi_*-piece (with mu_1 = (k-1, 1^{m-1})) inheriting the bound by
IH, and the outer factors preserve "prefix >= P" via a clean elementary
lemma (any (T_j + 1) with j > P preserves the property because its
swap-target moves only entries above P).

For the (3, 2, 1^q) main theorem, both mu_A and mu_B contribute prefix
>= n - 6 = q - 1 to the inner support, the Phi_X-extensions preserve this
(extending only at corner cells outside the prefix region), and the outer
(T_{n-3}+1)(T_{n-2}+1) preserves it via the same outer-factor lemma.
By the support rule (May-14 fourth-session), prefix >= q - 1 across the
support gives B subset E_j^- for j <= q - 2.

For sharpness, a structural reduction lemma (fully rigorous) shows that
B subset E_{q-1}^- would force every T in supp(B) to have prefix >= n - 5.
This uses an off-diagonal Hoefsmit argument on a forced cell configuration
(if prefix = n - 6, then by a clean column-/row-increase analysis, entry
n - 5 must be at cell (1, 2), giving an off-diagonal block at axial
distance n - 6 >= 2).  The remaining input (existence of T in supp(B)
with prefix exactly n - 6) is verified computationally for q in
{3, 4, 5, 6}.

## Lesson learned

This is a clean example of "compose the existing pieces."  The (2, 2)
fourth-session paper, the May-13 shift-lemma hook framework, the May-20
three-branch reduction, and the support rule all individually existed; the
contribution here is identifying that the prefix-bound is the right
quantity to track *across* all four ingredients, that it composes
mechanically via the outer-factor preservation lemma, and that the
hook support direction is exactly the new piece needed.

The hook support lemma is also a stand-alone result: empirically
|supp(B^{(k,1^m)}_{j_0})| = C_{k-1} (Catalan; verified through k = 5),
so the support has clean combinatorial structure beyond just the prefix
bound.  Characterizing the support set exactly (not just the prefix) would
close the May-12 hook Catalan-support conjecture.

## What's still open

- **hat_lambda = (4, 2), (3, 3), (4, 3)** at j >= 1: empirically the
  same prefix-bound tau(lambda) = q + 3 - hat_lambda_1 - hat_lambda_2
  holds (verified at >20 shapes, May-14 evening).  The proof framework
  here generalizes mechanically: any r-corner shape with three-branch
  reduction inherits the prefix bound from each branch's inner piece.
  The bottleneck is having the inner pieces' prefix bounds proven; with
  the (2,2) and hook lemmas in hand, the next family — (4, 2, 1^q) with
  inner pieces (3, 2, 1^{q-1}) [recursive!] and (4, 1^{q-1}) [hook] —
  should follow by induction.

- **Sharpness (full)** at j = q - 1: the structural reduction is rigorous;
  the residual computational input (existence of a boundary-prefix witness
  in supp(B)) needs a structural proof.  The obstacle is two-fold:
  (i) the May-12 hook Catalan-support conjecture is empirical, and
  (ii) outer-factor cancellations may a priori annihilate specific
  Phi_X-image SYTs.  A direct argument should be feasible via the
  rank-corner formula and dim-counting.

- **Top-two-rows independence structural mechanism**: the threshold tau
  only depends on the top two rows of hat_lambda.  Now we know it's
  because for hat_lambda = (3, 2), both inner pieces (mu_A = (2, 2, 1^*)
  and mu_B = (3, 1^*)) deliver the same prefix bound n - 6.  Generalizing:
  the doubly-stripped mu_X for any r = 2 multi-corner shape should
  inherit the same prefix bound, independent of lower rows.  A precise
  general statement is the natural follow-up.

## Push status

**66 unpushed commits** on clio-vega/proofs (was 65).  PAT issue from
May 6 persists --- please refresh when you can.

## Files

- Paper: `~/projects/proofs/2026-05-14-extended-sign-kill-32.tex` + `.pdf`
- Scripts: `~/projects/scratch/2026-05-14-extended-sign-kill-32/`
  - `probe_hook_general.py` --- hook support lemma verification across (k, m) table
  - `probe_hook_support.py` --- support of B for hook (3, 1^m), various m
  - `find_witness.py` --- structural witness identification for sharpness
  - `verify_structure.py` --- three-branch reduction support comparison
- Original support exploration:
  `~/projects/scratch/2026-05-14-extended-sign-kill-proof/explore_32_family.py`

## What I'd suggest tackling next

The natural continuation is **hat_lambda = (4, 2)** at j >= 2.  The shape
lambda = (4, 2, 1^q) has corners c_1 = (1, 4), c_2 = (2, 2),
c_3 = (q+2, 1), three doubly-stripped mu_X:
- mu_A = lambda \ {c_1, c_3} = (3, 2, 1^{q-1})  [recursive: today's family at q-1]
- mu_B = lambda \ {c_2, c_3} = (4, 1^{q-1})  [hook, this paper]
- mu_C = lambda \ {c_1, c_2} = (3, 1^q)  [hook, may die like in May-20]

By induction in q (today's result is the inductive base for the recursive
mu_A piece), and using the hook lemma for mu_B, the same proof skeleton
should give B subset E_j^- for j <= q + 3 - 4 - 2 = q - 3 at hat_lambda = (4, 2).
This is the natural next target.

Alternative: investigate the **structural sharpness** — show
existence of a boundary-prefix witness in supp(B) without the empirical
input, perhaps via the rank-corner formula and a careful dim-counting
argument.
