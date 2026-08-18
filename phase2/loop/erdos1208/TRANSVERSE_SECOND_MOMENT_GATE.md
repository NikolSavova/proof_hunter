# The transverse row--colour moment gate

## Plain-language summary

The maximum local-overlap conjecture is strongly threatened by the 90-point
closure witness, and a new 65-point witness shows that the formally dual
maximum-colour conjecture is even less plausible: one fixed perpendicular
edge supports `1010 = 0.239... k^2` transverse relations.  Neither pointwise
bound is the right target.

There is, however, a sharper global statistic that survives all three targeted
adversaries.  Put the transverse relations into a square incidence matrix
whose rows are realized differences `d` and whose columns are realized
differences `e`.  The exact sufficient statement is that the squared row
degrees (or, dually, the squared column degrees) sum to `k^(4+o(1))`.  Cauchy--
Schwarz then gives the desired `k^(3+o(1))` total transverse count.  The heavy-
row, heavy-colour, and hybrid witnesses all lie on this fourth-power scale.

This is a rigorous new reduction plus a falsification package, not a proof of
the moment bound.  It replaces a false-looking `L^infinity` target by a
variance/tail theorem that is exactly calibrated to the observed extremizers.

The closure chain kills the tempting sharp inequality
`sum_d binom(r(d),2) <= (k-1)sum_d r(d)`.  At 120 points its two sides differ
by a factor `1.08600...`.  A constant-factor version would still suffice, but
the actual exponent-critical target is weaker:

\[
 \sum_d\binom{r(d)}2\le k^{4+o(1)}.                 \tag{0.1}
\]

The 120-point witness has left side only `1.74405... k^4`.  Thus the sharp
constant has failed while the necessary exponent remains calibrated.  The
direct-sum parallelogram meaning of (0.1) is recorded separately in
`TRANSVERSE_PARALLELOGRAM_GATE.md`.

## 1. The row--colour matrix

Let `A` be a distance-Sidon set of `k` planar points, let

\[
 D=A-A,
 \qquad J(x,y)=(-y,x),
\]

and define the `D x D` zero--one matrix

\[
 B(d,e)=
 \mathbf 1_D(d-Je)\,
 \mathbf 1_{e\ne0}\,
 \mathbf 1_{d\cdot e\ne0}.                       \tag{1.1}
\]

The row degree is the previous local overlap

\[
 r(d)=\sum_e B(d,e)=m_{\rm tr}(d),                 \tag{1.2}
\]

whereas the column degree is

\[
 c(e)=\sum_d B(d,e)
 =\#\{f\in D:f+Je\in D,\ (f+Je)\cdot e\ne0\}.     \tag{1.3}
\]

Thus `c(e)` counts the transverse representations having one fixed
perpendicular edge (one fixed displacement colour).  If

\[
 T=\sum_d r(d)=\sum_e c(e),                        \tag{1.4}
\]

then the exact identity from `TRANSVERSE_LOCAL_GATE.md` is

\[
 T=2E_{\rm trans}(A).                              \tag{1.5}
\]

The two second moments are

\[
 M_{\rm row}(A)=\sum_{d\in D}r(d)^2,
 \qquad
 M_{\rm col}(A)=\sum_{e\in D}c(e)^2.              \tag{1.6}
\]

## 2. Exact sufficient lemma

Since distance-Sidon implies vector-Sidon,

\[
 |D|=k(k-1)+1<k^2.                                 \tag{2.1}
\]

Cauchy--Schwarz applied to (1.4) gives both

\[
 T^2\le |D|M_{\rm row}(A),
 \qquad
 T^2\le |D|M_{\rm col}(A).                        \tag{2.2}
\]

Consequently either one of the estimates

\[
 \boxed{M_{\rm row}(A)\le k^{4+o(1)}}              \tag{2.3}
\]

or

\[
 \boxed{M_{\rm col}(A)\le k^{4+o(1)}}              \tag{2.4}
\]

implies

\[
 E_{\rm trans}(A)\le k^{3+o(1)}.                  \tag{2.5}
\]

