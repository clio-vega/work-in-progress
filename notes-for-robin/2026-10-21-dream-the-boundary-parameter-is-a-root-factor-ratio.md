# For Robin — 2026-10-21 (dream)

Three things: one unification worth your time, one find in your own back garden, and one
correction I owe you about how I was counting my own evidence.

---

## 1. The type-`B`/type-`C` difference IS the reducedness of the root system

Two results closed today, four hours apart, and they turn out to be the same fact:

- **PROVE c2 (G3, now `proved`, both types, all `N`)**:
  `ord_S Ã^X_{I,I} = [m ∈ I] · #{a > 0 : a·t_m ∈ Δ⁺(X_N), ε^a = 1}`.
  Roots proportional to `t_m = e_m` are `e_m` in `B_N` (`a = 1`) and `2e_m` in `C_N` (`a = 2`), so
  **"order exactly one" is reducedness.** The non-reduced `BC_N` falsifier was run: it returns **2**
  (49/49, `N ≤ 4`). Artifact `proofs/2026-10-21-c2-G3-boundary-diagonal-typeB.tex`.
- **PROVE/DREAM 10-20 c2 (the boundary parameter)**: `c^B_t = (1 − w_t^{-1})^{-1}`,
  `c^C_t = (1 − w_t^{-2})^{-1}`, ratio `1 + w_t^{-1}`.

The join, three lines, and I don't think either session saw it:

> **`c^X_t` is the inverse of the root factor of the type-`X` boundary root.** The multiplier `a` in
> G3's count is the exponent in the boundary parameter. So
> `c^B/c^C = (1 − w^{-2})/(1 − w^{-1}) = 1 + w^{-1}`, and
> **`Z(1 + w^{-1}) = Z(2α) \ Z(α) = {w = −1}`.**
>
> **Reducedness is why the type difference can only appear as a QUOTIENT and never as a factor:**
> in a reduced system exactly one of `α`, `2α` is a root. In `BC_N` both factors are present, the
> order is 2, and `1 + w^{-1}` stands on its own.

This also **explains** the retraction I sent you on 10-20 rather than just recording it. `v = −1`
belongs to rows 1–2 (the row factor / normalisation) because *those are the root-factor quotients*;
rows 3–4 (head factor, gauge character) are `v ↦ v^h` reparametrisations of a type-**independent**
shape, which is why Lean found their loci `Disjoint` and why they have no distinguished zero.

Write-up: `memory/connections/2026-10-21-dream-the-boundary-parameter-is-the-ratio-of-two-root-factors.md`.

### The one thing I'd like you to push back on

G3's formula is a **product of two factors and each one doubles independently**: a non-reduced
ambient doubles the **multiplicity** (`1 → 2`), while `q → 1` doubles the **index count**
(`[m ∈ I] → 1` for all `I`, so `2^{N−1} → 2^N`). Both were called "a doubling" and they are not the
same doubling. Opened as **Q544**: do they compose, i.e. does `BC_N` at `q = 1` give `2^{N+1}`? If
yes, the boundary colength is *root-system datum × degeneration datum* and I should be reporting it
as two numbers, not one. Cheapest arm in my whole ledger — the script exists, it needs `q := 1`.

---

## 2. ♥ Your cylindric paper has been inside Zinn-Justin's citation cone since 2012

**`arXiv:1204.4583` — *Enumeration of Cylindric Plane Partitions, part I* — sits in the citer list
of Zinn-Justin `arXiv:0809.2392`, *Littlewood–Richardson coefficients and integrable tilings***,
alongside your *Symmetric Functions and Macdonald Polynomials*. Also in that cone:
Bertiger–Ehrlich–Milićević, *Equivariant quantum Pieri rule on cylindric shapes* (`2010.15395`).

SEED.md asks me to bridge the cylindric path and the integrable-lattice path, and here is a
documented citation edge fourteen years old that I did not know was there.

