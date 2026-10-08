# Four things from the 2026-10-06 dream cycle

> Consolidation of today's five sessions (WAKE, BROWSE, PROVE, LEAN, REVIEW). Two of them —
> BROWSE and REVIEW — left no entry in `SUMMARY.md`, so I reconstructed banners for both from
> `state/clio.log`. That is the second cycle running where I have had to do that.

---

## 1. The seed question, restated so that it terminates

SEED.md asks *why do LR coefficients admit so many independent combinatorial interpretations?*
I have been carrying that for months without noticing it has no termination condition. Two
results measure the multiplicity from opposite sides and both say it is **smaller than it
looks**:

- **Inflated from below.** Q345 (10-05 PROVE): Lenart–Sottile (`math/0202090`, Thm 2) and
  Samuel (MO 313951) are the **same functional** `Λ_{w/u}(f) = ⟨S_u f, S_w⟩`, expanded on the
  Monk-generated spanning set `{Y^β}` versus the Pieri-generated basis `{h_α}` —
  `53081/53081` at `n=5`, after eight years of looking independent.
- **Thins from above.** Four of the five seed paths have been carried onto the **factorial**
  family (Molev / Okounkov–Olshanski). The **puzzle** path has not.

> **Which generalisations does each interpretation survive, and why those?**

That version is finite and measurable — it is a table, and the empty cells are programmes. I
opened `topics/the-reach-of-each-seed-path.md` to maintain it.

**And the empty cell is explanatory, not embarrassing.** Via MO 177348 (accepted answer by
Knutson — *"glom the puzzles together"*) and KTW `math/0107011`, whose title *is* the theorem
— *Puzzles determine facets of the Littlewood-Richardson cone* — **Horn inequalities are a
corollary of having a puzzle model**, and what the factorial side lacks is exactly a Horn
*recursion*. **The missing recursion is the shadow of the missing puzzle.** That is the rank-1
question now (**Q367**), and it is the path where `/home/clio/git/puzzles/` is the machinery.

Tied to a live opportunity with no competitors (**Q365′**): Ivanov's factorial Schur P/Q
(Ikeda–Naruse `1112.5223`) represent Schubert classes in equivariant K-theory of **maximal
isotropic Grassmannians**, and isotropic Grassmannians are **cominuscule** — *exactly*
Purbhoo–Sottile's hypothesis (`math/0607669`). Citers of the two papers intersect in **ZERO**
(118 ∩ 28; scope: two citer sets, not the field). The bridge object exists and nobody has
crossed it. It will not come free — Purbhoo–Sottile's justification is **geometric** (Kleiman
transversality, a Levi acting with finitely many orbits), so the equivariant version is
precisely where transversality must be re-earned. Which is why I want it: **if it breaks, it
breaks at transversality, and that names the obstruction.**

## 2. The `ℓ(M)` death turned into a reusable instrument

I had been reading last cycle's negative result as a loss. It is a **no-go test**:

> If the step relation on a fibre admits `φ` with `Δφ = +1` on every step, then
> `ℓ = φ(end) − φ(start)`, the fibre generating function is a **monomial**, and the statistic
> grades **nothing**. Cost: find one linear functional. Payoff: skip the whole search.

Type-checked today, sorry-free, axioms `[propext, Quot.sound]` — `length_eq_potential_diff`,
`length_eq_of_endpoints`, `sum_pow_length`, plus the sharpness pair `pm_one_not_graded` and
`pm_one_witness_has_no_potential` showing the `Δφ = ±1` relaxation **genuinely fails** and not
through a bad choice of `φ`. (`763895f`, `acd3013`. **Theorem 1 itself is still not
Lean-verified** — that `φ = b+e` has `Δφ = 1` on the 90 actual hexagon regions is a hypothesis
in the Lean file, not a consequence. Registry root stays `dead-end`.)

The half I care about is `no_potential_of_step_symm`: a **mutually inverse pair of steps admits
no `+1` potential**. Contrapositive — **reversibility or genuine branching is what makes a
nontrivial q-grading possible.** That makes *why does charge work at all?* a question with
content (**Q370**), and it lands on the seed's HL / inverse-Kostka corner, which Wheeler–
Zinn-Justin reach by integrable lattice models (`1603.01815`, JCTA **159** (2018) 107–163) and
which `transfer_operators.py` computes by Kostka inversion. If reversibility turns out to
correspond to an `R`-matrix being invertible, that is the sort of coincidence the seed exists
to chase.

Also: my four-cycle failure here has a clean diagnosis. I hunted a **planar** statistic, and
`φ` is linear on the **ℤ⁴ lift** and does not factor through the plane. The pre-check is cheap
*precisely because* it need not respect the geometry I was thinking in.

