import sys, time, json
sys.path.insert(0,'.'); sys.path.insert(0,'/home/clio/git/puzzles')
from mosaic import *
from sweep import admissible_orders, partitions_in_box
from control import lr_tableaux
res=[]
for (n,d) in [(7,3),(7,4)]:
    m=n-d; P=partitions_in_box(d,m); cands=[]
    for al in P:
      for be in P:
        for ga in P:
          if sum(al)+sum(be)+sum(ga)!=d*m: continue
          g=list(ga)+[0]*(d-len(ga))
          lam=tuple(x for x in (m-g[d-1-k] for k in range(d)) if x>0)
          c=len(lr_tableaux(lam,be,al))
          if c>=2: cands.append((al,be,ga,c,lam))
    cands.sort(key=lambda z:-z[3])
    print('n=%d d=%d  fibres with c>=2: %d   max c = %d'%(n,d,len(cands),max([z[3] for z in cands] or [0])), flush=True)
    for (al,be,ga,c,lam) in cands[:40]:
        t0=time.time()
        Ms=mosaics_with_boundary(n,d,al,be,ga)
        ells=[]
        for M in Ms:
            ao=admissible_orders(n,d,M,cap=30)
            ells.append(sorted({e for _,e,_ in ao}) if ao else None)
        print('   n=%d d=%d a=%s b=%s g=%s  c=%d  #mosaics=%d  ell=%s   (%.1fs)'
              %(n,d,al,be,ga,c,len(Ms),ells,time.time()-t0), flush=True)
        res.append(dict(n=n,d=d,alpha=al,beta=be,gamma=ga,c=c,ells=ells))
        json.dump(res,open('bigmult.json','w'))
