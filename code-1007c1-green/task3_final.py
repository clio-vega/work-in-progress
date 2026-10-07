"""TASK 3 (final): bridge is the IDENTITY X = Y, established 209/209 by task3_bridge2.py
   (candidates t^n(lam)Y(1/t): 66/209; t^n(rho)Y(1/t): 16/209 -- both REFUTED).
   Only now is the Jing-Liu recurrence used as corroboration."""
import sympy as sp, hl, kostka_side as ks, mac2p_green as JL
t = sp.symbols('t')
def X(l,r): return sp.expand(sp.cancel(JL.X(l,r)))

tot=bad=0
for n in range(1, 7):
    order,_,_ = hl.HL_P_cached(n)
    for lam in order:
        l=len(lam)
        A = sp.expand((-1)**(l-1)*t**(hl.n_stat(lam)-l*(l-1)//2)*ks.phi(l-1))
        tot+=1
        if sp.expand(X(lam,(n,)) - A)!=0: bad+=1; print('  A FAIL', lam)
print(f'Theorem A  via Jing-Liu recurrence: {tot} partitions (n<=6), failures={bad}')

def thmC(a,b,x,y):
    s=sp.Integer(0)
    if y==b: s+=1
    if x==b: s+=1
    s += (t-1)*t**(b-1)
    if 1<=y<=b-1: s += (t-1)*t**(b-y-1)
    if 1<=x<=b-1: s += (t-1)*t**(b-x-1)
    return sp.expand(s)
tot=bad=0
for n in range(2,7):
    for b in range(1,n//2+1):
        a=n-b
        for y in range(1,n):
            x=n-y; rho=tuple(sorted((x,y),reverse=True)); tot+=1
            if sp.expand(X((a,b),rho) - thmC(a,b,x,y))!=0: bad+=1; print('  C FAIL',(a,b),rho)
print(f'Theorem C  via Jing-Liu recurrence: {tot} checks (n<=6), failures={bad}')

tot=bad=0
for n in range(2,7):
    for b in range(1,n//2+1):
        a=n-b; rho=tuple(sorted((n-b,b),reverse=True))
        D=sp.expand(t**b-t**(b-1)+1+(1 if a==b else 0)); tot+=1
        if sp.expand(X((a,b),rho)-D)!=0: bad+=1; print('  D FAIL',(a,b),rho)
print(f'Theorem D  diagonal family via Jing-Liu: {tot} (a,b) pairs (n<=6), failures={bad}')

tot=bad=0
for n in range(2,7):
    order,_,_ = hl.HL_P_cached(n)
    for lam in order:
        for y in range(1,n//2+1):
            x=n-y; rho=tuple(sorted((x,y),reverse=True)); tot+=1
            if sp.expand(X(lam,rho)-ks.Y(n,lam,rho))!=0: bad+=1
print(f'full two-part slice, two engines: {tot} checks (n<=6), failures={bad}')
