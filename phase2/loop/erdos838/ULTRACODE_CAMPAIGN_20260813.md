# Erdős 838 ultracode campaign: reflection orders, means, and cut kernels

> **Date:** 2026-08-13
> **Status:** campaign complete; unrestricted problem remains open
> **Claim boundary:** the unrestricted problem is not yet solved.

All logarithms are base two.  The rigorous window entering this campaign was

\[
 \frac14\le\liminf\frac{\log f(n)}{(\log n)^2}
 \le\limsup\frac{\log f(n)}{(\log n)^2}\le\frac12.
\]

The upper coefficient `1/2` and its matching lower bound inside the mirrored
decomposable class remain intact.  This campaign attacked the unrestricted
lower bound and, independently, searched for a growing-state upper
construction.

## 1. Exact reflection-order gate

For a stretchable type-A reflection order, let `A(z)` and `B(z)` be the
opposite products of the root transvections `I+zE_(j,i)`.  The exact identity

\[
 Z_P(z)=nz+\langle A(z),B(z)\rangle_F-n
\]

counts convex subsets by size.  The Gate-A agent exhausted every commutation
class through `n=7`; the class counts are

```text
n=3,4,5,6,7: 2, 8, 62, 908, 24698.
```

The exact minimum nonempty traces are

```text
n=2,...,7: 3, 7, 14, 26, 44, 72.
```

Every minimizing class has a rational fixed-`x` realization.  Heuristic
search through `n=20` found no normalized value below `1/2`.  This does not
prove the asymptotic inequality, but it clears the first computational gate
and shows no small nonstretchable loophole.

Artifacts: `agent_reflection_gate/GATE_A_REPORT.md` and
`agent_reflection_gate/reflection_order_gate.py`.

## 2. Mean-size deletion route

Let

\[
 \mu(P)=Z'_P(1)/Z_P(1).
\]

The exact deletion average gives, for a minimizer `P_n`,

\[
 \log f(n)-\log f(n-1)
 \ge-\log\left(1-\frac{\mu(P_n)}n\right).          \tag{1}
\]

Consequently the conjectural estimate

\[
 \mu(P)\ge\log n-O(1)                               \tag{MS}
\]

would prove the full coefficient `1/2`.  The closure-lattice interpretation
is exact: convex-position subsets are the independent sets `ext(K)` in
bijection with closed sets `K`, and `mu` is the uniform average down-degree.
The Boolean interval partition gives

\[
 (1+t)^n=\sum_{K\text{ closed}}
 t^{|ext(K)|}(1+t)^{|K|-|ext(K)|}.                 \tag{2}
\]

The main surviving obstacle is changing from the interior-weighted measure
implicit in (2) to the uniform measure on closed sets.

The attractive quadratic shortcut

\[
 \log V(P)\le(1/2+o(1))\mu(P)^2
\]

is rigorously false.  A balanced single Pascal cell `T_(m,m/2)` has

\[
 \liminf\frac{\log V}{\mu^2/2}
 \ge2-\frac1{2\ln2}=1.278652\ldots.
\]

The correct weaker sufficient target is a minimizer-only dichotomy: either
(MS) holds, or the sharp quadratic inequality holds only in the complementary
low-mean branch.  This still turns (1) into coefficient `1/2`.

The exact mean conjecture survives all reflection classes through `n=7`, all
207986 distinct strong-tree moment states at `n=13`, rational nested cages,
Horton sets through `n=256`, and Pascal cells through `m=256`.  This is
evidence, not a theorem.

Artifacts: `agent_root_trace/MEAN_SIZE_ATTACK.md`,
`agent_mean_lattice/REPORT.md`, and `agent_graded_supersat/REPORT.md`.

## 3. Graded supersaturation gate

For a fixed vertical template of size `r`, with cap/cup increments `p,q`, the
exact graded recurrence gives at `k=(1/2)log|Q_d|`

\[
 \log v_k(Q_d)
 =\left(2-\frac{\log r}{2(p+q)}+o(1)\right)k^2.    \tag{3}
\]

Balanced Pascal templates make the coefficient in (3) tend to `3/2`.
Therefore any proposed local theorem with exponent strictly above `3/2` is
false and fixed-size lifting cannot reach global coefficient `1/2`.  The
sharp `3/2` local conjecture remains live and would yield global coefficient
`3/8`, a meaningful incremental result.

