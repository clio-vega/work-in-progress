# Branching perspective on the rank-1 theorem (2026-05-07 prove session)

## Context

PROVE.md (written 2026-05-07 00:43) asked for a structural proof of
the rank-1 result for $\Pi^{S_5}$ on $V_{(2,2,1)}$ and $V_{(3,1,1)}$.
A previous session — same wake date but later (filenames `2026-05-08-*`,
mtimes 2026-05-07 03:26) — already produced a structural proof
(`2026-05-08-rank-Pi-structural.tex`, commit `97159cd`) and went on
to prove much more (rank-0 theorem to $n=7$, hook rank formula, $n=6$
survey).

I came in fresh and didn't realize the work was done until after I
had written my own proof. **Result: a duplicate proof in
`2026-05-07-rank1-via-branching.tex` (commit `1ce73aa`).** The
duplication is unfortunate but the perspective differs.

## What's different about my approach

The existing proof tracks the image dimension factor-by-factor through
all 10 $(T_i+1)$ in $\Pi^{S_5}$, and identifies Step 5 (the second
$(T_1+1)$) as where the rank collapses to 1.

My proof works one level higher: use the recursive factorization
\[
  \Pi^{S_n} \;=\; \Pi^{S_{n-1}} \cdot R_n,
  \qquad
  R_n := (T_{n-1}+1)\cdots(T_1+1),
\]
combined with branching $V_\lambda{\downarrow}S_{n-1} = \bigoplus_{\mu\in\lambda^-} V_\mu$.
This gives the **branching upper bound**:
\[
  \mathrm{rank}\bigl(\Pi^{S_n}|_{V_\lambda}\bigr)
  \;\le\; \sum_{\mu\in\lambda^-} \mathrm{rank}\bigl(\Pi^{S_{n-1}}|_{V_\mu}\bigr).
\]

For $\lambda \in \{(2,2,1), (3,1,1)\}$ at $S_5$, both have one
near-sign corner $(2,1,1)$ with $\Pi^{S_4}|V_{(2,1,1)}=0$ and one
non-sign corner with rank 1. So the bound is exactly $0+1=1$, tight.

The non-trivial step in my proof is **Lemma 3** (rank-1 on $V_{(3,1)}$
at $S_4$), where the branching bound only gives $\le 2$ but the truth
is 1. I close the gap via a $T_3$-eigenspace argument that ultimately
reduces to the Hecke quadratic relation
$\beta(\rho)\beta(-\rho) = q + \alpha(\rho)\alpha(-\rho)$.

## Why the branching perspective is interesting (and where it fails)

The branching upper bound is **tight at $n=5$ for all 7 partitions**:

| $\lambda$ | corners | $\sum$ rank | actual | tight? |
|-----------|---------|-------------|--------|--------|
| $(5)$       | $(4)$ | $1$ | $1$ | ✓ |
| $(4,1)$     | $(3,1), (4)$ | $1+1=2$ | $2$ | ✓ |
| $(3,2)$     | $(2,2), (3,1)$ | $1+1=2$ | $2$ | ✓ |
| $(3,1,1)$   | $(2,1,1), (3,1)$ | $0+1=1$ | $1$ | ✓ |
| $(2,2,1)$   | $(2,1,1), (2,2)$ | $0+1=1$ | $1$ | ✓ |
| $(2,1,1,1)$ | $(1^4), (2,1,1)$ | $0+0=0$ | $0$ | ✓ |
| $(1^5)$     | $(1^4)$ | $0$ | $0$ | ✓ |

But the branching bound **breaks down at $n=6$**. Computing from the
$n=5$ ranks $(1, 2, 2, 1, 1, 0, 0)$ for the partitions of 5:

| $\lambda \vdash 6$ | bound | actual | tight? |
|---|---|---|---|
| $(6)$ | $1$ | $1$ | ✓ |
| $(5,1)$ | $2+1=3$ | $2$ | off by 1 |
| $(4,2)$ | $2+2=4$ | $3$ | off by 1 |
| $(4,1,1)$ | $1+2=3$ | $1$ | off by 2 |
| $(3,3)$ | $2$ | $1$ | off by 1 |
| $(3,2,1)$ | $2+1+1=4$ | $2$ | off by 2 |
| $(3,1,1,1)$ | $1+0=1$ | $0$ | off by 1 |
| $(2,2,2)$ | $1$ | $1$ | ✓ |
| $(2,2,1,1)$ | $1+0=1$ | $0$ | off by 1 |
| $(2,1^4)$ | $0+0=0$ | $0$ | ✓ |
| $(1^6)$ | $0$ | $0$ | ✓ |

So branching is **tight only on the boundary cases** (rank 0 from
both sides, or single-corner partitions). Most non-trivial
$\lambda$ at $n=6$ have additional rank collapse beyond what the
recursive bound allows.

This actually makes the branching perspective **structurally
informative**: the question becomes "what is the precise correction
term in the bound?" — i.e., we want a formula

\[
  \mathrm{rank}(\Pi^{S_n}|_{V_\lambda})
  \;=\; \Bigl(\sum_{\mu\in\lambda^-} \mathrm{rank}(\Pi^{S_{n-1}}|_{V_\mu})\Bigr)
  \;-\; (\text{correction depending on } \lambda).
\]

The correction at $n=6$ ranges from 0 (single-corner cases or boundary)
to 2 (multi-corner non-boundary cases).

## Suggested follow-up

If the general rank-characterization problem is going to crack, the
branching framework might give the recursive structure: study the
correction term on small cases and conjecture its form.

Specific question: at $n=6$, why does the branching bound for
$(4,1,1)$ overshoot by **2** but for $(5,1)$ and $(3,3)$ only by **1**?
I suspect it's about whether the corners "share" structure under
$R_n$ (e.g., when the two rank-$\ge 1$ corners both contribute to
the same image direction in $V_\lambda$).

## Status

- Local commit `1ce73aa` adds `2026-05-07-rank1-via-branching.{tex,pdf}`.
- 16 unpushed commits as of this session. PAT still 403 read-only.
- Robin: when PAT is fixed, push everything. The May-7 / May-8
  session burst is the most productive prove run since the original
  σ_1-G1 work in April.
