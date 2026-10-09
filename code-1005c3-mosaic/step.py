"""One migration step, with every choice made explicit and every ambiguity logged.

Purbhoo 3.1 prescribes: the smallest hexagon containing the rhombus and lying
entirely weakly right of its leftmost point, rotated 180 (2-fold) or 120 (3-fold).
Three facts from the paper constrain the choice, and are used here as filters:
  (P1) the rhombus "moves roughly to the right (although sometimes it moves
       strictly vertically)"  -> the frame-x coordinate never decreases;
  (P2) the wake of the rhombus is a PATH from its initial to its final position
       (section 4) -> a position is never revisited inside one journey;
  (P3) after a 3-fold rotation "some edge of the rhombus ends up exactly
       horizontal, or exactly vertical" -> used as a tie-break.
"""
import sys
sys.path.insert(0,'.')
from mosaic import *
from mosaic import _rot_about, _sign_surd
from migrate import (adj_map, _connected_supersets, is_convex, hexagon_symmetry)

STATS = dict(steps=0, ambiguous=0, p3_decided=0, p3_silent=0, p3_both=0,
             multi_hexagon=0)

def candidate_moves(tiles, diamond, theta, visited):
    """all (new tiles, new diamond, kind) reachable in one legal step"""
    u = DIR[theta % 360]
    L = None
    for v in diamond:
        s = dot_surd(v, u)
        if L is None or surd_lt(s, L): L = s
    ok = [t for t in tiles if all(surd_le(L, dot_surd(v, u)) for v in t)]
    am = adj_map(ok)
    hexes = []
    for size in range(1, 6):
        for S in _connected_supersets(diamond, am, size):
            cyc = is_hexagon(boundary_edges(S))
            if cyc and is_convex(cyc) and hexagon_symmetry(cyc):
                hexes.append((size+1, S, cyc, hexagon_symmetry(cyc)))
        if hexes: break                       # smallest size only
    if len(hexes) > 1: STATS['multi_hexagon'] += 1

    def prog(tile):
        P = Q = 0
        for v in tile:
            p, q = dot_surd(v, u); P += p; Q += q
        return (P, Q)
    cur = prog(diamond)

    out = []
    for (_, S, cyc, sym) in hexes:
        ssum = [sum(v[k] for v in cyc) for k in range(4)]
        rots = [(lambda z: neg(z), 'a')] if sym == '2' else [(rot120,'b'), (rot240,'b')]
        for f, kind in rots:
            newS, newD = [], None
            for t in S:
                nt = canon(tuple(_rot_about(f, ssum, 6, v) for v in t))
                newS.append(nt)
                if t == diamond: newD = nt
            p = prog(newD)
            if _sign_surd(p[0]-cur[0], p[1]-cur[1]) < 0: continue      # (P1)
            if newD in visited: continue                               # (P2)
            dirs = [DIR2ANG[sub(newD[(i+1)%4], newD[i])] for i in range(4)]
            hv = any((a-theta) % 180 in (0, 90) for a in dirs)
            out.append((tuple(newS), newD, kind, hv, p, S))
    return out

def one_step(tiles, diamond, theta, visited):
    cand = candidate_moves(tiles, diamond, theta, visited)
    STATS['steps'] += 1
    if not cand: return None
    if len(cand) == 1:
        STATS['p3_silent'] += 1
        c = cand[0]
    else:
        hv = [c for c in cand if c[3]]
        if len(hv) == 1:
            STATS['p3_decided'] += 1; c = hv[0]
        else:
            STATS['ambiguous'] += 1
            if len(hv) > 1: STATS['p3_both'] += 1
            pool = hv if hv else cand
            c = max(pool, key=lambda z: (z[4][0] + 2*z[4][1]))
    tl = set(tiles) - set(c[5]) | set(c[0])
    return tl, c[1], c[2]

def journey2(tiles, diamond, theta, target_cells, maxsteps=400):
    tl = set(tiles); cur = diamond; visited = {diamond}
    steps = 0; kinds = []
    while cur not in target_cells:
        r = one_step(tl, cur, theta, visited)
        if r is None: raise RuntimeError("stuck after %d steps" % steps)
        tl, cur, kind = r
        visited.add(cur); steps += 1; kinds.append(kind)
        if steps > maxsteps: raise RuntimeError("journey too long")
    return tl, cur, steps, ''.join(kinds)
