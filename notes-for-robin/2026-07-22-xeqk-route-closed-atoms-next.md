# For Robin — X=K route for `(†)` is CLOSED; atoms route is next

*Wake cycle 2026-07-22. Full write-up of what today's probes settled.*

## TL;DR

Yesterday's dream journal proposed Gerber–Ion–Lecouvey–Lenart 2607.03966 (X=K, uniform for classical affine types via Koornwinder dual Cauchy) as a candidate published home for `(†)`. Today's two parallel probes both close this line.

**Result:** GILL's X=K identity puts the *modified* Hall–Littlewood `Q'_μ` on the RHS (Kostka–Foulkes-positive, `Q'_μ = Σ K_{λ,μ}(t) s_λ`). Clio's target `M^{(3)}_{(2,2,0)} = (1+t)·P_{(2,2,0)} = Q_{(2,2,0)}` is the *classical* HL `Q_μ` (signed Schur expansion including `−(t+t²)·s_{(2,1,1)}`). These are dual under the Macdonald involution `ω_t` but not equal, and no scalar-t factor, level restriction, or Cherednik–Ram post-symmetrisation reconciles them.

In type A, GILL's Thm 3.1 is a re-proof of Nakayashiki–Yamada 1996, which already gives `Q'_μ`. The DAHA machinery is not a new bridge — the Bernstein `Y^λ` presentation there is used to prove `X = K`, not to compute `v_μ · P_μ`.

## What both probes found

- **Probe A** (naive one-dim sum for `B^{2,1}⊗B^{2,1}` in `A_2^{(1)}` at level 3): result lives on Schur support `{(4),(3,1),(2,2)}` (all `λ ≥ μ` in dominance); target lives on `{(2,2),(2,1,1)}`. No scalar identity, no level restriction fixes it.

- **Probe A-2** (four rescue tests): `ω`, `ω_t` (four candidate `p_k` substitutions), `∑_{S_3} T_w` post-symmetrisation (which is scalar `[3]_t!` on any symmetric polynomial), and a check of what NY actually gives. None connects X=K RHS to `M^{(c)}_μ`.

- **Paper read** (GILL §3, lines 884–1046 of the PDF): Theorem 3.1 is the classical Nakayashiki–Yamada identity `X_{λ,μ}(q) = K_{λ',μ'}(q)`. The type-A case is a *reproof*, not a new identity.

A subtle bug also surfaced in Probe A: the raw one-dim sum over the 9 crystal elements is `t²·s_{(2,2)} + t³·s_{(2,1,1)}` — the tabloid restriction to classically highest-weight vectors is what gives `Q'_μ`. But this doesn't change the verdict on the naive bridge.

## What `M^{(c)}_μ` actually is (its published home)

The correct home is **van Diejen–Emsiz–Zurrián 2305.01931 Cor. 4.2** (Adv. Math. 392, 2021). This IS the cylindric HL Pieri identity Clio has been working with. Under `M^{(c)}_λ = v_λ(t)·P_λ` it matches Korff's cylindric HL Pieri in the interior of the alcove (07-21 ter verification, 34/34 with `v_λ/v_μ` cocycle at boundary).

## The path forward: atoms

Both agents independently recommend the **atoms route**. Blasiak et al. 2506.09015 (nonsymmetric flagged LLTs in Demazure atoms, conjectural) + Assaf-González 1901.07520 [was mis-cited as A-G 2512.19814] (local edge criterion for Demazure-union) is the composed strategy. `(†)` LHS is likely the affine Demazure sum, and if it decomposes into a *union of atoms*, Assaf–González's edge-local criterion may close the reduction combinatorially without needing to build Bernstein `Y^λ` in Python.

Probe B (running in background as I write this): compute the Demazure-atom decomposition of `M^{(3)}_{(2,2,0)}` in 3 variables, test for t-positivity, check the Assaf–González criterion.

## Loose ends I'm carrying

- **PAT still expired** — Probe A findings, this note, and the 07-22 tdagger tex are all local-only.
- **Correction request:** the 07-26 memory anchor for GILL claims the identification is a "sharp conjecture" — that language should be softened to "candidate identification, tested and closed today." I've already updated MEMORY.md with a top-line negative entry.
- **Rick** still can't be replied to; if any of this changes what you'd want him to know about the sprint, let me know.

## Why this is actually good news

Falsifying the X=K identification cheaply is a `browse cycle → probe cycle` doing what it should: turning a plausible external anchor into a hard yes/no. The atoms route is the natural next candidate, and it has three independent pieces of published work (vDEZ, Blasiak, Assaf–González) — same combinatorial house. And the ω_t / Q vs Q' duality that emerged today may itself be structurally useful — it's the "positive shadow" of `M^{(c)}_μ`, which is worth understanding regardless of `(†)`.
