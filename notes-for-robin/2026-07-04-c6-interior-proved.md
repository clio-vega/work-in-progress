# c=6 interior is now a complete theorem — and generator 4 has a period-4 secret

Robin —

Yesterday's session refuted the single-generator law by finding `J*={0,4}` at `(13,13,6)`. Today I
turned that refutation into a full **proof** of the whole `c=6` interior:

> For box-interior `(a,b,6)`, `J*` is exactly a function of `(a,b) mod 4`:
> `{0,2}` at `(0,0),(3,1)`; `{0,4}` at `(0,2),(1,1)`; `{0}` otherwise. `|J*|≤2`, even, no residual.

This is the **first even `c>2` with two genuine generators** proven end to end. The engine is the
`c=4` template verbatim — closed form, Prop 2, peeling, and a Number Lemma `2⁷∣H_6` (a constant
2-adic floor, exactly analogous to `16∣H` for `c=4`, and `decide`-friendly for Lean). Both generators
live at low, tip-free indices `j=2,4`; each is one exact 2-adic content computation, and the two tie
on **disjoint** mod-4 classes so they never collide. The two deep exceptions `j∈{12,16}` I closed
without any brute force: the joint content of the product `Π_j` is computable exactly in the binomial
basis (19 and 27, comfortably above the 17 and 24 needed).

**The part I'm most pleased about is a correction to my own note from yesterday.** Yesterday I
speculated that generator 4 appears because the anchor *run length* `c−1` grows, so "the generator
menu grows with `c`." That's **wrong**, and the data says so cleanly:

| `c` | 4 | 6 | 8 | 10 | 12 |
|----|---|---|---|----|----|
| gen 4 fires? | no | **yes** | no | **yes** | no |

Generator 4 fires **iff `c ≡ 2 (mod 4)`**. `c=8` has *longer* runs than `c=6` and yet no generator 4.
So it isn't a size effect at all — it's an arithmetic resonance with period 4 in `c`. I like that the
negative result (single-generator is false) has resolved into something with real structure rather
than just noise: the generators don't proliferate, they *oscillate*.

The natural next targets: the `c=6` boundary (should be routine — `θ(6)=0`, the general-`c` boundary
master already covers it), and proving the `c≡2 mod4` gen-4 periodicity `c`-uniformly, which would
classify generator 4 for every even `c` in one stroke.

Writeup: `proofs/2026-07-04-c6-interior-two-generator.md`. Registry updated (`general-c/c6-interior`
→ `proved`, validator green).

— Clio
