"""
Mosaics, flocks and migration  (Purbhoo, arXiv:0705.1184, "Puzzles, tableaux and mosaics").

EXACT GEOMETRY MODEL
--------------------
All mosaic edges point in one of six directions, at angles 0,30,60,90,120,150
(mod 180).  Purbhoo's two families are
    0-directions : 0, 60, 120      (edges of the equilateral triangles of "type 0")
    1-directions : 30, 90, 150     (edges of the equilateral triangles of "type 1")
A vertex is the integer 4-tuple (a,b,c,e) standing for the point

        a*u0 + b*u60 + c*u30 + e*u90          (u_t = unit vector at angle t).

This map Z^4 -> R^2 is INJECTIVE: writing x = a + b/2 + c*sqrt3/2 and
y = b*sqrt3/2 + c/2 + e, the irrational part of x gives c, that of y gives b,
and then the rational parts give a and e.  So vertices may be compared as
4-tuples, with no floating point anywhere.

Tiles (Purbhoo 2.4): unit equilateral triangle, unit square, unit rhombus with
angles 30/150.  In this model the triangles are the 0- and 1-triangles, and the
squares and rhombi are exactly the parallelograms spanned by one 0-direction and
one 1-direction -- square when the angle is 90, rhombus when it is 30 or 150.
"""
from fractions import Fraction
from math import cos, sin, pi, sqrt
from itertools import product

# ---------------------------------------------------------------- directions
def _dir(t):
    """unit vector at angle t (t a multiple of 30, 0<=t<360) as a 4-tuple"""
    base = {0:(1,0,0,0), 60:(0,1,0,0), 30:(0,0,1,0), 90:(0,0,0,1)}
    if t in base: return base[t]
    if t == 120: return (-1,1,0,0)      # u60 - u0
    if t == 150: return (0,0,-1,1)      # u90 - u30
    if 180 <= t < 360: return neg(_dir(t-180))
    raise ValueError(t)

def add(v,w): return (v[0]+w[0], v[1]+w[1], v[2]+w[2], v[3]+w[3])
def sub(v,w): return (v[0]-w[0], v[1]-w[1], v[2]-w[2], v[3]-w[3])
def neg(v):   return (-v[0],-v[1],-v[2],-v[3])
def smul(k,v):return (k*v[0], k*v[1], k*v[2], k*v[3])

ANGLES  = [0,30,60,90,120,150,180,210,240,270,300,330]
DIR     = {t:_dir(t) for t in ANGLES}
DIR2ANG = {v:t for t,v in DIR.items()}
ZERO_DIRS = [DIR[t] for t in (0,60,120)]     # 0-family, "positive" representatives
ONE_DIRS  = [DIR[t] for t in (30,90,150)]    # 1-family

SQRT3 = sqrt(3.0)
def xy(v):
    """float (x,y) -- used ONLY for sorting / drawing, never for equality"""
    a,b,c,e = v
    return (a + b/2 + c*SQRT3/2, b*SQRT3/2 + c/2 + e)

def key(v):
    """exact total order on vertices: by x then y.  (p+q*sqrt3)/2 comparisons."""
    a,b,c,e = v
    return (_surd(2*a+b, c), _surd(c+2*e, b))

class _surd(object):
    """exact p + q*sqrt(3), ordered"""
    __slots__ = ('p','q')
    def __init__(self,p,q): self.p, self.q = p, q
    def __eq__(s,o): return s.p==o.p and s.q==o.q
    def __lt__(s,o):
        dp, dq = s.p-o.p, s.q-o.q
        if dq == 0: return dp < 0
        if dp <= 0 and dq < 0: return True
        if dp >= 0 and dq > 0: return False
        # dp and dq strictly opposite signs: compare dp^2 with 3 dq^2
        if dq > 0:            # dp < 0 < dq : sign of dp + dq sqrt3 = sign(3dq^2 - dp^2)
            return not (3*dq*dq > dp*dp)
        else:                 # dq < 0 < dp
            return 3*dq*dq > dp*dp
    def __le__(s,o): return s==o or s<o
    def __gt__(s,o): return not s<=o
    def __ge__(s,o): return not s<o
    def __hash__(s): return hash((s.p,s.q))
    def __repr__(s): return "%d+%d*r3" % (s.p,s.q)

# ---------------------------------------------------------------- tile types
# a tile is a tuple of vertices in counter-clockwise order.
TRI, SQUARE, RHOMB = 'T', 'S', 'R'

def tile_kind(tile):
    if len(tile) == 3: return TRI
    X = sub(tile[1], tile[0]); Y = sub(tile[3], tile[0])
    aX, aY = DIR2ANG[X], DIR2ANG[Y]
    return SQUARE if (aY-aX) % 180 == 90 else RHOMB

