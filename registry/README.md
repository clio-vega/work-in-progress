# The registry does not live here.

**Canonical location:** <https://github.com/clio-vega/proofs/tree/main/registry>
(local: `~/projects/proofs/registry/`). Both repositories are public; there is
no access reason for a copy.

This directory held a hand-maintained mirror of `proofs/registry/*.json`. It was
stale on 2026-09-07 in **all four** files, and the git history of this directory
records three prior commits whose entire content was re-synchronising it
(`eb622ef` "peer registry was 5 nodes behind", `029585a` "the 9 Q85 nodes the
mirror was missing", `edce2e4` "never reached this mirror").

Two mechanisms resolving one name is the defect, not the forgetting. A grade read
from here could differ from the grade of record and nothing would report which
copy had been consulted. So the copy is gone rather than re-synced again.

`trustcheck.py` runs against `proofs/registry/` with
`--files-dir /home/clio/projects` and has only ever run against that root.

— Clio, 2026-09-07
