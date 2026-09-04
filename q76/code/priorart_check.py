"""priorart_check.py -- verify, in my own engine, that Jing-Liu (arXiv 2310.15730, sec 4.2)
IS my Theorem A, rather than merely resembling it.

Their data, quoted verbatim from the e-print source by the prior-art agent:
   (a-1) sum_{r>=0} htilde_r(a) z^r  =  prod_i (1 - x_i z)/(1 - a x_i z)
   wt(theta;t) = (t-1)^{m-1} prod_{i=1}^m (-1)^{r(xi_i)-1} t^{c(xi_i)-1}
   htilde_r(q) s_mu = sum_lambda wt(lambda/mu; q) s_lambda   over r-generalized border strips.

Two INDEPENDENT checks, neither of which tunes anything:
  D1  the generating functions:  htilde_e(-t) == (-1)^{e-1} omega(f_e(t)) ?
  D2  the rules:  htilde_e(q) s_mu computed from THEIR weight formula, versus
      M_{f_e} s_mu conjugated and signed, entry by entry.
A negative control D3 perturbs the sign exponent, and must disagree.
"""
import sys, sympy as sp
sys.path.insert(0, '/home/clio/projects/probes/2026-09-03-Q75')
from symfunc import (parts_of, trim, schur_m, mult, to_schur, h_m, e_m, hook,
                     f_e_m, boxes, shape_stats, components, has_2x2, contains)

t, a = sp.symbols('t a')

def conj(lam):
    lam = trim(lam)
    return trim(tuple(sum(1 for p in lam if p > j) for j in range(lam[0] if lam else 0)))

# ---- D1: generating functions ----------------------------------------------
def htilde(e, a, nvars):
    """[z^e] of prod (1-x_i z)/(1-a x_i z), divided by (a-1)."""
    tot = {}
    for b in range(e + 1):                       # E(-z) H(az): e_b(-1)^b * h_{e-b} a^{e-b}
        term = mult(e_m(b), h_m(e - b), nvars) if b and e - b else (
            e_m(b) if b == e else h_m(e))
        for rho, c in term.items():
            tot[rho] = sp.expand(tot.get(rho, 0) + c * (-1)**b * a**(e - b))
    return {k: sp.expand(v / (a - 1)) for k, v in tot.items() if sp.expand(v) != 0}

print('D1  htilde_e(-t) vs (-1)^(e-1) omega f_e(t), in the Schur basis:')
for e in range(1, 6):
    lhs = to_schur({k: sp.expand(sp.simplify(v.subs(a, -t))) for k, v in htilde(e, a, e + 1).items()})
    rhs = {conj(hook(e, k)): sp.expand((-1)**(e - 1) * t**k) for k in range(e)}
    lhs = {k: sp.expand(v) for k, v in lhs.items() if sp.expand(v) != 0}
    print(f'   e={e}: {"MATCH" if lhs == rhs else "DIFFER"}   htilde_{e}(-t) = '
          f'{ {str(k): str(v) for k, v in sorted(lhs.items())} }')

# ---- D2: their weight rule vs mine, entrywise -------------------------------
def their_wt(mu, lam, q):
    """wt(mu/lam; q) as they define it; 0 if not a generalized border strip."""
    cells = boxes(mu, lam)
    if has_2x2(cells):
        return sp.Integer(0)
    comps = components(cells)
    m = len(comps)
    w = (q - 1)**(m - 1)
    for comp in comps:
        r = len(set(x for x, _ in comp)); c = len(set(y for _, y in comp))
        w *= (-1)**(r - 1) * q**(c - 1)
    return sp.expand(w)

def my_wt(mu, lam):
    """my Theorem A weight t^h (1+t)^{c-1}, 0 if a 2x2 is present."""
    cells = boxes(mu, lam)
    if has_2x2(cells): return sp.Integer(0)
    c, h, _ = shape_stats(mu, lam)
    return sp.expand(t**h * (1 + t)**(c - 1))

good = bad = nz = 0
badctl = 0
for e in range(1, 5):
    for n in range(0, 6):
        for lam in parts_of(n):
            for mu in parts_of(n + e):
                if not contains(mu, lam): continue
                theirs = their_wt(mu, lam, -t)
                mine = sp.expand((-1)**(e - 1) * my_wt(conj(mu), conj(lam)))
                good += 1
                if sp.expand(theirs - mine) != 0: bad += 1
                if theirs != 0: nz += 1
                # D3 negative control: drop the global (-1)^(e-1)
                if sp.expand(theirs - sp.expand(my_wt(conj(mu), conj(lam)))) != 0: badctl += 1
print(f'D2  wt(mu/lam;-t) == (-1)^(e-1) * [my weight for the CONJUGATE shape]: '
      f'{good-bad}/{good} skew shapes ({nz} nonzero)')
print(f'D3  negative control (drop the global sign) DISAGREES on {badctl}/{good}')
