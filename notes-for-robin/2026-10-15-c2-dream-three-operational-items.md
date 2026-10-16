# Three operational items — DREAM 2026-10-15 c2

Short note. The mathematics from today is already in
`for-robin/2026-10-15-Q484-motegi-multiplication.md` and
`for-robin/2026-10-15-lean-Q473-order-lemmas.md`. These three are **infrastructure**, and the
first one has a fuse.

## 1. ⏰ FUSE — Rick's refresh token expires in about 3 days and needs an operator `/login`

My own health mail reports it. **If it lapses the PROTOCOL path breaks at the far end** — I can
send, he cannot act. He is currently the most productive edge in my week: overnight he graded my
Q460 `checked-sober` on his own scripts against the printed source, and he was **right twice
against me** (withdrew my "tight" overclaim, and showed a control of mine could not have fired
because `q³+1 = (q+1)(q²−q+1)` and I had enforced the primitive factor, excluding the one point
where the rank collapses). I cannot renew this from inside the container. **This is the only item
here with a deadline.**

## 2. `projects/peers/` is tracked by no git repo, so my registry's peer-evidence paths are private

My registry nodes carry `file:` paths pointing into `projects/peers/`. That directory is in **no
git repo**, so those certificates are readable by **nobody but me** — while Rick's equivalent
sits inside `rick-research` and works. Every citation I make to peer evidence is, from the
outside, an unverifiable assertion.

I did **not** push his PDFs to fix it. They are his documents, and publishing someone else's
correspondence is not my call. What I'd want is either a repo I can push peer *evidence* to (with
his agreement), or a convention that peer-evidence `file:` keys are marked as local-only so they
stop looking like citations.

## 3. `registry_validate.py`'s flagless default is the fault (reported, not patched)

`--proofs-dir` defaults to the registry's **parent** (`proofs/`), while node `file` fields
already carry `proofs/`. So the plain invocation double-prefixes every node and prints **13
false "not found" problems**, 11 of them on nodes predating today. There is **no wrong flag to
omit here — the default is wrong.** The correct form is `--proofs-dir .` run from `projects/`,
which gives `OK`, exit 0.

I did not patch it; `code/` is yours. Flagging it because it is the kind of defect that teaches
future-me to distrust a validator that is actually working — and because the *flagless* form is
the one a skill document would naturally prescribe.

---

## And one thing I got wrong in my own scheduling, for completeness

My WAKE session wrote a peer-review brief at 14:54 for Rick's braided ABS terminality work. But
both of the day's review cycles had **already run** (`LAST_REVIEW` = `2026-10-15:2`,
`REVIEW_ENDED_AT` = 10:18). **Arming a slot does not allocate it.** So his review is unread
through no fault of his, after he paid his side of the exchange overnight. I have made this
mistake seven times now and have written the check down (read `LAST_X` before writing a brief
for slot `X`) — mentioning it only so you know why he may be waiting.
