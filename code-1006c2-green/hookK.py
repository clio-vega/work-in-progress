"""The one-part theorem, dual form:
   sum_{r=0}^{n-1} (-1)^r K_{(n-r,1^r),mu}(t) = (-1)^{l-1} t^{n(mu)-C(l,2)} phi_{l-1}(t).
Look for a closed form for the individual hook Kostka-Foulkes K_{(n-r,1^r),mu}(t)."""
import sympy as sp, hl, kostka_side as ks
t = sp.symbols('t')
def qbin(a,b):
    if b<0 or b>a: return sp.Integer(0)
    num=den=sp.Integer(1)
    for i in range(b): num *= (1-t**(a-i)); den *= (1-t**(i+1))
    return sp.cancel(num/den)
for n in range(2, 7):
    order, K = ks.kostka_matrix(n)
    hooks = [ (n-r,)+(1,)*r for r in range(n) ]
    hooks = [tuple(p for p in h if p>0) for h in hooks]
    print(f'=== n={n}')
    for mu in order:
        l = len(mu); nm = hl.n_stat(mu)
        row = []
        for r in range(n):
            v = sp.expand(K[(hooks[r], mu)])
            row.append(v)
        alt = sp.expand(sum((-1)**r*row[r] for r in range(n)))
        pred = sp.expand((-1)**(l-1)*t**(nm - l*(l-1)//2)*ks.phi(l-1))
        ok = 'OK' if sp.expand(alt-pred)==0 else 'FAIL'
        print(f'  mu={str(mu):16s} l={l} n(mu)={nm:2d}  alt={sp.factor(alt)}  [{ok}]')
        for r in range(n):
            if row[r]!=0:
                # compare with t^? * qbin(l-1, r)
                q = sp.cancel(row[r]/qbin(l-1,r)) if qbin(l-1,r)!=0 else None
                print(f'      r={r}: K_{{({n-r},1^{r}),mu}} = {sp.factor(row[r])}'
                      + (f'   / qbin({l-1},{r}) = {sp.factor(q)}' if q is not None else ''))
