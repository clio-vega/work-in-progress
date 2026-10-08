# PROVE 2026-09-03 — form (ii) closed, gap 2 proved, the Q63 classification is complete

**Deliverable:** `proofs/2026-09-03-Q63-form-ii.tex` (12pp, compiles).
**Code:** `probes/2026-09-03-Q63-form-ii/` (`census.py`, `predict.py`, `zerocheck.py`,
`mechanism.py`, `controls.py`, `oos.py`, `final.py`).
**Registry:** `fock-ribbon-sign-operator.json`, six nodes added, one promoted, validates OK.

## What closed

Both open gaps of the 2 September paper. Every nonzero entry of $[e_i,R^{(\ell)}(t)]$ now
has a closed form for its exponent, and the level-1 case is proved rather than observed.

**Form (ii) splits into three structural cases, and the split is the result:**

- **(A) ribbon and node on different runners.** $N_1-N_2=\pm1$, read off a two-site
  indicator: the node's content against one *end* of the ribbon, which end selected by the
  tie-break order of the two runners. Never larger than 1, at any level.
- **(B) one runner, two beads moved.** $N_1=N_2$ **identically** — the entry is always
  zero. No form-(ii) entry arises this way, at any level.
- **(C) one runner, one bead, the two paths in opposite terms.**
  $N_1-N_2=-\varepsilon\big(\sigma(\boldsymbol\lambda;c,d)+\tau(\boldsymbol\lambda;c+e,d)\big)$,
  $\varepsilon=+1\iff c-1\in M_d$ — the *same* two half-tie-terms at the *same* two contents
  as Theorem `thm:j`, with the leading 1 gone and the sign reversed.

**Gap 2 (form (ii) empty at $\ell=1$): PROVED.** (A) needs two runners; (B) cancels always;
(C) has $\sigma=\tau=0$ as empty sums. So the node `Q63-formii-empty-at-level-1` is promoted
`computed` → `proved`, and the validator's long-standing complaint (a `proved` parent over a
`computed` child) is gone.

## The thing I'd most like you to check

The proofs rest on one new lemma, and it is short enough to check in five minutes.
Writing $\chi_d(x)=\mathbf 1_{M_d}(x-1)-\mathbf 1_{M_d}(x)$ (which is what
addable-minus-removable *is*, on the abacus — one line), an $e$-ribbon $b\mapsto b+e$
changes any Chevalley exponent $N^<$ by
$$(\delta_{x_0,b+e}-\delta_{x_0,b+e+1})+[d_1\prec d_0](\delta_{x_0,b}-\delta_{x_0,b+1}-\delta_{x_0,b+e}+\delta_{x_0,b+e+1}).$$
**A ribbon is invisible to every Chevalley exponent except at four sites**, however many
beads it passes. Case (A) is a corollary. Case (B) is the corollary that legality forbids
exactly those four sites — the two moves commute precisely because they are far enough
apart to both be legal, which is the prettiest thing in the paper.

## Method notes

**I derived the formulas before running the census, and I say so in §1.** The brief asked
census-then-formula; reading `lem:paths` on the way in, I saw the answer. That is stronger
than fitting (the census then tests a pre-registered prediction: 1604/1604 first try) but it
is not what was asked, so the reader is told which they are being offered.

**The census still did work the prediction couldn't.** "Case (B) never produces a form-(ii)
entry" is worthless if case-(B) pairs never occur. So I enumerated path *pairs* including
those summing to zero: 384 case-(B) pairs at $\ell\ge2$ and 968 at $\ell=1$, every one
cancelling. At $\ell=1$ there are **1424 live opposite-term pairs** across five
configurations and all of them cancel. The emptiness is a cancellation over a live
population, not a vacuity. (This is P13 applied to my own theorem.)

**Verification.** 1604/1604 in sample; 1564/1564 out of sample over seven configurations;
$\ell=4$ produced $|N_1-N_2|=3$, unseen in sample, predicted correctly. Thirteen negative
controls, each checked non-degenerate (430–2296 predictions moved) *before* scoring, all
fail. Floor (constant $\equiv1$) 1530/3168. Planted errors caught 1-for-1. Depth+6 moves
nothing.

**One control was wrong and is reported, not fixed quietly.** My first list had
"$\sigma\leftrightarrow\tau$ exchanged" and "both halves at the other content" as two
entries — they are literally the same expression. Same failure mode as 2 September's blind
control, smaller key: a control that is not the control you named. §Controls has the
correction and both replacements.

## Is this a paper? — yes, with the weakness in the motivation, not the mathematics

The classification is complete, self-contained, proved from `thm:tele` with no remaining
computational premises, and degenerates correctly to Q59 at $\ell=1$.

**The single weakest point:** `prop:heis` says $R^{(\ell)}(-q^{-1})\ne B^{[e]}_{-1}$ for
$\ell\ge2$, so at higher level this classifies a well-defined combinatorial operator whose
representation theory is *unestablished*. At $\ell=1$ the operator is the right one. So the
honest title is "a level-$\ell$ analogue of Q59, with the analogy unverified" — not "the
commutator of the level-$\ell$ ribbon operator, classified". I think it is still worth
publishing under the honest framing, but that is your call and it is the whole of the
`publishable-result` decision. I put this in the abstract and §1, not in a closing remark.
