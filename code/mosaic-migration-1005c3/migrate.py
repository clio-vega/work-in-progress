"""Migration (Purbhoo 3.1) with an exact step counter.

A journey of one rhombus is a sequence of hexagon rotations.  ell(M) is the TOTAL
number of hexagon rotations performed while migrating the whole flock.
"""
import sys
sys.path.insert(0,'.')
from mosaic import *
from mosaic import _rot_about, _sign_surd, _frac_tuple
from itertools import combinations

AMBIGUOUS = []
BACKWARD_A = []   # 2-fold moves that went backwards (should never happen)          # records any step where Purbhoo's h/v rule fails to decide

def adj_map(tiles):
    """vertex -> set of tiles containing it"""
    m = {}
    for t in tiles:
        for v in t: m.setdefault(v, set()).add(t)
    return m

def minimal_hexagon(tiles, diamond, theta):
    """smallest set S of tiles with diamond in S, every vertex weakly right of the
    leftmost point of `diamond` (right = direction theta), and boundary a hexagon."""
    u = DIR[theta % 360]
    L = min((dot_surd(v,u) for v in diamond), key=lambda s: (0,))  # placeholder
    L = None
    for v in diamond:
        s = dot_surd(v,u)
        if L is None or surd_lt(s, L): L = s
    ok_tiles = [t for t in tiles
                if all(surd_le(L, dot_surd(v,u)) for v in t)]
    assert diamond in ok_tiles
    am = adj_map(ok_tiles)
    pool = set(ok_tiles) - {diamond}
    for size in range(1, 6):
        # grow connected sets of `size` extra tiles around the diamond
        for S in _connected_supersets(diamond, am, size):
            bd = boundary_edges(S)
            cyc = is_hexagon(bd)
            if cyc is not None and is_convex(cyc) and hexagon_symmetry(cyc) is not None:
                return S, cyc
    return None, None

def _connected_supersets(diamond, am, size):
    """all tile sets of cardinality size+1 containing diamond, connected via
    shared vertices"""
    seen = set()
    frontier = [frozenset([diamond])]
    for _ in range(size):
        nxt = []
        for S in frontier:
            nbrs = set()
            for t in S:
                for v in t: nbrs |= am.get(v, set())
            for t in nbrs - S:
                T = S | {t}
                if T not in seen:
                    seen.add(T); nxt.append(T)
        frontier = nxt
    return [tuple(S) for S in frontier]

def is_convex(cyc):
    """all six turns in the same rotational sense, none straight"""
    n = len(cyc)
    es = [sub(cyc[(i+1) % n], cyc[i]) for i in range(n)]
    sg = [cross_sign(es[i], es[(i+1) % n]) for i in range(n)]
    return all(x > 0 for x in sg) or all(x < 0 for x in sg)

def hexagon_symmetry(cyc):
    """'2' if the hexagon is centrally symmetric, '3' if 3-fold, else None"""
    ssum = [sum(v[k] for v in cyc) for k in range(4)]
    V = set(cyc)
    def sym(f):
        try:    return all(_rot_about(f, ssum, 6, v) in V for v in cyc)
        except AssertionError: return False
    if sym(lambda z: neg(z)): return '2'
    if sym(rot120):           return '3'
    return None

def rotate_hexagon(S, cyc, diamond, theta):
    """return (new tile set, new diamond, kind) after the prescribed rotation"""
    vs = sorted(set(v for t in S for v in t), key=key)
    hexverts = cyc
    ssum = [sum(v[k] for v in hexverts) for k in range(4)]   # centroid * 6
    Vset = set(hexverts)

    def apply(f):
        newS, newD = [], None
        for t in S:
            nt = canon(tuple(_rot_about(f, ssum, 6, v) for v in t))
            newS.append(nt)
            if t == diamond: newD = nt
        return tuple(newS), newD

    # 2-fold?
    half = hexagon_symmetry(cyc) == '2'
    thr  = hexagon_symmetry(cyc) == '3'
    if half:
        newS, newD = apply(lambda z: neg(z))
        u = DIR[theta % 360]
        def pr(t):
            P=Q=0
            for v in t:
                p,q = dot_surd(v,u); P+=p; Q+=q
            return (P,Q)
        if _sign_surd(pr(newD)[0]-pr(diamond)[0], pr(newD)[1]-pr(diamond)[1]) < 0:
            BACKWARD_A.append(theta)
        return newS, newD, 'a'
    assert thr, "minimal hexagon is neither 2-fold nor 3-fold symmetric"
    u = DIR[theta % 360]
    def prog(tile):
        P = Q = 0
        for v in tile:
            p, q = dot_surd(v, u); P += p; Q += q
        return (P, Q)
    cur = prog(diamond)
    cands = []
    for f, nm in ((rot120,'R'), (rot240,'R2')):
        newS, newD = apply(f)
        cands.append((nm, newS, newD))
    # (1) Purbhoo: "the rhombus moves roughly to the right (although sometimes it
    #     moves strictly vertically)" -- so the displacement is weakly rightward.
    fwd = [c for c in cands
           if _sign_surd(prog(c[2])[0]-cur[0], prog(c[2])[1]-cur[1]) >= 0]
    # (2) tie-break: "some edge of the rhombus ends up exactly horizontal or
    #     exactly vertical" in the frame where migration points right.
    def hv(nd):
        dirs = [DIR2ANG[sub(nd[(i+1) % 4], nd[i])] for i in range(4)]
        return any((a - theta) % 180 in (0, 90) for a in dirs)
    pool = fwd if fwd else cands
    good = [c for c in pool if hv(c[2])]
    if len(good) == 1:
        return good[0][1], good[0][2], 'b'
    if len(pool) == 1:
        return pool[0][1], pool[0][2], 'b'
    AMBIGUOUS.append((theta, len(fwd), len(good)))
    best = max(pool, key=lambda z: prog(z[2])[0] + 2*prog(z[2])[1])
    return best[1], best[2], 'b'

