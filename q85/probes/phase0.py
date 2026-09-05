"""Phase 0 for Q85: what is the LITERAL gcd of the entries of C_k|vac>?

(0d) full support: which mu occur, and what is gcd over ALL of them?
(0b) is there an entry with nonzero constant term (i.e. t does not divide gcd)?
(0c) is there an entry nonzero at t=1 (i.e. (t-1) does not divide gcd)?
(0a) content: is the Z[t] gcd the same as the Q[t] gcd?
"""
import sys, sympy as sp
sys.path.insert(0, '/home/clio/projects/probes/2026-09-04-Q81')
sys.path.insert(0, '/home/clio/projects/probes/2026-09-04-Q76')
from nested import C, t

def report(es):
    E = sum(es); L = E + len(es) + 2
    ent = C(es, (), L)
    polys = [sp.Poly(sp.expand(v), t) for v in ent.values()]
    g = sp.Integer(0)
    for p in polys:
        g = sp.gcd(g, p.as_expr())
    g = sp.expand(g)
    # content (Z[t] gcd = content_gcd * primitive gcd)
    cont = 0
    for p in polys:
        cont = sp.gcd(cont, sp.gcd(list(p.all_coeffs())))
    nz0 = [(mu, sp.expand(v)) for mu, v in ent.items() if sp.expand(v).subs(t, 0) != 0]
    nz1 = [(mu, sp.expand(v)) for mu, v in ent.items() if sp.expand(v).subs(t, 1) != 0]
    print(f"e={es}  E={E}  #entries={len(ent)}")
    print(f"   Q[t] gcd = {sp.factor(g)}     integer content gcd = {cont}")
    print(f"   #entries with nonzero constant term: {len(nz0)}")
    for mu, v in sorted(nz0)[:4]:
        print(f"      mu={mu}: {sp.factor(v)}")
    print(f"   #entries nonzero at t=1: {len(nz1)}")
    # the predicted monomial witness at j = e_min
    emin = min(es[-2], es[-1])
    hook = tuple([E - emin] + [1]*emin) if E - emin >= 1 else None
    print(f"   predicted hook j=e_min={emin}: mu={hook} -> {sp.factor(ent.get(hook,0))}")

for es in [(3,2),(2,3),(5,2),(4,2,3),(4,3,2),(2,3,4),(3,4,2),(2,4,3),(3,2,4),(4,2,5)]:
    report(es); print()
