# Q424 / Q418 / Rick's D3 — the scope of the Korff refutation is settled

**Session:** PROVE 2026-10-11 c2
**Artifact:** `proofs/2026-10-11-c2-Q424-scope-and-domain.tex` (9 pp, compiles, commit `81e8a49` on p.1)
**Registry:** `proofs/registry/cylindric-statistic.json`, 30 → 34 nodes, trustcheck exit 0

Robin — three questions, all answered, and the order matters because the second one nearly
got the wrong answer for the right reason.

## 1. Rick's defect D3 is discharged

His referee report (UID 796) found that my Q410 witness family sat outside *both* of Korff's
standing restrictions (`n_K > 2`, and `n ≤ w` or his Def 5.5 sets `P ≡ 0`). He supplied a
replacement witness: `n = 2`, `α = (1,1)`.

It holds, and the `ℓ ≥ 1` half needs no computer. From the basepoint only `e_1` is a legal
step; from `e_1` only `e_1` and `e_2`. So the fibre is **exactly two** tableaux, both with
`ν(T) = 2`, and the HKKO signs are `+1` and `−[ℓ=0]`. For `ℓ ≥ 1` that gives
`c_α(1) = 1 ≠ 0`, hence `ord_{t=1} c_α = 0 < 2`, and the obstruction fires — at `k ≥ 2`,
*inside* Korff's domain. Half a page.

I verified it with **two engines sharing no code path** (his scripts deliberately not
fetched, so the two readings are two mechanisms rather than two handles on one): the Warnaar
determinant engine and the HKKO signed path count agree at `t = 1` in 16/16 pairs, and
`c_{(1,1)} ∈ {1−t, 1}` in 16/16 — his reported set, reached disjointly.

The control I like best: wherever `min ν = 0`, **Korff's identity holds exactly**. The
obstruction is located, not blanket.

I promoted his node to `proved` and **deliberately did not promote the parent** in the same
breath. The parent asserts a general statement about all cyclically ψ-graded weights; what
is now domain-legally witnessed is its corollary at `α = (1,1)`.

## 2. Q424 closes NO — but I would have got there dishonestly

Korff's Def 5.5 weight contains only `t`. If I had stopped at equation (5.13) I would have
written "no second parameter" and been right by accident.

There **is** a second free parameter grading the wrap. Three pages earlier Korff writes: *"We
introduce a formal variable `z` keeping track of the winding number around the cylinder"*,
and his Lemma 5.5 is `e_r|μ⟩ = Σ z^d Φ_{λ/d/μ}(t)|λ⟩`. The wrap degree `d` is graded, by `z`,
and `z` is free. What saves the refutation is his own parenthesis in the proof of Lemma 5.1:
*"the weights of the lattice configurations do not depend on `z`."* It is a monomial
**prefactor**, and a two-line proposition kills every prefactor regular at `t = 1` — evaluate
at `t = 1`, where the weight is already zero. That covers Korff–Vasilev's `z = ±q = ±√t`.

Also: Korff's `q` is **not** Macdonald's. §2.1 says *"we will often use `t = q²` instead of
`q`"*, so his lattice/Hecke `q` is `√t`. Macdonald's `q` is the one set to `0`, and that
substitution is what *creates* the Hall–Littlewood weight I refuted, not a collapse of a term
doing work.

The honest sentence is not *"there is no second parameter"*. It is *"there is one, it is named
and free, and it is a prefactor."*

## 3. Q418: the escape route survived its kill, then died of the opposite fault

The pre-registered kill was: if `1906.02565`'s weight is another `∏(1−t^m)` over a cyclic
index set, it dies in twenty minutes by Q410. **It did not fire.** The weight is
`(t−1)^{#b−1} ∏_{h∈b} (−1)^{r(h)−1} t^{c(h)−1}` — a *connectivity* factor, not a fold
product. A single box is one connected move, so `wt = 1` identically, and the weight therefore
**passes** the `W_T(1) = 1` screen that had exhausted Korff's five-member index-set family in
one evaluation. The capacity argument the brief gave was correct.

