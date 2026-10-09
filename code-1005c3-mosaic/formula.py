"""If phi is a potential then  ell = sum_{dest cells} phi_B - sum_{source cells} phi_A
with  phi_A(i,j) = j + 1/2   and   phi_B(i,j) = n - i - 1/2.
Check this closed form against every fibre of the sweep."""
import json, ast, collections
from fractions import Fraction
rows=json.load(open('sweep.json'))
bad=0; tot=0; tab=[]
for r in rows:
    n=r['n']; d=r['d']
    for f in r['fibre']:
        for A in f['assigns']:
            A=ast.literal_eval(A) if isinstance(A,str) else A
            s=Fraction(0)
            for (src,dst) in A:
                s += Fraction(n) - dst[0] - Fraction(1,2)
                s -= Fraction(src[1]) + Fraction(1,2)
            tot+=1
            if s != f['ell']: bad+=1
print('journeys checked: %d   closed form != simulated ell : %d' % (tot,bad))

# closed form purely in terms of the boundary data
def ell_closed(n,d,alpha,beta,gamma):
    """alpha in nest A, beta in nest B, gamma in nest C; the migration fills nest B
    up to lambda, where lambda is read off from the final configuration."""
    # lambda: beta plus the migrated cells. |lambda| = |alpha|+|beta|.
    # lambda^vee = gamma  =>  lambda_k = (n-d) - gamma_{d+1-k}
    m=n-d
    g=list(gamma)+[0]*(d-len(gamma))
    lam=[m-g[d-1-k] for k in range(d)]
    mu=list(beta)+[0]*(d-len(beta))
    al=list(alpha)+[0]*(d-len(alpha))
    s=Fraction(0)
    for i in range(d):
        s += (lam[i]-mu[i])*(Fraction(n)-i-Fraction(1,2))
        s -= Fraction(al[i]*al[i], 2)
    return s
bad2=0; ex=[]
for r in rows:
    e=ell_closed(r['n'],r['d'],r['alpha'],r['beta'],r['gamma'])
    got={f['ell'] for f in r['fibre']}
    if got != {e}:
        bad2+=1; ex.append((r['n'],r['d'],r['alpha'],r['beta'],r['gamma'],e,got))
print('fibres where the boundary-only formula fails:', bad2, 'of', len(rows))
for x in ex[:5]: print('   ',x)
