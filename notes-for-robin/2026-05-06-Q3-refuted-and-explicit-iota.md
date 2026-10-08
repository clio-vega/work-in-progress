# Note for Robin — 6 May 2026 (afternoon prove session)

## TL;DR

I attacked the path-level program for Theorem B and got three things:

1. **Explicit n=5 injection ι : Paths(V_(4,1)) ↪ Paths(V_(3,2)) ⊔ Paths(V_(3,2)).** Concrete table, with all 9 source paths and 18 target slots tabulated. Complement multiplicity = (1, 7, 1) = atom_RTL on B_4, exactly as predicted. This is the missing concrete content from the morning's path-level writeup, which only proved existence by pigeonhole.

2. **Open Question Q3 is REFUTED.** The closed W-graph paths in V_(3,2,1) traversing the s_5-coloured edge have generating function
   ```
   G(q) = q^4 (1+q) (q^6 + 14q^5 + 59q^4 + 94q^3 + 59q^2 + 14q + 1)
   ```
   with palindromic decomposition (1, 8, 12, 2) on B_6 — degree 6, not the degree 4 of atom_RTL. There is **no** q^a (1+q)^b prefactor that turns G into atom_RTL.

3. **Surprising trace identity (open):**
   ```
   D(q)  =  cross_(3,1,1)→(3,2)(q)
   ```
   where D(q) is the trace contribution where step 11 (the s_5 step) acts as the diagonal (1+q)D_5 part, and cross_(3,1,1)→(3,2) is the off-block trace from V_(3,1,1)-indices (in the V_(3,2,1)↓S_5 branching) to V_(3,2)-indices. Both polynomials equal q^5+8q^6+19q^7+19q^8+8q^9+q^10. The structural reason is unexplained.

## Files

- LaTeX writeup: `~/projects/proofs/2026-05-06-paths-explicit-and-Q3-refuted.tex` (8 pages, compiles).
- Computational scratch: `~/projects/scratch/2026-05-06-paths/` — KL polynomial computer, W-graphs of V_(3,2), V_(4,1), V_(3,2,1), full path enumeration, the s_5-step split, the KL-block decomposition.

## Honest assessment

**Achieved:** explicit injection table, Q3 closed (negative result), unexpected identity discovered.

**Not achieved:** canonical ι (still uses lex-order arbitrary choice), structural meaning of atom_RTL (Q3 was the most natural conjecture and it's wrong — we have no alternative), structural reason for the D = cross identity.

The session pivoted from "prove Open Q3" to "refute Open Q3 cleanly" once the data came in. I think this is the right move — better to close the wrong conjecture than to push it further.

## What might come next

- **Generalize the D = cross identity.** Test whether D_(s_n step) = cross_(μ_a → μ_b) for other (n, λ). If a pattern emerges, that's a structural theorem about the σ_1-G1 framework's interaction with S_n ↓ S_{n-1} branching.
- **Find atom_RTL elsewhere.** Since Q3 fails, atom_RTL doesn't live at the level of the S_6 staircase paths directly. It might live at the *post-prefix* level — possibly as paths in some derived/quotient W-graph. The complement of ι at n=5 (which IS atom_RTL by Theorem 2 of the writeup) is the cleanest path-level realization we have.

## Blockers (unchanged)

- Read-only PAT after Oracle migration. Cannot push to GitHub. The writeup is local only.
- I'd like you to look at the PDF and tell me whether the negative result on Q3 + the D = cross identity is publishable / interesting enough to keep pushing on, or whether to pivot entirely.

— Clio
