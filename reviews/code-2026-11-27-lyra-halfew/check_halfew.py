"""Independent checks on Lyra's half-EW out-of-sample delivery (b41109a).
Imports her generator/builder unchanged; recomputes per-seed quantities the JSON
does not store: shortfall vs per-seed best WINDOW, clamp hits, E[X_s] by stratum,
and the one-parameter-family sign identity sign(MW-HE) = sign(HE-EW)."""
import sys, json, time
import numpy as np
EV = '/tmp/lyra-rev/wip/code/evalue'
sys.path.insert(0, EV)
import importlib.util
spec = importlib.util.spec_from_file_location('halfew', sys.argv[1])
H = importlib.util.module_from_spec(spec); spec.loader.exec_module(H)
from dgp import null_dgp

R = int(sys.argv[2]); cells = [('REV', g) for g in (0.04, 0.10, 0.30)] + [('TP', g) for g in (0.04, 0.10)] + [('NULL', 0.0)]
out = {}
for name, g in cells:
    t0 = time.time()
    rows = []; Xsum = np.zeros(H.Q); nblk = 0; clamp = 0; zero = 0
    for r in range(R):
        rng = np.random.default_rng(H.SEED_BASE + r)
        if name == 'NULL': data = null_dgp(H.N, rng)
        elif name == 'REV': data = H.reversed_dgp(H.N, g, rng)
        else: data = H.twopeak_dgp(H.N, g, rng)
        X, b = H.build_increment_stream(data, rng, **H.BUILD_KW)
        Xsum += X.sum(0); nblk += X.shape[0]
        ew = H.ew_wealth(X, b); mw = H.mixwin_wealth(X, b); he = H.halfew_wealth(X, b)
        wins = np.array([H.wealth_path(X, w) for w in H.window_experts(b)])
        for p in [ew, mw, he, *wins]:
            if p[-1] < 1e-300: clamp += 1
            if p[-1] == 0: zero += 1
        L = lambda p: float(np.log(max(p[-1], 1e-300)))
        rows.append((L(ew), L(mw), L(he), [L(p) for p in wins]))
    ew = np.array([x[0] for x in rows]); mw = np.array([x[1] for x in rows]); he = np.array([x[2] for x in rows])
    win = np.array([x[3] for x in rows]); best = win.max(1)
    fixed = int(np.argmax(win.mean(0)))  # best window by mean growth over seeds
    s1 = np.sign(np.round(mw - he, 12)); s2 = np.sign(np.round(he - ew, 12))
    out[f'{name}{g}'] = dict(
        mean_ew=ew.mean(), mean_he=he.mean(), mean_mw=mw.mean(),
        he_minus_ew_min=float((he - ew).min()),
        he_minus_bestwin_min=float((he - best).min()),
        frac_he_below_bestwin_minus_log2=float(np.mean(he - best < -np.log(2))),
        he_minus_fixedwin_min=float((he - win[:, fixed]).min()), fixedwin=fixed,
        mw_minus_bestexpert_min=float((mw - np.maximum(best, ew)).min()),
        sign_identity_holds=float(np.mean(s1 == s2)),
        cliff_mw_vs_he=float(np.mean(mw > he) - np.mean(mw < he)),
        cliff_he_vs_ew=float(np.mean(he > ew) - np.mean(he < ew)),
        clamp_hits=clamp, zero_wealth=zero,
        EX_by_s=list(np.round(Xsum / nblk, 5)), secs=round(time.time() - t0, 1))
    print(name, g, json.dumps(out[f'{name}{g}']), flush=True)
json.dump(out, open(f'check_R{R}.json', 'w'), indent=2)
