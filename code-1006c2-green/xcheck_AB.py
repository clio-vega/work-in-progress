"""Cross-check: Mechanism A (charge statistic) vs Mechanism B (Gram-Schmidt).
Claim tested:  P_s = K(t)^{-1}, i.e.  P_s . K = I   where K_{nu mu}(t) is Kostka-Foulkes.
Equivalently <P_lam, Q'_mu> = delta.  These two computations share NO code path."""
import sympy as sp, hl
from charge_kostka import kostka_foulkes
t = sp.symbols('t')

for n in range(1, 8):
    order, Pp, Ps = hl.HL_P(n)
    K = {(nu, mu): kostka_foulkes(nu, mu) for nu in order for mu in order}
    bad = 0
    for lam in order:
        for mu in order:
            s = sum(Ps[lam].get(nu, 0) * K[(nu, mu)] for nu in order)
            s = sp.expand(sp.cancel(s))
            want = 1 if lam == mu else 0
            if sp.simplify(s - want) != 0:
                bad += 1
                if bad <= 3: print('  MISMATCH', lam, mu, s)
    print(f'n={n}: {len(order)}x{len(order)}  mismatches={bad}')
