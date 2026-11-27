"""REVIEW 2026-11-27 item 2: recount the 11-24 c2 mirror-lesion census (g12fresh mirror, n<=4: 12354 labellings, 582 lift)
by chirality class, and test the DREAM 11-26 explanation: a labelling lifts iff no label-2 ('10') edge is shared by a
KT triangle and a mirror triangle (a 'chirality interface')."""
import sys
from collections import Counter
sys.path.insert(0, '/home/clio/projects/proofs/code-1112c2-Q585')
import mosaic as MZ
KT = set(MZ.OK); MIR = set()
for r in range(3):
    t = (2, 1, 0); MIR.add(t[r:] + t[:r])
MZ.OK |= MIR
def tri_kind(n, lab, t):
    ls = tuple(lab[MZ.E(t[i], t[(i + 1) % 3])] for i in range(3))
    if 2 not in ls: return None
    return 'KT' if ls in KT else 'mirror'
def classify(n, lab):
    owner = {}; kinds = set(); iface10 = 0; iface_any = 0
    for t in MZ.tri_cells(n):
        k = tri_kind(n, lab, t)
        if k: kinds.add(k)
        for i in range(3):
            owner.setdefault(MZ.E(t[i], t[(i + 1) % 3]), []).append(k)
    for e, ks in owner.items():
        if len(ks) == 2 and set(ks) == {'KT', 'mirror'}:
            iface_any += 1; iface10 += lab[e] == 2
    cls = 'none' if not kinds else (next(iter(kinds)) if len(kinds) == 1 else 'mixed')
    return cls, iface10, iface_any
st = Counter()
for n in range(1, int(sys.argv[1]) + 1):
    for lab in MZ.puzzles(n, {}):
        try: MZ.build_mosaic(n, lab); lifts = True
        except AssertionError: lifts = False
        cls, i10, ia = classify(n, lab)
        st[('total',)] += 1; st[('lifts', lifts)] += 1
        st[(cls, 'lifts' if lifts else 'fails')] += 1
        if cls == 'mixed':
            st[('mixed', 'lifts' if lifts else 'fails', '10-interface present', i10 > 0)] += 1
for k in sorted(st, key=str): print(st[k], k)
