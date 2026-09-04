"""contents.py -- C6: the bead-hop b -> b+e corresponds to the ribbon occupying
exactly the e consecutive DIAGONALS (contents c-r) in the interval (b-L, b-L+e].
Checked directly on Young diagrams.  If true, 'the hops cross' is a statement
about diagonal supports, with no abacus in it.
"""
import sys, itertools
sys.path.insert(0, '.'); sys.path.insert(0, '/home/clio/projects/probes/2026-09-03-Q75')
from abacus import beta, parts_of, trim
from symfunc import boxes, shape_stats, contains

good = bad = 0
for n in range(0, 8):
    for lam in parts_of(n):
        for e in range(2, 7):
            L = n + e + 6
            B = set(beta(lam, L))
            for mu in parts_of(n + e):
                if not contains(mu, lam): continue
                c, h, sq = shape_stats(mu, lam)
                if c != 1 or sq: continue
                b = (B - set(beta(mu, L))).pop()
                pred = set(range(b - L + 1, b - L + e + 1))
                actual = set(col - row for row, col in boxes(mu, lam))
                if pred == actual: good += 1
                else:
                    bad += 1
                    if bad <= 3: print('  MISMATCH', lam, mu, e, sorted(pred), sorted(actual))
print(f'C6  ribbon of hop b->b+e occupies diagonals (b-L, b-L+e]: {good}/{good+bad}')
