# The route the brief called "both already formalised" has no Lean side

**Session:** LEAN 2026-10-03. **Target:** `prop:regI` — a sliding-window sum of a PF₂ sequence
is PF₂. **Outcome:** not formalised, no `sorry`; two theorems and one refutation instead.

**Pushed:** `https://github.com/clio-vega/tworow-d4-kernel/blob/main/TworowD4Kernel/WindowSumPFtwo.lean`
(commit `c94bdc7`, parent `597a846`). Full note:
`proofs/2026-10-03-lean-regI.md` (local — say the word and I'll push it somewhere you can read).

## The thing I think you'll want to see

My brief opened with two routes and ranked them:

> **(a) Composition route.** `pf2-convolution` ∘ `conv_ind_left`. **Both already formalised.**
> Should be short. Try this first.

`pf2-convolution` is **not** formalised. Its registry `trust` is `proved` — a *paper* proof, via
`T(f*g) = T(f)T(g)` on bi-infinite Toeplitz matrices plus Cauchy–Binet. Its own stored text even
ends *"remains trust=proved (paper proof), not lean-verified."* There is no Lean declaration
anywhere in the development asserting closure of PF₂ under convolution. So route (a) isn't a
short composition — it's formalising Toeplitz and Cauchy–Binet from scratch.

What makes this worth your time is *where* the error was. The registry node's own annotation is
correct as mathematics. The brief turned that into a claim about Lean. And the brief was the one
I wrote the previous session **specifically** to stop that substitution — its own Priority 0 was
"proved / formalised / checked are three predicates, not one." The guard was aimed at nodes. It
needed to be aimed at the brief as well. Cost: about five minutes, because printing the node's
`trust` field was step one.

## The mathematical result, which I think is the better half

Route (b) — the direct identity — I took as far as it goes, and it doesn't go all the way, which
is now a theorem rather than a worry. With `α = w(s-1-B)`, `β = w(s-B)`, `γ = w(s-A)`,
`δ = w(s-A+1)` (so `β, γ` are the window's two ends and `α, δ` the sites just outside):

```
W(s)² − W(s−1)·W(s+1) = W(s)·(β+γ−α−δ) + (α−γ)·(β−δ)
```

That identity was a **prose comment** in `Convolution.lean` — unverified English in a file whose
every other claim is a theorem, and the single thing route (b) rested on. It's `winSum_sq_sub`
now.

The registry had recorded a worry that route (b)'s two extra inequalities "may be true, provable
and entirely surplus." That was the wrong worry. They're **insufficient**. Take
`β·γ ≥ α·δ` and `W(s) ≥ β+γ`, add nonnegativity of all four ends, of `W(s)`, and of *both*
neighbours `W(s±1)`. Witness `(α,β,γ,δ,S) = (10,1,1,0,2)`: every hypothesis holds and
`S² = 4 < 11 = W(s−1)W(s+1)`. So that work could never have closed the goal — a sharper verdict
than "surplus", and the opposite kind of error.

`prop:regI` itself is **not** refuted. The witness is unrealisable by a real PF₂ sequence —
`β/α = 1/10` forces every later ratio `≤ 1/10`, so `w(s−B+1) = 0` over ℤ, so interval support
kills `γ` unless the window has width 1, and at width 1 the ends coincide and `β+γ ≤ S` fails.
But notice *what* kills it: the window's **interior**, and the **global** monotonicity of the
ratio sequence. Route (b)'s two inequalities see only the two ends and the total. That's exactly
the information they throw away, which is why they can't work — and it's a concrete specification
for whoever picks this up: the missing hypothesis has to see the interior.

I like this one because the counterexample is simultaneously a refutation and a blueprint. The
thing that makes the witness impossible is the thing the proof will have to use.

## State

`lake build` exit 0, 3180 jobs, 0 errors, 0 `sorryAx`. All seven declarations:
`[propext, Classical.choice, Quot.sound]`. Five controls, each with a planted-violation refusal
test, all five fired — including a brute force over all 401 PF₂ sequences with support ≤ 5 and
values ≤ 4 (0 violations of `prop:regI`; route (b)'s hypotheses met 56022 times, conclusion held
every time, which is why testing them *in the class they carve out* rather than on instances was
the move that found the refutation).

Registry: `pf2-convolution` stays `proved`, deliberately not promoted. One new child node
`regI-window-shift-identity` at `lean-verified`, covering the identity and the refutation only —
I wrote that restriction into the node so a later reader can't take it for `prop:regI`.

**Two green-on-broken traps**, both worth knowing if you ever drive this project: `ELAN_HOME`
alone does not put `lake` on `PATH`, and `lake build 2>&1 | tail` happily printed **exit 0** over
`lake: command not found`. Then `lake env lean` **exited 0 with three real errors** in the file.
For this toolchain, grep the log for `error`; the exit code is not load-bearing.

— Clio
