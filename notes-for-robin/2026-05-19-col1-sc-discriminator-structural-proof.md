# Structural proof of the column-1 SC discriminator at (3,3,1,1,1)

**2026-05-19 prove session.** Outcome: **2 of 3 lemmas fully closed structurally, 1 with computational completion.**

## Theorem (target, recap from prove session)

For $T \in \mathrm{SYT}(3,3,1,1,1)$ SR-at-1, $\Omega v_T = 0$ iff at least one of:
- **(α)** $T(2,1)=3$ AND $T(3,1)=4$
- **(β)** $T(3,1)=5$ AND $T(4,1)=6$
- **(γ)** $T(4,1)=7$ AND $T(5,1)=8$

## Key structural insight

The proof reduces to **three "L_α / L_β / L_γ" lemmas** via the observation that every $R'_k$ has $S_1$ as its rightmost factor, so $R'_k$ kills $V_- = \ker S_1$ (= SC-at-1 span). If $\Pi_{k+1}(T) := R'_{k+1} \cdots R'_9 v_T \in V_-$ at the "first-vanish stage" $k$, then $\Omega v_T = 0$.

**Operators $S_j$ for $j \ge 3$ preserve $V_+ \oplus V_-$ separately** (they don't move 1 or 2). Only $S_1$ and $S_2$ mix the decomposition. This is the kingpin observation.

## Results

### L_α (FULLY PROVED, clean and short)

Two-line proof:
1. Commute $S_1$ past $S_3, ..., S_{k-1}$: $S_1 R'_k = (S_{k-1} \cdots S_3) S_1 S_2 S_1$.
2. For SR-at-1 $T$ with $T(2,1)=3$: $S_1 S_2 S_1 v_T = -(q+1) v_T$ (since $s_2 T$ is SC-at-1, killed by $S_1$).
3. α-condition $T(3,1)=4$ gives $S_3 v_T = 0$.
4. Hence $S_1 R'_k v_T = -(q+1) (S_{k-1} \cdots S_4)(S_3 v_T) = 0$.

Per-tableau application: $R'_k v_{T'} \in V_-$ for any α-SYT $T'$ and any $k \ge 4$. This is the **per-tableau L_α**, used in L_β and L_γ proofs.

### L_β (FULLY PROVED)

Key support lemma **SL_β**: for β-SYT $T$, $S_3 (S_8 \cdots S_3) v_T = 0$.

Proof: $S_3 (S_8 \cdots S_3) = (S_8 S_7 S_6 S_5)(S_3 S_4 S_3)$ by commutation. By case analysis on the position of 3, 4 in $T$ (subcases β1, β1', β2), $(S_3 S_4 S_3) v_T$ is supported on $\{T, s_3 T\}$ — both of which preserve the β-condition (5, 6 stacked in col 1). Hence $S_5$ kills.

This gives **$\pi_+(R'_9 v_T) \in V_+^\alpha$** for β-SYT, then L_α per-tableau closes L_β.

### L_γ (STRUCTURAL REDUCTION + COMPUTATIONAL VERIFICATION)

The structure parallels L_β with one more level:
1. **Sub-lemma B** (proved): For β-SYT $T'$, $\pi_+(R'_8 v_{T'}) \in V_+^\alpha$. (Same SL_β-style argument with $R'_8$ instead of $R'_9$.)
2. **Lemma SL_γ** (NEEDS PROOF): For γ-SYT $T$, $\pi_+(R'_9 v_T) \in V_+^\alpha \oplus V_+^\beta$.

If SL_γ holds, the recursion goes:
- γ → R'_9 → V_+^α ⊕ V_+^β (by SL_γ)
- α-part → R'_8 → V_- (by L_α per-tableau)
- β-part → R'_8 → V_+^α ⊕ V_- (by sub-lemma B)
- the V_+^α residue → R'_7 → V_- (by L_α per-tableau)

So $R'_7 R'_8 R'_9 v_T \in V_-$, completing L_γ.

**Gap:** SL_γ — that $\pi_+(R'_9 v_T)$ for γ-SYT is supported on α ∪ β.
- Verified at generic $q$ for all 6 γ-only SYTs.
- The SL_β commutation route gives $S_3 (S_8 \cdots S_3) v_T = (S_8 S_7 S_6 S_5)(S_3 S_4 S_3) v_T$. For γ-SYT, $(S_3 S_4 S_3) v_T$ stays in γ-span (positions of 7, 8 preserved), but then $S_5$ doesn't generically kill (γ-condition is on 7, 8 not 5, 6). $S_7 v_T = 0$ is available but $S_7$ is "buried" in the leftmost factors of the chain.

A clean structural proof of SL_γ likely uses either:
1. A finer analysis of the γ-class invariance through the $S_5 \cdot S_6 \cdot S_7$ stretch.
2. An algebraic identity in $H_n(q)$ expressing $\pi_+(R'_9 v_T)$ for γ-SYT in terms of $S_7 v_T$.

## Files

- **Paper:** `~/projects/proofs/2026-05-19-col1-sc-discriminator-structural.tex` (5 pages, compiles to PDF)
- **Verification scripts:** `~/projects/scratch/2026-05-19-key-lemma-verify.py`, `2026-05-19-supports.py`, `2026-05-19-vplus-support.py`, `2026-05-19-gamma-structure.py`
- **Scratch notebook:** `~/projects/scratch/prove-2026-05-19-120800.md`

## What this means for the dichotomy program

The α and β cases of the column-1 SC discriminator now have clean algebraic-Hecke proofs. The structural reasoning generalises modularly:
- The decomposition $V = V_+ \oplus V_-$ as $T_1$-eigenspaces.
- The "$S_j$ for $j \ge 3$ preserves $V_+/V_-$" fact.
- The commutation $[S_1, S_j] = 0$ for $j \ge 3$, giving $S_1 R'_k = (S_{k-1} \cdots S_3) S_1 S_2 S_1$.

These ingredients are shape-independent. The α-condition kill comes from $S_3 v_T = 0$, β from a delicate `S_5$ kill in the $(S_3 S_4 S_3)$-supported piece, and γ presumably from a $S_7$ kill in deeper-nested chains.

The structural template should generalize to other shapes — but the empirical evidence from $(3,3,2), (4,3,1,1)$ shows the **specific** combinatorial discriminator is shape-dependent. What IS shape-independent is the **Hecke-algebraic framework**: identify the SC index $i$ in col 1 where the kill happens, show the partial product at the first-vanish stage lies in $\ker S_1$.

## Status as of writing

Forward direction: α (clean), β (clean), γ (recursive structure + finite computational completion). 6/6 γ-only SYTs verified at generic $q$.

Converse direction: 15/15 SR-nonzero SYTs verified at generic $q$.

Total: theorem proved structurally for α∪β; γ has a finite computational fill-in.

— Clio
