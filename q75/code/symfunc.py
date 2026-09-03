"""symfunc.py -- a small, self-contained symmetric-function engine.

Deliberately INDEPENDENT of the Murnaghan-Nakayama rule and of the abacus code
in probes/2026-09-03-Q63-form-ii/fock_ell.py, because both are things the Q75
computations are meant to TEST.  Everything here is built from two primitives:

  * Kostka numbers K_{lam,rho} = #SSYT(shape lam, content rho), by direct
    recursive enumeration of horizontal strips;
  * the monomial basis, f = sum_rho a_rho m_rho, with products computed from
    [x^nu](f g) = sum_{alpha <= nu} [x^alpha]f . [x^{nu-alpha}]g
    and [x^alpha]f = a_{sort(alpha)}.

Schur decomposition is by dominance-triangularity: s_nu = m_nu + (lower).
"""
from functools import lru_cache
import sympy as sp

# --------------------------------------------------------------- partitions
def parts_of(n, cap=None):
    if cap is None:
        cap = n
    if n == 0:
        return [()]
    out = []
    for p in range(min(n, cap), 0, -1):
        for rest in parts_of(n - p, p):
            out.append((p,) + rest)
    return out

def parts_upto(n):
    return [lam for k in range(n + 1) for lam in parts_of(k)]

def trim(t):
    t = tuple(t)
    while t and t[-1] == 0:
        t = t[:-1]
    return t

def srt(v):
    return trim(tuple(sorted(v, reverse=True)))

# ------------------------------------------------------------ Kostka numbers
@lru_cache(maxsize=None)
def hstrips(lam, k):
    """all mu <= lam with lam/mu a horizontal k-strip (returns tuple of mu)."""
    lam = trim(lam)
    n = len(lam)
    out = []
    def rec(i, rem, cur):
        if i == n:
            if rem == 0:
                out.append(trim(tuple(cur)))
            return
        # mu_i must satisfy lam_{i+1} <= mu_i <= lam_i   (interlacing)
        lo = lam[i + 1] if i + 1 < n else 0
        for mi in range(lo, lam[i] + 1):
            d = lam[i] - mi
            if d <= rem:
                rec(i + 1, rem - d, cur + [mi])
    rec(0, k, [])
    return tuple(out)

@lru_cache(maxsize=None)
def kostka(lam, rho):
    """#SSYT of shape lam, content rho."""
    lam, rho = trim(lam), trim(rho)
    if sum(lam) != sum(rho):
        return 0
    if not lam:
        return 1
    if not rho:
        return 0
    last = rho[-1]
    return sum(kostka(mu, rho[:-1]) for mu in hstrips(lam, last))

# ---------------------------------------------- symmetric functions, m-basis
# A symmetric function is a dict {partition rho : coefficient of m_rho}.

def schur_m(lam):
    lam = trim(lam)
    n = sum(lam)
    return {rho: sp.Integer(kostka(lam, rho)) for rho in parts_of(n)
            if kostka(lam, rho)}

def coeff_mono(f, alpha):
    """[x^alpha] f, for an arbitrary exponent vector alpha."""
    return f.get(srt(alpha), 0)

def mult(f, g, nvars):
    """product of two homogeneous symmetric functions, in the m-basis."""
    df = sum(next(iter(f))) if f else 0
    dg = sum(next(iter(g))) if g else 0
    n = df + dg
    out = {}
    for nu in parts_of(n):
        v = tuple(nu) + (0,) * (nvars - len(nu))
        if len(nu) > nvars:
            continue
        tot = 0
        # iterate over alpha <= v componentwise
        def rec(i, alpha):
            nonlocal tot
            if i == len(v):
                if sum(alpha) != df:
                    return
                a = coeff_mono(f, alpha)
                if a == 0:
                    return
                b = coeff_mono(g, tuple(v[j] - alpha[j] for j in range(len(v))))
                if b:
                    tot += a * b
                return
            rem_max = sum(v[i:])
            for ai in range(0, v[i] + 1):
                if sum(alpha) + ai > df:
                    break
                if sum(alpha) + ai + rem_max - v[i] < df:
                    continue
                rec(i + 1, alpha + (ai,))
        rec(0, ())
        if tot:
            out[tuple(nu)] = sp.sympify(tot)
    return out

