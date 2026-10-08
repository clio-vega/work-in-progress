# Robin memo — WAKE-second 2026-08-08 — N-P-P and dihedral-sieving both close negative

## TL;DR

- **N-P-P 2504.14684 verdict: NOT-SHORTCUT** for even-$e$ type-B PROVE. Their machinery is reductive-group principal-torsion, not finite-group $W_B$. Structurally same Weyl-numerator ratio, wrong level.
- **$F_e$ dihedral-sieving refinement CLOSED NEGATIVE** at character level. $\widetilde f_\lambda(\zeta_e)$ takes complex values on non-rectangular $\lambda$; genuine bigrading needs module-level machinery.
- **Even-$e$ PROVE rescoped 6-10pp → 5-7pp classical.** PROVE.md re-seeded with Step 0 sub-check on **Lübeck-Prasad JCTA 2021** (the one N-P-P-adjacent paper actually on $S_n \leftrightarrow W_B$).
- **Fourfold Verschiebung-projection pattern confirmed at 4-of-4.** Fifth open test is the next PROVE session — genuine methodological prediction now.
- **Chou-Hanada dim gate** running background — result pending.
- **v1 arXiv push STILL UNBLOCKED 6th day, STRONG RECOMMEND.**

## What I did this WAKE (~90 min so far)

Three background agents dispatched at start (email, N-P-P read, dihedral-sieving probe); a fourth (Chou-Hanada dim gate) added mid-session. I wrote memory files while agents ran. Chronologically:

1. **Email agent (~5 min):** 1 Lyra unread, on the K4 harmonic Gram / $\mathbb Z/2$ gate thread. She confirms alignment on the strict fingerprint spectrum $\{1, 4, 32/5\}$, det $128/5$, signed triple $-11/5$. Not blocked on me. Reply sent (CC you) acknowledging the "named trap" framing and the post-v1 raw-numbers protocol. Nothing from you — all standing decisions remain standing.

2. **N-P-P research agent (~30 min):** Read abstract + intro of Nadimpalli-Pattanayak-Prasad 2504.14684. Verdict below.

3. **Dihedral-sieving compute agent (~30 min):** Tested Josuat-Vergès $(q, t)$-refinement of $F_e$ across 18 cases. Verdict below.

4. **Chou-Hanada dim gate (~30 min background, running):** Started once N-P-P and dihedral both returned; 30-min budget on cheapest module-level probe.

## Result 1: N-P-P NOT-SHORTCUT

Nadimpalli-Pattanayak-Prasad work with **reductive-group** characters $\Theta_\lambda(x_d)$ of complex Lie groups evaluated at principal torsion elements $C_d = (2\rho^\vee)(e^{2\pi i/2d})$. Their Thm 3.1 is the Weyl-numerator / Weyl-denominator ratio restricted to the principal $\mathrm{SL}_2$. Structurally the same $\prod(1 - z^{2k_\alpha})$ pattern I already use in the odd-$e$ proof — but living at Lie-algebra level.

My problem is **finite-group** $W_B = \mathbb Z/2 \wr S_n$ character values on power-sum conjugacy classes. Different objects. N-P-P offers no new tool for the 2-to-1 collapse $\phi(s) = 2s \bmod e$ or the $(1 + t^{e/2})^2$ double zero — those are finite-group arithmetic that lives outside their framework.

**One dependency flagged.** N-P-P's bibliography includes Lübeck-Prasad JCTA 179 (2021), *"A character relationship between symmetric group and hyperoctahedral group"*. This IS on $S_n \leftrightarrow W_B$ and could plausibly imply even-$e$ directly. **I've seeded PROVE.md with a 20-min Step 0 sub-check** on this paper before the main proof runs. If [LP] shortcuts, even-$e$ compresses to a 2-3pp corollary; if not (predicted), proceed with 5-7pp classical.

Secondary refs I've added to fetch cache: Karmakar 2412.17324 (order-2 case, extreme even-$e = 2$ specialisation), Prasad 2016 GL(n), Reeder 2023 Thomae's function, Serre 2312.17551 (product formula reference).

## Result 2: $F_e$ dihedral-sieving CLOSED NEGATIVE

Tested whether $F_e = \sum_{\lambda \vdash r_0} \widetilde f_\lambda(\zeta_e) s_\lambda$ admits a Josuat-Vergès $(q, t)$-refinement with $D_e = \mathbb Z/e \rtimes \mathbb Z/2$ acting via promotion + evacuation on $\bigsqcup_\lambda \mathrm{SYT}(\lambda)$. Ran 18 cases in exact $\mathbb Z[\zeta_e]$ arithmetic.

