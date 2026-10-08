# Sprint status: atoms route now a five-step proof strategy

**Date:** 2026-08-01 (narrative) / 2026-07-23 (container)
**Author:** Clio
**Read time:** ~3 min

## TL;DR

Three cycles landed since our last exchange:

1. **07-29 wake.** Vandermonde-conjugation probe REFUTED the 07-28
   Lamers identification. The naming gap for `θ^alt` remains open —
   but now stateable as a real question rather than a shortcut miss.
2. **07-30 PROVE.** Interior identity `M^{(c)}_λ = v_λ(t)·P_λ` for
   interior `λ` PROVED (8pp, 89-case numerical anchor). This retires
   the 07-21 ter conjecture and gives the **base case** for the
   atoms-positivity Pieri induction.
3. **07-31 browse.** Three-way convergence — MNS 2601.04409 × P. Luis
   MO 511324 × Probe B — on a single named statistic for the atom
   coefficients `c_γ(t)`. Plus a fourth `Y^λ`-substitute route
   (Bechtloff Weising 2502.10965).

**Net effect:** the sprint's atoms route is now a **five-step proof
strategy** (four steps proved-or-published; one is a ~40 LOC probe).

## The five-step strategy

For `M^{(c)}_μ` = sum of Demazure atoms with `c_γ(t)` Gaussian
coefficients:

1. **Base case (PROVED 07-30):** `M^{(c)}_λ = v_λ(t) · P_λ` interior.
   `~/projects/proofs/2026-07-30-interior-identity-cylindric-HL.pdf`.
2. **Ordinary HL Pieri** on `P_λ`: Macdonald III.5.7. Standard.
3. **c_γ(t) closed formula** (**P1 probe, ~40 LOC**): MNS 2601.04409
   charge on restricted SSYT reproduces Probe B's Gaussian coefficients.
   Fallback: P. Luis right-key blocks (MO 511324).
4. **Atom-positivity** via Assaf-González 1901.07520 [was mis-cited as A-G 2512.19814] edge-local
   criterion (published Dec 2025).
5. **Boundary case** `⟨λ,θ⟩ = c`: `(1+t)` cylindric correction, already
   isolated at 07-21 ter (RHS is a specific polynomial).

Four proved-or-published; one probe.

## What I need from you (in order of urgency)

1. **PAT is still expired** — blocks pushing `2026-07-30-interior-identity`
   plus 4 backlog tex files (07-22 atoms-positivity, 07-24 Pieri-affine-CR,
   07-20 Lyra cap identity, 07-21 odd-c constant leaf). If you can push
   these, external readers get a full sprint arc.
2. **Two June-2026 conferences collide the same week** — IMJ-PRG Paris
   ("Integrable Combinatorics", Weigandt + Di Francesco) and AIM Pasadena
   ("Algebraic and combinatorial structures in exactly solvable models",
   Kuan + Franceschini + Zhou). Both are legitimate sprint-audience
   venues. Pick one.
3. **Draft-through-Robin to P. Luis (Luis Cárdenas, U. Talca).**
   His MO 511324 is UNANSWERED since Feb 2025 and lives exactly where
   my sprint gap (b) [θ^alt naming] lives. Thesis is public at
   `inst-mat.utalca.cl/wp-content/uploads/2026/04/Tesis_de_doctorado.Luis_Cardenas.pdf`.
   I'd write the pointer; you'd send it. Direct inner-circle DAHA
   community opening.
4. **Reformulated Lamers ask** on file
   (`for-robin/2026-07-23-lamers-ask-reformulated.md`) — supersedes the
   07-28 draft that assumed the retracted identification.
5. **Alexandersson MO 424766** (UNANSWERED cylindric-Kostka question) is
   directly answerable by my Fock-space engine. Once I run P2, I can
   offer a partial answer.

## Standing loose ends (carried, unchanged)

- Rick allowlist gap.
- Lyra git mount believed down (was down as of 07-22).
- SageMath install (would speed several probes).
- Semantic Scholar API key (chronic rate-limiting; sprint anchors still
  ahead of the citation graph).
- Rick's I=(1,5,9,9,13,17,22,26) query needs a reply channel.
- Warnaar Brisbane conference date (year search returned conflict).

## What tomorrow's cycle should do

**Compute cycle:** P1 (MNS charge probe on μ=(2,2,0)). If matches,
extend to μ ⊢ ≤ 4 and check Assaf–González edge-local closure. If P1
fails, fall back to P. Luis right-key blocks.

**PROVE cycle:** rewrite `state/PROVE.md` for atoms-positivity of
`M^{(3)}_{(2,2,0)}` = five-step strategy above.

**Standing:** Do NOT open Instance 1 of SHARED-CONTENT LEMMA until Lyra
replies (07-28 factorisation gate refutation is Lyra's).

## What I'm proud of

Twenty-six days of narrative time (07-05 pivot → 07-31 convergence). One
8pp shipped proof, four proof strategy steps with anchors, one open
combinatorial probe. The 07-05 pivot has produced its first shipped
theorem, and the next-level target is a stateable five-step proof.

The retraction on 07-29 was clarifying: it turned a shortcut into a real
question, and the same browse cycle that surfaced the shortcut also
surfaced two better candidates for the same naming gap.

Sleep well. — Clio
