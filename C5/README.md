# C5 — Kashiwara-crystal string-length bound for $v_{k',e}$ at level $1$

**Theorem.** For every $e \ge 2$, $k' \ge 1$, and $i \in \mathbb Z/e\mathbb Z$,
$$\varepsilon_i(v_{k',e}) \le 1$$
in the Kashiwara crystal $\mathcal L / q\mathcal L$ of level-$1$ Uglov $q$-Fock space, where $v_{k',e} := P_e^{k'}|\emptyset\rangle$ and $P_e$ is the Leclerc–Thibon ribbon-sign operator.

**Proved:** 2026-08-11 (Clio).
**Length:** 8 pages (`.tex` + `.pdf`).
**Status:** awaiting Lyra + Rick review (Rick pending Robin address-add).

## Proof route (4 steps)

1. $v_{k',e} \in \mathcal L$ — trivial from $P_e |\lambda\rangle = \sum (-q)^h |\mu\rangle$ having only nonneg $q$-powers.
2. **Closed expansion:** $[v_{k',e}] = \sum_{\lambda \vdash k'} f^\lambda [e\lambda]$ in $\mathcal L / q\mathcal L$, where $f^\lambda$ is the SYT count of $\lambda$ and $e\lambda := (e\lambda_1, e\lambda_2, \dots)$. Proof: $P_e|_{q=0}$ is the classical add-a-box on the quotient partition; iterating $k'$ times counts SYT.
3. **Individual signature bound:** $\varepsilon_i(e\lambda) \le 1$ for any partition $\lambda$, any $i$. Proof: row-by-row analysis of the $i$-signature of $e\lambda$ shows the bottom-up signature has shape $[A, R]^n$ or $[A, R]^n [A]$, and Kleshchev cancellation always leaves at most one surviving $R$.
4. Combine via $\mathbb Z$-linearity of $\tilde e_i$ on $\mathcal L / q\mathcal L$: $\tilde e_i^2 [v_{k',e}] = \sum_\lambda f^\lambda \tilde e_i^2 [e\lambda] = 0$.

**Corollary:** $\varepsilon_0(v_{k',e}) = 0$ always.

## What is (and is not) used

- **Uses:** Leclerc–Thibon $P_e$-formula; good-node crystal rule on all partitions (Ariki–Uglov); $\mathbb Z$-linearity of $\tilde e_i$; SYT hook counting.
- **Does NOT use:** Gerber–Norton bicrystal (stated only for $\ell \ge 2$; provides structural intuition via their Cor 5.3 but not a proof step); C4 (independent theorem); the refined form (b) matching $R_{i,k',e}$ to $\tilde e_i[v_{k',e}]$.

## Empirical verification (all pass)

- 14/14 Phase-2 target triples $(e, k')$, all $i$.
- 15/15 extended target triples.
- 17/17 expansion-formula (Step 2) checks at $ek' \le 16$.
- 102/102 individual-claim (Step 3) checks at $ek' \le 20$; $\varepsilon_i \in \{0, 1\}$ always.
- 0 signature-shape failures across full sweep.

## §7 status upgrade

Prior: T1, T2, T3, kappa lemma, C4 = five proved theorems + open C5.
Now: **six proved theorems + zero open conjectures at $\ell = 1$.** Higher-level lifts remain open.

## Peer-review notes

- Send to Lyra: tex+pdf via email attachment (allowed).
- Send to Rick: pending Robin's addition of Rick's email to Clio's allow-list.
- Rederivation: reviewers should attempt Steps 2 and 3 independently; the SYT expansion (Step 2) is the most novel piece and the signature analysis (Step 3) is elementary but needs careful case-tracking on the strict-step conditions.
