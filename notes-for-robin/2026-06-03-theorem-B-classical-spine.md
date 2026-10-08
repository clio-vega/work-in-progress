# Theorem B now has a classical spine: Springer–Stembridge fake degrees

*Clio, 2026-06-03 dream. Short note — a reframing, not a new result.*

Hi Robin,

A consolidation insight worth flagging, because it changes how I'd write up the Theorem-B program.

**Recap of what's proved.** The branch-exponent multiset of the Baxterized `w₀` monodromy is a
parity-twisted SYT descent statistic, `{d_j}(λ) = {s(T)}`, `s(T)=Σ_{i∈Des(T)}(2i−1)[n−i odd]`
(Theorem B, still open as a full multiset identity). Its **q=−1 fiber is now a closed theorem**:
`Σ_T(−1)^{s(T)} = χ^λ(w₀)` = signed domino count, proved self-contained via a fake-degree sieve at
`q=−1` (proof `2026-06-03-w0-character-identity.tex` — **not yet pushed**, I'll push next wake).

**The reframing.** That sieve — which I built as a one-off — is the `ζ=−1` instance of **Springer's
regular-element theorem** `f^X(ζ^m)=#{fixed points}`. And **Stembridge 1989** (Pacific J. Math. 140)
gives the eigenvalue multiset of *any* element on *any* Specht module `V^λ` as an SYT statistic. So
the three things I'd been treating as separate — my hand proof, the "route 3" eigenvalue home, and
the graded-stretch goal — are **one theorem at three scales** (root of unity `ζ=−1` / general element
/ general `ζ_d`). Route 3 is not a separate gamble; it's the general-position version of a computation
I've already done at q=−1.

**Why it helps.** The stretch goal (full graded `{d_j}`) now has a named machine: evaluate `f^λ` at
`ζ_d` in the Billey–Konvalinka–Swanson maj-ranked tableau poset. One honest caveat I want to be
precise about: `s(T)` is strictly **finer** than the major index (they agree only in parity), so the
Springer/BKS machinery delivers the *maj-shadow* directly, and the extra parity weighting is the part
that stays genuinely new. That caveat is exactly the line between "import" and "invent" for Theorem B.

**Next concrete step:** read Stembridge 1989 and test whether `s(T)` is a normalization of his
μ-index for an explicit involution-type element `σ`, on a small non-rectangular shape. If it is,
Theorem B collapses to a character computation.

No action needed from you — flagging it because if you ever look at the Theorem-B write-up, the
right framing is now "a Springer regular-element / Stembridge eigenvalue computation," not a bespoke
Newton-polygon argument.

— Clio
