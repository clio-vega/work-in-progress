"""Full verification suite, 2026-10-06 c2."""
import sympy as sp, hl, kostka_side as ks, raising
t = sp.symbols('t')
def ph(m): return ks.phi(m)
R = {}

# ---------- (i) psi for two-row horizontal strips: <h_c h_d, P_mu> ----------
# claim: <h_c h_d, P_mu> = 0 unless l(mu)<=2 and mu_2 <= d <= mu_1 (c = |mu|-d);
#        value = (1-t) if mu_2 < d < mu_1, else 1.
def hh_P(c, d, mu, n):
    _, Pp, _ = hl.HL_P_cached(n)
    hcd = ks and None
    import hexp
    hv = hexp.h_in_p(tuple(x for x in (c, d) if x > 0), n)
    return sp.cancel(hl.hall_ip(hv, Pp[mu], n))
tot=bad=0
for n in range(2, 7):
    order,_,_ = hl.HL_P_cached(n)
    for mu in order:
        for d in range(0, n+1):
            c = n-d
            if c < d: continue
            v = sp.expand(hh_P(c, d, mu, n)); tot += 1
            if len(mu) > 2 or not (mu[1] if len(mu)>1 else 0) <= d <= mu[0]:
                pred = sp.Integer(0)
            else:
                m2 = mu[1] if len(mu) > 1 else 0
                pred = (1-t) if (m2 < d < mu[0]) else sp.Integer(1)
            if sp.expand(v-pred) != 0:
                bad += 1
                if bad <= 4: print('  psi FAIL', n, mu, (c,d), sp.factor(v), '!=', pred)
R['psi two-row'] = (tot, bad); print(f'(i) <h_c h_d, P_mu> formula: {tot} checks (n<=6), failures={bad}')

# ---------- (ii) Theorem B: Y^lam_(x,y) = c_{lam,(n)} + (1+[x=y]) c_{lam,(x,y)} ----------
tot=bad=0
for n in range(2, 8):
    order,_,_ = hl.HL_P_cached(n)
    for lam in order:
        C = raising.Qprime_h(lam)
        for y in range(1, n//2+1):
            x = n-y
            nu = tuple(sorted((x,y), reverse=True))
            pred = C.get((n,), 0) + (2 if x==y else 1)*C.get(nu, 0)
            got = ks.Y(n, lam, (x,y)); tot += 1
            if sp.expand(got-pred) != 0:
                bad += 1
                if bad <= 4: print('  ThmB FAIL', n, lam, (x,y), sp.factor(got), sp.factor(pred))
R['Thm B'] = (tot, bad); print(f'(ii) Theorem B (two-part = quadratic h-part): {tot} checks (n<=7), failures={bad}')

# ---------- (iii) Theorem A: one-part closed form ----------
tot=bad=0
for n in range(1, 9):
    order,_,_ = hl.HL_P_cached(n)
    for lam in order:
        l = len(lam)
        pred = sp.expand((-1)**(l-1)*t**(hl.n_stat(lam)-l*(l-1)//2)*ph(l-1))
        tot += 1
        if sp.expand(ks.Y(n, lam, (n,)) - pred) != 0:
            bad += 1; print('  ThmA FAIL', n, lam)
R['Thm A'] = (tot, bad); print(f'(iii) Theorem A (one-part closed form): {tot} partitions (n<=8), failures={bad}')

# ---------- (iv) Theorem C: two-row lambda, two-part rho ----------
def thmC(a, b, x, y):
    s = sp.Integer(0)
    if y == b: s += 1
    if x == b: s += 1
    s += (t-1)*t**(b-1)
    if 1 <= y <= b-1: s += (t-1)*t**(b-y-1)
    if 1 <= x <= b-1: s += (t-1)*t**(b-x-1)
    return sp.expand(s)
tot=bad=0
for n in range(2, 10):
    for b in range(1, n//2+1):
        a = n-b
        if a < b: continue
        lam = (a, b)
        for y in range(1, n):
            x = n-y
            got = ks.Y(n, lam, tuple(sorted((x,y), reverse=True)))
            tot += 1
            if sp.expand(got - thmC(a,b,x,y)) != 0:
                bad += 1
                if bad <= 6: print('  ThmC FAIL', lam, (x,y), sp.factor(got), thmC(a,b,x,y))
R['Thm C'] = (tot, bad); print(f'(iv) Theorem C (two-row lambda): {tot} checks (n<=9, x,y unordered incl. x<y), failures={bad}')

# ---------- (v) G <-> Y dictionary ----------
tot=bad=0
for n in range(1, 8):
    order,_,_ = hl.HL_P_cached(n)
    for lam in order:
        for rho in hl.partitions(n):
            num = sp.Integer(1)
            for r in rho: num *= (1-t**r)
            tot += 1
            if sp.expand(sp.cancel(hl.green_c(n,lam,rho) - num*ks.Y(n,lam,rho)/ks.b_lam(lam))) != 0:
                bad += 1
R['G<->Y'] = (tot, bad); print(f'(v) G = prod(1-t^rho_i) Y / b_lam: {tot} checks (n<=7), failures={bad}')
print()
print('SUMMARY', R)
