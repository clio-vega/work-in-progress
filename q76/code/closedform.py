"""closedform.py -- the conjectured closed form for [R_e(t), R_{e'}(t)], and a
brute-force check against composition of the abacus operators.

PREDICTION (derived by hand, this session; see the paper).  Let B = beta(lam),
B' = beta(mu), D = B \ B', U = B' \ B.  For e != e':

  |D| = 1, D = {b}, U = {b+e+e'}:   ("Type 2", mu/lam is an (e+e')-ribbon)
      entry = ( [b+e in B] - [b+e' in B] ) * t^(N-1) * (1+t),  N = #(B cap (b,b+e+e'))

  |D| = 2:                          ("Type 1", two beads hop)
      find the unique bijection D -> U with displacement multiset {e,e'};
      let b hop by e and c hop by e'.  Then
      entry = +t^(H-1)(1-t^2) if b < c < b+e < c+e'   (the hops CROSS, b on the left)
              -t^(H-1)(1-t^2) if c < b < c+e' < b+e   (the hops CROSS, c on the left)
              0                otherwise,
      with H = #(B cap (b,b+e)) + #(B cap (c,c+e')).

  otherwise: 0.
"""
import sympy as sp
from abacus import t, beta, unbeta, R_abacus, parts_of, parts_upto, trim

def commutator_brute(lam, e, ep, L):
    """entry dict {mu: poly} of [R_e, R_e'] s_lam, by composing the abacus operators."""
    out = {}
    for sgn, (a, b) in ((1, (ep, e)), (-1, (e, ep))):
        # sgn * R_b R_a : apply R_a first
        for nu, w1 in R_abacus(lam, a, L).items():
            for mu, w2 in R_abacus(nu, b, L).items():
                out[mu] = sp.expand(out.get(mu, 0) + sgn * w1 * w2)
    return {k: v for k, v in out.items() if sp.expand(v) != 0}

def predict(lam, mu, e, ep, L):
    B = set(beta(lam, L)); Bp = set(beta(mu, L))
    D = sorted(B - Bp); U = sorted(Bp - B)
    if len(D) != len(U):
        return sp.Integer(0)
    if len(D) == 1:
        b = D[0]
        if U[0] != b + e + ep:
            return sp.Integer(0)
        N = sum(1 for c in B if b < c < b + e + ep)
        s = (1 if b + e in B else 0) - (1 if b + ep in B else 0)
        return sp.expand(s * t**(N - 1) * (1 + t))
    if len(D) == 2:
        b1, b2 = D
        cand = []
        for (b, c) in ((b1, b2), (b2, b1)):
            if sorted([b + e, c + ep]) == U:
                cand.append((b, c))
        if len(cand) != 1:
            return sp.Integer(0)      # e != e' => at most one; none => not reachable
        b, c = cand[0]
        H = sum(1 for x in B if b < x < b + e) + sum(1 for x in B if c < x < c + ep)
        if b < c < b + e < c + ep:
            return sp.expand(t**(H - 1) * (1 - t**2))
        if c < b < c + ep < b + e:
            return sp.expand(-t**(H - 1) * (1 - t**2))
        return sp.Integer(0)
    return sp.Integer(0)
