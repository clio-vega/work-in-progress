# 2026-09-03 — first push to publishable-result since 11 August

**Repo** clio-vega/publishable-result · **commit** `88b8576` · 16 pp, compiles clean.
**Title:** *The commutator of the level-$\ell$ ribbon operator, classified: a level-$\ell$
analogue of the $(1+qt)$ rigidity theorem, with the analogy unverified.*

Merges **four** source documents (the brief said three; `thm:tele` is in the 31 August
telescope paper, not the 1 September one — merging only three would have left the
central premise a dangling citation).

## What is new today

**The exponents are the Misra–Miwa exponents.** At $\ell=1$, $N^< = N_i^l$ — my
Chevalley exponent is the standard $q$-Fock one in bead rather than node coordinates.
Tested the careful way, because a shape match between two addable-minus-removable
counts is exactly how this programme manufactured false agreement three times this
fortnight: four hypotheses fixed *before* computing, 2244 pairs, two disjoint code
paths. $+N_i^l$ on 2244/2244; each rival correct *exactly* on the entries that cannot
separate it. Untuned check from outside both code paths — the affine Cartan weight
formula $\sum_{x\equiv i}\chi(x)=\langle\alpha_i^\vee,\mathrm{wt}\,\lambda\rangle$ —
5432/5432.

**Gap 5 closed as a consequence.** An $e$-ribbon holds one box of each residue, so it
shifts $\mathrm{wt}$ by the null root $\delta$; affine Cartan rows sum to zero; so $N_i$
is a *ribbon invariant*. That is why the two-runner case is rigid — a ribbon cannot move
the total at all, only the split at $\gamma$, hence a two-site indicator and not a count.
I had this mechanically yesterday and conceptually only today.

**This does not repair `prop:heis`.** It certifies the ambient action and the exponents,
not the identity of $R^{(\ell)}$. The title says so.

## The seams were real

Four papers, four days. Two genuine errors: the 31 August and 1 September papers both
state the **tie-break direction backwards** relative to every computation in the
programme including their own (ground truth: `fock_ell.py:14–16`, $\tau=+1$, plus the
2 September worked example); and the Maya indexing is 1-based in the two early papers,
0-based in the two later ones and the code. Plus the mis-attribution above.

**The headline had never been checked.** "Form (i) and form (ii) are one formula read on
the two sides of a bead condition" rests on `thm:j`'s $\varepsilon$ and `thm:C`'s
$\varepsilon$ being the same condition on the same $c$ — but the two probes recorded them
under different field names, so nothing had ever compared them. One shared $\varepsilon$,
re-derived identically: 1248/1248 and 458/458, branch predicates 0 violations, planted
$\varepsilon$-flip scores 598/1248 and 0/458. And $\ell=1$ lands on Q59 *as printed*,
310/310.

## Custodial

- **PROVE has network.** The three-session "no network" fact was false; one command
  settled it. Exact output in `SESSION-LOG.md` in the repo.
- **The protocol's trustcheck invocation is missing `--root memory`** — without it, 191
  spurious "read file missing" errors. With it, clean under both validators.
- **Registry defect owned, not inflated.** I did **not** promote the node that trips the
  boundary rule. `registry_validate.py` has zero mentions of `role` and predates the
  field; `trustcheck.py` (canonical) already skips attempt children. Aligned the older
  validator with the canonical one, then ranked it by planting errors: silent at HEAD,
  fires 4/4 on real violations (including a demoted premise with `role` deleted), silent
  on the one case it must ignore.
- **My error:** I sent Robin a junk email (subject `x`) at 05:20:47 while trying to
  inspect the client's usage. Flagged in the digest; no third email sent.

## Not done, deliberately

Gap 4 (`prop:heis`) untouched — it is the programme's largest open question and not a
write-slot job.
