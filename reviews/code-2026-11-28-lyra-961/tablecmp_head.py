"""Compare every cell of Tables reversed/twopeak in the b41109a PDF tex with results/novel_dgp_halfew_results.json."""
import json, re, subprocess, sys
tex = subprocess.run(['git', '-C', sys.argv[1], 'show', 'HEAD:correspondence/2026-11-26-halfew-out-of-sample.tex'], capture_output=True, text=True).stdout
d = json.load(open(sys.argv[1] + '/results/novel_dgp_halfew_results.json'))
tabs = re.findall(r'\\midrule\n(.*?)\\bottomrule', tex, re.S)[1:]   # skip Table mw-he
cols = ['mean_ew', 'mean_he', 'mean_mw', 'pow_ew', 'pow_he', 'he_cliff', 'he_worst']
bad = 0; tot = 0
for name, tab in zip(['reversed_gradient', 'two_peak'], tabs):
    rows = {r['gamma']: r for r in d[name]}
    for line in [l for l in tab.strip().split('\n') if not l.lstrip().startswith('%')]:
        v = [float(x.replace('$', '').replace('+', '')) for x in line.replace('\\\\', '').split('&')]
        g = v[0]; r = rows[g]
        for c, x in zip(cols, v[1:]):
            tot += 1
            if abs(x - r[c]) > 0.0015:
                bad += 1; print(f'{name[:3]} gamma={g:<5} {c:9} PDF={x:+.3f}  JSON={r[c]:+.4f}')
print(f'mismatched cells: {bad}/{tot}')
