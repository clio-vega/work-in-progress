# For Robin — 2026-06-29: a vertex-model home for the order law, and the literature finally meeting my proofs

Two browse cycles consolidated tonight (06-27, 06-28). No route to bury this time — both fed the surviving
program. Three things worth your attention.

## 1. GWZJ 2504.19205 is the vertex-model home of both my open programs

**Gunna–Wheeler–Zinn-Justin, "Structure constants for spin Hall–Littlewood functions"** (Apr 2025) computes
sHL LR-type structure constants as integrable-lattice partition functions, in closed form over *generalised
honeycombs*. It cites both the 2008 seed and Naprienko's free-fermionic Schur — a confluence of my two
threads. The spark: my order law `ord_{x=q²}Z_λ = τ(τ+1)/2` should be the **codimension of the honeycomb-
collapse locus at x=q²** (the number of frozen honeycomb edges). I have NOT scaffolded this — per the
discipline we've been burned on, the next action is a cheap probe: count frozen edges at x=q² for the hook
ladder (τ=1,2,3) and check against 1, 3, 6. I'll run that before reading the paper in full.

## 2. The literature finally touched the actual proof front (this is new)

For three weeks the real work has been 2-adic valuations of products/quotients of binomial coefficients
(the boundary lemma, NL_c, Compensation Lemma B — all now machine-checked or close). Two papers landed on
exactly that, for the first time:

- **Gatzweiler–Krattenthaler 2502.06032** — cyclotomic positivity of a *q-binomial quotient*. This is the
  q-lift of my `v₂(∏ C)` inequalities. If it specialises to the boundary/NL_c walls, the factor-in-product
  engine (Lemma F2) has a published q-analogue.
- **Ayyer–Kumari 2501.00275** — I need to correct my own record: my "Ayyer–Kumari DEAD" tag was scoped only
  to one lever (Φ not splitting linearly on ties). Their *factorization* theory is very much alive for d=4.
  "Odd power of an even root of unity" is exactly my `d≡2 mod4` vs `d=4` boundary, and their **{0,±1,±2}
  universal-character value bound** is a candidate single structural cause for "|J*| even" — which I've so
  far proved family-by-family (hook, two-row, three-row c=1/2/3). Worth a t=4 re-read.

Both are medium-cost probes I'll queue. They matter because the browse usually feeds the spectral wishlist;
this time it met the place where I'm actually proving theorems.

## 3. Pfannerer 2603.16598 is read — the super-maj question is now make-or-break

The standing block since 06-15. Super descent = (classical descent AND `i+1∉D`) OR (not-descent AND `i∈D`);
engine `f^λ(q,t)=f^λ(q)∏(1+t q^{c(□)})`. The decisive check: **is Pfannerer's supermaj weight equal to my
`s(T)=Σ_{i∈Des}w_i`?** If yes, that's a 4th independent literature home for the graded order law (and the
`{d_j}={s(T)}` multiset leg, which none of the five falsified probes ever touched). If no, super-maj is
finally pruned. I'll run the comparison on (3,1),(2,1,1) next.

## Standing item I keep deferring (calling myself out)

**MO#509068** — a one-line exterior-power answer (`χ^{(n−j,1^j)}=Λ^j V`) that's been in hand and greenlit
three dreams running. It's the lowest-effort public artifact on my board. I'll post it.

— Clio
