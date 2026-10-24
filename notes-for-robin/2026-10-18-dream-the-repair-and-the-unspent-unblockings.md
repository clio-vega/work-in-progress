# For Robin — DREAM 2026-10-18

Four sessions consolidated (WAKE 01:14, BROWSE 03:42, PROVE 06:29, LEAN 08:53). Three things you
may actually care about, then two operational items.

## 1. The mathematics landed, and the shape of it is simple

**Arity preservation is the discriminator.** A collision's effect on the type-C structure constants
is governed by what the reflection does to the *cardinality* of the label set — not by the root's
length, not by the type.

- `e_i − e_j` sends `M ↦ M △ {i,j}`: `|M|` **preserved**, so the collision merely permutes the
  argument multiset `w_M`, and `u`-symmetry of the `S_n` symmetrisation gives `ρ^A = 1` in one line,
  every `N`, both types B and C.
- `e_a + e_b` drops `|M|` by 2 and `h·e_m` by 1: symmetry says nothing, and that is where
  `ρ ≠ 1` and the poles live.

Theorem: `L_ij = G_ij` — the span of Motegi's basis **is** the A-type GKM lattice, colength
`2^(N−2)` computed over two genuinely different index sets. So the A-type direction imposes **no
condition** on `χ`, and `(COB)` + `(SR)` are the complete list across all three root families.
Paper `proofs/2026-10-18-atype-divisors-and-the-gkm-lattice.tex` (13 pp, `bd831d3`).

The pretty part: **the same fact that gave the theorem for free is what made yesterday's planned
measurement carry zero bits.** A point-indexed product `∏_{m∈M} f(w_m)` cannot see a permutation of
its index set — which is simultaneously why `ρ^A = 1` is free and why "`Ψ` is transposition-invariant
on `{w_i = w_j}`" is true of *every* candidate and therefore distinguishes nothing. The vacuity and
the theorem are one structural fact; which side you stand on decides which you get.

## 2. Koncki's table is real, first-hand, and the 15/16 figure is in print

The `LG(2,4)` table Rick and I had both been treating as a rumour is **Chapter 6 §6.2.1, pp. 70–71**
of Koncki's 2022 Warsaw PhD thesis — no arXiv ID, no DOI,
`https://www.mimuw.edu.pl/~jkoncki/pliki/dok.pdf` (md5 `ff6b82cce7d115df9fc724929b6289f0`, saved
locally with full text and a provenance file). Bare `curl` gives **403**; any browser user-agent
gives **200**.

And the "fifteen of the sixteen entries" figure is **Motegi's own published sentence** —
`arXiv:2610.15344`, §Discussion — along with a promise of the sequel that would do what my Q509/Q510
ask.

Two useful structural facts from the table: the twist is a **two-chamber wall-crossing**
(`α = 2⌈λ⌉ − ⌈2λ⌉ ∈ {0,1}`, so `λ` is not a coordinate I can differentiate along), and the **only
two entries carrying the case split sit at `e13`** — the point Koncki blows up. So the disagreeing
sixteenth entry is pre-registered as one of those two, and the comparison is now a finite check
against a document I hold rather than a comparison against a rumour.

## 3. My own correction, since you'd want it stated plainly

**My flagship paper's title was wrong and my own theorem is the proof.** `e_a + e_b` is *long* in
type B and *short* in type C; `h·e_m` is the reverse. The paper is about type C, so "long-root
divisor" / "short-root divisor" were inverted — 35 places including the title, in the PDF I emailed
Rick at 00:24 on 10-18. Fixed (`7002d00`), with a remark recording it as a **quantifier error** —
the long/short attribution is a function of `h`, and `h` is exactly what the theorem quantifies over
— rather than burying it. **No theorem moved**: I grepped for any step reasoning *from* root length
and there are none. New names are type-independent: **pair** divisor and **boundary** divisor.

## Operational — two items

**(a) The browse arXiv lane silently dropped four papers, and I have filed the remains.** The
coordinator returned no synthesis; three sub-agent files were written to `/tmp/browse/` and the
session closed. It recorded this honestly, named the paths — and `/tmp` is volatile. They were still
there tonight (75 KB); I copied them to
`memory/reading/2026-10-18-browse-arxiv-lane-UNREAD/` with md5s verified three-for-three and a
README whose first line says *FILED, NOT READ*. **Nothing in `memory/` rests on them.** If the
sub-agent fan-out can be made to write into `memory/` directly rather than `/tmp`, that failure mode
disappears; this is the second time in two days that the lane with the least durable output had the
day's best content.

**(b) `tracecheck`'s `init()` fragments a session while `report` reads one file.** Already flagged by
the prove session — it split one session into four fragments, and 2 of 3 real violations sat in a
fragment no report had covered. I did not patch shared tooling. Same session: `trustcheck
--sources /nonexistent.json` returns **`sources index OK (0 sources)`, exit 0** — the documented
vacuity hole is live in this build, confirmed rather than assumed.

## Registry

**No grade changed tonight.** Consolidation found no claim it needed to demote or promote, and I am
saying so explicitly because a silent dream is indistinguishable from an unexamined one. The
`coboundary-and-removable-poles` **parent remains at `proved`** despite four new `lean-verified`
children — `ρ`'s numerator `(1−q)²` comes from the bulk factor and contains no `K`-matrix, so
promoting the parent would convert a named gap into a certificate.

## What I'd do next, if you're choosing

Q510's `e13` test. I hold the document, the labels are finite, the two candidates are
pre-registered, and it is the one open task whose answer changes what I *say* rather than what I
believe about my instruments. Settle Q512 first in the same session — Motegi distinguishes the
geometric class from the *normalised* weight function one sentence earlier, so there are **three**
candidate objects in that comparison, not two.
