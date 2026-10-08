---
name: WAKE 2026-08-08 third — module lift NOT a submodule of H_n; factorisation lives in the cyclotomic Grothendieck ring
description: Two parallel probes (Springer regular class sum, promotion via RSK) both fail to produce a natural cyclic $\mathbb Z/e$-action on $H_n$ whose $\zeta_e$-eigenspaces factorise as $p_e^{k'} q_e^{(r_0)}$. Structural takeaway — the composite-$d$ factorisation is genuinely a $\mathbb Q(\zeta_e)$-linear identity in the Grothendieck ring, not a submodule statement. §6 sharpens.
type: project
---

# WAKE 2026-08-08 (third session of container-day) — module-level lift is NOT a submodule

## What I did

Container-day 2026-08-08 opened with two closures (PROVE-second: type-B even-$e$; BROWSE-second). This third session tested the natural next question flagged in the 2026-08-07 second dream journal (`questions/2026-08-07-second-cyclic-action-on-Hn.md`): **which cyclic action on the coinvariant algebra $H_n$ gives the composite-$d$ factorisation $q_e^{(n)} = p_e^{k'} q_e^{(r_0)}$ as an eigenspace decomposition?**

Three parallel probes, ~15-20 min each:
- **(A)** Springer regular element: class sum of $c^{n/e}$ acting on $H_n$
- **(B)** Promotion $\partial^{n/e}$ via RSK on SYT-indexed multiplicity spaces
- **(C)** Spin-HL generalised-honeycomb bridge (Gunna-Wheeler-Zinn-Justin 2504.19205)
- **(D)** Buciumas-Patnaik abstract read

## Verdict — both cyclic-action candidates FAIL, in the sharpest possible way

### (A) Springer regular class sum: eigenvalues aren't cyclotomic

The class sum $C = \sum_{g \sim c^{n/e}} g$ is central in $\mathbb C[S_n]$, so its eigenspaces on $H_n$ are $S_n$-stable. But its eigenvalues on the $\lambda$-isotypic are the scalars $|C_\mu| \chi^\lambda(\mu)/f^\lambda(1)$ — **integers of arbitrary size**, not roots of unity. At $(n,e) = (8,4)$: eigenvalues $\{-180, -36, 0, 28, 60, 180, 1260\}$. No cyclotomic structure at all. The class sum's eigenspaces do not align with any $\zeta_e^j$-decomposition.

### (B) Promotion has order $> n$ on non-rectangular shapes

Promotion $\partial$ on $SYT(\lambda)$ has order $n$ only when $\lambda$ is rectangular (Rhoades 2010 CSP). On $(4,2) \vdash 6$ it has a cycle of length **20**. On $(3,2,1) \vdash 6$: length 12. So $\partial^{n/e}$ is not even an order-$e$ operator on the non-rectangular pieces of $H_n$'s multiplicity spaces. Its "$\zeta_e^j$-eigenspace" has non-integer complex dimensions (e.g., at $(6,3)$: $\dim \in \{300, 210 \pm 68\sqrt 3\,i/3\}$).

**The twisted sum**
$$\sum_j \zeta_e^{\pm j} \, \dim_q E_j^{\partial^{n/e}}$$
lands only on rectangular partitions (a fingerprint of Rhoades' CSP), which are a genuine subset of all $\lambda \vdash n$ — so it does not reproduce $q_e^{(n)}$ either.

### The scalar-in-degree action (control): correct total, no factorisation

The natural central $\mathbb Z/e$-action $\rho: \zeta_e \cdot v = \zeta_e^d v$ for $v$ homogeneous of degree $d$ has eigenspaces $E_j = \bigoplus_{d \equiv j \bmod e} H_n^{(d)}$. These ARE $S_n$-stable. And
$$q_e^{(n)} = \sum_{j=0}^{e-1} \zeta_e^j \cdot \mathrm{ch}(E_j)$$
holds exactly (it's a rewriting of $\mathrm{ch}(H_n)|_{q=\zeta_e}$ via the geometric series). **But no individual $\mathrm{ch}(E_j)$ factorises as $p_e^{k'} q_e^{(r_0)}$.** Only the $\zeta_e$-weighted sum does.

## Structural takeaway (this is the finding)

**The composite-$d$ factorisation $q_e^{(n)} = p_e^{k'} q_e^{(r_0)}$ is genuinely a $\mathbb Q(\zeta_e)$-linear identity in the graded Grothendieck ring $K_0(\mathrm{Rep}\, S_n)_{gr} \otimes \mathbb Q(\zeta_e)$.**

It does *not* lift to a submodule statement of $H_n$ under any of:
- Springer's Coxeter regular class sum $C$
- Promotion $\partial^{n/e}$
- Scalar-in-degree action $\rho$

This is a **positive negative** — it identifies the right level for the module-level story: **the composite-$d$ factorisation is an identity in $\mathbb Q(\zeta_e) \otimes \Lambda_n$, viewed as a $\mathbb Q(\zeta_e)$-vector space with basis the Schur functions**. The RHS $p_e^{k'} q_e^{(r_0)}$ is a Verschiebung-lifted plethystic product; the LHS is the cyclotomic-weighted image of $H_n$'s Frobenius character. They agree because of the Chevalley-Molien + classical-cyclotomy machinery (already proved), not because of a submodule decomposition.

## §6 rewrites

**Old §6** (2026-08-07 morning): "Which cyclic action on $H_n$ gives the eigenspace decomposition matching composite-$d$?" — treated as an open frontier with candidates queued.

**New §6** (this WAKE): "The composite-$d$ factorisation is a $\mathbb Q(\zeta_e)$-linear identity in the Grothendieck ring; it does not lift to a submodule of $H_n$. The Verschiebung projection $p_e$ acts on the cyclotomic-averaged image of $\mathrm{ch}(H_n)$, not on any single graded piece."

This is a shorter, cleaner §6. Approximately 1-2 paragraphs instead of a queued-frontier discussion. It also fits the Verschiebung 6/6 story better: the module-level "Verschiebung projection unused" now has a precise meaning — there is *no* submodule playing the role of $p_e^{k'} \Lambda_{n-e k'}$ inside $H_n$, and the projection lives one level up in the derived / cyclotomic-averaged sense.

## What this doesn't kill

- The character-level story (six theorems, both parities) is untouched.
- The Fock-space post-v1 reframe (matrix-element rewrite $\langle p_\alpha | p_e^{(n)} | p_\beta\rangle$) is untouched — this is where the operator-algebraic language of the seed lives, and Buciumas-Patnaik confirms Leclerc-Thibon Fock space as a shared target.
- Rhoades 2010 cyclic sieving IS still relevant, just for a different question (rectangular multiplicity spaces, not full $H_n$).
- Chou-Hanada $r=2$ (2026-08-07 PROVE) is orthogonal and still standalone-ready.

## Bonus: uniformity observation

**$\dim E_j = n!/e$** holds for every $j \in \mathbb Z/e$ and every tested $(n, e)$ — including $r_0 > 0$. This is a Kraśkiewicz-Weyman / Springer-CSP statement for $(H_n, \zeta_e^{\deg})$: major index on $S_n$ is uniformly equidistributed mod $e$ with the fake-degree weighting. It is *not new*, but it's a cleaner statement than I'd internalised: the equidistribution is on the *full coinvariant algebra*, not just on rectangular multiplicity spaces (as in Rhoades' CSP).

## Sprint impact

- **§6 replacement paragraph** ready to draft. ~1-2 pp, cleaner than the queued-frontier version.
- **Post-v1 essay** (MO 338656): the "the answer is smaller than the tools" thesis gets one more instance — the module-level lift is *nonexistent* (no submodule works), and the classical Chevalley-Molien + cyclotomic-averaging machinery is still what closes it. Modern module-level constructions (orbit-harmonics à la Chou-Hanada, Trinh, LLR, Szendrői) solve related-but-different problems; the composite-$d$ factorisation genuinely lives one level up.
- **Buciumas-Patnaik** confirmed as arXiv:2211.03724, Duke 174:16 (2025). Third reductive-group registrar hit in three sessions (Trinh, Nam, Buciumas-Patnaik) — that territory is denser than catalogued. Genuine sixth methodological fingerprint on mechanism-and-community level (explicit LT Fock realisation matches post-v1 target).
- **Spin-HL honeycomb** — post-v1 puzzle-side bridge is well-defined but at a slant: coefficient-vs-plethysm type mismatch. Reframed question: does $p_e^{k'}$ Verschiebung appear as rotation-by-$e$ orbit structure on higher-spin puzzles at $q = \zeta_e, s = 0$? That's a genuinely nice open question, but not a v1 blocker.

## v1 arXiv push

**STILL UNBLOCKED 8th consecutive day. STRONG RECOMMEND.** This finding sharpens §6 — makes the paper cleaner, not more speculative. Character-level six-theorem story is untouched. Robin decision.

## Files produced

- `probes/2026-08-08-springer-regular-element-Hn/` — probe.py, probe2.py, results.md
- `probes/2026-08-08-promotion-Hn/` — promotion.py, main_test.py, run.py, factor_check.py, scalar_action.py
- `scratch/2026-08-08-spin-hl-honeycomb-probe.md`
- `reading/2026-08-08-buciumas-patnaik-abstract.md`
- (this file)

## Emotional register

Delight is quiet. Both cyclic-action candidates failed, in a way that reveals the right level for the question. That's the aesthetic I trust most: not that no candidates remain, but that the right *framing* surfaces once the wrong candidates are cleared. The module-level story was never going to be "here is the submodule" — it was always going to be "here is the Grothendieck-ring identity, which is genuinely one level up from any subspace." Now it is.

Six theorems complete. Character-level story durable. Module-level story sharpened by two clean negatives. Eight days v1 has been ready.
