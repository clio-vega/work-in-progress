# For Robin: extended sign-kill for hat_lambda = (4,2) — containment proved (2026-05-14, sixth session)

## TL;DR

Sixth prove session of May 14, building on this morning's fifth-session
hat_lambda = (3, 2) result.  **The extended sign-kill conjecture for
hat_lambda = (4, 2) is now proved in the containment direction at the
predicted threshold tau = q - 3, for q >= 4.**

For lambda = (4, 2, 1^q) with q >= 4:
- B subset E_j^- for j = 1, ..., q - 3  (containment, fully rigorous)
- B not subset E_{q-2}^-  (sharpness; rigorous reduction + computational
  witness for q in {4, 5, 6, 7})
- B subset E_ell^+ universally (Theorem A, May-13 evening)

At q = 3 the predicted intersection is empty so the containment is
vacuous; verified separately that dim B = 3 and supp(B) has the
expected structure.

Paper: `~/projects/proofs/2026-05-14-extended-sign-kill-42.tex` (10 pp).

## How it composed

This is the **first invocation of the recursive ladder**.  The fifth-pass
(3, 2) theorem (proved this morning) appears as an INPUT here: the
inner piece mu_A = (3, 2, 1^{q-1}) is handled by today's (3, 2) result
applied at q' = q - 1.  The hook lemma (also from this morning's paper)
handles mu_B = (4, 1^q).  The mu_C = (3, 1^{q+1}) piece vanishes by the
same column-1 leakage mechanism as in the May-20 (3, 2) paper.

Concretely:
1. **Three-branch reduction** (Theorem 9): B = (T_{n-4}+1)(T_{n-3}+1)(T_{n-2}+1) sum_X Phi_X(B^{mu_X} V_{mu_X}), proved by the same May-15/May-20 pull-through argument adapted to four R'-factors in Omega.
2. **C-piece vanishes** (Lemma 11): mu_C is a hook one row longer than mu_A, mu_B, so its j-formula sits at index n-3 rather than n-4; the rightmost (T_1+1) of R'_{n-4} annihilates the E_1^- image.
3. **Inner prefix bounds**: mu_A inherits prefix >= q - 2 from the (3, 2) recursive result at q' = q-1 (requires q >= 4); mu_B inherits prefix >= q - 2 from the hook lemma at k=4, m=q (requires q >= 4).
4. **Outer factors preserve prefix**: the three outer (T_j+1) at j in {n-4, n-3, n-2} all satisfy j > (n-8) + 1, so the May-14 fifth-pass outer-factor lemma applies.
5. **Support rule**: prefix >= q - 2 across supp(B) gives B subset E_j^- for j <= q - 3.

The sharpness reduction at j = q - 2 (Lemma 14) is structurally
identical to the May-14 fifth-pass paper's argument: if some
T in supp(B) has p(T) = n - 8 exactly, then a forced cell analysis
identifies entry n - 7 at (1, 2), and the swap argument gives the
contradiction via the off-diagonal Hoefsmit coefficient.

## Why this matters

The fifth-pass (3, 2) paper closed (3, 2) using (2, 2) as input.
Today closes (4, 2) using (3, 2) as input.  This validates the
**compositional/recursive strategy** implicit in the May-13 r-additivity
meta-theorem: each new hat_lambda row in the table inherits its prefix
bound from doubly-stripped inner pieces, each of which is its own
recursive entry.

The natural next family is **hat_lambda = (4, 3)**, lambda = (4, 3, 1^q).
This is the FIRST FULLY-RECURSIVE case: all three doubly-stripped
partitions (mu_A = (3, 3, 1^{q-1}), mu_B = (4, 2, 1^{q-1}), mu_C =
(3, 2, 1^q)) are non-hooks.  mu_A would need a (3, 3) recursive
theorem (not yet proved) but mu_B is today's (4, 2) at q-1 and mu_C is
this morning's (3, 2) at q.  The (3, 3) family has only TWO corners
(since lambda_1 = lambda_2 = 3), so it's r = 1 in the multi-corner
classification — a simpler single-branch reduction.  Sketch:

- For (3, 3, 1^q): two corners c_1 = (2, 3), c_2 = (q+2, 1).  Single
  inner piece mu = (3, 2, 1^{q-1}).  Single-branch reduction:
  B = (T_{n-3}+1)(T_{n-2}+1) Phi(B^mu V_mu).  Inherit prefix >= q - 2
  from (3, 2) at q' = q - 1.  Three outer factors preserve.  Done.

If (3, 3) goes through, then (4, 3) gets all three inner pieces
recursively, no hook input needed.

## Lesson

The recipe is now firmly established:
1. Identify the three doubly-stripped pieces mu_X for r = 2 shapes.
2. Apply the three-branch reduction (proved here in May-15 style).
3. mu_C-piece vanishes by column-1 leakage.
4. Inner prefix bounds: recursive call + hook lemma.
5. Outer factors preserve.
6. Support rule gives the E_j^- containment chain at predicted tau.

Sharpness: structural forced-cell argument + a computational witness
(42 of them per q for (4, 2)).

I'm starting to see this as a single THEOREM with many instances,
parameterized by hat_lambda.  Each new entry in the conjecture table
(May-14 evening) reduces mechanically once the doubly-stripped pieces
have known prefix bounds — and the doubly-stripped pieces are
themselves "smaller hat_lambda" entries in the same table or hooks.
The induction terminates in two ways:
- Hook leaves (mu = (k, 1^m)) — handled by the hook lemma.
- Boundary leaves (mu where the prefix bound becomes trivial) —
  vacuous statement, no work.

If this recursive structure is real, then the full extended sign-kill
conjecture (May-14 Conjecture 9, general hat_lambda) reduces to a
finite check at each hat_lambda + an inductive argument on
|hat_lambda|.  This is the natural conjectured generalization.

## What's still open

1. **hat_lambda = (3, 3)** — single-branch, recursive on (3, 2).
   Should be quick.
2. **hat_lambda = (4, 3)** — three-branch, fully recursive (no hook).
3. **Sharpness, structurally** — the "existence of boundary-prefix
   witness in supp(B)" remains computational at q in {4, 5, 6, 7}.
   A direct structural argument would need to either (i) characterize
   supp(B) exactly (would close the May-12 Catalan-support conjecture)
   or (ii) dimension-count B inside the eigenspace lattice.
4. **General hat_lambda**: with the recursive ladder validated,
   formulate and attempt the general theorem.

## Push status

**67 unpushed commits** on clio-vega/proofs (after today's commit).
PAT issue from May 6 persists --- please refresh when you can.

## Files

- Paper: `~/projects/proofs/2026-05-14-extended-sign-kill-42.tex` + `.pdf`
- Scripts: `~/projects/scratch/2026-05-14-extended-sign-kill-42/`
  - `explore_42_family.py` — main verification (dim B, supp, prefix, E_j^-)
  - `find_witness.py` — sharpness witnesses for q in {4, 5, 6, 7}
