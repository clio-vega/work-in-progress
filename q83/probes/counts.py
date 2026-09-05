"""counts.py -- the signed counts of Q81 lem:chain/legal/height/sign, for general k.

Entry <mu|C_k|0> with mu=(E-j,1^j), j=f_{k-1}:
    sum_{rho in S_k}  Sigma(rho, r(rho)) * t^{j-r(rho)+1},
    Sigma(rho,r) = sum over linear extensions tau of P^{(r)} of eps(rho,tau),
    P^{(r)}: min r, chains r<r-1<..<1 and r<r+1<..<k,
    word w_l = rho(tau_l);  eps = (-1)^{q-1} if w unimodal with peak-value k at
    position q, else 0.
"""
import itertools, sys
from functools import lru_cache

@lru_cache(maxsize=None)
def lin_ext(k, r):
    """linear extensions of P^{(r)}: start with r, interleave (r-1..1) and (r+1..k)."""
    down = list(range(r - 1, 0, -1))
    up = list(range(r + 1, k + 1))
    out = []
    def rec(i, jx, cur):
        if i == len(down) and jx == len(up):
            out.append(tuple([r] + cur)); return
        if i < len(down): rec(i + 1, jx, cur + [down[i]])
        if jx < len(up): rec(i, jx + 1, cur + [up[jx]])
    rec(0, 0, [])
    return tuple(out)

def eps(w, k):
    """(-1)^{q-1} if w is unimodal with peak value k; else 0."""
    q = w.index(k) + 1
    if any(w[i] >= w[i + 1] for i in range(q - 1)): return 0
    if any(w[i] <= w[i + 1] for i in range(q - 1, len(w) - 1)): return 0
    return (-1) ** (q - 1)

def Sigma(rho, r, k):
    return sum(eps(tuple(rho[tt - 1] for tt in tau), k) for tau in lin_ext(k, r))

for k in range(3, 8):
    print(f'=== k={k} ===')
    for r in range(1, k + 1):
        tot = {}
        for rho in itertools.permutations(range(1, k + 1)):
            s = Sigma(rho, r, k)
            if s: tot[rho] = s
        # group by m = slot of the largest size = position of value k?? no:
        # r(rho)=1 iff rho(1)=m.  Record the full multiset and the sum.
        print(f'  r={r}: #rho with Sigma!=0 : {len(tot)}   total sum over ALL rho = {sum(tot.values())}')
        if r >= 2 and len(tot) <= 30:
            for rho, s in sorted(tot.items()): print('        ', rho, s)

# ---------------- claim S: Sigma(rho,r) = (-1)^{r-1} (-1)^{q-1} [rho unimodal peak k]
def is_unimodal_peak_k(rho, k):
    q = rho.index(k) + 1
    if any(rho[i] >= rho[i+1] for i in range(q-1)): return False
    if any(rho[i] <= rho[i+1] for i in range(q-1, len(rho)-1)): return False
    return True

def check_claimS(kmax=8):
    bad = 0
    for k in range(2, kmax+1):
        for rho in itertools.permutations(range(1, k+1)):
            q = rho.index(k) + 1
            pred0 = (-1)**(q-1) if is_unimodal_peak_k(rho, k) else 0
            for r in range(1, k+1):
                pred = (-1)**(r-1) * pred0
                got = Sigma(rho, r, k)
                if pred != got:
                    bad += 1
                    if bad <= 5: print('  CLAIM-S FAIL', k, rho, r, 'pred', pred, 'got', got)
        print(f'  claim S verified k={k} ({len(list(itertools.permutations(range(1,k+1))))*k} (rho,r) pairs), bad so far {bad}')
    return bad