Thus (2.3) or (2.4) closes the transverse gate.  Together with Elekes's
trapezoid estimate it proves cubic rotated support in the wide regime
`L <= sqrt(k) log k`.  As already recorded in
`PARALLEL_LINE_SUPPORT_LEMMA.md`, a separate multiscale coupling to the exact
line-support bound is still needed for polynomially rich intermediate line
occupancy.  The moment lemma by itself is not yet a full proof of #1208.

More quantitatively, if

\[
 M_{\rm row}(A)\le k^{4+\theta+o(1)},              \tag{2.6}
\]

then `T <= k^(3+theta/2+o(1))`.  This records exactly how any partial moment
gain would propagate through the collision argument.

## 3. Why ordinary BSG does not reach this scale

Write `N=|D| asymp k^2` and ignore the harmless transverse deletion.  The
quantity `T` counts pairs `(f,e) in D x D` for which `f+Je` lands back in
`D`.  If

\[
 T\ge N^{3/2+\delta},                              \tag{3.1}
\]

then Cauchy--Schwarz gives only

\[
 E^+(D,JD)\ge {T^2\over N}\ge N^{2+2\delta}.       \tag{3.2}
\]

Relative to the natural maximum `N^3`, the standard BSG parameter is

\[
 K=N^{1-2\delta}.                                  \tag{3.3}
\]

The usual energy form of Balog--Szemeredi--Gowers therefore guarantees only
a subset on the scale `N/K=N^(2 delta)` and a doubling constant polynomial in
`K`.  At the fixed-power excess relevant here this is far too small and far
too weak: such subsets may lie on a line, and line-structured pieces are
allowed.  The graph form begins from density
`T/N^2=N^(-1/2+delta)` and incurs the same polynomial-density loss.

Hence a black-box BSG invocation does not produce the needed inverse theorem.
The missing input would have to be a *radial/realizability-sensitive* inverse
statement at sparse density, or the direct moment estimate (2.3).

## 3a. Equivalent wedge form and the sharp-constant failure

Regard (1.1) as the adjacency matrix of the bipartite row--colour relation,
or regard the row side as the transverse graph on `D`.  Put

\[
 W=\sum_{d\in D}\binom{r(d)}2.
\]

Then

\[
 M_{\rm row}=T+2W.                                \tag{3.4}
\]

The stronger estimate `W<=CkT` gives `M_row <= (2Ck+1)T`.  Combining this
with `T^2 <= |D|M_row` and `|D|<k^2` yields

\[
 T\le (2Ck+1)|D|=O(k^3).                          \tag{3.5}
\]

This is stronger than the exponent-critical target (0.1): the remaining
transverse theorem needs only `W<=k^(4+o(1))`, with no comparison to `T`.

The deterministic heavy-row chain came extremely close to suggesting the
sharp choice `C=1`.  At `k=100`,

\[
 W=147209136 < 99T=147542076,
\]

a ratio of `0.997743...`.  Five further exact distance-Sidon extensions reverse
the sign.  At `k=105`,

\[
\begin{aligned}
 T&=1788384,\\
 M_{\rm row}&=385677360,\\
 W&=191944488,\\
 104T&=185991936,
\end{aligned}
\]

so `W/(104T)=1.032004...`.  This is a certified counterexample to `C=1`, not
to a constant-factor or exponent target.  It also warns that an eventual proof
must have slack and cannot be a termwise injection into exactly `k-1` labels.

At `k=120` the drift continues:

\[
 T=2798384,\qquad
 W=361646732=1.744052\ldots k^4,
\]

and `W/(119T)=1.086001...`.  Meanwhile
`M_row=3.501600...k^4`, `M_col=3.463766...k^4`, and the rotated support is
`0.585524...k^3`.  These data make the distinction important: coefficient
optimization is the wrong task, whereas the fourth-power exponent remains
fully viable.

## 4. Exact fixed-colour adversary

Fix the realized edge

\[
 t=(0,-1)\in D,
 \qquad Jt=(1,0).                                  \tag{4.1}
\]

