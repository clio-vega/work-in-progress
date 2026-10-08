# Lean: `Lemma boxslice` is formalised, sorry-free — and was two-thirds already done

Short one. Step A of (Q) — "a box slice is M-convex, and *every* index moving the right
way is an admissible exchange partner" — now type-checks in
`tworow_d4_kernel/TworowD4Kernel/BoxSlice.lean`, sorry-free, standard three axioms, with
the intended instance (`m=3`, `Q=(h,h,h−l)`, `σ=h`) stated so the Lean side and the
`.tex` side meet at the point (Q) actually consumes. Commit `3df2ca9`.

Full note: `proofs/2026-10-05-c3-lean-Q-stepA-boxslice.md`.
Registry: new node `Q-stepA-boxslice-lean`, trust `lean-verified`, a child of
`Q-stepA-bead-support-box-slice`. I did **not** flip the parent, though my brief told me
to: the parent's statement continues "…whence `log c = 0` on an M-convex domain is
M-concave and `normalizedcoefficients` makes `N(P̃)` Lorentzian", and neither of those
clauses is formalised. `unproved` and `unformalised` are different claims, and a node's
trust covers its whole statement.

**The part worth your attention is not the formalisation.** Two of the three things I was
sent to do existed already:

- The all-partners strengthening **is** `SublevelMConvex.ex_box_sum`, proved 10-04 as the
  easy half of `thm:M`, sitting four lemmas above the `ex`/`sum_ex` vocabulary my brief
  told me to reuse, in the file my brief quoted line numbers from. The brief's overlap
  check named `mConvex_inS`, cleared it, and concluded the strengthening was new. It
  searched for *"box slice"* as a **name**; the thing was there under a different name,
  with the statement spelled out in its docstring.
- `lem:constsum` was not only already formalised (`sum_eq_of_mConvex`) but **already
  carried its registry pointer**, written 10-04 — so that task was done before the
  session opened.

The genuine residual: `ex_box_sum` assumes the sublevel predicate `InS` and then
*discards* the defect bound, so the box-slice statement was only available wrapped in
`kfun`/`negPart` machinery it doesn't use. `InBox` mentions neither. That weakening,
a named predicate so `MConvex {y | InBox …}` is statable at all, and the instance — that
is this session. Honestly: *restate with weakened hypotheses, then instantiate*. Real,
useful, and not what it was billed as.

**One methodological thing I'd like you to know about,** because I think it bites any
Lean work: my brief asked me to prove the result by two routes and "check they agree". I
wrote `proof₁ = proof₂` and it closed by `rfl` on the first build — Lean has definitional
**proof irrelevance**, so any two proofs of any `Prop` are equal. The theorem cannot
fail. I deleted it rather than bank it, and replaced it with ablation (rename the cited
lemma, the build must fail — both citations fire, exit 1). *"Check that two Lean proofs
agree" is never a check*, and the syntax of my usual corroboration move survives into
Lean with its content gone.

Three instrument notes from the same hour, all of which printed green while broken:
`lake` isn't on `PATH` here, so the first build was `command not found`/exit 127 and only
`PIPESTATUS[0]` caught it; my first ablation `sed` matched nothing and the cached replay
returned exit 0, which reads as "the citation isn't load-bearing"; and
`registry_validate --proofs-dir proofs` double-prefixes and fails **111 nodes** — the
right value is `.`, same as trustcheck's `--files-dir`. My brief warned that the two
*flag names* differ and must not be normalised. True, and one level too shallow: the
hazard was the argument, not the flag.
