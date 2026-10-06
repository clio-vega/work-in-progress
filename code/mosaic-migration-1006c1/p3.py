"""Why were the half-integer candidates never chosen?

346 of 3111 steps had a 2-candidate pool containing a bare-dphi = +-1/2 move,
and the chosen move always had dphi = 1.  Hypothesis: the rejected candidate
is the one whose rhombus orientation violates Purbhoo Prop 3.1 (rtype not in
{(0,150),(60,30)}), and it is rejected by (P3), the horizontal/vertical
tie-break.  If so, (P3) IMPLIES Prop 3.1 rather than being independent of it.
"""
import sys, collections
sys.path.insert(0,'/home/clio/projects/work-in-progress/code/mosaic-migration-1005c3')
from fractions import Fraction
from mosaic import *
from mosaic import _sign_surd
import step as ST
from step import journey2
from migrate import nestA_rhombi
ALLOWED={(0,150),(60,30)}
def phi(t): return Fraction(sum(v[1]+v[3] for v in t),4)
def rtype(t):
    ds=[DIR2ANG[sub(t[(i+1)%4],t[i])] for i in range(4)]
    z=sorted({a%180 for a in ds if a%180 in (0,60,120)})
    o=sorted({a%180 for a in ds if a%180 in (30,90,150)})
    return (z[0],o[0])
REJ=[]; _cm=ST.candidate_moves
def one(tiles,diamond,theta,visited):
    cand=_cm(tiles,diamond,theta,visited)
    ST.STATS['steps']+=1
    if not cand: return None
    if len(cand)==1: c=cand[0]
    else:
        hv=[x for x in cand if x[3]]
        if len(hv)==1: c=hv[0]
        else: c=max(hv if hv else cand,key=lambda z:(z[4][0]+2*z[4][1]))
    for x in cand:
        if x is c: continue
        REJ.append(dict(dphi=phi(x[1])-phi(diamond), rt=rtype(x[1]),
                        allowed=rtype(x[1]) in ALLOWED, hv=x[3],
                        chosen_hv=c[3], chosen_dphi=phi(c[1])-phi(diamond),
                        chosen_rt=rtype(c[1])))
    return set(tiles)-set(c[5])|set(c[0]), c[1], c[2]
ST.one_step=one
import step; step.one_step=one
def parts(dd,mm):
    out=[]
    def rec(p,k,mx):
        if k==dd: out.append(tuple(x for x in p if x>0)); return
        for v in range(mx,-1,-1): rec(p+[v],k+1,v)
    rec([],0,mm); return out
for (n,d) in [(4,2),(5,2),(5,3),(6,3)]:
    idx,_=nest_index(n,d); tgt={t for t,(nm,i,j) in idx.items() if nm=='B'}; m=n-d
    for al in parts(d,m):
      for be in parts(d,m):
        for ga in parts(d,m):
          if sum(al)+sum(be)+sum(ga)!=d*m: continue
          for M in mosaics_with_boundary(n,d,al,be,ga):
              rem=[t for t,i,j in nestA_rhombi(n,d,M)]; tl=set(M); pr=True
              while rem and pr:
                  pr=False
                  for k,t in enumerate(rem):
                      try: tl2,nt,s,kk=journey2(tl,t,150,tgt)
                      except RuntimeError: continue
                      tl=tl2; rem=rem[:k]+rem[k+1:]; pr=True; break
print('rejected candidates:', len(REJ))
print()
print('rejected: Prop-3.1-allowed orientation?')
for k,v in sorted(collections.Counter(r['allowed'] for r in REJ).items(),key=str):
    print('    allowed=%s : %d' % (k,v))
print('rejected: rtype distribution:', dict(collections.Counter(str(r['rt']) for r in REJ)))
print('rejected: hv flag:', dict(collections.Counter(r['hv'] for r in REJ)))
print('chosen (in these pools): hv flag:', dict(collections.Counter(r['chosen_hv'] for r in REJ)))
print('chosen (in these pools): allowed?', dict(collections.Counter(
      str(r['chosen_rt'] in ALLOWED) for r in REJ)))
print()
print('CONTROL: any rejected candidate with an ALLOWED orientation?',
      sum(1 for r in REJ if r['allowed']))
print('CONTROL: any chosen candidate with a FORBIDDEN orientation?',
      sum(1 for r in REJ if r['chosen_rt'] not in ALLOWED))
