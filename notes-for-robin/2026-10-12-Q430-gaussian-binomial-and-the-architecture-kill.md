# Q430 — the Gaussian binomial fails, and no multiplicity-determined weight can work

**For:** Robin · **cc:** Rick · **Date:** 2026-10-12 (PROVE c1)
**Paper:** https://github.com/clio-claude/proofs/blob/main/2026-10-12-Q430-gaussian-binomial-single-box.tex
**PDF:** https://github.com/clio-claude/proofs/blob/main/2026-10-12-Q430-gaussian-binomial-single-box.pdf
**Registry:** https://github.com/clio-claude/proofs/blob/main/registry/cylindric-statistic.json (46 → 55 nodes)

## The short version

Q430 asked a yes/no question about one candidate weight. The answer is **no**, and the
reason generalises twice, so I am handing you three results instead of one.

**Lemma A (forced first step).** On the fibre `α = (1^n)`, every cylindric tableau has
`θ^(1) = e_1` and its first step reads `m_h(0) = w`. Region arithmetic, two lines, and it
does not mention the HKKO sign rule. Everything below is this lemma.

**Theorem B (first-step divisibility) — new, and it applies to the whole multiplicative
class.** Because every tableau passes through that one edge, `ω(0,e_1)` is a *common
factor* of every `W_T`, so the identity forces

    ω(0, e_1)  |  c_α(t)   in Q[t].

Corollaries that cost nothing: `deg ω(0,e_1) ≤ deg c_α`, and (Gauss) `ω(0,e_1)|_{t=1}`
divides `c_α(1)` in **Z**. The Gaussian binomial has `ω(0,e_1) = [w+1]_t`, degree `w = 4`,
against `deg(3 − t²) = 2`; and `5 ∤ 2`. **Dead by comparing two integers** — a capacity
refutation in the Q405 sense, no model built, no tableau enumerated. Family test: 24
fibres, 9 vacuous (`c_α = 0`, all with `n` odd), and **all 15 non-vacuous ones refuted**,
10 inside Korff's domain.

Theorem B also **re-derives your 2011 kill by a different invariant** (degree `w`, where
Q417 used `ord_{t=1} = 4`) and is **blind to the 2019 ribbon** (`ω(0,e_1) = 1` divides
everything). So the three obstructions are genuinely independent and this is a new third.

**Theorem D — the actual result, and it kills an architecture.** Call a weight
*multiplicity-determined* if its single-box value is `f(m_{i−1}(x))`, independent of `i`.
**All three candidates ever proposed in this program are of that form**: Korff 2011 `Ψ`
(`f = 1 − t^m`), Korff 2019 ribbon (`f ≡ 1`), Q430 Gaussian binomial (`f = [m+1]_t`).

Take `ℓ = 0` (so `w = 2`), `α = (1,1)`, any `k ≥ 1`. The fibre has **exactly two**
cylindric tableaux:

| `T` | endpoint | `c⁻` | m-INDEX seq | m-VALUE seq |
|---|---|---|---|---|
| `T₁` | `(1,1,0,…,0)` | `+1` | `(h, 1)` | `(2, 1)` |
| `T₂` | `(2,0,…,0)` | `−1` | `(h, h)` | `(2, 1)` |

Same multiplicity sequence, opposite signs. **They differ only in which cyclic slot the
multiplicity sat in.** So for *every* multiplicity-determined weight,
`Σ_T c⁻(T) W_T = f(2)f(1) − f(2)f(1) = 0` identically, while `c_{(1,1)}(t) = 1 − t ≠ 0`.
Three candidates die at once, on a **two-tableau** fibre, one evaluation each — strictly
cheaper than either earlier kill (10 tableaux; a five-point sweep). Inside your domain for
`k ≥ 2`.

**The satisfiability control fires**, and it is the control that matters: the index-aware
weight `g(h,2) = g(1,1) = 1`, `g(h,1) = t` returns `1 − t` **exactly**. So the fibre is
satisfiable by a weight differing from a multiplicity-determined one *only* in reading the
index. The theorem tests the architecture and not the fibre — and it **names its own
repair**.

**Specification 5 (supersedes Specification 3).** A working single-box weight must (i)
depend on the cyclic index `i`, not only on `m_{i−1}(x)`; and (ii) have `ω(0,e_1)` dividing
`c_{(1^n)}(t)`. Clause (ii) survives the widening because Lemma A never used
multiplicity-determinedness. **This is Q433.** I am not calling any weight that passes it
alive — per the Q418 post-mortem the honest phrase is *"passes; unscreened."*

## Controls, as numbers

1. `ω ≡ 1` at (2,1,4) → **2** ✓ (engine right)
2. `ω = 1 − t^m` → **`(t−1)⁴(t+1)(t²+1)(t²+t+2)`** exact, `ord_{t=1} = 4` ✓
3. constant fibre (2,2,4): `c_α = 3`, `deg 0`; `ω ≡ 1` → **3** ✓; candidate → **476** ✗
4. generic index-aware symbols: **4** terms, **8** free symbols; specialising to `f(m)`
   returns Theorem C's `f₁²f₄(f₁+f₃)` ✓
5. three adversarial `f` at the `ℓ=0` fibre: all **0**, as Theorem D requires ✓

**Control 3 did not do what the brief predicted, and that is the informative part.** The
brief said a constant-`c_α` fibre "must be satisfied by *both* `ω≡1` and the candidate."
It is not — `ω≡1` returns 3 exactly (so the engine is right), the candidate returns 476. So
the brief's inference ("a test failing there is testing the fibre") does not apply. What
the control actually reports is better: the candidate fails **even where the t-freeness
obstruction is absent**, so its failure is about normalisation at `t=1`, which is exactly
Theorem B. Third session running where the arm I expected to be redundant was the
informative one.

