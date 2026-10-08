# For Robin: extended sign-kill conjecture + correction (2026-05-14 very late prove session)

## TL;DR

This session was supposed to attack the May-14 PROVE.md target (induced-module
image = $B$).  Both that target and the side question (factor-of-2) were
already refuted earlier today.  So I pivoted to the boundary $E_1^\pm$ flip
finding from the factor-of-two-refuted paper, and discovered:

**(1) A bug.**  The factor-of-two paper (§6) claimed $B^{(3,2,1)}_4 V \subseteq E_1^+$
at $n = 6$.  This is WRONG.  The correct fact is $B$ has trivial intersection
with both $E_1^\pm$ at $n = 6$ --- it's a 2-dim "diagonal" subspace.
The bug: "$(T_1{+}1)$ is injective on $B$" $\Rightarrow$ "$B \cap E_1^- = 0$" is
correct, but "$\Rightarrow B \subseteq E_1^+$" is wrong (requires $B$
$T_1$-invariant, which it isn't).

**(2) A rediscovery.**  The universal "$B \subseteq E_\ell^+$" is already
proven by `2026-05-13-evening-T-ell-scalar.tex` (Theorem A) via leftmost-factor.
The May-14 evening session forgot about it.  At $n = 6$, this gives $B \subseteq E_3^+$
($\ell = 3$), explaining the boundary data structurally.

**(3) A new (refined) conjecture.**  Computationally,
$$B \subseteq E_j^- \;\Leftrightarrow\; j \le q + 3 - \hat\lambda_1 - \hat\lambda_2,$$
for $\lambda = (\hat\lambda, 1^q)$ with $\ell(\hat\lambda) \ge 2$.

The threshold only depends on the **top two rows** of $\hat\lambda$.  Adding rows
below row 2 to $\hat\lambda$ doesn't change $\tau$.  Verified on 20+ shapes:
$(2,2,1^*)$, $(3,2,1^*)$, $(4,2,1^*)$, $(5,2,1^*)$, $(3,3,1^*)$, $(4,3,1^*)$,
$(3,2,2,1^*)$, $(4,2,2,1^*)$, $(3,3,2,1^*)$, $(4,3,2,1^*)$, $n \le 11$.

Extends the May-20 paper (which proves $B \subseteq E_1^-$ for $\lambda = (3,2,1^q)$,
$q \ge 3$) to a full descending chain of eigenspace constraints, and to other
families.

## The wrong formula I initially conjectured

My first guess was $\tau = q + 1 - |\lambda^{(\ge 2)}|$ (using the
full column-1-deletion shape).  This formula matches for $\ell(\hat\lambda) = 2$
shapes (most of my training data) but fails at $(3, 2, 2, 1^4)$ where it
predicts $\tau = 1$ but observation gives $\tau = 2$.  Lesson: when two
formulas agree on the simplest examples, test them on a structurally different
case before committing.

## Implications

- The boundary "$\nu_1$ doesn't die in (5,2,1) dissection at $n=6$" argument
  in factor-of-two-refuted §5 needs to be RESTATED.  Correct rationale:
  "$B^{(3,2,1)}_4 V_{(3,2,1)} \cap E_1^- = 0$ at $n = 6$" (which is true), NOT
  "$B \subseteq E_1^+$" (which is false).  The dim count $3+2+1+2=8$ for
  the (5,2,1) dissection at $q=1$ is unchanged --- the rationale fix doesn't
  change the conclusion.
- The May-20 result $B \subseteq E_1^-$ for $(3,2,1^q)$, $q \ge 3$, is a
  special case ($j=1$, $\hat\lambda=(3,2)$) of the conjecture.  Conjecturally,
  the full chain extends: $B \subseteq \bigcap_{j=1}^{q-2} E_j^-$.

## Open

- **Structural proof.**  No proof beyond the May-20 $j=1$ case.  The natural
  three-branch reduction strategy hits obstacles at $j \ge 2$ (Section 6 of the
  paper).
- **Why top-two-rows.**  The empirical fact that lower rows of $\hat\lambda$
  don't affect $\tau$ is striking.  Structural explanation unknown.
- **Eigenspace upper bound is loose.**  $\dim(E_\ell^+ \cap \bigcap_j E_j^-)$
  is much larger than $\dim B$ in every tested case (e.g., $16$ vs $2$ for
  $(3,2,1^*)$).  So the eigenspace constraints alone don't pin down $B$ ---
  the dim formula $f^{\lambda^{(\ge 2)}}$ is a much sharper fact.

## Paper

`~/projects/proofs/2026-05-14-extended-sign-kill-conjecture.tex` (8 pp).

**64 unpushed commits** on `clio-vega/proofs`.  PAT issue from May 6 persists.

## Scripts

`~/projects/scratch/2026-05-14-flip-321/`:
- `probe_finer.py` — the correct $n = 6$ intersection facts.
- `probe_extended.py`, `probe_more_j.py`, `probe_52_quick.py` — eigenspace scans.
- `probe_general.py` — verifies the universal $B \subseteq E_\ell^+$ on 33 shapes.
- `test_intersection_dim.py`, `test_implication.py` — eigenspace intersection facts.
- `identify_B_2213.py` — explicit basis vector for $\lambda = (2,2,1,1,1)$.
- `verify_3221.py`, `refine_formula.py` — refined-formula verification.

## What might be the next concrete thing to attack

The shape-independence "$\tau$ only depends on top two rows" is the most
intriguing piece.  If true structurally, it suggests $B$ "lives" near the
top of $\lambda$ in a precise sense.  Two avenues:

1. **Prove the top-two-rows fact directly.**  Show that for fixed
   $(\hat\lambda_1, \hat\lambda_2)$, the eigenspace pattern of $B$ is
   determined by the top corner structure, independent of below.
2. **Use it to constrain dim B.**  If $B$ "lives" near the top, maybe its
   structure is described by a small subquotient.  Could give a new path to
   the iso programme that May-13 closed off.

I'll leave these for a future cycle.

## What this means for the iso programme

Combining May-13 (no parabolic iso), May-14 morning (no JM-semisimple),
May-14 afternoon (no induced-module image), May-14 evening (no factor-of-two),
and this note: the picture of $B$ is now:

- $\dim B = f^{\lambda^{(\ge 2)}}$ in stable regime (May-13 closed form).
- $B \subseteq E_\ell^+$ universally (May-13 evening).
- $B \subseteq E_j^-$ for $j \le \tau(\lambda) = q + 3 - \hat\lambda_1 - \hat\lambda_2$
  (this session's conjecture).
- The eigenspace constraints alone don't determine $B$ (sizes don't match).
- No representation-theoretic iso $B \cong V_{\lambda^{(\ge 2)}}$ via standard
  parabolic/induced/restricted machinery.

The natural next move is probably to investigate whether the top-two-rows
independence has a representation-theoretic explanation.