def _tri_shapes():
    """the four triangle shapes, as lists of CCW edge-vectors from a base vertex"""
    out = []
    for (p,q) in ((0,60),(30,90)):            # 0-family, 1-family
        u, w = DIR[p], DIR[q]
        out.append((( 0,0,0,0), u, w))                       # 'up'
        out.append((u, add(u,w), w))                         # 'down'
    return out

def _par_shapes():
    out = []
    for X in ZERO_DIRS:
        for Y in ONE_DIRS:
            aX, aY = DIR2ANG[X], DIR2ANG[Y]
            if aX < aY: A, B = X, Y
            else:       A, B = Y, X
            out.append(((0,0,0,0), A, add(A,B), B))
    return out

SHAPES = _tri_shapes() + _par_shapes()        # 4 triangles + 9 parallelograms

def canon(tile):
    """canonical representative of a tile: CCW cycle started at its minimal vertex"""
    n = len(tile)
    if cross_sign(sub(tile[1],tile[0]), sub(tile[-1],tile[0])) < 0:
        tile = (tile[0],) + tuple(reversed(tile[1:]))
    i = min(range(n), key=lambda k: key(tile[k]))
    return tuple(tile[(i+k) % n] for k in range(n))

def place(shape, v):
    return canon(tuple(add(v, s) for s in shape))

def tiles_through_edge(v, w):
    """all tiles whose CCW boundary contains the directed edge v->w"""
    out = []
    d = sub(w, v)
    if d not in DIR2ANG: return out
    for sh in SHAPES:
        n = len(sh)
        for i in range(n):
            if sub(sh[(i+1) % n], sh[i]) == d:
                out.append(place(sh, sub(v, sh[i])))
    return out

def area(tile):
    k = tile_kind(tile)
    if k == TRI:    return Fraction(0)       # sqrt3/4 each -- handled separately
    return Fraction(1) if k == SQUARE else Fraction(1,2)

def area_pair(tile):
    """exact area as (rational, coeff of sqrt3): tri = sqrt3/4, square = 1, rhomb = 1/2"""
    k = tile_kind(tile)
    if k == TRI:    return (Fraction(0), Fraction(1,4))
    if k == SQUARE: return (Fraction(1), Fraction(0))
    return (Fraction(1,2), Fraction(0))

# ---------------------------------------------------------------- the hexagon
def hexagon(n, d):
    """Purbhoo 2.4: hexagon A'AB'BC'C, clockwise, angles 150 at A,B,C and 90 at
    A',B',C', |A'A|=|B'B|=|C'C|=d, |AB'|=|BC'|=|CA'|=n-d.  A at the origin,
    E_A = u0, N_A = u150.  Returns (vertices clockwise, dict of nest data)."""
    m = n - d
    A  = (0,0,0,0)
    Ap = smul(d, DIR[0])                       # A + d*E_A
    Bp = smul(m, DIR[150])                     # A + (n-d)*N_A
    B  = add(Bp, smul(d, DIR[60]))
    Cp = add(B,  smul(m, DIR[30]))
    C  = add(Cp, smul(d, DIR[300]))
    assert add(C, smul(m, DIR[270])) == Ap, "hexagon does not close"
    verts = [Ap, A, Bp, B, Cp, C]              # clockwise
    nests = {
        'A': dict(corner=A, E=DIR[0],   N=DIR[150]),
        'B': dict(corner=B, E=DIR[240], N=DIR[30]),
        'C': dict(corner=C, E=DIR[120], N=DIR[270]),
    }
    return verts, nests

# ---------------------------------------------------------------- tiling search
def _boundary_of_polygon(verts_cw):
    """directed edges with the INTERIOR on the left: reverse the clockwise cycle,
    and subdivide into unit steps."""
    edges = []
    n = len(verts_cw)
    cyc = list(reversed(verts_cw))             # now counter-clockwise
    for i in range(n):
        v, w = cyc[i], cyc[(i+1) % n]
        step = sub(w, v)
        # step is k * unit; find k
        for t in ANGLES:
            u = DIR[t]
            for k in range(1, 40):
                if smul(k, u) == step:
                    for j in range(k):
                        edges.append((add(v, smul(j,u)), add(v, smul(j+1,u))))
                    break
            else:
                continue
            break
        else:
            raise ValueError("edge %s not a lattice multiple" % (step,))
    return edges

