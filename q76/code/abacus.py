"""abacus.py -- the Maya-diagram (bead) model of R_e(t), and a cross-check
against the direct Young-diagram model in probes/2026-09-03-Q75/symfunc.py.

Conventions (fixed here once, and NOT tuned later):
  beta-set of lam with L runners:  B_L(lam) = { lam_i + L - i : 1 <= i <= L },
  a subset of Z_{>=0} of size L.  (This is the charge-0 beta set shifted by L.)
  Adding an e-ribbon  <->  b in B, b+e not in B, B -> B - {b} + {b+e}.
  Height h = #(B cap (b, b+e))  (beads strictly jumped over).
"""
import sys
sys.path.insert(0, '/home/clio/projects/probes/2026-09-03-Q75')
import sympy as sp
from symfunc import parts_of, parts_upto, trim, boxes, shape_stats, contains

t = sp.Symbol('t')

def beta(lam, L):
    lam = tuple(trim(lam))
    assert len(lam) <= L
    lam = lam + (0,) * (L - len(lam))
    return tuple(sorted(lam[i] + L - 1 - i for i in range(L)))

def unbeta(B, L):
    B = sorted(B, reverse=True)
    assert len(B) == L
    return trim(tuple(B[i] - (L - 1 - i) for i in range(L)))

def R_abacus(lam, e, L):
    """{mu : t^h} for mu obtained from lam by adding an e-ribbon."""
    B = set(beta(lam, L))
    out = {}
    for b in sorted(B):
        if b + e in B:
            continue
        h = sum(1 for c in B if b < c < b + e)
        mu = unbeta((B - {b}) | {b + e}, L)
        out[mu] = out.get(mu, 0) + t**h
    return out

def R_direct(lam, e, N):
    """same, by direct enumeration of skew shapes: connected, size e, no 2x2."""
    lam = trim(lam)
    out = {}
    for mu in parts_of(sum(lam) + e):
        if not contains(mu, lam):
            continue
        c, h, sq = shape_stats(mu, lam)
        if len(boxes(mu, lam)) == e and c == 1 and not sq:
            out[mu] = out.get(mu, 0) + t**h
    return out