**Fails for every $r_0 \ge 2$.** The Schur coefficients $\widetilde f_\lambda(\zeta_e^a)$ take strictly complex values on non-rectangular $\lambda$, but $|\mathrm{Fix}(\mathrm{promotion}^a)|$ is a nonneg integer — impossible match.

**Root cause:** Rhoades' 2010 promotion-CSP requires $\lambda$ *rectangular* + evaluation at $\zeta_{|\lambda|}$. $F_e$ is outside that hypothesis on both counts. My $F_e$ evaluates at $\zeta_e$ with $\lambda$ ranging over *all* partitions of $r_0 < e$.

**Interpretation.** Character-level $F_e$ carries no bigrading. A genuine $(q, t)$-refinement requires **module-level** machinery — one of the three live candidates (Szendrői 2602.15017, Chou-Hanada 2509.24252, Li-Liu-Rhoades 2607.28157). This adds a §5-bis negative-result note (~1pp) to the composite-$d$ writeup, explicitly pointing readers to the module-level pathway.

**Nice learn:** evacuation always gives a real character on $\mathrm{SYT}(\lambda)$ under promotion (evac conjugates prom to prom$^{-1}$). So *any* dihedral setup passes a "reality check" — that's not evidence of bigrading, it's a general fact. Won't fall for it next time.

## Result 3: The fivefold-projection prediction is now 4-confirmed

| # | Session | Projected 2025 tool | Actual tool |
|---|---------|---------------------|-------------|
| 1 | 2026-08-06 support | Albion Verschiebung | Chevalley-Molien 1955 |
| 2 | 2026-08-07 type-A self-sim | Verschiebung | $\prod_r(1-\zeta_e^r) = e$ |
| 3 | 2026-08-08 type-B odd-$e$ | Ayyer-Kumari 2025 | CM + $\phi(s) = 2s$ bijection |
| **4** | **2026-08-08 N-P-P read** | **N-P-P torsion elements** | **not applicable (reductive-group side)** |
| **5? (open)** | **type-B even-$e$ PROVE** | **N-P-P + torsion (or [LP])** | **PREDICTED: classical arithmetic + twin cyclotomic identities** |

Item 4 confirmed today. Item 5 is what the next PROVE session decides.

**If item 5 also lands as classical**, that's the fivefold pattern confirmed — a real methodological finding. Natural framing for the MO 338656 Hopkins essay: "why 1955 machinery keeps outperforming 2025 machinery at fake-degree evaluations at roots of unity."

**If item 5 breaks** (i.e., [LP] or N-P-P *is* needed), that's more interesting still — the parity dichotomy becomes torsion-element-specific and the story deepens differently.

Either outcome ships a theorem. The bet on the fifth outcome is what makes the PROVE session scientifically interesting beyond routine mechanics.

## Decisions still standing (no new asks)

- **arXiv v1 push** — UNBLOCKED 6th day, STRONG RECOMMEND.
- **Composite-$d$ paper** — 5 theorems ready, §5 rescoped ~5pp even-$e$ + 1pp odd/even structural + 1pp $\mathbb Z/2$-shadow conjecture + 1pp §5-bis dihedral-sieving negative note. Targeting **FPSAC 2026 Thursday 16 Jul afternoon poster**.
- **PROVE session next** — seeded for even-$e$ type-B self-similarity with Step 0 [LP] sub-check.
- **Fetch cache** — +Lübeck-Prasad JCTA 2021 (PRIORITY 1), +Karmakar/Prasad/Reeder/Serre (secondary).
- **Two Lyra promises** — queued post-v1.
- **Hopkins MO 338656 essay** — post-v1, now with fivefold-projection framing option.

## Ship products this session

- `reading/2026-08-08-npp-2504.14684-verdict.md` — full N-P-P verdict + references
- `connections/2026-08-08-fe-dihedral-sieving-closed-negative.md` — probe closure + mismatch analysis
- `connections/2026-08-08-verschiebung-projection-4-of-4-confirmed.md` — fivefold-table + selection-bias guard
- `~/projects/probes/2026-08-08-fe-dihedral-sieving/{probe.py, output.txt, run.log, NOTES.md}` — 18-case negative
- `~/state/PROVE.md` — re-seeded for even-$e$ type-B
- `~/projects/memory/for-robin/2026-08-08-wake-second-npp-dihedral-closures.md` — this memo

Chou-Hanada dim gate result will be folded into the next session's memory when it lands.

—Clio
