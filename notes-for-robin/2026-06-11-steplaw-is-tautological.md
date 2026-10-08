# The d=4 "step law" is circular — even-|J*| needs the involution, not the step

**Clio, 2026-06-11 (prove session)**

Robin — short version: I was asked to prove the M-half of the step law (M★),
"$v_2(M_{j+8})-v_2(M_j)=-4$ on pure-M toggle pairs of $J^*$," billed as *the* load-bearing fact
behind even-$|J^*|$. **I found it's a tautology, and that this matters.**

### What's true

If $\{j,\,j+2^a\}$ are *both* in $J^*$ (both Newton-minimal), then because $\mathrm{val}$ is constant
on $J^*$ by definition,
$$0=\mathrm{val}(j+2^a)-\mathrm{val}(j)=2^a+2\Delta v_2(\mathrm{bin})+2\Delta v_2(M)
\ \Longrightarrow\ \Delta v_2(M)=-2^{a-1}-\Delta v_2(\mathrm{bin}).$$
That's the whole step law — one line, no input about $M_j$ beyond "this index is in $J^*$." The
"$168/168$ verified" was checking $0=0$ (plus $\Delta v_2(\mathrm{bin})=0$, which is a separate
Kummer fact). So **proving (M★) does nothing for even-$|J^*|$.**

It's not salvageable as a non-circular statement: it's *false* if you drop the "$j+8\in J^*$"
hypothesis (toggling $j=2$ in $\lambda=(10,4,4,2,2)$ gives $-2$, not $-4$), and $j\in J^*$ does not
force $j+8\in J^*$ ($2470$ counterexamples, $m\le12$). The $a=3$ law fires *exactly* when $a$ is
already a generator of the box — which is the thing we want to prove.

### What even-$|J^*|$ actually is

Existence of a **fixed-point-free involution** on $J^*$ — equivalently $|J^*|$ a power of two
(empirically $\{1,2,4\}$), equivalently ruling out $|J^*|\in\{3,5,7,\dots\}$. A pairwise consistency
relation (the step law) can't manufacture a partner for a lonely index, so it can't exclude odd
sizes. The lever has to act on the whole generating polynomial.

### The right lever (non-circular), and where it stops

The engine's **exact lift** $\Phi(z)=\sum_r\binom mr 2^rR_r(1+z)^{m-r}$ is the correct object: a
$2$-adic filtration of the whole polynomial. It *proves* the box at the leading layer when
$\chi^\lambda(2^m)$ is odd. I verified that on **all 1624 ties** ($m\le12$), $\Phi/2^e\equiv
z^{j_0}(1+z)^g\bmod2$ with $g\ge2$, so the *coarse* Newton locus is an even box. Two honest gaps
remain: (i) coarse$\Rightarrow$sharp $J^*$, (ii) proving $g\ge1$ on ties from the $e_2\bmod2$ layer
(the engine collapses $p_1^2\equiv p_2$ at the top layer but there's no analogous collapse one layer
down). Same wall as 06-10 — but now I'm certain *this* is the wall, because the step-law detour is
empty.

### Three tools I proved on the way (verified $159/159$, exact)

- $D_j:=2^jM_j=\langle s_\lambda,p_1^{2(m-j)}(p_1^2-p_2)^j\rangle$, so $v_2(M_j)=v_2(D_j)-j$;
  $D_j$ is the signed binomial transform (Mahler coefficients) of the character vector $\chi_b$.
- Dual exact lift $A_\lambda(x)=\sum_r\binom mr R_r(x+2)^r$ (companion to the $(1+z)$-lift).
- $M_j=\sum_\mu(\#\text{vertical-2-strip chains }\lambda\to\mu)\,f^\mu$ — a positive SYT-count model
  (explains why no global $v_2(M_j)$ formula: it's $v_2$ of a positive sum).

Route B (Ayyer–Kumari) stays pruned — wrong mod-4 branch, $(2,2)$ is a $4$-core, and a factorisation
governs magnitudes not the Newton-locus involution.

Doc: `proofs/2026-06-11-steplaw-M-half.md`. Code: `code/jobM_explore.py`.

Not a win on the stated target, but I think a genuine course-correction: we were polishing a
tautology. The next prove session should attack the *coarse$\to$sharp box* directly via the exact
lift, not the step law.
