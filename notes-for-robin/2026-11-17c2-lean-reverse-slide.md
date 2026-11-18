# For Robin: G4 Lemma D half (i) is now formalised in both directions (LEAN 2026-11-17 c2)

`reverse_slide_eq_switch_product` in `TworowD4Kernel/SlideSwitchReverse.lean` (tworow-d4-kernel `785c955`) is sorry-free and uses only the standard three axioms.
It says that the reverse jdt slide ("larger of west/south") is the product of switches carrying F_j leftward past U_m, …, U_1, for every
diagram D and every standard U ++ [h]. With the forward theorem from this morning, the slide half of lem:D is done.
The parent node stays `proved`, not lean-verified: what remains is C3, the dictionary into `GrowthConfluence`.
Note: https://github.com/clio-vega/proofs/blob/main/2026-11-17c2-lean-reverse-slide.md (proofs commit e03b776).
