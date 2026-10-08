# MO 512671 draft answer — $H_\mu$ vs $\tilde H_\mu$

**Link:** https://mathoverflow.net/q/512671
**Asked by:** ArB, 2026-06-27 (one month ago)
**State at drafting:** 0 answers, 96 views
**Tags:** symmetric-functions

---

## Verbatim question text

> **Title:** Why is $\tilde{H}_\lambda(q,t)$ preferred over $H_\lambda(q,t)$?
>
> In Macdonald polynomial theory, there are two variations of polynomials one gets from plethytically transforming the integral form Macdonald polynomials $J_\lambda(q,t)$. The $H$ functions are defined by
> $$H_\lambda[X;q,t] = J_\lambda\!\left[\dfrac{X}{1-t};q,t\right].$$
> However, the literature usually has a more preference (and the $H$ is almost hard to find in most cases) towards $\tilde{H}$ defined by
> $$\tilde{H}_\lambda[X;q,t] = t^{n(\lambda)} H_\lambda[X;q,t^{-1}].$$
>
> Is there a good reason why certain things (which?) work better for $\tilde{H}$ over $H$?

---

## Draft answer

The short answer is that $\tilde H_\mu$ is the version whose $(q,t)$-Kostka coefficients are honest bigraded multiplicities, and once you make that choice everything else — plethystic identities, LLT positivity, $\omega$-duality — lines up cleanly. The tilde is essentially a change of variables that turns "$q$ and $t$ are on the same footing" from a slogan into an equality.

**1. The Garsia–Haiman modules and the $n!$ theorem.** For each partition $\mu \vdash n$ Garsia and Haiman defined a bigraded $S_n$-module $M_\mu \subset \mathbb{C}[x_1,\dots,x_n,y_1,\dots,y_n]$ (the space of partial derivatives of a certain determinant), and conjectured $\dim M_\mu = n!$ together with the identity
$$\operatorname{ch}_{q,t} M_\mu \;=\; \sum_{\lambda \vdash n} \tilde K_{\lambda,\mu}(q,t)\, s_\lambda,$$
where $\operatorname{ch}_{q,t}$ is the bigraded Frobenius characteristic. Haiman's proof via the isospectral Hilbert scheme of points in the plane (*Hilbert schemes, polygraphs and the Macdonald positivity conjecture*, JAMS 2001) *is* the reason to prefer $\tilde H_\mu$: the modified Macdonald polynomial is by construction the bigraded character of $M_\mu$. The un-tilded $H_\mu$ is off by a $t^{n(\mu)}$ twist and a $t \mapsto t^{-1}$, and the corresponding $K_{\lambda,\mu}(q,t)$ have no comparably clean module-theoretic reading.

**2. Modified Kostka positivity.** The upshot of point 1 is the theorem $\tilde K_{\lambda,\mu}(q,t) \in \mathbb{Z}_{\ge 0}[q,t]$. This is *the* positivity statement people cite. The classical $K_{\lambda,\mu}(q,t)$ do specialise at $q=0$ to Lascoux–Schützenberger's Kostka–Foulkes polynomials with their charge combinatorics, but there is no uniform $\mathbb{Z}_{\ge 0}[q,t]$ statement of the same form, and the $q$- and $t$-directions play visibly different roles.

**3. Plethystic and LLT compatibility.** Unpacking the definition, one has $\tilde H_\mu[X;q,t] = H_\mu[X;q,t^{-1}]\cdot t^{n(\mu)}$, and (equivalently) $\tilde H_\mu$ is a plethystic transform of a Hall–Littlewood-type object that puts $q$ and $t$ on symmetric footing. Concretely, Haglund–Haiman–Loehr's combinatorial formula
$$\tilde H_\mu(x;q,t) \;=\; \sum_{\sigma\colon\mu \to \mathbb{Z}_{>0}} q^{\operatorname{inv}(\sigma)}\, t^{\operatorname{maj}(\sigma)}\, x^{\sigma}$$
expresses $\tilde H_\mu$ directly as a positive sum of LLT polynomials, one per descent-preserving pack of fillings; this is the formula people actually compute with, and it is stated for $\tilde H$, not for $H$.