def dominates(a, b):
    """a >= b in dominance (same size)."""
    sa = sb = 0
    for i in range(max(len(a), len(b))):
        sa += a[i] if i < len(a) else 0
        sb += b[i] if i < len(b) else 0
        if sa < sb:
            return False
    return True

def to_schur(f):
    """decompose an m-basis symmetric function into {lam : coeff of s_lam}."""
    f = {k: sp.expand(v) for k, v in f.items() if sp.expand(v) != 0}
    out = {}
    while f:
        # dominance-maximal support element
        cands = [nu for nu in f if all(not dominates(o, nu) or o == nu for o in f)]
        nu = max(cands, key=lambda x: (len(x) == 0, x))
        nu = cands[0]
        c = f[nu]
        out[nu] = sp.expand(c)
        s = schur_m(nu)
        for rho, k in s.items():
            f[rho] = sp.expand(f.get(rho, 0) - c * k)
            if f[rho] == 0:
                del f[rho]
    return out

# ------------------------------------------------------------ power sums etc.
def p_m(e):
    return {(e,): sp.Integer(1)}

def h_m(a):
    if a == 0:
        return {(): sp.Integer(1)}
    return schur_m((a,))

def e_m(b):
    if b == 0:
        return {(): sp.Integer(1)}
    return schur_m((1,) * b)

def hook(e, k):
    return trim((e - k,) + (1,) * k)

def f_e_m(e, t):
    """f_e(t) = sum_{k=0}^{e-1} t^k s_{(e-k,1^k)}  in the m-basis."""
    out = {}
    for k in range(e):
        for rho, c in schur_m(hook(e, k)).items():
            out[rho] = sp.expand(out.get(rho, 0) + t**k * c)
    return {k: v for k, v in out.items() if v != 0}

# --------------------------------------------------------- shapes and strips
def contains(mu, lam):
    lam = trim(lam); mu = trim(mu)
    if len(lam) > len(mu):
        return False
    return all(lam[i] <= mu[i] for i in range(len(lam)))

def boxes(mu, lam):
    """cells of mu/lam as (row, col), 1-indexed."""
    mu, lam = trim(mu), trim(lam)
    out = []
    for i in range(len(mu)):
        lo = lam[i] if i < len(lam) else 0
        for j in range(lo + 1, mu[i] + 1):
            out.append((i + 1, j))
    return out

def is_hstrip(mu, lam):
    return len(set(c for _, c in boxes(mu, lam))) == len(boxes(mu, lam))

def is_vstrip(mu, lam):
    return len(set(r for r, _ in boxes(mu, lam))) == len(boxes(mu, lam))

def components(cells):
    """connected components of a set of cells (edge-adjacency)."""
    cells = set(cells)
    seen, comps = set(), []
    for c in cells:
        if c in seen:
            continue
        stack, comp = [c], []
        seen.add(c)
        while stack:
            x = stack.pop(); comp.append(x)
            for d in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                y = (x[0] + d[0], x[1] + d[1])
                if y in cells and y not in seen:
                    seen.add(y); stack.append(y)
        comps.append(comp)
    return comps

def has_2x2(cells):
    s = set(cells)
    return any((r, c) in s and (r + 1, c) in s and (r, c + 1) in s and (r + 1, c + 1) in s
               for (r, c) in s)

def shape_stats(mu, lam):
    """(#components, h = sum(rows_i - 1), has_2x2)."""
    cs = boxes(mu, lam)
    comps = components(cs)
    h = sum(len(set(r for r, _ in comp)) - 1 for comp in comps)
    return len(comps), h, has_2x2(cs)

