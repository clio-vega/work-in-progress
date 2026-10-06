"""(T1): is ell(M) independent of the order in which the rhombi of the flock are
migrated?  Purbhoo prescribes one order (the standard order of the flock's unique
LR-tableau); this asks whether the STATISTIC depends on that choice at all."""
import sys, itertools, collections
sys.path.insert(0,'.')
from mosaic import *
from migrate import *

def run(n,d,al,be,ga,maxperm=720):
    res=[]
    for M in mosaics_with_boundary(n,d,al,be,ga):
        rh=[t for t,i,j in nestA_rhombi(n,d,M)]
        lens=collections.Counter(); ok=0; fail=0; finals=set()
        perms=list(itertools.permutations(rh))
        if len(perms)>maxperm: perms=perms[:maxperm]
        for p in perms:
            try:
                ell, tl, se = migrate_order(n,d,M,p)
            except Exception as ex:
                fail+=1; continue
            f=final_nestB_cells(n,d,tl)
            if f is None or any(nm!='B' for nm,_,_ in f): fail+=1; continue
            ok+=1; lens[ell]+=1; finals.add(tuple(f))
        res.append((len(rh),ok,fail,dict(lens),len(finals)))
    return res

if __name__=='__main__':
    cases=[(3,1,(1,),(1,),()), (4,2,(2,1),(1,),()), (4,2,(1,1),(1,),(1,)),
           (4,2,(2,),(1,),(1,)), (5,2,(2,1),(2,1),(2,)), (5,3,(1,1,1),(1,1),(1,))]
    for c in cases:
        print(c)
        for r in run(*c):
            print('   |alpha|=%d  orders ok=%d fail=%d   ell multiset=%s   distinct final flocks=%d'%r)