Then it dies of something the brief did not predict. `wt` is **`t`-free** on single boxes, so
on the fibre `α = (1^n)` every `W_T = 1` and `Σ_T c^-(T) W_T` carries no `t` at all. And
`c_{(1⁴)}(t) = 3 − t²` at `k = 2, ℓ = 1` — a point inside Korff's domain. The `q^d` twist of
the 2019 paper cannot rescue it either: `Σ c^- q^d = −q⁴ + 2q² + q`, no constant `q` works,
and `q⁴ − 2q² − q + 3 − t²` is irreducible over `ℚ(t)`.

So: a candidate that passes the screen is not thereby alive. I have recorded the screen as
necessary, not sufficient.

## 4. What I think the real payoff is

The two failures bracket the answer from opposite sides of one invariant. On that fibre the
target `3 − t²` needs `ord_{t=1} = 0` **and** `deg_t = 2`:

| weight | single-box value | signed sum | fault |
|---|---|---|---|
| required | — | `3 − t²` | — |
| Korff 2011 `Ψ` | `(1 − t^{m_i})`, zero at `t=1` | `(t−1)⁴(t+1)(t²+1)(t²+t+2)` | `ord = 4`, **too high** |
| Korff 2019 `wt` | `1`, `t`-free | `2` | `ord = 0`, `deg = 0`, **too low** |

So the single-box weight must be non-vanishing at `t = 1` **and** not `t`-free. The Gaussian
binomial `(1 − t^{m+1})/(1 − t) = 1 + t + … + t^m` satisfies both, and the move from
`(1 − t^m)` to it is exactly the division by `(1 − t)` that turns a *fold* factor into a
*counting* factor. That is precisely what both of Korff's weights miss, in opposite
directions. The Q410 paper's closing Kostka–Foulkes guess is now the unique surviving type
among those examined, **by two independent exclusions rather than one**.

Next session's arithmetic, and it is small: does a Gaussian-binomial single-box weight
actually produce `3 − t²` on that fibre? 10 tableaux, 4 with `c^- ≠ 0`. Linear algebra.

## 5. The thing that is about me, not about Korff

My node `korff-own-range-excludes-the-target` records **both** of Rick's D3 restrictions, by
name, and grades itself *"RECORDED, NOT USED."*

So he did not find something I had missed. He found something I had written down and declined
to let bind. Not a coverage failure — the measurement was taken. Not a consultation failure —
the record was read; the node exists because I read the paper. A **decision** failure. My
stated ground was *"answering a mathematical question by a convention is not an answer"*, and
that ground was not wrong; what was wrong was treating it as a reason not to *also* prove the
in-domain statement, which turned out to cost two lattice paths and half a page.

The repair does not belong in the record, which was already correct. It belongs in the reading
rule: **a node graded "not used" must be re-read whenever the claim above it is pushed, cited,
or refereed.** A "not used" grade is an unexercised decision, and that is the one place where
a correct record and a false paper can coexist.

## 6. One instrument fault worth your attention

The trajectory emitter recorded the **opposite** of the evidence. My strongest verification —
two disjoint mechanisms agreeing 16/16, three controls each a number — was emitted as a
`verify` event **without** a `verification_target`. That is schema-invalid, so it was dropped;
and the claim it supports lists it as an input, so that claim now reads `tau=unsupported`.

I then appended four correctly-formed `verify` events and **nothing moved**. `tau` is a
function of a claim's own `inputs` chain at emission time, not of the `verify` events pointing
at it. An append-only log cannot be repaired in place.

So the best-evidenced claim of the session is the one the trajectory grades lowest, and the
cause is entirely mine. Two narrow rules follow: a `verify` must carry its target on the
**first** emission, and a claim must list its verifier as an **`input`**, not merely be its
`verification_target`. If you want the emitter to be forgiving here, the fix would be for
`tracecheck` to treat an inbound `verification_target` edge as support — but I'd rather you
know the current semantics than that I quietly patch around them.

## Gaps I am naming rather than papering over

- Theorem A at `ℓ = 0` rests on computation (`c_α = 1−t`, order 1), not on hand proof.
- The Task C refutation kills the ribbon **weight** transported onto HKKO cylindric tableaux
  via its single-box value. It does **not** refute Korff's 2019 construction as a whole, which
  computes cylindric Hecke characters over a different tableau set. What is proved is: no
  weight with a `t`-free single-box value answers Warnaar's question, and his does.
- The identification `d_a = θ_1` rests on one line of Korff's proof of Thm 5.6. The theorem
  does not depend on it; only the explicit `−q⁴+2q²+q` does.

— Clio
