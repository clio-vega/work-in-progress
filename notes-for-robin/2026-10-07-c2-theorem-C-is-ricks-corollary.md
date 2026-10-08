# For Robin — 2026-10-07 c2 (PROVE): Theorem C is Rick's corollary, and I found the reason Theorem B has its shape

**Artifacts:** `proofs/2026-10-07-c2-theorem-C-vs-rick-thm-2-5.tex` (13 pp, compiles clean, 0
undefined refs). `proofs/2026-10-07-two-part-green-polynomials.tex` amended in place (backup
`.bak-1007c2`). Registry `two-part-green-polynomials.json` updated, validates.

## The headline is a demotion I volunteer

**My Theorem C is a corollary of Rick's Theorem 2.5.** Not conjecturally — proved. His Thm 2.5
(= `thm:2pt`, *Two-point formula*) is a closed form for `⟨T_a g, p_x p_y⟩` for **every**
homogeneous `g ∈ Λ_a`, and `λ = ρ + 1^{ℓ(λ)}` restricts `λ` not at all, so with his dictionary it
computes the **entire** two-part-class slice for every `λ`. Theorem C is its `ℓ(λ)=2` case.

The derivation is not a substitution, which is the only reason the write-up is worth 13 pages. His
formula at `a=2` is a linear functional on the Laurent coefficients of `G_1(w) = P_ρ(1,w;t)`;
I evaluate it monomial-wise and the result **telescopes** against the potential
`α(k) = (t^{-k} + t^{k-1})/(1+t)` at every index `e ≥ 1` — and **fails to telescope at exactly one
index, `e = 0`**, where `α(1) = α(0) = 1/t` gives increment `0` while the true value is `1/t`.
That single broken step is the entire source of the integer terms `1`, `1+⟦a=b⟧`, `2` in
Theorem C. Ablating it drops agreement from 110/110 to 20/110.

**Why the demotion is not a loss.** My route (charge → two-letter Kostka–Foulkes is a monomial →
`h`-expansion of `Q'_{(a,b)}`) and his (constant-term adjoint formula → iterated residues →
`t`-strings → shuffle identity) share nothing. So the agreement is the cross-check he asked for in
his §3(a), and since the derivation is a chain of identities it runs both ways: **my independent
proof of Theorem C is a proof of his Theorem 2.5 restricted to `a=2`, `g=P_ρ`.**

## The thing I did not expect

Asking *why* the composition `c_{λ,(n)} = Y^λ_{(n)}`, `c_{λ,(u,v)} = (Y^λ_{(u,v)} − Y^λ_{(n)})/(1+⟦u=v⟧)`
closed at all gave a general statement:

> **Length-filtration duality.** `⟨p_ρ, h_ν⟩ = 0` whenever `ℓ(ν) > ℓ(ρ)` — the ordered-set-partition
> count needs `ℓ(ν)` nonempty blocks out of `ℓ(ρ)` indices. So the Gram matrix `M` of `{p_ρ}`
> against `{h_ν}` is lower block-triangular for the length filtration; it is invertible because both
> are bases under a nondegenerate form; hence **every** leading block `M^(L)` is invertible, and
> `(Y^λ_ρ)_{ℓ(ρ)≤L} = M^(L) (c_{λ,ν})_{ℓ(ν)≤L}` for every `λ`, through one integer matrix that
> mentions neither `λ` nor `t`.

**Theorem B is exactly the `L=2` rows of this.** It is not a two-part accident. `det M^(2) = 2` for
`n` even and `1` for `n` odd — the `2` being the single `1+⟦x=y⟧` diagonal entry, which exists iff
`n` is even. Verified for every `λ ⊢ n` and every `L`, `n ≤ 7`, 0 mismatches.

This is also the one result of the session that **cannot be scooped by a better closed form on
either side**, because it is a change of basis respecting a filtration, not a value formula — a
closed form *feeds* it. Opened **Q386**: at `L = 3` the duality makes "closed form for
three-part-class Green polynomials" and "closed form for `[h_ν]Q'_λ` at `ℓ(ν)=3`" the *same
problem*. That is a question for Rick as much as for me: his parameter is the number of **points**
(two), not the number of parts of `λ`, so the three-point case needs a **triple** shuffle identity
and the question is whether his `Sh_{A,B}` composes.

## `gap:rick`'s premise was false, and the failure mode is new

The gap said his statement "is in `grandpa-rick/work-in-progress` at `71b4cad`, which I do not
hold." **I held it, and had since 2026-10-06** — at `/tmp/rick-review/fpsac2027/fpsac2027-draft.tex`,
under the label `thm:2pt`. The string `2.5` does not occur near it. What resolved it was his own
`% registry: two-point-string-formula-thm25` comment line, **four lines above the environment**, in
a file I had read twice.

So: *a filename is a claim about contents* (10-06); *a scratch directory is invisible to an audit
that only scans designated corpora* (10-07 c1); and now **a theorem number is a claim about a
numbering, not about contents.** I searched for a number in a document that numbers by LaTeX label.

Everything is now copied out of `/tmp` into `peers/rick/incoming-20261007c2/` with `MD5SUMS`, plus
his proof file into `peers/rick/artifacts/proofs/` so the registry citation resolves.

## Where I was honest rather than tidy

- **I imported his theorem at `peer-claimed`, not `proved`.** I hold his proof file now; I have not
  read it. What I verified is the formula's *output*. The node
  `thmC-is-corollary-of-rick-thm25` therefore sits at `computed`, while the unconditional algebra
  (`A ≡ B` as expressions, independent of whether his theorem is true) sits at `proved` beside it.
- **The green table is 8.7× larger than its value content.** 271 ordered rows, **31 distinct
  values**. At `|λ|≤8` only **20 of 78** rows are generic. I have not written "271 checks" anywhere
  and the paper prints the generic count and the distinct-value count beside every green.
- **Branch `m>b` of Theorem C cannot occur when `a=b`** (`min(x,y) ≤ n/2 = b`), so on the square
  locus the theorem has two branches and the zero rows there are vacuous, not passing.
- **The decoupling of his theorem from his dictionary reaches only `|λ|≤6`** (32 rows). `n=7` did
  not finish. Off that range a compensating pair of errors in formula and dictionary would be
  invisible — named as a gap rather than glossed.

## One thing for you, if you have a minute

Two of my instruments misread this session in ways that would have been silent:
`grep -c` inside `$(...)` returns **empty, not `0`**, for a log with no matches, so a compile check
printed `errors: ` and read as clean; and `trustcheck.py:638` deliberately exempts shared stubs from
the evidence requirement, so the `claimed_by` paragraph I wrote is documentation **no tool reads**.
Neither is a bug in your code — the second is a design choice with a comment explaining it. But the
first is a shell trap I will hit again, and the second means cross-agent citations carry their
honesty in prose only. If you want `claimed_by` enforced on stubs too, that is a one-line change;
if you do not, it is worth a sentence in `proofs/registry/README.md` saying so, because I assumed
the opposite.
