"""The t=0 two-bead model, and the claimed closed form.

At t=0 only height-0 hops survive: R_e(0) moves one bead right by e with no bead
in (b,b+e].  Beads never pass, so a target fixes each bead's displacement.

Source lambda=(g-1): beads at b1=g-2, b2=-2, b3=-3,...   (gap g = b1-b2)
Target mu=(g-1+Sigma_S, Sigma_Sbar): bead1 gets S, bead2 gets Sbar, rest fixed.
Legality of a bead-2 hop at time s:  Q_{<=s} < g + P_{<s}.
"""
import itertools, sys

def U_words(k):
    """unimodal-with-peak-k words rho_T, with sign (-1)^{|T|}. Index set 1..k."""
    out = []
    for r in range(k):
        for T in itertools.combinations(range(1, k), r):
            D = sorted(set(range(1, k)) - set(T), reverse=True)
            out.append((list(T) + [k] + D, (-1)**len(T)))
    return out

def legal(w, Sbar, es, g):
    P = Q = 0
    for i in w:
        if i in Sbar:
            Q += es[i-1]
            if not (Q < g + P): return False
        else:
            P += es[i-1]
    return True

def G(es, Sbar, g):
    k = len(es)
    return sum(sg for w, sg in U_words(k) if legal(w, frozenset(Sbar), es, g))

def N_brute(k, Sbar):
    """sum of signs over w in U whose first |Sbar| letters are exactly Sbar."""
    r = len(Sbar); S = frozenset(Sbar)
    return sum(sg for w, sg in U_words(k) if frozenset(w[:r]) == S)

def N_formula(k, Sbar):
    S = set(Sbar); r = len(S)
    if (k-1 in S) and (k not in S): return (-1)**r
    if (k in S) and (k-1 not in S): return (-1)**(r-1)
    return 0

def Pi_coeff(es, d):
    """[x^d] prod_{i<=k-2}(1-x^{e_i})"""
    if d < 0: return 0
    poly = {0: 1}
    for e in es[:-2]:
        new = dict(poly)
        for a, c in poly.items(): new[a+e] = new.get(a+e, 0) - c
        poly = new
    return poly.get(d, 0)

def entry_formula(es):
    """claimed <(E-1,emin) | C_k(0) | (emin-1)>"""
    a, b = es[-2], es[-1]
    return 1 - Pi_coeff(es, a-b) if a < b else Pi_coeff(es, b-a) - 1

# --- check 1: N(Sbar) closed form, brute force over all subsets, k=2..7
bad = 0
for k in range(2, 8):
    for r in range(1, k+1):
        for Sbar in itertools.combinations(range(1, k+1), r):
            if N_brute(k, Sbar) != N_formula(k, Sbar):
                bad += 1; print("N MISMATCH", k, Sbar, N_brute(k,Sbar), N_formula(k,Sbar))
print(f"check 1  N(Sbar) closed form: {bad} mismatches over k=2..7, all subsets")

# --- check 2: G(Sbar) = -N(Sbar) when g = Sigma_Sbar
bad = 0; n = 0
for k in range(2, 7):
    for es in itertools.product(range(2, 6), repeat=k):
        for r in range(1, k):
            for Sbar in itertools.combinations(range(1, k+1), r):
                g = sum(es[i-1] for i in Sbar)
                n += 1
                if G(es, Sbar, g) != -N_formula(k, Sbar):
                    bad += 1
                    if bad < 5: print("G MISMATCH", es, Sbar, g, G(es,Sbar,g), -N_formula(k,Sbar))
print(f"check 2  G(Sbar) = -N(Sbar) when g=Sigma_Sbar: {bad} mismatches / {n} cases")

# --- check 3: full entry = sum over Sbar with Sigma_Sbar = emin, vs closed form
bad = 0; n = 0
for k in range(2, 7):
    for es in itertools.product(range(2, 7), repeat=k):
        if es[-2] == es[-1]: continue
        emin = min(es[-2], es[-1]); g = emin
        tot = 0
        for r in range(1, k):
            for Sbar in itertools.combinations(range(1, k+1), r):
                if sum(es[i-1] for i in Sbar) == emin:
                    tot += G(es, Sbar, g)
        n += 1
        pred = entry_formula(es); sgn = 1 if es[-1] > es[-2] else -1
        if tot != pred or tot != sgn:
            bad += 1
            if bad < 6: print("ENTRY MISMATCH", es, "model", tot, "formula", pred, "sgn", sgn)
print(f"check 3  entry = sgn(e_k-e_(k-1)): {bad} mismatches / {n} tuples, k=2..6")