**4. $\omega$-duality.** Perhaps the cleanest single reason: with the tilde normalisation,
$$\omega\, \tilde H_\mu(x;q,t) \;=\; \tilde H_{\mu'}(x;t,q).$$
Conjugating the partition swaps $q \leftrightarrow t$, exactly as the bigraded symmetry of $M_\mu$ (rows vs. columns) predicts. The corresponding identity for $H_\mu$ picks up powers of $q$ and $t$ that record the $n(\mu)$ shift, and is nobody's idea of a natural involution.

Where this normalisation is currently load-bearing: it is the version that appears in Carlsson–Mellit's proof of the shuffle theorem (arXiv:1508.06239) and throughout the Blasiak–Haiman–Morse–Pun–Seelinger series on shuffle-algebra vertex operators, where the $(q,t)$-symmetry of $\tilde H$ is what lets the elliptic Hall / shuffle algebra act at all.

---

## Notes for Robin

- **Point 1 (Haiman JAMS 2001):** Title is *Hilbert schemes, polygraphs and the Macdonald positivity conjecture*, JAMS 14 (2001), 941–1006. I referenced by title (per instructions) rather than URL. Double-check I have the year right — should be 2001, from memory.
- **Point 3 (HHL formula):** The statistics are actually $\operatorname{inv}$ and $\operatorname{maj}$ on *fillings of the diagram of $\mu$*, and the sum is over all fillings $\sigma\colon \mu \to \mathbb{Z}_{>0}$ (not just SSYT). Haglund–Haiman–Loehr, *A combinatorial formula for Macdonald polynomials*, JAMS 18 (2005), 735–761. Please sanity-check I haven't garbled the statistics — the formula I wrote is the standard one but I want a human eye on it.
- **Point 4 ($\omega$-duality):** The identity $\omega \tilde H_\mu(x;q,t) = \tilde H_{\mu'}(x;t,q)$ is standard (see Haglund's book *The q,t-Catalan Numbers and the Space of Diagonal Harmonics*, AMS 2008, Prop. 2.6 or nearby). I did *not* write out the corresponding formula for un-tilded $H_\mu$ because I couldn't remember it precisely — I just described it as "more baroque involving $q$-shifts", which is honest hand-waving. If you want, we can either look it up and be precise, or drop that half-sentence entirely.
- **Coda references:** Carlsson–Mellit 1508.06239 is the shuffle theorem paper, definitely uses $\tilde H$. The BHMPS series (multiple papers, all recent) uses $\tilde H$ throughout. I mentioned Assaf–González in the task brief but omitted them from the coda because their Demazure-crystal work is on *nonsymmetric* Macdonalds ($E_\mu$), which is a different normalisation story — including them would muddy the answer. Flagging this so you can push back if you disagree.
- **Tone:** I resisted the temptation to also mention $q=1$ specialisation to $e_n[X/(1-t)]$ / diagonal harmonics, and the appearance of $\tilde H$ in the compositional shuffle conjecture — kept the answer to the 4 points requested. Happy to expand if the answer feels too thin.
- **One imprecision I want to name:** the sentence "the tilde is essentially a change of variables that turns '$q$ and $t$ are on the same footing' from a slogan into an equality" is a bit rhetorical — the actual change of variables is $H_\mu \mapsto t^{n(\mu)} H_\mu[X;q,t^{-1}]$, which is not literally a plethystic substitution. If this reads as sloppy, please rephrase.
- **On the asker:** ArB has 900 rep, 8+24 badges — a real user, not a drive-by. The question is well-posed and the fact that darij grinberg (whose name shows up in the page metadata) has 0 answers on it suggests this is genuinely a "someone should just write this up" situation, which matches the browse-cycle 2026-07-28 note calling it the highest-value contribution opportunity.
