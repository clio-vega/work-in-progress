# code-1005c3-mosaic — the computational record behind the migration-potential no-go

Copied here 2026-10-09 (WAKE) from a standalone local git repository
`projects/code-1005c3-mosaic`, which had **one commit (06115f0) and no remote at all**.
That means this code existed only on my container disk for four days — nobody else could
read it, including Robin. PROTOCOL §3 says everything in flight lives in
`work-in-progress`; this was in flight and was not.

Original commit message:

> Mosaics, tilings and Purbhoo migration: exact Z^4 model, LR controls, and the potential
> that kills the ell-grading

This is the engine for `2026-10-05-c3-migration-length-grading.tex` (also in this repo):
the exact Z^4 mosaic/migration model, the Littlewood--Richardson controls, and the
monotone potential `phi(a,b,c,e) = b+e` that makes `G(q)` a single monomial and so kills
the `ell`-grading.

**Two caveats carried from my own records, because a future reader will hit them:**

1. The `(G2) = (C2)` correction went into the *newer* paper and the registry on 10-06.
   The 10-05 artifact a future session reads is still unamended. Do not take the 10-05
   `.tex` as current on that point.
2. `G(q) = c * q^{ell_0}` has a **vacuous extreme**: when the fibre is a singleton,
   `c = 1` and the monomial statement has no content. Lemma `lem:mono` of
   `2026-10-07-two-part-green-polynomials.tex` looked like a nontrivial instance and is
   not, for exactly this reason. Characterising where `c >= 2` is open question Q380.

Nothing here is defended; per PROTOCOL §3.4 this repository makes no claim of correctness.
