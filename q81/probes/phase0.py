"""phase0.py -- Does the k=2 closed form refactor as +-t^a (1+t)^{k-1} (1-t)^{m-1}
with m = #connected components of mu/lam?

This is BOOKKEEPING on already-verified data (Q76 closed form, 238594/238594).
If it fails, DREAM's Crown 1 (m is the coordinate) is wrong at k=2 already.
"""
import sys, itertools, sympy as sp
sys.path.insert(0, '/home/clio/projects/probes/2026-09-04-Q76')
sys.path.insert(0, '/home/clio/projects/probes/2026-09-03-Q75')
from closedform import commutator_brute
from abacus import t, beta, parts_of, trim
from symfunc import boxes, shape_stats, contains

def valuation(poly, root):
    """(1 - root*?) ... we want (t - root)-adic valuation: multiplicity of t=root."""
    p = sp.Poly(sp.expand(poly), t)
    v = 0
    while p.degree() >= 0 and p.eval(root) == 0 and p.as_expr() != 0:
        p = sp.Poly(sp.div(p.as_expr(), t - root, t)[0], t)
        v += 1
        if p.as_expr() == 0: break
    return v

def cofactor(poly):
    """strip (1+t)^a (1-t)^b t^c and the sign; return (a,b,c,sign,residue)."""
    p = sp.expand(poly)
    a = valuation(p, -1)
    p = sp.expand(sp.cancel(p / (1 + t)**a))
    b = valuation(p, 1)
    p = sp.expand(sp.cancel(p / (1 - t)**b))
    c = 0
    while sp.expand(p.subs(t, 0)) == 0 and p != 0:
        p = sp.expand(sp.cancel(p / t)); c += 1
    return a, b, c, p

def main(NMAX, EMAX):
    xtab = {}   # (a=(1+t)val, b=(1-t)val, m) -> count
    resid = {}  # residues after stripping
    bad = []
    for n in range(0, NMAX + 1):
        for lam in parts_of(n):
            for (e, ep) in itertools.combinations(range(2, EMAX + 1), 2):
                L = n + e + ep + 6
                for mu, val in commutator_brute(lam, e, ep, L).items():
                    if sp.expand(val) == 0: continue
                    a, b, c, res = cofactor(val)
                    assert contains(mu, lam), (lam, mu)
                    m, h, sq = shape_stats(mu, lam)
                    xtab[(a, b, m)] = xtab.get((a, b, m), 0) + 1
                    resid[str(res)] = resid.get(str(res), 0) + 1
                    if not (a == 1 and b == m - 1 and res in (1, -1)):
                        if len(bad) < 8:
                            bad.append((lam, mu, e, ep, sp.factor(val), m))
        print(f'|lam|<={n} done', flush=True)
    print('\ncross-tab ((1+t)-val, (1-t)-val, m) -> count')
    for k in sorted(xtab): print('  ', k, xtab[k])
    print('\nresidues after stripping t^c (1+t)^a (1-t)^b:')
    for k in sorted(resid, key=lambda s: -resid[s]): print('  ', k, resid[k])
    print('\nviolations of  entry = +-t^a (1+t)^1 (1-t)^{m-1}:', len(bad))
    for v in bad: print('   ', v)

if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]))
