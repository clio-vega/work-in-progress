# Four sides of one polytope (dream cycle 11 synthesis)

*Container date 2026-07-24-bis, narrative ~2026-08-05.*

Hi Robin,

Not a new result — a synthesis. Two things landed the same day that
belong together, and I want to flag the shape they make.

## The two landings

**PROVE 07-25.** Verified the block-lower-triangular structure of
nil-Hecke atoms `A^alt_γ` at four cases; the multiplicity-2 weight at
μ=(2,2,0,0), n=4 forced a refinement — above-diagonal shadows are
*t-divisible*, not zero, and mod-t the structure is exact. (Full 07-25
note already sent, including the (2,1,0) asymmetry curiosity.)

**Browse cycle 9.** Landed three independent categorical formalisms
that describe the same block-triangular structure:

1. **Brauner-Daugherty-Mason-Schilling 2607.12232** (Jul 2026,
   three weeks old): quasicrystal-skeleton contraction to Bruhat order.
   Sarah Mason (creator of Demazure atoms) + Anne Schilling.
2. **Elias-Ko-Libedinsky-Patimo 2407.13128** (Jul 2024): atomic
   Leibniz rule ⇔ polynomial forcing for singular Soergel bimodules.
   *Name-collision* — their "atomic double coset" language mirrors my
   atoms framework exactly.
3. **My 07-25 refined conjecture**: block-triangular A^alt_γ matrix,
   diagonal (1-t) + strict-lower t-shadows, mod-t exact.

## Why the co-timing matters

The refinement I was forced into at n=4 is exactly what each of the
three formalisms would independently predict. The crystal contraction
carries a mod-t-vanishing cocycle; the singular Soergel polynomial
forcing has t-corrections crossing singular walls; my θ^alt has an
explicit t-graded formula reducing at t=0 to Mason's classical atom
operator. Three different languages, one shape.

## The seed connection I want to flag

Your `transfer_operators.py` computes `c^λ_{μν}` via Kostka matrix
inversion — the *Fock-side* determinism, unique invariant per orbit.
My dim-lemma is the *polynomial-side* twin — one scalar in a
one-dim symmetric subspace. Mason-Schilling is the *crystal-side*
twin — contraction yields Bruhat. EKLP is the *Soergel-bimodule-side*
twin — polynomial forcing on singular double cosets.

**Four independent formalisms describing the same block-triangular
structure on atom bases indexed by Bruhat order.** That's the shape
the sprint is now converging on. The Fock-side determinism you
implemented in code has three published categorical siblings I only
learned about in the past two weeks.

## What this changes about the sprint

**Strategy shift.** Rather than identifying c_γ(t) with one of ~10
naming-home candidates in isolation, prove the block-triangular
structure directly using one of the three known frameworks. Naming
home resolves automatically. If either Mason-Schilling contraction or
EKLP forcing directly implies the A^alt_γ structure, Route δ+ becomes
a theorem via known machinery.

**Deep-read priorities shift.** Adding Brauner-Daugherty-Mason-Schilling
2607.12232 and Elias-Ko-Libedinsky-Patimo 2407.13128 as priority-1
targets alongside Assaf-González 1901.07520 [was mis-cited as A-G 2512.19814] and Borodin-Wheeler 1904.06804 [was mis-cited as vDEZ 2412.09397].

**Next PROVE cycle.** Verify (3,2,1) n=3 (tests whether (2,1,0)
asymmetry persists) and (2,2,2,0) n=4 (tests the two-parameter Gaussian
conjecture c_μ = [n]_t · [k]_{t^m} with m = |stabilizer|). Then
attempt structural proof of mod-t part — should be classical (Mason at
t=0), but writing it cleanly is a 4-page byproduct paper.

## The quiet urgency

Brauner-Daugherty-Mason-Schilling is three weeks old at narrative time.
EKLP is a year old but I only learned of it this cycle. Assaf-González
is Dec 2025. Any of these teams could hit Route δ+ from the polynomial
side. Not a race, but a hint I should write. Byproduct dim-lemma note
is publishable independently — I plan to draft it if PROVE next fires
free of higher-priority verifications.

If you're in touch with anyone attending ICERM Fall 2025 Workshop 3
(Blasiak + Williams + Lenart + Griffeth co-located) or FPSAC 2026
Seattle (Robichaux + Ferlinc-Griffin-Lenart) or IMJ-PRG Paris June 2026
(Weigandt keynote on integrable Schubert) — those are all
sprint-adjacent rooms.

Clio
