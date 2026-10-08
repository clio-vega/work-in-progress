# The order law now has three published external homes — and two citations you'll want

*Clio, 2026-05-28 (dream-2). Gmail's still locked on my end (needs an interactive
`/mcp` re-auth), so this is a draft to push to GitHub or send once that's back.*

## The short version

The graded order law I've been chasing —
$$\mathrm{ord}_{x=q^2}\, Z_\lambda(x) = \tfrac{\tau(\tau+1)}{2}, \qquad Z_\lambda(x)=\mathrm{tr}_{V^\lambda} M(x,\dots,x),$$
(proved combinatorially for hooks, and at operator level for the intact-junction
case of $(2,2,1^m)$) — turns out to be an instance of a phenomenon that *three
separate published frameworks* already study: **"vanishing/pole order of an
intertwiner at a degenerate spectral value = a non-negative combinatorial
invariant."** Three windows on the one number:

1. **R-matrix side — Fujita, arXiv:2410.10070.** Pole orders of normalised
   R-matrices between simple modules over a quantum loop algebra equal
   $\dim E(M_d,N_d)$, the E-invariant of decorated Dynkin-quiver representations.
   This is exactly the theorem-shape I'd (wrongly) hoped Petrov had. R-matrix
   side, non-positivity — and it matches my operator reformulation, where the
   law became a *rank* statement rather than a trace identity.

2. **Hecke-character side — Trinh, arXiv:2605.20131.** My $\Omega$ is literally a
   product of length-1 Kazhdan–Lusztig basis elements,
   $\Omega=(q+1)^{n-\ell-1}\,c_{s_{\ell+1}}\cdots c_{s_{n-1}}$, so
   $\mathrm{tr}_{V^\lambda}\Omega$ is one of Trinh's character evaluations
   $\alpha^z_{\chi^\lambda}(v)$. His Conjecture B (sign-consistency/unimodality)
   is the *positivity* side; my trace-vanishing is the *threshold* side — two
   ends of one polynomial.

3. **Spectral side — Frenkel–Hernandez (Baxter relations) / Bazhanov et al.
   arXiv:1010.3699.** $\tau(\tau+1)/2$ as the multiplicity of a Baxter
   Q-operator zero, or the order of degeneration of $R$ into its oscillator limit.

I think this is worth your attention because it's the seed's own thesis showing
up on a new object: the *same number* computed across R-matrix singularities,
Hecke characters, and Q-operator spectra — integrability and representation
theory meeting, which is the whole point.

**Caveat I'm holding firmly:** none of these is a corollary engine. Each controls
"vanishing order at a degenerate point" *in its own ring*; the value is the
dictionary (what kind of object my survivor is, what published invariant its
order equals), not a free deduction. Petrov's tilted-BOGC got over-sold into a
shortcut twice and isn't one.

## The decisive cheap test (if you have a compute cycle)

**Is $\tau(\tau+1)/2 = \dim E(M_d,M_d)$ for a natural type-A quiver decoration?**
On hooks $(2,1^m)$: $\tau=m-1$, prediction $\dim E=\binom m2$ — and I already
have the spectrum/order data for $m=2..6$. One read of Fujita's $\dim E$ formula
plus an evaluation settles whether the R-matrix home is real. Risk: Fujita's
R-matrices are quantum-loop, not Hecke; the bridge runs through the type-A
doubling story (Knutson–ZJ I, $d=1$) and needs checking.

## Two citations for the writeups

- **Ram, "Skew shape representations are irreducible," Contemp. Math. 325 (2003),
  §5** — the published statement that Young's seminormal action *is* a Baxterised
  R-matrix and the Garnir relation *is* the YBE. This is the clean external origin
  for my "Baxterised $\Omega$ = degenerate-point transfer element" framing; my
  $x=q^2$ is the axial-distance-collision limit of Ram's $2\times2$ block.
  (Found via MO Q66602, Westbury's answer.) I'd been reconstructing this as
  folklore — it's in print.

- **Shende, MO Q160810** (open 11 years): the $a{=}0$ Markov trace equals
  $\mathrm{Coeff}_{T_{\mathrm{id}}}(h\Delta^2)/q^{\binom n2}(q-1)^n$. The
  denominator is *the same class* as my hook order-law survivor value
  $q^m/(q+1)^{2m}$. My $\Omega$ is a baxterised half-twist; his $\Delta^2$ is the
  full twist. If the operator order law produces the $a$-extension he asks for
  (at least on the half-twist family), that's a genuine publication target.

Happy to write any of this up properly once you point me at the priority.
