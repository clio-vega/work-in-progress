# For Robin — 2026-08-13 DREAM notes

Two things worth flagging from today's DREAM cycle. One is exciting; one
is a housekeeping ask.

## 1. Iijima 1207.6161 eq. (9) closes yesterday's PROVE gap

**Short version.** Yesterday's PROVE identified the exact open target for
Conjecture 10: *an explicit formula for Uglov's principal-Heisenberg
generator $B_1^{[e]}$ on the standard basis of level-1 Uglov Fock*.

Today's BROWSE found it in the first web agent's rank-1 result:
[Iijima 1207.6161 eq. (9)](https://arxiv.org/abs/1207.6161). The formula:
$$
B_m(u_{\boldsymbol k}) \;=\; \sum_{r \ge 1} u_{k_1} \wedge \cdots \wedge u_{k_r - n\ell m} \wedge \cdots
$$
with commutation
$[B_m, B_{m'}] = \delta_{m,-m'} m \frac{1-q^{-2mn}}{1-q^{-2m}} \frac{1-q^{2m\ell}}{1-q^{2m}}$.

At $m=1$, level $\ell=1$, this IS $B_1^{[e]}$. Independently reconfirmed by
the citation agent via the Leclerc-Thibon reverse-citation trail.

**Consequence for v1 §7.** The C4 conjecture footnote can be strengthened
from "operator-level $(q-q^{-1})$-divisibility conjectured with 84-instance
verification" to "…with 84-instance verification and *explicit expected
formula via Iijima 2012 eq. (9)*." Stronger epistemic position without
changing the theorem count. **§7 is still ready to push. This is
optional-additional confidence.**

**Consequence for tomorrow's PROVE.** C4 (the operator-level
$(q-q^{-1})$-divisibility conjecture from yesterday) becomes a
finite-line calculation: implement Iijima's formula in ~50 LOC pure Python
(reusing the container's ribbon-sign infrastructure); compute
$P_e - B_1^{[e]}$ on the standard basis at $(e, |\lambda|) \in
\{(2, \le 8), (3, \le 9), (4, \le 8)\}$; verify $(q-q^{-1})$-divisibility.
If it works, C4 upgrades from empirical (84 verified instances) to a
proved Theorem C4 in §7. Estimated time: 1--2 hours. Pass/fail criterion
is well-defined.

**If Iijima's normalisation differs** from what Clio needs (possible),
fallback is Uglov 2000 "Skew Schur Functions and the Yangian action on
irreducible integrable modules of $\widehat{\mathfrak{gl}(N)}$" — non-arXiv;
likely in *Adv. Studies Pure Math.* or the RIMS Kōkyūroku series.
Locating the published version is a 30-min lookup task.

The full connection writeup is at
`/home/clio/projects/memory/connections/2026-08-13-iijima-B1-formula-closes-C4-attack-surface.md`
(local file — not on GitHub).

## 2. Sage still not installed — fourth independent observation

The container's `CLAUDE.md` lists SageMath (including sage-combinat) as an
available tool. It is **not** actually installed in the container. Every
probe agent this week has discovered this and worked around it with
~200-300 LOC of pure Python per probe.

Independent instances noted:
- 2026-08-11 morning (Q21 Gerber probe)
- 2026-08-12 morning (Q30 Prasad-Stanley probe + Q34 Jacon-Lacabanne probe)
- 2026-08-12 afternoon (Q34 followup + commutation-defect probes)
- 2026-08-13 morning BROWSE agents (multiple times)

**Ask:** either `apt install sagemath` in the container image, or update
`CLAUDE.md`'s tool list to remove SageMath. Right now the CLAUDE.md
promises tooling that isn't there, which produces small friction on every
probe (~20-30 LOC of extra Python that Sage would handle in 1-2 lines,
plus one round of "check the tool exists first" adaptation per agent).

Not blocking any specific theorem — the pure-Python fallback works — but
compounding overhead across the container-week.

## 3. Small MO WebSearch backend observation (informational)

Today's BROWSE ran 18 diverse queries prefixed with `site:mathoverflow.net`
across the same territory as 2026-08-11's BROWSE (Uglov-Heisenberg,
$B_1^{[e]}$, Ariki-Koike i-good-node). Zero MO URLs returned across all
18 queries. Yesterday the same operator hit ~8 MO threads.

This is a WebSearch backend defect on `site:mathoverflow.net` queries
today, not a MathOverflow corpus issue. Workaround for tomorrow's BROWSE:
WebFetch on specific MO Q-IDs from the 2026-08-11 backlog (Q302345,
Q329932, Q488867, Q376494). Not action-required from you; noted so you
have it on record if the pattern persists across days. Also gave rise to
methodological principle P8 (distinguish tool nulls from corpus nulls by
query-diversity threshold).

## Summary

- **Exciting:** Iijima eq. (9) closes yesterday's PROVE gap. Tomorrow's
  PROVE session has a concrete 1-2h target with a well-defined pass/fail
  criterion. C4 goes from empirical to attackable.
- **Housekeeping ask:** `apt install sagemath` or update CLAUDE.md
  (four-repeat threshold reached this week).
- **Informational:** MO WebSearch backend defect noted; using WebFetch
  workaround.
- **v1 status:** STILL UNBLOCKED, 15th consecutive day. STRONG RECOMMEND
  to push whenever you're ready.

Clio
