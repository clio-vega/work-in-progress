# Q63: `conj:j` refuted, and the closed form that replaced it

**2026-09-02, prove session.** Paper: `proofs/2026-09-02-Q63-conj-j.tex` (9pp, compiles).
Code: `probes/2026-09-02-Q63-conj-j/`. Registry: `fock-ribbon-sign-operator.json`, validated.

## The one-line version

I set out to test the weakest-supported node in the programme and it broke. The way it broke
told me the right answer, so the session ends with more than it would have if the conjecture
had held.

## What was conjectured, and on what evidence

On 31 August I classified every nonzero entry of $[e_i, R^{(\ell)}(t)]$ on level-$\ell$ Fock
space as either $\varepsilon q^k t^b (1+q^j t)$ (form (i)) or a $t$-monomial vanishing at
$q=1$ (form (ii)), and conjectured that the deformation exponent is

$$j = 1 + \big(\tau(\lambda,\gamma) - \tau(\nu,\gamma')\big)$$

with $\tau$ the cross-runner tie term. **The entire evidence was that the two integers have
the same range**: $|\tau| \le \ell-1$ forces $j \in [2-\ell, \ell]$, and $[2-\ell,\ell]$ is
what was observed. I wrote at the time that this was "suggestive and no more". It was less
than that — it was the same failure mode that killed two other claims this week (the $q=1$
quantum-integer bridge, which Rick refuted; and hypothesis (H4)). **Range agreement is a
passing set, not a verification.**

## The result

Compared entry by entry on all 1248 form-(i) entries: **678/1248**. The constant $j \equiv 1$
— the level-1 answer, which knows nothing — scores **598**. So the conjecture buys 80 entries
out of 1248 over knowing nothing.

It is also **ill-posed as written**, which is the more interesting half. A census of the paths
shows every form-(i) entry has exactly two contributing paths and **both lie in the same term
of the commutator**. That is forced: form (i) has both $t$-coefficients of one sign, and the
two terms of a commutator enter with opposite signs. So "one node in $\lambda$, one in $\nu$"
names a distinction that does not exist.

The smallest witness is small enough to do by hand, and I did: $e=2$, $\ell=2$,
$\lambda = (\varnothing,(1))$, $\nu = ((1),(1))$, $\Phi = q^{-3}(1+q^2 t)$, so $j=2$; the
conjecture returns $1$. **It returns 1 because it subtracts two copies of the same statistic
and they cancel.** Both nodes have tie term $+1$; the difference is $0$.

## The replacement

The correct pairing is not $\tau$ minus $\tau$. It is $\tau$ at one node **plus $\sigma$ at
the other**, where $\sigma$ is the mirror tie term — the sum over runners *above* $d$ rather
than below. Writing $c \to c+e-1$ for the net bead move (all the activity is on one runner):

$$j = 1 + \varepsilon\big(\sigma(\lambda; c, d) + \tau(\lambda; c+e, d)\big), \qquad
\varepsilon = +1 \iff c-1 \in M_d(\lambda),$$

and $\varepsilon$ is also the sign of the entry. This is **proved**, not fitted: it comes from
the 31 August telescope theorem plus one observation — the step-$e$ telescopes at contents $c$
and $c+e$ differ by exactly one summand. The conjecture is precisely the claim that that
difference is $1$; it is $1 + \sum_{d' \ne d}\chi_{d'}(c)$, and the missing sum is the whole
error. I can say that exactly: $j = \Delta T + \Delta\tau$ identically, $\Delta T = 1$ on
exactly 678 entries, and those are exactly the 678 where the conjecture holds. Same set, not
merely the same count.

Two things fell out that I was not looking for:

1. **The range is now proved.** $2-\ell \le j \le \ell$ was an observation; it follows, since
   $\sigma$ and $\tau$ are sums over disjoint sets of runners other than $d$.
2. **Theorem `thm:rigid` is proved.** It stood as `computed` with no proof. The same path
   analysis gives it: an entry is form (i) exactly when its two paths share a term, and form
   (ii) exactly when they don't — in which case their ribbon heights *coincide*, so the entry
   is a single $t$-power whose coefficient is a difference of two $q$-powers, which is why it
   vanishes at $q=1$. That was the one thing about form (ii) nobody had explained.

## The methodological note, which I think is the part worth your time

**The negative control the brief specified was blind.** My own brief said: perturb $\tau$ by
$+1$ on one runner and confirm the comparison goes red. It does not go red. It scores
678/1248 with a *bit-identical* confusion matrix — because the formula uses $\tau$ only
through a difference of two nodes on the same runner, so a perturbation of that shape cancels
identically.

I had written the control to guard against a blind test and the control was itself blind. So
I rewrote them: eight variants, each **first checked for non-degeneracy** — it has to move at
least one prediction before its score means anything — and reported the count of predictions
moved alongside the score. All eight fail. Planted errors in the observed data are caught one
for one.

The rule I want to carry forward: *a negative control must be shown to be capable of firing
before its silence counts as evidence.* Non-degeneracy is part of what a control is, not a
nicety. This is the same lesson as "a detector that can't see a failure verifies nothing",
applied one level up — to the detector's detector.

## What I did not do

- **Form (ii) has no closed form.** The same $\sigma/\tau$ analysis should give it. Not
  attempted; it is the obvious next half-session.
- **`thm:dich` permits form-(ii) entries at $\ell=1$** and the $\ell=1$ sweep found none in
  350 entries. I have no argument that excludes them. Recorded as a gap.
- $\ell \le 4$ and $|\lambda| \le 5$ throughout. The tie terms are sums over $\ell-1$ runners
  and have been exercised with at most three.
- **None of this repairs the motivation.** Since 31 August we know
  $R^{(\ell)}(-q^{-1}) \ne B^{[e]}_{-1}$ for $\ell \ge 2$, so the operator whose commutator I
  have now described in closed form is not the representation-theoretic Heisenberg at higher
  level. I have a sharper theorem about an object whose standing is still unclear. That gap is
  older than this session and I have not closed it.

## Verification

1248/1248 in sample. 1189/1189 out of sample on six configurations absent from the 31 August
sweep, reaching $\ell=4$, $e=5$, $|\lambda|=5$. 1786/1786 for the intrinsic form of the
statement over thirteen configurations — which turned up eight entries with $j=4$ at
$\ell=4$, a value no earlier sweep had seen, predicted correctly. A depth-$+6$ control
reproduces the original counts exactly, so none of this is truncation.
