"""LEMMA 1 (hook Kostka-Foulkes closed form).
   For mu |- n with l = l(mu) parts, and 0 <= r:
      K_{(n-r,1^r), mu}(t) = t^{ n(mu) - C(l,2) + C(l-r,2) } * qbinom(l-1, r)_t
   (in particular = 0 for r > l-1).
Also the cell-level claim: the SSYT of hook shape (n-r,1^r) and content mu are indexed by
r-subsets S of {2..l} (the column entries below the corner), with
      charge(T_S) = n(mu) - C(l,2) + C(l-r,2) + sum_{s in S}(s-1) - r(r+1)/2.
"""
import sympy as sp, hl, kostka_side as ks
from charge_kostka import ssyt, charge
from itertools import combinations
t = sp.symbols('t')
def qbin(a,b):
    if b<0 or b>a: return sp.Integer(0)
    num=den=sp.Integer(1)
    for i in range(b): num *= (1-t**(a-i)); den *= (1-t**(i+1))
    return sp.expand(sp.cancel(num/den))

tot=bad=0; ctot=cbad=0
for n in range(1, 10):
    for mu in hl.partitions(n):
        l = len(mu); nb = hl.n_stat(mu) - l*(l-1)//2
        for r in range(0, n):
            shape = tuple(p for p in ((n-r,)+(1,)*r) if p>0)
            if len(shape)>0 and shape[0] < 1: continue
            if n-r < 1: continue
            # need a valid partition shape
            if n-r < 1 or (r>0 and n-r < 1): continue
            Ks = sp.expand(sum(t**charge(T) for T in ssyt(shape, mu)))
            pred = sp.expand(t**(nb + (l-r)*(l-r-1)//2) * qbin(l-1, r)) if r <= l-1 else sp.Integer(0)
            tot += 1
            if sp.expand(Ks - pred) != 0:
                bad += 1
                if bad<=5: print('  K FAIL', n, mu, r, sp.factor(Ks), '!=', sp.factor(pred))
            # cell-level: charge of each T_S
            if r <= l-1:
                for S in combinations(range(2, l+1), r):
                    # build T_S explicitly and compare charge with the predicted exponent
                    cpred = nb + (l-r)*(l-r-1)//2 + sum(s-1 for s in S) - r*(r+1)//2
                    col = list(S)
                    rowmult = [mu[v-1] - (1 if v in S else 0) for v in range(1, l+1)]
                    row1 = []
                    for v in range(1, l+1): row1 += [v]*rowmult[v-1]
                    T = tuple([tuple(row1)] + [(c,) for c in col])
                    ctot += 1
                    if charge(T) != cpred:
                        cbad += 1
                        if cbad<=5: print('  CHARGE FAIL', mu, S, charge(T), cpred)
print(f'Lemma 1 (hook K closed form): {tot} (mu,r) pairs, n<=9, failures = {bad}')
print(f'cell-level charge formula:    {ctot} tableaux, failures = {cbad}')
