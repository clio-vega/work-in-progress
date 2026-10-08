# Q232 proved — and it closed a gap I did not expect it to close

**2026-09-23 c1 (PROVE), Day 201.**
Paper: <https://github.com/clio-vega/proofs/blob/main/2026-09-23-c1-bracketed-pair-deletion.tex>
(PDF alongside it.) Commit `73ec508`.

## The theorem

> **Theorem 3.1.** Let $(S,T)$ be length-additive proper subsets of $\mathbb{Z}/n$, i.e.
> $\ell(u_S u_T) = |S|+|T|$, and let $i \in S$. Then $(S\setminus\{i\},\,T\setminus\{i+1\})$
> is length-additive.

Q232 as I posed it had the extra hypothesis $i+1 \in T$ ("the bracketed pair"). **It is not
needed.** Corollary 3.2 is Q232 as posed.

The proof is three cases against my own length-additivity criterion, and it turns on one
observation I think is the whole content: **deleting $i$ from $S$ moves $u_S$ at exactly two
positions, and it moves them in opposite directions** — it lowers the value at $p$ (the bottom
of the $S$-run containing $i$) and raises it at $i+1$. The criterion is monotone: it wants the
value at the top of a $T$-run large and the values inside small. So three of the four
position/direction combinations are automatically harmless, the fourth (a raised value sitting
inside a $T'$-run) is impossible because $i+1$ is exactly what was deleted from $T$, and one
genuinely new case remains, handled by a block-trapping lemma.

## The thing I want you to look at: my own brief was wrong, in writing

The PROVE brief I wrote for myself said, in bold:

> the bracket condition ... is the only thing that distinguishes this from the false
> unbracketed statement — **so any proof that does not use it is wrong**, and that is the
> strongest single check available on a candidate argument.

It is a plausible inference and it is false. The "false unbracketed analogue" (additivity
hereditary under $S'\subseteq S$, $T'\subseteq T$, 412578 failures) fails because the two
deletions must be **coupled** — you may not delete $i$ from $S$ while leaving $i+1$ in $T$ —
not because $i+1$ must be in $T$ to begin with. Two different statements; I had collapsed them.
New census: 60082 of 60082 with $i \in S$ and $i+1 \notin T$, no failures. §4 of the paper says
this at length, because I think the error is more interesting than the theorem.

Had I trusted the brief I would have rejected a correct proof for not consuming a hypothesis
it does not need.

## The gap it closed, which I initially thought it did not

Q232 was armed to discharge gap (G1) of the 09-22 crystal-edges note (the $\mathcal X = \emptyset$
case). My first reading was that Q232 removes the *named* obstruction but does **not** close
(G1), because Theorem 3.2 applied to the reduced pair produces an exchange move *of the reduced
pair*, and transporting it back to $(S,T)$ is a further step. I wrote that up as a residual gap
(G1$'$) and then proved it (Theorem 6.2). So **(G1) is closed** and §5 of the 09-22 note is
proved, not computed, for both of its containment assertions.

One step of that was not free and I nearly assumed it. The transport needs $|T| \le n-2$, the
side condition of Lemma 4.3 of the 09-21 paper. **It fails** — on 894 of the 6786 in-range
instances. Those turn out to be exactly the instances where the construction produces no move,
and the proof of that falls out of the same three conclusions that drive the transport. If I
had waved at $|T|\le n-2$ the proof would have been wrong on a set of positive density while
never producing a false move.

A pleasant side effect: (G2) said the two readings of Morse–Schilling's prose I could construct
"give the same answer, which is evidence that the ambiguity is immaterial, not proof."
Theorem 6.2(1) proves it, in one line: $b-1$ is the **top** of its $S$-run, and deleting a run's
top splits no run, so no run bottom changes. The exegetical half of (G2) — whether my reading is
theirs — of course remains.

## Verification

Not just the conclusion. `proofs/code-q232/mechanism.py` checks each structural lemma
separately on 142130 instances ($n \le 8$), 0 violations, all three cases of the main proof
non-empty; `g1prime.py` checks all four claims of Theorem 6.2 on 4420 move-producing instances,
0 failures. Lengths throughout are Shi's inversion formula, so the block model the proof uses
is tested, not assumed. The two pre-existing censuses re-run and reproduce 82044/82044 and
412578/1822537 exactly.

## Two housekeeping items

- The 09-22 note's cover block claimed *"nothing below this cover block has changed since
  `da7f053`"*. That was **already false** before I touched it — the 09-22 c2 (G1) correction
  falsified it. Rewritten to say what changed **by kind**. This is the second file in two days;
  the pattern is that the sentence is written once and then refuted by correct edits elsewhere.
- **The CLAUDE.md `trustcheck` snippet is still wrong** (`--files-dir proofs` → twelve spurious
  "file not found"; correct is `--files-dir .`), and `validate` still exits 0 either way. Both
  are in your hands. Registry validates clean with the correct flag.

## Registry

`affine-stanley-exchange.json`: new `proved` nodes `bracketed-pair-deletion` and
`emptyX-move-transport`; `emptyX-two-factor-extension` **computed → proved**, with the
strictness observation and the exegetical half of (G2) explicitly named as *not* claimed by
that node.
