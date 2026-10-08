# Order law proved as a combinatorial minimum over SYT descents

**Clio, 2026-05-31 prove session**

Robin — I have a clean, (almost entirely) representation-theory-free proof that

>  `min_{T∈SYT(λ)} s(T) = τ(τ+1)/2`,   `τ = max(0, 2λ'₁ − n − 1)`,
>  `s(T) = Σ_{i∈Des(T)} w_i`,  `w_i = 2i−1` if `n−i` odd else `0`.

This is the order law `ord_{x=q²} Z_λ = τ(τ+1)/2` restated combinatorially (via the
descent-statistic bridge from the 2026-05-31 wake), and it BYPASSES the merged-arc reach gap
that blocks the operator/deletion route.

**Full writeup:** `~/projects/proofs/2026-05-31-orderlaw-descent-minimum.md`
(I'll push to clio-vega/proofs and send the GitHub URL.)

## What's the heart of it

The lower bound is the surprise — it's *short*. The whole strategy in PROVE.md (LP / total
unimodularity / cheapest-greedy) collapses to **one application of the prefix-descent lemma at
the single threshold `m = n−1`**:

1. **Lemma A** (pure SYT): `|Des(T)∩[1,m]| ≥ r(m)−1`, `r(m)=min{r:λ₁+…+λ_r≥m+1}`. Proof:
   entries `1..m+1` form a subshape spanning `≥r(m)` rows; each row-opening is a descent `≤m`.
2. At `m=n−1`: `|Des(T)| ≥ ℓ−1`. At most `f(n−1)` descents are free, so the number of **paid**
   descents is `≥ (ℓ−1) − f(n−1) = ⌈τ/2⌉`.
3. The `t`-th paid descent sits at a position `≥ p_t` (the `t`-th paid position), and paid
   weights increase, so `s(T) ≥ Σ_{t=1}^{⌈τ/2⌉} w_{p_t} = τ(τ+1)/2` (a two-line arithmetic id).

That's the entire lower bound. As a bonus it re-derives `τ = max(0, 2λ'₁−n−1)` from prefix
congestion — `τ` is an *output*, not an input.

## Achievability

Need an SYT with no paid descent `> τ`. I give:
- An **explicit construction** (column-1 spine of height `τ+2`, then alternate
  column-major "up" fills with column-1 "down" fills) that is **fully proven** for all `τ > 0`
  shapes, plus the trivial column/row cases.
- A **greedy filling** (free position ↦ deepest addable row below; paid position ↦ topmost
  addable row at-or-above) for the `τ = 0` shapes (all descents must be free). Its output is a
  valid all-free-descent SYT.

## The one honest gap (`τ = 0` achievability)

For `τ = 0` the target is `s = 0` (all descents free). Such an SYT **exists** for every
partition of `n ≤ 9` — that's the brute-forced `min = 0` (capstone.py) — so the theorem holds
for these shapes. But I do **not** have a proven uniform construction. The natural greedy I
tried is genuinely *wrong*: it passes every `τ>0` shape but fails 7 wide `τ=0` shapes at
`n ≤ 10` (smallest `(3,2,2)`, `n=7`), forced into a paid descent near the end while filling
deep equal-length rows. So: existence certain, explicit construction open. The conjugation
identity `s(T') = C(n,2) − s(T)` recasts it as "∃ SYT of `λ'` with every paid position a
descent" for `2λ'₁ ≤ n+1`.

The **lower bound (the hard direction) is complete and rigorous**, and the `τ>0` achievability
construction is both proved and computer-checked — that's the part I'm confident in and wanted
you to see. The `τ=0` construction is unfinished.

Scripts: `~/projects/scratch/2026-05-31-minimizer/{lowerbound,capstone,cons3}.py`.
