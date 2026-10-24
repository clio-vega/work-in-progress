# For Robin — DREAM 2026-10-20

Three things from tonight, one administrative worry at the end.

## 1. G1 is closed, and the boundary-divisor programme is down to one gap

**Hypothesis `L^S` is a theorem** (PROVE 10-20 c1, `proofs/2026-10-20-hypothesis-LS.tex`, 10 pp,
`12e3b48`): all `N`, **both types**, every `m`, every **finite nonzero** `ε`, and **no genericity**
on `q` or the remaining `w`. Registry `lemma-LS-boundary-sharp-triangularity` moved
**`computed` → `proved`**. Six instruments, three genuinely independent mechanisms; the full-`q`
`N=5` census (`2622/2622`, plant `5058/5058`) never mentions `q=0` at all.

The part worth your time is **how** it closed. My own 10-19 paper §3 said in print that Rick's
degeneration *"cannot be run with `w_m` pinned at `ε`."* Rick's Lemma L **already pins two
coordinates and already excludes them from the row index** — which is verbatim my hypothesis
`m ∉ A`. I had cited that lemma **twice without opening it**. Stated generally, his `|Σ|=2` lemma,
my `L^S` at `|Σ|=1`, and sharp triangularity at `Σ=∅` are **one lemma**, so type-`B` sharp
triangularity — which I did not have — comes out on the same line.

What remains is **G3** ((BD) in type `B`), and `L^S` does **not** supply it: G3 *is* the excluded
case `m ∈ A`, where the conclusion is **false**.

## 2. The mathematical find: five type-dependences are one substitution, at one point

Five sessions each measured "type `B` differs from type `C`" in a different notation and none
compared them:

`∏(1−qw_k²) → ∏(1−qw_k)` · `2t_k → t_k` · `(v²−1) → (v−1)` · `h=2 → h=1` · `x⊕y⊕y → x⊕y`

All five are the long/short-root exchange `α ↦ 2α`. Squaring changes the solution set of
`coordinate = 1` by **exactly one point**, so every type-dependence should be supported at
**`v = −1`** — and that is what each session had already measured without saying so:
`tauFiring_typeB_ssubset_typeC` is strict by the single element `−1`; type-`B` head exclusion
**fails at `−1`**; `{w_m = −1}` is not a root hyperplane of `B_N`; and the char-2 collapse theorem
says the types merge precisely when `−1 = 1`. The `h mod 2` behaviour then follows: **a parity is
what survives a squaring.**

**Status: conjecture-shaped**, falsifier written down, cheapest arm costs a script because the
machinery is mine on both sides. `questions/2026-10-20-dream-ledger.md` **Q534**. If it holds, G3
becomes localised rather than general, and `ψ`'s type-C-specificity gets a *mechanism* instead of a
stipulation.

## 3. A gap on the seed path that has been open fifteen years, and sits on one slide

I have to retract something first: I told you (10-18) that the type-C `β`-deformed
excited-diagram weight was unwritten. **It is in print** — Kirillov–Naruse `arXiv:1504.08089`
(*Tokyo J. Math.* **39**(3), 2017) **Theorem 5**, types B and C, full border factor, Yang–Baxter
relations invoked by name. I inferred "unwritten" from a dead pointer and built on the inference.
*(That reading is currently **agent-summary** provenance; I have not opened Theorem 5 myself, and
discharging that is the first item tomorrow.)*

What is genuinely absent is narrower and much more interesting: **the coproduct rule.** Zero in
`1504.08089`, zero in Ikeda's 2026 paper (where the K-theoretic-LR bibitem is **deliberately
commented out**), zero across arXiv abstracts for types B/C/D, and absent from Naruse's entire
33-work OpenAlex record 1985–2026. It exists written out in full on **logical slide 9 of 10** of his
MSJ Autumn Meeting talk, 2011-09-28. I read it first-hand as a rendered image — the text layer is
Type 3 bitmap glyphs that destroy every formula:

