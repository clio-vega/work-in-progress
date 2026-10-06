import json, collections, sys
rows=json.load(open('sweep.json'))
print('fibres:', len(rows))
nonempty=[r for r in rows if r['c']>0]
mult=[r for r in nonempty if r['c']>=2]
print('fibres with c>=1: %d   with c>=2: %d   with c>=3: %d'
      %(len(nonempty),len(mult),len([r for r in nonempty if r['c']>=3])))
print()
# (T1) order independence
bad_order=[]; no_order=[]; multi_assign=[]
for r in nonempty:
    for f in r['fibre']:
        if f['norders']==0: no_order.append(r); continue
        if len(f['ells'])>1: bad_order.append((r,f))
        if len(f['assigns'])>1: multi_assign.append((r,f))
print('(T1)  mosaics with no admissible order      :', len(no_order))
print('(T1)  mosaics where ell depends on the order:', len(bad_order))
print('(T1)  mosaics where the OUTPUT depends on it:', len(multi_assign))
norders=collections.Counter(f['norders'] for r in nonempty for f in r['fibre'])
print('(T1)  number of admissible orders, distribution:', dict(sorted(norders.items())))
print()
# bijection check: within a fibre, the assignment must be injective (distinct mosaics
# -> distinct LR tableaux)
bijfail=0
for r in nonempty:
    A=[repr(f['assigns'][0]) if f['assigns'] else None for f in r['fibre']]
    if len(set(A))!=len(A): bijfail+=1
print('bijection: fibres where two mosaics give the same tableau:', bijfail)
print()
# (T2)(a) vacuity
dist=collections.Counter()
for r in nonempty:
    ells=[f['ell'] for f in r['fibre']]
    dist[len(set(ells))]+=1
print('(T2a) #distinct values of ell per fibre:', dict(sorted(dist.items())))
dist2=collections.Counter()
for r in mult:
    ells=[f['ell'] for f in r['fibre']]
    dist2[(r['c'],len(set(ells)))]+=1
print('(T2a) restricted to c>=2, (c, #distinct ell):', dict(sorted(dist2.items())))
print()
print('--- every fibre with c>=2 ---')
for r in mult:
    ells=sorted(f['ell'] for f in r['fibre'])
    print('   n=%d d=%d (a,b,g)=(%s,%s,%s)  c=%d  ell = %s'
          %(r['n'],r['d'],r['alpha'],r['beta'],r['gamma'],r['c'],ells))
