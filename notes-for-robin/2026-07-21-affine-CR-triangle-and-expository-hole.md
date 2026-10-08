# Follow-up on the 07-05 Steer: Infrastructure for Cylindric CR Is Assembled

*For Robin. 2026-07-21 dream cycle. Follow-up to 2026-07-20 note on Demazure re-entry
and the sharp affine Cherednik–Ram conjecture.*

## TL;DR

Yesterday's browse produced three pieces I did not have on 07-13, and they slot together into
exactly the infrastructure my affine Cherednik–Ram conjecture needs. The conjecture I stated on
07-20 has become a concrete ~two-session PROVE program with published anchors on all sides. I also
noticed a genuine expository niche you may or may not want me to fill.

## The infrastructure triangle

Three separate research programs converge:

1. **Cylindric HL as object.** *Korff–Palazzo, "Cylindric Hall–Littlewood functions and
   Verlinde-type algebras", Algebraic Combinatorics 3(4), 2020* + *Korff 1110.6356* define
   `P^{(c,k)}_μ(x_1,…,x_n; t)` at level k with a deformed Verlinde algebra whose structure
   constants are WZW 3-point fusion coefficients. This is the RHS of my conjecture.
2. **Affine Demazure crystals as LHS side.** *Assaf–Gonzalez arXiv:2002.04141* proves nonsymmetric
   Macdonald at t=0 **are** affine Demazure characters (type A). The construction gives the affine
   embedding `E_0` that grades finite Demazure sub-crystals into the level-k affine crystal — the
   level-k "wrap" my LHS `T̃_w` needs.
3. **Target positivity, unconditionally proved on rectangles.** *Warnaar arXiv:2511.17034* (SIGMA
   22 (2026) 062, 50 pp.) proves affine dual Jacobi–Trudi identities for so_{2n+1}/sp_{2n} on
   rectangular partitions of maximal height, giving q,t-Rogers–Ramanujan / Andrews–Gordon / GGA as
   characters of standard affine modules. Rectangular case is proved, so restricting to type A gives
   a direct testbed for my conjecture at μ = (k^n).

Before yesterday all three were on the horizon in isolation. Two agents (arXiv + web) surfaced them
as a triangle. My sharp conjecture from 07-20 is the missing edge that binds them into one
theorem. Full connection file at
`memory/connections/2026-07-21-affine-CR-infrastructure-triangle.md`.

## Direct testable prediction

If my affine CR conjecture holds, its **rectangular level-k instance μ = (k^n)** must reproduce the
type-A restriction of Warnaar's proved so/sp identity. That is a *proved* anchor, not a conjectural
one — the first concrete cross-check my program has ever had beyond my own 21/21 linear
verification. I can run it as soon as I have Korff 1110.6356 as text (WebFetch fails on the
FlateDecoded PDF; needs `wget` + `pdftotext`).

## The 2-adic shadow, briefly

The 07-20 browse also handed me a plausible mechanism candidate for the 2-adic shadow: **q-Dwork
congruences** (*Kartik–Smirnov arXiv:2505.04039*). At q → 1 these give a p-adic recursion on
integer coefficients of K-theoretic vertex functions — the shape of my Number Lemmas as a *whole
family theorem* rather than a case-by-case content bound. This is separate from the CR work; I
mention it because it's the first named-paper candidate for "why the shadow exists" I have found in
17 months. Formal open question is what I call the **Bridge Theorem** —
`⟨s_{(a,b,c)}, h_1^{2m-2j} e_2^j⟩` as a matrix element on cyclic-quiver Nakajima K-theory. Without
it, this is still a nearby analog. Connection file:
`memory/connections/2026-07-21-q-dwork-is-the-2adic-mechanism.md`.

## An expository niche I noticed (asking before writing)

Alexandersson's SymmetricFunctions.com wiki has a well-maintained **cylindric-Schur** page (with
Postnikov, Lam, McNamara/Lee) but **no cylindric Hall–Littlewood or cylindric-Macdonald page**.
Given the Korff–Palazzo + Warnaar + Assaf–Gonzalez + IMSS story now visible, this is a genuine hole.
A ~15-page `~/projects/expository/cylindric-hall-littlewood.tex` synthesising the four sources
would:

- give me a canonical reference to cite in the affine CR conjecture writeup;
- force me to state the RHS `P^{(c,k)}_μ` precisely before I attempt the conjecture (right way
  round — expository before proof, matches my usual `/expository` → `/prove` flow);
- fill a public gap on a site the community actually reads.

**Question for you:** worth the ~two focused sessions, or better to keep my head down on the
conjecture itself? I lean *do it*, because the definitional discipline of writing it up is exactly
what my last PROVE session was missing (I could not state the cylindric CR conjecture with the
right `T̃_w` because Korff was WebFetch-blocked). But it is your steer.

## Loose ends still standing (unchanged from 07-20)

- Whitelist for Lyra: `scot.macbeth20@gmail.com` (a colleague of hers, mentioned in her Day 100
  email).
- Two `curl` requests are queued for the Schilling Paris 2026 PDF (from feeds.md 07-11).
- SageMath is not installed in the container, contra CLAUDE.md tools list. Both compute agents on
  07-20 hand-rolled Python. Real infra bug — either install Sage or update CLAUDE.md.

Nothing urgent. All good on my end.

— Clio
