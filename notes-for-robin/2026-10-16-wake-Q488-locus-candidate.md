# WAKE 2026-10-16 — a candidate LOCUS for Q492, read off Motegi 2026's own K-matrix

**Status:** hypothesis, **no computation behind it**. Written at wake from a first-hand read of
`/home/clio/projects/library/sources/2026-10-15-browse-arxiv/sub1-ep-2610.15344.tar.gz`
(`typebcweightfunctions_arxivversionfinal-3.tex`, 216,486 B, 6430 lines — the paper PROVE c2
worked from, now read for its boundary data rather than its weight functions).

## 1. Term census of Motegi 2026 (first-hand, `grep -ci` on the .tex)

| term | count |
|---|---|
| `Pfaffian` / `pfaffian` | **0** / **0** |
| `determinant` | **0** |
| `Izergin` / `Korepin` | 2 / 2 (**both in the bibliography only** — lines 6203, 6322) |
| `triangular` | **15** (the 10-15 c2 dream said 17; my count on the .tex is 15 — correct the dream) |
| `off-diagonal` | 2 (lines 343, 4807) |
| `K-matrix` (hyphenated) | 0 — he writes `$K$-matrix`, so the hyphenated grep is a **false zero** |
| `Kuperberg`, `free-fermion` | 0, 0 |
| `Laurent` | 22 |

⇒ **The 2026 paper is silent on BOTH halves of the determinant/Pfaffian dichotomy.** It is not
that he chose the determinant; he never evaluates the partition function in closed form at all.
So Q488 is a genuine open computation, **not** a reproduction — which is the stronger position
the dream asked for.

## 2. ⚠ TWO-COORDINATE CHECK: his "Laurent polynomiality" is NOT my Laurent criterion

His 22 `Laurent` hits are about **specializations of the weight functions / branching
coefficients** `F_M` (claim at line 153; proof §`Laurent polynomiality`, line 3276, by
**equivariant geometric localization** with `λ_y`-classes). Q484 measured Laurent-ness of the
**structure constants** `c^ν_{λμ}` in that basis. **Same noun, different object.**

⇒ His theorem does **not** imply mine, and my measured **failure** at jump ≥ 2 does **not**
contradict his theorem. I could have read the collision either way and been wrong twice. Logged
because this is the `[[the-missing-coordinate-is-one-rule-in-nine-drawers]]` shape again, caught
*before* it cost anything, on a noun I already had on both sides.

## 3. The K-matrix is explicit, and it is triangular-with-a-live-off-diagonal

`eq:Ktri-components`, line 333:

    [K(u)]_0^0 = β − γu⁻¹        [K(u)]_0^1 = 1 − u⁻²
    [K(u)]_1^0 = 0               [K(u)]_1^1 = βu⁻² − γu⁻¹

Two specializations `K^C`, `K^B` follow (lines ~348, ~1346 defines type-B M-smallness) — so the
**type-B arm of Q484** (open thread 3) has its definitions in this same file.

This sits **strictly between** diagonal and generic: upper-triangular, `(1,0) = 0`, but the
`(0,1)` entry `1 − u⁻²` is **not identically zero**. Under Q492's dichotomy that puts the object
on the **off-diagonal ⇒ Pfaffian** side — i.e. **Q492 predicts a Pfaffian for a paper whose own
text says `Pfaffian` zero times.** A prediction about a silence is falsifiable, and nobody has
spent the knowledge; cf.
`[[2026-10-15-c2-dream-an-author-who-publishes-both-halves-and-cites-one]]`.

## 4. ★ THE CANDIDATE LOCUS — and it has the right *shape*

The off-diagonal entry `1 − u⁻²` **vanishes exactly at `u² = 1`**. And Motegi uses precisely
that, twice, as his own technical engine:

- line **1750**: *"the `$K$-matrix` reduces essentially to the identity matrix `K(1) = (β−γ)Id`"*
  — and with the ice rule the configuration is then **uniquely determined row by row**.
- line **2094**: *"Upon setting `u_{r+1} = … = u_n = 1`, the configuration in the top `(n−r)`
  rows is uniquely determined by the condition `[K(1)]_0^1 = 0`."*

So **"diagonal boundary" is not a separate model — it is the specialization `u_j → 1`**, and the
**number of spectral parameters he sets to 1 is `n − r`, a CARDINALITY DIFFERENCE of the indexing
subsets.**

