"""Was the dphi=-1 vertical slide ever AVAILABLE?

91 of 707 steps were strictly vertical and all 91 took dphi=+1.  But step.py
breaks a tie among equal-progress candidates with `max(..., key=progress)`,
which is CONSTANT on vertical candidates -- so `max` returns the first in list
order.  If the -1 slide was ever in the candidate pool, the 91/91 null is an
artifact of enumeration order, not a geometric fact.

This instruments candidate_moves and records, for every step, the full
candidate multiset labelled by (progress sign, dphi).
"""
import sys, collections
sys.path.insert(0,'/home/clio/projects/work-in-progress/code/mosaic-migration-1005c3')
from fractions import Fraction
from mosaic import *
from mosaic import _sign_surd
import step as ST
from step import candidate_moves, journey2
from migrate import nestA_rhombi

def phi_v(v): return v[1]+v[3]
def phi(t): return Fraction(sum(phi_v(v) for v in t),4)
def prog(t,theta):
    u=DIR[theta%360]; P=Q=0
    for v in t:
        p,q=dot_surd(v,u); P+=p; Q+=q
    return (P,Q)

POOLS=[]            # one entry per step: list of (progsign, dphi, hv)
CHOSEN=[]
_cm = ST.candidate_moves
_os = ST.one_step

def logged_one_step(tiles, diamond, theta, visited):
    cand = _cm(tiles, diamond, theta, visited)
    cur = prog(diamond, theta)
    rec=[]
    for c in cand:
        nd=c[1]
        p=prog(nd,theta)
        s=_sign_surd(p[0]-cur[0], p[1]-cur[1])
        rec.append((s, phi(nd)-phi(diamond), c[3]))
    r = _os(tiles, diamond, theta, visited)
    if r is not None:
        POOLS.append(rec)
        CHOSEN.append((_sign_surd(*[a-b for a,b in zip(prog(r[1],theta),cur)]),
                       phi(r[1])-phi(diamond)))
    return r

ST.one_step = logged_one_step
import step
step.one_step = logged_one_step
import potential   # potential.py rebinds step.one_step for its own LOG; re-patch after
step.one_step = logged_one_step
ST.one_step = logged_one_step

def parts(dd,mm):
    out=[]
    def rec(p,k,mx):
        if k==dd: out.append(tuple(x for x in p if x>0)); return
        for v in range(mx,-1,-1): rec(p+[v],k+1,v)
    rec([],0,mm); return out

def run(cases):
    for (n,d) in cases:
        idx,_=nest_index(n,d)
        tgt={t for t,(nm,i,j) in idx.items() if nm=='B'}
        m=n-d
        nm_=0
        for al in parts(d,m):
          for be in parts(d,m):
            for ga in parts(d,m):
              if sum(al)+sum(be)+sum(ga)!=d*m: continue
              for M in mosaics_with_boundary(n,d,al,be,ga):
                  nm_+=1
                  rem=[t for t,i,j in nestA_rhombi(n,d,M)]
                  tl=set(M); progress=True
                  while rem and progress:
                      progress=False
                      for k,t in enumerate(rem):
                          try: tl2,nt,s,kk = journey2(tl,t,150,tgt)
                          except RuntimeError: continue
                          tl=tl2; rem=rem[:k]+rem[k+1:]; progress=True; break
        print('  (n,d)=(%d,%d): %d mosaics' % (n,d,nm_))

run([(4,2),(5,2),(5,3),(6,3)])

print()
print('steps logged:', len(POOLS))
nvert_chosen = sum(1 for c in CHOSEN if c[0]==0)
print('steps whose CHOSEN move was strictly vertical:', nvert_chosen)
print('  of those, dphi=+1:', sum(1 for c in CHOSEN if c[0]==0 and c[1]==1))
print('  of those, dphi=-1:', sum(1 for c in CHOSEN if c[0]==0 and c[1]==-1))
print()
# THE control: was a vertical dphi=-1 candidate ever in the pool?
avail = [i for i,rec in enumerate(POOLS) if any(s==0 and dp==-1 for s,dp,hv in rec)]
print('steps where a vertical dphi=-1 candidate was AVAILABLE:', len(avail))
availup = [i for i,rec in enumerate(POOLS) if any(s==0 and dp==1 for s,dp,hv in rec)]
print('steps where a vertical dphi=+1 candidate was AVAILABLE:', len(availup))
both = [i for i in avail if i in set(availup)]
print('steps where BOTH vertical candidates were available:', len(both))
print()
print('pool-size distribution:', dict(collections.Counter(len(r) for r in POOLS)))
print('candidate labels overall (progsign,dphi) -> count:')
for k,v in sorted(collections.Counter(
        (s,dp) for r in POOLS for s,dp,hv in r).items(), key=str):
    print('   progress=%-9s dphi=%-4s : %d' % ({1:'forward',0:'vertical',-1:'backward'}[k[0]],k[1],v))
