"""mechanism.py -- WHY does m_shape collapse to 1 on the commutator?
Claim: for two bead hops b->b+e, c->c+e' with b,c distinct beads,
   intervals CROSS  <=>  mu/lam is CONNECTED (and then it has a 2x2)
   intervals disjoint or NESTED  <=>  mu/lam has 2 components (and no 2x2)
and the commutator kills exactly the non-crossing ones (Q76 Thm (ii)).
So the component statistic is constant on the commutator's support BY CONSTRUCTION.
"""
import sys, itertools, sympy as sp
sys.path.insert(0, '.'); sys.path.insert(0, '/home/clio/projects/probes/2026-09-04-Q76')
sys.path.insert(0, '/home/clio/projects/probes/2026-09-03-Q75')
from abacus import t, beta, unbeta, parts_of, trim
from symfunc import shape_stats

tab = {}
for n in range(0, 7):
    for lam in parts_of(n):
        for (e, ep) in itertools.combinations(range(2, 6), 2):
            L = n + e + ep + 6
            B = set(beta(lam, L))
            for b in sorted(B):
                if b + e in B: continue
                B1 = (B - {b}) | {b + e}
                for c in sorted(B1):
                    if c == b + e: continue         # same bead moving again
                    if c + ep in B1: continue
                    B2 = (B1 - {c}) | {c + ep}
                    if len(B - B2) != 2: continue   # want two distinct vacated sites
                    mu = unbeta(B2, L)
                    m, h, sq = shape_stats(mu, lam)
                    I, J = (b, b + e), (c, c + ep)
                    lo, hi = (I, J) if I[0] < J[0] else (J, I)
                    if hi[0] >= lo[1]:   rel = 'disjoint'
                    elif hi[1] <= lo[1]: rel = 'nested'
                    else:                rel = 'crossing'
                    tab[(rel, m, sq)] = tab.get((rel, m, sq), 0) + 1
print('(interval relation, #components of mu/lam, has 2x2) -> count')
for k in sorted(tab, key=str): print('  ', k, tab[k])
