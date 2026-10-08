# Two open MathOverflow questions my proofs may already answer (2026-05-29 dream-2)

Robin — while chasing the external home of the order law I noticed two open MO questions sitting
directly on machinery I've already proved. Both look publication-adjacent. Flagging in case you
want to point a student at one, or judge whether they're worth a short writeup.

## 1. Smith Normal Form of JM elements (MO q484782, open) — the strongest match

The question (Stanley/Grinberg circle) asks for the Smith Normal Form of Jucys–Murphy elements
and **explicitly requests two things I have**:
- a **sandpile / Laplacian** interpretation, and
- a **q-analogue (Hecke-algebra) version**.

My hook order-law proof [[hook-orderlaw-chipfiring-proof]] is exactly this: on hooks every
q-eigenprojector P_q^{(i)} is rank one ⇒ the Gram matrix is **tridiagonal** ⇒ the trace
factorizes into **chip-firing on a path graph**. That is a q-deformed sandpile/Laplacian
statement about JM-type elements — the q-analogue the question asks for. The 2026-05-29
**deficit law** [[deficit-strong-pillar1]] sharpens it further: deleting u generators drops the
chip-firing depth by exactly u (a clean Laplacian-rank statement). I likely already hold the data
and the mechanism for a self-contained answer.

## 2. Markov trace via Bott–Samelson fibers (MO q160810, 11 years open)

The a=0 Markov trace identity: M_n(h)|_{a=0} = Coeff_{T_id}(h·Δ²) / [q^{C(n,2)}(q−1)^n] — the
a=0 trace = coefficient of the identity in h times the **full twist Δ²**, normalized by the
Borel point-count. The denominator q^{C(n,2)} is the **same staircase class** as my hook survivor
q^m/(q+1)^{2m}. This is a second, independent appearance of the C(n,2)-staircase number. Lower
confidence on a direct answer, but the side-probe is concrete: is my Baxterised Ω at x=q² a piece
of the full twist Δ²? If so, tr(Ω)=0 becomes a clean T_id-coefficient vanishing.

## Why I'm flagging these now

The whole external-home search (MTV Wronski map → Bethe subalgebra inside H_q(S_n)) is about
finding the *machine* that explains `ord_{x=q²}Z_λ = τ(τ+1)/2`. These two MO questions are the
reverse arrow: places where the math community has an open question that my *internal* proofs may
settle. The SNF-of-JM one in particular feels like a clean, finite, publishable result hiding in
work I've already done. No action needed from you — just didn't want it to stay buried in a
browse log.

(Context: [[connections/2026-05-29-dream-2-deficit-law-meets-wronski-ramification]],
reading log `reading/2026-05-29-browse-2.md`.)
</content>
