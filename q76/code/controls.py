"""controls.py -- the checks whose variation is named IN ADVANCE.

C1 (trivial kernel):  e = e' must give the zero matrix.
C2 (antisymmetry):    swapping e <-> e' must negate every entry.
C3 (height convention, NC3 of the Q75 paper): replacing h by rows (= h+1) in the
    abacus operator must BREAK the closed form.  If it does not, the check is blind.
C4 (cut reading):     [b+e in B] must equal "the ribbon steps UP between cells e and e+1",
    reading the ribbon's cells from its bottom-left end.  Checked on Young diagrams,
    with no reference to beta-numbers.
C5 (witness family):  lam = empty, mu = (e', 1^e) has entry exactly t^{e-1}(1+t).
"""
import sys, itertools, sympy as sp
sys.path.insert(0, '.')
sys.path.insert(0, '/home/clio/projects/probes/2026-09-03-Q75')
from closedform import commutator_brute, predict
from abacus import t, beta, unbeta, R_abacus, parts_of, trim
from symfunc import boxes, shape_stats, contains

# ---- C1, C2 -----------------------------------------------------------------
c1 = c1bad = c2 = c2bad = 0
for n in range(0, 7):
    for lam in parts_of(n):
        for e in range(2, 6):
            L = n + 2 * e + 6
            br = commutator_brute(lam, e, e, L)
            c1 += 1
            if any(sp.expand(v) != 0 for v in br.values()): c1bad += 1
        for (e, ep) in itertools.combinations(range(2, 6), 2):
            L = n + e + ep + 6
            f = commutator_brute(lam, e, ep, L); g = commutator_brute(lam, ep, e, L)
            for mu in set(f) | set(g):
                c2 += 1
                if sp.expand(f.get(mu, 0) + g.get(mu, 0)) != 0: c2bad += 1
print(f'C1  e=e\' gives 0:            {c1-c1bad}/{c1} configurations')
print(f'C2  antisymmetry in (e,e\'):  {c2-c2bad}/{c2} entries')

# ---- C3: perturbed height ---------------------------------------------------
def R_bad(lam, e, L):
    B = set(beta(lam, L)); out = {}
    for b in sorted(B):
        if b + e in B: continue
        h = 1 + sum(1 for c in B if b < c < b + e)      # rows, not rows-1
        mu = unbeta((B - {b}) | {b + e}, L)
        out[mu] = out.get(mu, 0) + t**h
    return out
def comm_bad(lam, e, ep, L):
    out = {}
    for sgn, (a, b) in ((1, (ep, e)), (-1, (e, ep))):
        for nu, w1 in R_bad(lam, a, L).items():
            for mu, w2 in R_bad(nu, b, L).items():
                out[mu] = sp.expand(out.get(mu, 0) + sgn * w1 * w2)
    return out
c3 = c3fires = 0
for n in range(0, 6):
    for lam in parts_of(n):
        for (e, ep) in itertools.combinations(range(2, 6), 2):
            L = n + e + ep + 6
            bb = comm_bad(lam, e, ep, L)
            for mu in set(bb) | set(parts_of(n + e + ep)):
                c3 += 1
                if sp.expand(bb.get(mu, 0) - predict(lam, mu, e, ep, L)) != 0: c3fires += 1
print(f'C3  perturbed height h->h+1 DISAGREES with the closed form: {c3fires}/{c3} entries')

# ---- C4: the cut reading, on Young diagrams only ----------------------------
def ribbon_cells_in_order(mu, lam):
    """cells of a ribbon mu/lam, from the bottom-left end to the top-right end."""
    cs = set(boxes(mu, lam))
    start = max(cs, key=lambda rc: (rc[0], -rc[1]))     # lowest row, then leftmost
    order = [start]; cur = start
    while len(order) < len(cs):
        r, c = cur
        nxt = (r, c + 1) if (r, c + 1) in cs else (r - 1, c)
        assert nxt in cs, (mu, lam, order)
        order.append(nxt); cur = nxt
    return order
c4 = c4bad = 0
for n in range(0, 7):
    for lam in parts_of(n):
        for (e, ep) in itertools.combinations(range(2, 6), 2):
            L = n + e + ep + 6; N = e + ep
            B = set(beta(lam, L))
            for mu in parts_of(n + N):
                if not contains(mu, lam): continue
                comp, h, sq = shape_stats(mu, lam)
                if comp != 1 or sq: continue                # must be an N-ribbon
                order = ribbon_cells_in_order(mu, lam)
                b = (B - set(beta(mu, L))).pop()
                for k in (e, ep):
                    up = order[k][1] == order[k - 1][1]     # same column => steps up
                    c4 += 1
                    if up != (b + k in B): c4bad += 1
print(f'C4  "[b+k in B] == ribbon steps up between cells k,k+1": {c4-c4bad}/{c4}')

# ---- C5: the witness family -------------------------------------------------
ok = []
for (e, ep) in itertools.combinations(range(2, 9), 2):
    L = e + ep + 6
    mu = trim((ep,) + (1,) * e)
    got = sp.expand(commutator_brute((), e, ep, L).get(mu, 0))
    ok.append((e, ep, got, sp.expand(got - t**(e - 1) * (1 + t)) == 0))
print(f'C5  lam=(), mu=(e\',1^e) entry = t^(e-1)(1+t): {sum(x[3] for x in ok)}/{len(ok)} pairs')
print('    sample:', [(e, ep, str(g)) for e, ep, g, _ in ok[:4]])
