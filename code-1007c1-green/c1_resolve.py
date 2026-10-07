"""TASK 1: resolve the silence of control C1, with quantifiers, then TEST the reason.

C1 perturbed K[(nu,lam)] with nu=(3,1,1), lam=(2,1,1,1) by +t and checked Theorem B
on the 14 (lam, (x,y)) pairs at n=5.  It was SILENT (0/14).

Theorem B's check compares
    LHS  Y^lam_rho = sum_nu K_{nu lam}(t) chi^nu_rho          <- reads K
    RHS  c_{lam,(n)} + (1+[x=y]) c_{lam,(x,y)}  from raising   <- does NOT read K
so perturbing K_{nu lam} by +t shifts the LHS by exactly  t * chi^nu_rho  for that one
lam, and by 0 for every other lam.

CANDIDATE REASON (to be tested, not assumed):
    chi^{(3,1,1)}_rho = 0 for EVERY two-part rho |- 5.
=> the control perturbs a quantity that enters the tested identity with coefficient 0.
   VACUOUS BY CONSTRUCTION -- and not for the reason the brief guessed (it guessed
   "Theorem B may not read K at that entry"; it does read it).
"""
import sympy as sp, hl, kostka_side as ks, raising
t = sp.symbols('t')
n = 5
order, K = ks.kostka_matrix(n)
two_part = [tuple(sorted((n-y, y), reverse=True)) for y in range(1, n//2+1)]
print('two-part classes of 5 used by the Theorem B loop:', two_part)

# ---- (a) the brief's guess: does Theorem B's evaluation read K at that entry? ----
nu0, lam0 = (3,1,1), (2,1,1,1)
print()
print('(a) brief\'s guess -- "Theorem B may not read K at that entry":')
print('    K[(nu,lam)] =', sp.factor(K[(nu0,lam0)]), ' (nonzero => the entry IS in the sum)')
print('    LHS Y^lam_rho = sum over ALL', len(order), 'nu of K_{nu lam} chi^nu_rho, so the entry is read.')
print('    => the brief\'s guess is FALSE.')

# ---- (b) the real reason, with quantifiers ----
print()
print('(b) candidate reason: chi^{(3,1,1)}_rho = 0 for every two-part rho |- 5')
for rho in two_part:
    print(f'    chi^{nu0}_{rho} = {hl.chi(nu0, rho)}')
print('    border strips of (3,1,1) of size r:')
for r in range(1, n+1):
    bs = hl.border_strips(nu0, r)
    print(f'      r={r}: {bs}')

# ---- (c) the general statement the silence is an instance of ----
print()
print('(c) GENERAL: perturbing K_{nu lam} by +t makes Theorem B fail at (lam,rho)')
print('    exactly when chi^nu_rho != 0.  Predicted failure count for a +t perturbation')
print('    at (nu, lam) is  #{rho two-part : chi^nu_rho != 0}  (only one lam is affected).')
print()
print('    nu            chi^nu_(4,1)  chi^nu_(3,2)   predicted fails/14')
pred = {}
for nu in order:
    c1_, c2_ = hl.chi(nu,(4,1)), hl.chi(nu,(3,2))
    p = (1 if c1_ else 0) + (1 if c2_ else 0)
    pred[nu] = p
    print(f'    {str(nu):14s} {c1_:>8d} {c2_:>12d} {p:>18d}')
