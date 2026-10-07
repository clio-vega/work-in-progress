"""Raising-operator (Jing / Garsia-Procesi) form of the modified Hall-Littlewood:
       Q'_lam  =  prod_{i<j} (1 - R_ij)/(1 - t R_ij) . h_lam ,
   R_ij : h_nu -> h_{nu + e_i - e_j};  h_nu = 0 if some nu_i < 0.
   Per-pair weight from (1-R)(1+tR+t^2R^2+...):  w(0)=1,  w(k)=t^{k-1}(t-1), k>=1.

Processing order: rows are drained bottom-up (j = l-1 down to 1).  When row j is
drained it has already received everything it ever will (donors are strictly below),
so sum_i k_ij <= nu[j] is a valid bound.  R_ij commute, so order is immaterial.
"""
import sympy as sp, hl
t = sp.symbols('t')
def w(k): return sp.Integer(1) if k == 0 else t**(k-1)*(t-1)

def _splits(total, slots):
    """all tuples of length `slots` of nonneg ints with sum <= total"""
    if slots == 0:
        yield (); return
    for first in range(total+1):
        for rest in _splits(total-first, slots-1):
            yield (first,)+rest

def Qprime_h(lam):
    l = len(lam)
    states = {tuple(lam): sp.Integer(1)}
    for j in range(l-1, 0, -1):
        new = {}
        for nu, c in states.items():
            for ks in _splits(nu[j], j):
                nn = list(nu)
                nn[j] -= sum(ks)
                for i in range(j): nn[i] += ks[i]
                coef = c
                for k in ks: coef *= w(k)
                key = tuple(nn)
                new[key] = new.get(key, 0) + coef
        states = {k: sp.expand(v) for k, v in new.items() if sp.expand(v) != 0}
    out = {}
    for nu, c in states.items():
        key = tuple(sorted((v for v in nu if v > 0), reverse=True))
        out[key] = sp.expand(out.get(key, 0) + c)
    return {k: v for k, v in out.items() if v != 0}

if __name__ == '__main__':
    import hexp
    tot=bad=0
    for n in range(1, 7):
        order,_,_ = hl.HL_P_cached(n)
        for lam in order:
            a = Qprime_h(lam)
            b = hexp.hexpand(n, lam) if n > 1 else {(1,): sp.Integer(1)}
            tot += 1
            d = [(k, sp.factor(a.get(k,0)-b.get(k,0))) for k in set(a)|set(b)
                 if sp.expand(a.get(k,0)-b.get(k,0)) != 0]
            if d:
                bad += 1; print(f'  MISMATCH lam={lam}: {d[:3]}')
    print(f'raising-operator form vs direct h-expansion: {tot} partitions (n<=6), failures = {bad}')