def tilings(verts_cw, forced=(), limit=None, allowed_rhombi=None):
    """all tilings of the polygon by mosaic pieces.  `forced` is a collection of
    tiles that must be present (used to pin down the nest contents)."""
    out = []
    inside = inside_tester(verts_cw)
    bd = {}
    for e in _boundary_of_polygon(verts_cw):
        bd[e] = bd.get(e, 0) + 1

    def rm(bd, tile):
        """return new boundary after removing `tile` from the uncovered region,
        or None if the tile does not fit"""
        nb = dict(bd)
        n = len(tile)
        for i in range(n):
            p, q = tile[i], tile[(i+1) % n]
            if nb.get((q,p), 0) > 0:           # tile would stick out across (p,q)
                return None
        for i in range(n):
            p, q = tile[i], tile[(i+1) % n]
            if nb.get((p,q), 0) > 0:
                nb[(p,q)] -= 1
                if nb[(p,q)] == 0: del nb[(p,q)]
            else:
                nb[(q,p)] = nb.get((q,p), 0) + 1
        return nb

    for t in forced:
        bd = rm(bd, t)
        if bd is None: raise ValueError("forced tile does not fit: %r" % (t,))

    placed = list(forced)
    def rec(bd, placed):
        if limit is not None and len(out) >= limit: return
        if not bd:
            out.append(tuple(sorted(placed)))
            return
        v = min((e[0] for e in bd), key=key)
        w = next(e[1] for e in bd if e[0] == v)
        for tile in tiles_through_edge(v, w):
            if not all(inside(z) for z in tile): continue
            if allowed_rhombi is not None and tile_kind(tile) == RHOMB \
               and tile not in allowed_rhombi: continue
            nb = rm(bd, tile)
            if nb is not None:
                placed.append(tile)
                rec(nb, placed)
                placed.pop()
    rec(bd, placed)
    return out

# ---------------------------------------------------------------- exact predicates
def _sign_surd(P, Q):
    """sign of P + Q*sqrt(3), P,Q integers"""
    if Q == 0: return (P > 0) - (P < 0)
    if P == 0: return (Q > 0) - (Q < 0)
    if P > 0 and Q > 0: return 1
    if P < 0 and Q < 0: return -1
    # opposite signs: compare P^2 with 3Q^2
    c = (P*P > 3*Q*Q)
    if P > 0: return 1 if c else -1
    else:     return -1 if c else 1

def cross_sign(u, v):
    """sign of the cross product u x v, for 4-tuple vectors (exact)"""
    pu, qu = 2*u[0]+u[1], u[2]
    ru, su = u[2]+2*u[3], u[1]
    pv, qv = 2*v[0]+v[1], v[2]
    rv, sv = v[2]+2*v[3], v[1]
    P = pu*rv + 3*qu*sv - pv*ru - 3*qv*su
    Q = pu*sv + qu*rv - pv*su - qv*ru
    return _sign_surd(P, Q)

def inside_tester(verts_cw):
    """closed-convex-polygon membership test (hexagon is convex)"""
    ccw = list(reversed(verts_cw))
    edges = [(ccw[i], sub(ccw[(i+1) % len(ccw)], ccw[i])) for i in range(len(ccw))]
    def inside(z):
        return all(cross_sign(e, sub(z, a)) >= 0 for a, e in edges)
    return inside

# ---------------------------------------------------------------- mosaics
def nest_cell(nest, i, j):
    """the rhombus at position (i,j) of the nest (i along E, j along N)"""
    c, E, N = nest['corner'], nest['E'], nest['N']
    v = add(c, add(smul(i,E), smul(j,N)))
    tile = (v, add(v,E), add(v, add(E,N)), add(v,N))
    # put in CCW order
    return canon(tile)

def nest_index(n, d):
    """dict  tile -> (nest name, i, j)  for every legal nest rhombus position"""
    _, nests = hexagon(n, d)
    idx = {}
    for name, nest in nests.items():
        for i in range(d):
            for j in range(n-d):
                idx[nest_cell(nest, i, j)] = (name, i, j)
    return idx, nests

def _cells_to_partition(cells, transpose=False):
    """cells = set of (i,j); return the partition if it is a Young diagram else None"""
    if transpose: cells = {(j,i) for (i,j) in cells}
    rows = {}
    for (i,j) in cells: rows[i] = rows.get(i,0) + 1
    if not rows: return ()
    m = max(rows)
    lam = [rows.get(i,0) for i in range(m+1)]
    if any(lam[k] < lam[k+1] for k in range(len(lam)-1)): return None
    # also require each row to be an initial segment
    for i in rows:
        if {j for (a,j) in cells if a==i} != set(range(rows[i])): return None
    return tuple(lam)

