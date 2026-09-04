"""nested.py -- k-fold nested brackets of the ribbon operators R_e(t) on Fock space.

State: dict {partition : sympy poly in t}.  Operators act linearly.
All bead arithmetic is inherited from probes/2026-09-04-Q76/abacus.py, which
agreed with the independent border-strip engine on 238594 entries.
"""
import sys, sympy as sp
sys.path.insert(0, '/home/clio/projects/probes/2026-09-04-Q76')
sys.path.insert(0, '/home/clio/projects/probes/2026-09-03-Q75')
from abacus import t, beta, unbeta, R_abacus, parts_of, trim

def apply_R(state, e, L):
    out = {}
    for lam, w in state.items():
        if w == 0: continue
        for mu, u in R_abacus(lam, e, L).items():
            out[mu] = out.get(mu, 0) + w * u
    return {k: sp.expand(v) for k, v in out.items() if sp.expand(v) != 0}

def sub(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = sp.expand(out.get(k, 0) - v)
    return {k: v for k, v in out.items() if v != 0}

def bracket(word_left, word_right, state, L):
    """[A,B] where A = product of ops in word_left (applied right-to-left)."""
    raise NotImplementedError

def apply_word(state, word, L):
    """word = (e_1,...,e_r) means R_{e_1} R_{e_2} ... R_{e_r}, rightmost acts first."""
    for e in reversed(word):
        state = apply_R(state, e, L)
    return state

def nested(es, state, L):
    """[R_{e1}, [R_{e2}, [ ... [R_{e_{k-1}}, R_{e_k}] ... ]]] applied to state.

    Implemented as a sum over signed words: represent the nested bracket as a
    formal linear combination of words in the e_i, built recursively.
    """
    words = _nested_words(list(es))
    out = {}
    for sgn, w in words:
        for mu, v in apply_word(state, w, L).items():
            out[mu] = sp.expand(out.get(mu, 0) + sgn * v)
    return {k: v for k, v in out.items() if sp.expand(v) != 0}

def _nested_words(es):
    """signed word expansion of the right-nested bracket [e1,[e2,[...,ek]]]."""
    if len(es) == 1:
        return [(1, (es[0],))]
    inner = _nested_words(es[1:])
    a = es[0]
    out = []
    for sgn, w in inner:
        out.append((sgn, (a,) + w))        # R_a * inner
        out.append((-sgn, w + (a,)))       # - inner * R_a
    return out

def C(es, lam, L):
    """entries of the nested bracket applied to |lam>."""
    return nested(es, {tuple(trim(lam)): sp.Integer(1)}, L)
