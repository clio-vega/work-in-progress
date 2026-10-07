"""TASK 2, sharpened: the obstruction becomes a THEOREM, proved, on two-row lam.

Theorem C specialised to min(x,y) = b gives the diagonal family
    D_{a,b}(t) := Y^{(a,b)}_{(x,y)} = 1 + [a=b] + (t-1)t^{b-1} = t^b - t^{b-1} + 1 + [a=b].
If some member is irreducible-and-non-cyclotomic, NO product of cyclotomics and monomials
can equal it -- the product-form null, proved rather than measured.
"""
import sympy as sp, hl, kostka_side as ks
t = sp.symbols('t')
cyclos = {sp.Poly(sp.cyclotomic_poly(k, t), t) for k in range(1, 80)}
def classify(f):
    fl = sp.factor_list(f)[1]
    out = []
    for fac, m in fl:
        fp = sp.Poly(fac, t)
        if fp.total_degree() == 0: continue
        tag = 'cyclotomic' if fp in cyclos else ('monomial' if fac == t else 'NON-CYCLOTOMIC')
        out.append((sp.factor(fac), m, tag, sp.Poly(fac,t).degree()))
    return out

print('no cyclotomic polynomial has odd degree > 1: phi(n) in {1,2,4,6,...}; degrees present:',
      sorted({sp.Poly(sp.cyclotomic_poly(k,t),t).degree() for k in range(1,80)})[:12], '...')
print('  => in particular there is NO cyclotomic polynomial of degree 3.')
print()
print('  b  a>b: D = t^b-t^(b-1)+1          factors                   | a=b: D+1')
for b in range(1, 8):
    D1 = sp.expand(t**b - t**(b-1) + 1)
    D2 = sp.expand(D1 + 1)
    print(f'  {b}  {str(D1):24s} {str(classify(D1)):50s}')
    print(f'     {str(D2):24s} {str(classify(D2)):50s}  (a=b)')

print()
print('--- cross-check against the engine (not the formula) ---')
bad=0; tot=0
for n in range(2, 10):
    for b in range(1, n//2+1):
        a = n-b
        rho = tuple(sorted((n-b, b), reverse=True))
        got = ks.Y(n, (a,b), rho)
        pred = sp.expand(t**b - t**(b-1) + 1 + (1 if a==b else 0))
        tot+=1
        if sp.expand(got-pred)!=0:
            bad+=1; print('  FAIL', (a,b), rho, sp.factor(got), pred)
print(f'diagonal family D_(a,b) vs engine: {tot} (a,b) pairs, n<=9, failures={bad}')
print()
print('witness provenance, PROVED (not measured):')
print('  t^3-t^2+1  = D_(a,3), a>3   e.g. lam=(4,3), rho=(4,3)   irreducible, degree 3 => non-cyclotomic')
print('  t^2-2t+2   | D_(3,3) = t^3-t^2+2 = (t+1)(t^2-2t+2)      roots 1+-i, |1+-i|=sqrt2 => not roots of unity')
print('  t^2-t+2    = D_(2,2) = t^2-t+2                          roots (1+-i sqrt7)/2, modulus sqrt2')
for p in [t**3-t**2+1, t**2-2*t+2, t**2-t+2]:
    rts = sp.Poly(p,t).all_roots()
    print(f'  {p}: |roots| = {[sp.nsimplify(sp.Abs(r)).evalf(6) for r in rts]}')
