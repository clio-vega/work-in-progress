"""Full verification of the Q85 witness theorem.

THEOREM  lam* = (emin-1),  mu* = (E-1, emin),  emin = min(e_{k-1}, e_k):
    <mu* | C_k | lam*>  =  sgn(e_k - e_{k-1}) * (1+t)   exactly.

Checked against the Maya engine (probes/2026-09-04-Q76/abacus.py), which shares
no primitive with the two-sector argument below.
"""
import sys, itertools, sympy as sp
sys.path.insert(0, '/home/clio/projects/probes/2026-09-04-Q81')
sys.path.insert(0, '/home/clio/projects/2026-09-05-Q85')
sys.path.insert(0, '/home/clio/projects/probes/2026-09-05-Q85')
from nested import C, t
from twobead import U_words, N_formula

def sectors(es):
    """the two-sector model: (non-crossing, crossing) contributions, and X."""
    k = len(es); emin = min(es[-2], es[-1])
    X = 0
    for r in range(1, k+1):
        for Sbar in itertools.combinations(range(1, k+1), r):
            if sum(es[i-1] for i in Sbar) == emin:
                X += N_formula(k, Sbar)
    return -X, -X*t, X                      # sector (i), sector (ii), X

def engine_entry(es):
    k = len(es); E = sum(es); emin = min(es[-2], es[-1])
    lam = (emin-1,); mu = (E-1, emin)
    return sp.expand(C(es, lam, E + emin + k + 3).get(mu, 0))

# ---- check A: theorem vs Maya engine, exhaustive sweep
bad = n = 0
for k in (2, 3, 4):
    for es in itertools.product(range(2, 6), repeat=k):
        if es[-2] == es[-1]: continue
        sgn = 1 if es[-1] > es[-2] else -1
        got = engine_entry(es); want = sp.expand(sgn*(1+t))
        s0, s1, X = sectors(es)
        n += 1
        if sp.expand(got - want) != 0 or sp.expand(s0 + s1 - want) != 0 or X != -sgn:
            bad += 1; print("FAIL", es, got, want, (s0, s1, X))
print(f"check A  <mu*|C_k|lam*> = sgn*(1+t), engine vs theorem vs sector model:"
      f" {bad} failures / {n} tuples (k=2,3,4; e_i in 2..5)")

# ---- check B: k=5,6 spot check (engine is slow, so a sample)
bad = n = 0
for es in [(2,3,4,5,6),(6,5,4,3,2),(3,3,2,5,4),(2,2,2,3,2),(4,2,3,2,5),(5,5,5,2,3),
           (2,3,4,5,6,7),(3,2,4,2,5,3)]:
    sgn = 1 if es[-1] > es[-2] else -1
    got = engine_entry(es); n += 1
    if sp.expand(got - sgn*(1+t)) != 0:
        bad += 1; print("FAIL", es, got)
print(f"check B  same at k=5,6: {bad} failures / {n} tuples")

# ---- check C: NEGATIVE CONTROL.  Plant an error: use emin = max(e_{k-1},e_k).
moved = n = 0
for es in [(2,3,4),(4,3,2),(2,4,5,3),(3,2,4,5),(2,3,4,5),(5,2,3)]:
    k=len(es); E=sum(es); emax = max(es[-2], es[-1])
    ent = C(es, (emax-1,), E+emax+k+3).get((E-1, emax), 0)
    n += 1
    if sp.expand(sp.expand(ent) - (1 if es[-1]>es[-2] else -1)*(1+t)) != 0: moved += 1
print(f"check C  planted error (emin -> emax): {moved}/{n} tuples now DISAGREE"
      f"  (must be > 0, else the test is blind)")

# ---- check D: literal gcd over ALL matrix entries reachable from lam*, and from vac
bad = n = 0
for es in [(3,2),(2,3),(4,2,3),(2,3,4),(3,4,2),(2,4,5,3),(3,2,4,5),(2,3,10,5),(4,4,2,3)]:
    k=len(es); E=sum(es); emin=min(es[-2],es[-1])
    allent = []
    for lam in [(), (emin-1,)]:
        allent += [sp.expand(v) for v in C(es, lam, E+emin+k+3).values()]
    g = sp.Integer(0)
    for p in allent: g = sp.gcd(g, p)
    cont = 0
    for p in allent: cont = sp.gcd(cont, sp.gcd(sp.Poly(p, t).all_coeffs()))
    n += 1
    ok = sp.expand(g-(1+t)) == 0 and cont == 1
    if not ok: bad += 1
    print(f"   e={str(es):<15} #entries={len(allent):<4} gcd={sp.factor(g)}  content={cont}")
print(f"check D  literal gcd = 1+t and content 1: {bad} failures / {n} tuples")
