"""Remark rem:kernel: the conjugation symmetry <mu'|C_k|vac> = t^{E-k} <mu|C_k(1/t)|vac>,
and the consequence that mu=(2,2,1^{E-4}) is always divisible by t."""
import sys, sympy as sp, itertools
sys.path.insert(0, '/home/clio/projects/probes/2026-09-04-Q81')
from nested import C, t

def conj(l):
    l = [x for x in l if x]
    return tuple(sum(1 for x in l if x > j) for j in range(l[0])) if l else ()

bad = n = 0
for es in [(4,2,3),(2,3,4),(3,4,2),(2,4,5,3),(3,2,4,5),(5,2,3)]:
    E, k = sum(es), len(es); ent = C(es, (), E+k+2)
    for mu, v in ent.items():
        n += 1
        lhs = sp.expand(ent.get(conj(mu), 0))
        rhs = sp.expand(t**(E-k) * sp.expand(v).subs(t, 1/t))
        if sp.simplify(lhs - rhs) != 0: bad += 1; print("FAIL", es, mu)
print(f"conjugation symmetry: {bad} failures / {n} entries")

found = 0
for k in (2,3,4):
    for es in itertools.product(range(2,5), repeat=k):
        if es[-2] == es[-1]: continue
        E = sum(es)
        v = sp.expand(C(es, (), E+k+2).get(tuple([2,2]+[1]*(E-4)), 0))
        if v != 0 and v.subs(t,0) != 0: found += 1; print("a=0 at", es, sp.factor(v))
print(f"entries at (2,2,1^(E-4)) with nonzero constant term: {found} (k<=4, e_i in 2..4)")
