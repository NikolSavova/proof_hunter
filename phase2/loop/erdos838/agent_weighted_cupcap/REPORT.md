# Weighted cup--cap endpoints: a counterfamily and the corrected localization target

**Date:** 2026-08-14  
**Verdict:** the proposed constant-loss weighted endpoint-span inequality is
false, even for an elementary integral point family.  Its deficit tends to
minus infinity.  The failure is fully compensated by exponentially many
convex subsets which abandon the bad right endpoint.  This isolates a
strictly stronger and still-live localization-compensation statement, but I
did not prove the bounded-congestion lemma needed to turn it into the full
half-weight theorem.

All logarithms are base two.  A monotone path with `r` edges has weight
`z^r`.  Thus, for endpoints `i<j`,

\[
 F_{ij}(z):=U_{ij}(z)C_{ij}(z)
\]

is the generating polynomial of convex subsets with exact horizontal
endpoints `i,j`, weighted by their number of vertices.  Write

\[
 \mu_{ij,z}=z\frac{F'_{ij}(z)}{F_{ij}(z)}.
\]

## 1. WES is false by an unbounded amount

For every `n>=3`, take the integral point set

\[
 P_n=\{q_k=(k,k^2):0\le k\le n-2\}\cup\{t=(n-1,0)\}.
                                                               \tag{1}
\]

The points are in general position.  Three parabola points have positive
orientation.  For `0<=a<b<=n-2`,

\[
 \operatorname{orient}(q_a,q_b,t)
 =-(b-a)\{a^2+(a+b)(n-1-a)\}<0.                \tag{2}
\]

Consider the full-span endpoint pair `(q_0,t)`.

* A cup from `q_0` to `t` cannot use an interior `q_a`, since the triple
  `(q_0,q_a,t)` has negative orientation.  Hence it is only the direct edge.
* A cap from `q_0` to `t` cannot use two interior points, since every triple
  `(q_0,q_a,q_b)` on the strict parabola has positive orientation.  Every
  choice of one interior point does give a three-vertex cap.

Consequently the endpoint polynomials are exactly

\[
 U_{0,n-1}(z)=z,\qquad
 C_{0,n-1}(z)=z+(n-2)z^2,
\]

and therefore

\[
 F_{0,n-1}(z)=z^2+(n-2)z^3.                    \tag{3}
\]

At half activity,

\[
 \boxed{\mu_{0,n-1,1/2}=3-\frac2n.}             \tag{4}
\]

Thus

\[
 \mu_{0,n-1,1/2}-\log n=3-\frac2n-\log n
 \longrightarrow-\infty.                       \tag{5}
\]

This disproves

\[
 \mu_{1/2}(U_{ij})+\mu_{1/2}(C_{ij})
 \ge\log(j-i+1)-O(1)
\]

for stretchable order types.  It also kills an integrated per-endpoint
repair: from (3),

\[
 \frac{F(1)}{F(1/2)}=\frac{8(n-1)}n<8.          \tag{6}
\]

So neither the half-activity mean nor the activity integral of a single
long endpoint pair need grow at all.

The earlier span-seven polynomial `z^2+5z^3` was not an isolated finite
obstruction: it is the `n=7` member of (3).

## 2. The compensation is exact and exponential

Deleting `t` leaves `n-1` points on a strict convex parabola, so all of their
subsets are convex.  In fact the complete profile of (1) is

\[
 v_k(P_n)=
 \begin{cases}
  1,&k=0,\\
  \binom nk,&1\le k\le3,\\
  \binom{n-1}k,&4\le k\le n.
 \end{cases}                                      \tag{7}
\]

Indeed, a subset avoiding `t` is convex.  A subset containing `t` and at
least three parabola points is not convex: for three selected parabola
points `q_a,q_b,q_c`, `a<b<c`, the middle point lies in the triangle
`q_a q_c t`.  Hence

\[
 Z_{P_n}(1)=2^{n-1}+1+(n-1)+\binom{n-1}{2},       \tag{8}
\]

whereas the bad endpoint contributes only `F(1)=n-1`.  At half activity,

\[
 Z_{P_n}(1/2)
 =(3/2)^{n-1}+\frac12+\frac{n-1}{4}
   +\frac1{8}\binom{n-1}{2}.                     \tag{9}
\]

In particular `H(P_n)=nZ(1/2)/Z(1)` decays exponentially.  The local failure
therefore points in exactly the wrong direction for a counterexample to the
global half-weight inequality.

There is a useful comparison with the visible-pocket certificate

\[
 q_i=(i,i(L-i)),\quad p=(-1,(L+1)^2).
\]

It has the same global profile: the chain points form a Boolean convex
family, while a set containing `p` is convex only when it uses at most two
chain points.  But for the endpoint pair formed by the two ends of the chain,
the endpoint cap polynomial is `z(1+z)^m`, so its weighted mean is large.
Thus the parabola-chord and visible-pocket views exhibit complementary local
obstructions inside the same abstract convexity profile.  A proof cannot
choose only one local operation.

## 3. A universal constant localization lemma

There is one elementary statement which always survives.  Let `I=[i,j]`,
let `m=|I|`, and let `\mathcal L_{ij}` be the link of the endpoint pair:

\[
 \mathcal L_{ij}=\{S\subset I\setminus\{i,j\}:
                    S\cup\{i,j\}\text{ is convex}\}.
\]

It is a down-set and

\[
 F_{ij}(z)=z^2\sum_{S\in\mathcal L_{ij}}z^{|S|}. \tag{10}
\]

For every `S` in the link, all four sets

\[
 S,\quad S\cup\{i\},\quad S\cup\{j\},
 \quad S\cup\{i,j\}
\]

are distinct convex subsets of `P[I]`.  Hence

\[
 Z_{P[I]}(1)\ge4F_{ij}(1).                       \tag{11}
\]

Jensen under the endpoint Gibbs law also gives

\[
 \frac{F_{ij}(1)}{F_{ij}(1/2)}
 =\mathbb E_{ij,1/2}2^{|A|}
 \ge2^{\mu_{ij,1/2}}.                            \tag{12}
\]

Combining them,

\[
 \boxed{
 \log\frac{Z_{P[I]}(1)}{F_{ij}(1/2)}
 \ge\mu_{ij,1/2}+2.}                            \tag{13}
\]

This proves only constant localization.  The missing factor is precisely
the horizontal span.

## 4. The corrected target

The counterfamily suggests replacing WES by an explicit endpoint-dilution
term:

\[
 \boxed{
 \mu_{ij,1/2}
 +\log\frac{Z_{P[I]}(1)}{F_{ij}(1)}
 \ge\log m-O(1).}                               \tag{LC-WES}
\]

By (12), `(LC-WES)` implies the mass-localization inequality

\[
 \boxed{
 mF_{ij}(1/2)\le O(1)Z_{P[I]}(1).}              \tag{ML}
\]

This is the right pointwise dichotomy:

* if the endpoint Gibbs mean is logarithmic, the endpoint family pays for
  itself through its activity ratio;
* if the mean is small, the endpoint family must be diluted by many convex
  faces elsewhere in its interval.

Both the parabola-chord and visible-pocket families have exponential slack
in `(LC-WES)` and `(ML)`.

An exhaustive walk over every commutation class in `B(n,2)` through `n=8`
found no failure of either corrected inequality.  The numerical minima were

\[
\begin{array}{c|rrrrrr}
n&3&4&5&6&7&8\\\hline
\min(\mu-\log\mathrm{span})
 &.7484&.5000&.2781&.0817&-.0931&-.2500
\end{array}
\]

for the false WES score.  In contrast, over the same complete search,

\[
 \min\left\{\log\frac{Z_I(1)}{F_{ij}(1/2)}-\log m\right\}
 =\log(64/9)=2.830074998\ldots,                  \tag{14}
\]

always attained on a three-point interval.  Equivalently, the attractive
finite strengthening

\[
 mF_{ij}(1/2)\le\frac9{64}Z_{P[I]}(1)            \tag{15}
\]

survives every reflection order through eight wires.  This is evidence, not
a theorem.  The exact `n=20,24,30` planar half-weight records also satisfy
(14), with whole-span slack `4.74,5.37,5.61` bits respectively.

### Stronger span weights and endpoint markers

The follow-up census tested where the compensating faces are allowed to
live.  Define

\[
\begin{aligned}
 L_{ij}&=1+\sum_{i<b\le j}F_{ib}(1),\\
 R_{ij}&=1+\sum_{i\le a<j}F_{aj}(1),\\
 E_{ij}&=L_{ij}+R_{ij}-F_{ij}(1).
\end{aligned}                                      \tag{16}
\]

Thus `L` counts interval faces whose exact left endpoint is the left marker,
`R` is reflected, and `E` counts faces which retain at least one marker.
The numerical exponent fingerprints are:

\[
\begin{array}{c|c|c}
\text{allowed compensating mass}&\text{largest surviving exponent}
 &\text{candidate inequality}\\\hline
Z_{P[I]}(1)&2&m^2F_{ij}(1/2)\le O(1)Z_{P[I]}(1)\\
E_{ij}&5/3&m^{5/3}F_{ij}(1/2)\le O(1)E_{ij}\\
\max(L_{ij},R_{ij})&3/2&m^{3/2}F_{ij}(1/2)\le O(1)\max(L_{ij},R_{ij})\\
F_{ij}(1)&0&\text{no positive span power is possible.}
\end{array}                                       \tag{17}
\]

The last row is rigorously killed by (6).  The first three rows are
conjectures, not theorems.  They survived the complete `B(8,2)` census and
the exact planar `n=20,24,30` records.  Their tightest observed logarithmic
scores `log(RHS/Fhalf)-a log m` were:

\[
\begin{array}{c|rrrr}
&B(8,2)&n=20&n=24&n=30\\\hline
a=2,\ RHS=Z_I&-0.0786&+0.1962&+0.1596&+0.1821\\
a=3/2,\ RHS=\max(L,R)&+0.0052&+0.154&+0.259&+0.147\\
a=5/3,\ RHS=E&+0.0902&+0.272&+0.355&+0.178.
\end{array}                                      \tag{18}
\]

The near equalities at three different exponents appear structural rather
than a loose constant effect.  Span cubed against the full interval has
scores `-3.91,-4.07,-4.39` on the three planar records, so no finite evidence
supports an exponent above two.

## 5. Why pointwise localization still does not close #838

Even a proof of `(ML)` cannot simply be summed over endpoint pairs.  The
right-hand intervals overlap.  A convex face with horizontal span `d` is
contained in many larger intervals, and

\[
 \sum_{i\le\min A,\,j\ge\max A}\frac1{j-i+1}
\]

can have order `n` for a short centrally located face.  Thus the naive sum
of `(ML)` loses a polynomial factor, whereas the half-weight theorem permits
only `n^{o(1)}` congestion.

The stronger exponent ladder (17) clarifies the overlap calculation.  If an
interval inequality has weight `m^{-a}`, then a target face of exact span
`d` occurs in superintervals with total weight

\[
 \sum_{I\supseteq A}|I|^{-a}
 =\begin{cases}
   O(\log(n/d)),&a=2,\\
   O(d^{2-a}),&a>2.
  \end{cases}                                      \tag{19}
\]

Thus the conjectural span-squared full-interval inequality has only
logarithmic congestion.  For a one-marker charge, only one endpoint of the
superinterval varies, and the corresponding tail is

\[
 \sum_{r\ge d}r^{-a}=O(d^{1-a}).                  \tag{20}
\]

So the `3/2` and `5/3` marker conjectures give respectively
`d^{-1/2}` and `d^{-2/3}` reuse.  These are genuine improvements over the
unweighted interval charge, but they still do not by themselves supply the
global `1/n` factor: full-count mass could be concentrated in faces of short
horizontal span.  A final proof needs a multiscale escape statement saying
that such concentration recursively creates enough mass in disjoint or
translated intervals.

The remaining theorem has to be a **history-retaining localization flow**:
charge a bad endpoint face to the convex faces which cause its dilution,
while recording enough of the abandoned endpoint/tangent chain that any
target receives only `n^{o(1)}` total charge.  Collapsing to the interval
alone is insufficient, just as collapsing a visible-chain inverse fibre to
its root is insufficient.

I found no proof of this bounded-congestion statement.  A generic simplicial
down-set argument cannot prove it: rank-truncated links give abstract
counterexamples to the span factor.  The load-bearing input must be planar
rooted-circuit/tangent structure or global minimizer status.

## 6. Verification

The exact integral-family and visible-pocket certificates are generated by

```bash
python3 phase2/loop/erdos838/agent_weighted_cupcap/verify_counterexamples.py
```

It checks orientations, endpoint polynomials, the formula (4), the profiles
through `n=13`, and writes `certificate.json`.

The complete higher-Bruhat audit is

```bash
c++ -std=c++17 -O3 \
  phase2/loop/erdos838/agent_weighted_cupcap/exhaustive_wes.cpp \
  -o /tmp/exhaustive_wes
for n in 3 4 5 6 7 8; do /tmp/exhaustive_wes "$n"; done
```

It enumerates `1,232,944` commutation classes at `n=8` and evaluates WES,
`(LC-WES)`, and `(ML)` on every endpoint interval.
