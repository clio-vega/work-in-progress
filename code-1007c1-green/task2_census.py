"""TASK 2: where do the four non-cyclotomic witnesses live?  Factorisation census of
Y^lam_rho over ALL two-part rho, n<=8, recording l(lam) for each witness occurrence.

Theorem C (now PROVED) predicts, for two-row lam=(a,b) and rho=(x,y) with min(x,y)=b:
   Y = 1 + [a=b] + (t-1)t^{b-1}
 b=3, a>3 :  t^3 - t^2 + 1          <- witness, IRREDUCIBLE, degree 3
 b=3, a=3 :  t^3 - t^2 + 2 = (t+1)(t^2-2t+2)   <- witness t^2-2t+2
If these occur, the brief's guessed reconciliation ("obstruction is about general lam,
Theorem C is two-row") is FALSE and the real scope separator is PRODUCT vs SUM.
"""
import sympy as sp, hl, kostka_side as ks
t = sp.symbols('t')
W = {sp.Poly(p, t): s for p, s in [(t**2-t+2,'t^2-t+2'), (t**2-2*t+2,'t^2-2t+2'),
                                   (t**3+t**2-1,'t^3+t^2-1'), (t**3-t**2+1,'t^3-t^2+1')]}
def is_cyclo(f):
    f = sp.Poly(f, t)
    if f.degree() == 0: return True
    for k in range(1, 60):
        if sp.Poly(sp.cyclotomic_poly(k, t), t) == f.monic()*f.LC()/f.LC(): pass
    return any(sp.Poly(sp.cyclotomic_poly(k, t), t) == f for k in range(1, 60))

print('--- direct check of Theorem C\'s prediction ---')
for (a,b) in [(4,3),(5,3),(3,3),(6,3)]:
    n=a+b; rho=tuple(sorted((n-b,b),reverse=True))
    y=ks.Y(n,(a,b),rho)
    print(f'  lam={(a,b)} rho={rho}:  Y = {sp.factor(y)}')

print()
print('--- full census: non-cyclotomic irreducible factors of Y^lam_rho, two-part rho, n<=8 ---')
found = {}
noncyc_lengths = {}
for n in range(2, 9):
    order,_,_ = hl.HL_P_cached(n)
    for lam in order:
        for y in range(1, n//2+1):
            x = n-y; rho = tuple(sorted((x,y),reverse=True))
            Yv = ks.Y(n, lam, rho)
            if Yv == 0: continue
            for fac, mult in sp.factor_list(Yv)[1]:
                fp = sp.Poly(fac, t)
                if fp.degree() == 0: continue
                if is_cyclo(fp): continue
                key = str(sp.factor(fac))
                found.setdefault(key, []).append((n, lam, rho))
                noncyc_lengths.setdefault(key, set()).add(len(lam))
for k in sorted(found, key=lambda s: (len(found[s]), s)):
    lens = sorted(noncyc_lengths[k])
    tworow = [o for o in found[k] if len(o[1]) == 2]
    print(f'  {k:16s} occurrences={len(found[k]):3d}  l(lam) seen={lens}'
          f'  two-row instances={len(tworow)}')
    for o in found[k][:3]: print(f'        e.g. n={o[0]} lam={o[1]} rho={o[2]}')
print()
print('WITNESS CHECK (the four named in Q372):')
for p, s in [(t**2-t+2,'t^2-t+2'), (t**2-2*t+2,'t^2-2t+2'), (t**3+t**2-1,'t^3+t^2-1'), (t**3-t**2+1,'t^3-t^2+1')]:
    k = str(sp.factor(p))
    hits = found.get(k, [])
    tr = [o for o in hits if len(o[1])==2]
    print(f'  {s:12s}: {len(hits):3d} occurrences, {len(tr):3d} with TWO-ROW lam'
          + (f'   e.g. {tr[0]}' if tr else '   (none two-row)'))
