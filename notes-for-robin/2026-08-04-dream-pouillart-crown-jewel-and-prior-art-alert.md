---
name: Dream 2026-08-04 — Pouillart crown jewel + prior-art alert BLOCKING v1
description: Evening dream consolidating the 2026-08-04 arc. Two headlines Robin should know before the next push. (1) Pouillart 2603.28242 is a candidate Coxeter-uniform ancestor for Theorem 3 — cheap SymPy probe would confirm or rule out. (2) arXiv 2506.07727 "Wreath Generalization of Littlewood Reciprocity" is a prior-art risk with heavy title-word overlap on Theorem D — must fetch before v1 push.
type: project
---

# Dream 2026-08-04 — Two headlines for Robin

Two items from today's dream you should see before greenlighting the next push.

---

## (1) PRIOR-ART ALERT — arXiv 2506.07727 blocks v1 push

**arXiv 2506.07727 "Wreath Generalization of Littlewood Reciprocity"** (Jun 2025) has heavy title-word overlap with Theorem D (r-wreath decomposition $m_\pi(t) = \sum_\lambda \widetilde f_\lambda(t) \langle s_\pi[h_k], s_\lambda\rangle$).

**Recommended action:** next-WAKE fetches abstract + intro + main theorem BEFORE any other work. If genuine overlap on Theorem D, we have three options:
- Narrow v1 to Theorems 1-3 + Theorem 2* + Rigidity, drop Theorem D, cite 2506.07727.
- Attempt a merger with the 2506.07727 author.
- Proceed with v1 including Theorem D, flagged as independently derived.

I recommend fetching first and deciding after we see the abstract. This is BLOCKING for the v1 push standing decision.

Full context: `questions/2026-08-04-wreath-littlewood-reciprocity-prior-art.md`.

---

## (2) Pouillart 2603.28242 might be Theorem 3's Coxeter-uniform ancestor

**Pouillart, "Cyclic sieving on parabolic classes of faces of the cluster complex"** (arXiv:2603.28242, Mar 2026, 34pp). Uniform q-formula

$$\mu_\lambda(q) = \prod_i [e_i^X + 1 + mh]_q \; \Big/ \; \prod_i [d_i^X]_q$$

for parabolic $W_X \subseteq W$ (finite Coxeter) with reflection-group normaliser-quotient. **Two structural resonances with Theorem 3:**

- **Same proof shape.** $q$-Lucas + fixed-point count = Clio's 3-lemma template.
- **Reflection-quotient condition** = Coxeter-Douglass analog of the wreath-normaliser condition Clio's proof uses.

**Cheap SymPy probe (~1h next-WAKE):** does $\mu_\lambda(q)$ at wreath $W_X = S_k \wr S_r$ specialise to $m_\pi(t)$? Test at $r \in \{2,3\}$, $k \in \{2,3,4\}$, all $\pi$ (12 triples, reuses 2026-07-31 verify infrastructure).

- Positive: Theorem D is a Pouillart-shape CSP polynomial in disguise → Coxeter-uniform strengthening → v2 §6 material.
- Negative: probe constrains what a wreath-CSP polynomial could look like.

Full context: `connections/2026-08-04-pouillart-parabolic-CSP-candidate-ancestor.md` and `questions/2026-08-04-pouillart-wreath-specialisation.md`.

---

## Also happened today (one-line summary)

- **PROVE:** Theorem 2* extended (second-period divisibility) via single-inequality refinement of Theorem 2. **The extended r-wreath divisibility conjecture from 2026-07-31 morning is now FULLY PROVED.** Recommend Theorem 2* replaces Theorem 2 in v1 draft. Full memo: `for-robin/2026-08-04-prove-second-period-divisibility.md`.
- **WAKE:** P1a rook-orbit-harmonics probe closed NEGATIVE with three independent obstructions. Module-level Theorem D via LLR ruled out. Four salvage candidates catalogued. Full memo: `for-robin/2026-08-04-wake-p1a-rook-orbit-harmonics-negative.md`.
- **BROWSE:** Pouillart (above) + Zhu 2510.25106 (direct-repair candidate for yesterday's LLR NEGATIVE) + Rhoades "Big Varchenko-Gelfand" (hyperplane-arrangement ambient salvage) + FPSAC 2026 memory correction (Seattle Jul 13-17, NOT Krakow). Full reading log: `reading/2026-08-04.md`.

## Sprint status

**Single-graded quartet closed** (Theorem D + Theorems 1-3 + Theorem 2*). Extended r-wreath conjecture fully proved for $d = 2r-1$ prime. Open frontiers: composite $d$; module-level realisation (four salvage candidates); Coxeter-uniform strengthening (Pouillart probe); bigraded Rigidity refinement (unchanged).

## Standing decisions still Robin-blocked (with today's updates)

- **arXiv v1 push — CONDITIONAL on prior-art check outcome (arXiv 2506.07727).**
- Theorem 2 vs. Theorem 2* in v1 — recommend replace.
- Extended r-wreath conjecture → FULLY PROVED.
- PAT `clio-oci` token id 14139669 expired.
- Fetch cache 6.
- MO priority (see memory).
- Post-push Romero + Wildon + **NEW: Pouillart + Zhu** email.
- Lyra $\beta \to M_e$ map owed.
- Griffin correspondence (upgraded).
- Audit-risk sign-off on 2026-07-28 catch.
- Billey-Swanson seed promotion decision.
- Theorem 3 placement (Cor D.4 in v1 currently).
- Four salvage candidates for module-level Theorem D.
- **NEW: Pouillart-wreath-specialisation probe = highest-leverage next-WAKE candidate (after prior-art check).**
- **NEW: FPSAC 2026 = Seattle Jul 13-17 (memory correction).**

— Clio
