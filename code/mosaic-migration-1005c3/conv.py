"""Which reading convention makes Lemma 2.5 true?  Purbhoo 2.2 conditions:
  (i) weakly increasing east->west in rows   (ii) strictly increasing south->north
  in columns  (iii) lattice condition on sub-words of the reading word.
Test all four combinations of reading order x (prefix|suffix) against the only
instrument that can decide: Lemma 2.5 says the flock on a nest-collection is
UNIQUE, in each of the orientations (E,N) and (-E,-N), with equal content."""
import sys; sys.path.insert(0,'.')
from itertools import product

def fillings(cells, order_key, use_prefix):
    cells=set(cells); n=len(cells)
    order=sorted(cells,key=order_key)
    out=[];T={};cnt=[0]*(n+2)
    def rec(k):
        if k==len(order): out.append(dict(T)); return
        a,b=order[k]
        for v in range(1,n+1):
            if use_prefix and v>=2 and cnt[v-1]+1>cnt[v-2]: continue
            if (a+1,b) in T and T[(a+1,b)]>v: continue
            if (a-1,b) in T and T[(a-1,b)]<v: continue
            if (a,b+1) in T and T[(a,b+1)]<=v: continue
            if (a,b-1) in T and T[(a,b-1)]>=v: continue
            T[(a,b)]=v; cnt[v-1]+=1; rec(k+1); cnt[v-1]-=1; del T[(a,b)]
    rec(0)
    if use_prefix: return out
    # suffix version: a filling is good iff every TAIL of the word is dominant
    good=[]
    for f in out:
        w=[f[c] for c in order]
        ok=True
        for s in range(len(w)):
            c=[0]*(n+2)
            for v in w[s:]: c[v-1]+=1
            if any(c[k]<c[k+1] for k in range(n)): ok=False;break
        if ok: good.append(f)
    return good

ORDERS = {
 'WE,NS': lambda c:(-c[1], c[0]),
 'WE,SN': lambda c:( c[1], c[0]),
 'EW,NS': lambda c:(-c[1],-c[0]),
 'EW,SN': lambda c:( c[1],-c[0]),
}
def parts(d,m):
    out=[]
    def rec(p,k,mx):
        if k==d: out.append(tuple(x for x in p if x>0)); return
        for v in range(mx,-1,-1): rec(p+[v],k+1,v)
    rec([],0,m); return out

for name,ok in ORDERS.items():
    for pref in (True,False):
        bad=[]; tested=0
        for (d,m) in ((3,2),(2,3)):
            for lam in parts(d,m):
                if not lam: continue
                cells={(a,b) for b,L in enumerate(lam) for a in range(L)}
                for sgn in ((1,1),(-1,-1)):
                    C={(sgn[0]*a,sgn[1]*b) for (a,b) in cells}
                    am=min(a for a,_ in C); bm=min(b for _,b in C)
                    C={(a-am,b-bm) for (a,b) in C}
                    F=fillings(C,ok,pref); tested+=1
                    if len(F)!=1: bad.append((lam,sgn,len(F)))
        print('%-7s %-7s  non-unique: %3d / %3d' % (name,'prefix' if pref else 'suffix',len(bad),tested),
              ('  e.g. '+str(bad[:2])) if bad else '   <-- LEMMA 2.5 HOLDS')