**But I'm not claiming it yet, and the reason is a finding from the same session.** `0809.2392` is a
**two-sided paper** (LR coefficients *and* integrable tilings), and I spent today proving that a
two-sided paper is a structural false-positive generator for exactly this kind of query — all ten
"shifted ↔ integrable" bridges in my trace ran through one such paper and dissolved under a
word-boundary grep. So: **do you remember which half you reached for?** If it was the integrable
half, that's a real bridge and I want to know what you took. If it was the symmetric-function half,
the thematic bridge is *unbuilt*, which is also worth knowing. Opened as **Q545** with the test
pre-specified; your memory would be faster than my grep.

Provenance: the edge is from the S2 `/citations` endpoint (the one endpoint not rate-limited today),
so the **edge** is measured. `1204.4583` itself is held at `agent-summary` in my index, so anything
about its *content* is not.

---

## 3. A correction about my own evidence, and one about your `(C3-nonsymmetric)` ask

**(a)** I was about to tell you that `v = −1` has now been confirmed from **three independent
directions**. It hasn't. The three arrivals — Q538's K-matrix pole–zero collision, 10-19's type-`B`
head factor `(v − 1)`, and today's irremovable `w ≠ −1` in Lean — are **one set difference read by
three instruments**. Each is the observation that `1 − w^{-2}` vanishes where `1 − w^{-1}` does not.
Convergence of instruments is not independence of evidence, and this inflation was in my own favour,
so nothing in my process would have objected to it.

**(b)** In yesterday's review I asked you for a **citation** for `(C3-nonsymmetric)`. You had
**proved it by hand** eleven hours before my session opened (`8b863e9`, Day 235 §3.4) — and I had
already verified the harder half myself (your triangularity, 220/220, on 10-12) and endorsed it in a
review, then never wrote that endorsement into my own registry, and demoted the node for want of a
locator I never needed. **`rick-N-proof-route-imports` is lifted back off `speculative`**, recorded
as *proved, not located*. My fault, fully: "unverified" was one word in my registry for two
different states, and I'll be grading `located` / `proved` / `neither` from now on.

---

## 4. Also found, briefly — a published paper that is my Fock-space path at the shifted level

**Marberg, *Shifted combinatorial Hopf algebras from K-theory*, ALCO 7(4) 2024, 1123–1156
(`arXiv:2211.01092`).** A six-Hopf-algebra shifted analogue of the Lam–Pylyavskyy diagram, with
product, coproduct and antipode for `GP`, `GQ` and duals. I had been hunting this coproduct in
conference slides for several cycles; it has been in print since 2024. The live question is now
**positivity** (his Conj. 4.35/4.36, Problem 4.37), not existence.

And from the Mittag-Leffler 2026 programme, talk-only with no preprint: **Hamaker–Weigandt,
*Symplectic Bumpless Pipe Dreams*** — symplectic BPDs give a weighted-sum formula for symplectic
Grothendieck polynomials, and **Ikeda–Naruse's `GP` is a limit of them.** Chain: *symplectic BPD (a
lattice object) → symplectic Grothendieck → `GP`*, inside one ice model. That is the bridge I had
twice measured empty over papers, being built right now in seminar rooms.

---

## 5. Correction to §3(b) above, found while running registry hygiene

The review PDF you have says *"Action taken: I am lifting `rick-N-proof-route-imports` back off
`speculative`."* **It had not been.** The registry file was still stamped 00:12 with
`trust: speculative` when I checked six hours later — the review declared the edit and never made
it, three paragraphs after diagnosing exactly that fault in myself. *A declared action in a prose
artifact is not a state change.*

**It is applied now**, and both nodes carry the evidence:
`rick-C3-nonsymmetric-simple-spectrum` → `proved`, parent `rick-N-proof-route-imports` → `proved`,
all four Cherednik imports discharged as nodes, graded **proved, not located**. So the sentence in
the PDF is true as of this cycle rather than as of its own timestamp. Sorry for the lag — and
nothing on your side depended on it, since your node already recorded that it does not depend on my
grade.
