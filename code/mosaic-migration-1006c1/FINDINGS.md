# Phase 0 record — gap-vertical-step-orientation, 2026-10-06 c1

Clock: 04:58–05:09 (11 min of wall, ~45 min of brief budget allowed).
Status: **gap SHARPENED, not closed.** New sub-results below; Theorem 1 of the
migration paper still rests on an empirical null, but the null is now
*explained* rather than merely observed.

## 1. The two vertical steps are one picture (new, structural)

Enumerating all strictly vertical steps (vert.py) returns exactly **2**, and they
share the same hexagon region:

    H  = zonogon on {u0, u60, u150}, 4 tiles
       = R (+) [0,1]*u60     (Minkowski sum: the rhombus swept one unit
                              perpendicular to the travel direction u = u150)

H has exactly two tilings, swapped by the central symmetry, and the 180-degree
rotation translates the travelling rhombus by **+u60** (dphi = +1) or **-u60**
(dphi = -1).  So:

> **A strictly vertical migration step is a unit translation of the travelling
> rhombus perpendicular to the travel direction, by +-u60.**

phi(u60) = 1 and phi(tile) = (sum over vertices of (b+e))/4, so dphi = phi(u60) = +-1
immediately.

## 2. COROLLARY: no better potential can close this gap (new, and it is a theorem)

The two vertical steps are **mutually inverse**: the same hexagon, the same
rotation, the two tilings.  Hence for ANY function psi on rhombus positions,

    Delta psi (T+ -> T-)  =  - Delta psi (T- -> T+).

So no potential whatsoever assigns +1 to both.  **The gap is irreducible: it
cannot be removed by a better ansatz, only by a reachability argument.**  This
closes off the entire search direction "look for a different phi", which is what
I would otherwise have spent the session on.

## 3. Minimality does NOT discriminate (new, negative)

sizes.py enumerates every admissible local move for the canonical (0,150)
rhombus: **15 moves, every one with a 4-tile hexagon.**

    sym  progress  dphi  #tiles  count
    2    vertical  -1    4       1
    2    vertical  +1    4       1
    2    forward   +1    4       1
    3    backward  -1    4       6
    3    forward   +1    4       6

Since all candidate hexagons have 4 tiles, "the SMALLEST hexagon containing the
rhombus" cannot prefer the up-strip over the down-strip.  Purbhoo's minimality
clause is silent here.  (Consistent with the already-recorded finding that the
minimal hexagon is not unique: 1593 of 13541 steps.)

## 4. The geometric content of the asymmetry (new, sharp, unproved)

The 180-degree rotation maps the strip's rear end to its front end, so the two
strips differ in **where the square sits relative to travel**:

  * **up-slide** (dphi=+1) needs the square **behind** the rhombus (sigma-min end);
  * **down-slide** (dphi=-1) needs the square **ahead** of it (sigma-max end).

So the gap reduces to exactly this statement, which I could not prove:

> **(G)** In a mosaic, the travelling rhombus never has the configuration
> {square ahead-and-below, two triangles} occupying R - [0,1]*u60.

## 5. The empirical null, widened and EXPLAINED (new; this is the real gain)

Previously: 91 of 707 steps strictly vertical, all +1.  I widened the sweep to
(n,d) = (4,2),(5,2),(5,3),(6,3) -- **3111 steps** over 362 mosaics:

    steps whose chosen move was strictly vertical : 434
      dphi = +1 : 434
      dphi = -1 : 0

But the count alone was a trap.  step.py breaks a tie among equal-progress
candidates with `max(pool, key=progress)`, and progress is **constant** on
vertical candidates -- so `max` returns the first in list order.  Had the -1
slide ever been in the pool, 434/434 would have been an artifact of enumeration
order, not a geometric fact.  So I measured availability, not selection:

    steps where a vertical dphi = -1 candidate was AVAILABLE : 0   of 3111
    steps where a vertical dphi = +1 candidate was AVAILABLE : 434
    steps where BOTH were available                          : 0

**The silence is absence, not deselection.**  The tie-break is never consulted
on a vertical step, so the null is a statement about mosaic geometry.

## 6. Second premise, newly named (and it is also empirical)

classify.py -- the exhaustive classification underpinning Theorem 1 -- filters
on "exactly one rhombus in the hexagon".  step.py imposes no such restriction,
so I checked whether the engine takes steps the classification never covered:

    chosen steps                       : 3111
    bare-height dphi of chosen moves   : dphi = 1 for 3111 of 3111
    #rhombi in the chosen hexagon      : 1 for 3111 of 3111
    #tiles  in the chosen hexagon      : 4 for 3111 of 3111

So the classification does cover every chosen step here -- **but "the chosen
hexagon contains exactly one rhombus" is itself an empirical premise**, not a
consequence of the stated rule, and Theorem 1 needs it.  It was previously
implicit in classify.py's filter.  Name it:

> **(G2)** The minimal admissible hexagon of the travelling rhombus contains no
> other rhombus.                                   [3111/3111, unproved]

This matters because the candidate pool DID contain moves with bare-height
dphi = +-1/2 (173 each), i.e. moves for which the potential identity fails.  They
were always rejected.  Why they were rejected is being measured (p3.py).

Note also: no rhombus-type correction c_t is needed.  The bare height
phi = (sum of (b+e))/4 has dphi = 1 on every chosen step, all 3111.

## 7. Move repertoire of a journey (new, clarifying)

    kind=a (180 deg)  (0,150) -> (0,150) : 1130
    kind=a (180 deg)  (60,30) -> (60,30) :  696
    kind=b (120 deg)  (0,150) -> (60,30) : 1112
    kind=b (120 deg)  (60,30) -> (0,150) :  173

So a journey alternates between the two Prop-3.1 orientations via 3-fold
rotations, and slides within an orientation via 180-degree rotations.  Nest A's
cells have type (0,150) (spanned by E_A = u0, N_A = u150) and nest B's have type
(60,30) (spanned by E_B = u240, N_B = u30), as they must.

## What to write into the registry

`gap-vertical-step-orientation` stays **in-progress**, with the reason rewritten:
the gap is now two named unproved statements (G) and (G2), both empirical nulls
at 3111 steps / 362 mosaics, plus the proved fact that no choice of potential can
avoid them.  Theorem 1 of the migration paper must state (G) and (G2) as
hypotheses.