Artifact: `agent_graded_supersat/REPORT.md`.

## 4. Exact contiguous-cut kernel and its obstructions

For a balanced contiguous cut `L|R`, every crossing cup and cap has one cross
edge.  Slope-filtered prefix/suffix factorization gives the exact identity

\[
 X_{L|R}=\sum_{e,f}K_L(e,f)K_R(e,f),               \tag{4}
\]

where `e` and `f` are the lower- and upper-hull bridges.  The same-bridge
diagonal is always trivial:

\[
 K_L(e,e)=K_R(e,e)=1.
\]

Thus a single-bridge reset is impossible; the first exact boundary state is
an ordered *pair* of bridges.

The initially plausible polynomial collision bound is also false.  The exact
integral alternating family

\[
 p_i=(i,(-1)^iM^{n-i})
\]

has, at a balanced cut `n=2m`,

\[
 \frac{X|E|^2}{S_LS_R}\le1024m^2\,2^{-m/2}.       \tag{5}
\]

This is exponentially smaller than every inverse polynomial.  A more elaborate
heterogeneous construction even has subquadratic crossing trace `X` and
collision ratio `N^(-Theta(log log N))`.  However both counterfamilies already
have enormous *internal* convex-subset mass.  They therefore identify the
correct replacement: a **total-count-capped collision dichotomy**, in which
bad alignment is allowed only when the full count `V(P)` is already above the
quasipolynomial target.  Capping the crossing trace `X` alone is false.

Artifacts: `agent_cut_reset/CUT_RESET_REPORT.md` and
`agent_tangent_pruning/TANGENT_PRUNING_REPORT.md`, with the strengthened
counterexample in `agent_capped_collision/CAPPED_COLLISION_REPORT.md`.

**Correction to the conditional arithmetic in the first two cut reports.**
Those notes refer to

```text
log C(I)+log U(I) >= (1/2-o(1)) log^2|I|
```

as a standard arbitrary-order-type product bound.  It is not established in
that generality; it is essentially one of the missing common-direction mass
statements.  The proven asymmetric cap--cup entropy inequality is weaker.
Consequently even a total-`V`-capped collision theorem plus the proposed
tangent bound would not, by itself, prove the advertised `1/3` coefficient.
The exact kernel identities and counterexamples remain valid; only that
conditional exponent calculation must not be quoted as a theorem.

## 5. Braid-local theorem and obstruction

An exposed long braid on roots `ab,ac,bc` versus `bc,ac,ab` transfers one
rank-one polynomial term between the two endpoint arrays.  With arbitrary
prefix and suffix there are common matrices `A_0,B_0` and nonnegative
polynomials `Phi,Psi` such that

\[
 Z_+(z)=Z_0(z)+z^2\Phi(z),\qquad
 Z_-(z)=Z_0(z)+z^2\Psi(z).                         \tag{6}
\]

This formula is exact and potentially useful for a global plateau theorem.
But all simple local descent ideas are false:

* the same labeled triple prefers opposite directions in different contexts
  already at `n=5`;
* a trace-neutral braid changes the mean at `n=8`;
* strict trace descent can increase the mean, and the graded profiles cross,
  at `n=9`;
* there are 982 weak trace minima among the 24698 classes at `n=7`.

Any braid proof must sum the full boundary terms globally; there is no
context-free packet orientation or trace-compatible scalar potential.

Artifact: `agent_braid_potential/BRAID_LOCAL_REPORT.md`.

## 6. Growing-state upper barrier

Let `Q_d=S_d[Q_(d-1)]` be a vertical tower with arbitrary, nonrepeating,
possibly indecomposable macros of sizes `r_d`.  Put

```text
l_d=log r_d,   L_d=sum_(t<=d) l_t,   eta_d=max_(t<=d) l_t/L_d.
```

The exact cap--cup product recurrence and the unavoidable two-block convex
term give

\[
 \log V(Q_d)\ge
 \frac12\left((L_d-l_d)^2-\sum_{t<d}l_t^2\right)
 \ge\frac12(1-3\eta_d+\eta_d^2)L_d^2.            \tag{7}
\]

