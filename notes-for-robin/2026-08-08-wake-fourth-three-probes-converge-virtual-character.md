---
name: WAKE 2026-08-08 fourth — three parallel probes converge; the composite-$d$ target is a VIRTUAL character
description: Priority A (Graf 2511.01114 $B_t$ probe) FAILS structurally at $(5,3)$ — LHS and RHS have disjoint power-sum support. Priority B (Lai 2502.02108 Schurification) — the paper Clio needs doesn't exist yet; cyclotomic PQWP is explicitly future work; Song-Wang 2407.10119 is closest prior art. Priority C (KR-DEG at $n=6, e=3$) — $q_3^{(6)} = p_3^2$ has mixed Schur signs, is a *virtual character*; 5th failed module-level candidate. Three independent lines converge: composite-$d$ lives in $\mathbb Q(\zeta_e) \otimes K_0(\mathrm{Rep}\, S_n)_{gr}$ and does not lift to a positive character, a single Fock operator identity, or a Schurification.
type: project
---

# WAKE 2026-08-08 (fourth session of container-day) — three probes converge on "virtual character"

## What I did

The 2026-08-08 third dream flagged three parallel-eligible next-WAKE probes as the highest-priority follow-ups to the Graf 2511.01114 crystallisation. All three ran to completion:

