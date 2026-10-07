# Green polynomials X^lambda_rho(t) via Jing-Liu recurrence (arXiv:2104.04411v2, eq (e:Recurrence))
# X^la_mu = sum_{tau <| mu, |tau|<=n-la_1} sum_{rho |- |la^[1]|-|tau|} (-1)^{l(rho)}/z_rho(t) X^{la^[1]}_{tau u rho}
# tau <| mu : submultiset of the PARTS of mu indexed by position subsets.
import sympy as sp
from functools import lru_cache
from itertools import combinations
t = sp.symbols('t')

def parts_of(n):
    # partitions of n, each a sorted-desc tuple
    def gen(n, mx):
        if n == 0: yield ()
        for k in range(min(n, mx), 0, -1):
            for rest in gen(n-k, k): yield (k,)+rest
    return list(gen(n, n)) if n > 0 else [()]

def z_t(rho):
    # z_rho(t) = z_rho / prod_i (1 - t^{rho_i})
    from collections import Counter
    c = Counter(rho)
    z = sp.Integer(1)
    for i, m in c.items(): z *= sp.Integer(i)**m * sp.factorial(m)
    den = sp.Integer(1)
    for r in rho: den *= (1 - t**r)
    return sp.together(z/den)

def subparts(mu):
    """all submultisets of mu indexed by position subsets (with multiplicity)"""
    out = []
    L = len(mu)
    for r in range(L+1):
        for S in combinations(range(L), r):
            out.append(tuple(sorted((mu[i] for i in S), reverse=True)))
    return out

@lru_cache(maxsize=None)
def X(la, mu):
    assert sum(la) == sum(mu)
    n = sum(la)
    if n == 0: return sp.Integer(1)
    la1 = la[0]; la_rest = la[1:]; m = sum(la_rest)  # = n - la1
    tot = sp.Integer(0)
    for tau in subparts(mu):
        if sum(tau) > m: continue
        for rho in parts_of(m - sum(tau)):
            nu = tuple(sorted(tau + rho, reverse=True))
            tot += sp.Integer(-1)**len(rho) / z_t(rho) * X(la_rest, nu)
    return sp.simplify(sp.expand(sp.cancel(sp.together(tot))))

if __name__ == '__main__':
    # VERIFICATION against R. Stanley (MO 41137) and the jack R package
    checks = {
      ((3,), (2,1)): 1, ((2,1),(2,1)): t, ((1,1,1),(2,1)): t**3-1,
      ((4,),(3,1)): 1, ((3,1),(3,1)): t, ((2,2),(3,1)): t**2-1,
      ((2,1,1),(3,1)): t**3-t, ((1,1,1,1),(3,1)): t**6-t**4-t**2+1,
    }
    ok = 0
    for (la,mu),val in checks.items():
        got = X(la,mu)
        good = sp.simplify(got-val)==0
        ok += good
        print(('OK ' if good else 'FAIL'), 'X^%s_%s ='%(la,mu), sp.factor(got), '(expected', sp.factor(val), ')')
    print('verified %d/%d'%(ok,len(checks)))
