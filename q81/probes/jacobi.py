"""jacobi.py -- CONTROL 4: instrument check, not a conjecture test.
[A,[B,C]] + [B,[C,A]] + [C,[A,B]] = 0 must hold entrywise for the engine.
Also checks anti-symmetry [A,[B,C]] = -[A,[C,B]].
"""
import sys, itertools, sympy as sp
sys.path.insert(0, '.')
from nested import C, sub, t
sys.path.insert(0, '/home/clio/projects/probes/2026-09-04-Q76')
from abacus import parts_of

def add(*ds):
    out = {}
    for d in ds:
        for k, v in d.items(): out[k] = sp.expand(out.get(k, 0) + v)
    return {k: v for k, v in out.items() if v != 0}

bad = 0; n_checked = 0
for n in range(0, 4):
    for lam in parts_of(n):
        for (a, b, c) in itertools.combinations([2, 3, 4, 5], 3):
            L = n + a + b + c + 6
            J = add(C([a, b, c], lam, L), C([b, c, a], lam, L), C([c, a, b], lam, L))
            n_checked += 1
            if J: bad += 1; print('  JACOBI FAIL', lam, (a,b,c), J)
            # antisymmetry of the inner bracket
            A1 = C([a, b, c], lam, L); A2 = C([a, c, b], lam, L)
            if sub(A1, {k: -v for k, v in A2.items()}):
                bad += 1; print('  ANTISYM FAIL', lam, (a,b,c))
print(f'Jacobi + antisymmetry: {n_checked} configurations, {bad} failures')
