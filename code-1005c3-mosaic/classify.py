"""Exhaustive classification of migration steps.

A step rotates a hexagon of type (a) (centrally symmetric, 3 zone directions) or
type (b) (3-fold symmetric).  Enumerate EVERY such hexagon up to translation,
EVERY tiling of it, EVERY rhombus in that tiling, and EVERY admissible rotation,
and record the change in the height  phi(v) = b + e  (v = a*u0+b*u60+c*u30+e*u90).
"""
import sys, collections, itertools
sys.path.insert(0,'.')
from fractions import Fraction
from mosaic import *
from mosaic import _rot_about, _sign_surd
from migrate import is_convex, hexagon_symmetry

THETA = 150
# Proposition 3.1: during a migration the travelling rhombus takes only two of the
# three nest orientations.  For A -> B these are the nest-A type (edges 0,150) and
# the nest-B type (edges 60,30).
ALLOWED = {(0,150), (60,30)}
def rtype(t):
    ds=[DIR2ANG[sub(t[(i+1)%4],t[i])] for i in range(4)]
    z=sorted({a%180 for a in ds if a%180 in (0,60,120)})
    o=sorted({a%180 for a in ds if a%180 in (30,90,150)})
    return (z[0],o[0])
def phi_v(v): return v[1] + v[3]
def phi(tile): return Fraction(sum(phi_v(v) for v in tile), 4)
def prog(tile):
    u = DIR[THETA]; P=Q=0
    for v in tile:
        p,q = dot_surd(v,u); P+=p; Q+=q
    return (P,Q)
def fwd(a,b):   # sign of prog(a)-prog(b)
    return _sign_surd(a[0]-b[0], a[1]-b[1])

def poly_from_dirs(dirs):
    v=(0,0,0,0); out=[v]
    for dd in dirs[:-1]:
        v=add(v,DIR[dd]); out.append(v)
    assert add(v,DIR[dirs[-1]])==(0,0,0,0), dirs
    return out

HEXES=[]
# type (a): zonogon on three distinct directions (angles in [0,180))
for trip in itertools.combinations([0,30,60,90,120,150],3):
    ds=list(trip)+[(x+180)%360 for x in trip]
    try: P=poly_from_dirs(ds)
    except AssertionError: continue
    HEXES.append(('a',tuple(reversed(P))))
# type (b): 3-fold, boundary p,q,Rp,Rq,R2p,R2q
for p in range(0,360,30):
    for q in range(0,360,30):
        ds=[p,q,(p+120)%360,(q+120)%360,(p+240)%360,(q+240)%360]
        try: P=poly_from_dirs(ds)
        except AssertionError: continue
        HEXES.append(('b',tuple(reversed(P))))

seen=set(); table=collections.Counter(); offenders=[]
nhex=0
for kind,P in HEXES:
    Pn=tuple(sorted(P,key=key))
    if Pn in seen: continue
    seen.add(Pn)
    cyc=list(P)
    if not is_convex(cyc): continue
    sym=hexagon_symmetry(cyc)
    if sym is None: continue
    nhex+=1
    ssum=[sum(v[k] for v in cyc) for k in range(4)]
    rots=[(lambda z: neg(z),'180')] if sym=='2' else [(rot120,'120'),(rot240,'240')]
    u = DIR[THETA]
    hexmin = min((dot_surd(v,u) for v in cyc), key=lambda z: (0,))
    hexmin = None
    for v in cyc:
        z = dot_surd(v,u)
        if hexmin is None or surd_lt(z,hexmin): hexmin = z
    for T in tilings(list(P)):
        if sum(1 for t in T if tile_kind(t)==RHOMB)!=1: continue
        for t in T:
            if tile_kind(t)!=RHOMB: continue
            # Purbhoo: the hexagon lies entirely weakly right of the LEFTMOST POINT
            # of the rhombus, so the hexagon's leftmost point is the rhombus's.
            dmin = None
            for v in t:
                z = dot_surd(v,u)
                if dmin is None or surd_lt(z,dmin): dmin = z
            if dmin != hexmin: continue
            if rtype(t) not in ALLOWED: continue       # Proposition 3.1
            for f,nm in rots:
                nt=canon(tuple(_rot_about(f,ssum,6,v) for v in t))
                if rtype(nt) not in ALLOWED: continue
                dphi=phi(nt)-phi(t)
                s=fwd(prog(nt),prog(t))
                dirs=[DIR2ANG[sub(nt[(i+1)%4],nt[i])] for i in range(4)]
                hv=any((a-THETA)%180 in (0,90) for a in dirs)
                table[(sym,s,dphi,hv)]+=1
                if s>=0 and dphi!=1: offenders.append((sym,nm,s,dphi,hv,t,nt))
print('distinct hexagon regions (up to translation):',nhex)
print()
print('%-4s %-9s %-6s %-6s  count' % ('sym','progress','dphi','h/v'))
for k in sorted(table, key=lambda z:(z[0],z[1],str(z[2]))):
    sym,s,dp,hv=k
    print('%-4s %-9s %-6s %-6s  %d'%(sym,{1:'forward',0:'vertical',-1:'backward'}[s],dp,hv,table[k]))
print()
print('FORWARD-OR-VERTICAL steps with dphi != 1 :', len(offenders))
bysig=collections.Counter((o[0],o[2],o[3],o[4]) for o in offenders)
for k,v in sorted(bysig.items(), key=str): print('   sym=%s progress=%s dphi=%s h/v=%s : %d'%(k[0],{1:'forward',0:'vertical',-1:'backward'}[k[1]],k[2],k[3],v))
