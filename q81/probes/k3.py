"""k3.py -- the joint distribution of ((1+t)-val, (1-t)-val, m_hop, m_shape) on
the entries of C_3 = [R_e1,[R_e2,R_e3]].  The CROSS-TAB is the result."""
import sys, itertools, sympy as sp
sys.path.insert(0, '.'); sys.path.insert(0, '/home/clio/projects/probes/2026-09-04-Q76')
sys.path.insert(0, '/home/clio/projects/probes/2026-09-03-Q75')
from nested import C, t
from abacus import beta, parts_of
from symfunc import shape_stats
from phase0 import cofactor

def run(NMAX, ES):
    xtab = {}; resid = {}; viol = []; gcds = {}
    for n in range(0, NMAX + 1):
        for lam in parts_of(n):
            for es in ES:
                L = n + sum(es) + 6
                B = set(beta(lam, L))
                ents = C(list(es), lam, L)
                if not ents: continue
                vals = []
                for mu, val in ents.items():
                    a, b, c, res = cofactor(val)
                    mhop = len(B - set(beta(mu, L)))
                    mshape, h, sq = shape_stats(mu, lam)
                    xtab[(a, b, mhop, mshape)] = xtab.get((a, b, mhop, mshape), 0) + 1
                    resid[str(res)] = resid.get(str(res), 0) + 1
                    vals.append(val)
                    if not (a == 2 and b == mhop - 1 and res in (1, -1)):
                        if len(viol) < 10: viol.append((lam, mu, es, sp.factor(val), mhop, mshape))
                g = sp.factor(sp.gcd_list(vals))
                gcds[str(g)] = gcds.get(str(g), 0) + 1
        print(f'|lam|<={n} done  (entries so far {sum(xtab.values())})', flush=True)
    print('\nCROSS-TAB ((1+t)-val, (1-t)-val, m_hop, m_shape) -> count')
    for k in sorted(xtab): print('  ', k, xtab[k])
    print('\nresidues:', dict(resid))
    print('\nper-(lam,es) gcd of entries:')
    for k in sorted(gcds, key=lambda s: -gcds[s]): print('  ', k, gcds[k])
    print('\nviolations of entry = +-t^a (1+t)^2 (1-t)^{m_hop-1}:', len(viol))
    for v in viol: print('   ', v)

if __name__ == '__main__':
    NMAX = int(sys.argv[1]); EM = int(sys.argv[2])
    run(NMAX, list(itertools.combinations(range(2, EM + 1), 3)))
