# The publishable one is on your thesis territory — three sources name the same gap

**For:** Robin. **Written:** 2026-09-19 (DREAM c2); **gloss corrected at source, WAKE 2026-09-20.** *Not yet emailed* — the 09-19 digest went
out at WAKE c2, so this is the lead item for the next digest.

## The short version

Three independent sources, none citing the others, name the same open problem, and it sits on
the **cylindric** path — your masters-thesis territory:

1. **Wang–Zhang–Zhang, `arXiv:2401.14632`, Problem 5.2** — they prove cylindric skew Schur
   functions have **M-convex support** (Cor 4.9) and then ask, in print, for a **combinatorial
   proof from the cylindric tableau side**. Their stated reason (attached to the companion
   Problem 5.1, which 5.2 is posed as "similar to"): their own route leans on **Lam's Cor 8.5,
   "a deep result"**, and they want a direct proof from the definition. So the target is a
   proof that *bypasses Lam* — which is a checkable success criterion, not just a wish.
2. **MathOverflow 424766** (Per Alexandersson, June 2022) — asks for a Kostant-style
   alternating-sum formula for **cylindric/skew Kostka numbers**. **Zero answers in four years.**
3. **symmetricfunctions.com, "Cylindric Schur polynomials"** (Alexandersson) — notes that a
   positive combinatorial rule for **toric-Schur / Gromov–Witten** coefficients is still open,
   and points at **Korff (CMP 2020)** and **Korff–Palazzo (Alg. Comb. 2020)** as the integrable
   way in.

All three want the same missing ingredient: a **local move on cylindric tableaux** transparent
enough to prove a global structural statement. The M-convex exchange axiom is "move one box
from row `i` to row `j`", which on a cylindric skew tableau is a **two-site move on the Maya
diagram** — the technique that has already paid three times for me (Q59, Q63-ii, Q76). And
`transfer_operators.py` already found that **Kostka matrix inversion**, not hook-content
evaluation, is the right computational strategy, which is the shape of what MO 424766 asks for.

I verified the thing that makes this a contribution rather than a translation: **WZZ's existing
proof has no integrable content at all.** Zero occurrences of *transfer matrix*, *vertex
model*, *Yang–Baxter*, *R-matrix* or *toric Schur* in their source; it is greedy
horizontal-strip filling of a `(k+1)`-core plus dominance triangularity.

## The correction you should know about, since I sent you the claim yesterday

Yesterday's note said free-fermion six-vertex partition functions **fail** M-convexity, and
suggested that was a fact about free fermions. **That is retracted**, by my own hand, in two
steps recorded in the registry:

- I was taking the support in the **doubled** alphabet `Z^{2n}` while my own row-degree lemma
  pins it to the graph `Γ = {(α, c−α)}`. On a graph almost no exchange is legal, so the
  "failures" were partly counting my own parametrisation.
- The repaired statement is a clean theorem: for `S ⊆ Γ_c`, **`S` is M-convex ⟺ its
  `x`-projection is an integer box**, hence `supp(Z)` is M-convex **iff the rows decouple**.
  Since a transfer matrix exists precisely to *couple* rows, M-convexity on that
  parametrisation is a **triviality condition** — it says nothing about free fermions.
  (`proofs/2026-09-19-c2-mconvexity-on-the-graph.tex`, registry node `mconvex-iff-box` at
  `proved`, https://github.com/clio-vega/proofs/blob/main/2026-09-19-c2-mconvexity-on-the-graph.pdf)

Please do **not** cite `2026-09-19-c1-lorentzian-obstruction.pdf` as "free fermions are not
M-convex". The registry node carries the caveat with the superseded text preserved.

## One 22-year-old paper you may find as interesting as I do

**Danilov–Koshevoy, `math/0409447`, "A simple proof of associativity and commutativity of
LR-coefficients (or the hive ring)" (2004)** — a **discrete-convexity** proof of the hive
ring's ring structure, with one Semantic Scholar citer and that one spurious. My seed question
is *why* LR coefficients admit so many independent combinatorial interpretations; this is a
candidate **reason**, and it has been sitting uncited for 22 years. I found it only by running
two citation censuses with **different** convexity anchors (HMMS vs Murota): 5 contacts and 6
contacts, **intersection zero**.

## The standing ask, unchanged

`CYCLES_PER_DAY=1`. The weekly window has ~32 of ~38 sessions spent with ~3 days left; the
ungated floor of 6 sessions/day means it dies around 09-20/21 regardless of what I choose to
write. It is the only lever that closes the gap and it is not inside this container.
