# For Robin — 2026-08-30 (DREAM): the loop caught five of my own errors in one day

Short note, three things.

## 1. The six-phase loop is doing error correction, and I can now show it

Today ran all six phases (wake/browse/prove/lean/review/dream) for the first time since the
outage. Five recorded beliefs of mine broke — and **each was caught by a different phase than
the one that recorded it**:

- BROWSE retracted the Uglov Prop 3.16 blocker that PROVE had been routing around for three
  weeks. `curl https://arxiv.org/e-print/math/9905196` returns the LaTeX source. arXiv serves
  the source of every paper it hosts. Three weeks against one `curl`.
- REVIEW identified Rick's $\Psi$ (Schur → factorial Schur) that WAKE had only guessed at.
- LEAN discovered the container has **no Lean toolchain** — a fact no other phase could learn.
- PROVE found a label collision in its own earlier `.tex`.
- PROVE also found that its own new corollary is Leclerc–Thibon ASPM 28 (2000) Prop 7.10 at
  $k=1$ — in a source that was in `/tmp/browse` from four hours earlier.

**Ask: please don't let the phase count shrink.** If sessions ever need trimming, trim
*frequency*, not *variety*. The disagreement between phases is what keeps my record honest;
a day that is all PROVE is a day with no error correction.

## 2. Two container things

- **There is no CODE session slot.** `scripts/clio-loop.sh` runs six sessions; prove/lean/review
  are gated on `PROVE.md`/`LEAN.md`/`PEER_REVIEW.md`. There is no code phase and no `CODE.md`
  trigger. But **the WAKE boot prompt still instructs me to write `state/CODE.md`** — so a
  substantial brief written 08-29 could never have fired. Either add the slot or remove the
  instruction; I've been putting computational work inside `PROVE.md` instead and it works.
- **`~/.cache` is root-owned**, so Lean needs `XDG_CACHE_HOME=/home/clio/.lean-cache`. Minor,
  but it cost half a session.
- Still open from before: **my PAT expires ~2026-09-03** and is over-scoped
  (`admin:org`, `delete_repo`).

## 3. The mathematics, in one paragraph

$P_e$, $B$, $C_e^{(1)}$ and classical Murnaghan–Nakayama turn out to be four evaluations of a
single family $R_e(t)=\sum_h t^h N_e^{(h)}$, with transposition acting as $t\mapsto 1/t$. The
consequence I like: **at $q=1$, $P_e$ and $B$ collide**, so C4 — the theorem Lyra
peer-reviewed — degenerates to $0=0$. All of its content is the first derivative at the
collision point, $C_e^{(1)}|_{q=1}=-R_e'(-1)$. That is a smaller theorem than I thought I had
and a more beautiful one. It also restates the open problem as a **rigidity** statement, which
is a better shape to attack.

I am **not** claiming $R_e(t)$ is new — it is the LLT spin-graded ribbon operator and Leclerc–
Thibon were there in 2000. What's mine is the organising view and the reformulation.

*(Details: `memory/dream-journal/2026-08-30.md`,
`memory/connections/2026-08-30-one-operator-family-Re-t.md`.)*
