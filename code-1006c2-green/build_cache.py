import sys, time, hl
for n in range(1, int(sys.argv[1]) + 1):
    t0 = time.time(); hl.HL_P_cached(n)
    print(f'n={n} built in {time.time()-t0:.1f}s', flush=True)
