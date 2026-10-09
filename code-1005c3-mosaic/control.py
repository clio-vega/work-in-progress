"""Positive control: #mosaics with boundary (alpha,beta,gamma) must equal the
Littlewood-Richardson number, computed by two INDEPENDENT mechanisms:
  - lr_count          (KTW puzzle transfer matrix, git/puzzles/lr_coefficients.py)
  - lr_tableaux       (direct LR-tableau enumeration, written here, no shared code)
"""
import sys, time
sys.path.insert(0,'.'); sys.path.insert(0,'/home/clio/git/puzzles')
from mosaic import *
from lr_coefficients import lr_count
from itertools import product as iproduct

def partitions_in_box(d, m):
    out=[]
    def rec(pref, k, mx):
        if k==d: out.append(tuple(x for x in pref if x>0)); return
        for v in range(mx, -1, -1): rec(pref+[v], k+1, v)
    rec([], 0, m); return out

def lr_tableaux(lam, mu, nu):
    """LR tableaux of shape lam/mu, content nu (English convention: rows weakly
    increase L->R, columns strictly increase top->bottom, reading word right-to-left
    top-to-bottom is a reverse lattice word).  Returns the list of fillings."""
    lam = list(lam); mu = list(mu)+[0]*(len(lam)-len(mu))
    if any(mu[i] > lam[i] for i in range(len(lam))): return []
    cells = [(i,j) for i in range(len(lam)) for j in range(mu[i], lam[i])]
    if len(cells) != sum(nu): return []
    order = sorted(cells, key=lambda c: (c[0], -c[1]))   # reading word order
    out=[]; T={}
    cnt=[0]*(len(nu)+1)
    def rec(k):
        if k==len(order): out.append(dict(T)); return
        (i,j)=order[k]
        for v in range(1, len(nu)+1):
            if cnt[v-1] >= nu[v-1]: continue
            if cnt[v-1]+1 > (cnt[v-2] if v>=2 else 10**9): continue   # lattice
            if (i,j+1) in T and T[(i,j+1)] < v: continue              # row weakly incr L->R
            if (i-1,j) in T and T[(i-1,j)] >= v: continue             # col strictly incr
            T[(i,j)]=v; cnt[v-1]+=1
            rec(k+1)
            cnt[v-1]-=1; del T[(i,j)]
    rec(0); return out

if __name__ == '__main__':
    import collections
    bad=0; tested=0; hi=[]
    for (n,d) in [(4,2),(5,2),(5,3),(6,3)]:
        m=n-d
        P = partitions_in_box(d,m)
        for al in P:
            for be in P:
                for ga in P:
                    if sum(al)+sum(be)+sum(ga) != d*m: continue
                    # boundary (alpha,beta,gamma) = (nu, mu, lam^vee)
                    nu, mu = al, be
                    lamv = ga
                    lam = tuple(m - lamv[d-1-k] if d-1-k < len(lamv) else m
                                for k in range(d))
                    lam = tuple(x for x in lam if x>0)
                    c1 = lr_count(list(mu), list(nu), list(lam))   # lr_count(a,b,c) = c^c_{a,b}
                    c2 = len(lr_tableaux(lam, mu, nu))
                    t0=time.time()
                    M  = mosaics_with_boundary(n,d,al,be,ga)
                    dt=time.time()-t0
                    tested+=1
                    if not (len(M)==c1==c2):
                        bad+=1
                        print('MISMATCH n=%d d=%d  a=%s b=%s g=%s  | lam=%s mu=%s nu=%s | mosaics=%d puzzles=%d tableaux=%d'
                              %(n,d,al,be,ga,lam,mu,nu,len(M),c1,c2))
                    if c2>=2: hi.append((n,d,al,be,ga,lam,mu,nu,len(M),c1,c2,dt))
        print('n=%d d=%d done, tested=%d mismatches=%d'%(n,d,tested,bad))
    print()
    print('--- fibres with multiplicity >= 2 (the cases a mult-1 sweep cannot see) ---')
    for h in sorted(hi, key=lambda z:-z[9])[:12]:
        print('  n=%d d=%d  lam=%s mu=%s nu=%s  mosaics=%d puzzles=%d tableaux=%d  (%.1fs)'
              %(h[0],h[1],h[5],h[6],h[7],h[8],h[9],h[10],h[11]))
    print('TOTAL tested=%d  mismatches=%d  mult>=2 fibres=%d'%(tested,bad,len(hi)))
