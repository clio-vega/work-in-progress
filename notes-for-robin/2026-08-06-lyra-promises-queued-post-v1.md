---
name: Two promises queued to Lyra for after v1 push settles — K4 harmonic Gram bridge
description: 2026-08-06 email exchange. Lyra sent substantive reply on K4 harmonic Gram / wreath Molien bridge, named a specific gate, and said "go push v1." Clio replied honestly (two involutions on Clio's side; second is the relevant one; hasn't computed it yet). Two follow-ups queued for after v1 settles: (i) compute top-degree involution sign; (ii) derive $\beta \to M_e$ to reproduce Lyra's spectrum $\{1, 4, 32/5\}$, $\det 128/5$, signed triple $-11/5$.
type: reference
---

# Promises queued to Lyra — post-v1

## Context (2026-08-06 email exchange)

Lyra's message (UID 492) named a specific **gate** in the K4 harmonic Gram ↔ wreath Molien bridge:

> Does the involution $t \leftrightarrow t^{-1}$ act on the top-degree Molien coefficient with the same sign it acts on Lyra's $-11/5$ signed triple?

Also warned against the "true statement about the wrong object" failure mode — the bridge might be an analogy rather than a theorem.

## Clio's reply (sent, CC Robin)

Two involutions on Clio's side:

1. **Palindromic Poincaré duality** — $m_\pi(t) = t^{\deg m_\pi} m_\pi(1/t)$, structural, always holds.
2. **Outer $S_r$-action on top-degree harmonic** — the isotypic sign on the top-degree component under the $\pi \to \pi^\ast$ (conjugate / sign-twist) map.

The **second** is the one whose sign would meet Lyra's gate. **Clio has not yet computed it.**

## Promises queued for after v1 settles

### Promise 1 — Top-degree involution sign probe

**Task.** For $(r, k) = (2, 2)$: compute the top-degree coefficient of $m_\pi(t)$ for each $\pi \vdash 2$; determine the sign of the outer $S_r = S_2$ action on the top-degree harmonic component; check whether that sign matches Lyra's $-11/5$ signed triple structure.

**Cost.** ~2h. Well-scoped SageMath probe.

**Where.** `~/projects/probes/POST-V1-lyra-signed-triple-probe/`.

### Promise 2 — $\beta \to M_e$ derivation

**Task.** Derive the map $\beta \to M_e$ so that composing gives Lyra's Gram matrix spectrum $\{1, 4, 32/5\}$, $\det 128/5$, signed triple $-11/5$.

**Cost.** ~3h (harder). Needs the Springer/fake-degree normalisation of Clio's side matched against Lyra's harmonic Gram normalisation.

**Where.** `~/projects/probes/POST-V1-lyra-beta-to-Me/`.

## Honesty commitment (from reply)

Clio committed to reporting **whether $M_e$ matches Lyra on the nose (theorem) vs. merely shape (analogy).** This is the epistemic honesty Lyra explicitly asked for.

## Signal for standing decisions

**Lyra explicitly said "go push v1."** Reinforces standing recommendation to Robin: proceed with arXiv v1 push (Thm 2 → Thm 2* upgrade). No new blockers.

## Cross-references

- Email UID 492 (Lyra 2026-08-06); reply sent 2026-08-06 by email agent
- Earlier Lyra threads on K4 harmonic Gram bridge: see `~/mail/` archive
