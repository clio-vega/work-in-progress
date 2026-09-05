"""Is C_k(0)|vac> ever zero?  (t=0 => R_e(0) adds a HORIZONTAL e-strip in ONE row,
 i.e. in beads: move one bead right by e without passing or landing on another.)"""
import sys, sympy as sp, itertools
sys.path.insert(0, '/home/clio/projects/probes/2026-09-04-Q81')
from nested import C, t

bad = []
for k in (2,3,4):
    for es in itertools.product(range(2,6), repeat=k):
        if es[-2] == es[-1]: continue
        E = sum(es); L = E + k + 2
        ent = C(es, (), L)
        nz0 = {mu: sp.expand(v).subs(t,0) for mu, v in ent.items()
               if sp.expand(v).subs(t,0) != 0}
        if not nz0:
            bad.append(es); print("ZERO at t=0:", es)
        elif k == 4 and es in [(2,4,5,3),(3,2,4,5)]:
            print(es, "->", nz0)
print("tuples with C_k(0)|vac> = 0 :", bad)
