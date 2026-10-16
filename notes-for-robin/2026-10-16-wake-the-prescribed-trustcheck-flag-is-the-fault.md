# The prescribed `trustcheck` flag is the fault, and its exit code is not a verdict

**2026-10-16 WAKE.** Reported, not patched — `code/` is yours and the boot prompt is read-only.

## 1. The flag in my wake instructions double-prefixes

My wake instructions prescribe, verbatim:

```
python3 code/trustcheck.py --deployment code/clio.json --sources skip --chunks-dir skip \
    validate proofs/registry/<name>.json --files-dir proofs
```

Run from `projects/`, that form **double-prefixes every node**: the registry's `file` fields
already carry `proofs/`, so `--files-dir proofs` looks for `proofs/proofs/…`. It printed
**13 false "not found" problems** against
`proofs/registry/motegi-typeBC-multiplication.json`, whose single target
`proofs/2026-10-15-Q484-motegi-puzzle-Gm.tex` exists at 30,969 B.

The correct form is **`--files-dir .`**, run from `projects/`:

```
OK: proofs/registry/motegi-typeBC-multiplication.json is valid (status: proved, deployment: clio)
```

This is the same shape as `registry_validate.py`'s `--proofs-dir` (whose *flagless default* is the
wrong one) and as `--files-dir registry`. **There is no wrong flag to omit — the prescribed form is
wrong**, which means following the instruction is reproducing the fault, and it renews every
session. I have hit this class eleven times now and this is the first time the *prescription itself*
was the carrier for `trustcheck`.

## 2. The sharper half: `rc=0` on BOTH runs

The 13-problem run and the clean run **both exited 0**. The exit status was identical for a registry
reported broken and the same registry reported valid. So the only verdict this tool emits is the
`OK:` line, and anything that keys off `$?` — a hook, a loop guard, a pre-push check — will read a
13-problem registry as healthy.

That matters more than the flag, because the flag is a thing I can remember and the exit code is a
thing I would *delegate to*.

## 3. What I would want

Either `--files-dir` defaulting to `.` (so the prescribed and correct forms coincide), or a nonzero
exit when `problem(s)` is printed. The second is the one that protects anything automated.

Both are one-line changes in your tree, and I have not made either.
