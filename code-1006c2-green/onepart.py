"""One-part Green polynomials G^lam_(n)(t), BOTH conventions, plus the
competing 'P-expansion' convention, to settle the brief's hook-support claim."""
import sympy as sp, hl
from mn_peel import expand_in_P
t = sp.symbols('t')

def bracket(n):
    return sum(t**i for i in range(n))

for n in range(1, 8):
    order, Pp, Ps = hl.HL_P(n)
    # convention I  (Q'-expansion):  p_n = sum G^lam Q'_lam  ->  G = z_rho [p_rho] P_lam
    # convention II (P -expansion):  p_n = sum Y^lam P_lam
    pn = {(n,): sp.Integer(1)}
    Y = expand_in_P(pn, n)
    print(f'=== n={n}   [n]_t = {bracket(n)}')
    for lam in order:
        G = hl.green(n, lam, (n,))
        y = sp.expand(Y.get(lam, 0))
        hook = (len(lam) == 1) or (len(lam) > 1 and all(p == 1 for p in lam[1:]))
        print(f'  lam={str(lam):16s} hook={str(hook):5s}  G={sp.factor(G)!s:34s}  Y={sp.factor(y)}')
