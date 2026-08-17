# Optimal closure strategy after the decoder and mutation audits

**Date:** 2026-08-17. All logarithms are base two.

## Executive verdict

The rigorous window for Erdos 838 is still

\[
 {1\over4}\leq\liminf {\log f(n)\over(\log n)^2}
 \leq\limsup {\log f(n)\over(\log n)^2}\leq {1\over2}.
\]

The last round of work substantially improved the obstruction map but did
not improve either endpoint.  Its most important strategic consequence is
that the problem should no longer be described as a generic decoder
problem.  Once a compatible mixed reservoir is present, weighted Hall
allocation, label replacement, and global bounded-overlap assembly work on
the main stress families.  The unresolved step is the **production of that
reservoir in an arbitrary low-face configuration**.

There are only two coefficient-bearing exits left.  The primary route is a
direct fixed-rank or positive-rank-interval gain.  The secondary route is a
common-core conversion or mutation theorem genuinely conditioned on a
strict sub-half deficit.  Every
other current target is a construction-class theorem, a barrier, or a
reformulation at essentially full difficulty.

## 1. What the new integration settles

### 1.1 Capacity and global reuse are not the main gap

The pooled decoder results prove the following division of labour.

1. Literal histories below the quarter-log boundary can be jointly assigned
   to one ordinary rank bank with load and recovery fibre one.
2. Matching-star and coherent-root extremals which defeat natural local
   two-tangent maps can be repaired by pooled rank-four/rank-five or mixed
   label-replacing codes.
3. If a local compatible reservoir has Hall expansion, superposing its local
   codes costs only the actual rank/trace incidence.

Thus another abstract max-flow, Cauchy, or history-tag argument is not a
new route.  The missing statement must first force ordinary outputs with the
right physical compatibility.

### 1.2 The high-rank pocket lift reaches a genuine wall

The induced-subset double count supplies, outside any
\(n/\operatorname{polylog}n\) pocket, a rank-\((1-o(1))\log n\)
source bank with enough product surplus to close the fixed gap.  A common
exposed source edge costs only a polynomial factor.  Almost every
source--pocket pair is therefore bad and carries many disjoint crossing
circuits.

The exact deletion theorem then gives a sharp dichotomy.  Low circuit
transversal number produces an ordinary mixed face with its true deletion
load.  High transversal number produces \(\Omega(\log\log n)\) disjoint
circuits, and a small fixed physical matching can be localized while
retaining quasipolynomial record mass.  What it does **not** produce is the
needed \(2^{\Theta((\log n)\log\log n)}\) one-face bank.  Detached toggles
have only \(2^{O(\log\log n)}\) capacity, while describing the varying
source history costs exactly the available surplus.

This is a real wall, not loose bookkeeping.  The anti-aligned two-cloud
configuration realizes the local failure; its Boolean internal banks show
what a global low-face theorem would have to charge.

### 1.3 A fixed strict gap now forces a linear common-circuit core

The pocket ledger becomes substantially sharper when its scale is allowed
to be a fixed power of the parent. Assume
\(\log V(P)\le(1/2-\delta+o(1))L^2\), take a pocket of size
\(n^{1-\delta^2}\), and use only the established quarter lower bound
inside that pocket. A rank-\((1/2-o(1))L\) source bank in the complement
gives a Cartesian rectangle larger than \(V(P)\) by

\[
 2^{(\eta_\delta-o(1))L^2},\qquad
 \eta_\delta=\delta-\delta^2/2+\delta^4/4>0.
\]

The exact deletion theorem and literal circuit pigeonholing then produce a
subrectangle of size at least
\(V(P)2^{(\eta_\delta/2-o(1))L^2}\) sharing
\(\Omega_\delta(L)\) fixed, vertex-disjoint crossing four-circuits. Both
row and column families remain quadratically large. Their continuation
labels have only \(O_\delta(L)^2\) visible-interval types relative to the
common core, but traces in those intervals are not automatically
recombinable.

This is the first scale-matched strict-deficit reduction: quadratic mass is
paired with a linear physical circuit core, rather than quasipolynomial mass
with only \(\Theta(\log\log n)\) circuits. It still does not close. The
fixed matching need not be a transversal of the residual bad circuits, and
deleting it can expose fresh bad circuits on private continuation labels.
See
`agent_common_shield_mixing/STRICT_SUBHALF_LINEAR_POCKET_CIRCUIT_CORE_GATE.md`.

The bounded repair audit gives a sharp correction. In the exact global
nine-point minimizer there are complete fixed-circuit rectangles for which
no subset of the common circuit labels releases every record. The smallest
has \(2\times8\) records. Deleting the entire circuit releases \(15/16\),
but one private-continuation circuit survives. Across all \(10{,}800\) such
rectangles, \(1{,}569\) have no universal common-label deletion.

The exact positive replacement is a deletion cascade. After deleting the
current common core, released records inject into ordinary faces; if most
records remain bad, one fixes a fresh residual four-circuit at cost at most
\(\binom n4\) and repeats. For row and column ranks \(r,h\), this gives only

\[
 |\mathcal A||\mathcal H|
 \le2V(P)\left(2\binom n4\right)^{\min(r-c_Y,h-c_X)},
\]

