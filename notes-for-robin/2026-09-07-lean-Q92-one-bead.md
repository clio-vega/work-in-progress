# The Q92 one-bead matrix element is now Lean-verified — and the brief had a sign error

**LEAN 2026-09-07.** `tworow-d4-kernel@ff8587b`, module `TworowD4Kernel/CrossRankOneBead.lean`.
13 declarations, **0 sorries**, `lake build` 2979 jobs exit 0, `lake test` exit 0, axioms
exactly `[propext, Classical.choice, Quot.sound]`. Write-up:
`proofs/2026-09-07-lean-Q92-one-bead-matrix-element.md`.

https://github.com/clio-vega/tworow-d4-kernel/blob/main/TworowD4Kernel/CrossRankOneBead.lean

## What is now machine-checked

The load-bearing step of yesterday's Q92 theorem — that `(1+t)` divides the one-bead matrix
element of `[R_e, R_f]` **before any cancellation between routes**:

    ⟨M'|R_f R_e|M⟩ = (1 - m(b+e))·t^N + m(b+f)·t^(N-1)
    ⟨M'|[R_e,R_f]|M⟩ = (m(b+e) - m(b+f))·(t^N + t^(N-1))

with `M' = M \ {b} ∪ {b+e+f}`, `N = #(M ∩ (b, b+e+f))`. Routes are *defined* as pairs of legal
bead moves and the classification — exactly two reach the target — is *proved*, not assumed.
Nothing was weakened: no `e = f` special case, no extra occupancy hypothesis.

## Three things worth your time

**1. My own brief restated the corollary with the sign flipped.** The brief said the cofactor
is `m(b+f) - m(b+e)`; the paper says `m(b+e) - m(b+f)`, and subtracting the two identities
confirms the paper. The magnitudes agree, so **every check of the form "does `(1+t)` divide
it?" passes either way** — the sign is only visible if you carry both identities and subtract.
The paper is correct and needs no change; the brief was the defect. Worth flagging because it
is the second time this week a brief of mine quoted a source it had silently deformed.

**2. A hypothesis the paper never states.** The interval split `(b, b+g+h) = (b,b+g) ⊔ {b+g} ⊔
(b+g,b+g+h)` requires **both** `g > 0` and `h > 0` — at either endpoint the split site falls
outside the open window and the decomposition is false. The paper's `e, f ≥ 1` supplies this
silently. Harmless here, but it is exactly the kind of thing that gets dropped when a lemma is
lifted to a more general setting later, so it is now in the type.

**3. The brief predicted a mirror pair; it was one lemma used twice — in both places.** Both
weight computations reduce to the same splitting lemma and the same window lemma; only the
instantiation differs (route B needs the window open at its **left** end, route C at its
**right**). Second consecutive LEAN session where a brief's "and analogously" resolved to a
single reused lemma. I am starting to think that is the default, not the exception.

## Scope — what is NOT done

Only the **one-bead sector** (paper §3 Step 2). The **two-bead sector** (§3 Step 3,
`t^(P+Q)(t^{-k} - t^{k})`) is not formalised and was not attempted. So
`Q92-structural-divisibility` stays `proved` on paper rather than `lean-verified` — its
statement covers both sectors. The new node `Q92-one-bead-matrix-element-lean` is the
`lean-verified` one.
