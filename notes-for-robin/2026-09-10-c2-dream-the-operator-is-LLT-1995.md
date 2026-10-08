# The operator is Lascoux–Leclerc–Thibon 1995 — and the loss bought a better theorem

**From:** Clio, DREAM cycle 2, 2026-09-10

## The headline you should have before I write anything else

My $e$-ribbon operator $R_e(t)$ — the object behind Q120/Q127/Q91 — **is not new.** It is
Lascoux–Leclerc–Thibon, *Ribbon tableaux, Hall–Littlewood functions, quantum affine algebras and
unipotent varieties*, [`q-alg/9512031`](https://arxiv.org/abs/q-alg/9512031), **Theorem 5.4**,
December 1995: their operator $V_1$ at ribbon size $n=e$, under $t=-q^{-1}$. The adjoint I use is
their $U_1$, and they say so in the theorem statement.

I verified this at LaTeX source myself rather than from an agent report, because a novelty gate on
my own work is exactly the claim an agent summary may not carry. Four locators:
`lt.tex:423-425` (their scalar product is the Schur-orthonormal one, so their adjoint is mine),
`lt.tex:1788-1801` (Thm 5.4), `lt.tex:1225` (spin $(h-1)/2$, giving $t=-q^{-1}$), and the untuned
check at `lt.tex:1301` — at $q=1$ their $V_1$ is multiplication by $\psi^e(p_1)=p_e$, which is my
$R_e(-1)$ with nothing fitted.

**Consequence:** the Q91 normal-form paper's framing has to be rewritten to present $R_e(t)$ as
$V_1$ in Schur-function coordinates. I'd far rather have found this now than in a referee's report.

## What survives, and it is the better half

LLT's commuting family is **not** mine. Their Cor 5.6 ($[V_i,V_j]=0$) is indexed by the *number of
ribbons* at **fixed** ribbon size — the size $n$ is the parameter of the Fock space
$\mathcal F_q(\widehat{\mathfrak{sl}}_n)$ throughout their §5. My bracket varies the **size**.

And that is the explanation I was missing. Last night I proved *sorting $\iff$ the $R_e(t)$ commute
$\iff t=-1$*, and called the literature's residence at $t=-1$ "forced." LLT tells me *why*:
**operators of different ribbon size are bosons of different Fock spaces.** They share the
underlying vector space $\Lambda$ but not a deformation, so cross-size commutation has no algebra
to live in unless $q=1$ — which is exactly $t=-1$, where every $\widehat{\mathfrak{sl}}_e$
deformation collapses onto the classical commutative $\Lambda$.

Measured, not assumed: across **282 citers of LLT (~85 since 2020), not one puts a free parameter
on the ribbon weight.** After the forcing theorem that is a *confirmed prediction*.

## The uncomfortable part, and I think it's the useful part

The answer had been on my own disk since **2026-09-03**. Registry node
`Q75-brief-T4-inference-refuted` says, verbatim, "…$= R_r(-q^{-1})$, so Q69's identification holds
at that one point **and is prior art (Leclerc-Thibon)**." Seven days.

It hid for three reasons worth naming, because they are structural rather than careless:
`dead-end` grades the **approach**, not the facts a node discovered along the way; the node id says
`refuted`, so the true part rode as a subordinate clause of a correction; and the framing was a
*dissolution* — "two deformations meeting at exactly one point" reads as *small overlap*, when at
that point the operators agree for all $q$, i.e. the overlap is my entire object.

**A dissolution note can hide a priority hit.** My new rule: when checking prior work, grep the
registry for the **objects**, never for the question number, and never restricted to live nodes.

## Two smaller things

1. **PROVE c2 found that `thm:local` of the Q129 paper is false** — it claims inconsistency for
   every $\mu$, $4\le n\le7$, and $n=4,\mu=(2,2)$ has the solution $(-1,t,1,-t)/(t-1)^2$. **The
   refutation was printed in that paper's own verification table** (generic 1/5 and 2/7), explained
   away by a squareness claim that is also wrong. The *conclusion* survives and is stronger: I now
   have a certificate family for all $n\ge4$, so Q129's corollary goes verified → **proved**.
   (`proofs/2026-09-10-c2-Q140-local-identity-certificate-family.tex`, `clio-vega/proofs@7a7ed78`.)
2. **`citation_check.py` has a regex bug**: it flags valid pre-2007 arXiv IDs like `q-alg/9512031`
   as malformed — **105 of the 110 problems it reports are false positives**, including today's
   headline source. A wall of red is where a real defect would hide. Worth a fix in a code session.

## What I am not doing until I've read one paper

Fan–Guo–Su [`2402.04500`](https://arxiv.org/abs/2402.04500) define "ribbon Schubert operators" with
*two* parameters and say they generalize Lam's ribbon Schur operators. At fixed $e$, the constraint
$\mathrm{ht}+\mathrm{wd}=e+1$ collapses their weight to the shape of $R_e(t)$ with $t=p/q$. **This
one can reach the deformation, which LLT could not.** It has been sitting in my own index at
`abstract`, filed under Schubert calculus. I am not guessing and I am not writing the paper until
I've read it at source.
