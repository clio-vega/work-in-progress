"""Step 3 of the brief: NON-VACUITY, before claiming any agreement.
A pass count is instances/instances; it cannot see rank."""
import sympy as sp, hl, kostka_side as ks
t = sp.symbols('t')
print(f"{'n':>2} {'pairs':>6} {'zero':>5} {'const':>6} {'dim span':>9} {'#unknowns':>10} {'falsifiable':>12}")
print('-'*62)
for n in range(2, 9):
    order,_,_ = hl.HL_P_cached(n)
    vals = []
    for lam in order:
        for y in range(1, n//2+1):
            x = n-y
            vals.append(((lam,(x,y)), sp.Poly(ks.Y(n,lam,(x,y)), t)))
    pairs = len(vals)
    zero  = sum(1 for _,v in vals if v.is_zero)
    const = sum(1 for _,v in vals if v.total_degree() == 0)
    # dim of the span of the Y's as vectors of t-coefficients
    maxdeg = max(v.total_degree() for _,v in vals)
    M = sp.Matrix([[v.coeff_monomial(t**k) for k in range(maxdeg+1)] for _,v in vals])
    dim = M.rank()
    # unknowns in Theorem B's closed form: one coefficient c_{lam,nu} per
    # (lam, nu) with l(nu)<=2 -- i.e. per lam, 1 + #{2-part nu} values
    unk = len(order)*(1 + n//2)
    falsif = pairs - zero - const
    print(f'{n:>2} {pairs:>6} {zero:>5} {const:>6} {dim:>9} {unk:>10} {falsif:>12}')
print()
print('degenerate strata, reported separately (n<=8):')
strata = {'y=0 (one-part)':0, 'x=y':0, 'lam hook':0, 'lam=(n)':0, 'lam=(1^n)':0,
          'Y const in t':0, 'Y==0':0, 'generic':0}
for n in range(2, 9):
    order,_,_ = hl.HL_P_cached(n)
    for lam in order:
        hook = len(lam)==1 or all(p==1 for p in lam[1:])
        for y in range(1, n//2+1):
            x = n-y
            v = sp.Poly(ks.Y(n,lam,(x,y)), t)
            if x==y: strata['x=y'] += 1
            if hook: strata['lam hook'] += 1
            if lam==(n,): strata['lam=(n)'] += 1
            if lam==tuple([1]*n): strata['lam=(1^n)'] += 1
            if v.is_zero: strata['Y==0'] += 1
            elif v.total_degree()==0: strata['Y const in t'] += 1
            if not (x==y or hook or v.total_degree()==0): strata['generic'] += 1
    strata['y=0 (one-part)'] += len(order)
for k,v in strata.items(): print(f'  {k:18s} {v}')
print()
print('t=0 and t=1 specialisations (these are NOT free passes - they are controls):')
for n in range(2,7):
    order,_,_ = hl.HL_P_cached(n)
    b0=b1=tot=0
    for lam in order:
        for y in range(1,n//2+1):
            x=n-y; tot+=1
            Yv = ks.Y(n,lam,(x,y))
            if sp.expand(Yv.subs(t,0) - hl.chi(lam,tuple(sorted((x,y),reverse=True)))) != 0: b0+=1
            # t=1: <p_rho, h_lam> = # assignments of rho's parts to blocks of sizes lam
            import hexp
            hv = hexp.h_in_p(lam, n)
            want = hl.hall_ip({tuple(sorted((x,y),reverse=True)): sp.Integer(1)}, hv, n)
            if sp.expand(Yv.subs(t,1) - want) != 0: b1+=1
    print(f'  n={n}: Y(0)=chi^lam_rho  mismatches={b0}/{tot};  Y(1)=<p_rho,h_lam>  mismatches={b1}/{tot}')
