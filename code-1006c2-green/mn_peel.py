"""Compute the HL Murnaghan-Nakayama coefficients
      p_n^perp P_lam = sum_mu c^lam_{mu}(n;t) P_mu
by acting with n*d/dp_n on the p-expansion of P_lam and re-expanding in P.
p_n^perp is the adjoint of multiplication by p_n for the ORDINARY Hall product."""
import sympy as sp, hl
t = sp.symbols('t')

def p_perp(f, n, deg):
    """n * d/dp_n applied to a p-basis dict of degree deg -> degree deg-n."""
    out = {}
    for rho, c in f.items():
        # multiplicity of n in rho
        m = rho.count(n)
        if m == 0: continue
        rest = list(rho); rest.remove(n); rest = tuple(rest)
        out[rest] = out.get(rest, 0) + c * n * m
    return {k: sp.cancel(v) for k, v in out.items() if sp.cancel(v) != 0}

def expand_in_P(f, deg):
    """Write a p-basis dict of degree deg in the P_lam basis: coeff = <f, Q'_lam>.
    We do it by triangular solve against P_s is unnecessary: use <P_lam,Q'_mu>=delta,
    so f = sum_lam a_lam P_lam  with a_lam obtained by solving the linear system
    in the p-basis."""
    if deg == 0:
        return {(): f.get((), 0)} if f.get((), 0) not in (0, None) else {}
    order, Pp, Ps = hl.HL_P(deg)
    # solve sum_lam a_lam Pp[lam] = f, triangular in dominance (largest first)
    res = {}
    g = dict(f)
    for lam in reversed(order):      # largest first
        a = sp.cancel(g.get(lam, 0))   # P_lam = p_lam-leading? NO: use Schur-leading
        res[lam] = a
    # that is wrong; do an honest linear solve on the p-basis instead
    import itertools
    parts = list(order)
    A = sp.Matrix([[Pp[lam].get(rho, 0) for lam in parts] for rho in parts])
    b = sp.Matrix([[f.get(rho, 0)] for rho in parts])
    sol = A.solve(b)
    return {parts[i]: sp.cancel(sp.together(sol[i])) for i in range(len(parts))
            if sp.cancel(sol[i]) != 0}

if __name__ == '__main__':
    for deg in range(2, 6):
        order, Pp, Ps = hl.HL_P(deg)
        for n in range(1, deg + 1):
            print(f'--- deg {deg}, p_{n}^perp ---')
            for lam in order:
                g = p_perp(Pp[lam], n, deg)
                e = expand_in_P(g, deg - n) if g else {}
                if e:
                    s = '  '.join(f'{mu}: {sp.factor(sp.simplify(v))}' for mu, v in sorted(e.items()))
                    print(f'  P_{lam} -> {s}')
                else:
                    print(f'  P_{lam} -> 0')
