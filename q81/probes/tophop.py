"""tophop.py -- the survivor of conjecture (B): is the MAXIMAL-hop entry
(m_hop = k, i.e. k distinct beads each hop once) always +- t^a (1-t^2)^{k-1}?
Cross-tab entry shape against m_hop for k=2 and k=3."""
import sys, itertools, sympy as sp
sys.path.insert(0, '.'); sys.path.insert(0, '/home/clio/projects/probes/2026-09-04-Q76')
sys.path.insert(0, '/home/clio/projects/probes/2026-09-03-Q75')
from nested import C, t
from abacus import beta, parts_of
from phase0 import cofactor

def run(NMAX, EMAX, K):
    tab = {}
    for es in itertools.combinations(range(2, EMAX + 1), K):
        for n in range(0, NMAX + 1):
            for lam in parts_of(n):
                L = n + sum(es) + 6
                B = set(beta(lam, L))
                for mu, val in C(list(es), lam, L).items():
                    a, b, c, res = cofactor(val)
                    mhop = len(B - set(beta(mu, L)))
                    tab.setdefault(mhop, {})
                    key = f'(1+t)^{a} (1-t)^{b} * [{sp.expand(res)}]'
                    tab[mhop][key] = tab[mhop].get(key, 0) + 1
    for m in sorted(tab):
        print(f'm_hop = {m}:')
        for k_ in sorted(tab[m], key=lambda s: -tab[m][s]): print('   ', k_, tab[m][k_])

if __name__ == '__main__':
    run(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
