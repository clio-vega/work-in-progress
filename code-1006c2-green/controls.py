"""PLANTED CONTROLS - one per claim, each with its silence PREDICTED IN ADVANCE.
 C1 perturb one entry of K(t) by +t  -> Theorem B check must FAIL (pipeline sensitivity).
 C2 exponent n(lam)-C(l,2) -> +1 in Thm A -> must fail on ALL (no Y is zero).
 C3 phi_{l-1} -> phi_l in Thm A           -> must fail on ALL (incl l=1: 1 vs 1-t).
 C4 sign (-1)^{l-1} -> +1 in Thm A        -> SILENT exactly when l odd; must fail
    exactly on the partitions of EVEN length.  (Predicted vacuity, not a bug.)
 C5 drop [x=b] in Thm C -> SILENT unless x=b; must fail exactly on the 16 x=b instances.
 C6 drop [y<b] in Thm C -> must fail exactly on the 14 instances with 1<=y<=b-1.
 C7 t^{b-1}->t^b in Thm C -> must fail on ALL 78.
"""
import sympy as sp, hl, kostka_side as ks, raising
t = sp.symbols('t')

n = 5; order, K = ks.kostka_matrix(n)
Kp = dict(K); key = ((3,1,1),(2,1,1,1)); Kp[key] = sp.expand(Kp[key] + t)
def Yp(lam, rho):
    return sp.expand(sum(Kp[(nu,lam)]*hl.chi(nu,tuple(rho)) for nu in order))
diff = 0
for lam in order:
    for y in range(1, n//2+1):
        x = n-y
        C = raising.Qprime_h(lam)
        pred = C.get((n,),0) + (2 if x==y else 1)*C.get(tuple(sorted((x,y),reverse=True)),0)
        if sp.expand(Yp(lam,(x,y)) - pred) != 0: diff += 1
print(f'C1 perturb K[{key}] by +t: Theorem B fails on {diff}/14 pairs at n=5  '
      f'[{"FIRED" if diff else "SILENT - INVESTIGATE"}]', flush=True)

def thmA(lam, dexp=0, dphi=0, sign=True):
    l = len(lam); s = (-1)**(l-1) if sign else 1
    return sp.expand(s*t**(hl.n_stat(lam)-l*(l-1)//2+dexp)*ks.phi(l-1+dphi))
for tag, kw in [('C2 exponent +1', dict(dexp=1)), ('C3 phi_{l-1}->phi_l', dict(dphi=1)),
                ('C4 sign -> +1', dict(sign=False))]:
    f = tot = evenlen = 0
    for nn in range(1, 9):
        o,_,_ = hl.HL_P_cached(nn)
        for lam in o:
            tot += 1
            if len(lam) % 2 == 0: evenlen += 1
            if sp.expand(ks.Y(nn,lam,(nn,)) - thmA(lam, **kw)) != 0: f += 1
    extra = f' (partitions of even length = {evenlen})' if 'C4' in tag else ''
    print(f'{tag}: fails {f}/{tot}{extra}', flush=True)

def thmC(a,b,x,y, drop_xb=False, drop_ylt=False, shift=0):
    s = sp.Integer(0)
    if y==b: s += 1
    if x==b and not drop_xb: s += 1
    s += (t-1)*t**(b-1+shift)
    if 1<=y<=b-1 and not drop_ylt: s += (t-1)*t**(b-y-1)
    if 1<=x<=b-1: s += (t-1)*t**(b-x-1)
    return sp.expand(s)
for tag, kw in [('C5 drop [x=b]', dict(drop_xb=True)), ('C6 drop [y<b]', dict(drop_ylt=True)),
                ('C7 t^{b-1}->t^b', dict(shift=1))]:
    f = tot = 0
    for nn in range(2,9):
        for b in range(1, nn//2+1):
            a = nn-b
            if a<b: continue
            for y in range(1,nn):
                x = nn-y; tot += 1
                if sp.expand(ks.Y(nn,(a,b),tuple(sorted((x,y),reverse=True))) - thmC(a,b,x,y,**kw)) != 0:
                    f += 1
    print(f'{tag}: fails {f}/{tot}', flush=True)
