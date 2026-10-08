# PROVE 2026-08-30 — Q55 closed, and half of it was already published

**One-line:** transposition reverses the $e$-ribbon height grading; that answers Q55, but
the $q$-specialised form turns out to be Leclerc–Thibon Prop 7.10 at $k=1$, which I found
on disk *after* proving it. The genuinely new pieces are elsewhere and, I think, better.

## What I proved

**Theorem.** $\Omega N_e^{(h)}\Omega = N_e^{(e-1-h)}$, where $\Omega|\lambda\rangle=|\lambda'\rangle$
and $N_e^{(h)}$ counts $e$-ribbon additions of height $h$. Two lemmas: an $e$-ribbon spanning
$r$ rows and $c$ columns has $r+c=e+1$; transposition is a bijection on ribbon additions
exchanging $r$ and $c$.

Everything about $P_e$ follows from the functional equation $\Omega R_e(t)\Omega = t^{e-1}R_e(1/t)$:
- $\Omega P_e \Omega = (-q)^{e-1}B_{-1}^{[e]}$, so **the coefficientwise bar involution on this
  operator is transposition** (up to the spin scalar, which disappears after the LLT recentering).
- Q55: $(q-q^{-1})C_e^{(1)} = P_e - (-q)^{-(e-1)}\Omega P_e\Omega$. A coboundary — for the
  order-2 twisted conjugation, named explicitly. Not group cohomology, and I say so.
- **Negative result worth having:** the hoped-for reading "$C_e^{(1)}$ is an artifact of an
  inflation convention" is *false*. $C_e^{(1)}=0$ iff $e=1$. Only the scalar is a convention.

## The attribution, which is the part I want you to see

The $q$-specialised corollary is **not new**. It is Leclerc–Thibon, ASPM 28 (2000), Prop 7.10
at $k=1$, quoted verbatim in Lam `math/0310250`. This morning's BROWSE had already flagged
it and left `lam.tex` in `/tmp/browse/`. I proved the theorem first, then read the source,
then built the dictionary rather than assuming it — their spin of a single ribbon is its
height (lam.tex:429–436); $\mathcal V_k = \sum(-q)^{-s}$ (lam.tex:848) so $\mathcal V_1 = B_{-1}^{[e]}$,
**not** $P_e$; a single ribbon is both a horizontal and a vertical strip so
$\tilde{\mathcal V}_1 = \mathcal V_1$. The scalars then match exactly.

That check is the thing. Reading their statement at the level of shape, I would have said
"$\mathcal V$ is my $P_e$" and the exponent would have come out $(-q)^{e-1}$ against my
$(-q^{-1})^{e-1}$ and I would have had a phantom discrepancy to explain. One line of their
paper prevented it. This is the fifth time in three weeks a shape match nearly became a
claimed identification.

Two questions from this morning's reading log are settled as a by-product: **Q56** — my
linear $\Omega$ is *not* their involution; theirs is $\Omega_{\rm bar}=\text{bar}\circ\Omega$,
and the bridge is $B=\overline{P_e}$. **Q57** — yes, $r+c=e+1$ *is* the spin/cospin exchange
for one ribbon. Conversely their $k\ge2$ statement is stronger than anything I proved.

## The new parts

1. **A structural proof of the $(q-q^{-1})$-divisibility of $[e_i,P_e]$, independent of C4.**
   Bar is a ring automorphism and sends $B\mapsto P_e$, so $[\bar e_i,P_e]=0$; subtract, and
   $e_i-\bar e_i$ is entrywise $-(q-q^{-1})[N]_q$. Cross-check: $[e_i,C_e^{(1)}]=[E_i,P_e]$,
   so the C4 route and the bar route agree.

2. **The registry's "T3: the quotient is linear in $q$" is the wrong statement, and the right
   one is much better.** Every nonzero entry of $[e_i,P_e]$ and $[f_i,P_e]$ is exactly
   $\pm q^m(q-q^{-1})$ — a *unit monomial* quotient (2683 entries, $e\le6$, $|\lambda|\le10$,
   0 exceptions). And I **proved the reduction**: with $\Phi(t)=([x,R_e(t)])_{\nu\lambda}$, the
   single vanishing $\Phi(-q^{-1})=0$ forces $|H|\ne1$ and, given a two-element support with
   unit-monomial entries, forces every coefficient — quotient $=\pm q^m[d]_q$, monomial iff
   the gap $d=1$. **All the $q$-arithmetic is forced by one vanishing; what is left is a purely
   combinatorial support statement about $[e_i,N_e^{(h)}]$.** That is the next session.

3. **The vertical/horizontal dichotomy explained at level 1.** Within the addable/removable
   $i$-nodes the column strictly decreases as the row increases, so transposition *reverses*
   the signature word; and the word of $e\lambda$ is exactly $A^\delta(RA)^m$. So
   $\varepsilon=1$ (prefix max) and $\varepsilon^{\rm op}=0$ (suffix max): **the dichotomy is
   prefix-max versus suffix-max of the same $\pm1$ walk.** 490 explicit instances confirm
   $\Omega$ is not a crystal morphism, so this is not a vacuous equality.

4. **Lyra's C5 gap (3b) is closed**, from the same computation. The addable node of row $r$
   and the removable node of row $r-1$ are one inequality read twice — removability looks one
   row down, addability one row up, the index shift cancels. Divisibility by $e$ is used *only*
   to align the two residues. Written into `2026-08-11-C5-gerber-bicrystal.tex` as a lemma with
   proof; recompiles clean. **Please tell Lyra it is done** — she found the seam unasked and
   should hear that it held.

## Housekeeping

- Also found: a label collision. In `2026-08-12-commutation-defect.tex`, T2/T3 are the $q=1$
  and $(q-1)$ statements (proved there); the $(q-q^{-1})$-divisibility is *Conjecture 4*,
  flagged empirical. The registry and PROVE.md reuse "T2/T3" for the latter. No result
  affected. Corrected in the registry.
- `proofs/2026-08-30-Q55-transpose-twist.tex` (+ pdf, 12pp), probes in
  `probes/2026-08-30-Q55-transpose/`, registry updated and validating.
- **Nothing here needs Uglov Prop 3.16 and nothing here is level $\ge2$.** I have stated the
  level-1 scope explicitly in the paper, including which parts will and will not lift.

Not pushed to GitHub yet — this was a prove session with email and browsing off. Say the word
and I will push the tex+pdf to `work-in-progress` and send the pair to Lyra and Rick.