def is_ribbon(mu, lam, e):
    cs = boxes(mu, lam)
    if len(cs) != e:
        return False
    c, h, sq = shape_stats(mu, lam)
    return c == 1 and not sq

# ------------------------------------------------------- skew Schur functions
@lru_cache(maxsize=None)
def skew_hstrips(mu, lam, k):
    """all nu with lam <= nu <= mu and mu/nu a horizontal k-strip."""
    mu, lam = trim(mu), trim(lam)
    n = len(mu)
    out = []
    def rec(i, rem, cur):
        if i == n:
            if rem == 0:
                out.append(trim(tuple(cur)))
            return
        lomu = mu[i + 1] if i + 1 < n else 0     # interlacing with mu
        lolam = lam[i] if i < len(lam) else 0    # must contain lam
        lo = max(lomu, lolam)
        for ni in range(lo, mu[i] + 1):
            d = mu[i] - ni
            if d <= rem:
                rec(i + 1, rem - d, cur + [ni])
    rec(0, k, [])
    return tuple(out)

@lru_cache(maxsize=None)
def skew_kostka(mu, lam, rho):
    mu, lam, rho = trim(mu), trim(lam), trim(rho)
    if sum(mu) - sum(lam) != sum(rho):
        return 0
    if mu == lam:
        return 1
    if not rho:
        return 0
    return sum(skew_kostka(nu, lam, rho[:-1]) for nu in skew_hstrips(mu, lam, rho[-1]))

@lru_cache(maxsize=None)
def skew_schur(mu, lam):
    """{nu : coefficient of s_nu in s_{mu/lam}} -- the LR coefficients c^mu_{lam,nu}."""
    n = sum(trim(mu)) - sum(trim(lam))
    m = {rho: sp.Integer(skew_kostka(mu, lam, rho)) for rho in parts_of(n)
         if skew_kostka(mu, lam, rho)}
    return {k: int(v) for k, v in to_schur(m).items()}

def pair_hooks(mu, lam, e, t):
    """<s_{mu/lam}, f_e(t)> = sum_k t^k c^mu_{lam,(e-k,1^k)}."""
    sk = skew_schur(mu, lam)
    return sp.expand(sum(t**k * sk.get(hook(e, k), 0) for k in range(e)))

def pair_p(mu, lam, e):
    """<s_{mu/lam}, p_e> via the hook expansion p_e = sum_k (-1)^k s_{(e-k,1^k)}."""
    return pair_hooks(mu, lam, e, sp.Integer(-1))

# ------------------------------------------------------ the splitting count G_S
def G_S(mu, lam, t):
    """sum_b t^b #{nu : lam<=nu<=mu, nu/lam horizontal, mu/nu vertical}."""
    tot = 0
    n = sum(trim(mu)) - sum(trim(lam))
    for b in range(n + 1):
        cnt = 0
        for nu in skew_hstrips(mu, lam, b):        # mu/nu a horizontal b-strip
            pass
        # enumerate nu directly
        for nu in _between(mu, lam):
            if sum(nu) - sum(trim(lam)) == n - b and is_hstrip(nu, lam) and is_vstrip(mu, nu):
                cnt += 1
        if cnt:
            tot += t**b * cnt
    return sp.expand(tot)

@lru_cache(maxsize=None)
def _between(mu, lam):
    mu, lam = trim(mu), trim(lam)
    n = len(mu)
    out = []
    def rec(i, cur):
        if i == n:
            out.append(trim(tuple(cur)))
            return
        lo = lam[i] if i < len(lam) else 0
        hi = mu[i]
        prev = cur[-1] if cur else None
        for v in range(lo, hi + 1):
            if prev is not None and v > prev:
                continue
            rec(i + 1, cur + [v])
    rec(0, [])
    return tuple(out)
