# For Robin — 2026-07-25 (bundle: BHMPS ω-duality + community news + asks)

*Bundle four things for the next PAT-cleared push. First item is the
research-relevant one; the other three are lower-priority but worth
mentioning together.*

## 1. BHMPS 2509.24040 is working the ω-dual of our conjecture

Blasiak-Haiman-Morse-Pun-Seelinger have a paper from September 2025
(Sep 24, 2025 → arxiv 2509.24040) titled *A nonsymmetric compositional
shuffle theorem via `H_{η|λ}`*. In it they conjecture **atom-positivity**
for their modified nonsymmetric Macdonald `H_{η|λ}` — expansion in
Demazure atoms with non-negative coefficient polynomials.

**This is ω-dual to the c_γ(t) ∈ ℤ_≥0[t] conjecture I've been
working.**

Two heavyweight teams working the same conjecture from opposite sides
of the ω-involution. Two possibilities:
- **Passive.** If BHMPS prove atom-positivity, my atoms conjecture
  follows automatically via ω-transport.
- **Active.** If we send them a short note pointing out the ω-duality,
  it's high-impact — potentially opens collaboration and gives our
  atoms-side machinery (nil-Hecke A^alt_γ, chain-regime `[N−L]_t`)
  visibility to a heavyweight team.

The specific connecting claim: **your `transfer_operators.py` computing
`lr_via_transfer(λ)` and BHMPS's `H_{η|λ}` construction on ω(λ) should
compute ω-related coefficient data.** I haven't run the test yet — but
it's a small probe. If you're interested in a Blasiak note, I'll draft
one and you can review.

## 2. Community news — Stanley-Gasharov claw-free Schur-positivity conjecture fell

MathOverflow question 513515 (asked 2026-07-23). Two independent
counterexamples posted this week:
- Prajapati (via GitHub search)
- Matherne-Morales (via ChatGPT 5.6, of all things)

Both verified by Darij Grinberg in the answer.

**Jose Morales is one hop from you** (Morales is with Aguiar and Ceballos
in the combinatorial-Hopf-algebras community that intersects your
symmetric-functions territory via the Schur-positivity literature). If
you didn't hear about this yet, you might want to.

The meta-observation: positivity conjectures in this area are turning
out to be *finite-checkable* — brute-force + LLM-augmented search
can win. Might be relevant to how we approach the atom-positivity
statement.

## 3. Ask — Matt Samuel affiliation?

Matt Samuel keeps appearing as a repeat asker on Schubert-side
Bruhat-descent MathOverflow questions (MO 453974, 454322, 470160,
513337, 469006, 471198, 481281 over the past ~2 years). He is working
the CS-side of the same Bruhat-descent axis I'm working on the HL
side.

Do you know his affiliation? He might be a natural collaborator when
the chain-regime formula extends to the collision regime — his
questions have exactly the flavor of "which Bruhat-descent structures
determine which polynomial invariants."

## 4. Ask / mention — Schilling summer contact windows

Anne Schilling's 2026 summer schedule (from her ICERM 2025 slides +
follow-up talks I've been tracking):
- **IMJ-PRG Paris**, June 15–19 (mini-course "Crystals and symmetric
  functions")
- TCA Guimarães (workshop)
- CMND Notre Dame (visit)
- Simons Stony Brook (visit)
- **Mittag-Leffler** (she is organizing a workshop)

**Five contact windows.** Brauner-Daugherty-Mason-Schilling
2607.12232 (Jul 2026) is one face of the polytope I'm mapping — the
crystal side. If we want to make contact with the Mason-Schilling
crystal-skeleton programme, those five windows are the natural
opportunities.

## What I proved this cycle (for context)

*(One-line summary — full proof at
`~/projects/proofs/2026-07-25-bruhat-chain-regime.pdf`, 9pp;
for-Robin memo at
`~/projects/memory/for-robin/2026-07-25-bruhat-chain-regime-proved.md`
already sent.)*

**Chain-regime closed form**: for μ = (a^p b^q) with min(p,q)=1,
`c_{γ(L)}(t) = [N−L]_t`. Unconditional for d ≤ 2, conditional on
V_{<μ}-consistency for d ≥ 3 (verified computationally on 25 cases).

The rigorous heart is the **Chain-Extremal Coefficient Lemma**, which
holds for all d. The BHMPS ω-duality above sharpens the pitch: if the
chain-regime formula holds via ω-transport on the shuffle side too,
it's the same theorem in two languages.
