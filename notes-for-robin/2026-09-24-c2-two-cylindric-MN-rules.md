# For Robin — 2026-09-24 (PROVE c2): Q253 is closed, and it turned up two errata

**⚠ SEND OWED: this proof is a LOCAL file. You cannot read it until I push
`proofs/2026-09-24-cylindric-MN-two-rules.tex` to GitHub. That is an unspent action, not a
finished one** — recording it here so the next session sees a *verb*, not a file.

## The question

Alexandersson–Kantarcı Oğuz (`2311.07382`, src l.232) write of their own main theorem: *"A similar
formula **seems to appear** in [Korff–Palazzo, Eq. (145)]."* A hedge in print, owned by nobody.
Both papers are on the volume. I settled it.

## The answer: no, they are different theorems

AKO expand `s_D` over stacked-ribbon data **on `D`**. KP expand `s_D` over cylindric-ribbon data **on
the conjugate `D'`**. Classically those are the same statement, because `ω(s_{λ/μ}) = s_{λ'/μ'}`.
**Cylindrically `ω(s_D) ≠ s_{D'}`** — and the smallest cylindric shape there is already shows it: on
`C_{1,1}` the two-box diagram is *self-conjugate*, `s_D = e₂`, and `ω(e₂) = h₂`. (67 of 357 shapes fail.)

The two rules sum over the **same** sets of ribbons with the **same** signs, and differ on **fully
wound steps only**, by `−k/(n−k)`. That ratio is level-rank duality: the multiplicity on a wound
ribbon is the width of the cylinder on which the *Schur function* lives — `n−k` for AKO, `k` for KP.

## The instrument, which is the part I'd most like you to poke at

Any MN-type rule for cylindric Schur functions has a **unique** weight function,
`w(R) = ⟨s_R, p_{|R|}⟩`: apply the rule to `D = R` with `ν = (|R|)`, where the only chain is the single
step. So the whole comparison collapses to *one number per region*, computable from the CSSYT
definition alone — an arbiter independent of both papers. It calibrated on AKO's own worked example:
I reproduced their printed power-sum expansion exactly.

## Two errata, each confined to the winding case

**(A) AKO, src l.1182–1187.** They define the height of a stacked ribbon **twice** and assert the two
agree. They differ by `ℓ`: an extended ribbon is a *path*, so it must cross one vertical edge at each
of the `ℓ` junctions. Their closed form `ht = ℓy + ht(F)` therefore has the **wrong sign when `ℓ` is
odd**; correct is `ℓ(y+1) + ht(F)`. **Their own example annotates the ribbon "height 3" — the correct
value — while their formula gives 2.** The example is right; the prose is not. Verified 0/797 regions
and 0/874 multi-part pairs (as-stated: 174/797), and *proved*, since it is equivalent to Korff
`1906.02565` `lem:cylMNrule`(i).

**(B) Korff–Palazzo.** Their `χ`, as literally defined, is short by a factor `k` per fully wound
ribbon. Minimal counterexample: a **single circular ribbon** (`n=4, k=2, λ̄=μ̄=(0,0), d=1`, `ν=(4)`):
definition gives `−1`, their equation needs `−2`. The multiplicity is present in their *proof*
(*"`P*_r` adds **all possible** ribbons"*) and their `lem:CR` asserts a unique starting diagonal only
when `r ∉ nℕ` — **the case it excludes is exactly the one that carries the degeneracy.** A ribbon
plane partition records shapes, not shapes-with-a-marked-starting-diagonal, so the count is lost in
passing from the matrix element to `χ`. Verified (0/16791 with the factor; 439 without), **not proved**.

## What is mine, and what isn't

The corrected AKO rule **is** Korff `1906.02565` `lem:cylMNrule` in the `t→1` limit — 2019, predating
AKO, and not cited by them there. **Neither rule is new here.** Mine is the comparison, the
dictionary (with a `d=0` calibration that passes 0/3731), the reduction above, and the two errata.
AKO's real contribution — a combinatorial proof and a closed non-recursive form — is untouched.

## The old debt, half paid

The 5-day-old "reconcile my `(−1)^{k−1}(n−k)` with Korff's `(−1)^k(n−k)`": **his sign is the correct
one**, measured against ground truth. His `cor:cylchi2cylschur` puts his ribbons and his Schur
function on the *same* cylinder, so his conjugation was never the obstruction. **Still open:** whether
my constant is a real disagreement or an artefact of my own `R_e(−1)` normalisation — I did not
re-check that computation, so I am not yet entitled to say we agree.

## Honest limits

Theorem (the weight function) and the KP correction are **verified in range, not proved from first
principles**; Erratum A alone is proved, via Korff. "Eq. (145)" is identified with `\eqref{cylSchur}`
by counting environments in the **e-print**, while AKO cite the **journal** rendering — strong
evidence, not proof, so I cite by label throughout. And the geometric reading of Erratum A (the
extended ribbon) is an *explanation*: in 37 of 127 cases the junction carries two vertical
adjacencies, of which a path uses one — consistent with the count, not a proof of it.
