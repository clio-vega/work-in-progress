import sympy as sp, hl, kostka_side as ks
t = sp.symbols('t')
def thmC(a,b,x,y):
    s = sp.Integer(0)
    if y==b: s += 1
    if x==b: s += 1
    s += (t-1)*t**(b-1)
    if 1<=y<=b-1: s += (t-1)*t**(b-y-1)
    if 1<=x<=b-1: s += (t-1)*t**(b-x-1)
    return sp.expand(s)
tot=bad=0; fired={'x=b':0,'y<b':0,'x<b':0,'y=b':0}
for n in range(2,9):
    for b in range(1,n//2+1):
        a=n-b
        if a<b: continue
        for y in range(1,n):
            x=n-y
            got=ks.Y(n,(a,b),tuple(sorted((x,y),reverse=True))); tot+=1
            if x==b: fired['x=b']+=1
            if y==b: fired['y=b']+=1
            if 1<=y<=b-1: fired['y<b']+=1
            if 1<=x<=b-1: fired['x<b']+=1
            if sp.expand(got-thmC(a,b,x,y))!=0:
                bad+=1
                if bad<=6: print('  FAIL',(a,b),(x,y),sp.factor(got),thmC(a,b,x,y))
print(f'Theorem C: {tot} checks (n<=8, x,y unordered), failures={bad}')
print('  indicator terms exercised:', fired)
