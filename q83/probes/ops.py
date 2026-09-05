"""ops.py -- operators as state->state maps; iterated ad_{p_a} against N_e.

REDUCTION (Q81 thm:red + brief section 1), rewritten:
  C_k/(1+t)|_{t=-1} = ad_{p_{e1}}..ad_{p_{e_{k-2}}} ( [N_{ek},M_{p_{e_{k-1}}}] - [N_{e_{k-1}},M_{p_{ek}}] )
                    = - T(e1..e_{k-1}; e_k)  +  T(e1..e_{k-2},e_k ; e_{k-1})
  where T(a_1..a_r; e) := ad_{p_{a_1}}...ad_{p_{a_r}} (N_e)   (symmetric in the a's,
  since the M_{p_a} commute).  So SHARPNESS at level k  <=>  the two T's differ.
"""
import sys, itertools
sys.path.insert(0, '.')
from nlib import _op_row, add_shapes
sys.path.insert(0, '/home/clio/projects/probes/2026-09-03-Q75')
from symfunc import trim

def shape_op(e, want_c):
    def op(state):
        out = {}
        for lam, w in state.items():
            for mu, u in _op_row(lam, e, want_c):
                out[mu] = out.get(mu, 0) + w * u
        return {k: v for k, v in out.items() if v}
    return op

def comm(A, B):
    def op(state):
        x = A(B(state)); y = B(A(state))
        out = dict(x)
        for k, v in y.items(): out[k] = out.get(k, 0) - v
        return {k: v for k, v in out.items() if v}
    return op

def T(alist, e):
    """ad_{p_{a_1}} ... ad_{p_{a_r}} (N_e)"""
    op = shape_op(e, 2)
    for a in reversed(alist):
        op = comm(shape_op(a, 1), op)
    return op
