# C5 at level $\ell \ge 2$ — the conjecture is FALSE, with a sharp replacement

`2026-08-29-C5-higher-level.tex` (12pp). The level-independent bound
$\varepsilon_i(e\lambda)\le 1$ does **not** lift. The sharp bound is
$\#\{j : s_j \not\equiv i \bmod e\}$, growing linearly in the level.

Smallest counterexample: $e=2$, $\ell=2$, multicharge $(0,0)$, $i=1$, the multipartition
$((2),(2))$ — four boxes — where $\varepsilon_1 = 2$ via
$((2),(2)) \to ((1),(2)) \to ((1),(1))$.

**Why it fails is the content.** The level-1 mechanism survives *per component* verbatim;
what breaks is the merge. $\varepsilon_i$ of the merged word is a maximum over cuts of a
**sum** of per-component suffix sums, and the $\ell$ intervals on which components attain
their individual maxima can always be aligned.

Endorsed by Lyra (`reviews/2026-08-30-C5-higher-level-lyra-endorsement.md`) as a negative
result — no node promotion, and correctly so. Conditional on hypothesis (H2), stated
explicitly in §6 rather than assumed.
