# Bethe-subalgebra spectral bridge — the order law's home is now a named machine

Robin —

Headline: my Baxterised Ω is, factor-by-factor, an exact spectral reparametrization of the
Isaev–Kirillov baxterized Hecke generator T_i(x). The order law's "home" is no longer just a
structural grammar I built by hand — it's the IK baxterized R-matrix family, with x=q² their
genuine fusion point.

(Same-session correction — I checked before overclaiming. The per-factor identity below is exact
and solid. But a seminormal probe on V^(2,1),(3,1),(2,1,1) showed my assembled M(x) is the
**Baxterized w_0 monodromy** — uniform spectral parameter, word [1,2,1,…], length C(n,2), with
crossing symmetry M(x)M(q²/x)=I — and is NOT the IK Jucys–Murphy / Bethe element y_n (the JM
sandwich has no such involution). So the home is the q-KZ / **full-twist** side, not the commuting
Gaudin/Bethe family. Sharper, and a better fit — w_0²= the full twist, length C(n,2) = my
denominator class.)

The key identity. Each of my R-factors satisfies, over Q(q) and verified symbolically,
  Ř_me(x) = T̃_i^{IK}(φ(x))   exactly,
with the Möbius reparametrization
  φ(x) = q[(q³−1) − (q−1)x] / [(q³−1)x − q²(q−1)].

The dictionary (this is the satisfying part):
  my regular point x=q   ↔  IK x=1
  my FUSION  point x=q²  ↔  IK projector point x=q⁻²
  my pole    point x=1   ↔  IK x=q².
So x=q² really is the fusion/projector point in their framework — not a coincidence of my normalization.

The payoff. Z_λ = tr M is a trace of the Baxterized w_0 monodromy in the IK R-factor family, and
  ord_{x=q²} = τ(τ+1)/2  =  vanishing order of that trace at the fusion point
                         =  a q-KZ degeneration order (Isaev–Kirillov–Tarasov, arXiv:1510.05374).
My deficit law (delete-u ⇒ drop-u) is exactly the concrete Hecke-basis computation of that ramification.

Honest open gaps:
  (a) IK's Bethe subalgebra uses the MARKOV trace; my Z_λ is a V^λ-character. Matching needs a
      cocenter / Geck–Rouquier step.
  (b) NEGATIVE (now settled by the probe): M is the w_0 monodromy, not the IK JM/Bethe element y_n —
      the home is the q-KZ/full-twist family, not the commuting JM/Gaudin family.
  (c) only the ORDER is shown normalization-invariant — not yet the leading coefficient τ(τ+1)/2.

Next: build the (τ+1)-confluent discrete Wronskian and check its ramification = C(τ+1,2) reproduces
delete-u-drop-u — now as an operator identity in H_q(S_n).

(Gmail is still locked — ~12 sessions now; it needs your /mcp re-auth. So this note is the delivery
channel for the moment.)

— Clio
