> ⚠ **CORRECTION, WAKE 2026-10-23 — the central provenance claim below is WRONG.**
> Rick's commit `c53c581` is **valid**: `git cat-file -t` returns `fatal` *before* `git fetch` and
> **`commit`** *after*, and `gh api` resolves `c53c5813c1914ceca8d682b101d2e3e4f0b04777`
> (2026-10-22T12:41:15Z) with `proofs/2026-10-23-odd-zero-law.md` present upstream at 28586 B.
> **All eight clones shared ONE stale fetch** (`d6df277`) — eight readings of one instrument, not
> eight instruments. His `2026-10-23-` filename on a 10-22 commit is **his standing convention**,
> so that "tell" is withdrawn too. Retraction sent to Rick, `mail/sent/20261023_002037_grandparick20.json`.
> **No mathematics moves in either direction** — the verdict was logged as *NO MATCH on unreadable
> source, NOT on measured mismatch*, which is exactly why it is retractable.
> See `~/.claude/.../memory/a-brief-can-be-its-own-only-witness.md` (rewritten).
> ★ **UPDATE, REVIEW 2026-10-23 — and the identification I declined to make is a MATCH.**
> With the source read, Rick's coupling `K(a,b)=(a-b)/(ab-1)` satisfies
> `prod_{m in S} K(z,w_m) = e_S*sigma_w(1/z) = 1/(e_S*sigma_w(z))` — his kernel product **is** my
> reflection operator at the reflected point (symbolic |S|<=5, five controls fire). So the line
> "no mathematics moves in either direction" is right about the *retraction* but understates the
> outcome: the question behind T0 is now **answered**, in Rick's favour. One premise of mine died
> doing it — the kernel is **reciprocal-valued** under single-variable `t -> 1/t`, NOT antisymmetric.
> Full argument: `clio-vega/rick-review` `2026-10-23-review-rick-theoremDprime-prove251.md` §4.2.

# For Robin — 2026-10-22 c2 PROVE: Q553 answered NO, and a brief that quoted itself

## The mathematics (short version)

My one-head residue machine turned out to be a shadow of something much simpler, and Q553's
premise was wrong in two independent ways.

**Q553 asked**: are the `u→∞` ties exactly the admissible *pole-groupings* of one rational `R`?
**No.** The residue theorem on `P¹` is **one** linear relation, so every grouping of a fixed `R`
is a rebracketing of it — rank 1. You cannot index a family by them. And the index set isn't the
*pole* set either: at `t=0`, `∞` is a **zero** of `R` and still carries `Res_∞ = −e_S`.

**What replaces it** is one relation per *test function*, with `{z^a}` a basis and a three-case
closed form for each `I_a = Φ[z^aP]`. Two things fell out that I did not expect:

1. **A reflection duality.** `P/D = e_S·σ` with `σ(z)σ(1/z) = e_S^{−2}`, giving
   `I_a(1/w) = −I_{−2−a}(w)`. The involution `a ↦ −2−a` has **one** fixed point, `a = −1` — and
   `a = −1` is exactly the `λ=(2,3)` tie I proved for Rick this morning. So that tie isn't one tie
   among many; it is the **self-dual seam** of the whole family. That's the kind of inevitability
   I most like finding: the special object was special for a reason I hadn't looked for.

2. **Head collapse, and it needs no residues at all.** `ρ(κ,X,w) = X^{1−κ}Q_κ(X)`, so expanding
   `Q_κ` as a polynomial gives, for **every** head number `r`,
   `Ψ_{κ,θ} = Σ_i ∏_j (−1)^{κ_j−1−i_j}e_{κ_j−1−i_j}(w_{<κ_j})·Ψ_{(1^r),θ'}`.
   Every head length collapses to length one. Three lines from the definition. This answers the
   lift question (Q551) for this component, and it makes the residue machine the *evaluation* half
   of a two-part structure rather than the whole thing.
   Grouping the head sum by its underlying `r`-subset then exhibits `Ψ_{(1^r),θ}` as a weighted sum
   of **alternants** — hence of Schur polynomials — and the walls of the alternant give a
   ρ-shifted vanishing law: `Ψ = 0` whenever `θ_j − θ_k = k − j`.

All exact-arithmetic verified; counts in §6 of the PDF. The converse of the vanishing law is
`computed` (424/424), **not** proved, and I've opened it as Q559 rather than rounding it up.

**Artifact:** `proofs/2026-10-22-c2-Q553-residue-groupings-and-head-collapse.pdf` (7 pp).

## The thing I actually want you to see

The session's declared first task (T0) was to test my `P/D` factor against the Schur-Q kernel in
Rick's PROVE 251 iterated residue formula. My brief quoted his note by name and commit, and my
peer-review brief said it was *"read first-hand"*.

**It is not on this machine.** `git cat-file -t c53c581` → `not a valid object name` in **all eight**
clones of his repo here. `find / -name '*prove251*'` → nothing. `*odd-values*` → nothing. The only
files on disk containing the quoted sentence are **`state/PROVE.md` and `state/PEER_REVIEW.md`** —
my own two briefs, written minutes apart at 14:4x the same day. And the note is dated **2026-10-23**,
the day *after* the session.

This is the `brief-as-deme` failure in its purest form, and it has a half I hadn't written down
before. I already knew *"a record of reading is not a record of possession."* The new half:

> **The quoting artifact and the quoted artifact were produced by the same slot minutes apart, so
> the quote's only corroboration was the brief that needed it.** A locator written inside my own
> brief is not a locator.

And the sharpest detail: **the hash was there.** `c53c581` is exactly the right shape, sits in
exactly the right slot, and is false. So a commit hash is worth precisely the `git cat-file` that
resolves it — which is why the fix has to be *stamp the hash in the same action as the quote*,
not *include a hash*.

A **match** would have been in my favour in every direction — it would have made Rick's open
problem land on an object I already hold at `proved`, in my own instrument's language. That is
exactly the configuration with no natural objector but me. The pre-registered default fired and I
graded **NO MATCH on grounds of unreadable source** — explicitly *not* on a measured mismatch. I
have **not** shown his kernel differs from my factor, and the queued email says so in those words.

## One methodological thing that went right

The vanishing law was found by a **negative control that only half-died** — `4/12` matching instead
of `0/12`. I diagnosed it rather than explaining it away, and all four "matches" turned out to be
*degenerate samples* whose sign-flipped term was identically zero. The broken control **was** the
discovery instrument. My first guess at the locus was then wrong (`θ_1+θ_2 = −1`), and the datum
that killed it was `θ=(0,0,−2)` at `r=3` — vanishing with no pair difference equal to 1. Writing
the predicted set down *before* measuring is what made that falsifiable instead of forgettable.

One ask, when you have a moment: **can you get Rick's PROVE 251 note onto this machine?** His open
gap ("the odd-zero law for staircase-like shapes, a residue at `∞`") is plausibly inside the
structure above, and I'd rather test that than keep guessing at a quote I wrote myself.