which is quadratically expensive at live ranks. Thus the literal
common-transversal version of the secondary route is closed. The surviving
strict-deficit target is specifically a **positive-mass release theorem**
or a sub-\(n^4\) amortized charge for the residual cascade. See
`agent_common_shield_mixing/COMMON_CIRCUIT_DELETION_CASCADE_AND_MINIMIZER_GATE.md`.

### 1.4 Fixed-block mutation is narrower, not dead

The exact three-block audit has two logically different conclusions.

- An unconditioned rule saying that every nonminimal configuration has a
  decreasing fixed-\(q\) ordered-block mutation is false.
- The saved cyclic and coordinate-annealed controls are above the
  coefficient-one-half scale.  They do not refute the stronger statement
  that a *strict sub-half* configuration must admit such a mutation.

The conditional version remains possible, but it currently has neither a
sub-half witness nor a selection theorem.  It is therefore a secondary
hope rather than the active plan.

### 1.5 The weighted recursive-construction lane is fenced but unfinished

Hinged Kraft closes finite grammars and broad balanced or polynomially
imbalanced heterogeneous recursions at coefficient one half.  The exact
weighted-hinge conjecture is false, while the square-mesh variant survives
all current tests.  Even a proof of the local square statement would still
need a global bound on accumulated square losses along near-star paths.
This is worth preserving as construction-side work, but it is not presently
the shortest route to an unconditional lower gain.

## 2. Primary route: a direct positive rank interval

At \(N=4^k\), the clean target is

\[
 v_k(P)\geq 2^{(1+\eta-o(1))k^2}
\]

for one fixed \(\eta>0\).  This immediately raises the unrestricted lower
coefficient to \((1+\eta)/4\).

An equivalent sufficient target with more room is the averaged density
decay inequality

\[
 \log {p_r\over p_k}
 \leq {c\over2}(k^2-r^2)+o(k^2),
 \qquad r=\alpha k,\qquad c<2,
\]

where \(p_j=v_j/\binom Nj\).  Any fixed saving below the ordinary decay
constant two gives a strict coefficient improvement.

This route is parked until a genuinely new theorem already averages a
positive fraction of the ranks.  The following do not qualify:

- a single positive-fraction transversal box;
- a one-layer extension inequality;
- scalar hull identities or all-restriction rank moments;
- total endpoint mass without graded extraction;
- another bounded-rank history code below the already solved range.

The right new input would have to use planar circuit compatibility across
many ranks, or produce the rank-\(k\) bank directly.

## 3. Secondary route: strict-deficit selected mutation

A legitimate weaker target than the full half theorem is to fix one
\(\delta>0\) and prove:

> Every sufficiently large configuration satisfying
> \(V(P)<2^{(1/2-\delta)(\log n)^2}\) admits a physical mutation which
> strictly decreases \(V\).

Applied to a global minimizer, this would contradict the assumed strict
sub-half bound.  Ordered three-block mutation is one candidate family, but
the theorem must be conditioned on the deficit; no unconditioned selector
survives the exact controls.

The linear-pocket theorem now supplies the conditioning structure for free.
It is enough to handle a bad face-family rectangle with quadratic excess,
two quadratically large sides, and a literal linear disjoint-circuit core.
A positive-mass release after deleting the common core would give an
injective mixed-face map immediately. A universal common deletion is false
even in the exact nine-point minimizer, so the statement must be
quantitative. Failing that, a valid mutation must use the residual
crossing-circuit cascade; moving or toggling only the fixed core cannot work
because the core itself has only \(2^{O(L)}\) subfaces.

A promotion of this route needs one of the following concrete inputs:

1. a deficit-to-release theorem forcing a
   \(2^{-o((\log n)^2)}\) released fraction after common-core deletion;
2. a nonincreasing multi-chart/circuit mutation retaining both physical
   anchors; or
3. a proof that fixed-block stability itself creates a mixed reservoir with
   a fixed exponent gain.

Merely averaging the mutation inequalities returns the known Gibbs kernel
and is not progress.

## 4. Stop rules

1. Do not reopen the fixed-rank route with a third local or threshold
   surrogate.  Reopen only with a statement already averaged over
   \(\Theta(k)\) ranks or with a direct rank-\(k\) bank.
2. Do not open another decoder branch unless it creates ordinary compatible
   outputs.  Capacity and global overlap without compatibility are solved or
   known insufficient.
3. Do not claim the conditional mutation route is killed by an above-half
   stable family.  Conversely, do not promote it without a strict-sub-half
   implication and kill condition.
4. Any new reduction which is coefficient-equivalent to Erdos 838 is to be
   marked **EQUIVALENT** and parked immediately.
5. Construction-side searches must target either an actual sub-half
   scalable configuration or a theorem closing a named surviving class;
   finite square-mesh evidence alone is not a coefficient gain.

## 5. Progress bar and next action

The obstruction/architecture map is approximately **91%** complete.  The
conservative completed-proof estimate is approximately **46%**.  The
rigorous coefficient bar has not moved from \([1/4,1/2]\).

The bounded literal repair attempt is complete: universal common deletion
is false, and the exact residual cascade has full quadratic cost. The only
secondary continuation worth one further bounded attack is a
strict-deficit **positive-mass** release or decreasing-mutation theorem. If
that reduces to unrestricted two-sided profile composition or merely pays
\(n^4\) per fresh circuit, park the secondary route. The primary admissible
route remains a theorem already averaged over a positive rank interval.
