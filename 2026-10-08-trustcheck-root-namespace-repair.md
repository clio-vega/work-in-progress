# The `--root` namespace collision in `trustcheck.py`, repaired — 2026-10-08 (PEER REVIEW c1)

**Status: FIXED on disk. The fixed file is `projects/code/clio.json`, which is tracked by NO
repository** — so this note is the only readable record of it. Flagging per the 10-08 WAKE
finding that four artifacts existed only where nobody could read them.

## The fault

`trustcheck.py` resolves two different kinds of path against the single `--root`:

- source `read` paths inside `sources.json` are relative to `memory/`;
- peer `registry_dir` / `artifact_root` / `sources_path` in the deployment descriptor were
  relative strings, resolved by `Dep._resolve` against `--root`.

So one `--root` could not serve both namespaces. Measured, before the fix, on
`proofs/registry/two-part-green-polynomials.json`:

| invocation | exit | what fails |
|---|---|---|
| `--root .` | 1 | every source `read` path (`reading/…` sought under the project root) |
| `--root memory` | 1 | `registry 'rick/hikita-star-dominance-support' not found at memory/peers/rick/registry/…` |

The file is at `projects/peers/rick/registry/hikita-star-dominance-support.json` and always was.
Whichever root you pick, the bulk of the problems is phantom in the namespace that root is not
serving — which is how this survived: **both arms look broken, so neither reading is trusted.**

## The repair

`Dep._resolve` already calls `os.path.expanduser`. So making the six peer-interface paths
`~`-anchored decouples them from `--root` entirely, without touching `trustcheck.py`:

```json
"interfaces": {
  "rick":    { "registry_dir": "~/projects/peers/rick/registry",    "artifact_root": "~/projects/peers/rick/artifacts",    "sources_path": "~/projects/peers/rick/sources.json" },
  "macbeth": { "registry_dir": "~/projects/peers/macbeth/registry", "artifact_root": "~/projects/peers/macbeth/artifacts", "sources_path": "~/projects/peers/macbeth/sources.json" }
}
```

After (same registry file, same command):

| invocation | exit | reading |
|---|---|---|
| `--root memory … validate --files-dir .` | **0** | `OK … (status: computed, deployment: clio)` |
| planted control: `registry_dir` → `…/NO-SUCH-DIR` | 1 | `1 problem(s)`, naming the bad path |
| `--root memory --sources <abs> … sources` | 0 | `OK (**781 sources**)` — a cardinality, not a vacuous green |

The planted control matters: a repair that cannot read red is indistinguishable from the fault
it replaced, and a half-applied fix is *less* safe than the fault because the fault was loud.

## Still open, for Robin

1. **`scripts/boot-prompt.md` and `PROTOCOL.md` are bind-mounted read-only.** The
   `--files-dir .` correction (not `proofs`, which double-prefixes and fails every node) has now
   been rediscovered in three separate cycles because the one phase that needs it — WAKE — cannot
   edit its own prompt. Named ask: in `scripts/boot-prompt.md`, replace `--files-dir proofs` with
   `--files-dir .`, and the same for `registry_validate.py --proofs-dir`.
2. **The two validators disagree about two enums, and neither disagreement is a bug in the file.**
   - `trust: "peer-claimed"` — accepted by `trustcheck.py`, **rejected** by `registry_validate.py`.
   - `extraction: "title-only"` — legal per `clio.json`'s `extraction_chain`, **rejected** by
     `citation_check.py`'s hardcoded `LEVELS` (170 of today's 411 advisory problems are this, and
     226 more are MathOverflow ids failing an arXiv-id regex by design).
   *"Does it validate?"* is not well-posed without naming the tool. Either the enums should be read
   from one place, or every grade sentence has to name its validator.
3. **`code/clio.json` is in no repo.** Neither is `code/citation_check.py` or `code/trustcheck.py`.
   The trust system's own configuration is the least readable thing I own.
