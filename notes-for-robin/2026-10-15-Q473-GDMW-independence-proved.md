# Q473 — the GDMW linear-independence lemma is proved

**2026-10-15, PROVE session. Outcome O1.**

Pushed: https://github.com/clio-vega/proofs/blob/main/2026-10-15-Q473-GDMW-independence.tex
(PDF beside it, 354,369 B; code and evidence in `code-1015-q473/`; registry node
`registry/halfspace-sixvertex-orthogonality.json`, validates `proved`.)

## What it is

Garbali, de Gier, Mead and Wheeler (`arXiv:2312.14348`, Wheeler is one of my seed authors)
reduce their orthogonality conjecture `conj:F-orth` to exactly one unproved statement and say
so: *"it remains conjectural as we have not established that the functions
`lim_{c→∞} G_κ(x_1,…,x_L)` are linearly independent."* I proved that statement.

The mechanism is small enough to state in three lines. `G_κ` is built out of one-variable
functions
`φ_m(x) = (1−q)x y_m/(1−q x y_m) · ∏_{j<m}(1−x y_j)/(1−q x y_j)`,
and `φ_m(1/y_{m'}) = 0` **iff** `m > m'` — the zero locus is *nested*. So evaluating at
`x_i = 1/y_{κ_i}` annihilates `G_{κ'}` unless `κ' ⪯ κ`, and the diagonal survives as a single
term (`K=[d]`, `σ=id`) which I compute in closed form and which is manifestly nonzero.
Triangular with nonzero diagonal ⇒ independent.

## The part I'm actually pleased by

`⪯` has **finite principal down-sets**. So the same functional turns the *infinite* relation
into a *finite* one in one stroke — and the infinite version is what the authors' coefficient
stripping actually uses. I only noticed this after I'd already proved the finite statement by a
*different* functional (iterated residues at the **poles** `x_i = 1/(q y_{κ_i})`, triangular for
the **opposite** order `⪰`). The pole route cannot reach the infinite statement, because `⪰` has
infinite ascending chains while `⪯` is well-founded. Two functionals, one from the zeros and one
from the poles of the same `φ_m`, and the asymmetry between them is not cosmetic — it is exactly
which theorem each one can prove.

## What I want you to decide

**The authors have claimed this problem**: *"we plan to return to its proof in a later text."*
I've said so in §1.2 of the writeup and claimed nothing about priority. Whether to make contact
is yours (PROTOCOL §1, §5). I have not emailed anyone.

## The one thing that is not closed

Deducing `conj:F-orth` needs the infinite form, and that needs **Hypothesis H**: that the
convergent `κ`-sum may be specialised termwise at the configuration
`(1/y_{κ_1},…,1/y_{κ_d},1,…,1)`. It is an *interchange* assumption, not a disguised
independence assumption, and the independence theorem does not need it. I did **not** do the
estimate that would place that configuration inside their convergence domain, and I do not
claim it. Two things make it look reachable: their regime *requires* the points `y_k^{-1}` to be
"arbitrarily close to the points `x_i`" — which is exactly my evaluation point — and they note
their contours "allow us to choose elements of our alphabet, `x_i`, to be arbitrarily close to
1". If you want one more thing from me on this, that estimate is the thing.

## Two corrections worth your time

1. **The brief's primary strategy was wrong, and the mandatory census caught it before any
   code.** The brief proposed separating the `G_κ` by residues in the `y`-alphabet. But the
   coefficients `A_{ν,κ}` being stripped are *themselves* `y`-dependent, so `y`-residues are not
   linear over the field. The `y`-support fact the brief leaned on is **true** and **useless**.
   Three hours would have gone into it. The §1 census requirement is paying for itself — that is
   now twice in two days that counting which symbols the *other* object carries has been the
   whole game.

2. **A control I ran first looked informative and read nothing.** Symmetry of `G_κ` in the `x_i`
   is not manifest in the subset formula, so I used it as a check — and the planted sign error
   passed it too, because `Σ_{σ∈S_d}` is symmetric *whatever* its summand. Vacuous by
   construction. I only found that out because I ran the plant. It's in the writeup as a control
   that read nothing, next to the one that did (subset formula vs the paper's independently
   derived contour-integral formula: 7 cases exact, and the plant breaks all five with
   `|κ| ≥ 2`).

## Plumbing (report, not patch — these files are read-only to me)

- `--files-dir registry` in the PROVE template **double-prefixes** and produces spurious
  "file not found" on every node; `--files-dir /home/clio/projects` is clean. 12th instance.
- `/home/clio/projects` is **not** a git repository, so §7's `git` instructions can't be run
  from there; `/home/clio/projects/proofs` is the repo. Worth fixing in the template.
