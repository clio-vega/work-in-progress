# The Ehrhart route never existed — so §1 of the M-convexity paper can claim inevitability

**2026-09-30, DREAM.** Short note, one mathematical point and one you may care about for the paper's
framing.

## 1. The volume/Ehrhart handle is provably absent

I had been carrying two possible routes to `thm:main`, both polytopal: **volume** (via Ehrhart, using
Alexandersson–Oğuz `2311.07382`) and **exchange** (the bead hop, mine).

Reading Brändén–Huh `1902.03719` at source, by internal `\label` and line number rather than
build-dependent numbering:

- `\label{RealizationQuestion}` (l.3658) **asks** whether Lorentzian polynomials are limits of volume
  polynomials.
- The added-in-proof footnote (l.3681) **answers it negatively.**

So there is no characterisation to lean on. The volume route was never a route.

**What this buys the paper:** §1 can say something stronger than "we prove X". It can say *there were
two candidate routes, one is provably shut, and this paper takes the other.* I think that is worth a
paragraph — it converts a technical choice into a structural claim.

Also settled at source while I was there, in case it saves you a lookup:
**products closed** (`\label{CorollaryProduct}` l.1758); **nonnegative linear substitution**
(`\label{flow}` l.785, no positivity/invertibility/squareness required); **derivatives**
(`\label{derivatives}` l.828). **Addition: the paper says nothing about it anywhere, and it is
false** — `(x+y)² + (2x+y)²` has a rank-2 PSD Hessian. That last is the reason the Schur route stays
dead even inside Postnikov's positive range.

One hygiene point: their Def A (analytic, l.433) and Def B (M-convex support, l.637) are proved
equivalent at l.1623, and "the support of a Lorentzian polynomial is M-convex" is a *theorem* under A
and a *tautology* under B. Worth naming the definition in force wherever we cite it.

## 2. Condition (A) is not a lemma — at ℓ=3 it is the conjecture

`\label{normalizedcoefficients}` (l.2853): `log c_α` M-concave ⟹ Lorentzian, and it has a **local**
form requiring only `|α−β|₁ = 4`. That local form is usable for us precisely because (L2) is already
proved.

**At ℓ=3, the case `α−β = (2,−2,0)` is exactly condition (A).**

Which reframes the last three sessions: the work on (A) was the main line, not preparation for it.
And it fits the 09-29 reduction — at ℓ=3 the Hessian is 3×3 nonnegative symmetric, so "at most one
positive eigenvalue" is `e₂ ≤ 0` (exactly the sum of the three raw RLC quantities) **and** `det ≥ 0`,
so the whole open content is a determinant sign, which is what (A) governs.

I have **not** promoted the registry node (`m-concavity-via-normalizedcoefficients` is
`unclassified`), because this rests on a reading and not yet on Murota at source.

## 3. Where (A) actually stands, honestly

Reformulated for **every** `m`: `k(a,b) = Σ_{ν ∈ Box(μ), S_ν = |μ|+b} f_ν(a)` with
`Box(μ) = ∏_i [μ_i, μ_{i+1}−1]`, each `f_ν` an ℓ=2 cylindric Kostka sequence and hence PF₂ by the
proved `ell2-all-m`. So **(A) says: a sum of PF₂ sequences over one slice of a box is log-concave.**

At `m=2` I have it on **79.9%** of slices (the single-region case, criterion proved and verified
5187/5187). The remaining gap is **one inequality**:

```
2 G_R(s) G_R'(s) ≥ G_R(s−1) G_R'(s+1) + G_R(s+1) G_R'(s−1)      between distinct regions R ≠ R'
```

525/525 verified, **unproved**. Given it, symmetrisation closes (A) at m=2 outright.

The useful constraint on any proof: **it cannot be slice-local.** The same inequality already fails
between individual slice members (`n=6, μ=(0,3), λ=(4,5), ν=(0,5)` vs `(2,3)`). Term-by-term fails,
region-by-region holds — the grouping *is* the content, and the missing step is a cancellation across
an antichain rather than a pointwise comparison. (Ahlswede–Daykin does not apply: `(S_κ, S_σ)` is
modular on the interlacing sublattice but not a lattice homomorphism.)

## 4. One thing I nearly got wrong, recorded because you may find it useful

I almost wrote down that `k(·,b)` is **concave**. It held **905/905** on the sweep that suggested it.
It is **false** one range further out — 1758 failures in 96781 interior points, smallest witness
`(1,3,6,7,6,3,1)`. Log-concavity failed 0/96781.

The silver lining is that the refutation *located* the gap: regions II and IV are proved **by** a
concavity argument, so that argument provably cannot reach the multi-region case. A killed
strengthening turned out to be a scope statement for the proof that survived it.

## 5. Small owed edit

The Lean formalisation showed the paper's "affine in each variable hence minimised at a vertex of
`[0,1]³`" step is **unnecessary** — there is an explicit certificate,
`xyz + 2t³ − t²(x+y+z) = x(t−y)(t−z) + t(t−x)(t−y) + t(t−x)(t−z)`, a `ring` identity whose three
summands are products of nonnegatives under `0 ≤ x,y,z ≤ t`, and it covers `t=0` and `t>0` uniformly.
I have not yet pushed that into `2026-09-29-c1-cylindric-lorentzian-ell3.tex`. It shortens the proof
and removes a general lemma we do not need.

---

## 6. Two tooling things, one of which is in a file you own

**(a) `DREAM.md`'s protocol line is wrong about what the check does.** It says to run

```
python3 code/trustcheck.py --deployment code/clio.json --root memory --sources ... sources
```

*"to catch any arXiv IDs orphaned by compression."* It does not do that. `grep arxiv trustcheck.py`
returns nothing — the tool has no notion of an arXiv ID. `validate_sources` checks the **index's own
schema**: `format`, the `title`/`extraction`/`read` fields, that `extraction` is in the allowed
chain, that `read:` files exist, that `corrections` carry `date` and `note`. It never scans
`--root memory` prose for citations; `--root` is used only to resolve `read:` paths.

I caught it by deleting a key I cite heavily (`2609.18502`) from a temp copy of the index and
re-running. It still printed `sources index OK` and exited 0.

This matters because my 09-25 dream journal recorded *"Zero orphaned arXiv IDs, which is what this
sweep exists to catch"* — a conclusion the command could not support, on the night I compressed
notes. Tonight I moved 1875 lines out of `SUMMARY.md`, so it would have been the night it bit.

Either the protocol line should stop claiming the sweep is an orphan check, or the tool should grow
one (scan `--root` for `\d{4}\.\d{4,5}|math/\d{7}` and resolve against index keys **plus** each
entry's `arxiv` field — the second half matters, several of my entries are label-keyed). Happy to do
whichever you prefer; I didn't want to change a protocol file unilaterally.

**(b) A seed paper is invisible to my own index.** Running the orphan check by hand found that
**Purbhoo `0705.1184`, *Puzzles, Tableaux and Mosaics*** — one of the eight seed papers — does not
resolve in `sources.json`, neither as a key nor as any entry's `arxiv` field. Tonight I wrote a
connection specifically about that paper's citation isolation. I'll fix it at the next wake; noting
it here because it is the sort of gap that stays invisible precisely because the paper feels
familiar.

Good news from the same check: **tonight's compression destroyed no citation.** The archived
material moved to `SUMMARY-archive-2026-09-16-to-09-24.md`, still under `memory/`, nothing deleted.
