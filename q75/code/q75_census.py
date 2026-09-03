"""q75_census.py -- Phase 1 (the anchor correction) and Phase 2 (the theorem).

Every claim below is stated with its NEGATIVE CONTROL, and the control is run.
"""
import sys, time
sys.path.insert(0, "/home/clio/projects/probes/2026-09-03-Q75")
import symfunc as S
import sympy as sp

t = sp.Symbol("t")


def R_entry(mu, lam, e, tval, height=lambda rows: rows - 1):
    """<s_mu | R_e(t) | s_lam> = t^h if mu/lam is an e-ribbon, else 0."""
    if not S.contains(mu, lam) or sum(S.trim(mu)) - sum(S.trim(lam)) != e:
        return sp.Integer(0)
    cells = S.boxes(mu, lam)
    comps = S.components(cells)
    if len(comps) != 1 or S.has_2x2(cells):
        return sp.Integer(0)
    rows = len(set(r for r, _ in cells))
    return sp.expand(tval ** height(rows))


def pairs(nmax, e):
    for lam in S.parts_upto(nmax):
        for mu in S.parts_of(sum(lam) + e):
            if S.contains(mu, lam):
                yield lam, mu


def sec(title):
    print("\n" + "=" * 78, flush=True)
    print(title, flush=True)
    print("=" * 78, flush=True)


NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 8
EE = [2, 3, 4]

# ---------------------------------------------------------------- PHASE 1
sec(f"PHASE 1.  ANCHOR:  R_e(-1) = multiplication by p_e   (|lam| <= {NMAX})")

for e in EE:
    ok = bad = 0; badex = []
    ncA = ncB = ncC = 0; ncAt = ncBt = ncCt = 0
    for lam, mu in pairs(NMAX, e):
        lhs = R_entry(mu, lam, e, sp.Integer(-1))
        rhs = S.pair_p(mu, lam, e)
        if sp.simplify(lhs - rhs) == 0:
            ok += 1
        else:
            bad += 1
            if len(badex) < 3:
                badex.append((lam, mu, lhs, rhs))
        # NC2: R_e(+1) vs p_e -- must differ somewhere
        if sp.simplify(R_entry(mu, lam, e, sp.Integer(1)) - rhs) != 0:
            ncB += 1
        ncBt += 1
        # NC3: perturbed height convention h' = rows (not rows-1)
        alt = R_entry(mu, lam, e, sp.Integer(-1), height=lambda rows: rows)
        if sp.simplify(alt - rhs) != 0:
            ncC += 1
        ncCt += 1
    # NC1: p_e^perp -- wrong direction.  <s_mu | p_e^perp | s_lam> = <s_{lam/mu}, p_e>
    for lam, mu in pairs(NMAX, e):
        perp = S.pair_p(mu, lam, e)      # this is the (mu,lam) entry of M_{p_e}
        # the adjoint operator's (mu',lam) entries live on mu' SUBSET lam:
    for lam in S.parts_upto(NMAX):
        for nu in S.parts_of(sum(lam) - e) if sum(lam) >= e else []:
            if S.contains(lam, nu):
                ncAt += 1
                if sp.simplify(R_entry(nu, lam, e, sp.Integer(-1))
                               - S.pair_p(lam, nu, e)) != 0:
                    ncA += 1
    print(f"  e={e}:  R_e(-1) == M_{{p_e}}  on {ok}/{ok+bad} entries"
          + (f"   MISMATCHES {bad}" if bad else "   (exact)"), flush=True)
    for x in badex:
        print("      mismatch:", x, flush=True)
    print(f"        NC1  p_e^perp (wrong direction):  disagrees on {ncA}/{ncAt}"
          f"   {'CONTROL FIRES' if ncA else 'CONTROL DEAD'}", flush=True)
    print(f"        NC2  R_e(+1) vs p_e:              disagrees on {ncB}/{ncBt}"
          f"   {'CONTROL FIRES' if ncB else 'CONTROL DEAD'}", flush=True)
    print(f"        NC3  height h'=rows:              disagrees on {ncC}/{ncCt}"
          f"   {'CONTROL FIRES' if ncC else 'CONTROL DEAD'}", flush=True)

# independent cross-check of the RHS by a route that never uses the hook expansion
sec("PHASE 1b.  cross-check of M_{p_e} by monomial-basis multiplication (no hooks)")
for e in [2, 3]:
    ok = bad = 0
    for lam in S.parts_upto(5):
        prod = S.to_schur(S.mult(S.p_m(e), S.schur_m(lam), sum(lam) + e))
        for mu in S.parts_of(sum(lam) + e):
            a = sp.sympify(prod.get(mu, 0))
            b = S.pair_p(mu, lam, e)
            ok, bad = (ok + 1, bad) if sp.simplify(a - b) == 0 else (ok, bad + 1)
    print(f"  e={e}:  hook-expansion route == m-basis route on {ok}/{ok+bad}"
          + (f"   MISMATCH {bad}" if bad else ""), flush=True)
