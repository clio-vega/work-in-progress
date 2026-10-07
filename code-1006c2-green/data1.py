import sympy as sp, hl
t = sp.symbols('t')
def br(n): return sum(t**i for i in range(n))
def bt(lam):
    from collections import Counter
    c = Counter(lam); r = sp.Integer(1)
    for part, m in c.items():
        for k in range(1, m+1): r *= (1 - t**k)
    return r
print("### ONE-PART  G^lam_(n)(t) = <p_n, P_lam>   [Q'-convention]")
for n in range(2, 8):
    order, Pp, Ps = hl.HL_P_cached(n)
    print(f'--- n={n}')
    for lam in order:
        G = sp.expand(hl.green_c(n, lam, (n,)))
        if G == 0:
            print(f'  {str(lam):18s} G = 0'); continue
        # divide by (1-t^n)/(1-t^d) for d = 1..n to find which is exact
        ds = []
        for d in range(1, n+1):
            if n % d: continue
            q = sp.cancel(G * (1 - t**d) / (1 - t**n))
            if sp.simplify(sp.denom(sp.together(q))) == 1:
                ds.append((d, sp.factor(q)))
        Y = sp.cancel(bt(lam) * G / (1 - t**n))
        print(f'  {str(lam):18s} G = {str(sp.factor(G)):40s} Y=[P_lam]p_n = {sp.factor(Y)}   (d,quot)={ds}')
