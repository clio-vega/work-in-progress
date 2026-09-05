"""entry.py -- the witness entry from the (verified) Claim S closed form.

  <mu|C_k|0> = sum_{T subset [k-1]} (-1)^{|T|} (-1)^{r_T - 1} t^{j+1-r_T},
  rho_T = (sorted T increasing, k, sorted [k-1]\T decreasing),
  r_T   = min{ i : e_{rho_T(1)} + ... + e_{rho_T(i)} > j },  j = f_{k-1}.
"""
import itertools, sympy as sp
t = sp.Symbol('t')

def r_of(rho, es, j):
    s = 0
    for i, sl in enumerate(rho, 1):
        s += es[sl - 1]
        if s > j: return i
    raise RuntimeError('no threshold')  # cannot happen: total E > j

def rho_T(T, k):
    return tuple(sorted(T)) + (k,) + tuple(sorted(set(range(1, k)) - set(T), reverse=True))

def entry(es):
    """es = (e_1,...,e_k) in SLOT order (e_k innermost)."""
    k = len(es); j = sorted(es)[-2]
    tot = 0
    for size in range(k):
        for T in itertools.combinations(range(1, k), size):
            r = r_of(rho_T(T, k), es, j)
            tot += (-1)**len(T) * (-1)**(r - 1) * t**(j + 1 - r)
    return sp.expand(tot)
