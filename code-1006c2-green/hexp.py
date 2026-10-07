"""h-expansion of the modified Hall-Littlewood Q'_lam.
If Q'_lam = sum_nu c_{lam,nu}(t) h_nu then for ANY rho
     Y^lam_rho = <p_rho, Q'_lam> = sum_nu c_{lam,nu}(t) * <p_rho, h_nu>
and <p_rho,h_nu> is a pure counting number (ways to distribute the parts of rho
into blocks with sums nu).  So a closed form for c gives a closed form for every Y.
"""
import sympy as sp, hl, kostka_side as ks
t = sp.symbols('t')

def h_in_p(nu, n):
    """h_nu = prod h_{nu_i} in the p-basis."""
    cur = {(): sp.Integer(1)}
    for part in nu:
        hp = {rho: sp.Rational(1, hl.z_lam(rho)) for rho in hl.partitions(part)}
        new = {}
        for r1, c1 in cur.items():
            for r2, c2 in hp.items():
                k = tuple(sorted(r1+r2, reverse=True))
                new[k] = new.get(k, 0) + c1*c2
        cur = new
    return cur

def Qprime_in_p(n, lam):
    order, K = ks.kostka_matrix(n)
    S = hl.p_of_schur(n)
    out = {}
    for nu in order:
        c = K[(nu, lam)]
        if c == 0: continue
        for rho, v in S[nu].items():
            out[rho] = out.get(rho, 0) + c*v
    return {k: sp.expand(v) for k, v in out.items() if sp.expand(v) != 0}

def hexpand(n, lam):
    """Solve Q'_lam = sum_nu c_nu h_nu over the p-basis."""
    parts = list(hl.partitions(n))
    A = sp.Matrix([[h_in_p(nu, n).get(rho, 0) for nu in parts] for rho in parts])
    b = sp.Matrix([[Qprime_in_p(n, lam).get(rho, 0)] for rho in parts])
    sol = A.solve(b)
    return {parts[i]: sp.expand(sp.cancel(sol[i])) for i in range(len(parts))
            if sp.cancel(sol[i]) != 0}

if __name__ == '__main__':
    import sys
    for n in range(2, int(sys.argv[1])+1):
        order,_,_ = hl.HL_P_cached(n)
        print(f'=== n={n}')
        for lam in order:
            e = hexpand(n, lam)
            s = '  '.join(f'{sp.factor(v)} * h_{nu}' for nu, v in sorted(e.items(), reverse=True))
            print(f"  Q'_{lam} = {s}")
