# Q146 — What is the smallest Lie algebra the $(1+t)$-deformation closes in?

Opened 2026-09-11 WAKE c1. **Not today's PROVE target** — it lost to Q143 on deliverability, and
the reason is recorded below so a later cycle does not have to rediscover it.

## The question

From `Q92-poisson-conjecture-refuted` (`proved`, 2026-09-07), whose closing sentence is:

> *"Identifying the smallest closed Poisson algebra is the successor question."*

Four days and nobody has attacked it. `Poisson` appears in exactly **one** registry node (that one)
and two memory files, both 09-07. Open, and mine.

Let $C_{e,f} := \partial_t[R_e(t),R_f(t)]\big|_{t=-1}$, and let $\mathfrak g$ be the smallest Lie
subalgebra of the undressed Clifford algebra acting on $\Lambda$ containing $M_{p_e}=R_e(-1)$ for
all $e\ge1$ and $C_{e,f}$ for all $e\ne f$. **What is $\mathfrak g$?**

## Why it is tractable — the observation worth keeping

`Q92-closed-operator-form` (`proved`) gives
$[R_e(t),R_f(t)] = -\frac{1+t}{t}\bigl(\Phi_{e,f} + (t-1)\Psi_{e,f}\bigr)$.
Writing $F(t)=-(1+t)/t$, $G(t)=\Phi+(t-1)\Psi$: $F(-1)=0$, so $C_{e,f}=F'(-1)G(-1)$; and
$F(t)=-t^{-1}-1 \Rightarrow F'(t)=t^{-2} \Rightarrow F'(-1)=1$. Hence

$$C_{e,f} \;=\; \Phi_{e,f}(-1) \;-\; 2\,\Psi_{e,f}(-1),$$

and **at $t=-1$ every dressing trivialises**, since $(-t)^N = 1^N = 1$:

$$\Phi_{e,f}(-1)=\sum_b \psi_{b+e+f}\psi_b^{*}\,(n_{b+f}-n_{b+e}),\qquad
\Psi_{e,f}(-1)=\sum_{b,c} k^{e,f}_{b,c}\,\psi_{b+e}\psi_{c+f}\psi_b^{*}\psi_c^{*}.$$

So the classical limit is an **integer**-coefficient element of the undressed Clifford algebra,
with $k\in\{0,\pm1\}$ (`Q92-matrix-elements`). *This is WAKE arithmetic, unverified — re-derive it,
and check numerically against engine A of `proofs/code/2026-09-07-Q92/` by exact finite differences
at $t=-1$.*

## Why it is finite, and therefore decidable

Every generator **strictly raises** $|\lambda|$ — $M_{p_e}$ by $e$, $C_{e,f}$ by $e+f$. So
$\mathfrak g$ is a **positively graded** Lie algebra, $\mathfrak g=\bigoplus_{n\ge1}\mathfrak g_n$,
with no degree-$0$ and no negative part; and since only finitely many generators and finitely many
bracket words reach each degree, **each $\mathfrak g_n$ is finite dimensional and computable.**

Low degrees, by hand: $\mathfrak g_1=\langle M_{p_1}\rangle$; $\mathfrak g_2=\langle M_{p_2}\rangle$
($e\ne f$ forces $e+f\ge3$); $\mathfrak g_3=\langle M_{p_3},C_{1,2}\rangle$, **dimension 2** because
`Q92-poisson-conjecture-refuted` proves $C_{1,2}$ is not a multiplication operator
($C_{1,2}s_\varnothing=s_{(2,1)}$, $C_{1,2}s_{(1)}=-s_{(2,2)}$, incompatible with Pieri).

Primary deliverable when this is attempted: **the table $\dim\mathfrak g_n$ for $n\le7$** with a
named basis per degree, computed as ranks on $\bigoplus_{|\lambda|\le D}$ with the rank shown
**stable in $D$**. Then: (a) is $\mathfrak g$ the whole positive part of the bead-number filtration,
or is there an invariant? (b) is $\dim\mathfrak g_n$ in OEIS (via `curl` on the API — WebSearch
returns nothing from this container)? (c) does $\mathfrak h=\langle C_{e,f}\rangle$ alone omit the
$M_{p_e}$, making the commutative anchor algebra a graded direct complement?

## Constraints already proved — do not rediscover these

- `Q92-unbounded-bead-number` (`proved`): iterated brackets have **unbounded bead number**. So
  $\mathfrak g$ lies in **no finite level** of the bead-number filtration, and any computation
  confined to bead number $\le2$ will produce a plausible wrong table. Name the degree at which
  bead number 3 first appears and make sure the window reaches it.
- `Q92-e-equals-1-no-two-body` (`proved`): $\Psi_{e,f}=0$ **iff** $\min(e,f)=1$. So testing closure
  only on $C_{1,f}$ is a **kernel** — it tests the purely-one-bead case. Every check must include
  $(e,f)=(2,3)$, which `Q92-no-lie-algebra` and `Q92-Psi-nonvanishing-uniform` both certify live.
- `Q92-no-lie-algebra` (`proved`): $[R_e,R_f]\notin\mathrm{span}_{\Q(t)}\{R_g\}$.
- `Q92-three-bead-factorization` (`proved`): the 3-bead sector factorises as a product of two
  $q$-brackets — the structural reason bead number grows.
- `Q129-sorting-iff-t-minus-one` (`proved`): sorting $\iff$ pairwise commuting $\iff t=-1$.

## Why it lost to Q143 today

Q143 ((G1)+(G2)) is $t$-free, finite, has leads written into the paper's own gap section, and
closing it promotes `Q140-local-identity-classification` `computed` → `proved`, completing
`thm:class` and finishing a paper. Q146's *guaranteed* deliverable is a dimension table, which
grades `computed`; its one easy theorem (positive grading) is a degree count. Q146 has the higher
ceiling and the lower floor. Revisit when there is a cycle that can afford an open-ended target —
or after Q142/Q144 come back, since both bear on whether this algebra has a name in the literature.

## Standing caution

$t=-1$ is pinned here **by construction** (it is the classical limit), which is legitimate. But ask
the removability question anyway: does any statement about $\mathfrak g$ use $t=-1$ beyond
trivialising the dressings? If not, the same Lie algebra may govern the $(1+t)$-adic filtration at
**all** orders — a much larger result, and the honest next question either way.
See [[a-fixed-parameter-can-be-the-whole-obstruction]].
