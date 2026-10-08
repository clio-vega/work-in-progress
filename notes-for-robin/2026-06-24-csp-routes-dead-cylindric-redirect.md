# For Robin — both CSP routes to the order law are dead; the redirect is your cylindric thesis path

*2026-06-24 (narrative; system 06-14). Dream consolidation of CODE Jobs A/B + browses 06-22/06-23.*

## Two negatives that save effort

1. **The CTT domino-CSP (Colmenarejo–Tenner–Thompson 2602.23343) cannot prove the order law.** I'd
   crowned it last week as the surviving route to a 4th proof. Job A killed it cleanly: domino tableaux
   exist only on **tileable** shapes (empty 2-core), which is exactly where `ord_{q=−1}G_λ=0`; and
   `|SDT(λ)|` factors through the **2-quotient** (verified, 0 fail). The order law reads the **2-core** —
   the complementary half. The discriminating staircases δ_k aren't even in CTT's domain. Both external
   CSP candidates (odd-content, CTT-maj) are now dead by one cause: neither reads the 2-core.

2. **The even-|J*| fixed-point-free involution is NOT Sawin's adjacent pairing.** On the first family
   with `|J*|=4` (three-row c=3), the leading-unit residues mod (1+i)² alternate by `j mod 4`. Pairing
   adjacent generators (`j↔j+2`) pairs `1` with `i` and does not cancel; the real involution toggles the
   **top** generator (`j↔j+4`), pairing equal residues. The Pfaffian (Fischer–Gangl / Rains–Warnaar
   bounded Littlewood) survives as the symmetric-function home, but it must realize a residue-class
   pairing.

## The redirect — and why you'll like it

A CSP/structural home for the order law must read the **2-core**, which means **spin/cospin** (Littlewood
t=2), or — the prime candidate now — **Dobner's cylindric level-2 fusion** (2605.20540). Reinterpreting
`G_λ=⟨s_λ,(p₂+ie₂−e₂)^m⟩` in the level-restricted (cylindric) Fock space: the conjecture is that
`ord_{q=−1}G_λ` is a **level-2 fusion (cylindric LR) multiplicity**, and `ord_{ζ_d}G_λ` tracks level-d
truncation — which would explain *why the order law is d=2-only* (level 2 is where the affine/cylindric
truncation first bites). **This is your cylindric-plane-partition thesis path connecting directly to my
ζ_d / 2-core work.** It's the most promising structural lead I have, and it's seed-native.

## Status of the closures (all standing, all Lean-checked at the arithmetic core)

The three-row even-|J*| program now has hook, two-row, and three-row c=1/c=2/c=3 all closed. c=3 is the
first family with a real `|J*|=4` (two-generator box). The c-pattern is fully legible: inhomogeneous tip
`(2c)!·C(j,2c)`, generators `2,…,2c`, modulus stays mod 4. The general `e₂ mod 2` wall is the only thing
between here and the full general-λ statement.

## One ask (carried from 06-14): paper amendment

The Compensation Lemma and the c=2 Number Lemma, as stated "for all j" in the draft, are false under the
standard `padicVal 0 = 0` convention without the restriction their proofs silently use (Lemma C needs
`D≠0`; Number Lemma needs `j≤F+3`). Both hold in-application, so the closures stand — but the statements
should be amended. Details in `for-robin/2026-06-14-compensation-lemma-lean.md`.

## If you want to point me somewhere

Highest-value next probe is the **Dobner level-2 fusion test** (cheap-medium code). After that, three
MathOverflow questions are answerable with machinery I already have (MO#509068 hook-character vanishing;
MO#404938 Bowman LLT-vs-graded-Specht n=2; MO#424601 Alexandersson forest↔skew-SYT) — public artifacts in
my exact wheelhouse if you'd like me to write one up.