> `Δ(GQ_{λ/μ}(x)) = Σ_{ν/ν' rook, λ ⊃ ν ⊃ ν' ⊃ μ} β^{|ν/ν'|} GQ_{λ/ν'}(x) ⊗ GQ_{ν/μ}(x)`

**At `β = 0` this is `Δ(s_λ) = Σ c^λ_{μν} s_μ ⊗ s_ν` with the shifted LR coefficients.** That is
the Fock Space Path of `SEED.md`, in type C, K-theoretically deformed — and `arXiv:1112.5223`
(which I hold at `verified-quote`, full LaTeX source) names exactly those structure constants as
its own open problem: *"As for the equivariant case … we do not even have a conjecture."*

**And the obstruction has a mechanism, which is the part I did not expect.** `ℬ(D)` is **not** a
border — it is an **unbounded-range diagonal ray**, so the `(1+βw)` factors **cannot be per-vertex
weights**. That refutes my own 10-19 proposal and refutes it in the useful direction: a transfer
matrix is a product of local weights, and a diagonal ray of unbounded range is not one. ***The
reason nobody has written the integrable proof may be that the naive integrable formulation cannot
hold the correction term.*** Independent corroboration from an unexpected place: Panova–Petrov
`arXiv:2409.17842` attempted the K-theoretic case **in commented-out LaTeX source** and stalled at
*"adding border strips… weird."* They hit the wall and deleted the evidence.

So the research target is not "apply Zinn-Justin 2008 to `1112.5223`." It is: **find the
non-local-to-local trade** — a lattice in which a diagonal ray becomes a boundary condition, an
extra spectral line, or a transfer matrix in a second direction. `questions/…ledger.md` **Q533**.

## 4. My dominant fault class now has a name, and it is not the one I expected

Six sessions, **five findings, all location errors, none truth errors.** Wrong declaration, wrong
family, wrong document, wrong quantifier index, wrong channel. Every instrument I own grades
**truth**; none grades **siting**, because each takes the siting as given in order to run.
`9558/9558` was right. `336/336` was right. `36` declarations was right.

And four of the six landed **in my own favour or against myself in a way nobody would contest** —
"his method cannot do this" closes *my* door, a false `NOT IN INDEX` is about *my own* reading
state, two under-claims in a covering email against my own tex. ***A claim that only narrows my own
options recruits no objector.*** So the detector cannot be a reviewer; it has to be structural. The
one that keeps working: **make the citation machine-resolvable and see whether it does.**
`trustcheck`'s refusal of a shared stub is what sent me to Lemma L's text, and that read closed G1.
→ `connections/2026-10-20-dream-a-hypothesis-has-an-address.md`

## 5. Two things I am flagging rather than diagnosing

- **RTV stable-envelope uniqueness is unread by both Rick and me**, and it now sits under **three**
  results — his `D∞`, his Theorem W determinant lemma, my `lem:inverse` — **two of them graded
  `proved`**. It is unranked not because it is unimportant but because neither of us owns it. That
  is a shared single point of failure in two people's `proved` grades and I would rather you knew
  than that I quietly carried it.
- ⚠ **No agent-health mail since 10-17 17:17**, with ~47 h of silence from Rick as of this
  morning. Health mail is problem-triggered, so its absence is **equally consistent** with *all
  clear* and with *the health check stopped running*, and the two absences cannot distinguish each
  other. That detector's recall is **7/18**. **Not escalated, not diagnosed** — recorded as an
  ambiguity I cannot resolve from inside the container, in case you can from outside.

⚠ This note is **local only** — `memory/for-robin/` is not a git repo, so you cannot see it until
it goes out by mail or gets written into a pushed repo. The mathematics above is pushed:
`proofs/2026-10-20-hypothesis-LS.tex` at `12e3b48`, and the Lean at
`https://github.com/clio-vega/tworow-d4-kernel/blob/main/TworowD4Kernel/MotegiOrderTailCount.lean`.
