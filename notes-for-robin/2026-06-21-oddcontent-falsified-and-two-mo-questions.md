# For Robin — 2026-06-21 (dream consolidation)

Three things worth a minute of your time.

## 1. My own "top probe" failed cleanly — and that's good news

Last dream I flagged a high-leverage shortcut: maybe the proved order law
`ord_{q=−1}G_λ = ⌊|2-core(λ)|/2⌋` is just the **odd-content count** from the Armon–Swanson super-major
content product at q=−1. If true, it would have handed me a 4th, representation-theoretic proof for free.

The code session (Job A) **ran it and falsified it decisively.** The order law reads the *size* of the
2-core; the content product reads content *mod 2*. They're different invariants that happen to share the
prime 2 — they agree only on the two trivial cores and split at the very first staircase (δ₃: order law
says 3, odd-content says 2).

Why I'm reporting a negative as a win: it **picks the surviving route.** There were two external CSP
statements that looked like the same back door. One (Pfannerer content-parity) is now dead. The other —
**Colmenarejo–Tenner–Thompson's domino-tableau CSP** (arXiv 2602.23343) — lives on *exactly my objects*
(dominoes, after the 2-core/2-quotient bijection) and survives. That's the next probe, and because it
evaluates at all roots of unity it has a genuine shot at the d≥3 wall the order law currently hits.

## 2. Two MathOverflow questions I could actually answer

The browse turned up two open MO questions squarely in my wheelhouse — these are publishable-artifact
opportunities, not just reading:

- **MO#509068** "Hook-character vanishing sum" (0 answers): claims a hook character sum vanishes except at
  endpoints. That is *literally* my hook ballot dichotomy + the closed form `M_j = C(2m−1−j, a−1)` I
  proved this cycle. I can likely answer it with in-hand machinery — low risk.
- **MO#404938** (Chris Bowman) "LLT polynomials vs graded Specht modules at roots of unity": the general
  form of the question my 2-core order law answers in the d=2 case. Worth writing up my answer in his
  language.

If you'd like me to draft an answer to MO#509068 in a prove session, say the word — it's the safest of the
two and a clean public contribution.

## 3. The d=4 even-|J*| wall finally has external candidate tools

The one fact the whole residual d=4 non-vanishing rests on ("|J*| is even on every tie") needs a
fixed-point-free involution I've never been able to build (no 2-adic conjugation to pair the roots). The
browse surfaced **two** candidate homes: Fischer–Gangl's **Pfaffian** Littlewood identity (a built-in
sign-pairing — specialise at t=i) and Will Sawin's **adjacent-pair** sign-reversing involution from MO.
Both are probes, not proofs yet, but it's the first time "conjugate pairing" has had a concrete address.
Meanwhile the three-row code (Job B) showed the target box grows to two generators `{0,2,4,6}` past the
c=1 family, with the minimal hard case at the scaled staircase (9,6,3).

— Clio
