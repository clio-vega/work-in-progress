# The one thing today's two results only say together

**2026-09-25, DREAM c1.** PROVE and LEAN each sent you a note. This is the part neither could see
alone. No action needed — but item 3 is a change to how I spend the LEAN slot, and you may disagree.

## 1. Q254's answer is bigger than Q254

I closed Q254 this morning (`thm:main` is **not** a corollary of FMS `1706.04935` Thm 7). Tonight I
read a MathOverflow answer (MO 512139) proving `Supp(κ_α) = Σ_c W(R_c(α))` — a Minkowski sum with
**one summand per column** — which is structurally identical to FMS Thm 7's
`Newton(χ_D) = Σ_j P(SM_n(D_j))`. Different people, different setting, no cross-citation.

So the column-Minkowski decomposition is **the standard route** to a support theorem in this area,
and today's rigidity theorem says exactly why it cannot reach a skew shape: `supp(χ_D)` is a
**sumset over columns** — columns independent, tied to the shape only by a *column-local* flag —
whereas a semistandard tableau **couples adjacent columns**. The flag is trivial precisely when the
column is bottom-justified, which is precisely the symmetry-rigidity condition. Chain those and
FMS Thm 7 restricted to symmetric functions collapses to **Rado 1952**.

That converts a verdict about one paper into a test to run on the next: *does its decomposition
couple adjacent columns?* If not, it cannot reach me, however general its diagram class.

**Open and possibly larger than my theorem:** has the coupled case been attacked *at all*? If not,
the adjacent-column coupling is open for ordinary skew shapes too. That is **Q260**.

## 2. The Schur door is shut on both sides, and it improves the paper's introduction

McNamara shut the ordinary side by theorem. Today I shut the cylindric side by computation: 13
winding instances carry a negative Schur coefficient, smallest `n=3, m=1, λ=(3), ℓ=3`,
`s^c = s_{21} − s_{111}` (same phenomenon as WZZ Ex 4.2). So the cheap route —
Schur-positive ⇒ union of Schur supports ⇒ SNP by Rado — is unavailable.

**This makes `thm:main` harder, not easier, and I think it belongs in §1.** There are exactly two
handles on a cylindric support theorem and both are polytopal: **volume** (Alexandersson–Oğuz
`2311.07382`, via Ehrhart) and **exchange** (mine, the bead hop). AKO took one; this paper takes
the other. That is a better opening than any list of results.

## 3. I am changing what I point Lean at, and here is the reason

`linarith` refused a step in `prop:perm-mconvex` today: the paper displayed `≥` and justified it
with "every term with `j ∈ S*∖D` is `≤ 0`" — **which gives `≤`**. The theorem survives (count on
the complement instead; only ingredients the proof already had), and the `.tex` is corrected with
an erratum remark.

The part worth your attention: **the conclusion was true, so nothing else I own could have caught
it.** Not the 876,317-triple brute force, not the 164-pair differential check, not the compile.
Every instrument I have grades an *assertion* — a claim, a citation, a node status, an output. A
*because*-clause is not an assertion. Lean caught it only because formalisation has no syntactic
category for "because": every reason must become a proposition or the tactic fails.

So going forward I will point Lean at **steps that carry a justification in prose**, not at
theorems I am confident in. The tell in my own `.tex` is a displayed chain of inequalities with
words between the links. If you think the certificate value of formalising whole theorems outweighs
this, say so — I would rather hear it now than after a month of small lemmas.

## 4. Two things I owe, recorded so they are reachable

- **The trustcheck extraction gate is vacuous across all ten registries.** It binds only on a
  *bare* arXiv id; the id+locator form my own protocol prescribes fails to resolve and degrades to
  a soft warning. Every existing node carries locator-suffixed ids only. Owed: a bare id beside
  every locator. **Not done today.**
- **62 `sources.json` entries have a completely blank note** (I filled 4). A blank note is
  invisible to a detector that fires on confessions — it does not say "not read", it says nothing.
  One of the four I filled, Gorbounov–Korff `1402.2907`, **overturned a conclusion I published in
  yesterday's dream**. This needs an inventory pass, not a cleverer detector.
