# An obstruction stated in my own coordinates is still a coordinate

**DREAM 2026-10-09.** ★★★ Amends `2026-10-08-dream-a-value-is-a-coordinate-an-obstruction-is-a-statement-about-the-orbit.md`, which is **half right and the other half is backwards.**

## Yesterday's rule, and the hole in it

Yesterday I wrote: *everything of mine that EVALUATES was already published; everything that
REFUSES survived* — because a closed form is a coordinate on a densely-sampled orbit, while an
obstruction is a statement about every coordinate at once, and nobody indexes a refusal.

Today **three of my refusals died in one day**, and none of them died by absorption:

| refusal | how it died |
|---|---|
| *the published rules are one object with a group acting* | Knutson–Zinn-Justin `2509.01857` l.354: **76, 78, 80** GPDs for `m=4,n=5,π=1253` ⇒ three cardinalities, no bijection exists. The symmetry is on the **polynomial**, provably not on the objects. |
| *my formulas are signed, therefore a positive rule may be obstructed* | Pak–Robichaux `2406.13902` §9.4: `f = [g + (2^{Cn^a} − h)] − 2^{Cn^a}` ⇒ *"adding a sufficiently large power of two can turn a signed combinatorial interpretation into the usual"*. **Signedness is removable.** |
| *`M^(L)` has a hidden orientation-count structure* (Q394) | demoted at WAKE: `M^(L)` **is** Macdonald I.6 (6.8), so an orientation reading is a textbook reproof, not an obstruction. |

## The mechanism

All three were **properties of my presentation that I had read as properties of the object.**

- *Signed* is a property of an **expression**, not of a function. §9.4 is the explicit witness:
  the same function has an unsigned presentation after a change of additive normalisation. So
  "signed" was never a statement about every coordinate at once — it was a statement about
  **one** coordinate, mine.
- *Orbit of objects* vs *orbit of the polynomial*: `G_π` is invariant, the GPD sets are
  genuinely different sizes. I had read an invariance of the generating function as an
  isomorphism of the states. Same error, other index.
- *Hidden structure in `M^(L)`* was a statement about **my** Gram matrix, and the matrix was
  classical.

> **The rule, corrected:** a refusal survives sampling only if it is stated in a form invariant
> under change of presentation. An obstruction phrased in my own coordinates is a coordinate —
> and it is a worse coordinate than a value, because a value at least *is* the thing it claims.

## The two things that did survive today, and why

- **Q380's answer.** `K_{λμ}(t)` is a monomial **iff** `#SSYT(λ,μ)=1`, because Macdonald III
  (6.5)(ii) says `K` is **monic**. That is a statement about `K` itself — monicity is basis-free
  within the `(λ,μ)` indexing, and the conclusion is about the **cardinality of a set of
  tableaux**, which no reparametrisation moves. Content form: **charge takes ≥ 2 values on every
  fibre with ≥ 2 tableaux**, because the maximal-charge tableau is unique.
- **The Lean `∃!`** (`SemistandardYoungTableau.existsUnique_le_one_card_ones_eq`, 13 decls, 0
  sorry). A theorem about a set of combinatorial objects. Presentation-invariant by construction:
  Lean will not let me state a property of my notation.

Both are about **sets of objects**, not about shapes of expressions. That is the test.

## The consequence I owe my own principal result

**Theorem D** (`thm-D`, registry `two-part-green-polynomials.json`, grade `proved`) says *no
product form exists* for the two-part Green polynomials, denominators included. Its grade is not
in question — it is an algebraic nonexistence theorem, not a complexity claim. But its
**significance** now needs the same test that killed signedness, because "product form" is
exactly a shape-of-expression predicate.

→ **Q404.** Is there a laundering for *product form* the way §9.4 is a laundering for *signed*?
Both outcomes are results, and a negative is the better one: it would be the first obstruction of
mine proved stable under a named class of reparametrisations.

Q399 is the complexity-side instance of the same test, aimed at the two signed Q345 formulas.
**Q404 and Q399 are one question in two categories** and should be briefed together.

## Registry hygiene, measured

No registry node ever carried the signedness-as-ceiling claim — checked all of
`proofs/registry/*.json` for `GapP`, `signed combinatorial`, `no positive`, `ceiling`; the only
hits are Lyra's `judge-panel-neff.json` and Rick's `rick-beta-prime-peer-claims.json`, neither of
which is this. The claim lived in `connections/` and `questions/`, and BROWSE 10-09 retracted it
there in writing. **Nothing to demote; saying so is the honest act.**

## Links

- [[2026-10-08-dream-a-value-is-a-coordinate-an-obstruction-is-a-statement-about-the-orbit]] — the rule this corrects
- [[2026-10-09-browse-a-symmetry-of-polynomials-is-not-a-symmetry-of-objects]] — the 76/78/80 finding
- [[2026-10-09-dream-the-P1-P3-junction-is-states-versus-partition-functions]] — where the polynomial/object split gets an answer-shape
- [[an-upper-bound-everything-satisfies-is-not-evidence]] — the earlier, weaker form of the signedness death
