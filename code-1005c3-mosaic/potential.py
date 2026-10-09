"""Is there a function phi on rhombus positions with  phi(after) - phi(before) = 1
for EVERY migration step?  If so ell(M) = sum_{end cells} phi - sum_{start cells} phi
depends only on the boundary (alpha,beta,gamma) -- which proves both observations
(constant on fibres, independent of the order) at once.

Ansatz:  phi(tile) = L(s) + c_t,  s = sum of the four vertices in Z^4 (= 4*centroid),
L a linear form on Q^4, t the rhombus type (which 0-direction, which 1-direction).
"""
import sys, itertools, collections
sys.path.insert(0,'.')
from fractions import Fraction
from mosaic import *
from migrate import nestA_rhombi
import step as ST
from step import journey2

LOG = []
_orig = ST.one_step
def logged(tiles, diamond, theta, visited):
    r = _orig(tiles, diamond, theta, visited)
    if r is not None: LOG.append((diamond, r[1], r[2]))
    return r
ST.one_step = logged
import step
step.one_step = logged

def rtype(t):
    ds = [DIR2ANG[sub(t[(i+1)%4], t[i])] for i in range(4)]
    z = sorted({a % 180 for a in ds if a % 180 in (0,60,120)})
    o = sorted({a % 180 for a in ds if a % 180 in (30,90,150)})
    return (z[0], o[0])

def vsum(t):
    return tuple(sum(v[k] for v in t) for k in range(4))

def collect(cases):
    for (n,d) in cases:
        idx,_ = nest_index(n,d)
        tgt = {t for t,(nm,i,j) in idx.items() if nm=='B'}
        P=[]
        def parts(dd,mm):
            out=[]
            def rec(p,k,mx):
                if k==dd: out.append(tuple(x for x in p if x>0)); return
                for v in range(mx,-1,-1): rec(p+[v],k+1,v)
            rec([],0,mm); return out
        m=n-d
        for al in parts(d,m):
          for be in parts(d,m):
            for ga in parts(d,m):
              if sum(al)+sum(be)+sum(ga)!=d*m: continue
              for M in mosaics_with_boundary(n,d,al,be,ga):
                  rem=[t for t,i,j in nestA_rhombi(n,d,M)]
                  tl=set(M)
                  prog=True
                  while rem and prog:
                      prog=False
                      for k,t in enumerate(rem):
                          try:
                              tl2,nt,s,kk = journey2(tl,t,150,tgt)
                          except RuntimeError: continue
                          tl=tl2; rem=rem[:k]+rem[k+1:]; prog=True; break

TYPES = [(0,30),(0,150),(60,30),(60,90),(120,90),(120,150)]

def solve():
    # unknowns: L0..L3, c_t for t in TYPES  (fix c_{TYPES[0]} = 0)
    names = ['L0','L1','L2','L3'] + ['c'+str(t) for t in TYPES]
    rows=[]; rhs=[]
    seen=set()
    for (b,a,kind) in LOG:
        sb, sa = vsum(b), vsum(a)
        tb, ta = rtype(b), rtype(a)
        key_=(tuple(x-y for x,y in zip(sa,sb)), tb, ta)
        if key_ in seen: continue
        seen.add(key_)
        row=[Fraction(x-y) for x,y in zip(sa,sb)] + [Fraction(0)]*len(TYPES)
        row[4+TYPES.index(ta)] += 1
        row[4+TYPES.index(tb)] -= 1
        rows.append(row); rhs.append(Fraction(1))
    # gauge: c_{TYPES[0]} = 0
    g=[Fraction(0)]*len(names); g[4]=Fraction(1); rows.append(g); rhs.append(Fraction(0))
    # gaussian elimination
    nr, nc = len(rows), len(names)
    A=[rows[i][:]+[rhs[i]] for i in range(nr)]
    piv=[]; r=0
    for c in range(nc):
        p=None
        for i in range(r,nr):
            if A[i][c]!=0: p=i; break
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        f=A[r][c]
        A[r]=[x/f for x in A[r]]
        for i in range(nr):
            if i!=r and A[i][c]!=0:
                f2=A[i][c]; A[i]=[x-f2*y for x,y in zip(A[i],A[r])]
        piv.append(c); r+=1
        if r==nr: break
    for i in range(r,nr):
        if all(A[i][c]==0 for c in range(nc)) and A[i][nc]!=0:
            return None, len(seen), names
    sol={}
    for i,c in enumerate(piv): sol[names[c]]=A[i][nc]
    for nm in names: sol.setdefault(nm, Fraction(0))
    return sol, len(seen), names

if __name__=='__main__':
    collect([(4,2),(5,2),(5,3)])
    print('migration steps logged:', len(LOG))
    sol, nd, names = solve()
    print('distinct local move signatures:', nd)
    if sol is None:
        print('NO such phi exists (the linear system is inconsistent)')
    else:
        print('phi exists.  phi(tile) = L(sum of vertices) + c_type   with')
        for nm in names: print('    %-12s = %s' % (nm, sol[nm]))
        # verify on every logged step
        bad=0
        def phi(t):
            s=vsum(t); L=sum(sol['L%d'%k]*s[k] for k in range(4))
            return L + sol['c'+str(rtype(t))]
        for (b,a,k) in LOG:
            if phi(a)-phi(b) != 1: bad+=1
        print('steps with phi(after)-phi(before) != 1 :', bad, 'of', len(LOG))
