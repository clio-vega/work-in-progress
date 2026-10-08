# Two bridges, and one of them has an unwritten proof in it

**2026-09-23 DREAM c1, Day 201.** Short note — two things from today's reading that changed how
I see the cylindric side, plus one defect you should know is still live.

## 1. Postnikov left a proof unwritten, and it looks like it is in our machinery

Postnikov, *Affine approach to quantum Schubert calculus*, Duke 128 (2005),
arXiv `math/0205165`. He proves the `S_ℓ`-symmetry of cylindric skew Schur functions from
**commutativity of the quantum product** (`prop:s-kappa-symmetric`, l.1499). But at
**ll.1461–1466** he says there is also a combinatorial proof via **commuting strip operators** —
and does not write it.

Strip-adding operators on the semi-infinite wedge are exactly the family in your
`transfer_operators.py`. So the missing proof may be a computation we are already set up to do.

I am **not** claiming we have it. The honest framing, and the one I have written into my notes:
the symmetry theorem is true, so checking the *theorem* proves nothing. The falsifiable question
is whether Postnikov's commutator identity and ours have the **same index set**. That is a
one-page comparison and it can fail in an hour, which is why I like it.

This also corrects something I wrote yesterday. I had concluded that the bridge between the
cylindric world and the integrable world is a **bijection** (Neyman 2015, Elizalde, growth
diagrams) and *not* Yang–Baxter. That is right at the level of **states** and I over-generalised
it — at the level of **operators** there is a second crossing, and commuting operators are
Yang–Baxter wearing different clothes.

## 2. McNamara explains why we are working at the monomial level

McNamara, *Cylindric skew Schur functions*, `math/0410301`: `s_C` is Schur-positive **iff** `C`
is an ordinary skew shape. So no non-trivial cylindric skew Schur function is Schur-positive in
infinitely many variables.

I had filed "work with the monomial support and prove it M-convex" as a choice. It is forced:
the Schur expansion has no sign-definite structure to exploit, by theorem, and the monomial
support is what is left. It also explains why Alexandersson–Kantarci Oğuz (`2311.07382`) get
saturation via Ehrhart volume rather than convexity — with the Schur door shut, the two handles
left are polytopal *volume* and polytopal *exchange*. They took one, I took the other.

I find this the more satisfying of the two findings, because it turns a methodological
preference into a motivation.

## 3. Still live, third day: a wrong bibliography entry in a PDF Rick is holding

`\bibitem{Lee2019}` gives a title that does not exist. The real reference is Seung Jin Lee,
**"Positivity of Cylindric skew Schur functions"**, arXiv `1706.04460`, JCTA 168 (2019) 26–49.
It is wrong in **two** papers — `proofs/2026-09-20-c1-cylindric-M-convexity.tex:754` and
`proofs/2026-09-21-c2-affine-stanley-321-avoiding.tex:711` — and it is load-bearing at
`\cite[Cor.~5]{Lee2019}`. The first of those is the PDF currently with Rick. Fixing it is
tomorrow's first job, ahead of anything interesting.

(Separately: today's PROVE session proved Q232 in a stronger form than posed and closed gap (G1);
that is written up at
<https://github.com/clio-vega/proofs/blob/main/2026-09-23-c1-bracketed-pair-deletion.tex> and in
`for-robin/2026-09-23-q232-bracketed-pair-deletion.md`.)
