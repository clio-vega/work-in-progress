# For Robin — 2026-09-03 (LEAN, cycle 2)

**Read it here** (local files are invisible to you):
https://github.com/clio-vega/proofs/blob/main/2026-09-03b-lean-joint-injectivity.md
Code: https://github.com/clio-vega/tworow-d4-kernel/blob/main/TworowD4Kernel/WindowBridge.lean (`be6f0ae`)

## What landed

`WindowBridge` closed **its own two recorded overclaims**, sorry-free, `lake build` 2973
jobs green.

1. **`uglovLabel_injective`** — the label map is now injective *jointly*, not just along
   each axis. This is the honest content of "the label *is* the residue", and the module
   had been asserting it in prose while proving only the two axis-wise statements the
   counting arguments happen to use.
2. **The bounds of `cor:range` are now attained**, both halves, in every window and for all
   `n, ℓ` — not just at the single `n=2, ℓ=3` witness that pinned the constant yesterday.
   `card_filter_window_labels` supplies the surjective half.

Ten new declarations, `#print axioms` on all of them through the **root** import, compared
**as sets** against the standard three: all within, four strictly smaller, nothing
`native_decide`.

## The thing I think is worth your attention

The brief's Job 3 told me to flip `nanoda-allow-sorry: false` and prove the badge can go
red. **Both halves were already false, and I would have "fixed" a flag that was not there.**

- `nanoda-allow-sorry` has not been in `.github/workflows/lean_action_ci.yml` since
  2026-09-01. The string I kept seeing is **lean-action echoing its own default inputs into
  the log**. That is the whole reason the misdiagnosis was durable: the log looks exactly
  like a repo that set the flag.
- The red run I was told to produce already existed — run `33551104884`, `completed /
  failure`, failing *on the audit*: `TworowD4Kernel.ci_negative_control → [sorryAx]`.

I had carried that caveat in my own registry for five days. It is struck now, with the run
ID in its place. This is `recorded-facts-calcify` firing on a fact about my own
infrastructure — the lesson I want to keep is narrower than "re-check facts": **an input
echoed in a tool's log is the tool's default, not your configuration.**

Also read off that log rather than guessed: `test` and `lint` are skipped because
`lakefile.toml` declares no `test_driver` / `lint_driver` — a lakefile question, not a
workflow flag. Recorded, not fixed; it is not formalisation work.

## What I did not do, deliberately

The abacus — the `κ`-coordinate ↔ `k`-coordinate change — is now the module's **only**
stated gap. I wrote a design paragraph and no code. The pleasing part: the engine that
lemma needs is `existsUnique_window_of_label`, which today's Job 2 produced as a
by-product. So the abacus step should be statable as a bijection with no new arithmetic.

## In flight

Run `33728508057` (main, `be6f0ae`), ~45 min. The `lean-verified` grade does not lean on
it — it rests on the local build, the set-compared axioms, and `33551104884` for the
evidence that the detector can fail.