## Two things I need to tell you against myself

**1. The Q424 paper shipped a claim with no computation behind it.** Line 551 listed, under
*"Rests on computation"*, the irreducibility of `q⁴ − 2q² − q + 3 − t²` over `Q(t)`.
`taskC3.py` had **crashed partway through section 4** (`sp.factor(…, extension=False)`, an
invalid SymPy option). `C3.out` was 30 lines, **ended at a plausible place**, and lacked
section 5; a **1,437-byte `C3.err`** holding the traceback sat unread beside it. Re-run
today: `C3b.err` **0 bytes**, `C3b.out` **44 lines**, section 5 present. The claim holds
(irreducible over `Q` in `(q,t)`, and primitive in `Z[t][q]` since `gcd(−1,2,1,t²−3) = 1`,
so Gauss upgrades it to `Q(t)[q]`). **It was unbacked when the PDF was stamped.** The kill
at line 435 never needed it anyway.

The lesson is sharper than "a script written and a script run look identical": the script
**ran and died partway**, and the surviving `.out` ended somewhere plausible and read as
complete. **A non-empty `.err` beside a plausible `.out` is the tell, and the `.err` was on
disk the whole time.** Every script I wrote today prints a sentinel on its last line, and I
`wc -c`'d every `.err` before reading its `.out`.

**2. The holdings row in my own brief recorded a document as absent that was on disk.** My
brief's §0 — a table written this morning *expressly* as a corrective, headed *"Read this
table before recording any absence"* — said HKKO `2301.13117` was **"NOT ON DISK IN ANY
FORM."** It is at `/home/clio/data/fetched/arxiv-2301.13117.pdf`, 662,217 B, `%PDF-`, with
a 32,147-word text layer, **fetched at 02:33 today, 2.5 hours before my slot**.

Worse: **BROWSE fetched it on purpose to pay that exact debt and said so in writing** —
keyword 1 justified as *"Pay the HKKO 2301.13117 reading debt"*, fetch table annotated
*"genuine debt, now closed"* — and that BROWSE is the **top banner of `SUMMARY.md`**, whose
headline lesson is *measure the path the entry's own `local` field records*.

So the morning ran: **BROWSE closes the debt and writes the lesson → WAKE records the
document as absent in the table built to prevent that → PROVE copies the absence into a
paper and builds a gap section on it.** My standing note says *a correct record prevents
nothing until a brief quotes it.* This is the inverse and sharper: **the brief did quote a
record, and quoted the wrong one.** A brief inherits the authority of whichever session
wrote it last, not whichever measured best.

The rule I am taking from it is about the *index entry*, not any session's prose:
**`sources.json`'s `local` field is the first thing to measure, not the last.** The audit
asked the entry for its extraction level (`deep-read`) and mention count (11) and weighed
those against a filesystem sweep, while the one field that is the document's *address* went
unread. I found it only because `trustcheck sources` made me print the entry.

**Upside:** the gap is closed, not just explained. HKKO Thm 3.3 eq. (3.4) is now quoted
verbatim in §7 of the paper, and `sign_hkko` is verified against it by an **independent
re-implementation in HKKO's own 1-indexed notation** (deliberately not reusing my 0-indexed
code, to avoid inheriting an off-by-one): **2,291 cases, 403 returning a nonzero sign,
0 mismatches**, and two negative controls fire (67 and 286 disagreements). The §0 caveat
*"audited only by Control 2"* is withdrawn. Dictionary confirmed: HKKO's `h` = my `k`,
HKKO's `2h` = my `h = 2k`.

## Gaps I am not papering over

1. **Q434 (conjecture, unproved):** `deg_t c_{(1^n)}(t) < w` on every non-vacuous fibre.
   This would upgrade Theorem B's kill from "15 of 15 tested" to "every fibre". I report
   the cardinality, not the generalisation.
2. **Theorem D is scoped to the multiplicity-determined sub-class.** Specification 3's
   general multiplicative class is **not** refuted — the satisfiability control exhibits a
   member that works. What is refuted is the only sub-class anybody has tried.
3. **`c_{(1,1)} = 1 − t` is computed for `k = 1..5`, not proved for all `k`.** The
   tableau-side `Σ ≡ 0` *is* proved for all `k ≥ 1` (checked symbolically to `k = 7`); it
   is the contradiction that needs `c_{(1,1)} ≠ 0`.
4. **Nothing here constructs a working weight.** Every result is a negative or a necessary
   condition. Specification 5 is a constraint, not a candidate.

## Validation

`trustcheck validate` on the registry: **0 problems, exit 0**. Not taken on trust — a
planted bogus file path on today's headline node fires (**1 problem, exit 1**) and a bogus
trust enum fires (**2 problems, exit 1**), both re-run against the *final* file. Separately:
the brief told me to look for a `; N file(s) resolve cleanly` suffix on `validate` and to
treat its absence as proof the checker opened nothing. **That suffix belongs to the
`sources` subcommand, not `validate`** (trustcheck.py:1969 vs :698) — so its absence there
means nothing, and I verified `validate` by planting instead. `sources` run properly reads
`sources index OK (858 sources); 2 file(s) resolve cleanly`.

Allocated: **Q433**, **Q434** (433 → 435, read-and-bump in one action).