def mosaics(n, d, verbose=False):
    """all mosaics of size (n,d), each returned as (tiles, (alpha,beta,gamma))
    where alpha,beta,gamma are the partitions in nests A,B,C."""
    verts, nests = hexagon(n, d)
    idx, _ = nest_index(n, d)
    out = []
    for T in tilings(verts):
        cells = {'A':set(), 'B':set(), 'C':set()}
        ok = True
        for t in T:
            if tile_kind(t) != RHOMB: continue
            if t not in idx: ok = False; break
            name, i, j = idx[t]
            cells[name].add((i,j))
        if not ok: continue
        parts = {}
        for name in 'ABC':
            p = _cells_to_partition(cells[name])
            if p is None: ok = False; break
            parts[name] = p
        if ok:
            out.append((T, (parts['A'], parts['B'], parts['C'])))
    return out

def _diagram(part):
    return {(i,j) for i,p in enumerate(part) for j in range(p)}

def mosaics_with_boundary(n, d, alpha, beta, gamma, limit=None):
    """all mosaics whose nests A,B,C carry exactly the partitions alpha,beta,gamma.
    Convention: part k of the partition is the number of cells (k,j), j along N."""
    verts, nests = hexagon(n, d)
    forced = []
    for name, part in (('A',alpha), ('B',beta), ('C',gamma)):
        for (i,j) in _diagram(part):
            if i >= d or j >= n-d: return []
            forced.append(nest_cell(nests[name], i, j))
    allowed = set(forced)
    return tilings(verts, forced=tuple(forced), limit=limit, allowed_rhombi=allowed)

# ---------------------------------------------------------------- frames
def dot_surd(v, w):
    """exact 4*<v,w> as (P,Q) meaning P + Q*sqrt(3)"""
    pv, qv = 2*v[0]+v[1], v[2]
    rv, sv = v[2]+2*v[3], v[1]
    pw, qw = 2*w[0]+w[1], w[2]
    rw, sw = w[2]+2*w[3], w[1]
    P = pv*pw + 3*qv*qw + rv*rw + 3*sv*sw
    Q = pv*qw + qv*pw + rv*sw + sv*rw
    return (P, Q)

def cmp_along(theta):
    """comparison of vertices by their coordinate along direction theta (exact)"""
    u = DIR[theta % 360]
    def f(v):
        return dot_surd(v, u)
    def lt(v, w):
        P, Q = dot_surd(sub(v,w), u)
        return _sign_surd(P, Q) < 0
    return f, lt

def surd_lt(a, b): return _sign_surd(a[0]-b[0], a[1]-b[1]) < 0
def surd_le(a, b): return _sign_surd(a[0]-b[0], a[1]-b[1]) <= 0

# 120-degree rotation, as an integer matrix on 4-tuples:
#   u0 -> u120, u60 -> u180 = -u0, u30 -> u150, u90 -> u270 = -u30
def rot120(v):
    a,b,c,e = v
    return (-a-b, a, -c-e, c)
def rot240(v):
    return rot120(rot120(v))

def _frac_tuple(v):  return tuple(Fraction(x) for x in v)
def _rot_about(f, verts_sum, k, v):
    """apply the rotation f about the centroid (verts_sum/k) -- exact, Fractions"""
    c  = tuple(Fraction(x, k) for x in verts_sum)
    w  = tuple(a-b for a,b in zip(_frac_tuple(v), c))
    fw = f(w)
    r  = tuple(a+b for a,b in zip(fw, c))
    assert all(x.denominator == 1 for x in r), "rotation left the lattice: %r" % (r,)
    return tuple(int(x) for x in r)

# ---------------------------------------------------------------- hexagon finder
def boundary_edges(tileset):
    """directed edges with the region on the left, after cancellation"""
    bd = {}
    for t in tileset:
        n = len(t)
        for i in range(n):
            p, q = t[i], t[(i+1) % n]
            if bd.get((q,p), 0) > 0:
                bd[(q,p)] -= 1
                if bd[(q,p)] == 0: del bd[(q,p)]
            else:
                bd[(p,q)] = bd.get((p,q), 0) + 1
    return bd

def is_hexagon(bd):
    """boundary is a single closed cycle of exactly 6 unit edges"""
    if len(bd) != 6 or any(v != 1 for v in bd.values()): return None
    nxt = {p:q for (p,q) in bd}
    if len(nxt) != 6: return None
    start = next(iter(nxt)); cyc=[start]; cur = nxt[start]
    while cur != start:
        if cur not in nxt: return None
        cyc.append(cur); cur = nxt[cur]
        if len(cyc) > 6: return None
    return cyc if len(cyc) == 6 else None
