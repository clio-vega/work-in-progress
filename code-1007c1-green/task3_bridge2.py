"""TASK 3 retry: identify the bridge EMPIRICALLY over a family of candidates,
then demand it hold on 100% of a range before using it."""
import sympy as sp, hl, kostka_side as ks, mac2p_green as JL
t = sp.symbols('t')
cands = {
 'X = Y'                        : lambda n,l,r,Y,G: Y,
 'X = G'                        : lambda n,l,r,Y,G: G,
 'X = t^n(lam) Y(1/t)'          : lambda n,l,r,Y,G: t**hl.n_stat(l)*Y.subs(t,1/t),
 'X = t^n(lam) G(1/t)'          : lambda n,l,r,Y,G: t**hl.n_stat(l)*G.subs(t,1/t),
 'X = b_lam(t) Y / prod(1-t^r)' : lambda n,l,r,Y,G: ks.b_lam(l)*Y/sp.prod([1-t**x for x in r]),
}
score = {k:0 for k in cands}; tot=0; ex={}
for n in range(1, 7):
    order,_,_ = hl.HL_P_cached(n)
    for lam in order:
        for rho in hl.partitions(n):
            X = sp.expand(sp.cancel(JL.X(lam, rho)))
            Y = ks.Y(n, lam, rho); G = ks.G(n, lam, rho)
            tot += 1
            for k,f in cands.items():
                if sp.expand(sp.cancel(X - f(n,lam,rho,Y,G))) == 0: score[k]+=1
                elif k not in ex: ex[k]=(lam,rho,X,sp.cancel(f(n,lam,rho,Y,G)))
print(f'n<=6, {tot} (lam,rho) pairs:')
for k in cands:
    mark = 'EXACT' if score[k]==tot else ''
    print(f'  {k:32s} {score[k]:4d}/{tot}  {mark}')
    if score[k]!=tot: print(f'       first disagreement: lam={ex[k][0]} rho={ex[k][1]}  X={ex[k][2]}  cand={ex[k][3]}')
