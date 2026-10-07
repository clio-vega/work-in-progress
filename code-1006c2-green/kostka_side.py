"""Fast exact engine on the KOSTKA side.
   K(t) = (P_s)^{-1} by triangular solve (pure polynomial arithmetic, no denominators).
   Y^lam_rho(t) := [P_lam] p_rho = <p_rho, Q'_lam> = sum_nu K_{nu lam}(t) chi^nu_rho.
   G^lam_rho(t) := [Q'_lam] p_rho = prod_i (1-t^{rho_i}) * Y^lam_rho / b_lam(t).
"""
import sympy as sp, hl, pickle, os
from collections import Counter
t = sp.symbols('t')

def phi(m):
    r = sp.Integer(1)
    for k in range(1, m+1): r *= (1 - t**k)
    return sp.expand(r)

def b_lam(lam):
    r = sp.Integer(1)
    for part, m in Counter(lam).items(): r *= phi(m)
    return sp.expand(r)

def kostka_matrix(n):
    """K_{nu mu}(t) by inverting the unitriangular P_s matrix (order: smallest first)."""
    f = os.path.join(hl.CACHE, f'K{n}.pkl')
    if os.path.exists(f):
        with open(f,'rb') as fh: return pickle.load(fh)
    order, Pp, Ps = hl.HL_P_cached(n)
    N = len(order); idx = {l:i for i,l in enumerate(order)}
    # A[i][j] = coeff of s_{order[j]} in P_{order[i]};  A unitriangular LOWER
    # (nonzero only for order[j] <= order[i], i.e. j <= i)
    A = [[sp.expand(Ps[order[i]].get(order[j], 0)) for j in range(N)] for i in range(N)]
    for i in range(N):
        assert A[i][i] == 1, (order[i], A[i][i])
        for j in range(i+1, N):
            assert A[i][j] == 0, ('upper tri violated', order[i], order[j], A[i][j])
    # invert lower unitriangular: B = A^{-1},  B[i][j] for j<=i
    B = [[sp.Integer(0)]*N for _ in range(N)]
    for i in range(N):
        B[i][i] = sp.Integer(1)
        for j in range(i-1, -1, -1):
            s = sp.Integer(0)
            for k in range(j, i):
                s += A[i][k]*B[k][j]
            B[i][j] = sp.expand(-s)
    # P_lam = sum_nu (K^{-1})_{lam nu} s_nu  =>  A = K^{-1}, so K = B
    # K_{nu mu}: Q'_mu = sum_nu K_{nu mu} s_nu.  B = A^{-1} means sum_j A[i][j]B[j][k]=delta
    # i.e. sum_nu (K^{-1})_{lam nu} B[nu][mu] = delta_{lam mu}  =>  B[nu][mu] = K_{nu mu}. OK.
    K = {(order[i], order[j]): B[i][j] for i in range(N) for j in range(N)}
    with open(f,'wb') as fh: pickle.dump((order, K), fh)
    return order, K

def Y(n, lam, rho):
    order, K = kostka_matrix(n)
    return sp.expand(sum(K[(nu, lam)]*hl.chi(nu, tuple(rho)) for nu in order))

def G(n, lam, rho):
    num = sp.Integer(1)
    for r in rho: num *= (1 - t**r)
    return sp.cancel(num * Y(n, lam, rho) / b_lam(lam))
