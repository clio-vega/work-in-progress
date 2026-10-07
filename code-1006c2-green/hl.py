"""
Hall-Littlewood / Green polynomial engine, 2026-10-06 c2.

TWO INDEPENDENT MECHANISMS for the same matrices:

  Mechanism A (combinatorial): Kostka-Foulkes K_{lam mu}(t) = sum_{SSYT} t^charge,
     then Q'_mu = sum_lam K_{lam mu}(t) s_lam, and G is got by a triangular solve.

  Mechanism B (analytic): P_lam defined as the UNIQUE basis that is
     (i) unitriangular on Schur in dominance order, (ii) orthogonal for the
     HL inner product <p_lam,p_mu>_t = delta z_lam prod (1-t^{lam_i})^{-1}.
     Built by Gram-Schmidt in the POWER SUM basis. No tableaux anywhere.

CONVENTION (pinned here, nowhere quoted):
     p_rho = sum_lam G^lam_rho(t) Q'_lam(x;t),      Q'_lam = sum_nu K_{nu lam}(t) s_nu
  Equivalently, since <P_lam, Q'_mu> = delta (ordinary Hall product),
     G^lam_rho(t) = <p_rho, P_lam(x;t)> = z_rho * [p_rho] P_lam.
"""
from functools import lru_cache
import sympy as sp

t = sp.symbols('t')

# ---------------- partitions ----------------
@lru_cache(maxsize=None)
def partitions(n, maxpart=None):
    if maxpart is None: maxpart = n
    if n == 0: return ((),)
    out = []
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k):
            out.append((k,) + rest)
    return tuple(out)

def conj(lam):
    if not lam: return ()
    return tuple(sum(1 for p in lam if p > i) for i in range(lam[0]))

def n_stat(lam):
    return sum(i * p for i, p in enumerate(lam))

def z_lam(lam):
    from collections import Counter
    c = Counter(lam)
    z = sp.Integer(1)
    for part, m in c.items():
        z *= part**m * sp.factorial(m)
    return z

def dominates(mu, lam):
    """mu >= lam in dominance order."""
    sm = sl = 0
    for i in range(max(len(mu), len(lam))):
        sm += mu[i] if i < len(mu) else 0
        sl += lam[i] if i < len(lam) else 0
        if sm < sl: return False
    return True

def dom_sorted(n):
    """Linear extension of dominance, SMALLEST first ((1^n) ... (n))."""
    ps = list(partitions(n))
    # sort by (number of parts desc) then reverse-lex: a valid linear extension
    # verified below by assert
    ps.sort(key=lambda l: tuple(list(l) + [0]*n))   # lex ascending = linear ext, smallest first
    for i, a in enumerate(ps):
        for b in ps[i+1:]:
            assert not (dominates(a, b) and a != b), (a, b)
    return ps

# ---------------- characters: Murnaghan-Nakayama ----------------
@lru_cache(maxsize=None)
def chi(lam, rho):
    """Irreducible S_n character chi^lam_rho by Murnaghan-Nakayama."""
    if sum(lam) != sum(rho): return 0
    if not rho: return 1
    r, rest = rho[0], rho[1:]
    total = 0
    # remove a border strip of size r from lam in all ways
    for mu, ht in border_strips(lam, r):
        total += (-1)**ht * chi(mu, rest)
    return total

@lru_cache(maxsize=None)
def border_strips(lam, r):
    """All (mu, height-1) with lam/mu a connected border strip of size r.
    Uses the beta-number (first-column hook length) model: a rim hook of
    length r corresponds to beta_i -> beta_i - r when that is free."""
    L = len(lam)
    beta = [lam[i] + (L - 1 - i) for i in range(L)]      # strictly decreasing
    bset = set(beta)
    out = []
    for i in range(L):
        nb = beta[i] - r
        if nb < 0 or nb in bset: continue
        newbeta = sorted([nb if j == i else beta[j] for j in range(L)], reverse=True)
        # height = number of rows the strip spans - 1 = number of beta's strictly
        # between nb and beta[i]  (standard: ht = #{j : nb < beta_j < beta_i})
        ht = sum(1 for b in beta if nb < b < beta[i])
        mu = tuple(newbeta[j] - (L - 1 - j) for j in range(L))
        mu = tuple(x for x in mu if x > 0)
        out.append((mu, ht))
    return tuple(out)

