# The two log-concavity banks meet at one paper, and I merged them by mistake

**Date:** 2026-09-18 (DREAM c2, from BROWSE c2 + Trails B and C)
**Status:** structural finding, bibliographic evidence verified at source; the mathematical
consequence (Q173) is **open**, not settled.
**Seed path:** Puzzle (hives/honeycombs) × the seed's central question — *why so many models?*

## The claim

Discrete log-concavity of Littlewood–Richardson / Schur data is being proved right now by
**two near-disjoint communities**, and they are the two halves of **Murota's dual pair**:

| bank | machinery | anchor | size (S2 citers) |
|---|---|---|---|
| **M-convex / polymatroid** | Lorentzian polynomials | Brändén–Huh `1902.03719` | 238 (paginated to `next:null`; a floor) |
| **L-convex** | Murota L-convexity, hives/skeps | Knutson–Tao `math/9807160` + KTW-II `math/0107011` | 640 unique |

**Exactly 2 papers cite both** — Pak's survey `2209.06142` and Gui–Xiong `2205.05420`.
Reference lists pulled and checked: Speyer `2601.05007` cites KT and **HMMS `1906.09633`**
but *not* Brändén–Huh; Le–Nguyen `2608.13544` cites KT but neither BH nor HMMS.

So **HMMS `1906.09633` (Huh–Matherne–Mészáros–St. Dizier, normalized Schur is Lorentzian) is
an articulation point** of the union graph: remove it and the hive bank and the Lorentzian
bank fall apart. It is the highest-value unread item I hold.

## Why this is mine and not trivia

My seed asks *why LR coefficients admit so many independent combinatorial interpretations*.
Today that question acquired a **measurable, graph-theoretic form**. The multiplicity of
models is partly sociological, and the sociology is a cut vertex — a far better answer than
"lots of bijections exist."

The same census says the integrable bank is **absent from the Lorentzian side entirely**:
of 238 BH citers, `hall-littlewood 0, lattice model 0, vertex model 0, yang-baxter 0,
puzzle 0, hive 0, honeycomb 0`. That is `one-bibliography-is-not-a-field` in positive form —
the connection gets made by a third party reading both banks. I read both banks.

Two integrable edges *do* exist into the honeycomb citer set and both are new to me:
hives as a random surface (Narayanan–Sheffield–Tao `2306.11514`; Gangopadhyay–Narayanan
`2410.12619` gives hives a surface tension) and vertex models (T. C. Miller `2503.09240`
explicitly extends **Zinn-Justin's** technique; Gaetz–Gao `2408.07863` via
Aggarwal–Borodin–Wheeler interlacing arrays).

## The mathematical cost — my July attribution is on the wrong half

`for-robin/2026-07-25-wake-log-concavity-and-chou-hamaker-honesty.md` says:

> **Speyer 2601.05007** (Lorentzian polynomials → strong log-concavity) covers chain regime
> + (3,3,∗,0) type-invariant family (46/46).

**Speyer's route is not Lorentzian. It is L-convexity.** Lorentzian = the M-convex half.
L and M are Legendre-dual, not the same theory. Whether Speyer covers my chain regime and
the (3,3,∗,0) family is therefore **open again** — that is **Q173**, and it went to Robin
as settled (three for-robin notes, since 2026-07-25).

The antidote was on my own disk: my 09-16 index entry says *"New 2026 LR model via Murota's
**L-convexity**"* — mechanism right, title wrong — while the July note had the title's gist
right and mechanism wrong. Two halves of one correct statement, eight weeks, never in the
same room. → `dictionary-before-identification`: I matched on the shape "discrete convexity
proves log-concavity" and never asked *which* convexity.

## What the literature actually says (verified, with locators)

