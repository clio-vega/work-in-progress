"""Exact (enumeration) check of the theta-neighbour pair factors in Lyra ee7a961.

Item a, partner b (same block).  Under H0 the four indicators W_i(a), W_i(b), W_j(a), W_j(b)
are independent Bernoulli(p_i(a)), (p_i(b)), (q(a)), (q(b)), q = p_j.
Lyra's per-item increments:  X_a = W_i(a)W_j(a) - W_i(a)W_j(b) - delta,
                             X_b = W_i(b)W_j(b) - W_i(b)W_j(a) - delta,
delta = 2 eps_pair^2,  eps_pair = max(|dp_i|, |dq|)/2   (make_theta_neighbour_block_pairing).
Checks:
 (1) per-item mean E[X] <= 0 ?  (the docstring's inequality  p_i * 2eps <= 2eps^2)
 (2) pair-sum mean E[X_a + X_b] <= 0 ?   (the n=2 Prop-1 bound)
 (3) pair product E[(1+lam X_a)(1+lam X_b)] <= 1 for lam in [0, 1/(1+delta)] ?
"""
import itertools, numpy as np

def judge_probs(theta):                       # copied from dgp.py (Lyra)
    return (np.clip(0.30 + 0.50*(theta-0.5), 0.02, 0.98),
            np.clip(0.35 + 0.50*(theta-0.5), 0.02, 0.98))

def moments(pa, pb, qa, qb, lam):
    eps = max(abs(pa-pb), abs(qa-qb))/2; d = 2*eps**2
    EXa = EXb = Eprod = 0.0
    for wia, wib, wja, wjb in itertools.product((0,1), repeat=4):
        pr = ((pa if wia else 1-pa)*(pb if wib else 1-pb)*(qa if wja else 1-qa)*(qb if wjb else 1-qb))
        xa = wia*wja - wia*wjb - d; xb = wib*wjb - wib*wja - d
        EXa += pr*xa; EXb += pr*xb; Eprod += pr*(1+lam*xa)*(1+lam*xb)
    return EXa, EXb, Eprod, d

# (A) Lyra's DGP: theta_a < theta_b, gap g (typical neighbour gap ~ 1/21)
print("Lyra DGP, theta_a=0.5-g/2, theta_b=0.5+g/2")
for g in (0.01, 1/21, 0.1, 0.2):
    (pa, pb), (qa, qb) = [judge_probs(np.array([0.5-g/2, 0.5+g/2]))[k] for k in (0,1)]
    EXa, EXb, Ep, d = moments(pa, pb, qa, qb, 0.9)
    print(f"  g={g:.4f} delta={d:.2e}  E[X_a]={EXa:+.2e}  E[X_b]={EXb:+.2e}  "
          f"E[X_a+X_b]={EXa+EXb:+.2e}  E[pair product, lam=.9]-1={Ep-1:+.2e}")

# (B) worst case over a grid of all marginals in [0,1]^4 and lam on its cap
rng = np.random.default_rng(0)
worst_item = worst_sum = worst_prod = -9
for _ in range(20000):
    pa, pb, qa, qb = rng.uniform(size=4)
    for lam in (0.25, 0.5, 1.0):
        EXa, EXb, Ep, d = moments(pa, pb, qa, qb, min(lam, 1/(1+2*(max(abs(pa-pb),abs(qa-qb))/2)**2)))
        worst_item = max(worst_item, EXa, EXb); worst_sum = max(worst_sum, EXa+EXb)
        worst_prod = max(worst_prod, Ep-1)
print(f"random [0,1]^4 x lam: max per-item mean {worst_item:+.4f}; max pair-sum mean {worst_sum:+.2e}; "
      f"max E[pair product]-1 {worst_prod:+.2e}")
