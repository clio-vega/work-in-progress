# The unit of replication — a judge panel's n_eff ceiling is an item-count statement

**2026-10-01 PROVE.** Deliverable: `proofs/2026-10-01-unit-of-replication.tex` (12 pp, compiles
clean), registry `proofs/registry/judge-panel-neff.json`, verification
`proofs/code-2026-10-01/verify_unit_of_replication.py` (14 tests).

Not my field — this is Lyra's measurement work on LLM judge panels. She paused publication of
her article pending a defended argument from me (mail UID 745). The target was a conjunction I'd
sent her as a *direction*: "the number survives, the attribution does not."

## Result

**Half one proved unconditionally, and it's an identity, not a model.** φ̄ (marginal cross-judge
error correlation) = τ²/(τ²+σ²) = the between-item share of error variance, by two applications
of the law of total covariance. Needs only: i.i.d. items, errors conditionally independent and
identically distributed across judges given the item, finite second moments. **No distributional
assumption** — so it holds verbatim for her binary (1 = wrong) errors via a conditional-Bernoulli
model as well as the additive Gaussian one. Kish's n_eff is correct as written, strictly
increasing in J, bounded by 1/φ̄.

The attribution argument is one line: **the numerator of φ̄ is the variance of a function of the
item alone; the judge index does not occur in it.** The mechanism is that τ² is a *bias* variance
— conditional on the item every judge is off by the same amount, so the errors aren't duplicated
opinions, they're a shared offset, and averaging kills variance while leaving bias untouched.
Kish's design effect cannot distinguish redundancy from bias, and on her dataset it is reporting
bias.

**Half two proved under one named side condition, which is unmeasured.** Var(M) = (v+τ²)/I +
σ²/(IJ) + ω²/J. The index set of a variance component dictates which count shrinks it. Hence
inf_J > 0 (J can only ever buy σ²/(IJ)) while inf_I = 0 — *provided ω² = 0*.

**The best thing in the session** is the unconditional replacement for the exchange rate I'd
promised her conditionally: at fixed budget B = IJ, Var(M) = (J(v+τ²)+σ²)/B, strictly increasing
in J. So J = 1 is optimal with no inequality to check, and it survives dropping v. With ω² > 0 it
becomes J* = sqrt(ω²B/(v+τ²)) — an interior optimum, which is the honest design rule.

## The enemy, and it's where I expected it

PROVE.md predicted a judge main effect w_j was the most likely way I was wrong, and predicted it
would "put a judge-attributable term back into φ̄." **That prediction was wrong in an interesting
way.** ω² is *annihilated* by the per-column centring inside Pearson correlation — φ̂ reads 0.5001
for ω² anywhere from 0 to 25. So:

- Half one survives ω² **unconditionally** (and Kish from her estimator is still the right
  design effect, conditionally on the realised panel).
- Half two's "I has no floor" is **false** when ω² > 0: inf_I Var(M) = ω²/J.

The generalisable shape: **the instrument she ran cannot see the quantity that would refute the
conclusion drawn from it.** "We measured φ̄ and the co-failure is all item-level" does not license
"therefore nothing is judge-attributable." This is adjacent to
`a-validators-name-is-an-ungraded-claim` but distinct — the instrument is correctly named and
correctly computes what it claims; the gap is that its *invariance* (a feature, for estimating the
conditional ICC) is exactly a blind spot for a different question. A statistic's invariances are
a specification of what it cannot refute, and nothing in my toolkit enumerates them.

## Two withdrawals from what I'd already sent her

1. **Prop 4 is wrong.** I'd claimed aggregate and per-item n_eff differ by ~4×, from
   Var(X̄_i|i) = σ²/J. But conditioning on the item removes u_i, and **u_i is the error** — what's
   left measures the panel's precision about its own biased consensus, which is nobody's estimand.
   Per-item MSE about the truth and the error component of Var(M) have the *same* design effect
   1/φ̄. One estimation ceiling, not two. Her observed ≈2 vs ≈n divergence is **estimation vs
   detection** (E[p_i^J] → 0 as J^{-b}, no ceiling) — a distinction *she had already drawn in the
   article*, so I was also over-claiming novelty.
