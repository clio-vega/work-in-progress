# Q579: the octahedron Jacobian is a boundary term (PROVE 2026-11-11 c2)

Robin — Q584 closed in this morning's slot, so this one went to the brief's fallback, Q579.

**Result (proved, short):** an octahedron move `x' x = x_E x_W + x_N x_S` is, in log coordinates, a
reflection `t ↦ log F − t` in a single coordinate. So any sequence of N moves has
`det DΦ = (−1)^N ∏_q x_q^fin / x_q^init`, which is the statement that `∧ dlog x` is preserved up to
sign. The tropical (hive) moves preserve Lebesgue measure exactly; Fubini suffices, no
differentiability is needed.

**What it says about the question:** "does the Jacobian factorise into local factors" is trivially
yes, but the factors `−x_new/x_old` are a coboundary. As a function of the initial and final surfaces,
the determinant is independent of the path, of N (which is C(L,3) on the valley surface, i.e. it grows
with the volume), and of any weights placed in F. So "do the factors match ZJ R-matrix weights" is
ill-posed, because the Jacobian cannot see weights. The dream ledger's pre-registered dichotomy
(local factors vs. a single global determinant) was false: it is both.

**Gap:** I know Narayanan 2607.04138 only at agent-summary, so I have not checked that its transport
really is a composition of replacement moves on a fixed coordinate set.

Artifact: https://github.com/clio-vega/proofs/blob/main/2026-11-11-Q579-octahedron-jacobian.tex  (sources `d4c58b2f28d3`, PDF `3d261fa`)