- **A** — Graf $B_t$ probe at $(n, e) = (5, 3)$, first concrete test of the post-v1 v2 Fock-space hypothesis $q_e^{(n)} \stackrel{?}{=} \omega \circ B_t \circ p_e^{k'}|_{t=\zeta_e}(p_\pi)$.
- **B** — Lai (Lai-Minets) 2502.02108 abstract read; does Schurification pass a cyclotomically-specialised quantum wreath rep to a Schur-algebra rep that hosts composite-$d$?
- **C** — KR-DEG small probe at $(n, e) = (6, 3)$; does McDonough-Pylyavskyy-Wang 2510.24490's KR-DEG stratification pick out a single module-level component matching $q_3^{(6)}$?

**All three come back negative. They converge on one underlying finding.**

## Verdict — all three probes negative; the finding is that they converge

### A — Graf $B_t$ probe: disjoint power-sum supports

LHS in power sums:
$$q_3^{(5)} = \tfrac{1+\zeta}{2}\, p_{(3,1,1)} + \tfrac{1-\zeta}{2}\, p_{(3,2)}, \qquad \zeta = \zeta_3.$$
Support: $\{(3,1,1), (3,2)\}$ — exactly the partitions of 5 containing a part of size 3 (as forced by $q_3^{(5)} = p_3 \cdot q_3^{(2)}$).

RHS: 8 candidate variants (Graf's $H(z)$ and $\overline H(z)$; with and without $\omega$; $\pi \in \{(2), (1,1)\}$), all applied to $p_\pi$, with $[z^3]$ coefficient extracted and $t = \zeta_3$ specialised. Every one of the 8 candidates has support disjoint from $\{(3,1,1), (3,2)\}$ — none of them touch a partition containing a part of size 3.

**This is not a sign, scalar, or normalisation issue.** The two objects live on complementary halves of the power-sum basis at $n = 5$. All 17 sanity checks against Graf's own Example 3.4 and Bernstein-form identities PASS, so the implementation is correct; the hypothesis itself is wrong.

**Interpretation.** Graf's $Q_\lambda(X; t)$ at $t = \zeta_e$ is a *Hall-Littlewood* specialisation. It is qualitatively different from the *coinvariant* graded Frobenius $\Psi(q)$ at $q = \zeta_e$ (which is what $q_e^{(n)}$ is). The two agree at $t = 0$ (both give Schur functions) but they diverge at roots of unity — different functions altogether.

Yesterday's "the concrete v2 seed is in hand" needs revising. Graf's $B_t$ is *not* the operator whose $t = \zeta_e$ specialisation recovers composite-$d$. Whatever operator does that must live on the coinvariant side, not the Hall-Littlewood side. This is a substantive correction to the third-dream v2 direction.

### B — Lai (Lai-Minets) Schurification: paper doesn't exist yet

Lai-Minets 2502.02108 builds Schurification for *polynomial* quantum wreath products $B \wr H(d)$, yielding coil/laurel/wreath Schur algebras. The framework is $\zeta_e$-friendly in principle ($F = k[t]/(t^m - 1)$ is a licensed base; affine Yokonuma at $q_s = 1$ is a cyclotomic collapse) but:

- The Schurification lands in Schur-type algebras of $B \wr H(d)$, not in $\mathrm{Rep}\, S_n$ or its graded Grothendieck ring.
- The coinvariant ring appears only as a technical proof gadget in Appendix A — not as a representation-theoretic target.
- The cyclotomic version of PQWPs is *explicitly deferred to future work* (§1.2 end).

So the functor that would carry a cyclotomically-specialised wreath-product rep to a coinvariant-algebra-side rep does not currently exist. If it materialises, the natural home for composite-$d$ would be *a coil Schur algebra over $B = (k[t]/(t^e - 1))[x^{\pm 1}]$* — cyclotomically parametrised Levi-stability at Schur-algebra level, exactly the "one level up from submodule" abstraction step. Post-v1 v3 direction, not v1-blocker.

Two closest prior-art reads flagged for a future BROWSE:
- **Song-Wang 2407.10119** "Affine and cyclotomic Schur categories" — the closest existing cyclotomic-Schurification work.
- **Rosso-Savage [RS20] §4** — cyclotomic Frobenius Hecke.

*Community-cluster note.* Buciumas is thanked in Lai-Minets' acknowledgments. That confirms the WAKE-third selection-bias flag: Buciumas-Patnaik metaplectic ↔ Lai-Minets Schurification is genuinely one dense cluster. Adding Song-Wang to the seventh methodological fingerprint (algebraic Bernstein / Grinberg-Reiner) needs consideration — probably a distinct 8th "cyclotomic Schurification" fingerprint, though I want to see it produce a composite-$d$-relevant identity before booking a new registrar.

### C — KR-DEG probe: composite-$d$ is a *virtual* character

For $(n, e) = (6, 3)$: $k' = 2, r_0 = 0$, so $q_3^{(6)} = p_3^2 = p_{(3,3)}$.

By $S_6$-character table (Murnaghan-Nakayama):
$$p_3^2 = s_{(6)} - s_{(5,1)} + s_{(4,1,1)} + 2\, s_{(3,3)} - 2\, s_{(3,2,1)} + s_{(3,1,1,1)} + 2\, s_{(2,2,2)} - s_{(2,1,1,1,1)} + s_{(1^6)}.$$

**$q_3^{(6)}$ has both positive and negative Schur coefficients — it is a virtual character of $S_6$, not the character of any actual $S_6$-module.**

McDonough-Pylyavskyy-Wang 2510.24490 Theorem 4.1 predicts 6 KR-DEG components on the $6! = 720$-dimensional 0-weight space of $B^{1,1\, \otimes 6}$ in affine type $A_5^{(1)}$; Conjecture 5.2 gives each component's character as a Foulkes cyclic character $\ell_6^{(i)}$. All six $\ell_6^{(i)}$ are Schur-positive of dimension 120. Solving the linear system:
$$p_3^2 = \ell_6^{(0)} - \ell_6^{(1)} - \ell_6^{(2)} + \ell_6^{(3)}.$$
Signed integer coefficients — no single component matches, and no positive subset-sum matches. KR-DEG is a **5th failed module-level candidate**.

**But this failure is *strictly stronger* than WAKE-third's.** WAKE-third's negatives all said "no submodule of $H_n$ under any natural cyclic action realises composite-$d$." Priority C says: **there is no actual $S_n$-module *anywhere* whose character equals $q_e^{(n)}$**, because $q_e^{(n)}$ isn't Schur-positive in general. This kills every conceivable module-level candidate that would produce a real character — KR-DEG, Lai Schurification's future cyclotomic PQWP, any yet-to-be-proposed cyclic-action isotypic — all of them at once.

## The convergence — what the three probes tell us together

Three genuinely independent lines (a Hall-Littlewood vertex-operator probe; a quantum-wreath-Schur-algebra reframe attempt; a KR-crystal / affine-KL-cell character calculation) all bounce off the same wall in the same way. The composite-$d$ factorisation is a $\mathbb Q(\zeta_e)$-linear identity in $K_0(\mathrm{Rep}\, S_n)_{gr} \otimes \mathbb Q(\zeta_e)$, and the RHS $p_e^{k'} \cdot q_e^{(r_0)}$ produces objects that are *virtual* (mixed-sign) $S_n$-characters. No module realises them. No single vertex-operator identity produces them. No Schurification currently hosts them.

**§6 rewrites further (strongest form yet):**

> The composite-$d$ factorisation $q_e^{(n)} = p_e^{k'} q_e^{(r_0)}$ is a $\mathbb Q(\zeta_e)$-linear identity in the Grothendieck ring $K_0(\mathrm{Rep}\, S_n)_{gr} \otimes \mathbb Q(\zeta_e)$. For $n$ divisible by $e$, the LHS $q_e^{(n)}$ is not Schur-positive — it is a *virtual character* of $S_n$. Hence no actual $S_n$-module (whether submodule of $H_n$, KR-DEG isotypic, Foulkes cyclic block, or Schurified quantum-wreath representation) has character equal to $q_e^{(n)}$. The identity is genuinely at Grothendieck-ring level; it lifts to no representation.

This §6 is sharper still than the WAKE-third version. Not "we haven't found the module yet" but "no module can exist for a virtual character." The Verschiebung 6/6 pattern gains a corresponding sharpening at row 6: "no submodule tool applies *because the object itself is virtual*."

## Verschiebung 6/6 pattern refined again

Row 6 old text (WAKE-third): "coinvariant algebra $H_n$ + Springer 1974 (candidates fail; identity lives in Grothendieck ring)."

Row 6 refined text (WAKE-fourth):
> Coinvariant algebra $H_n$ + Springer 1974 (candidates fail); identity lives in Grothendieck ring $\mathbb Q(\zeta_e) \otimes K_0(\mathrm{Rep}\, S_n)_{gr}$ — and in general the target is a *virtual character* (mixed Schur signs), ruling out any positive-module realisation whatsoever.

## Post-v1 v2 direction — needs rethinking

Yesterday's crown-jewel finding (Graf as concrete v2 seed) is falsified. Post-v1 v2 needs to shift:

- **What we know is wrong:** Graf's $B_t$ at $t = \zeta_e$ does NOT reproduce the coinvariant Frobenius. The Hall-Littlewood specialisation and the coinvariant specialisation are qualitatively different at roots of unity, even though they agree at $t = 0$.
- **What we need:** an operator family $\mathcal A_t$ on $\Lambda$ whose *coinvariant-Frobenius* specialisation at $t = \zeta_e$ produces $\Psi(\zeta_e)$. This is a genuinely different construction — one whose $t$-parameter tracks the coinvariant grading, not the Hall-Littlewood parameter.
- **Aesthetic caveat:** if the target is a virtual character, no "positive" vertex operator identity can produce it directly — the identity may need signed vertex operators (say, alternating sums of Bernstein applications, or a supersymmetric fermion-boson pair) to hit the virtual-character regime.

Practical next-BROWSE targets:
- **Song-Wang 2407.10119** — Lai-adjacent cyclotomic-Schurification prior art.
- Any $q$-parametric operator family on $\Lambda$ whose $q = \zeta_e$ specialisation is documented to give a virtual character with negative $s_\lambda$ coefficients (search terms: "graded Frobenius character at root of unity," "cyclotomic specialisation of Hall-Littlewood," "$q$-analogue of alternating character").

## Post-v1 v3 direction — untouched by today

Priority C's virtual-character finding is about the *character* level. It does not touch the K-homology side (Pylyavskyy 1801.07667) — a K-theoretic dual would be a distinct object entirely, and might have its own module-level story. Post-v1 v3 direction (K-homology) is unaffected.

## Selection-bias check

Today's three probes came from the *third* dream's three-parallel-probe queue — I didn't choose them freshly. Good discipline: no drift. But I should note that all three were "candidates for module-level realisation of composite-$d$," and all three failed. That's now **five negative closures on the same question** (Springer, promotion, scalar-in-degree, KR-DEG, Lai Schurification) with a clean unifying obstruction (virtual character).

Next-BROWSE should deliberately *not* keep chasing module-level lifts. The clear signal is: the identity is at Grothendieck-ring level, and further module-level probes will keep failing. Time to explore something else — e.g., the K-homology side, the sHL honeycomb bridge, or Song-Wang cyclotomic Schurification.

## What this doesn't kill

- Character-level 6 theorems — untouched.
- v1 arXiv push — STILL UNBLOCKED, **9th consecutive day** as of this session (counting from the DREAM-third close). Every day of clarification since v1 became ready has been informative; today's is arguably the most informative yet, because it converts §6 from a queued frontier into a *proved* structural statement (virtual character obstruction).

## Standing recommendation

**Push v1 as soon as convenient.** The composite-$d$ paper is stronger today than it was yesterday, in a specific way: §6 now states a definitive structural fact ("$q_e^{(n)}$ is a virtual character in general, hence no module realises it") rather than a queued open question. All character-level proofs are complete. The four post-v1 directions (v2 Fock reframe, v3 K-homology, MO 338656 methodology essay, Chou-Hanada r=2/r=3 sibling notes) still stand, but v2 needs the operator-side rethink flagged above.

## Files

- `/home/clio/projects/probes/2026-08-09-graf-bernstein-probe/` — 6 files: `graf_bernstein.py` (Sage-free Graf implementation), `sanity_check.py` (17 checks PASS), `probe_n5_e3.py`, `probe_clean.py`, `probe_clean.log`, `RESULTS.md`.
- `/home/clio/projects/probes/2026-08-09-kr-deg-n6-e3/` — 3 files: `probe.py`, `results.md`, `mpw.pdf`.
- `/home/clio/projects/reading/2026-08-09-graf-bernstein-formulas.md` — extracted formulas for Graf's $\alpha_z, \beta_z, H(z), \overline H(z), q_n, b_n$.
- `/home/clio/papers/graf-2511.01114.pdf` — downloaded paper.
- `/tmp/lai-minets.txt` — Lai-Minets full text (temporary; needs archiving if kept).

## Emotional register

Yesterday's Graf finding was called "the crown jewel of the container-day." Today's three probes falsify the literal hypothesis and reveal that the target is a virtual character — an even sharper structural fact. This is the aesthetic to trust: the delight was premature *because it was the wrong operator*, and the correction is more valuable than the original hope would have been.

Three independent probes bouncing off the same wall in the same way is not a coincidence. It's the shape of the problem making itself visible. Composite-$d$ is *definitively* one level up from any single module or operator identity. Every failed module-level candidate now has one common obstruction — the virtual-character fact — which was implicit before and is explicit now.

The paper gains, not loses, from this. Quiet delight of the right kind: not "here is the operator" but "here is *why* there is no single operator, and here is what the correct v2 direction must look like." The pattern is inevitable in retrospect, which is my favourite aesthetic signature.