# ---------------- symmetric functions in the p-basis ----------------
# A degree-n symmetric function is a dict {partition: coeff}, coeff in QQ(t).

def p_of_schur(n):
    """s_lam = sum_rho chi^lam_rho / z_rho * p_rho."""
    out = {}
    for lam in partitions(n):
        out[lam] = {rho: sp.Rational(chi(lam, rho), 1) / z_lam(rho)
                    for rho in partitions(n) if chi(lam, rho) != 0}
    return out

def hl_ip(f, g, n):
    """<f,g>_t with <p_lam,p_mu>_t = delta_{lam mu} z_lam prod (1-t^{lam_i})^{-1}."""
    s = sp.Integer(0)
    for rho, c in f.items():
        d = g.get(rho)
        if d is None: continue
        w = z_lam(rho)
        for part in rho: w /= (1 - t**part)
        s += c * d * w
    return sp.cancel(sp.together(s))

def hall_ip(f, g, n):
    """ordinary Hall product: <p_lam,p_mu> = delta z_lam."""
    s = sp.Integer(0)
    for rho, c in f.items():
        d = g.get(rho)
        if d is None: continue
        s += c * d * z_lam(rho)
    return sp.cancel(sp.together(s))

def lin(*pairs):
    """linear combination: lin((c1,f1),(c2,f2),...) of p-basis dicts."""
    out = {}
    for c, f in pairs:
        for rho, v in f.items():
            out[rho] = out.get(rho, 0) + c * v
    return {k: sp.cancel(v) for k, v in out.items() if sp.cancel(v) != 0}

# ---------------- Mechanism B: P_lam by Gram-Schmidt ----------------
@lru_cache(maxsize=None)
def HL_P(n):
    """Returns (order, P_p, P_s): P in p-basis and in Schur basis."""
    order = dom_sorted(n)              # smallest first
    S = p_of_schur(n)
    P_p, norms = {}, {}
    for lam in order:
        v = dict(S[lam])
        for mu in order:
            if mu == lam: break
            c = hl_ip(v, P_p[mu], n)
            if c != 0:
                v = lin((sp.Integer(1), v), (-c / norms[mu], P_p[mu]))
        P_p[lam] = v
        norms[lam] = hl_ip(v, v, n)
    # express in Schur basis:  coefficient of s_nu in f  is  <f, s_nu> (Hall)
    P_s = {}
    for lam in order:
        row = {}
        for nu in order:
            c = hall_ip(P_p[lam], S[nu], n)
            if c != 0: row[nu] = c
        P_s[lam] = row
    return order, P_p, P_s

def green(n, lam, rho):
    """G^lam_rho(t) = z_rho * [p_rho] P_lam   (mechanism B)."""
    _, P_p, _ = HL_P(n)
    return sp.expand(sp.cancel(z_lam(rho) * P_p[lam].get(tuple(rho), 0)))

# ---------------- disk cache ----------------
import os, pickle
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cache')
os.makedirs(CACHE, exist_ok=True)

def HL_P_cached(n):
    f = os.path.join(CACHE, f'P{n}.pkl')
    if os.path.exists(f):
        with open(f, 'rb') as fh: return pickle.load(fh)
    r = HL_P(n)
    with open(f, 'wb') as fh: pickle.dump(r, fh)
    return r

def green_c(n, lam, rho):
    _, P_p, _ = HL_P_cached(n)
    return sp.expand(sp.cancel(z_lam(rho) * P_p[lam].get(tuple(rho), 0)))
