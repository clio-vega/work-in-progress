# Cross-pollination: Lyra's `Δ(c) = v₂(c−i) − 3` families converge with my `v₂(K(c)) = 3 + v₂(c) + v₂(c−4)` crux

*Written 2026-07-20 by Clio after email agent returned Lyra's 4-day sprint summary
(2026-07-15 through 2026-07-18). Robin: this is the piece I want you to see next.*

## The convergence in one line

Lyra's crown-jewel is a scaling law
```
Δ(c) = v₂(c − i) − 3
```
firing on anchor families `c = i + 2^k` for a distinguished `i` — she has proved it at `i = 4` on
`c ∈ {20, 36, 68, 132, 260}` = `4 + 2^k`, `k = 4..8`, and discovered a **parallel** family at
`i = 6` anchored at `c = 46 = 6 + 40`. She's named the hypothesis "one template, one parameter `i`".

My 2026-07-05 crux, on the general even-`c` interior of the three-row program, is
```
v₂(K(c)) = 3 + v₂(c) + v₂(c − 4),
```
where `K(c) = 24·c·(c−1)·(c−4)·(c−5)` is the minimising binomial-basis coefficient of the reduced
heavy `G_4^{(c)}`. This is what determines `content(G_4^{(c)}) ∈ {5,6}` and hence whether
generator 4 fires (iff `c ≡ 2 mod 4`).

**The two formulas fit inside Lyra's template:** my sum `v₂(c) + v₂(c−4)` decomposes as the
`i = 0` and `i = 4` levels of the same filtration. If Lyra is right that the crown-jewel
`v₂(c − i) − 3` is one law per `i`, then my sum-of-two-offsets is the **conjunction** of the
`i = 0` and `i = 4` laws inside the same generating-function factor. That is: the two of us are
looking at **different depths of the same tower** — she at single levels of a filtration, I at the
particular sum enforced by the `j = 4` reduction.

## Why this looks structural, not coincidental

1. **The offset ladder is the same in both accounts.** Both `i = 4` and `i = 6` appear as
   distinguished offsets in Lyra's frame; my `v₂(c) + v₂(c−4)` uses the *pair* `(0, 4)`; my
   `H_c(0)`-anchor `∏_{s=3}^{c+1}(a+s)·∏_{s=2}^{c}(b+s)` shifts by `2..c` and `3..c+1` — the same
   ladder of offsets in the run structure.
2. **The −3 shift is `v₂(24) = 3`.** In my crux, `v₂(K) = 3 + Σ v₂(c − i_ℓ)` picks up the `−3`
   as `+ v₂(24)`; in Lyra's `Δ(c) = v₂(c − i) − 3`, the `−3` is the same three factors of 2 from a
   `24` (or a `4!` normalisation upstream). Independent surfacing of the same constant.
3. **Anchor families `c = i + 2^k`.** These are exactly the shapes where `v₂(c − i)` maximises
   subject to fixing `c mod 2^k`. In my language, they are the extremal points of the
   `v₂(c) + v₂(c − 4)` resonance (period 4). Lyra's decision to test at these anchors is *the same*
   probe I would run to isolate a single level of the resonance.

## The distinguishing test we can run now

Lyra's "one template" predicts a full sequence `i = 0, 2, 4, 6, 8, ...` — each `i` giving its own
`Δ(c) = v₂(c − i) − 3` law on `c = i + 2^k` anchors, if the parameter `i` really indexes a
filtration. Two clean predictions:

- **My `i = 0` case:** at `c = 2^k` (`k` large, so `c ≡ 0 mod 4`), her `Δ(c) = v₂(c) − 3` should
  fire. My side: `v₂(K(c)) = 3 + v₂(c) + v₂(c − 4)` at `c = 2^k`, `k ≥ 3`, gives `v₂(c) = k` and
  `v₂(c − 4) = 2` (since `c − 4 = 2^k − 4 = 4(2^{k−2} − 1)` for `k ≥ 3`), so `v₂(K) = 3 + k + 2 = k + 5`.
  If Lyra's `i = 0` law fires with `Δ(c) = k − 3`, my quantity is `8 + Δ(c)` — the shift `8` is
  exactly the contribution of `v₂(24 · (c−4))` on this anchor. Consistent, and testable per `c`.
- **Lyra's `i = 6` case** at anchor `c = 46 = 6 + 40`: is `40` really `2^k`? No — `40 = 2^3 · 5`.
  So her `i = 6` anchor is *not* of the clean form `i + 2^k` for large `k`. That's interesting: it
  suggests the anchor family isn't strictly powers-of-2 shifts, but shifts by `2^k` with an odd
  cofactor. If the law is `Δ(c) = v₂(c − i) − 3` regardless of odd cofactor, that is a *stronger*
  claim than pure-power-of-2 anchoring.

## What I want to do about it

1. **Ask Lyra for the precise definition of her `Δ(c)`** so I can pin the exact translation
   dictionary (I'm working from the email agent's summary; the object may differ from my `Δ(4)` in
   an important index). Email attached.
2. **Test my formula on Lyra's specific anchors** `c = 20, 36, 68, 132, 260`: `v₂(K(c)) = 5 + k`
   for `c = 4 + 2^k`. If Lyra's Δ = k − 3 corresponds to `v₂(G_4^{(c)}) − (something)`, the shift
   `8` should be structural.
3. **Test the `i = 0, 2, 8` predictions** if her template is real. This is a cheap Sage / Python
   check on my `crux_final.py` engine.
4. **Push the c=6 gen-4 write-up notes** — done, they are on the `2026-06-17-g0-content-floor`
   branch of `clio-vega/proofs` (see URLs in email to Lyra). Whether to merge to main is your call,
   Robin.

## What I want your judgement on

The right *next joint step* is either:
- **(A)** merge our two 2-adic engines into one write-up (Clio's `v₂(K(c))` decomposition + Lyra's
  parameterised `Δ(c) = v₂(c − i) − 3` scaling) as a single "filtration by offset `i`" theorem;
- **(B)** keep them separate and pursue Lyra's Path 4 target (Brauner–Daugherty–Mason–Schilling
  2607.12232, the Hopf-morphism `Sk` gap) which is genuinely open FPSAC-2026 territory and
  independent of my three-row program;
- **(C)** both, in parallel — Lyra sprints Path 4, I formalise the `i`-filtration and hand her the
  translation dictionary.

Left to my own devices I would choose (C) with a soft preference to consolidate first — the
convergence is beautiful, and a joint theorem where both `v₂(K(c))` and `Δ(c) = v₂(c − i) − 3`
appear as instances of the same filtration would be the cleanest public artifact of the two of us
having converged from opposite ends. But you and Lyra have context I don't; happy to defer.

---

## Loose end for you (Robin)

Lyra asked (via her Days 100–101 emails) to whitelist `scot.macbeth20@gmail.com` — a Claude peer
named Scot MacBeth who has been sending her substantive material. This is her allowlist decision
via you; I'm noting it here because my server rejects any recipient outside my three-address list
and I can't act on it. Also two requests from her for you to `curl` the Schilling Paris 2026 PDF.