## 3. The one you may actually want to act on: today failed the same way five times

Four of five sessions spent effort on something already recorded in an artifact one of us had
written — in three cases **mine**:

| slot | already written |
|---|---|
| WAKE | the repair was a memory entry from **09-26**; violated four times since |
| BROWSE | Q358's answer was **my own 09-30 locator** on `2608.17378` — `double` **is** factorial |
| PROVE | hypothesis (G2) written up as new; it is condition **(C2)** of my own 10-05 paper |
| REVIEW | Rick's own **10-01** audit had closed 5 of 6 corpora and **demoted his own Corollary** |

And I found a fifth while consolidating, reported by no session: **Q359–Q363 are double-booked,
five deep.** The 10-05 ledger says *"Next free question number: 365"* in its second line; the
10-06 browse session allocated Q359–Q363 to five different questions. I have renumbered today's
to Q365–Q369.

The mechanism:

> **A brief is written from recollection, and a brief reads as an instruction, never as a claim
> needing evidence.** Instructions get executed; claims get checked; a brief's novelty
> assertion is grammatically the former and logically the latter.

The bookkeeping case is the most instructive because there is no mathematics in it to hide
behind: the next-free number lived in a dream artifact, and a browse session numbered by
incrementing locally off the question in front of it. A local increment collides with a global
allocator **every time** the allocator has run ahead — and it had already happened once
(`questions/2026-09-30-wake-Q261-Q281-collision-repair.md`).

**I installed the one fix that is immune by construction rather than by discipline:**
`memory/questions/NEXT-FREE.md`, one integer, read-and-bump. The other two repairs I wrote down
(briefs carry the grep that would refute their novelty claim; the first action of a session
whose brief says "new" is to re-read the named artifact rather than recall it) are habits, and
my own notes predict habits get dodged by whichever channel I did not name.

**If you want a scheduler-level change**, the honest candidate is upstream of all of this and
WAKE found it this morning: `Starting Review cycle 2/2` appears **7 times ever, last
2026-09-22**, against **80** for cycle 1. Cycle 2 completes wake→browse→prove→lean and is cut
off — c2 LEAN started 22:17/22:18/22:37 on the last three days against a c1 wake at ~00:08,
about 1h50, which LEAN consumes alone. I armed `PEER_REVIEW.md` at a c2 wake four times, filing
it to a slot that does not open. Rick waited from 10-01 with nothing wrong in the brief.

## 4. Two smaller things

**The gap in my own index was on my core axis.** A title search for `factorial` across 743
entries returns **four**, and these two were not among them: `1108.3087` Bump–McNamara–Nakasuji
*Factorial Schur functions and the **Yang-Baxter equation***, and `0910.5288` McNamara
*Factorial Schur functions via the **six vertex model***. That is the Zinn-Justin/Wheeler thesis
— the transfer matrix literally computes the coefficient — carried onto Molev's family. Two seed
paths meeting; I owned both halves and not the join. Also absent: `1008.4979` Knutson–Purbhoo
(BK-puzzles, two seed authors), `math/0703462` Richmond (who **coins** "Horn recursion", and
whose title already hedges it — *A **partial** Horn recursion*), and **`math/0607669`
Purbhoo–Sottile itself** — I reasoned about "the Purbhoo–Sottile Horn recursion" for two
sessions with neither paper in my index.

**An instrument finding that upgrades a repair I thought I had made.** On 10-04 c2 I concluded
the fix was "compute citer-set intersections." Today that fix found the right nulls and could
not see the most relevant paper: **Kiers `2106.08425`** (the only genuinely inductive
equivariant object, 1 citation) **cites none of my four seeds**, and surfaced only on a second
hop off a hub. An intersection measures who **cites both**, not who **bridges both** — it finds
confluence and is blind to **replacement**, which is the normal case for a paper that closes a
gap. And my other instrument, keyword grep, is blind to **renaming**. The two blind spots are
**correlated, not complementary**: both key on what a paper says about its ancestry. Repair:
always take a second hop off the hubs.

---

**Owed, and it is the debt this whole cycle is about:** I have not amended
`proofs/2026-10-05-c3-migration-length-grading.tex`. PROVE's (G2)=(C2) correction went into the
*new* paper and the registry; the *old* artifact a future session will read and believe is
unchanged.

Full detail: `memory/dream-journal/2026-10-06.md`, `memory/questions/2026-10-06-dream-ledger.md`,
and five new files in `memory/connections/`. Local volume only — tell me if you want any of it
pushed to `clio-vega/proofs` where you can actually read it.
