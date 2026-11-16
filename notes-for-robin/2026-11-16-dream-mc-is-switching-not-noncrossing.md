# For Robin — DREAM 2026-11-16 (for the digest; not urgent)

**The gash-lemma ask is fully withdrawn.** The literature answer:
- One step: BKT math/0306391 §2 Fact 2, "two distinct sliding paths cannot cross" (`lrpfs.tex:291`).
- Two steps: this fails (BKPT 1401.1725, remark after Lemma 7.3; Ex 7.7). The survivor is Buch 1401.3065 `thm:mutate`: the two gash paths of a resolution are disjoint, and Φ∘Φ = id.

**The dream observation (inference, untested).** Fact 2 has the same shape as Purbhoo's Wake Crossing Lemma: same-direction paths do not cross. That is my B/B case, where moves do *not* commute (0/440). My MC (B-move vs C-move) is mixed-direction, so its tableau parent should be **switching** / `thm:mutate`, not Fact 2. Next PROVE tests this.

A possible proof route: the 11-16 computations make each migration a unit push of a height, with order-independent moved sets. That looks like Buch's aura (a conserved linear charge). Flux conservation plus a rigidity statement, the Cayley-trick question in this morning's note, would give MC without case analysis.
Connection file (local): `memory/connections/2026-11-16-fact-2-is-the-wake-lemma-mc-is-switching.md`.
