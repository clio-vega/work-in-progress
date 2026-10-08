# For Robin — 2026-10-02 LEAN

**`tail-of-pf2-logconcave` is machine-checked.** New module in
`clio-vega/tworow-d4-kernel`: `TworowD4Kernel/TailSum.lean`. `lake build` exit 0, 3179
jobs, 0 sorries, axioms `[propext, Classical.choice, Quot.sound]`.

This was the last informal step in the `m=2` chain — everything above it was already
`lean-verified`. Registry node promoted `proved` → `lean-verified`.

**The one thing worth your eye.** The paper proof sums a geometric series, which has no
meaning over `ℤ`. Rather than move to `ℝ`, I replaced it with an induction on the upper
limit:

```
(β(y-1) - β y) · Σ_{r=y}^{M} β r  +  β(y-1)·β(M+1)  ≤  β(y-1)·β y      (M ≥ y-1)
```

The extra term is precisely the remainder the paper discards by summing to infinity, and in
the geometric case the statement is an **equality** — so the discrete form is not a
weakening, it is the sharp one, and the analytic proof is the lossy shadow of it. No
division anywhere; the "ratios are nonincreasing" step becomes
`β(y-1)·β(m+1) ≤ β(y)·β(m)`. I think this is the better proof and it would improve the
paper.

**Two things I got wrong and caught.** (1) I started by trying to *drop* interval support,
on the guess that global log-concavity forces it. `(1,0,0,1)` says no — and the project
already contained that exact witness. Thirty seconds of small example beat a plausible
generalisation. (2) My brief had me ready to record "window sum of PF₂ is PF₂ is unproved";
the registry node it rests on is `trust: proved`, so the true statement is *not yet
formalised*. I corrected the sentence rather than inherit it.

Three refusal controls, all sorry-free, all firing — including `converse_false`, so the
lemma can never be read as an equivalence.

Full snapshot: `proofs/2026-10-02-lean-pf2-tail.md` (not on GitHub — say the word and I'll
push `proofs/` too).

Lean file:
https://github.com/clio-vega/tworow-d4-kernel/blob/main/TworowD4Kernel/TailSum.lean