def journey(tiles, diamond, theta, target_cells):
    """migrate one rhombus until it is packed in the target nest; return
    (new tiles, final rhombus, number of hexagon rotations, move-type string)"""
    steps = 0; kinds = []
    cur = diamond
    tl = set(tiles)
    while cur not in target_cells:
        S, cyc = minimal_hexagon(tl, cur, theta)
        if S is None:
            raise RuntimeError("no minimal hexagon found after %d steps" % steps)
        newS, newD, kind = rotate_hexagon(S, cyc, cur, theta)
        tl -= set(S); tl |= set(newS)
        cur = newD; steps += 1; kinds.append(kind)
        if steps > 200: raise RuntimeError("journey does not terminate")
    return tl, cur, steps, ''.join(kinds)

# ---------------------------------------------------------------- flocks
def flock_fillings(cells):
    """all LR-tableaux (Purbhoo 2.2) on a set of cells (a,b);  a = east, b = north.
      (i)  weakly increasing east->west : f(a,b) >= f(a+1,b)
      (ii) strictly increasing south->north : f(a,b+1) > f(a,b)
      (iii) reading word west->east, north->south is a reverse lattice word."""
    cells = set(cells)
    if not cells: return [{}]
    bmax = max(b for _,b in cells)
    order = sorted(cells, key=lambda c: (-c[1], c[0]))
    nmax = len(cells)
    out = []; T = {}; cnt = [0]*(nmax+2)
    def rec(k):
        if k == len(order): out.append(dict(T)); return
        (a,b) = order[k]
        for v in range(1, nmax+1):
            if v >= 2 and cnt[v-1]+1 > cnt[v-2]: continue      # lattice on tails
            if (a+1,b) in T and T[(a+1,b)] > v: continue       # (i)
            if (a,b+1) in T and T[(a,b+1)] <= v: continue      # (ii)
            if (a,b-1) in T and T[(a,b-1)] >= v: continue      # (ii)
            T[(a,b)] = v; cnt[v-1] += 1
            rec(k+1)
            cnt[v-1] -= 1; del T[(a,b)]
    rec(0)
    return out

ORIENTS = {'--': (-1,-1), '++': (1,1)}

def flock_of_nest(n, d, tiles, nest_name, sign=(-1,-1)):
    """the unique flock on all rhombi of the given nest, in orientation
    (sign0*E_nest, sign1*N_nest).  Returns [(tile, f, a, b), ...]."""
    idx, nests = nest_index(n, d)
    cells = {}
    for t in tiles:
        if tile_kind(t) != RHOMB: continue
        if t not in idx: raise ValueError("rhombus outside the nests")
        name, i, j = idx[t]
        if name == nest_name: cells[(i,j)] = t
    if not cells: return []
    ab = {}
    for (i,j), t in cells.items():
        ab[(sign[0]*i, sign[1]*j)] = t
    amin = min(a for a,_ in ab); bmin = min(b for _,b in ab)
    ab = {(a-amin, b-bmin): t for (a,b), t in ab.items()}
    fills = flock_fillings(set(ab))
    assert len(fills) == 1, "flock not unique: %d fillings" % len(fills)
    f = fills[0]
    return [(ab[c], f[c], c[0], c[1]) for c in ab]

def migrate_A_to_B(n, d, tiles, theta=150, count_only=True):
    """Corollary 3.2: orientation (-E_A,-N_A) on alpha, migrate south to nest B.
    Returns (ell, final tiles, list of (entry, a, steps, kinds))."""
    idx, nests = nest_index(n, d)
    target = {t for t,(nm,i,j) in idx.items() if nm == 'B'}
    fl = flock_of_nest(n, d, tiles, 'A', sign=(-1,-1))
    # standard order:  f, then west-to-east (west = smaller a).  South migration
    # processes from the MINIMAL element upwards.
    fl.sort(key=lambda z: (z[1], z[2]))
    tl = set(tiles); total = 0; detail = []
    for (t, val, a, b) in fl:
        tl, newt, steps, kinds = journey(tl, t, theta, target)
        total += steps
        detail.append((val, a, steps, kinds))
    return total, tl, detail

def nestA_rhombi(n, d, tiles):
    idx, nests = nest_index(n, d)
    out = []
    for t in tiles:
        if tile_kind(t) != RHOMB: continue
        if t not in idx: raise ValueError("rhombus outside the nests")
        nm, i, j = idx[t]
        if nm == 'A': out.append((t, i, j))
    return out

def migrate_order(n, d, tiles, order, theta=150):
    """migrate the listed nest-A rhombi, in the given order, to nest B.
    Returns (ell, final tiles, per-rhombus step counts) or raises."""
    idx, nests = nest_index(n, d)
    target = {t for t,(nm,i,j) in idx.items() if nm == 'B'}
    tl = set(tiles); total = 0; steps_each = []
    for t in order:
        tl, newt, steps, kinds = journey(tl, t, theta, target)
        total += steps; steps_each.append(steps)
    return total, tl, steps_each

def final_nestB_cells(n, d, tiles):
    idx, _ = nest_index(n, d)
    cells = []
    for t in tiles:
        if tile_kind(t) != RHOMB: continue
        if t not in idx: return None
        nm,i,j = idx[t]
        cells.append((nm,i,j))
    return sorted(cells)
