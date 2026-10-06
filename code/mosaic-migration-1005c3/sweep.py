"""(T1) + (T2): compute ell(M) for every mosaic, by every admissible order."""
import sys, time, collections, itertools, json
sys.path.insert(0,'.')
from mosaic import *
from migrate import nestA_rhombi
from step import journey2, STATS

THETA = 150   # "south" = -N for the flock orientation (-E_A,-N_A); Purbhoo Cor 3.2

def admissible_orders(n, d, M, cap=200):
    """DFS over orders in which the nest-A rhombi can be migrated to nest B.
    Returns list of (order_cells, ell, assignment) where assignment maps the
    source nest-A cell to the destination nest-B cell."""
    idx, _ = nest_index(n, d)
    tgt = {t for t,(nm,i,j) in idx.items() if nm == 'B'}
    start = [t for t,i,j in nestA_rhombi(n, d, M)]
    out = []
    def rec(tiles, remaining, order, ell, assign):
        if len(out) >= cap: return
        if not remaining:
            out.append((tuple(order), ell, tuple(sorted(assign)))); return
        for k, t in enumerate(remaining):
            try:
                tl, nt, s, kinds = journey2(tiles, t, THETA, tgt)
            except RuntimeError:
                continue
            rec(tl, remaining[:k]+remaining[k+1:], order+[idx[t][1:]],
                ell+s, assign+[(idx[t][1:], idx[nt][1:])])
    rec(set(M), start, [], 0, [])
    return out

def check_final(n, d, M, order_tiles):
    pass

def partitions_in_box(d, m):
    out=[]
    def rec(p,k,mx):
        if k==d: out.append(tuple(x for x in p if x>0)); return
        for v in range(mx,-1,-1): rec(p+[v],k+1,v)
    rec([],0,m); return out

def sweep(cases, cap=200, verbose=True):
    rows = []
    for (n, d) in cases:
        m = n-d; P = partitions_in_box(d, m); t0=time.time()
        for al in P:
          for be in P:
            for ga in P:
              if sum(al)+sum(be)+sum(ga) != d*m: continue
              Ms = mosaics_with_boundary(n, d, al, be, ga)
              if not Ms: continue
              fib = []
              for M in Ms:
                  ao = admissible_orders(n, d, M, cap=cap)
                  if not ao:
                      fib.append(dict(ell=None, norders=0, ells=[], assigns=[]))
                      continue
                  ells = sorted({e for _,e,_ in ao})
                  asg  = {a for _,_,a in ao}
                  fib.append(dict(ell=ells[0], norders=len(ao),
                                  ells=ells, assigns=sorted(asg)))
              rows.append(dict(n=n,d=d,alpha=al,beta=be,gamma=ga,
                               c=len(Ms), fibre=fib))
        if verbose: print('  n=%d d=%d done in %.1fs'%(n,d,time.time()-t0))
    return rows

if __name__ == '__main__':
    cases = [(4,2),(5,2),(5,3),(6,3)]
    rows = sweep(cases)
    json.dump([{k:(v if k!='fibre' else v) for k,v in r.items()} for r in rows],
              open('sweep.json','w'), default=str)
    print('fibres:', len(rows), ' STATS:', STATS)
