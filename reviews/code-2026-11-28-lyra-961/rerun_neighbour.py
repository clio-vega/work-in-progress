"""Rerun Lyra's ee7a961 theta-neighbour null with her code unchanged.
(i) Are the Q=5 and Q=80 wealth paths identical?  (Q enters only the unused stratum label.)
(ii) Type-I with Ville applied at every item (her rule) vs only at block ends (t = 20k-1),
     where the pair-level product argument licenses the supermartingale property."""
import sys, json, numpy as np
sys.path.insert(0, '/tmp/lyra-wip/code/evalue')
from dgp import null_dgp, alt_dgp
from run_qsweep import method_A_Q
R, N, SEED, THR = int(sys.argv[1]), 2000, 42, 20.0
out = {}
for name, dgp, seed in [('null', null_dgp, SEED), ('alt010', lambda n, r: alt_dgp(n, 0.10, r), SEED + 2)]:
    rng5, rng80 = np.random.default_rng(seed), np.random.default_rng(seed)
    same = 0; rej_all = rej_blk = 0; maxgap = 0.0
    for r in range(R):
        d5 = dgp(N, rng5); d80 = dgp(N, rng80)
        M5 = method_A_Q(d5, rng5, Q=5, pairing='theta_neighbour')['M_mix']
        M80 = method_A_Q(d80, rng80, Q=80, pairing='theta_neighbour')['M_mix']
        same += np.array_equal(M5, M80)
        rej_all += (M5 >= THR).any(); rej_blk += (M5[19::20] >= THR).any()
    out[name] = dict(R=R, identical_paths_Q5_Q80=int(same), reject_every_item=rej_all / R, reject_block_ends=rej_blk / R)
    print(name, out[name], flush=True)
json.dump(out, open(f'rerun_neighbour_R{R}.json', 'w'), indent=2)
