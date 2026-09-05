"""Cross-check the two-bead witness against the INDEPENDENT Maya engine,
and assemble the literal gcd."""
import sys, itertools, sympy as sp
sys.path.insert(0, '/home/clio/projects/probes/2026-09-04-Q81')
from nested import C, t

def witness(es, verbose=False):
    k = len(es); E = sum(es); emin = min(es[-2], es[-1]); sgn = 1 if es[-1] > es[-2] else -1
    lam = (emin-1,) if emin > 1 else ()
    mu  = (E-1, emin)
    L = E + emin + k + 3
    ent = C(es, lam, L)
    B = sp.expand(ent.get(mu, 0))
    hook = tuple([E-emin] + [1]*emin)
    A = sp.expand(C(es, (), E+k+2).get(hook, 0))
    return A, B, sgn, mu, lam

print(f"{'e':<16}{'A = hook entry':<24}{'B = two-bead entry':<32}{'B(0)':>5}{'sgn':>5}  gcd(A,B)")
bad = 0
tuples = [(3,2),(2,3),(5,2),(2,5),(4,2,3),(4,3,2),(2,3,4),(3,4,2),(3,2,4),(2,4,3),
          (4,2,5),(5,3,2),(2,4,5,3),(3,2,4,5),(2,3,4,5),(5,4,3,2),(2,2,3,5),(3,3,5,2),
          (2,3,10,5),(4,4,2,3),(2,5,3,6),(3,2,2,4,3)]
for es in tuples:
    A, B, sgn, mu, lam = witness(es)
    g = sp.factor(sp.gcd(A, B))
    ok = (B.subs(t,0) == sgn) and sp.expand(g - (1+t)) == 0
    bad += 0 if ok else 1
    print(f"{str(es):<16}{str(sp.factor(A)):<24}{str(sp.factor(B)):<32}{str(B.subs(t,0)):>5}{sgn:>5}  {g}   {'' if ok else '<-- FAIL'}")
print(f"\n{bad} failures / {len(tuples)} tuples")
