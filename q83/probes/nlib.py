"""nlib.py -- Q83 Phase 0.  The operator N_e = E_e(-1) and iterated ad_{p_a}.

N_e : |lam> -> sum_mu (-1)^{ht(mu/lam)} |mu>, over mu/lam of size e,
      NO 2x2, EXACTLY 2 connected components.        (Q75 thm:Q75 at t=-1)
M_a : |lam> -> sum_mu (-1)^{ht(mu/lam)} |mu>, over mu/lam a genuine e-ribbon
      (size e, 1 component, no 2x2).  = multiplication by p_e (Murnaghan-Nakayama).

Everything below is on the SCHUR basis, states are dicts {partition: int}.
Shape engine only (symfunc.shape_stats); a bead-model cross-check lives in beads.py.
"""
import sys, itertools
sys.path.insert(0, '/home/clio/projects/probes/2026-09-03-Q75')
from functools import lru_cache
from symfunc import boxes, shape_stats, trim

@lru_cache(maxsize=None)
def add_shapes(lam, e):
    """all mu >= lam (containment) with |mu/lam| = e, as a tuple of partitions."""
    lam = trim(lam)
    R = len(lam) + e
    pad = lam + (0,) * (R - len(lam))
    out = []
    def rec(i, rem, below):       # build rows from the bottom up
        if i < 0:
            if rem == 0:
                out.append(trim(tuple(cur)))
            return
        lo = max(pad[i], below)
        for v in range(lo, pad[i] + rem + 1):
            d = v - pad[i]
            if d > rem: break
            cur[i] = v
            rec(i - 1, rem - d, v)
    cur = [0] * R
    rec(R - 1, e, 0)
    return tuple(out)

@lru_cache(maxsize=None)
def _op_row(lam, e, want_c):
    """{mu: (-1)^h} over mu/lam of size e, no 2x2, exactly want_c components."""
    out = {}
    for mu in add_shapes(lam, e):
        c, h, sq = shape_stats(mu, lam)
        if sq or c != want_c: continue
        out[mu] = out.get(mu, 0) + (-1) ** h
    return tuple(sorted((k, v) for k, v in out.items() if v))

def apply(e, want_c, state):
    out = {}
    for lam, w in state.items():
        for mu, u in _op_row(lam, e, want_c):
            out[mu] = out.get(mu, 0) + w * u
    return {k: v for k, v in out.items() if v}

def sub(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) - v
    return {k: v for k, v in out.items() if v}

def ad_p(a, opfun):
    """[M_{p_a}, opfun] as a function lam -> state."""
    def f(lam):
        s = opfun(lam)
        return sub(apply(a, 1, s), opfun_state(opfun, apply(a, 1, {trim(lam): 1})))
    return f

def opfun_state(opfun, state):
    out = {}
    for lam, w in state.items():
        for mu, u in opfun(lam).items():
            out[mu] = out.get(mu, 0) + w * u
    return {k: v for k, v in out.items() if v}

def N_fun(e):
    return lambda lam: dict(_op_row(trim(lam), e, 2))

def M_fun(e):
    return lambda lam: dict(_op_row(trim(lam), e, 1))

def T(alist, e):
    """ad_{p_{a_1}} ... ad_{p_{a_r}} ( N_e ), as a function lam -> state."""
    f = N_fun(e)
    for a in reversed(alist):
        f = ad_p(a, f)
    return f
