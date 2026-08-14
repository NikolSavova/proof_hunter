# Erdős 838: the sharp diagonal `3/2` attack

**Date:** 2026-08-13
**Verdict:** the unrestricted fixed-size conjecture is still open.  I found
neither a proof nor a stretchable counterfamily.  I did prove a new
construction-side barrier: every nonstationary homogeneous vertical tower
whose individual macro levels have sublinear logarithmic size satisfies the
sharp `3/2` diagonal lower bound.  Thus a vertical-composition counterexample
must contain a single macroscopic uncontrolled template (or leave the
homogeneous vertical model).  Ordinary hereditary thresholds, asymmetric
cap/cup counts, and off-the-shelf containers do not supply the missing
quadratic half-exponent.

All logarithms are base two.  Write `v_k(P)` for the number of convex
`k`-subsets.

## 1. Exact exponent transfer: `3/2` locally gives `3/8` globally

Suppose, uniformly for `m=2^{(2+o(1))k}`, that every `m`-point set satisfies

\[
 v_k(P)\ge 2^{(\sigma-o(1))k^2}.                 \tag{1}
\]

For an `n`-point set, apply (1) in every `m`-subset and double count.  If
`k=(\beta+o(1))\log n`, then

\[
 \log v_k(P)\ge
 \bigl(\beta-(2-\sigma)\beta^2-o(1)\bigr)(\log n)^2,
 \qquad \beta\le\tfrac12.                       \tag{2}
\]

For `sigma=3/2`, the right side is increasing on `[0,1/2]`, and at
`beta=1/2` it is `3/8`.  Equivalently, when the local theorem is uniform in
the `2k+o(k)` window, take `k=floor((log n)/2)` directly:

\[
 \log V(P)\ge\log v_k(P)
 \ge(3/2-o(1))k^2=(3/8-o(1))(\log n)^2.          \tag{3}
\]

This is the exact claim strength.  The balanced iterated Pascal templates in
`agent_graded_supersat/REPORT.md` have diagonal exponent tending to `3/2`, so
no universal exponent strictly above `3/2` is possible.

## 2. One additional exact endpoint identity

With the notation of the reverse-product trace identity, put

\[
 A(z)=T_{e_M}(z)\cdots T_{e_1}(z),\qquad
 B(z)=T_{e_1}(z)\cdots T_{e_M}(z).
\]

Since `T_e(z)^{-1}=T_e(-z)`, there is the exact polynomial-matrix identity

\[
 \boxed{A(z)=B(-z)^{-1},\qquad A(z)B(-z)=I.}     \tag{4}
\]

Let `R=sum_(i<j) E_(j,i)` and write
`A=I+zR+z^2A_2+...`, `B=I+zR+z^2B_2+...`.  The degree-two part of (4) is

\[
 \boxed{A_2+B_2=R^2.}                            \tag{5}
\]

Entrywise, for `s<t`, this says

\[
 (A_2)_{t,s}+(B_2)_{t,s}=t-s-1.                 \tag{6}
\]

Geometrically, every choice of one intermediate point is exactly a 3-cap or
a 3-cup with endpoints `s,t`.  This is the first common-endpoint conservation
law.  Higher coefficients of (4) are alternating convolutions, not positive
conservation laws; for example degree three contains both `RB_2` and
`A_2R`.  I found no valid way to turn them into a coefficientwise lower bound
for

\[
 v_k(P)=\sum_{a+b=k}\langle A_a,B_b\rangle_F.    \tag{7}
\]

Thus (4) is useful exact structure, but not a proof of the diagonal target.

## 3. Theorem: every fine nonstationary vertical tower has exponent `3/2`

This extends the fixed-template calculation to an unbounded, depth-dependent
sequence of templates.

Let `Q_0` be one point and

\[
 Q_i=S_i[Q_{i-1}]\qquad(1\le i\le d),             \tag{8}
\]

where every macro point of the stretchable template `S_i` is replaced by the
same sufficiently small vertical copy of `Q_(i-1)`.  Put

\[
 r_i=|S_i|,\quad \ell_i=\log r_i,\quad
 L_i=\sum_{h\le i}\ell_h=\log|Q_i|.              \tag{9}
\]

