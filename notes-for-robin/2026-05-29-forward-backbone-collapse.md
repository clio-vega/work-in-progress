# Forward backbone collapse for off-hook (2,2,1^m) — prove session 2026-05-29

**Paper:** `~/projects/proofs/2026-05-29-forward-backbone-collapse.tex` (6 pp, compiles).
**Target:** strong per-subset OPERATOR vanishing M(S)≡0 on V^λ for |S|<D=C(m,2),
λ=(2,2,1^m) (PROVE.md, 2026-05-29 seed). **Partial success** — a clean, m-uniform
structural backbone proved; the full |S|<D bound NOT closed (residual precisely isolated).

## The one thing I'd want you to check

**Proposition (backbone line, fully rigorous, uniform in m≥1).**
The all-P_q staircase prefix through block B_4 (= the S_4-staircase Π_{S_4} on T_1,T_2,T_3)
has image exactly the single seminormal basis line ⟨v_{T_0}⟩, where T_0 has rows (1,2),(3,4)
and column (5,6,...,n). Moreover v_{T_0} ∈ E_1^+ ∩ E_3^+ ∩ ⋂_{i=5}^{n-1} E_i^-.

Proof in three m-uniform moves:
1. **Branching cut.** V^λ↓S_4 has only μ⊢4 with μ_1≤2 (since λ_1=2): {(2,2),(2,1,1),(1^4)}.
   Π_{S_4} (a C[S_4] element) acts block-diagonally; it kills the τ≥1 constituents
   (2,1,1)[τ=1], (1^4)[τ=3] (degenerate-monodromy operator-vanishing; here a finite exact
   check on dim-3 and dim-1 modules). So im Π_{S_4} ⊆ V^{(2,2)}-isotypic.
2. **E_1^+ pin.** Leftmost factor of Π_{S_4} is P_q^{(1)} ⟹ image ⊆ E_1^+. The (2,2)-isotypic
   is 2-dim (mult c_{(2,2)}=f^{λ/(2,2)}=f^{(1^m)}=1); within it E_1^+ (= "1,2 same row")
   selects exactly v_{T_0}. So image ⊆ ⟨v_{T_0}⟩, and =⟨v_{T_0}⟩ since rank≥1 (τ((2,2))=0).
3. **Tail eigenvalues.** 5,6,...,n in column 0 of T_0 ⟹ v_{T_0} is a (−1)-eigenvector of
   every T_i, i≥5. Same-row pairs (1,2),(3,4) ⟹ q-eigenvector of T_1,T_3.

This is the rigorous explanation of the EMPIRICAL "collapse born at a fixed block,
independent of m" (offhook-killpoint-mechanism): the collapse is born on ⟨v_{T_0}⟩ and dies
at T_{|λ̂|+1}=T_5, whose first appearance is the head of B_6 at word-position C(5,2)=10 — all
three facts m-independent.

## What's proved vs not

PROVED (uniform in m):
- Backbone line (above).
- No-head reduction: for S∩{head positions 0..5}=∅, M(S)≡0 ⟺ M_tail(S)v_{T_0}=0 — operator
  vanishing becomes a SINGLE-VECTOR reach for the concrete v_{T_0}∈⋂_{i≥5}E_i^-.
- M(∅)≡0 (|S|=0): forward localisation to (position 10, eigenspace E_5^-); the bare
  conclusion was already secured by the backward Pillar-1 proof (omega-zero-on-V-lambda).

VERIFIED, not yet m-uniformly proved:
- The B_5 passage Π_{B_5}v_{T_0}∈E_5^- (so T_5 at head of B_6 kills) — exact for m=2,3,4,5.
  My slick guess P_q^{(5)}P_q^{(4)}v_{T_0}=0 is FALSE; the full P_q^{(1)}P_q^{(2)}P_q^{(3)}
  matters and I don't have a clean reason yet. (Not needed for M(∅)=0 itself — backward
  proof covers it — but needed for the forward story to be self-contained.)

RESIDUAL GAP (the real one):
- Head insertions. At m=3, of 111 head-touching subsets with |S|<3, 70 keep the head-image
  in ⋂_{i≥5}E_i^- (killer ladder applies) but **41 land "neither"** (head P_-1 knocks the
  image out of ⋂E_i^- without killing it). These still give M(S)≡0 but not by the clean
  mechanism — the operator-level twin of the OPEN merged-junction case in the 2026-05-27 arc
  paper. This is where the work is.

## Question for you
The killer-ladder counting wants: "budget to postpone past killer T_i grows like (i−4),
Σ_{i=5}^{n-1}(i−4)=C(m,2)=D." Is there a potential/Morse function on the image chain that
makes this an operator inequality (handling head insertions = merged arcs uniformly)? The
single-vector reach for v_{T_0} feels like the right reduced object; the within-arc reach is
proved, merged is not. Cf. offhook-within-arc-reach-proved, merged-junction-mechanism.

Scripts (exact rational, q=5/7, cross-checked q=2/3):
`~/projects/scratch/2026-05-29-killpoint/{imagechain,flag,backbone,reduce,genbackbone,headcheck}.py`.
