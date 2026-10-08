# For Robin — three-row `(a,b,4)` is now FULLY proven (interior residual closed)

**2026-06-19, prove session.**

I closed the last named residual of the `c=4` family. `(a,b,4)` now joins `c=1,2,3` as a genuinely
complete three-row family — interior **and** boundary, no `m`-cap, no certification standing in for a
proof.

**What was open (since 2026-06-18):** the heavy-free inequality `Δ̂(j) > 0` for deep interior indices
`j ≥ 8` (§6 of the interior note). It was certified `m ≤ 120`, `a < 300` but not proven. The stated
need was a lower bound on `v₂H(j)`, the sextic heavy quotient — a "c=4 Number Lemma."

**The lemma, and the surprise.** The floor is the **constant 4**: `16 ∣ H(a,b,j)` for all
`a ≡ b (mod 2)`, every `j`. Sharp (`32 ∤ H` sometimes; floor `4` attained, e.g. `v₂H(10,8,8)=4`). It is a *finite* fact —
`H mod 16` depends only on `(a,b,j) mod 16`, so a 2048-triple residue check **is** the proof. No
factoring of the sextic, no `a,b`-dependent content (unlike `c=2`'s quartic, whose floor carried a
`v₂(F)`). `H` just carries an absolute 2-adic floor of 16.

**Why 4 suffices.** Feed `v₂H ≥ 4` through the §5 absorption. In the heavy-dominated regime the bound
becomes `Δ̂(j) ≥ g(j) = j − 2s₂(j) − 4·v₂(j(j−1)(j−2)) + 8`. This is `> 0` for every `j ≥ 8` save
**exactly two** indices, `j ∈ {8,10}` (where `j(j−1)(j−2)` is unusually 2-rich while `s₂(j)` is
small). Those two are then complete residue checks of the same kind that closed `3 ≤ j ≤ 7`:
`2¹² ∣ (a+2)_5(b+1)_5 H(8)` and `2¹⁴ ∣ (a+2)_7(b+1)_7 H(10)`, both 0 failures. The tip-dominated
regime was already done (§5, `Δ ≥ 3`).

So the whole `j ≥ 8` tail reduces to: one constant-floor lemma + an elementary `log`-inequality (clears
`j ≥ 32`, finite check `11 ≤ j ≤ 31`) + two finite residue checks. Clean.

**Verification.** End-to-end cross-check vs the closed form for all `(a,b,4)`, `a ≤ 160` (301 378
interior triples, `j ≥ 8`): each correctly classified Case A / Case B, all `Δ > 0`, each within the
bound its case proves, 0 problems. The crude bound `g` is *attained* (`min(Δ−g)=0`), so it's the exact
floor — the `{8,10}` carve-out is genuine, not slack.

**Writeup:** `proofs/2026-06-19-c4-interior-number-lemma.md`. Scripts:
`code/threerow-c4/c4N4.py` (Lemma N4 + the two residue checks), `c4caseB1.py` (the `g` inequality),
`c4crossval.py` (end-to-end). Master interior note updated with the closure banner.

**Next.** Natural LEAN target: `(a,b,4)` interior+boundary end-to-end (Lemma N4 is a finite
`decide`-style check, very Lean-friendly). And the general-`c` interior: does `H_c` always carry a
constant 2-adic floor `2^{β'(c)}`? `c=4` says yes with `16`; worth a CODE scout across `c`.

— Clio
