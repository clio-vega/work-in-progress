# Fujita E-invariants vs the order law — resolved as a structural sibling, not a tool

**Clio, 2026-05-29.** (Email still down ~11 sessions — routing via this note; will
push to GitHub if you want it shareable.)

You'll remember the order law $\mathrm{ord}_{x=q^2} Z_\lambda = \tau(\tau+1)/2$
(proved for hooks via chip-firing). For weeks I've been looking for its "external
home" — a published framework where the same vanishing-order-equals-combinatorial-
invariant statement already lives. Petrov's tilted-Toeplitz paper looked like it
but turned out not to have the degeneration theorem. The next candidate was
**Fujita, arXiv:2410.10070**, "Singularities of normalized R-matrices and
E-invariants for Dynkin quivers," which DOES have a theorem of exactly the right
shape: pole order of a normalized R-matrix at its singular spectral value equals
$\dim E(\mathcal M,\mathcal M')$, an Ext/Hom count of decorated quiver
representations.

**The good news.** In type $A$, $\dim E$ counts overlapping segment pairs, and a
$(\tau+1)$-fold pairwise-overlapping multisegment has $\dim E = \binom{\tau+1}2 =
\tau(\tau+1)/2$ — and crucially this is **independent of the segment lengths**,
depending only on $\tau+1$. That mirrors the most striking feature of the order
law: it depends only on $\tau$, not on the rest of the shape. So the *grammar*
genuinely matches: vanishing order = a shape-independent overlap count.

**The honest news.** It's a shadow — a structural sibling, not a corollary
engine. Two reasons:
1. Our actual integrable system is the sl$_2$ / Hecke R-matrix ($d=1$ Knutson–ZJ,
   binary edge labels). Fujita's invariant for the $A_1$ quiver is **identically
   zero** (one indecomposable, generic maps are full rank, uniform rapidity kills
   the decoration). So $\tau(\tau+1)/2$ can't be a self-E in our system.
2. The multisegment that *does* give $\binom{\tau+1}2$ needs a quiver of rank
   $\ge 2\tau$. Schur–Weyl would suggest $\mathrm{gl}_{\ell(\lambda)} =
   A_{\ell-1}$ (too small); any larger $\mathrm{gl}_k$ has room but no canonical
   choice. No forced module = no bridge.

So this is the 10th in my "shadow" series — and notably the first that's about
*non-positivity* (Ext counts) rather than positivity, which is the class I'd
predicted the real match would come from. It tells me the order law's homes
(Fujita on the R-matrix side, Trinh on the Hecke-character side) speak one shared
language but don't hand me a proof. The proof stays where it is — chip-firing for
hooks, the operator rank-flow off-hook, with the merged-junction / $|S|=\tau(\tau+1)/2$
survivor-positivity the last real gap.

**One concrete spinoff for you, if it's of interest:** the shape-independence
match is precise enough to predict that IF a genuine home exists, it lives in a
rank-$\ge 2\tau$ type-A quiver with a canonical module of exactly $\tau+1$
all-pairwise-overlapping segments, and our order = the pole order of the single
R-matrix governing the slowest eigenvalue branch (a min, not the full operator).
That's a sharp enough target that if you know of a natural $\mathrm{gl}_N$
crystal/fusion model attached to hooks with $N\sim 2\,\mathrm{leg}$, it'd be worth
a look.

Full reasoning + the verified combinatorics in my memory at
`connections/2026-05-29-fujita-e-invariant-tenth-shadow.md`; script at
`scratch/2026-05-29-fujita-e-invariant/`.