> **HYPOTHESIS (Q492's missing locus).** The determinant/diagonal regime is cut out by
> `u_j = ±1` on the rows the jump forces, and the jump statistic `|ν| − max(|λ|,|μ|)` **is** (or
> controls) the count `n − r` of parameters that must be specialized to 1. Jump ≤ 1 ⇒ at most one
> row escapes the diagonal specialization ⇒ determinant ⇒ a puzzle can exist. Jump ≥ 2 ⇒ two or
> more live off-diagonal rows ⇒ Pfaffian ⇒ no puzzle.

That would upgrade Q492 from *"two binary splits agree on being binary"* (**one coordinate**) to
*"two splits with the same locus"* — because `u² = 1` is a **named subvariety** and `n − r` is a
**named integer**, so the comparison can come out false.

## 5. Pre-registered failure modes — stated now, before any computation

1. **`n − r` need not be `|ν| − max(|λ|,|μ|)`.** It is a cardinality gap between indexing
   subsets; the jump is a gap between partition sizes. **These are two different integers until
   the dictionary is written out.** If they disagree, §4 is a coincidence of shapes and Q492 goes
   back to one coordinate. ***This is the check, and it is cheap — do it FIRST, by hand, at
   `N = 2`, before any Korepin machinery.***
2. `1 − u⁻²` vanishes at `u = −1` as well as `u = 1`. Motegi only ever uses `u = 1`. **Name the
   component I am skipping** — this is exactly the `q³+1 = (q+1)(q²−q+1)` fault Rick caught on
   10-15 (`[[a-control-names-a-locus-but-implements-one-factor]]`). At `u = −1` the diagonal
   entries become `β+γ` and `β+γ`, i.e. `K(−1) = (β+γ)Id` — **also** scalar. So the honest locus
   is `u² = 1`, **both** points, and I should check whether the `u = −1` branch is trivial
   (as the `q = −1` collapse was) before claiming the locus is one point.
3. **Everything on the Pfaffian side is still unread.** `1806.00933` is at `extraction:
   abstract`, `2309.08446` (the load-bearing *"Pfaffians general, determinants degenerate"*) at
   `agent-summary`, `2603.20865` at `title-only`, `math/0008184` (Kuperberg OSASM, origin of the
   OS boundary) at `title-only`. **None of the three is on disk** — a `find` for all four IDs
   returned only the 2610.15344 tarball. §3 and §4 above rest on **my own first-hand read of the
   2026 source only**, which is the one input that is read.
4. The `(0,1)` entry being nonzero makes the boundary off-*diagonal* but **upper-triangular**, and
   Motegi 2018's Pfaffian paper (per its abstract) used an **OS triangular** boundary. Whether
   *triangular* suffices for a Pfaffian or whether a genuinely **non-triangular** `(1,0) ≠ 0`
   entry is required is **unverified**, and it is the difference between Q492 applying to this
   object and not applying at all. ⚠ This one can make the whole §4 vacuous.

## Links

`[[2026-10-15-c2-dream-the-pfaffian-is-the-jump-stratification]]` (Q492) ·
`[[2026-10-15-dream-a-published-open-problem-hit-my-own-boundary]]` ·
`topics/general-c-boundary.md` · `topics/pfaffians-and-minor-summation.md`

---

## Addendum (same session) — the noun is ALREADY shared, which makes failure mode 1 sharper, not weaker

Grepping my own Q484 writeup (`proofs/2026-10-15-Q484-motegi-puzzle-Gm.tex`, 30,969 B):

- L63 calls my statistic a **"cardinality jump"** in so many words: *"it bites only at cardinality
  jump ≥ 2"*.
- L489 records the diagonal stratum as **`s = r`, hence `n = r`** — i.e. `n − r = 0` exactly on
  the diagonal, which is also where Motegi's `K` goes scalar.
- L431–432: the smallest witness is `λ = μ = ∅`, `ν = (1,2)`, **jump 2**, and it is the *only*
  failure at `N = 2`.

So `n − r` and `|ν| − max(|λ|,|μ|)` **already share the word "cardinality"**, and they **agree at
zero**. That is encouraging and it is also precisely the trap: *agreeing at one value plus sharing
a noun is a one-coordinate match* — the same shape as `y`-vs-`κ` (nine days, Q442), `modulus`-vs-
`rank`, and this week's `Laurent`-vs-`Laurent` above in §2.

⇒ **The check is not "do they look the same", it is: write the dictionary `(λ,μ,ν) ↔ (I,M,K)`
explicitly and evaluate BOTH integers on the `ν = (1,2)`, `λ = μ = ∅` witness at `N = 2`.** If
`n − r ≠ 2` there, §4 is dead in one line and three hours are saved. Do this before Korepin.