For `S_i`, let `p_i` be largest-cap-size minus one and `q_i` be
largest-cup-size minus one.

> **Fine-tower theorem.**  Consider any sequence of such towers and integers
> `k->infinity` for which
> \[
> L_d=2k+o(k),\qquad \delta_k:=\max_{i\le d}\ell_i=o(k). \tag{10}
> \]
> Then
> \[
> \boxed{\log v_k(Q_d)\ge(3/2-o(1))k^2.}         \tag{11}
> \]

### Proof

Write

\[
 A_i(x)=\sum_{j\ge1}c_j(S_i)x^{j-1},\qquad
 B_i(x)=\sum_{j\ge1}u_j(S_i)x^{j-1}.
\]

The exact graded composition recurrence iterates to

\[
 C_{Q_j}(z)=z\prod_{i=1}^j A_i(2^{L_{i-1}}z),
 \qquad
 U_{Q_j}(z)=z\prod_{i=1}^j B_i(2^{L_{i-1}}z).    \tag{12}
\]

Every subset of a cap is a cap, so `c_(x+1)(S_i)>=1` for every integer
`0<=x<=p_i`; similarly on the cup side.  Therefore, for any such `x_i`,

\[
 c_{1+\sum x_i}(Q_j)
 \ge 2^{\sum_i L_{i-1}x_i},                     \tag{13}
\]

and the identical bound holds for cups with capacities `q_i`.

The cup--cap theorem gives

\[
 r_i\le {p_i+q_i\choose p_i}\le2^{p_i+q_i},
 \qquad s_i:=p_i+q_i\ge\ell_i.                  \tag{14}
\]

At the last composition level choose any two macro blocks.  The exact convex
recurrence contains

\[
 {r_d\choose2}C_{Q_{d-1}}(z)U_{Q_{d-1}}(z).     \tag{15}
\]

Set `t=k-2`.  Since `L_(d-1)=2k+o(k)` by (10), the capacities
`s_1,...,s_(d-1)` contain at least `t` units.  Choose integers
`0<=z_i<=s_i`, `sum z_i=t`, maximizing

\[
 \sum_{i<d}L_{i-1}z_i.                           \tag{16}
\]

Every `z_i` splits as `x_i+y_i` with `0<=x_i<=p_i` and
`0<=y_i<=q_i`.  Equations (13) and (15) then give

\[
 \log v_k(Q_d)\ge\sum_{i<d}L_{i-1}z_i.          \tag{17}
\]

It remains only a weighted-slot estimate.  Give level `i` at least
`ell_i` units of capacity, all at weight `L_(i-1)`, and take the `t` largest
weights.  Compare this measure with Lebesgue measure on `[0,L_(d-1)]` by
collapsing each interval `[L_(i-1),L_i)` to its left endpoint.  Every unit
moves left by at most `delta_k`.  Extra integer capacity from
`s_i>=ell_i` can only increase the top-`t` sum.  Hence

\[
 \max (16)\ge
 \int_{L_{d-1}-t}^{L_{d-1}}x\,dx-\delta_k t
 =L_{d-1}t-\frac{t^2}{2}-\delta_k t.             \tag{18}
\]

Using `L_(d-1)=2k+o(k)`, `t=k-2`, and `delta_k=o(k)`, (18) is
`(3/2-o(1))k^2`.  This proves (11). `square`

### Consequence for counterexample design

The theorem permits different, growing templates at every level and does not
assume periodicity or a finite state space.  Therefore a homogeneous vertical
countertower below `3/2` must have

\[
 \max_i\log r_i=\Omega(k),                       \tag{19}
\]

so one macro template already occupies a positive fraction of the full
logarithmic scale.  Its diagonal behavior is essentially the original
unrestricted problem, not an entropy gain created by many small blow-up
levels.  Heterogeneous child types or nonvertical mixed-triple signatures
remain outside this theorem.

## 4. Why the requested standard tools stop short

### 4.1 Hereditary and asymmetric cap/cup multiplicity

