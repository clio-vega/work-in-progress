"""q75_phase2.py -- the Q75 theorem.

CLAIM (Theorem A).  For any skew shape S = mu/lam with |S| = e,
    <s_S, f_e(t)> = t^{h(S)} (1+t)^{c(S)-1}   if S contains no 2x2 square,
                  = 0                          otherwise,
where c(S) = #connected components and h(S) = sum over components of (rows - 1).
Equivalently  G_S(t) = t^{h}(1+t)^{c}  resp. 0, where G_S counts splittings of S
into a horizontal strip (lower/left) and a vertical strip (upper/right).

VARIATION NAMED IN ADVANCE (this is the anti-kernel clause):
  * at t = 0 the two sides of  M_{f_e} = R_e + (1+t)E_e  must GENUINELY DIFFER,
    i.e. E_e(0) != 0 -- otherwise the whole statement is about the zero operator.
  * the c >= 2 entries are the ones carrying the difference; count them.
"""
import sys, time
sys.path.insert(0, "/home/clio/projects/probes/2026-09-03-Q75")
import symfunc as S
import sympy as sp
from q75_census import R_entry, pairs, sec

t = sp.Symbol("t")
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 8
EE = [2, 3, 4]

sec("PHASE 2, STEP 0.  THE KERNEL CHECK.  t=0 must separate R_e(0) from M_{h_e}.")
for e in EE:
    same = diff = 0; ex = []
    for lam, mu in pairs(6, e):
        a = R_entry(mu, lam, e, sp.Integer(0))
        b = S.pair_hooks(mu, lam, e, sp.Integer(0))     # <s_{mu/lam}, h_e>
        if sp.simplify(a - b) == 0:
            same += 1
        else:
            diff += 1
            if len(ex) < 2:
                ex.append((lam, mu, a, b))
    print(f"  e={e}:  R_e(0) vs M_{{h_e}}:  DIFFER on {diff}/{same+diff} entries"
          f"   {'SEPARATOR LIVE' if diff else '*** KERNEL: test is vacuous ***'}", flush=True)
    for x in ex:
        print("      e.g. lam,mu,R_e(0),h_e =", x, flush=True)

sec(f"PHASE 2, STEP 1.  Theorem A, entry by entry   (|lam| <= {NMAX})")
for e in EE:
    ok = bad = 0; badex = []
    nrib = nmulti = nsq = 0
    degmax = 0
    for lam, mu in pairs(NMAX, e):
        lhs = S.pair_hooks(mu, lam, e, t)
        cells = S.boxes(mu, lam)
        c, h, sq = S.shape_stats(mu, lam)
        rhs = sp.Integer(0) if sq else sp.expand(t**h * (1 + t)**(c - 1))
        if c == 1 and not sq:
            nrib += 1
        elif sq:
            nsq += 1
        else:
            nmulti += 1
        if sp.expand(lhs - rhs) == 0:
            ok += 1
            degmax = max(degmax, sp.Poly(lhs, t).degree() if lhs != 0 else 0)
        else:
            bad += 1
            if len(badex) < 4:
                badex.append((lam, mu, "c=%d h=%d sq=%s" % (c, h, sq), lhs, rhs))
    print(f"  e={e}:  Theorem A holds on {ok}/{ok+bad} entries"
          + (f"   *** FAILURES {bad} ***" if bad else "   (exact)"), flush=True)
    print(f"        support split: {nrib} single ribbons, {nmulti} multi-component"
          f" (no 2x2), {nsq} containing a 2x2 (all zero);  max deg_t = {degmax}"
          f"  (f_e has deg_t = {e-1})", flush=True)
    for x in badex:
        print("      FAIL:", x, flush=True)

sec(f"PHASE 2, STEP 2.  T2:  M_{{f_e(t)}} - R_e(t) = (1+t) E_e(t),  E_e polynomial")
for e in EE:
    ok = bad = 0; nz = 0; ex = []
    for lam, mu in pairs(NMAX, e):
        D = sp.expand(S.pair_hooks(mu, lam, e, t) - R_entry(mu, lam, e, t))
        if D == 0:
            ok += 1
            continue
        Q, Rm = sp.div(sp.Poly(D, t), sp.Poly(1 + t, t))
        if Rm.as_expr() == 0:
            ok += 1; nz += 1
            if len(ex) < 2:
                ex.append((lam, mu, sp.factor(D)))
        else:
            bad += 1
    print(f"  e={e}:  (1+t) | (M_f - R) on {ok}/{ok+bad};  {nz} entries with NONZERO defect"
          + (f"   *** NOT DIVISIBLE: {bad} ***" if bad else ""), flush=True)
    for x in ex:
        print("      nonzero defect e.g.:", x, flush=True)

sec("PHASE 2, STEP 3.  T4:  is [R_e(t), R_e'(t)] nonzero at generic t?")
for (e1, e2) in [(2, 3), (2, 4), (3, 4), (2, 2)]:
    NM = 10 if (e1, e2) == (2, 3) else 8
    lams = S.parts_upto(NM)
    allp = {}
    for k in range(0, NM + e1 + e2 + 1):
        allp[k] = S.parts_of(k)
    nz_entries = 0; total = 0; ex = []
    div_ok = div_bad = 0
    for lam in lams:
        n = sum(lam)
        # (R_{e1} R_{e2} - R_{e2} R_{e1}) |lam>
        acc = {}
        for (a, b, sgn) in [(e1, e2, 1), (e2, e1, -1)]:
            for nu in allp[n + b]:
                if not S.contains(nu, lam):
                    continue
                c1 = R_entry(nu, lam, b, t)
                if c1 == 0:
                    continue
                for mu in allp[n + b + a]:
                    if not S.contains(mu, nu):
                        continue
                    c2 = R_entry(mu, nu, a, t)
                    if c2 == 0:
                        continue
                    acc[mu] = sp.expand(acc.get(mu, 0) + sgn * c1 * c2)
        for mu, v in acc.items():
            total += 1
            v = sp.expand(v)
            if v != 0:
                nz_entries += 1
                if len(ex) < 3:
                    ex.append((lam, mu, sp.factor(v)))
                if sp.expand(v.subs(t, -1)) == 0:
                    div_ok += 1
                else:
                    div_bad += 1
            else:
                div_ok += 1
    print(f"  [R_{e1}(t), R_{e2}(t)]  on |lam|<={NM}:  {nz_entries} NONZERO entries"
          f" of {total} reachable;  vanish at t=-1: {div_ok} ok, {div_bad} BAD", flush=True)
    for x in ex:
        print("      e.g.:", x, flush=True)
