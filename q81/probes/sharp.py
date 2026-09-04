"""sharp.py -- sharpness for larger k, via the reduction formula ONLY
(no abacus, no nested-word expansion).  Tests whether

    D(Q) := ad_{p_e1} ... ad_{p_e_{k-2}} ( [M_{p_ek}, N_{e_{k-1}}] - [M_{p_e_{k-1}}, N_ek] )

is a nonzero operator, i.e. whether gcd of C_k's entries is exactly (1+t).
Operators are sparse dicts {lam: {mu: int}} built from skew-shape statistics.
"""
import sys, itertools
sys.path.insert(0, '/home/clio/projects/probes/2026-09-03-Q75')
from symfunc import parts_of, shape_stats, contains, trim
from functools import lru_cache

@lru_cache(maxsize=None)
def _row(lam, e, want_c):
    out = {}
    for mu in parts_of(sum(lam) + e):
        if not contains(mu, lam): continue
        c, h, sq = shape_stats(mu, lam)
        if sq or c != want_c: continue
        out[mu] = (-1)**h
    return tuple(sorted(out.items()))

def apply_op(e, want_c, state):
    out = {}
    for lam, w in state.items():
        for mu, u in _row(lam, e, want_c):
            out[mu] = out.get(mu, 0) + w*u
    return {k: v for k, v in out.items() if v}

def sub(a, b):
    o = dict(a)
    for k, v in b.items(): o[k] = o.get(k, 0) - v
    return {k: v for k, v in o.items() if v}

def run(es, lams):
    k = len(es)
    def base(lam):                       # Q_{e_{k-1},e_k}(-1) applied to |lam>
        s = {trim(lam): 1}
        A = apply_op(es[k-1], 1, apply_op(es[k-2], 2, s))   # M_{p_ek} N_{e_{k-1}}
        B = apply_op(es[k-2], 2, apply_op(es[k-1], 1, s))
        C = apply_op(es[k-2], 1, apply_op(es[k-1], 2, s))   # M_{p_e_{k-1}} N_{ek}
        D = apply_op(es[k-1], 2, apply_op(es[k-2], 1, s))
        return sub(sub(A, B), sub(C, D))
    cur = base
    for j in range(k-2, 0, -1):          # outermost ad applied last
        e = es[j-1]
        def nxt(lam, cur=cur, e=e):
            return sub(apply_op(e, 1, cur(lam)), cur_shift(cur, e, lam))
        cur = nxt
    return {lam: cur(lam) for lam in lams}

def cur_shift(cur, e, lam):
    """(X M_{p_e}) |lam> = X ( p_e . s_lam )"""
    out = {}
    for nu, w in apply_op(e, 1, {trim(lam): 1}).items():
        for mu, u in cur(nu).items(): out[mu] = out.get(mu, 0) + w*u
    return {k: v for k, v in out.items() if v}

if __name__ == '__main__':
    EMAX = int(sys.argv[1]); K = int(sys.argv[2]); NMAX = int(sys.argv[3])
    lams = [lam for n in range(NMAX+1) for lam in parts_of(n)]
    for es in itertools.combinations(range(2, EMAX+1), K):
        res = run(list(es), lams)
        nz = {l: len(v) for l, v in res.items() if v}
        tot = sum(len(v) for v in res.values())
        print(f'k={K} es={es}: nonzero entries {tot} over {len(lams)} lambdas; '
              f'{"SHARP (gcd = 1+t)" if tot else "*** VANISHES -- gcd divisible by (1+t)^2 ***"}',
              flush=True)
