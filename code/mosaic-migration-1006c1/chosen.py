"""Does the engine take steps the exhaustive classification never classified?

classify.py filters on `sum(1 for t in T if tile_kind(t)==RHOMB)!=1` -- exactly
ONE rhombus in the hexagon.  step.py imposes no such restriction.  Measure:
  (a) the dphi distribution of CHOSEN moves (bare height, no type correction);
  (b) how many rhombi the chosen hexagon actually contained.
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
def rtype(t):
    ds=[DIR2ANG[sub(t[(i+1)%4],t[i])] for i in range(4)]
    z=sorted({a%180 for a in ds if a%180 in (0,60,120)})
    o=sorted({a%180 for a in ds if a%180 in (30,90,150)})
    return (z[0],o[0])

REC=[]
_cm = ST.candidate_moves
def logged_one_step(tiles, diamond, theta, visited):
    cand = _cm(tiles, diamond, theta, visited)
    ST.STATS['steps'] += 1
    if not cand: return None
    if len(cand)==1: c=cand[0]
    else:
        hv=[x for x in cand if x[3]]
        if len(hv)==1: c=hv[0]
        else:
            pool = hv if hv else cand
            c = max(pool, key=lambda z:(z[4][0]+2*z[4][1]))
    cur=prog(diamond,theta); p=prog(c[1],theta)
    nrh = sum(1 for t in c[5] if tile_kind(t)==RHOMB)   # c[5] = hexagon tile set S
    REC.append(dict(prog=_sign_surd(p[0]-cur[0],p[1]-cur[1]),
                    dphi=phi(c[1])-phi(diamond),
                    nrhomb=nrh, nhex=len(c[5]),
                    tb=rtype(diamond), ta=rtype(c[1]), kind=c[2]))
    tl=set(tiles)-set(c[5])|set(c[0])
    return tl, c[1], c[2]
ST.one_step = logged_one_step
import step; step.one_step = logged_one_step

def parts(dd,mm):
    out=[]
    def rec(p,k,mx):
        if k==dd: out.append(tuple(x for x in p if x>0)); return
        for v in range(mx,-1,-1): rec(p+[v],k+1,v)
    rec([],0,mm); return out

for (n,d) in [(4,2),(5,2),(5,3),(6,3)]:
    idx,_=nest_index(n,d)
    tgt={t for t,(nm,i,j) in idx.items() if nm=='B'}
    m=n-d
    for al in parts(d,m):
      for be in parts(d,m):
        for ga in parts(d,m):
          if sum(al)+sum(be)+sum(ga)!=d*m: continue
          for M in mosaics_with_boundary(n,d,al,be,ga):
              rem=[t for t,i,j in nestA_rhombi(n,d,M)]
              tl=set(M); pr=True
              while rem and pr:
                  pr=False
                  for k,t in enumerate(rem):
                      try: tl2,nt,s,kk=journey2(tl,t,150,tgt)
                      except RuntimeError: continue
                      tl=tl2; rem=rem[:k]+rem[k+1:]; pr=True; break

print('chosen steps:', len(REC))
print()
print('(a) bare-height dphi of CHOSEN moves:')
for k,v in sorted(collections.Counter(r['dphi'] for r in REC).items(), key=lambda z:float(z[0])):
    print('    dphi = %-5s : %d' % (k,v))
print()
print('(b) #rhombi in the chosen hexagon:')
for k,v in sorted(collections.Counter(r['nrhomb'] for r in REC).items()):
    print('    %d rhombi : %d steps' % (k,v))
print('    #tiles in chosen hexagon:', dict(collections.Counter(r['nhex'] for r in REC)))
print()
print('(c) cross-tab: #rhombi in hexagon  x  bare dphi')
ct=collections.Counter((r['nrhomb'],r['dphi']) for r in REC)
for k in sorted(ct, key=lambda z:(z[0],float(z[1]))):
    print('    rhombi=%d dphi=%-5s : %d' % (k[0],k[1],ct[k]))
print()
print('(d) rhombus type before -> after, by move kind:')
for k,v in sorted(collections.Counter((r['kind'],r['tb'],r['ta']) for r in REC).items(), key=str):
    print('    kind=%s  %s -> %s : %d' % (k[0],k[1],k[2],v))
