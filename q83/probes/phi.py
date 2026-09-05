"""phi.py -- THE CLOSED FORM.  For lambda=empty, mu=(E-j,1^j), 0<=j<=E-1:

  <mu| C_k |0>  =  sgn(e_k - e_{k-1}) (1+t) * sum_{T in S_j} t^{j-1-|T|},
  S_j = { T subset [k-2] : Sigma_T + e_min <= j < Sigma_T + e_max }.

Equivalently, with Phi(x) = (x^{e_{k-1}} - x^{e_k})/(1-x) * prod_{i<=k-2}(1-x^{e_i}):

  <mu| C_k/(1+t) |0> |_{t=-1}  =  (-1)^{j-1} [x^j] Phi(x).

Phi != 0 in Z[x] ALWAYS (integral domain, e_{k-1} != e_k), so some j works.
"""
import sympy as sp
t, x = sp.symbols('t x')

def entry_j(es, j):
    k = len(es); emin, emax = min(es[-2], es[-1]), max(es[-2], es[-1])
    sgn = 1 if es[-1] > es[-2] else -1
    tot = 0
    for mask in range(1 << (k - 2)):
        T = [es[i] for i in range(k - 2) if mask >> i & 1]
        S = sum(T)
        if S + emin <= j < S + emax:
            tot += t ** (j - 1 - len(T))
    return sp.expand(sgn * (1 + t) * tot)

def Phi(es):
    k = len(es)
    p = sp.cancel((x**es[-2] - x**es[-1]) / (1 - x))
    for i in range(k - 2): p *= (1 - x**es[i])
    return sp.expand(sp.cancel(p))
