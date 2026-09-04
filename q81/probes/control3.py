"""control3.py -- CONTROL 3: REPEATED sizes.  The conjecture was stated for
pairwise distinct e_i.  Theorem 1 (divisibility) and Theorem 2 (reduction) do
NOT use distinctness -- so test them where the conjecture did not claim to live.
Report what happens; do not restrict the statement to make it true.
"""
import sys, itertools, sympy as sp
sys.path.insert(0, '.'); sys.path.insert(0, '/home/clio/projects/probes/2026-09-04-Q76')
sys.path.insert(0, '/home/clio/projects/probes/2026-09-03-Q75')
from nested import C, t
from abacus import parts_of
from phase0 import cofactor

WORDS = [(2,3,2), (3,2,3), (2,2,3), (2,3,3), (2,2,2), (3,4,3), (2,3,2,3), (2,2,3,3)]
for es in WORDS:
    tot = nz = 0; vals = []; minval = None
    for n in range(0, 4 if len(es)==3 else 2):
        for lam in parts_of(n):
            L = n + sum(es) + 6
            for mu, v in C(list(es), lam, L).items():
                a, b, c, res = cofactor(v)
                tot += 1; nz += 1; vals.append(v)
                minval = a if minval is None else min(minval, a)
    g = sp.factor(sp.gcd_list(vals)) if vals else sp.Integer(0)
    print(f'es={es}: {nz} nonzero entries, min (1+t)-valuation = {minval}, gcd = {g}', flush=True)
