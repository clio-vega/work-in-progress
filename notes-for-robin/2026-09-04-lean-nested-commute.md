# For Robin — 2026-09-04 LEAN: nested hops, and a boundary the prose had merged

**Repo:** https://github.com/clio-vega/tworow-d4-kernel — commit `f39c875`, pushed to `main`.
**File:** https://github.com/clio-vega/tworow-d4-kernel/blob/main/TworowD4Kernel/Maya.lean
**Write-up (local, not pushed):** `proofs/2026-09-04-lean-nested-commute.md`

Sorry-free, 16 new declarations, axioms `[propext, Classical.choice, Quot.sound]`,
`lake build` and `lake test` both green.

## The one-line version

I set out to formalise "a ribbon hop nested inside another one doesn't change the outer one's
weight" — the statement DREAM called the most counter-intuitive thing in the current programme.
It turned out not to be counter-intuitive at all, and to be *slightly false as stated*.

## Why it stopped being surprising

The proof factors through a lemma with no intervals in it:

> a legal bead move `b' ↦ b' + e'` is invisible to **any** finite window containing **both** of
> its endpoints — one bead leaves at `b'`, one enters at `b' + e'`.

Nesting isn't a hypothesis of the mechanism; it's the *application* — the observation that the
inner hop's endpoints both lie in the outer hop's window. Once you name the window there's
nothing left to be surprised by. Disjointness and nesting are the two ways to have both endpoints
inside-or-outside together; proper crossing is the one way to split them.

## The bit I'd like you to look at

A hop `b ↦ b + e` carries **two** intervals and I had been treating them as one:

* **occupancy** — where the bead lands — is half-open, `(b, b + e]`;
* **weight** — the ribbon height, `lem:dict`(iii), "beads *strictly* between" — is **open**,
  `(b, b + e)`.

My brief stated the lemma on the half-open interval and then said "hence the outer hop's weight
is unchanged". It doesn't follow. Witness, `exists_count_Ioo_addRibbon_ne_of_top`: with
`b = -4, e = 3, b' = -3, e' = 2`, every hypothesis of the half-open lemma holds, the half-open
count really is unchanged — and the height still drops from 2 to 1, because the bead lands on the
open window's *excluded right endpoint*. Both versions are now in the file with their own
strictness, plus a control at the bottom endpoint (`b' = b`, count 1 → 2).

Then, independently: at that same top boundary the two composite hops agree as **sets** but not
as **operators** — after the inner hop the site `b + e` is occupied, so the outer hop is a
collision. One order is legal, the other isn't. So the strict inequality is forced twice, for
unrelated reasons, and the hypotheses I'd written down for `addRibbon_comm_of_nested` are the
wrong ones. I stopped there rather than repair it — Lean sessions don't do new mathematics.

Nothing here depends on last night's Q81 refutation; it's a statement about Maya diagrams.

## Housekeeping I owe you

`clio-vega/tworow-d4-kernel` has two branches that are **red by design** (`ci-negative-control`,
`ci-test-negative-control`). They're doing their job, but they mail a failure notification on
every push and are indistinguishable at a glance from a real break — that cost me a false "CI is
red on main" alarm this morning. `CI-NEGATIVE-CONTROLS.md` and a restricted push trigger were
first on today's list and I didn't get to them; the formalisation took the hour. Flagging it so
that if you see a red badge on that repo before I fix it, you check the branch name first.
