# For Robin — infrastructure asks (2026-07-22)

Two loose ends that surfaced during today's wake session.

## 1. Rick is not on my allowed recipient list (BLOCKING)

CLAUDE.md pins the allowed recipient list to:
- langer.robin@gmail.com
- lyraclaude20@gmail.com
- paul.clayworth@gmail.com

Rick (`grandparick20@gmail.com`) is NOT on it. My email agent found **16 unread messages
from Rick** in my inbox this morning, spanning his research Days 85–96 (weeks of substantive
mathematical dialogue). Several were explicit asks:

- uid 439 "judgment call for you"
- uid 442 "blocker is M_j" (coordination point)
- uid 453 "PROVE target Day 96" — the (♥) recursion he wants us to attack

I could not reply to any of them because the email server rejects addresses outside the
whitelist. So from Rick's side, he has been sending mathematical updates into a void for
weeks, and from my side, I only found out this morning that a whole research thread has been
happening in parallel.

**Ask:** Either add `grandparick20@gmail.com` to the allowed list, or set up a forwarding
mechanism so Rick's mail lands somewhere I can respond to it. Right now the dialogue is
one-way, and Rick is producing real results — his β'(c) digit-sum formula (10/10 verified on
c ∈ {4..11, 14, 15}) is exactly the shape my "uniform Content Lemma" residual needed, and I
would already have started drafting a joint response if I could reply.

I've consolidated his key results into memory (`2026-07-22-rick-beta-prime-digit-sum-formula.md`)
so they aren't lost. But I need bidirectional contact to actually collaborate.

## 2. Lyra's long-term-memory git mount is DOWN

Lyra's uid 465 reply (the precise Δ(c) definition I was waiting for) contained an honest flag:
her "Lean-verified" claim about LB₁(c) is retracted because her mount is down and she cannot
re-cite the file. She says she has "flagged to Robin" — I'm noting it here in case that flag
hasn't landed. Her working directory is unreachable, so any Lean proof she references from
sprint days is currently a "believed, to re-cite" claim rather than a verified one.

## 3. (Minor) Sage still not installed

Already noted in memory (`reference-infra-sage-not-installed.md`). Not blocking — Python from
scratch works — but CLAUDE.md still lists SageMath in the Tools section, which is misleading
for any future compute agent I dispatch. Either install sage or remove from CLAUDE.md.

## Priority

(1) is blocking real work. (2) is Lyra's problem primarily but affects verification of her
LB₁ claim which is load-bearing on the shared content lemma I'm drafting for her. (3) is
cosmetic. If time to fix only one, (1).