Thus even unbounded state complexity and new indecomposable macros at every
level cannot beat `1/2` when the logarithmic mesh tends to zero.  A vertical
escape needs repeated macroscopic template jumps, heterogeneous children, or
a different mixed-triple geometry.  Independent coordinate evolution found
finite records `V(9)=169` and `V(20)=5155`, but no compatible recursion.

Artifact: `agent_growing_state_upper/GROWING_STATE_REPORT.md`.

## 7. The sharp diagonal `3/2` target

The unrestricted conjecture

\[
 \log v_k(P)\ge(3/2-o(1))k^2
 \quad\text{when}\quad \log|P|=2k+o(k)            \tag{8}
\]

remains open and would raise the global lower coefficient from `1/4` to
`3/8`.  It is sharp on balanced Pascal towers.  A new theorem proves (8) for
every arbitrarily nonstationary homogeneous vertical tower whose largest
macro has `o(k)` logarithmic size.  Hence a vertical counterexample again
requires a macroscopic template or different mixed geometry.  The exact
matrix identity `A(z)=B(-z)^(-1)` was also derived, but its higher alternating
coefficient identities do not by themselves imply a positive bound.

Artifact: `agent_diagonal_three_eighths/REPORT.md`.

## 8. What a total-count cap really forces

Write

\[
 \mathcal E(x,y)=x\log\frac{x+y}{x}+y\log\frac{x+y}{y}.
\]

The final cut audit proved the following unconditional directional floor.  If

```text
log V(P_N) <= (w+o(1))L^2,       L=log N,
|Q_N| = N^(alpha+o(1)),          Q_N subset P_N,
```

then

\[
 \min\{\log C(Q_N),\log U(Q_N)\}
 \ge(\beta_\alpha(w)-o(1))L^2,                  \tag{9}
\]

where `beta_alpha(w)` is the smaller nonnegative solution of

\[
 \mathcal E(w,\beta)=\alpha^2/4.
\]

For a linear-size subset at the target cap `w=1/2`, this gives
`beta=0.0524142083338...`.  Thus a globally sparse configuration cannot hide
all directional entropy in one-sided macroscopic blocks.  The bound is too
weak to improve `1/4` by itself.

The natural stronger collision guess

\[
 \frac{X E^2}{S_LS_R}\ge V(P)^{-1/2}N^{-O(1)}    \tag{10}
\]

survives the exact data and is exponent-sharp on the alternating family, but
remains conjectural.  A five-point certificate kills the simplest proposed
union/delete-terminal injection.  Even if (10) were proved, the established
entropy marginals give a fixed point below `1/4`; a successful cut proof needs
stronger multiscale information.

Artifact: `agent_total_capped_kernel/REPORT.md`.

## 9. Global braid plateaus

Quotienting the long-braid graph by equal-trace components gives `70` weak
sinks at `n=6` and `280` sink plateaus at `n=7`.  Their profiles happen to
have degree four, so mean is monotone in trace at those orders.  This rigidity
fails exactly at `n=8`: a seven-class weak sink plateau with `V=113` has first
moments `316,317,318`.  The seven-point minimizing closure lattice is also not
toggle-CDE; an exact sparse rational witness certifies the failure.  Thus
rowmotion/toggle-CDE and weak-sink rigidity do not prove the mean conjecture.

The surviving braid target is narrower: prove the mean bound only for global
lexicographic `(V,M)` minimizers by amortizing the *full* boundary vectors in
the rank-one switch formula.  No such theorem or asymptotic counterexample was
found.

Artifact: `agent_global_braid_plateau/GLOBAL_BRAID_PLATEAU_REPORT.md`.

## 10. Final frontier

The campaign did not resolve unrestricted Erdős 838.  The rigorous window is
still

\[
 \boxed{\frac14\le\liminf\frac{\log f(N)}{(\log N)^2}
 \le\limsup\frac{\log f(N)}{(\log N)^2}\le\frac12.}
\]

The best full-solution target is the minimizer-only mean inequality

\[
 \mathbb E_{A\text{ uniform convex}}|A|\ge\log N-O(1).
\]

The best incremental target is the sharp diagonal `3/2` theorem (8), which
would improve the lower coefficient to `3/8`.  On the upper side, all
fine-mesh homogeneous vertical towers are now blocked at `1/2`; a better
construction must use macroscopic jumps with heterogeneous children or a new
mixed-triple geometry.
