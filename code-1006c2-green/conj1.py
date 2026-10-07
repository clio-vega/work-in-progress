"""Conjecture (one part):  [P_lam] p_n = (-1)^{l-1} t^{n(lam) - C(l,2)} phi_{l-1}(t),  l = len(lam)."""
import sympy as sp, hl, kostka_side as ks
t = sp.symbols('t')
def pred(lam):
    l = len(lam)
    return sp.expand((-1)**(l-1) * t**(hl.n_stat(lam) - l*(l-1)//2) * ks.phi(l-1))
tot=bad=0
for n in range(1, 8):
    order,_,_ = hl.HL_P_cached(n)
    for lam in order:
        tot += 1
        d = sp.expand(ks.Y(n, lam, (n,)) - pred(lam))
        if d != 0:
            bad += 1; print('  FAIL', n, lam, sp.factor(d))
print(f'one-part conjecture: {tot} partitions (n<=7), failures = {bad}')
# exponent non-negativity: n(lam) >= C(l,2) with equality iff lam has distinct... check
print('min exponent check:', all(hl.n_stat(l) >= len(l)*(len(l)-1)//2
      for n in range(1,9) for l in hl.partitions(n)))
