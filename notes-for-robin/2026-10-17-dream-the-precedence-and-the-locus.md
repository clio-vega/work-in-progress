# For Robin — a precedence threat I lost for ten hours, and the frame it fixed

**DREAM 2026-10-17.** Two things, one of them operational and one of them mathematical, and they
are the same thing seen twice.

## 1. A browse session reported its findings and never filed them

BROWSE ran 02:15→02:41 today. It created its pre-write backup at 02:19, then died
(`Background tasks still running after 600s; terminating.` / its own last words: `One agent
left.`). Its findings went out as its **final message** — into `clio.log`, which no protocol of
mine reads by content. For ten hours its output existed in exactly one place nothing looks at.

**In `memory/`, an unfiled session and a session that never ran are identical.** I found it only
because the orphaned backup is a tell: *the backup proves intent, the modified target proves
completion.* The check is one command —

```
comm -23  <dates with sources.json.bak-*browse*-pre>  <dates with reading/2026-*-browse*.md>
```

— and over all of October the difference is **exactly `1017`**. Zero false positives in 17 days.
I have put it in `topics/methodological-principles.md` and I will run it at every wake.

**Two things you may want to fix at the generator, not the instance:**

- The browse protocol should write its reading log **before** it dispatches its last agents, or at
  minimum write a stub it appends to. Right now the write is the last step and it is the step that
  gets killed.
- **`for-robin/` exists at two paths.** The LEAN skill writes to `/home/clio/projects/for-robin/`
  (8 notes, 2026-08-31 → today); PROVE/REVIEW/DREAM write to
  `/home/clio/projects/memory/for-robin/` (10 notes). It is not even consistent within LEAN. A
  dream cycle that inventories the canonical path silently loses the other eight. I have not moved
  any files — that is a path fix in the skill.

The cost today was not hypothetical. **Rick's S1 novelty objection, which I answered at 09:59, and
the concrete precedence threat below, found at 02:41, are the same objection raised seven hours
apart by two of my own sessions, and neither could see the other.** I answered the weaker one.

## 2. The precedence threat — and why it is good news

**Digalaki (MIT, with Wheeler), "Structure Constants for Free-Fermion Six Vertex Model Symmetric
Functions", in preparation.** Mittag-Leffler July 2026 programme. `F_κ G_{λ/μ} = Σ C^ν F_ν`, with
the structure constants *"realized as partition functions of an integrable lattice region — a
**puzzle**"*, proved by evaluating an auxiliary cubic configuration two ways.

⚠ **Provenance: `agent-summary`, from a programme page, no arXiv ID, not deep-read.** I am not
treating it as established; I am treating it as a reason to stop writing novelty sentences until I
have read it. Wheeler is a seed author and the method overlaps Q484/Q491/Q492 closely.

**Here is the part worth your time.** Their hypothesis is the **free-fermion locus**. My own
conjecture — from the 10-16 c2 dream, before I knew their paper existed — was that combinatorial
interpretations exist exactly on the locus where my multiplier `ρ` equals 1, i.e. where the
**charge is conserved**. *Those are the same locus under two names.* They have the theorem because
they had the standard name for the thing; my keyword was fresh precisely because it is nobody's
word for it.

So the **positive** half of my conjecture is (probably) already somebody's theorem — which means
the **negative** half is clean and mine: *off that locus, the non-Laurent structure constants are
Pfaffian-category objects that no tiling can count.* Q491's measured criterion
(`Laurent ⟺ |ν| − max(|λ|,|μ|) ≤ 1`, **225/225**, no false positives or negatives) is the data for
it.

## 3. And the frame was wrong in a way three sources fixed in one day

I spent 10-14 → 10-16 trying to make the obstruction a property of **type C**. That is false:

- **Weigandt–Hamaker, *Symplectic Bumpless Pipe Dreams*** (same venue, talk title,
  `agent-summary`) gives a **tiling** for `Sp_2n`-orbit-closure K-classes. Some type-C objects are
  tileable.
- **This morning's PROVE (proved, after retracting my own 48/48 from yesterday)**: type reaches my
  multiplier **only** through the integer `h` = length of the boundary root.
  `ρ^X = (1−q)²/((1−qw_a^h)(1−qw_b^h))`.
- **Bump's Stanford 263C Lect. 20**: type-C ice as **U-turn** models closed by **cap** vertices
  "whose Boltzmann weights must be specified", and *"changing just the cap weights results in
  another interesting model."*

⇒ **The cap weight is the coordinate; `ρ` is the function on it; `ρ=1` is the tileable locus.**
Full statement with gates: `connections/2026-10-17-dream-the-cap-weight-is-the-coordinate.md`,
`topics/the-tileable-locus.md`. Falsifier pre-registered as **Q505**: if the symplectic BPD model
sits **off** `ρ=1`, a tiling exists where my conjecture forbids one and the frame dies. I expect
it on the locus, which is historically when I have been wrong.

Bump also records something you might enjoy: *"finding a Tokuyama formula for orthogonal groups is
an open problem."* That is the `h=1` side of my own identity.
