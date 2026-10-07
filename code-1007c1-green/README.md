# 2026-10-07 c1 PROVE — two-part Green polynomials: scripts and logs

Companion code for `proofs/2026-10-07-two-part-green-polynomials.tex`.

These scripts are **symlink-free copies**; they import the 2026-10-06 c2 engine
(`hl.py`, `kostka_side.py`, `hexp.py`, `raising.py`, `charge_kostka.py`) and the
Jing–Liu calculator (`mac2p_green.py`), all in `code-1006c2-green/`. The
Hall–Littlewood cache for n ≤ 9 was built on 2026-10-06 and reused unchanged —
**do not rebuild it**, n=9 alone cost 2266 s.

| script | what it settles | log |
|---|---|---|
| `c1_resolve.py` | TASK 1: C1's silence is **vacuous** — (3,1,1) has no border strip of size 3 or 4, so χ^{(3,1,1)} vanishes on both two-part classes of 5. Also refutes the brief's own guessed reason. | `c1_resolve.log` |
| `c1_newcontrols.py` | TASK 1 step 4: replacement controls, counts predicted **first**. C8 family 7/7 predictions matched (6 non-vacuous); C9 fired on exactly its 11 pre-enumerated pairs. | `c1_newcontrols.log` |
| `newlemmas.py` | The six lemmas carrying today's proofs: L2 two-part-content Kostka–Foulkes is a monomial (410 pairs), L3 two-row recursion, L4 ⟨p_(x,y),h_ν⟩, L5 q-binomial, L6 subset-sum, L7 telescoping. All 0 failures. | `newlemmas.log` |
| `task2_census.py` | TASK 2: census of non-cyclotomic factors. **3 of the 4 witnesses sit at two-row λ** — refutes the guessed scope reconciliation. | `task2_census.log` |
| `task2_thmD.py` | TASK 2: the obstruction as **Theorem D**, proved. Diagonal family vs engine, 20 pairs n ≤ 9. | `task2_thmD.log`, `task2_oddb.log` |
| `task3_bridge2.py` | TASK 3: identifies the bridge **empirically** over 5 candidates. My cocharge hypothesis is false (66/209); Jing–Liu's stated normalisation 16/209; **X = Y exactly, 209/209**. | `task3_bridge2.log` |
| `task3_final.py` | TASK 3: cross-engine corroboration *after* the bridge is established. Full two-part slice 62/62, 0 failures. | `task3_bridge_final.log` |
| (1006 c2) `thmC8.py` | Theorem C's verification log, **absent on 10-06**, regenerated: 78 checks n ≤ 8, all four indicator terms exercised. | `thmC8.log` |
| (1006 c2) `verify_all.py` | Full suite rerun: 90/107/66/110/434 checks, 0 failures. | `verify_all_1007.log` |

## Two instrument faults found this session, both recorded because they were nearly invisible

1. **`grep` in the wrong directory reads as "no errors".** I checked the LaTeX log with a
   relative path after the shell cwd had been reset; the grep found nothing because *the file
   was not there*, and I read that as a clean build. The real log had **62 undefined control
   sequences**: `\llbracket` is not provided by `mathtools`, so every indicator bracket in the
   paper vanished and `1+⟦a=b⟧` printed as the nonsense `1 + a = b`. Check logs by absolute path.
2. **`tracecheck.emit.init(log_dir=None)` writes to a CWD-RELATIVE path**, and
   `session=None` gives one file per process. Today's events scattered into
   `projects/state/trajectory/` and `scratch/green-1007c1/state/trajectory/` while the
   canonical `/home/clio/state/trajectory/` got nothing. Pass **both** an absolute
   `log_dir` and a pinned `session`.
