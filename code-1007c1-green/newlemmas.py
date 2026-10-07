"""Verification of the NEW lemmas that carry today's proofs.  Each is a step I
claim to have PROVED; the run is an independent check of the proved statement."""
import sympy as sp, hl, kostka_side as ks, hexp, raising
from charge_kostka import ssyt, charge
from itertools import combinations
t = sp.symbols('t')
def qbin(a,b):
    if b<0 or b>a: return sp.Integer(0)
    num=den=sp.Integer(1)
    for i in range(b): num*=(1-t**(a-i)); den*=(1-t**(i+1))
    return sp.expand(sp.cancel(num/den))

# ---- L2: two-part CONTENT Kostka-Foulkes is a MONOMIAL ------------------------
# K_{nu,(a,b)}(t) = t^{b-nu_2}  if l(nu)<=2 and nu_2 <= b <= nu_1 ; else 0.
tot=bad=0
for n in range(2, 10):
    for b in range(0, n//2+1):
        a = n-b
        mu = tuple(x for x in (a,b) if x>0)
        for nu in hl.partitions(n):
            K = sp.expand(sum(t**charge(T) for T in ssyt(nu, mu)))
            n2 = nu[1] if len(nu)>1 else 0
            pred = t**(b-n2) if (len(nu)<=2 and n2 <= b <= nu[0]) else sp.Integer(0)
            tot+=1
            if sp.expand(K-pred)!=0:
                bad+=1
                if bad<=5: print('  L2 FAIL', nu, mu, sp.factor(K), '!=', pred)
print(f'L2  K_nu,(a,b)(t) = t^(b-nu_2) monomial: {tot} (nu,(a,b)) pairs, n<=9, failures={bad}')

# ---- L3: the two-row recursion  Q'_(a,b) - t Q'_(a+1,b-1) = h_a h_b - h_{a+1} h_{b-1}
tot=bad=0
for n in range(2, 8):
    order,_,_ = hl.HL_P_cached(n)
    for b in range(1, n//2+1):
        a = n-b
        lhs = hexp.Qprime_in_p(n,(a,b))
        hi  = hexp.Qprime_in_p(n, tuple(x for x in (a+1,b-1) if x>0))
        L = hl.lin((sp.Integer(1),lhs), (-t,hi))
        hab = hexp.h_in_p(tuple(x for x in (a,b) if x>0), n)
        hab2= hexp.h_in_p(tuple(x for x in (a+1,b-1) if x>0), n)
        R = hl.lin((sp.Integer(1),hab), (sp.Integer(-1),hab2))
        tot+=1
        d = [(k,sp.factor(L.get(k,0)-R.get(k,0))) for k in set(L)|set(R)
             if sp.expand(L.get(k,0)-R.get(k,0))!=0]
        if d: bad+=1; print('  L3 FAIL', n,(a,b), d[:3])
print(f'L3  two-row recursion: {tot} (a,b) pairs, n<=7, failures={bad}')

# ---- L4: <p_(x,y), h_nu> = [nu=(n)] + (1+[x=y])[nu=sort(x,y)] ------------------
tot=bad=0
for n in range(2, 9):
    for y in range(1, n//2+1):
        x = n-y
        rho = tuple(sorted((x,y), reverse=True))
        for nu in hl.partitions(n):
            got = sp.Integer(hl.z_lam(rho))*hexp.h_in_p(nu,n).get(rho,0)
            pred = (1 if nu==(n,) else 0) + ((2 if x==y else 1) if nu==rho else 0)
            tot+=1
            if sp.expand(got-pred)!=0:
                bad+=1
                if bad<=5: print('  L4 FAIL', rho, nu, got, pred)
print(f'L4  <p_(x,y),h_nu> counting formula: {tot} (rho,nu) pairs, n<=8, failures={bad}')

# ---- L5: the q-binomial identity used in Theorem A -----------------------------
bad=0
for m in range(0, 13):
    s = sp.expand(sum((-1)**j * t**(j*(j+1)//2) * qbin(m,j) for j in range(m+1)))
    if sp.expand(s - ks.phi(m)) != 0: bad+=1; print('  L5 FAIL m=',m)
print(f'L5  sum_j (-1)^j t^(j(j+1)/2) [m,j]_t = phi_m: m<=12, failures={bad}')

# ---- L6: the subset-sum identity used in Lemma 1 -------------------------------
bad=0; tot=0
for l in range(1, 10):
    for r in range(0, l):
        lhs = sp.expand(sum(t**sum(s-1 for s in S) for S in combinations(range(2,l+1), r)))
        rhs = sp.expand(t**(r*(r+1)//2) * qbin(l-1, r))
        tot+=1
        if sp.expand(lhs-rhs)!=0: bad+=1; print('  L6 FAIL', l, r)
print(f'L6  sum_{{S}} t^sum(s-1) = t^C(r+1,2)[l-1,r]_t: {tot} (l,r), failures={bad}')

# ---- L7: partial sums of the raising weights  sum_{k=0}^K w(k) = t^K -----------
bad=0
for K in range(0, 12):
    s = sp.expand(1 + sum(t**(k-1)*(t-1) for k in range(1,K+1)))
    if sp.expand(s - t**K)!=0: bad+=1; print('  L7 FAIL K=',K)
print(f'L7  sum_{{k<=K}} w(k) = t^K: K<=11, failures={bad}')
