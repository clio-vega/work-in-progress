# For Robin — the general-`c` boundary residual just found its home (and it's on the seed)

*Dream 2026-07-05 (system date 2026-06-18). A status note on where the three-row even-`|J*|` program now
stands after today's CODE jobs + this week's reading.*

## The headline

The one thing blocking the general-`c` three-row boundary close — a **uniform Content Lemma** (a
`c`-uniform lower bound on the 2-adic content of the master deficit `N_i^{(c)}`) — now has **four
independent import routes**, and they all converged in a single week. More striking: two of them are the
*same root-of-unity substrate*, which is what finally reconnects this 2-adic side-quest to the seed.

## What today's compute settled

- **Job A (deep content census):** the exact content `g[c][k]` is genuinely `c`-dependent with **no
  closed form at low modulus** (`c=5` vs `c=9` disagree at `k=3` despite `5≡9 mod 4`). I'd been hunting an
  exact formula for several cycles — Job A *proves* it doesn't exist. The good news: the certified **floor**
  `v₂(N_i) ≥ 2⌊k/2⌋` (both parity slices), `≥k` (even slice) is all the boundary lemma ever needed, and
  it's verified to 0 violations (`c≤12`, `b≤200`). So the route is "build on the floor", not "find the
  content."
- **Job B (Gatzweiler–Krattenthaler q-lift): POSITIVE.** The `v₂(∏C)` walls (Lemma F2, NL_c, Compensation
  Lemma B) are exactly the `q=−1` cyclotomic shadow of q-binomial multiplicity inequalities. Lemma F2 and
  NL_2 both lift cleanly to a q-positive statement. This is the first time the literature has touched the
  *proof-level* arithmetic rather than the spectral framing.

## Why it matters (the seed connection)

For weeks the even-`|J*|` / order-law work felt like a private 2-adic cul-de-sac. It isn't. The Content
Lemma's natural home is **q-binomial cyclotomic positivity** (the integrable-lattice / Hall–Littlewood
path) and the **fusion quotient** `Λ/I` (the cylindric path — your thesis territory, since fusion
coefficients are LR coefficients at a root of unity). Dobner's two 2026 cylindric papers (`2605.20540`
fusion-quotient positivity; `2603.09119` cylindric RSK) supply the structural route, and the q-binomial
side (Job B) supplies the arithmetic route — and they're two faces of one object read at `q=−1`. The 2-adic
program is the `Φ₂`/root-of-unity specialisation of the integrable q-vertex-model world.

## Also done today

- **Lean: the `c=2` boundary is closed end-to-end, `sorry`-free** (`threerow_c2_boundary`, 3 standard
  axioms). With `c=1` (06-16), **both** complete three-row `d=4` families are now machine-checked,
  interior + boundary. Reusable kernel: the bridge `vz_prod_Icc`.

## The cheap, decisive next probes (for a wake session)

1. **Does `N_i^{(c)}` have a q-analogue that is a G–K quotient?** If yes, its `Φ₂`-multiplicity is the
   exact content, and one q-positivity = the whole uniform Content Lemma. (Needs reading `2502.06032`.)
2. **Prototype the Chand/Rowland automaton** for `Δ(b+i)` on base-2 digits of `(a,b,m)` — tests whether
   the `c`-dependence is just a state-vector artifact (one `c`-independent transition matrix).
3. **MCW vs `s(T)`:** is Dobner's minimum-cylindric-width statistic the cylindric shadow of my descent
   statistic? Cheap, and would give a growth-diagram derivation of `τ(τ+1)/2`.

No action needed from you — this is a "where things stand" note. Email's been down on my side; flag if you
want any of this written up.
