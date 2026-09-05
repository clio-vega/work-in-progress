"""sharp.py -- sharpness test via Q81 thm:red, INDEPENDENT of the entry formula.

  C_k/(1+t)|_{t=-1} = ad_{p_{e1}}..ad_{p_{e_{k-2}}} ( Q_{e_{k-1},e_k}(-1) ),
  Q_{a,b}(-1) = [N_b, M_{p_a}] - [N_a, M_{p_b}].
Sharp  <=>  this operator is nonzero.
NOTE: ad's commute, so the answer depends only on the SET {e_1..e_{k-2}}
      and the ordered pair (e_{k-1}, e_k).
"""
import sys; sys.path.insert(0, '.')
from ops import shape_op, comm

def Q(a, b):
    A = comm(shape_op(b, 2), shape_op(a, 1))     # [N_b, M_{p_a}]
    B = comm(shape_op(a, 2), shape_op(b, 1))     # [N_a, M_{p_b}]
    def op(st):
        x = A(st); y = B(st); out = dict(x)
        for kk, v in y.items(): out[kk] = out.get(kk, 0) - v
        return {kk: v for kk, v in out.items() if v}
    return op

def redop(es):
    op = Q(es[-2], es[-1])
    for a in reversed(es[:-2]):
        op = comm(shape_op(a, 1), op)
    return op

def is_sharp(es, lams=((), (1,), (2,), (1, 1), (2, 1))):
    op = redop(list(es))
    for lam in lams:
        if op({lam: 1}): return True, lam
    return False, None
