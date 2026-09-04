"""verify.py -- exhaustive check of the closed form, with named negative controls.

Streams one line per configuration (lam-size, e, e') so a timeout still leaves a
partial count with a stated denominator.
"""
import sys, itertools, sympy as sp
sys.path.insert(0, '.')
from closedform import commutator_brute, predict
from abacus import t, beta, unbeta, R_abacus, parts_of, trim

def type_census(lam, mu, e, ep, L):
    """classify the (lam,mu) pair: returns (type, crossing?/split?, reachable?)"""
    B = set(beta(lam, L)); Bp = set(beta(mu, L))
    D = sorted(B - Bp); U = sorted(Bp - B)
    if len(D) != len(U):
        return ('unreachable', None)
    if len(D) == 1:
        b = D[0]
        if U[0] != b + e + ep:
            return ('unreachable', None)
        return ('ribbon', (b + e in B) != (b + ep in B))
    if len(D) == 2:
        b1, b2 = D
        cand = [(b, c) for (b, c) in ((b1, b2), (b2, b1)) if sorted([b + e, c + ep]) == U]
        if len(cand) != 1:
            return ('unreachable', None)
        b, c = cand[0]
        cross = (b < c < b + e < c + ep) or (c < b < c + ep < b + e)
        return ('pair', cross)
    return ('unreachable', None)

# --- negative controls, each a DELIBERATELY WRONG variant of the prediction ---
def predict_NC_noncross(lam, mu, e, ep, L):
    """NC2: same as predict, but Type 1 ignores the crossing condition."""
    B = set(beta(lam, L)); Bp = set(beta(mu, L))
    D = sorted(B - Bp); U = sorted(Bp - B)
    if len(D) == 2 and len(U) == 2:
        cand = [(b, c) for (b, c) in ((D[0], D[1]), (D[1], D[0])) if sorted([b + e, c + ep]) == U]
        if len(cand) == 1:
            b, c = cand[0]
            H = sum(1 for x in B if b < x < b + e) + sum(1 for x in B if c < x < c + ep)
            return sp.expand((1 if b < c else -1) * t**(H - 1) * (1 - t**2))
    return predict(lam, mu, e, ep, L)

def predict_NC_nosplit(lam, mu, e, ep, L):
    """NC3: same as predict, but Type 2 ignores which cut is vertical."""
    B = set(beta(lam, L)); Bp = set(beta(mu, L))
    D = sorted(B - Bp); U = sorted(Bp - B)
    if len(D) == 1 and len(U) == 1 and U[0] == D[0] + e + ep:
        b = D[0]
        N = sum(1 for c in B if b < c < b + e + ep)
        return sp.expand(t**(N - 1) * (1 + t))
    return predict(lam, mu, e, ep, L)

def main(NMAX, EMAX):
    tot = nz = bad = 0
    nc2 = nc3 = 0
    census = {}
    for n in range(0, NMAX + 1):
        for lam in parts_of(n):
            for (e, ep) in itertools.combinations(range(2, EMAX + 1), 2):
                L = n + e + ep + 6
                br = commutator_brute(lam, e, ep, L)
                targets = set(br) | set(parts_of(n + e + ep))
                for mu in targets:
                    a = sp.expand(br.get(mu, 0))
                    p = predict(lam, mu, e, ep, L)
                    tot += 1
                    if sp.expand(a - p) != 0:
                        bad += 1
                        if bad <= 3: print('  MISMATCH', lam, mu, e, ep, a, p, flush=True)
                    if a != 0: nz += 1
                    if sp.expand(a - predict_NC_noncross(lam, mu, e, ep, L)) != 0: nc2 += 1
                    if sp.expand(a - predict_NC_nosplit(lam, mu, e, ep, L)) != 0: nc3 += 1
                    ty, flag = type_census(lam, mu, e, ep, L)
                    census[(ty, flag)] = census.get((ty, flag), 0) + 1
        print(f'|lam|={n:2d}  cumulative entries={tot:7d} nonzero={nz:6d} '
              f'MISMATCH={bad}  NC2fires={nc2} NC3fires={nc3}', flush=True)
    print('census (type, flag) -> count:', flush=True)
    for k in sorted(census, key=str): print('   ', k, census[k], flush=True)
    return bad

if __name__ == '__main__':
    sys.exit(0 if main(int(sys.argv[1]), int(sys.argv[2])) == 0 else 1)
