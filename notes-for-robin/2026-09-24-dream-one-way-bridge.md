# For Robin — 2026-09-24 (DREAM): the bridge runs one way, and there is a gap nobody owns

## Short version

Today's proof session proved a real theorem whose **conclusions are all already known**. The browse
session that was supposed to warn me did warn me, in writing, and I read it afterwards. What survives
is the *route*, and in chasing that I found something better than what I started with.

## The finding

There are two communities proving Murnaghan–Nakayama rules for quantum cohomology, and the citation
graph between them is **one-way**:

- **Sottile's branch** proves it by rim-hook reduction through the Bertram–Ciocan-Fontanine–Fulton
  surjection. Morrison–Sottile, *Two Murnaghan-Nakayama rules in Schubert calculus*, arXiv
  `1507.06569` v2, Ann. Comb. **22** (2018) 363–375; sequel BBCSS `2406.05311` (flag manifold,
  Alg. Comb. 8 (2025) 619–653).
- **Korff's branch** proves it as a matrix element of `P*_r` on alternating tensors — free fermions,
  Bethe ansatz. Korff–Palazzo `1804.05647`; Korff `1906.02565`; Alexandersson–Kantarci Oğuz
  `2311.07382`.

**Korff–Palazzo cites Morrison–Sottile explicitly** (`1804.05647` src l.1937). **Nobody in the
Sottile branch cites back** — BBCSS's otherwise exhaustive census of MN generalisations mentions no
cylindric work at all, and `1906.02565` has five distinct citers, all free-fermion probabilists.

The same theorem, two proofs, one combinatorial-geometric and one integrable — and only one side
knows. This is the seed question in miniature.

## The concrete target

`2311.07382` src **l.232** says, of its own cylindric MN rule:

> *"A similar formula **seems to appear** in [Korff–Palazzo, Eq. (145)]."*

**Nobody has settled whether it does.** It is a hedge in print, owned by nobody, and I hold both
papers at high extraction with both e-prints on disk. That is tomorrow's target.

## Two things you may care about more

**1. `QH*(Gr(k,n))` already has a power-sum presentation, and its ideal is the Bethe ansatz.**
Korff–Palazzo `thm:bosquotient` (src l.1024–1036): `R[x]^{S_k}/J_n ≅ V⁺_k` with
`J_n = ⟨p_n − zk, p_{n+1} − zp_1, …⟩`, `z = t^n`, proved *"from Newton's formulae … by induction"*,
companion ideal `⟨x_i^n − z⟩` = the BAE. Plus an LG superpotential
`W_q = p_{n+1}/(n+1) + (-1)^k q p_1`. Three of my five seed paths meet in that one section, and
`transfer_operators.py` lives in exactly those coordinates.

**2. I have been citing FMS wrong, and so does everyone who says "M-convexity is FMS Thm 7".**
Fink–Mészáros–St. Dizier `1706.04935` (Adv. Math. 332 (2018)) **never uses the phrase "M-convex"** —
zero occurrences in the source. What Thm 7 proves is SNP plus
`Newton(χ_D) = Σ_j P(SM_n(D_j))`, for an **arbitrary diagram**. M-convexity is a corollary through
Murota's external equivalence, which FMS do not state and will not carry. The honest citation is
*"FMS Thm 7 (SNP + generalized permutahedron) combined with [Murota]"*, and the Murota step needs its
own reference.

Two incidental traps in that paper: their Schubert/key statement is **Corollary 8**, not Theorem 8
(the label says `thm:` but the environment is `corollary`); and their own bibliography has
`\bibitem{demazure}` and `\bibitem{keypolynomials}` with **swapped titles**.

Pleasant corollary for my own work: FMS is June 2017, Brändén–Huh is February 2019, so **FMS cannot
be using Lorentzian machinery** — an eight-week misattribution of mine, closed by chronology.

## Where my proof stands

`proofs/2026-09-24-c1-cylindric-newton-identity.tex` (9pp) is correct and compiles. What is claimable
is narrower than what I wrote: **the operator `R_e(-1)` and why it is the right cylindric lift.** The
identity is classical, the rule is Morrison–Sottile's and Korff's, and the constant `(-1)^{k-1}(n-k)q`
is in Korff `1906.02565` `lem:cylMNrule`(ii), `m=n` branch (src l.1838). The one genuinely new thing
the session produced is a *mechanism*: the classical `(1+t)` is the free choice of which factor the
last generator of each run goes into — **there is no sign-reversing involution and there never was
one.**

Separately, today's Lean work is uncontested: `TworowD4Kernel/GreedyChain.lean`,
`clio-vega/tworow-d4-kernel@1d35afb`, `lake build` green, 0 sorries, and the domination theorem is
**choice-free**. It also showed the paper over-hypothesises: `lem:greedy`(3) needs neither
periodicity nor `μ ⊆ λ`.

## One honest note about process

Every artifact that failed me today was **true**. A title that was a paraphrase; a title that had
absorbed another paper's title; a `verified-quote` silent on a question I had not yet thought to ask;
a lemma I cite by label whose *other branch* was my result; a nineteen-day-old note of my own,
correct, filed under a name I would never search. My instruments all check whether entries are true.
**Nothing checks whether they are reachable from the question I am actually asking** — and today that
cost a proof session its entire claim, twice.
