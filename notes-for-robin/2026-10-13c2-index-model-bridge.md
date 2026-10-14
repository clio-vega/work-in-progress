# For Robin — the index-model bridge landed (2026-10-13 c2)

**Read it here (I can't show you local files):**
https://github.com/clio-vega/proofs/blob/main/2026-10-13c2-lean-index-model-bridge.md
Lean: https://github.com/clio-vega/tworow-d4-kernel/blob/main/TworowD4Kernel/IndexModelBridge.lean

## The short version

For four sessions `ord_{t=1} Ψ_T = ν(T)` has been *two* Lean theorems that could not be
multiplied together. Gap 2 lives on `ZMod h` (0-based, wrap in the ring); gap 3 lives on
1-based `ℕ` (wrap in a function `succIdx`). Both said `|J|`. Neither `|J|` was the other's.
That's now fixed: `idxEquiv : ZMod h ≃ {i // 1 ≤ i ∧ i ≤ h}`, `j ↦ j.val + 1`, and the
composite `sum_rootMultiplicity_eq_content_ones` chains gap 2 → bridge → gap 3 → gap 1 in one
declaration with no leftover hypothesis on the multiplicities. 18 declarations, 0 sorries,
standard three axioms.

## The part I think you'll like

I went in expecting a twist. Yesterday's note flagged that Model A reads the `i`-th unit
vector's ascent set as `{i − 1}`, not `{i}`, and warned that a bridge off by one is *worse*
than no bridge because it type-checks. That warning was right about the shift and wrong about
its address. The intertwining square commutes on the nose. The `−1` lives in the **word**
transport — a 1-based word has to read a 0-based word one place down — not in the index map.

A bridge between index models is a composite of two maps, and a predicted off-by-one tells you
the composite is shifted without telling you which factor carries it. So I stated the index
fact and the word fact as separate declarations, specifically so neither could hide inside the
other, and then ablated: the shift-free transport is a perfectly well-typed bridge that puts
the ascent at index 1 when the truth is index 2. The failure mode was real. It was just one
map over from where we were looking.

## What I did not do

I did **not** promote `cyclic-ascent-lemma`. It asserts six things; Lean carries three
outright and one only at content `(1^n)`. That's the fifth consecutive decline and I still
think it's the right call. What genuinely changed is the obstruction count: **2 → 1**. The
A-against-B non-composition is closed. What's left is the tableau-to-word reduction — that
content `(1^n)` forces each occupation word to *be* a unit vector — which is strip
combinatorics, not index bookkeeping, and is a different session.

## Two things about the tooling, since they'd bite you too

* `registry_validate.py`'s documented invocation reports **67 problems over 67 nodes** — it
  joins `proofs/` onto a path that already starts with `proofs/`. `--proofs-dir .` is clean.
  That's the ninth tool with this exact fault, and the signature is unmistakable once you look
  for it: *a problem count equal to the node count is the diagnosis, not the problem.*
* `autoImplicit` is **on** in the Lean project — `lakefile.toml` sets only
  `relaxedAutoImplicit = false`. I confirmed by probe rather than by reading, and the new file
  opts out locally. Worth deciding whether to set it false project-wide; I didn't, because 60+
  files is a different target than the one I was given.

And one on me: my first declaration count read 17 instead of 18, because `@[simp] theorem` hid
a declaration from a line-anchored grep — so both controls ran over the wrong domain while
agreeing with each other perfectly. I caught it only by counting a second way. Then I read a
67-line problem list as 12 because I tailed the log. Both numbers were re-measured; the ones in
the writeup are the real ones.
