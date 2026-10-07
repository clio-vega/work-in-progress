"""TASK 1 step 4: NON-VACUOUS replacement controls for Theorem B, counts predicted FIRST.

C8_nu (nu |- 5):  perturb K[(nu, (1^5))] by +t.   Only lam=(1^5) is affected, and the
   LHS shifts by t*chi^nu_rho, so Theorem B must fail at ((1^5),rho) exactly when
   chi^nu_rho != 0.  PREDICTION: fails = #{rho two-part |- 5 : chi^nu_rho != 0}.
   This family CONTAINS C1's silence as its nu=(3,1,1) instance, predicted in advance.

C9: drop the multiplicity factor (1+[x=y]) -> 1 in Theorem B.  PREDICTION: fails exactly
   on the pairs with x=y and c_{lam,(x,y)} != 0, i.e. n even and lam with a nonzero
   h_{(n/2,n/2)} coefficient.  Counted in advance below, then tested.
"""
import sympy as sp, hl, kostka_side as ks, raising
t = sp.symbols('t')

# ================= C8 family =================
n = 5
order, K = ks.kostka_matrix(n)
two_part = [tuple(sorted((n-y,y), reverse=True)) for y in range(1, n//2+1)]
lam_pert = (1,1,1,1,1)
RHS = {}
for lam in order:
    C = raising.Qprime_h(lam)
    for y in range(1, n//2+1):
        x = n-y
        RHS[(lam,(x,y))] = C.get((n,),0) + (2 if x==y else 1)*C.get(tuple(sorted((x,y),reverse=True)),0)

print('C8 family: perturb K[(nu,(1^5))] by +t.  nonvacuous <=> some chi^nu_rho != 0')
print(' nu              K entry nonzero?  predicted  observed  match')
allmatch = True
for nu in order:
    predicted = sum(1 for rho in two_part if hl.chi(nu, rho) != 0)
    Kp = dict(K); Kp[(nu,lam_pert)] = sp.expand(Kp[(nu,lam_pert)] + t)
    obs = 0
    for lam in order:
        for y in range(1, n//2+1):
            x = n-y
            Yp = sp.expand(sum(Kp[(v,lam)]*hl.chi(v,(x,y)) for v in order))
            if sp.expand(Yp - RHS[(lam,(x,y))]) != 0: obs += 1
    ok = (obs == predicted); allmatch &= ok
    print(f' {str(nu):15s} {str(K[(nu,lam_pert)]!=0):>8s}        {predicted:>6d}    {obs:>6d}   {"OK" if ok else "MISMATCH"}')
print(f'C8: all 7 predictions match = {allmatch}')
print(f'C8 non-vacuous instances (predicted fails > 0): '
      f'{sum(1 for nu in order if any(hl.chi(nu,r)!=0 for r in two_part))}/7')

# ================= C9 =================
print()
pred_list = []
for nn in range(2, 8):
    if nn % 2: continue
    o,_,_ = hl.HL_P_cached(nn)
    h = nn//2
    for lam in o:
        if raising.Qprime_h(lam).get((h,h), 0) != 0: pred_list.append((nn,lam))
print(f'C9 PREDICTION (made before running): fails on exactly the {len(pred_list)} pairs')
print('    ', pred_list)
obs = []
for nn in range(2, 8):
    o,_,_ = hl.HL_P_cached(nn)
    for lam in o:
        C = raising.Qprime_h(lam)
        for y in range(1, nn//2+1):
            x = nn-y
            bad_pred = C.get((nn,),0) + 1*C.get(tuple(sorted((x,y),reverse=True)),0)   # factor dropped
            if sp.expand(ks.Y(nn,lam,(x,y)) - bad_pred) != 0: obs.append((nn,lam))
print(f'C9 OBSERVED: fails on {len(obs)} pairs')
print('    ', obs)
print(f'C9: prediction matches observation = {sorted(obs)==sorted(pred_list)}   [{"FIRED" if obs else "SILENT"}]')
