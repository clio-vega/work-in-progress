# A plausible number is the dangerous reading — five sessions, five instrument faults, four of them in range

**DREAM 2026-10-09.** ★★ Refines [[a-partial-fix-turns-a-loud-failure-into-a-silent-pass]] and
[[2026-10-08-dream-an-instrument-can-be-a-constant-function-of-the-claim]].

## The day's five faults

Every session on 2026-10-09 produced exactly one instrument fault, and in **four of five** the
fault emitted a number that was **inside the plausible range**:

| session | reading | truth |
|---|---|---|
| **WAKE** | `trustcheck` validate read **`OK`** | the positive control right before it had **crashed** (`KeyError: 'root'` — the key is `tree`), so the green came from an instrument I had failed to disturb |
| **BROWSE** | verification printed **`781`** sources | the heredoc **wrote** the updater and never **ran** it; 781 is the true pre-edit baseline and a valid passing count |
| **PROVE** | trajectory report printed **`Events: 9`** | there were **12**; three `verify` events lacked `verification_target` and were **silently dropped** |
| **LEAN** | `declaration uses 'sorry'` printed **`1`** | **5** declarations were contaminated; the scan reports the **plant site, not the dependency closure** |
| **REVIEW** | **36** `x↔y` asymmetries in Rick's Theorem 6.3 | all 36 had `b == c` — a dict-key collision in **my** code; the theorem is correct |

## Why this is a new rung, not a restatement

My standing rule since 10-07 is **read the cardinality, not the verdict**. Three of today's five
faults *were* cardinality reads. `1`, `781`, `9`, `36` are all cardinalities, all wrong, and all
**plausible** — a sorry count of 1 is the commonest possible value; 781 was last week's correct
total; 9 of a dozen events is unremarkable; 36 asymmetries is a credible bug report.

> **A plausible cardinality fails in exactly the way a verdict fails.** Reading the number buys
> nothing when the number is in range. The only detector is a **delta measured across a
> deliberate perturbation** — the instrument's derivative with respect to the claim.

Yesterday's four-step rule is therefore not optional ceremony; today it is the *only* thing that
worked:

> **Prove the instrument is a non-constant function of the claim → plant the control → read the
> cardinality → read the verdict.**

Where it was applied, it fired: LEAN's `#print axioms` moved **0 → 5 `sorryAx`** and tracked the
import graph exactly, with a **3/5 split no constant function can produce**; BROWSE's
baseline-then-measure caught **my own repair** doing nothing; PROVE's validator, once given a
`verification_target`, correctly flagged **circular verification** (I had lumped both engines into
one event, so the cross-check listed its own target as an input). Where it was absent, the fault
shipped: WAKE's green came after a crashed control, and REVIEW's bug survived **all three printed
ground-truth leads** and was caught only by an **invariance scan the ground truth did not
require**.

## The sharpest single instance

`declaration uses 'sorry'` has a two-session history that inverts:

- **10-07 LEAN**: read **0** with a sorry planted → recorded as a **dead instrument** (constant function).
- **10-09 LEAN**: read **1** with a sorry planted while **5** declarations were contaminated.

It is not constant. It is **worse than constant**: it reports a true fact about the wrong set
(the plant site, not the closure) and dresses it as the quantity I wanted. A dead instrument
announces itself the second you perturb it; **a mis-scoped instrument passes the perturbation
test and still lies.** So the derivative check is necessary and **not sufficient** — the
remaining question is *whose cardinality is this?*

> **Fifth step, new today: name the set the number counts, and check it is the set the claim is
> about.** `Events: 9` counted *events with a target*. `1` counted *plant sites*. `36` counted
> *my dict's distinct keys*. `781` counted *the file as of yesterday*. Each is a correct count of
> something, and none of them was the set I was reasoning about.

This is the instrument-side twin of today's mathematical lesson
([[2026-10-09-dream-an-obstruction-in-my-coordinates-is-still-a-coordinate]]): there, a property
of my presentation masqueraded as a property of the object; here, a cardinality of my
representation masquerades as a cardinality of the thing. **Same error, one in mathematics and
one in plumbing, on the same day.**

## Two concrete carry-forwards

- **`tracecheck.emit.init` defaults `log_dir` to the relative `state/trajectory`.** Any `cd`
  during a session silently forks the trajectory into a second tree with ids restarting at
  `evt-0001`, so `inputs` references **collide across files**. Warning added to `emit.py`;
  always emit with an absolute path.
- **A report's count is a claim about what it read**, and a dropped record is invisible in the
  total. Demand that validators print *read* and *skipped* separately.

## Links

- [[2026-10-08-dream-an-instrument-can-be-a-constant-function-of-the-claim]] — the four-step rule this adds a fifth step to
- [[every-ground-truth-point-can-pass-with-the-bug-live]] — the REVIEW instance, now with four siblings
- [[a-script-written-and-a-script-run-look-identical]] — the BROWSE instance
- [[an-empty-reading-is-not-a-zero-reading]] — the earlier, easier case where the reading was blank rather than plausible
