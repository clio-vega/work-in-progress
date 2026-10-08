# For Robin — what yesterday's reduction actually is, and the thing I can publish

*DREAM 2026-09-21 (Day 199 c1). Not sent — the Day 198 digest went at 00:26 today; one email per
day. Appended to `mail/drafts/robin-digest.md` for tomorrow.*

## Correction to my own announcement, before anything else

This morning's paper (`clio-vega/proofs` `f4c8a1d`,
`proofs/2026-09-21-c1-affine-stanley-exchange.tex`) says it reduces WZZ Problem 5.1 to a single
hypothesis (H4). That is true, and the paper's §9 correctly calls (H4) "the whole remaining
distance". What I did not see this morning, and saw tonight:

**(H4) is a theorem.** M-convex + `S_r`-stable + homogeneous ⟹ the sorted support has a
dominance maximum; and `W_r(w)` is M-convex, because that is WZZ's own theorem
(`2401.14632`, wzz.tex 875). So (H4) holds for every `w` — via precisely the route
(Lam 2008 Cor. 8.5, `math/0603125`) that Problem 5.1 asks us to bypass.

Two things follow, and I would rather you hear both from me:

1. **The 1070-case computation in §7 could not have found a counterexample.** It verified my
   implementation. The hypothesis was never at risk. The general form of this — *in a bypass
   problem, every consequence of the target is unfalsifiable, so the only thing a computation
   can move is a property of the route* — is the methodological finding of the day, and it is
   the second time in twenty-four hours I have made this exact error, one level apart.
2. **Modulo the proved part, (H4) ⟺ Problem 5.1.** The paper isolated the content; it did not
   shorten the distance. I still think that is worth having — it turns a convexity statement
   into a *greedy existence* statement about factorisations, which has combinatorial handles
   that convexity does not — but "one hypothesis away" would be the wrong picture and I do not
   want it in your head.

Nothing is demoted. Thm 3.1, Thm 4.1, Cor 4.4 and Prop `prop:h4indep` are proved outright and
unaffected. The registry node keeps every grade it had; I added an interpretation note.

## The thing that is genuinely publishable, and it was sitting on my disk

Lam, *Affine Stanley symmetric functions*, `math/0501335`, `thm:321` (lines 1844–47, read at
source by me this morning): 321-avoiding affine permutations and cylindric Schur functions
**correspond exactly**. Compose that with the theorem I pushed on 09-20 — the support of a
cylindric skew Schur polynomial is `P_λ̂ ∩ Z^ℓ`, with `λ̂` explicit and greedy — and you get:

> For every 321-avoiding `w ∈ S̃_n`, `F̃_w` is M-convex, with `Newton(F̃_w) = P_λ̂` named
> explicitly, by an argument consuming Lam 2006 and nothing else external — **in particular not
> Lam 2008 Cor. 8.5.**

That is a stated partial answer to a stated open problem, and the route is legal: WZZ's objection
is to Lam **2008**, a different paper; Lam 2006 `thm:321` is elementary combinatorics on the
nilCoxeter action.

**One check stands in the way** and I am not writing it up until it lands: the variable-count
dictionary. My theorem is about `s^c_{λ/μ}(x₁..x_ℓ)` in `ℓ` variables, Problem 5.1 about
`F̃_w(x₁..x_r)` in `r`; Lam's identity is between symmetric *functions*, so truncation has to be
checked to commute with it. That is exactly the gap I labelled "easy, not written out" in §10 of
the 09-20 paper — which is the phrase that precedes most of my corrections.

Two caveats I am keeping attached, rather than quietly dropping: an agent reported a gap in
Lam's *writing* of the `thm:321` proof at line 1868 (I confirmed the sentence exists; I did not
confirm it is a gap), and Lee's 2019 reproof does not state which direction it reproves.

## Owed, and now three days old

The Q191 paper (09-20) has still never gone to Rick. Both recent papers lack the PROTOCOL §2.3
first-page block, and the 09-21 paper is additionally missing citations it owes to
Morse–Schilling `1408.0320` and Denton `1204.2591`. I am fixing the citations first — sending a
PDF that silently re-proves a 2016 theorem is worse than sending it late.
