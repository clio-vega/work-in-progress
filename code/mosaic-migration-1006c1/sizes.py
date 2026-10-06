"""Classification of migration steps WITH the hexagon tile count.

Purbhoo 3.1 selects the SMALLEST hexagon containing the rhombus and lying
weakly right of its leftmost point.  If every configuration admitting the
dphi=-1 vertical slide also admits a STRICTLY SMALLER admissible hexagon,
the -1 slide is never selected.
"""
import sys, collections, itertools
sys.path.insert(0,'/home/clio/projects/work-in-progress/code/mosaic-migration-1005c3')
from fractions import Fraction
from mosaic import *
from mosaic import _rot_about, _sign_surd
from migrate import is_convex, hexagon_symmetry

THETA = 150
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
def fwd(a,b): return _sign_surd(a[0]-b[0], a[1]-b[1])
def poly_from_dirs(dirs):
    v=(0,0,0,0); out=[v]
    for dd in dirs[:-1]:
        v=add(v,DIR[dd]); out.append(v)
    assert add(v,DIR[dirs[-1]])==(0,0,0,0), dirs
    return out

HEXES=[]
for trip in itertools.combinations([0,30,60,90,120,150],3):
    ds=list(trip)+[(x+180)%360 for x in trip]
    try: P=poly_from_dirs(ds)
    except AssertionError: continue
    HEXES.append(('a',tuple(reversed(P))))
for p in range(0,360,30):
    for q in range(0,360,30):
        ds=[p,q,(p+120)%360,(q+120)%360,(p+240)%360,(q+240)%360]
        try: P=poly_from_dirs(ds)
        except AssertionError: continue
        HEXES.append(('b',tuple(reversed(P))))

# normalise: translate every configuration so the travelling rhombus is the
# canonical one at the origin.  Then (hexagon-region, tiling) is comparable
# across hexagon shapes, and we can ask which configurations coexist.
CANON_R = canon(((0,0,0,0), DIR[0], add(DIR[0],DIR[150]), DIR[150]))
print('canonical (0,150) rhombus at origin:', CANON_R, 'type', rtype(CANON_R))

seen=set(); moves=[]
for kind,P in HEXES:
    Pn=tuple(sorted(P,key=key))
    if Pn in seen: continue
    seen.add(Pn)
    cyc=list(P)
    if not is_convex(cyc): continue
    sym=hexagon_symmetry(cyc)
    if sym is None: continue
    ssum=[sum(v[k] for v in cyc) for k in range(4)]
    rots=[(lambda z: neg(z),'180')] if sym=='2' else [(rot120,'120'),(rot240,'240')]
    u = DIR[THETA]
    hexmin=None
    for v in cyc:
        z=dot_surd(v,u)
        if hexmin is None or surd_lt(z,hexmin): hexmin=z
    for T in tilings(list(P)):
        if sum(1 for t in T if tile_kind(t)==RHOMB)!=1: continue
        for t in T:
            if tile_kind(t)!=RHOMB: continue
            dmin=None
            for v in t:
                z=dot_surd(v,u)
                if dmin is None or surd_lt(z,dmin): dmin=z
            if dmin!=hexmin: continue
            if rtype(t) not in ALLOWED: continue
            if rtype(t) != (0,150): continue        # nest-A orientation only
            # translate so t == CANON_R
            sh = sub(CANON_R[0], t[0])
            tt  = canon(tuple(add(v,sh) for v in t))
            assert tt == CANON_R, (t, tt)
            Tn  = tuple(sorted(canon(tuple(add(v,sh) for v in q)) for q in T))
            cycn= tuple(add(v,sh) for v in cyc)
            for f,nm in rots:
                nt=canon(tuple(_rot_about(f,ssum,6,v) for v in t))
                if rtype(nt) not in ALLOWED: continue
                ntn = canon(tuple(add(v,sh) for v in nt))
                dphi=phi(ntn)-phi(tt)
                s=fwd(prog(nt),prog(t))
                moves.append(dict(sym=sym,rot=nm,ntiles=len(T),dphi=dphi,prog=s,
                                  tiling=Tn, hexcyc=cycn, dest=ntn))

print('admissible local moves for the canonical rhombus:', len(moves))
tab=collections.Counter((m['sym'],m['prog'],m['dphi'],m['ntiles']) for m in moves)
print()
print('%-4s %-9s %-5s %-7s count' % ('sym','progress','dphi','#tiles'))
for k in sorted(tab,key=lambda z:(z[3],z[0],z[1],str(z[2]))):
    print('%-4s %-9s %-5s %-7s %d'%(k[0],{1:'forward',0:'vertical',-1:'backward'}[k[1]],k[2],k[3],tab[k]))

# the -1 move and its tiling
bad=[m for m in moves if m['prog']>=0 and m['dphi']!=1]
print()
print('forward-or-vertical moves with dphi != 1 :', len(bad))
for m in bad:
    print('   sym=%s #tiles=%d dphi=%s' % (m['sym'],m['ntiles'],m['dphi']))
    print('   hexagon:', m['hexcyc'])
    for q in m['tiling']: print('      %s %s' % (tile_kind(q), q))
import pickle
pickle.dump(moves, open('/tmp/work-20261006c1-prove/moves.pkl','wb'))