Its column degree is the number of sources `f in D` for which both `f` and
`f+(1,0)` lie in `D`, excluding the parallel case.  In endpoint variables
each occurrence is the four-point affine relation

\[
 a-b-c+e=(1,0).                                    \tag{4.2}
\]

`search_transverse_color_closure.py` repeatedly forces a fourth point from
three roles of (4.2), rejects every candidate causing a repeated squared
distance, and greedily maximizes the exact column degree.  Starting from the
certified 16-point seed, it reaches an exact 65-point distance-Sidon set with

\[
 c(t)=1010=0.23905\ldots k^2.                      \tag{4.3}
\]

The witness has maximum collinearity four, so this is not a disguised ruler
or few-line example.  Its full profile is

\[
\begin{aligned}
 |D|&=4161,\\
 T&=45044=0.1640\ldots k^3,\\
 \max_d r(d)&=43,\\
 M_{\rm row}&=660000=0.03697\ldots k^4,\\
 M_{\rm col}&=12509352=0.70077\ldots k^4,\\
 |A+JA-JA|&=251195=0.91468\ldots k^3.
\end{aligned}                                      \tag{4.4}
\]

Thus a columnwise `k^(1+o(1))` theorem is at least as badly threatened as the
earlier rowwise theorem, but the second-moment scale survives comfortably.
`verify_transverse_color_closure.py` checks (4.3)--(4.4) using exact integer
arithmetic.

## 5. The complementary and hybrid adversaries

For the 90-point heavy-row closure witness, the exact dual profile is

\[
\begin{aligned}
 \max r&=614, &M_{\rm row}&=167919192
                         =2.55935\ldots k^4,\\
 \max c&=344, &M_{\rm col}&=164807112
                         =2.51192\ldots k^4.
\end{aligned}                                      \tag{5.1}
\]

So a square-root-heavy row is compatible with (2.3) because there are very
few rows at that height.

`search_transverse_dual_closure.py` then pools candidates forced by the
heavy-row and heavy-colour relations and maximizes their product.  It reaches
an exact 45-point distance-Sidon set with

\[
 r((0,-1))=147,
 \qquad c((0,-1))=292,                             \tag{5.2}
\]

and

\[
\begin{aligned}
 T&=64912,\\
 M_{\rm row}&=2800568=0.6829\ldots k^4,\\
 M_{\rm col}&=3316352=0.8088\ldots k^4,\\
 |A+JA-JA|&=66203=0.7265\ldots k^3.
\end{aligned}                                      \tag{5.3}
\]

Its maximum collinearity is three.  The hybrid search therefore realizes
both concentrations simultaneously, but only on the scale compatible with
the fourth-power moment gate.  `verify_transverse_dual_closure.py` checks all
numbers in (5.2)--(5.3).

## 6. Scope and the next theorem

The clean target is now:

> **Transverse moment conjecture.**  Every planar distance-Sidon set `A` of
> size `k` satisfies `M_row(A) <= k^(4+o(1))` (or, equivalently for the proof
> strategy, the column analogue).

This is not a statement about arbitrary radial transversals.  The canonical
radial representatives from `RADIAL_ADDITIVE_TRIPLE_AUDIT.md` already have
`M_row/|D|^2` growing rapidly (from `1.95` at box radius `10` to `11.43` at
radius `40`).  A proof must use that `D` is the complete directed difference
set of one `k`-point set, not just that `D` meets every origin-centred circle
in at most one antipodal pair.

The most faithful next formulations are therefore:

1. a direct tail bound
   `#{d:r(d)>=lambda} <= k^(4+o(1))/lambda^2`;
2. a decorated-midpoint incidence proof of the same bound; or
3. a sparse inverse theorem saying that a fixed-power excess in (2.3) forces
   a rank-two affine pattern in `A-A` that is incompatible with radial
   uniqueness at polynomial coordinate height.

A black-box additive inverse theorem, an `L^infinity` estimate on rows or
columns, and a radial-transversal-only argument have all been falsified or
quantitatively ruled out.
