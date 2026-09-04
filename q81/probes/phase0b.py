"""phase0b.py -- if m_shape is not the coordinate, what is?
Candidates:
  m_hop   = |D| = #beads that move  (= #hops = 'orbits of hop-sharing')
  m_shape = #connected components of mu/lam
Also record has_2x2 and the box count, to see what mu/lam actually IS in Type 1.
"""
import sys, itertools, sympy as sp
sys.path.insert(0, '/home/clio/projects/probes/2026-09-04-Q76')
sys.path.insert(0, '/home/clio/projects/probes/2026-09-03-Q75')
from closedform import commutator_brute
from abacus import t, beta, parts_of
from symfunc import boxes, shape_stats
from phase0 import cofactor

def main(NMAX, EMAX):
    xtab = {}; bad = []
    for n in range(0, NMAX + 1):
        for lam in parts_of(n):
            for (e, ep) in itertools.combinations(range(2, EMAX + 1), 2):
                L = n + e + ep + 6
                B = set(beta(lam, L))
                for mu, val in commutator_brute(lam, e, ep, L).items():
                    if sp.expand(val) == 0: continue
                    a, b, c, res = cofactor(val)
                    Bp = set(beta(mu, L)); mhop = len(B - Bp)
                    mshape, h, sq = shape_stats(mu, lam)
                    key = (a, b, mhop, mshape, sq)
                    xtab[key] = xtab.get(key, 0) + 1
                    if not (a == 1 and b == mhop - 1 and res in (1, -1)):
                        if len(bad) < 5: bad.append((lam, mu, e, ep, sp.factor(val), mhop))
    print('cross-tab ((1+t)val, (1-t)val, m_hop, m_shape, has2x2) -> count')
    for k in sorted(xtab): print('  ', k, xtab[k])
    print('violations of entry = +-t^a (1+t)(1-t)^{m_hop-1}:', len(bad))
    for v in bad: print('   ', v)

if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]))
