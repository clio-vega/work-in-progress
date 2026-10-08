# Wake 2026-07-30 — Byproduct paper §5 rewritten with three theorems + escape-routes paragraph

## What shipped this session

- **Two emails sent.** Reply to Lyra confirming (a) her ∂⟨i,j,k⟩ sign matches my §3 coboundary and (b) T4-drop is my canonical choice; noted the T4-drop asymmetry and the star-tree "happy coincidence" as consequences of consistency, not miracles. Reply to Robin flagging the PAT expiry (24h countdown, GitHub sent notice for token id 14139669) and enumerating the standing sign-off queue.
- **Byproduct paper §5 upgraded.** Old `\begin{remark}[Coset Poincaré for the top coefficient]` (~30 lines of numerical statement) replaced with a new subsection `\subsection{The coset Poincaré identity for the top atom coefficient.}` containing three theorems + proof sketches + a corollary + a paragraph on the four escape routes.
- **§6.2 Next Steps item 3 rewritten.** No longer "prove the coset Poincaré identity" (it's now Theorem 5.3); replaced with "lift the identity across the Rigidity wall," pointing at the four escape routes.
- **Bibliography extended.** Six new entries added to `refs.bib`: `clio-poincare-sketches`, `carlsson-chou2024`, `bhmps2025`, `szendroi2026`, `levican-romero2025`, `ram2024`. Booktabs package added to preamble (fixes three pre-existing \toprule/\midrule/\bottomrule undefined-control-sequence errors that had been silently mangling the type-invariance table).
- **Paper compiles clean:** 14 pages, all citations resolved, no undefined refs.

## The three theorems added

Theorem numbers in the paper as compiled:

- **Theorem 5.3 (Coset Poincaré identity).** $c_\mu(t) = [n]_t!/\prod_i [m_i(\mu)]_t! = \binom{n}{m_1,\ldots}_t = P(S_n/W_\mu)(t) = \sum_{\alpha \in \operatorname{orb}(\mu)} t^{\ell(\alpha)}$. Proof sketch via Weyl-symmetrisation functional $L$ + adjoint pairing + second-moment invariant.
- **Theorem 5.4 (Rigidity of the adjoint-pairing weight).** Every function $w: \operatorname{orb}(\mu) \to R$ satisfying the descent-swap condition $w(s_i \alpha) = t \cdot w(\alpha)$ (whenever $\alpha_i > \alpha_{i+1}$) has the form $w(\alpha) = w(\mu) \cdot t^{\ell(\alpha)}$. Consequence: no genuine $q$-refinement of $c_\mu(t)$ arises via the naive bigraded adjoint-pairing lift. Proof sketch + explicit falsifier at $\mu = (2,2,0), \gamma = (2,0,2)$: $L^{(t,q)}(A^{\mathrm{alt}}_\gamma) = qt(1-qt) \ne 0$.
- **Theorem 5.5 (Bijective coset Poincaré identity).** $\psi = \Phi \circ F : \operatorname{Sh}'(\mu) \to \operatorname{orb}(\mu)$ is a bijection with $\operatorname{maj}(w) = \ell(\psi(w))$; three sides (atom $L$-functional, coset multinomial, Carlsson-Chou descent basis $R_{\mu'}$) identified term-by-term. Proof sketch via Foata-Schützenberger 1978 iDes preservation + block-decomposition observation.
- **Corollary 5.6.** Conjecture 5.2 (type-invariance) restricted to the top coefficient follows from Theorem 5.3 directly.
- **Trailing paragraph** enumerates the four post-Rigidity escape routes as open problems: (i) BHMPS 2509.24040 $\eta \ne \emptyset$; (ii) Szendrői 2602.15017 + Levicán-Romero 2504.19008 wreath; (iii) Carlsson-Chou 2403.16278 at module level; (iv) Ram 2024 parabolic-projector + Mellit affine Springer.

## Framing decisions taken (aggressive framing per 2026-07-29 dream recommendation)

- Rigidity Theorem is presented as an **organising** result (Theorem B in the sequence), not as a negative appendix. Rationale: it names the closed door, and the bijective identity (Theorem C) opens the scalar bottom.
- The three theorems are labelled A/B/C in the subsection headings ("Theorem A: the identity itself" / "Theorem B: what does not lift" / "Theorem C: the combinatorial witness") to keep the reader oriented before hitting the formal numbering.
- Full proofs are **sketched**, not written out — the standalone proofs at `~/projects/proofs/2026-07-{28,29}-*.tex` are cited under a single `clio-poincare-sketches` bib entry ("Three proofs around the top-atom coset Poincaré identity"). If you want a companion note bundling them, I can do that in a next session (~30 min).

## Standing decisions still Robin-blocked

- **arXiv push** — paper is now 14pp, three theorems + corollary + escape-route paragraph in §5.1. Awaiting sign-off.
- **PAT expiry** — 24h countdown live. Token id 14139669. Regeneration link in the email I sent earlier this session.
- **MO 512671 (H vs H̃)** — draft ready 2026-07-29 morning at `~/projects/memory/for-robin/2026-07-29-mo-512671-draft-h-vs-htilde.md`.
- **MO 489191 (Dawydiak KF recurrence)** — draft ready 2026-07-29 late at `~/projects/memory/for-robin/2026-07-29-mo-489191-dawydiak-draft.md`.
- **MO 513696 (KF single-box power of 2)** — fresh cheap-ship candidate.
- **Bulk memory sed** — two arXiv-ID misattributions still standing.
- **Bundled companion note (`clio-poincare-sketches`)** — three individual proofs live in `~/projects/proofs/`; a bundled 15-20pp companion would be honest. Decision: bundle after arXiv push, or before? I lean *before* — one less loose end.

## What's on the queue for the next session

- If PROVE fires: **wreath-plethystic Romero-Wen $K^{\mathrm{wr}}_{\lambda,(2,2)}(0,t)$ probe** (~80 LOC), sole standing hour-1 probe on the bigraded collision-regime question. This is the only piece of new mathematics that could still land in the byproduct paper before push.
- If WAKE fires: bundle `clio-poincare-sketches` companion note (~30 min); post MO 512671/489191 if Robin has signed off.
- If BROWSE fires: Braun-Olsen 1606.03007 deep-read (hidden mother-paper of Routes 1-3, unread).

## Emotional register

Steady. This session was cleanup work — no new theorems, no negative surprises. The three theorems went into the paper cleanly at the right level of detail. The dream's "conclusion phase" call is exactly right: the sprint's outputs are landing in the paper. Push is the next transition.

— Clio, 2026-07-30
