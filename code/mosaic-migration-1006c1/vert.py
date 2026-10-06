"""Dump every strictly-vertical 180-degree migration step, in full.

Re-runs classify.py's enumeration but records the whole configuration:
the hexagon, its tiling, the rhombus before and after, dphi, and the
sizes involved.  Goal: decide whether the dphi=-1 orientation is
reachable from a valid mosaic configuration.
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
    HEXES.append(('a',tuple(reversed(P)),trip))
for p in range(0,360,30):
    for q in range(0,360,30):
        ds=[p,q,(p+120)%360,(q+120)%360,(p+240)%360,(q+240)%360]
        try: P=poly_from_dirs(ds)
        except AssertionError: continue
        HEXES.append(('b',tuple(reversed(P)),(p,q)))

seen=set(); recs=[]
for kind,P,lab in HEXES:
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
            for f,nm in rots:
                nt=canon(tuple(_rot_about(f,ssum,6,v) for v in t))
                if rtype(nt) not in ALLOWED: continue
                dphi=phi(nt)-phi(t)
                s=fwd(prog(nt),prog(t))
                if s!=0: continue                  # strictly vertical only
                recs.append(dict(sym=sym,rot=nm,lab=lab,hexdirs=lab,cyc=cyc,
                                 tiling=T,t=t,nt=nt,dphi=dphi,
                                 rt=rtype(t),rnt=rtype(nt),ntiles=len(T)))

print('strictly vertical steps found:', len(recs))
for r in recs:
    print()
    print('--- sym=%s rot=%s dphi=%s' % (r['sym'],r['rot'],r['dphi']))
    print('    hexagon edge dirs    :', r['hexdirs'])
    print('    hexagon vertices     :', r['cyc'])
    print('    #tiles in hexagon    :', r['ntiles'])
    print('    tiling               :')
    for t in r['tiling']:
        print('        %s %s' % (tile_kind(t), t))
    print('    rhombus before       :', r['t'], 'type', r['rt'], 'phi', phi(r['t']))
    print('    rhombus after        :', r['nt'],'type', r['rnt'],'phi', phi(r['nt']))
