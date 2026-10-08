# For Robin: extended sign-kill for hat_lambda = (3, 3) — containment proved (2026-05-14, seventh session)

## TL;DR

Seventh prove session of May 14, building on this morning's sixth-session
(4, 2) result.  **The extended sign-kill conjecture for
hat_lambda = (3, 3) is now proved in the containment direction at the
predicted threshold tau = q - 3, for q >= 4.**

For lambda = (3, 3, 1^q) with q >= 4:
- B subset E_j^- for j = 1, ..., q - 3  (containment, fully rigorous)
- B not subset E_{q-2}^-  (sharpness; rigorous reduction + computational
  witness for q in {4, 5, 6, 7})
- B subset E_ell^+ universally with T_ell = q*Id (May-13 evening)

At q in {2, 3} the predicted threshold is non-positive so the
containment is vacuous; verified separately that dim B = 2 throughout.

Paper: `~/projects/proofs/2026-05-14-extended-sign-kill-33.tex` (10 pp).

## New structural ingredient: r = 1 + same-row hook

This is the first r = 1 case (only two removable corners) in the
extended sign-kill program.  The corner structure forces a *new* piece
in the E^+_{n-1} decomposition that wasn't present in (3, 2) or visible
in the (4, 2) write-up:

For lambda = (3, 3, 1^q):
- 2-block Phi piece at {c_1, c_2} = {(2, 3), (q+2, 1)}: inner shape
  mu_A = (3, 2, 1^{q-1}).  Recursive on (3, 2).
- **Same-row hook piece at c_1**: SYTs with (n-1, n) at (2, 2), (2, 3).
  Inner shape mu_hook = (3, 1^{q+1}).  This is a +q-eigenvector of
  T_{n-1} (n-1, n in same row), distinct from any 2-block, with its
  own Phi_hook embedding.

The two pieces together span E^+_{n-1} = R'_n V_lambda.  This is *not*
covered by the multi-corner setup in May-20 / May-14 fifth & sixth
papers, which only describe the 2-block pieces.

The hook piece's pullback contribution to B vanishes by the May-12
hook column-1 theorem: B^{(mu_hook)}_{ell+1} V_{mu_hook} ⊆ E_1^- (needs
q+1 >= 3), and the rightmost (T_1+1) of the leftover R'^{(mu_hook)}_{n-4}
kills it.  Structurally identical to the C-piece vanishing in the (4, 2)
paper, but with a hook inner shape rather than a non-hook one.

After the vanishing, the reduction collapses to single-branch:
  B = (T_{n-4}+1)(T_{n-3}+1)(T_{n-2}+1) Phi_A(B^{(mu_A)}_{n-4} V_{mu_A}).

The prefix bound then comes from the recursive (3, 2) input at q' = q-1.

## Side discovery: gap in the (4, 2) sixth-pass paper

While working through the (3, 3) decomposition I noticed that the (4, 2)
paper's Lemma 3.1(ii) is **strictly false** computationally.  It claims

  E^+_{n-1} = Phi_A(V_{mu_A}) (+) Phi_B(V_{mu_B}) (+) Phi_C(V_{mu_C})

(direct sum of three 2-block Phi-pieces), but lambda = (4, 2, 1^q) also
has a same-row +q-piece at c_1 = (1, 4) with inner shape (2, 2, 1^q).
Verified at q in {2, 3, 4, 5}: the missed dimension equals f^{(2, 2, 1^q)}.

The (4, 2) main theorem conclusion (B ⊆ E_j^- for j <= q-3 at q >= 4)
is nonetheless computationally correct.  The gap is *closable* by the
same vanishing mechanism as in (3, 3): the missing same-row piece is
killed by the additional R'^{(2,2,1^q)}_{n-4} factor + an application
of the May-14 fourth-pass (2, 2) extended sign-kill theorem (which
puts B^{(2,2,1^q)}_{n-3} V inside E_1^-).

I marked this in the (3, 3) paper as Remark 4 and Discussion §6.3.
A companion erratum / extension to the (4, 2) paper will close the gap
explicitly.  Whether to publish it as a separate note or fold it into a
revision of the sixth-pass paper is for a later session — for now the
companion note pending.

## Updated table of proved hat_lambda rows

| hat_lambda | predicted tau | status                                              |
|------------|---------------|-----------------------------------------------------|
| (2, 2)     | q - 1         | proved (May-14 fourth pass)                         |
| (3, 2)     | q - 2         | proved (May-14 fifth pass)                          |
| (3, 3)     | q - 3         | **proved (this paper)**                             |
| (4, 2)     | q - 3         | proved with same-row gap to close (May-14 sixth)    |

Next natural target: hat_lambda = (4, 3), the first FULLY recursive
three-branch case (all three doubly-stripped pieces are non-hooks,
each handled by a recursive input from the table above).

## What composed here that didn't before

This is the third recursive use of an extended sign-kill theorem as
INPUT to a proof of a strictly larger hat_lambda (after (3, 2) -> (4, 2)
in the sixth pass).  Now (3, 2) -> (3, 3) using the same recursive
input but applied with a fundamentally different reduction topology
(single-branch r=1 vs three-branch r=2).

The "table of recursive ladders" is filling out: every hat_lambda entry
in the conjecture so far either reduces mechanically to smaller entries
(plus hook inputs) or terminates as a hook leaf.

## Push status

**68 unpushed commits** on clio-vega/proofs (after today's commit).
PAT issue from May 6 persists — please refresh when you can.

## Files

- Paper: `~/projects/proofs/2026-05-14-extended-sign-kill-33.tex` + `.pdf`
- Scripts: `~/projects/scratch/2026-05-14-extended-sign-kill-33/`
  - `explore_33_family.py` — main verification (dim B, supp, prefix, E_j^-)
  - `check_reduction.py` — two-piece decomposition of E^+
  - `check_samerow_contribution.py` — same-row tableaux exist in supp(B)
    in both (3, 3) and (4, 2) cases (motivating the gap fix)
