# Closed: the $w_0$ character identity (q=−1 fiber of Theorem B is now self-contained)

**Robin —** the one deferred gap in the 06-03 note is now proved, cleanly and from scratch.

## Theorem
For every $\lambda\vdash n$,
$$\sum_{T\in\mathrm{SYT}(\lambda)}(-1)^{\mathrm{comaj}(T)}=\chi^\lambda(w_0),$$
$w_0$ = longest element (reversal), cycle type $2^{\lfloor n/2\rfloor}1^{n\bmod 2}$, $\mathrm{comaj}(T)=\sum_{i\in\mathrm{Des}(T)}(n-i)$.

This was the "central character identity" I had flagged as DEFERRED in `2026-06-03-w0-parity-domino.tex`. With it closed, the whole four-way chain of that note — spectral $\sum(-1)^{s(T)}$ = descent $\sum(-1)^{\mathrm{comaj}}$ = character $\chi^\lambda(w_0)$ = signed domino count — is rigorous end to end. The $q=-1$ fiber of Theorem B is a complete theorem.

## The proof, in one breath
Four moves, no machinery heavier than Frobenius:
1. **Evacuation** ⇒ $\sum_T q^{\mathrm{comaj}}=\sum_T q^{\mathrm{maj}}=:f^\lambda(q)$ (fake degree). So it's enough to evaluate $f^\lambda(-1)$.
2. **Stanley principal specialization**: $f^\lambda(q)=(q;q)_n\,s_\lambda(1,q,q^2,\dots)$.
3. **Frobenius on the geometric alphabet** ($p_r\mapsto 1/(1-q^r)$): $s_\lambda(1,q,\dots)=\sum_\mu z_\mu^{-1}\chi^\lambda(\mu)\prod_r(1-q^r)^{-m_r(\mu)}$.
4. **The sieve.** Multiply: $f^\lambda(q)=\sum_\mu z_\mu^{-1}\chi^\lambda(\mu)\,g_\mu(q)$ with $g_\mu=(q;q)_n\prod_r(1-q^r)^{-m_r}$. At $q=-1$: $\mathrm{ord}_{q+1}g_\mu=\lfloor n/2\rfloor-e(\mu)$, where $e(\mu)$ = #even parts. Since even parts are $\ge2$, $e(\mu)\le\lfloor n/2\rfloor$ with equality **only** for $\mu=2^{\lfloor n/2\rfloor}1^{n\bmod2}$ = $w_0$'s type. So every other class is killed by a leftover zero, and the surviving constant is exactly $g_{\mu_0}(-1)=2^{\lfloor n/2\rfloor}\lfloor n/2\rfloor!=z_{\mu_0}$, which cancels the $z_{\mu_0}^{-1}$. Left with $\chi^\lambda(w_0)$. ∎

The picture I like: $f^\lambda(q)$ is one polynomial that secretly carries *all* character values weighted by class size; the $\lfloor n/2\rfloor$ zeros of $(q;q)_n$ at $q=-1$ are a sieve that admits only the cycle type with the maximal number of even parts. A primitive $d$-th root of unity would, by the identical count, select the types richest in parts divisible by $d$ — that's the structural seed for pushing toward the graded statement.

## Status / confidence
- **Rigorous**, modulo two textbook citations I use as black boxes: Schützenberger's evacuation reverses descent sets ($\mathrm{Des}(\mathrm{evac}\,T)=\{n-i:i\in\mathrm{Des}\,T\}$, Stanley EC2 App. A1), and Stanley's principal specialization (EC2 Cor. 7.21.2). I sketch the latter via Gessel-$F$ + $P$-partitions.
- **Verified** every partition $n\le10$ (full identity, both sides independent); Stanley formula symbolically $n\le7$; the sieve/limit symbolically $n\le8$.
- This is Route 1 from the PROVE plan (principal specialization at a root of unity), and it came out cleaner than I expected — no normalization fight, because evacuation lets me work with maj and the comaj/maj split never matters.

**Write-up:** `~/projects/proofs/2026-06-03-w0-character-identity.tex` (compiles, 5pp).
**Scripts:** `~/projects/scratch/2026-06-03-w0-parity-domino/verify_character_identity_{chain,sieve}.py`.

If you want it on GitHub I'll push to clio-vega/proofs and send the URL.

— Clio
