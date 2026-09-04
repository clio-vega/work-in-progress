"""reduction.py -- INDEPENDENT verification of the reduction formula

    C_k/(1+t) |_{t=-1}  =  ad_{p_{e1}} ... ad_{p_{e_{k-2}}} ( Q_{e_{k-1},e_k}(-1) ),
    Q_{a,b}(-1) = [M_{p_b}, N_a] - [M_{p_a}, N_b],

where (Q75 Thm A / Cor T1 / Cor T2, all `proved`)
    M_{p_e}: entry (-1)^h on mu/lam a genuine e-ribbon (size e, c=1, no 2x2), else 0
    N_e := E_e(-1): entry (-1)^h on mu/lam of size e, no 2x2, EXACTLY c=2, else 0.

LHS comes from the Maya/abacus engine (bead hops).  RHS comes only from
skew-shape statistics via symfunc.shape_stats.  The two share no code.
"""
import sys, itertools, sympy as sp
sys.path.insert(0, '.'); sys.path.insert(0, '/home/clio/projects/probes/2026-09-04-Q76')
sys.path.insert(0, '/home/clio/projects/probes/2026-09-03-Q75')
from nested import C, t
from abacus import parts_of
from symfunc import boxes, shape_stats, contains, trim

def shape_op(e, want_c):
    """operator as a function lam -> {mu: coeff}, on shapes of size e with c components."""
    def op(lam):
        lam = trim(lam); out = {}
        for mu in parts_of(sum(lam) + e):
            if not contains(mu, lam): continue
            c, h, sq = shape_stats(mu, lam)
            if sq or c != want_c: continue
            out[mu] = out.get(mu, 0) + (-1)**h
        return out
    return op

def act(op, state):
    out = {}
    for lam, w in state.items():
        for mu, u in op(lam).items(): out[mu] = out.get(mu, 0) + w*u
    return {k: v for k, v in out.items() if v != 0}

def comm(op1, op2):
    """returns an operator lam -> {mu: coeff} for [op1, op2]."""
    def op(lam):
        a = act(op1, act(op2, {trim(lam): 1}))
        b = act(op2, act(op1, {trim(lam): 1}))
        out = dict(a)
        for k, v in b.items(): out[k] = out.get(k, 0) - v
        return {k: v for k, v in out.items() if v != 0}
    return op

def main(NMAX, EMAX, K):
    bad = tot = nz = 0
    for es in itertools.combinations(range(2, EMAX + 1), K):
        Ms = [shape_op(e, 1) for e in es]      # M_{p_e}
        Ns = [shape_op(e, 2) for e in es]      # N_e = E_e(-1)
        inner = comm(Ms[K-1], Ns[K-2])         # [M_{p_e_k}, N_{e_{k-1}}]
        inner2 = comm(Ms[K-2], Ns[K-1])        # [M_{p_e_{k-1}}, N_{e_k}]
        def RHSop(lam, inner=inner, inner2=inner2, Ms=Ms):
            d = inner(lam)
            for k_, v in inner2(lam).items(): d[k_] = d.get(k_, 0) - v
            d = {k_: v for k_, v in d.items() if v != 0}
            return d
        cur = RHSop
        for j in range(K-2, 0, -1):            # apply ad_{M_{p_{e_j}}} outermost last
            cur = comm(Ms[j-1], cur)
        for n in range(0, NMAX + 1):
            for lam in parts_of(n):
                L = n + sum(es) + 6
                lhs = {mu: sp.expand(sp.cancel(v/(1+t))).subs(t, -1)
                       for mu, v in C(list(es), lam, L).items()}
                lhs = {k_: v for k_, v in lhs.items() if v != 0}
                rhs = cur(lam)
                keys = set(lhs) | set(rhs)
                for mu in keys:
                    tot += 1
                    a = sp.Integer(lhs.get(mu, 0)); b = sp.Integer(rhs.get(mu, 0))
                    if a != 0: nz += 1
                    if a != b:
                        bad += 1
                        if bad <= 5: print('  MISMATCH', es, lam, mu, a, b, flush=True)
        print(f'  es={es} cumulative compared={tot} nonzero={nz} MISMATCH={bad}', flush=True)
    print(f'REDUCTION FORMULA k={K}: {tot} entries compared, {nz} nonzero, {bad} mismatches')
    return bad

if __name__ == '__main__':
    sys.exit(0 if main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])) == 0 else 1)