- **Okounkov's 2003 conjecture** — `(λ,μ,ν) ↦ log c^ν_{λμ}` concave — **is FALSE**:
  Chindris–Derksen–Weyman, *Compositio* 143 (2007) 1545–1557, family
  `λ(n)=(4ⁿ,3^{2n},2ⁿ)`, `μ=ν=(3ⁿ,2ⁿ,1ⁿ)`, fails for `n ≥ 21`. Asymptotically true
  (Okounkov). *(Source: St. Dizier ICERM slides, 24 Feb 2021, read via `pdftotext`.)*
- **HMMS `1906.09633`:** normalized Schur `N(s_λ)` is Lorentzian ⟹
  `K²_{λα} ≥ K_{λ,α+e_i−e_j}·K_{λ,α−e_i+e_j}` — **log-concavity of Kostka numbers**.
- **HMMS, LR case:** holds when `ν/μ` has **at most one box per column** — which is exactly
  where `c^ν_{λμ} = K_{λ,(ν−μ)}`. Suspect this as a **pin in someone else's hypothesis**
  collapsing LR to Kostka. → `a-fixed-parameter-can-be-the-whole-obstruction`.
- **Le–Nguyen `2608.13544`** (2026-08-13, *Skew Hives, Skew Skeps, Skew Schur
  Log-Concavity*): a **skep** = a KT hive transported through the octahedron recurrence so
  its boundary word **interleaves** λ and μ instead of concatenating — and the interleaving
  is what makes the fibres **L-convex**. Thm 1.2 generalises LPP and LPP07 Thms 5, 12,
  Cor 14. Log-concavity is **discrete, on the weight lattice ℤ^{2n}**, not in a degree and
  not in `q`. Plus a **k-phased family**, `1 ≤ |k| ≤ n`, interpolating skew hive (k=n) to
  skew skep (k=1), with **octahedron recurrence ↔ Bender–Knuth involutions** under an
  explicit GT bijection to Nguyen–Nguyen–Woodruff peelable tableaux.

## The ten-minute test on my desk

`2608.13544` Example 1.3 answers Speyer's Question 2.17 **negatively**:
`ν=(9,5,3), π=(6,5,4,2), x=(6,4,3), y=(5,3,1)` gives
`f(x)f(y) = 6 > 5 = f(⌈(x+y)/2⌉)·f(⌊(x+y)/2⌋)`.
Four LR coefficients, stated by someone else, **untuned**, decisive either way — and it
lands on the exact claim I mis-attributed in July. → `detector-that-picks-a-parameter-cannot-confirm`
(this one is not tuned by me), `a-disagreement-is-two-sided` (it is their control, not mine).

## Why this connects to the seed's machinery, not just its questions

My transfer-operator strategy computes LR coefficients **by Kostka matrix inversion** —
the seed's own stated discovery. A log-concavity theorem *about Kostka numbers* therefore
sits on the object my machinery manipulates, not the object I nominally study.

→ **Q177** is the edge I am positioned to build: normalized Schur is Lorentzian; Schur is a
lattice-model partition function; **is the normalized partition function of a free-fermion
six-vertex model Lorentzian?** Zero of 238 BH citers has asked.

## Links
`an-index-cannot-measure-its-own-recall` · `one-bibliography-is-not-a-field` ·
`dictionary-before-identification` · `a-fixed-parameter-can-be-the-whole-obstruction` ·
`witnesses-must-be-checked-for-distinctness`

## Source status (checked 2026-09-18 DREAM c2)

Every arXiv ID above is in `reading/sources.json` **except the two overlap papers
themselves** — Pak `2209.06142` and Gui–Xiong `2205.05420` are **not indexed and not
opened**; they are known to me only as the intersection of two citer sets returned by the
Semantic Scholar API. The "exactly 2" count therefore rests on an **API census, not on
reading either paper** — an `agent-summary`-grade fact by the standard of
`reading/sources.json`. Open them before the count becomes load-bearing.
The 238 and 640 figures are **floors**: S2 splits arXiv and journal records.
