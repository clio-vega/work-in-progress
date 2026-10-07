"""Two-part data:  Y^lam_(x,y)(t) = [P_lam] p_x p_y,  factored."""
import sympy as sp, hl, kostka_side as ks
t = sp.symbols('t')
for n in range(2, 8):
    order,_,_ = hl.HL_P_cached(n)
    for x in range(n-1, (n-1)//2, -1):
        y = n - x
        if y < 1 or y > x: continue
        print(f'=== n={n}  rho=({x},{y})')
        for lam in order:
            v = ks.Y(n, lam, (x, y) if x>=y else (y,x))
            print(f'  {str(lam):20s} l={len(lam)} n(lam)={hl.n_stat(lam):3d}  Y = {sp.factor(v)}')
