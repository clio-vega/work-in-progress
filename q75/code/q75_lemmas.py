"""Direct verification of the three lemmas the proof of Theorem A rests on,
plus the sharpness of the rigid factor."""
import sys
sys.path.insert(0, "/home/clio/projects/probes/2026-09-03-Q75")
import symfunc as S, sympy as sp
from q75_census import R_entry, pairs, sec
t = sp.Symbol("t")

sec("LEMMA 1.  (1+t) f_e(t) = sum_b t^b h_{e-b} e_b   (identity in Lambda[t])")
for e in [2, 3, 4, 5]:
    lhs = {k: sp.expand((1 + t) * v) for k, v in S.f_e_m(e, t).items()}
    rhs = {}
    for b in range(e + 1):
        pr = S.mult(S.h_m(e - b), S.e_m(b), e)
        for rho, c in pr.items():
            rhs[rho] = sp.expand(rhs.get(rho, 0) + t**b * c)
    rhs = {k: v for k, v in rhs.items() if v != 0}
    ok = all(sp.expand(lhs.get(k, 0) - rhs.get(k, 0)) == 0 for k in set(lhs) | set(rhs))
    print(f"  e={e}: {'OK' if ok else '*** FAIL ***'}", flush=True)

sec("LEMMAS 3,4,5 combined:  G_S(t) = t^h (1+t)^c  if no 2x2, else 0  (|lam|<=7)")
for e in [2, 3, 4]:
    ok = bad = 0; nsq = 0; badex = []
    for lam, mu in pairs(7, e):
        g = S.G_S(mu, lam, t)
        c, h, sq = S.shape_stats(mu, lam)
        pred = sp.Integer(0) if sq else sp.expand(t**h * (1 + t)**c)
        if sq:
            nsq += 1
        if sp.expand(g - pred) == 0:
            ok += 1
        else:
            bad += 1
            if len(badex) < 3:
                badex.append((lam, mu, c, h, sq, g, pred))
    print(f"  e={e}: {ok}/{ok+bad} entries" + (f"  *** FAIL {bad} ***" if bad else "  (exact)")
          + f"   [{nsq} shapes containing a 2x2]", flush=True)
    for x in badex:
        print("     ", x, flush=True)

sec("SHARPNESS.  gcd over all entries of [R_e,R_e'] -- is the rigid factor exactly (1+t)?")
for (e1, e2) in [(2, 3), (2, 4), (3, 4)]:
    NM = 8
    g = None
    for lam in S.parts_upto(NM):
        n = sum(lam)
        acc = {}
        for (a, b, sgn) in [(e1, e2, 1), (e2, e1, -1)]:
            for nu in S.parts_of(n + b):
                if not S.contains(nu, lam):
                    continue
                c1 = R_entry(nu, lam, b, t)
                if c1 == 0:
                    continue
                for mu in S.parts_of(n + b + a):
                    if not S.contains(mu, nu):
                        continue
                    c2 = R_entry(mu, nu, a, t)
                    if c2 == 0:
                        continue
                    acc[mu] = sp.expand(acc.get(mu, 0) + sgn * c1 * c2)
        for v in acc.values():
            v = sp.expand(v)
            if v != 0:
                g = v if g is None else sp.gcd(g, v)
    print(f"  gcd of all nonzero entries of [R_{e1},R_{e2}] on |lam|<={NM}:  {sp.factor(g)}",
          flush=True)

sec("COROLLARY.  R_e(t) is a multiplication operator  <=>  t = -1")
for e in [2, 3, 4]:
    # the defect entries, as polynomials; their common zero set
    ds = set()
    for lam, mu in pairs(6, e):
        D = sp.expand(S.pair_hooks(mu, lam, e, t) - R_entry(mu, lam, e, t))
        if D != 0:
            ds.add(sp.factor(D))
    common = None
    for D in ds:
        common = D if common is None else sp.gcd(common, D)
    print(f"  e={e}: {len(ds)} distinct nonzero defect polynomials; gcd = {sp.factor(common)}"
          f"  -> common zero locus t = {sp.solve(common, t)}", flush=True)
    # forcing: the lambda=() column determines the only possible multiplier
    col = {mu: R_entry(mu, (), e, t) for mu in S.parts_of(e) if R_entry(mu, (), e, t) != 0}
    print(f"        lambda=() column of R_e(t) = {col}"
          f"   -> forces f = sum_k t^k s_(e-k,1^k)", flush=True)
