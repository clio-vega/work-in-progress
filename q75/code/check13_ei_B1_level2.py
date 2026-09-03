"""check13 -- DETECTOR (0a):  [e_i, B_{-1}] = 0  at level ell=2.

Decorrelated by construction:
  * e_i          : MINE.  probes/2026-09-03-Q63-form-ii/fock_ell.py, my Chevalley
                   action (merge-by-content order, tie-break tau).
  * B_{-1}       : LYRA'S, used as a BLACK BOX.  /tmp/lyra-math @ cf743f2
                   (the commit she froze), level2-route1/heisenberg.apply_Bminus,
                   which calls her own straightener wedge.straighten.
                   I have not read either implementation.

BRIDGE (derived from her two ENCODING functions only, wedge.content / wedge.runner,
which are coordinate declarations, not algorithm):
    k = c + n(d-1) + n*ell*m,   c = ((k-1) mod n) + 1 in {1..n},  d in {1..ell}
    iota(k) := c + n*m   is an ORDER-PRESERVING bijection {k : runner(k)=d} -> Z,
    and iota is the shifted-content coordinate p of fock_ell's runner d.
  Consequences, both checked below rather than assumed:
    - B_{-1} sends k -> k + n*ell, i.e. p -> p + n: a bead move b -> b+e on its
      own runner.  Runner-preserving.
    - tau is FORCED, not fitted: larger d  <=>  larger k  <=>  earlier in the
      wedge  <=>  ABOVE.  fock_ell.above(n1,n2,tau) puts d1 > d2 above iff
      tau = -1.  tau = +1 is therefore a NEGATIVE CONTROL and must FAIL.
  A global shift of p changes only the labelling of i, so the offset between my
  charge convention and hers is immaterial provided ALL i in {0..e-1} are tested.
  They are.
"""
import sys, time
import sympy as sp

sys.path.insert(0, "/home/clio/projects/probes/2026-09-03-Q63-form-ii")
sys.path.insert(0, "/tmp/lyra-math/level2-route1")
import fock_ell as ME
import wedge as LYRA_W
import heisenberg as LYRA_H

q = ME.q


# ------------------------------------------------------------------ bridge
def iota_inv(p, d, n, ell):
    """shifted-content p on runner d (1-based) -> wedge index k."""
    c = ((p - 1) % n) + 1
    m = (p - c) // n
    return c + n * (d - 1) + n * ell * m


def iota(k, n, ell):
    """wedge index k -> (p, d) with d 1-based."""
    c = LYRA_W.content(k, n)
    d = LYRA_W.runner(k, n, ell)
    j = (k - c) // n
    m = (j - (d - 1)) // ell
    return c + n * m, d


def mp_to_wedge(mps, s, D, n, ell):
    ks = []
    for d0, lam in enumerate(mps):
        for p in ME.maya(lam, s[d0], D):
            ks.append(iota_inv(p, d0 + 1, n, ell))
    ks.sort(reverse=True)
    assert len(set(ks)) == len(ks)
    return tuple(ks)


def wedge_to_mp(ks, s, D, n, ell):
    """inverse; None if any runner has the wrong bead count or is not a partition."""
    per = {d: [] for d in range(1, ell + 1)}
    for k in ks:
        p, d = iota(k, n, ell)
        per[d].append(p)
    out = []
    for d in range(1, ell + 1):
        if len(per[d]) != D:
            return None
        lam = ME.maya_to_partition(set(per[d]), s[d - 1], D)
        if lam is None:
            return None
        out.append(lam)
    return tuple(out)


def B_lyra(vec, s, D, n, ell):
    """Lyra's B_{-1} transported to the multipartition basis."""
    out = {}
    for mps, coeff in vec.items():
        st = {mp_to_wedge(mps, s, D, n, ell): sp.Integer(1)}
        res = LYRA_H.apply_Bminus(st, 1, n, ell)
        for kt, c2 in res.items():
            tgt = wedge_to_mp(tuple(kt), s, D, n, ell)
            if tgt is None:                       # fell off the truncation
                return None
            out[tgt] = sp.expand(out.get(tgt, 0) + coeff * c2)
    return {k: v for k, v in out.items() if sp.simplify(v) != 0}


def e_mine(vec, i, s, e, D, tau):
    return ME.e_i(vec, i, s, e, D, tau)


def commutator(mps, i, s, e, ell, D, tau):
    v0 = {mps: sp.Integer(1)}
    a = B_lyra(e_mine(v0, i, s, e, D, tau), s, D, e, ell)
    b = e_mine(B_lyra(v0, s, D, e, ell) or {}, i, s, e, D, tau)
    if a is None or B_lyra(v0, s, D, e, ell) is None:
        return "TRUNC"
    diff = {}
    for k in set(a) | set(b):
        d = sp.simplify(sp.expand(a.get(k, 0) - b.get(k, 0)))
        if d != 0:
            diff[k] = d
    return diff


def multiparts(nmax, ell):
    singles = [()]
    def rec(rem, cap, cur):
        for part in range(min(rem, cap), 0, -1):
            nc = cur + (part,)
            singles.append(nc)
            if rem - part > 0:
                rec(rem - part, part, nc)
    for t in range(1, nmax + 1):
        rec(t, t, ())
    singles = list(dict.fromkeys(singles))
    out = []
    for a in singles:
        for b in singles:
            if sum(a) + sum(b) <= nmax:
                out.append((a, b))
    return out


if __name__ == "__main__":
    ELL = 2
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    TAU = int(sys.argv[2]) if len(sys.argv) > 2 else -1
    CHARGES = [(0, 0), (0, 1)]
    EE = [2, 3]
    mps_list = multiparts(NMAX, ELL)
    print("=" * 78, flush=True)
    print(f"DETECTOR (0a):  [e_i, B_-1] = 0   at ell={ELL},  tau={TAU}"
          + ("   <-- FORCED value" if TAU == -1 else "   <-- NEGATIVE CONTROL, must FAIL"),
          flush=True)
    print(f"  my e_i (fock_ell.py) vs Lyra's B_-1 (level2-route1 @ cf743f2, black box)",
          flush=True)
    print(f"  |lam^(1)|+|lam^(2)| <= {NMAX}, charges {CHARGES}, e in {EE}, all i in 0..e-1",
          flush=True)
    print("=" * 78, flush=True)
    t0 = time.time()
    zero = fail = trunc = 0
    examples = []
    for e in EE:
        for s in CHARGES:
            for mps in mps_list:
                D = max(len(mps[0]), len(mps[1])) + e + 2
                for i in range(e):
                    r = commutator(mps, i, list(s), e, ELL, D, TAU)
                    if r == "TRUNC":
                        trunc += 1; tag = "trunc"
                    elif r:
                        fail += 1; tag = "FAIL " + str(list(r.items())[:1])
                        if len(examples) < 3:
                            examples.append((e, s, mps, i, list(r.items())[:1]))
                    else:
                        zero += 1; tag = "zero"
                    print(f"  e={e} s={s} i={i} mps={mps!s:<22} D={D}  {tag}"
                          f"   [{zero}/{zero+fail} zero, {time.time()-t0:6.1f}s]",
                          flush=True)
    print("=" * 78, flush=True)
    print(f"RESULT tau={TAU}:  ZERO {zero}/{zero+fail}   FAILURES {fail}   truncated {trunc}",
          flush=True)
    for x in examples:
        print("   example failure:", x, flush=True)
