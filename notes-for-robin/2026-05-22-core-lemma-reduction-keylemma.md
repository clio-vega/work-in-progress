# Core Lemma → a clean per-walk Key Lemma (2026-05-22, prove session 2)

Hi Robin — continuation of this morning's all-stay result. I found a **clean reduction**
of the full Core Lemma lower bound to a single per-walk statement, plus several rigorous
side-results. The Core Lemma is no longer "a min over walks ≥ n(λ)"; it's now "one per-walk
inequality that bottoms out in the all-stay lemma I already proved."

## What's new and PROVEN

1. **Cost convention fix.** The matrix-order computation makes cost an *after-state*
   quantity, $\cost_k=\delta_{U_k}(i_k)$. The old `walklib.py` used the *before*-state. They
   coincide on every closed walk (Prop. below), so all prior verification stands — but the
   after-state version is the one the algebra dictates.

2. **Pairing lemma (proven).** Swapping values $i,i{+}1$ is exactly an adjacent transposition
   of the content-sequence $(\cont_U(1),\dots,\cont_U(n))$, so the inversion number $F$
   changes by $\pm1$ per swap. Since the walk is closed, $\#\text{sorting}=\#\text{de-sorting}$
   swaps. Hence
   $$\cost=\#\{\text{cost-1 stays}\}+\tfrac12\#\{\text{swaps}\}=\#\{\text{descending encounters}\}.$$

3. **The reduction (proven).** Define the *Key Lemma*: every feasible closed walk has
   $\cost\ge\min_t D(U_t)$. Then Core Lemma follows immediately, because $D(U_t)\ge n(\lambda)$
   for **every** tableau (the all-stay lemma, no feasibility needed), so
   $\min_t D(U_t)\ge n(\lambda)$.

## What's VERIFIED but not yet proven

- **Key Lemma:** $\cost\ge\min_t D(U_t)$ — DP-verified all feasible shapes $n\le7$; direct
  exhaustive enumeration $n\le6$. **Zero violations.**
- **Split at argmin:** with $W=U_{t^\ast}$ ($D$-minimal), $\cost_{\text{prefix}}\ge c_{t^\ast}(W)$
  and $\cost_{\text{suffix}}\ge R_{t^\ast}(W)$ (Claims A,B). Both exhaustive $n\le6$.

## The crux (why it's hard, sharply stated)

At one swap, $D$ can jump by up to $\pm3(n-i)$ while the step cost moves by $0/1$ — **$D$ is
not Lipschitz in cost**. A single sorting swap can drop $D$ far below the cost paid, so the
bound can only be recovered globally (the walk must *return*). This kills every naive
potential I tried (natural $n(\lambda)-R_k$; $k$-independent $c_k+\psi$; symmetric
$c_k+\tfrac12 F$; forward-prop; the running-min invariant $\Theta_k\ge\min_{t\le k}D$ —
true at the endpoint, false mid-walk). A valid integral LP potential exists per shape but is
genuinely $k$-dependent; the honest closed form is the value function of the 2-parameter DP
on (tableau, running-min-$D$).

## A clue I'd flag

Feasible closed walks are **astonishingly rare** — $(2,2,2)$ has exactly ONE; $(4,2)$ has 24.
Feasibility (never firing a comparator on a same-column pair, $d=-1$) plus closure is
extremely rigid, and that rigidity is **completely unused** in Claims A/B so far. I suspect
the proof comes from directly characterising these rare walks, not from a potential.

Paper: `~/projects/proofs/2026-05-22-core-lemma-reduction-to-minD.tex` (compiles, 3pp) and a
fuller `.md` companion. Scratch: `2026-05-22-corewalk.py`, `-minD-test.py`, `-endpoint-AB.py`,
`-theta-invariant.py`, `-split-AB.py`, `-segment-lemma.py`, `-psi-potential.py`,
`-Fpotential.py`, `-fwd-potential.py`.

Question for you: does the "rare rigid feasible walks" angle look like something with a known
combinatorial home (sorting networks that return to identity, or 0-Hecke / Coxeter sorting)?
That feels like the missing lever.