At `N=2^{2k+o(k)}`, the ordinary convex-`k` threshold double count gives
only `2^{(1-o(1))k^2}` objects.  Iterating over intermediate subset sizes
telescopes exactly, as proved in `HEREDITARY_MULTIPLICITY_BARRIER.md`.
The desired theorem needs an additional `2^{(1/2-o(1))k^2}` multiplicity;
no selection of scales creates it.

The asymmetric cap--cup threshold gives an incidence lower bound on a **sum**
of cap and cup marginals.  It does not force both colors, because an arbitrarily
large pure cup contains no long cap, and conversely.  Even in the deliberately
optimistic symmetric calculation, a monochromatic path of size `k/2` has
threshold `2^{k+o(k)}`.  Lifting to `N=2^{2k}` gives only
`2^{(1/2+o(1))k^2}` such paths per side, whose hypothetical perfectly aligned
product has exponent only `1`, not `3/2`.  Genuine endpoint anti-alignment is
worse: valid vertical compositions can place cup-heavy blocks before cap-heavy
blocks, making the forward common-endpoint product exponentially smaller than
the product of the two marginals.  Thus asymmetric threshold counts need a new
common-endpoint supersaturation theorem; they do not prove it.

### 4.2 Entropy and containers

Convex `k`-sets are the `k`-cliques in the 4-uniform hypergraph of convex
quadruples, equivalently the independent `k`-sets in the hypergraph of rooted
nonconvex quadruples.  This is a clean reformulation, but the standard
container hypotheses are absent uniformly.  A triangle containing `N-3`
other points gives a bad-quadruple triple-codegree `N-3`; lower codegrees can
also be polynomially maximal.  The Erdős--Szekeres independence-number input
alone is far too weak: one guaranteed convex `2k`-set supplies only
`binom(2k,k)=2^{O(k)}` convex `k`-sets.

Consequently a container proof would need a new rank-three realizability
lemma that either stratifies these high-codegree rooted triangles or proves
stability toward Pascal-type recursive orders.  Generic container entropy
does not yield the missing `k^2/2` exponent.

## 5. Exact finite optimization and evidence boundary

`diagonal_probe.py` writes `certificate.json` using integer arithmetic.

* All `292864` reduced words for `w_0` at `n=6` were exhausted.  The exact
  coefficientwise minima are
  \[
  (v_1,\ldots,v_6)_{\min}=(6,15,20,3,1,1).
  \]
  A rational fixed-`x` realization is stored for every minimizer.  These
  values are only a small-order diagnostic; `n=6` is not in the asymptotic
  diagonal regime.
* The exact balanced-Pascal scan covers `88` pairs
  `4<=h<=18`, `1<=d<=6`.  Among rows with `k>=5`, the smallest observed
  `log(v_k)/k^2` is `1.539138765...` (`h=5,d=4,k=9`); among rows with
  `k>=10`, it is `1.560605697...` (`h=9,d=3,k=18`).  No scanned growing or
  iterated Pascal cell is below `3/2` after the very small rounded cases are
  excluded.  This is evidence only; the fine-tower theorem is the rigorous
  asymptotic statement.
* The exact weighted-capacity optimizer shows the finite discretization
  loss explicitly.  For total log-size `16`, the minimum top-half weight is
  `92,88,83,80` when the largest level has size `1,2,3,4` bits.  The proof's
  error `O(delta*k)` is therefore necessary at finite scale and becomes
  `o(k^2)` exactly under (10).

Reproduce with

```bash
python3 phase2/loop/erdos838/agent_diagonal_three_eighths/diagonal_probe.py
```

## 6. Final verdict

* **Unrestricted `3/2` conjecture:** live; no proof obtained.
* **Stretchable counterfamily:** none found.
* **Rigorous progress:** the sharp exponent holds for every fine-grained,
  arbitrarily nonstationary homogeneous vertical tower, so a countertower
  needs a macroscopic template or a genuinely different mixed geometry.
* **Remaining mathematical bottleneck:** a positive common-endpoint
  coefficient inequality for the reverse products, or an equivalent
  geometric codegree/stability theorem.  Marginal cap/cup counts and generic
  containers do not contain that information.
