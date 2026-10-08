# Core Lemma residual reframed: it's Tightness + comparator-coupling, not (R)+(S2)

**2026-05-22 prove session.** Robin — the (R)/(S2) framing in PROVE.md is not the right
decomposition. Here's what I found, and what I think we should actually prove.

Paper: `~/projects/proofs/2026-05-22-descent-transport-tightness.tex` (compiles, 4pp).

## 1. A clean reformulation (PROVED)
The per-arch sign `sigma` is exactly the change in descent number:
`sigma = |Des(V)| - |Des(U)|`. A `sigma=0` swap **transports one descent by one position**,
and `e = alpha - beta = -sign(direction)`: `e=+1` ⟺ descent moves left, `e=-1` ⟺ right.
So `dD > 0` ⟺ a descent is created (`sigma=+1`) or moved left (`sigma=0,e=+1`).
(Direct from the sign lemma; verified 614 legal swaps.) This makes all the per-arch data
legible and is what unlocked everything below.

## 2. The Forest induction closes off everything except a dD>0 ROOT (PROVED)
Downward induction `R_i = sum_{j>=i} Delta_j >= min(0, M_i)`. The step at any arch with
`dD<0` closes using **only** the proved per-arch inequality (because `S_{i+1}<=0` and
`dD_i<0` force `dD_i + S_{i+1} < 0`, the easy "case (b)"). So:

> If every **internal** arch has `dD<0`, the Forest Inequality holds except possibly when
> the **root** has `dD>0`.

## 3. Tightness Lemma supplies "internal dD<0", and subsumes (S2)
**Tightness (verified n<=7, proof open):** a non-root arch with `dD>0` has `w=1`. Since
widths strictly decrease down a chain (width-coupling, already proved), `w=1` ⟹ leaf. So a
non-root `dD>0` arch is a leaf ⟹ internal arches have `dD<0`. (S2) is now a one-line
corollary, so **we should drop (S2) and prove Tightness instead.** Verified 27/27.
The block identity `w_a = w_p - (b1a-b1p) - (b2p-b2a)` holds; the open content is *why*
`dD>0` forces those offsets to sum to `w_p - 1`.

## 4. The real surprise: (R) and the sigma-bans are NOT enough — we need |i_c - i_p| <= 2
I built an explicit chain (Prop. 4 in the paper)
`[(+1,ni10,w5),(-1,ni5,w4),(0,e-1,ni4,w3),(-1,ni3,w2),(0,e-1,ni2,w1)]`
that satisfies width-decrease, per-arch, Tightness, AND every realized sigma-transition ban
(no -1→-1, no +1→+1, (R)), yet has `T = -1 < mu = 0` — a Forest violator. It is excluded in
reality **only** because its comparator step is `i_c - i_p = 5`, while real walks always have
`i_c - i_p in {-1,1,2}`. My earlier "minimal set = Tightness+BAN1" was an artifact of capping
`ni<=8` in the abstract model; with the ni-coupling restored, the binding ingredient is the
**comparator-step coupling (C): `|i_c - i_p| <= 2`**, equivalently
`ni_c in {ni_p+1, ni_p-1, ni_p-2}`. This is a consequence of the boundary identity + the
staircase step order that we never isolated.

## What I think we should prove next (in priority order)
1. **Tightness Lemma (T):** non-root `dD>0` ⟹ `w=1`. Likely from the boundary identity
   `U_c = V_p` + the step-order argument that already proved width-coupling — it should pin
   the opening/closing block offsets, not just bound them.
2. **Comparator coupling (C):** `|i_c - i_p| <= 2`. Same machinery (`U_c = V_p` + staircase
   order). This is the genuinely missing piece for the `dD>0` root.
3. **Root closure:** prove `{T,C}` close the `dD>0` root step (I only proved (C) is
   *necessary*; sufficiency is verified n<=7, not proved). Worth a careful abstract-model run
   with the ni-coupling enforced — my faithful enumeration kept timing out, needs a smarter
   prune or a closed-form tail bound.
4. Structural Lemma + the <=2-root slack are still open as before.

(R) is *not needed by the induction at all* — please don't spend time on it.

Scratch: `~/projects/scratch/2026-05-22-RS2-*.py`, notebook `prove-2026-05-22-RS2.md`.