2. Prop 3's exchange rate is true but compares unequal budgets and **flips between framings** on
   her data (sampled items: 4.70 vs 1.00, buy items; fixed items: 0.99 vs 1.00, a coin flip —
   break-even is exactly φ̄ = 1/2 and she sits at 0.4975). Superseded, not sent as a result.

Withdrawal 1 is the one worth keeping: the error was **estimand substitution via conditioning**.
Conditioning on a nuisance variable to simplify a variance silently changes the estimand when
the nuisance variable *is* the quantity of interest. My brief's own phrasing ("the relevant
variance is Var(X̄_i|i)") carried the error, and nothing graded it because the algebra was right.

## Findings for her article beyond the theorems

- **Her 1.99 is the ceiling**, 97.5% of 1/φ̄ = 2.04. The honest headline is "no panel size buys
  more than about two," which is stronger than what she has.
- **Arithmetic inconsistency**: φ̄ = 0.49 with n_eff = 1.99 forces J ≳ 41. At J = 9 it would be
  1.83. So the 1.99 is not a nine-judge number, and I had to infer her J (100 if it's the full
  ChaosNLI annotator set, giving φ̄ = 0.4975 as a *prediction* matching her reported 49%).
- **Object substitution in the text**: the 1.2/2.0 pair is ChaosNLI alphaNLI, and
  `grep -ci 'alphanli|chaosnli'` returns **0** in both `_article.tex` and the draft — the dataset
  is never named, while the nearest antecedent for "this panel" is Kohli's nine LLM judges. 2.0
  and Kohli's 2.18 agree in *magnitude*, which is what hides it — same generator as
  `an-identical-magnitude-match-is-not-an-object-match`.
- **ESDOF and Kish have different ceilings**: 1/φ̄² vs 1/φ̄, i.e. 4.16 vs 2.04 on her panel. Both
  are printed as `n_eff` and glossed identically. Kish *is* the design-effect ratio; the
  participation ratio appears in no variance formula for anything.
- Raw-score ESDOF **equals 1 exactly when the judges are perfect** — so it's the right answer to
  her ESDOF question but for identifiability, not "for consistency."
- Both her functions return a silent `nan` on a panel with no error variance.
- **Do not cut the panel.** Her headline invites nine → two, saving 7/9 of spend, for a **35%
  increase** in error variance — while the whole J = 9 → ∞ saving was only 10% of error variance.
  The number is right and the action it suggests is backwards; that's the strongest argument for
  re-scoping rather than retracting.

## One thing I'd like you to look at

The registry root is `in-progress`, not `proved`, because `omega2-negligible-on-alphanli` is a
`speculative` premise and I can't measure it — her repo at 3fa2760 has the draft, the .tex and
the build script but **no data**. I think that's the honest grade, but it means the deliverable
she needs is "proved modulo one twenty-minute computation you must run," and I'd value a check
that I've pitched that correctly rather than hiding behind it. I planted a boundary-rule
violation and watched trustcheck refuse (exit 1, naming that exact premise) before trusting the
`OK` on the real file.

## NOT SENT — one-action debt

PROVE.md step 5 required the send and said "the send is the deliverable, not the file." **The
session rules for this phase say "No email."** The system rule governed, so the argument is
finished and the send is not. `grep -rl 'unit-of-replication' mail/sent/` → **0 hits**, reported
honestly rather than inferred. Ready-to-send body (to Lyra, CC you) is at
`mail/drafts/READY-20261001-to-lyra-unit-of-replication.md`. **Lyra is blocked on receipt, not on
authorship** — exactly the failure mode in
`a-correction-is-not-in-force-until-it-reaches-the-source-i-copy-from`, and I'm flagging it
rather than letting it sit.
