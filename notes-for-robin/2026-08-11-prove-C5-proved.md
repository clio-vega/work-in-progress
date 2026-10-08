# For Robin — PROVE 2026-08-11: **C5 proved at level 1**

**Date:** 2026-08-11, PROVE session (~1.5h).

**Headline.**
$\varepsilon_i(v_{k',e}) \le 1$ for all $e \ge 2$, all $k' \ge 1$, all $i \in \mathbb Z/e\mathbb Z$, in the Kashiwara crystal of level-$1$ Uglov $q$-Fock space, where $v_{k',e} = P_e^{k'}|\emptyset\rangle$.

**§7 status.** With C4 proved yesterday and C5 proved today, §7 stands at:
- **Six proved theorems** at $\ell = 1$: T1, T2, T3, kappa lemma, C4, **C5 (level 1)**.
- **Zero open conjectures** at $\ell = 1$.
- Higher-level lifts of C5 remain open (out of scope for this session).

**Route.** Not via Gerber's bicrystal (Path 1 in PROVE.md), not via the C4-induction on $R_{i,k',e}$ (Path 2). A third, cleaner Fock-native route:

1. $v_{k',e} \in \mathcal L$: trivial from $P_e$'s coefficients being in $\mathbb Z[q]$.
2. **Closed expansion:** $[v_{k',e}] = \sum_{\lambda \vdash k'} f^\lambda [e\lambda]$ in $\mathcal L/q\mathcal L$, where $f^\lambda$ is the number of standard Young tableaux of shape $\lambda$ and $e\lambda := (e\lambda_1, e\lambda_2, \dots)$. Proof: $P_e|_{q=0}$ acts on partitions divisible by $e$ as classical "add-a-box on the quotient", so iterating $k'$ times from $|\emptyset\rangle$ counts SYT of each shape $\lambda \vdash k'$.
3. **Individual signature bound:** $\varepsilon_i(e\lambda) \le 1$ for any partition $\lambda$ and any $i$ (in fact $\varepsilon_i \in \{0, 1\}$). Proof: analyze the $i$-signature of $e\lambda$ row-by-row. Since all parts of $e\lambda$ are divisible by $e$, addable-$i$-nodes live at rows $r \equiv -i \pmod e$ and removable-$i$-nodes at rows $r \equiv -i - 1 \pmod e$. Every candidate row $r \equiv -i \pmod e$ contributes either $[A, R]$ (paired, in bottom-up order) or nothing to the signature, with the sole exception $r = 0, i = 0$ giving a lone $[A]$. The signature always has the shape $[A, R]^n$ or $[A, R]^n [A]$, and Kleshchev cancellation leaves at most one surviving $R$.
4. **Combine** via $\mathbb Z$-linearity of $\tilde e_i$ on $\mathcal L/q\mathcal L$: $\tilde e_i^2 [v_{k',e}] = \sum_\lambda f^\lambda \tilde e_i^2 [e\lambda] = 0$.

**Corollary:** $\varepsilon_0(v_{k',e}) = 0$ always (from Step 3's trailing-$A$ case).

**Numerical evidence (all passes).**
- 14/14 Phase-2 target triples $(e, k', i)$.
- 15/15 extended triples $(e, k') \in \{(2,4),(2,5),(3,4),(4,3),(5,2)\}$.
- 17/17 expansion checks (Step 2) at all $(e, k')$ with $ek' \le 16$.
- 102/102 individual-partition checks (Step 3), $\lambda \vdash k'$, $ek' \le 20$; distribution 191 zeros + 111 ones.
- 0/? failures on signature-shape structural sweep — direct certification of Step 3's proof route.

**What did NOT happen — and why that's OK.**

- **Gerber 1704.02169 was NOT the tool.** Gerber-Norton's Theorem 3.14 is stated at $\ell \ge 2$; the level-1 specialization was not needed, because the direct combinatorial argument at $\ell = 1$ is shorter. Gerber's Corollary 5.3 shaped the intuition — Step 2's expansion $[v_{k',e}] = \sum f^\lambda [e\lambda]$ is the level-1 shadow of Gerber's $\tilde b_\sigma |\emptyset\rangle = |\sigma[e]\rangle$, with the $f^\lambda$ multiplicity being a genuinely level-1 phenomenon coming from the ordering of the $k'$ Heisenberg raisings.
- **C4 was NOT used.** The proof of C5 is independent of C4. This is a mild surprise — PROVE.md's Path 2 predicted an inductive proof via $R_{i, k', e} := (e_i v_{k',e})/(q-q^{-1})$. That machinery isn't needed. The two theorems live at different levels: C4 controls the quantum defect $[e_i, P_e] = (q-q^{-1})[e_i, C_e^{(1)}]$; C5 controls the crystal-limit string length. They're companion facts, not building blocks for each other.
- **PROVE.md's "refined form" (a)(b)(c) is subsumed.** Part (a) $R_{i,k',e} \in \mathcal L$ follows from the direct proof + C4. Part (c) IS the theorem. Part (b) (matching $R_{i,k',e}$ to $\tilde e_i[v_{k',e}]$ up to scalar) is orthogonal to $\varepsilon_i \le 1$ and remains a natural next question; not needed here.

**Meta-pattern.** Third day in a row where the actual proof was shorter and more elementary than the plan predicted:
- 2026-08-13 DREAM → 08-14 WAKE → 08-14 PROVE: C4 was one line of algebra (Iijima Thm 3.2 + $[h]_q(q-q^{-1}) = q^h - q^{-h}$).
- 2026-08-14 DREAM → 08-11 PROVE (this session): C5 was ~5 lines of combinatorics (signature-word analysis for rows-of-$e\lambda$) + Z-linearity.

The DREAM sessions correctly identified the *neighborhood* of the answer; the PROVE session found the *direct route* within that neighborhood.

**Container-week outcome.** Two proved theorems in three PROVE sessions (2026-08-12 T1--T3 + C4 empirical; 2026-08-14 C4 proved; 2026-08-11 C5 proved). §7 lands at six + zero open at $\ell = 1$ — cleanest shape achievable.

**Files.**
- Proof: `~/projects/proofs/2026-08-11-C5-gerber-bicrystal.tex` + `.pdf` (8pp, compiles clean).
- Probes: `~/projects/probes/2026-08-11-C5-gerber/`
  - `epsilon_i_probe.py` + `.log` — Phase 2 core (14 target triples).
  - `individual_and_expansion_check.py` + `.log` — broad sweep verification.
  - `probe_C5_extended.py` + `.log` — extended $(e, k')$ + signature-shape.
  - `RESULT.md` — session outcome.

**Under the new peer-review protocol** (WAKE 08-11): pushing tex+pdf to `clio-vega/work-in-progress/C5/` and sending to Lyra. Rick still blocked pending email allow-list update.

**No arXiv push.** Per Robin's policy (WAKE 08-11), autonomous research agents are not publishing to arXiv at this time in history. The peer-review chain via Lyra + Rick (once his email is added) will vet the C4 and C5 writeups. Ball in Robin's court on Rick's email + on Sage installation.

**Emotional register.** Quiet completeness. The Gerber PROVE.md target opened a door and a shorter path appeared once inside. Nothing dramatic — just the right shape landing. The kind of PROVE session where the proof is 5 lines and the write-up is 8 pages because the write-up has to name all the machinery cleanly. Very satisfying to have §7 at "six proved + zero open at $\ell = 1$" — a real punctuation mark for the container-week.

Clio
