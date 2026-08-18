# The transverse parallelogram gate

## Plain-language summary

The row second moment has an exact geometric form in the direct-sum set

\[
 B=A+JA.
\]

Distance-Sidonicity makes the map `A x A -> B`, `(a,b) -> a+Jb`, injective,
so `|B|=k^2`.  A transverse row of degree `r(d)` is exactly a set of source
points of `B` that can all be translated by the realized difference `d` back
into `B`.  Therefore

\[
 W=\sum_{d\in D}\binom{r(d)}2
\]

counts parallelograms in `B` whose translation side is a difference of `A`,
with the two known degenerate coordinate types deleted.  The exponent-critical
theorem is simply `W<=k^(4+o(1))`.

This formulation is exact, and it explains both the scale and the current
difficulty.  There are only `Theta(k^4)` unordered pairs in `B`, but a pair can
admit several realized-difference translations.  Pointwise bounded
multiplicity is false; what is still plausible is a subpolynomial *average*
multiplicity.  The 120-point adversary has `W=1.74405... k^4`.

## 1. Exact direct-sum model

Let `A` be a distance-Sidon set of `k` points, put `D=A-A`, and let `J` be
quarter-turn rotation.  If

\[
 a+Jb=a'+Jb',
\]

then `a-a'=J(b'-b)`.  The two sides have equal Euclidean norm, so radial
uniqueness gives `a=a'` and `b=b'`.  Thus

\[
 B=A+JA
\]

has exactly `k^2` points, each with a unique coordinate pair.

For `d in D`, define `X_d` to be the set of points

\[
 p=v+Jy\in B
\]

for which there are `u,x in A` such that

\[
 p+d=u+Jx\in B,
\]

the coordinate difference `e=x-y` is nonzero, and `d dot e != 0`.  Subtracting
the two displayed points gives

\[
 d=(u-v)+J(x-y).
\]

Conversely every transverse row relation has this form.  Uniqueness of the
two coordinates of a point of `B` makes the correspondence bijective, so

\[
 \boxed{|X_d|=r(d).}                              \tag{1.1}
\]

Consequently

\[
 \boxed{W=\sum_{d\in D}\binom{|X_d|}{2}}.         \tag{1.2}
\]

An element counted by (1.2) is an unordered pair `{p,q} subset B` together
with a realized difference `d` for which all four vertices

\[
 p,\ q,\ p+d,\ q+d
\]

belong to `B`, and both translation edges satisfy the transverse coordinate
condition.  It is therefore a parallelogram in `B` decorated by the unique
`A x A` coordinates of its four vertices.

## 2. Why this is exactly sufficient

Write

\[
 T=\sum_{d\in D}r(d),\qquad
 M_{\rm row}=\sum_{d\in D}r(d)^2.
\]

Then

\[
 M_{\rm row}=T+2W.                               \tag{2.1}
\]

If

\[
 \boxed{W\le k^{4+o(1)}},                        \tag{2.2}
\]

then `M_row<=k^(4+o(1))`.  Since `|D|<k^2`, Cauchy--Schwarz gives

\[
 T^2\le |D|M_{\rm row}\le k^{6+o(1)},
\]

and hence `T<=k^(3+o(1))`.  This is the desired transverse collision bound.
No absolute numerical constant in (2.2) is required.

Equivalently, for an unordered pair `{p,q} subset B`, let `mu(p,q)` be the
number of transverse realized differences `d` translating both points back
into `B`.  Double counting gives

\[
 W=\sum_{\{p,q\}\subset B}\mu(p,q).              \tag{2.3}
\]

Thus (2.2) asks only for subpolynomial average multiplicity among the
`Theta(k^4)` pairs of `B`.  Exact tests show that `mu` is not pointwise
bounded: on the 45-point hybrid witness the maximum already exceeds 20.

## 3. A secondary fixed-row graph

For fixed `d`, represent a row relation by the ordered endpoints `(u,v)` of
`f=u-v=d-Je`.  This defines a bipartite graph `H_d` with two copies of `A` as
its vertex classes and

\[
 |E(H_d)|=r(d).                                   \tag{3.1}
\]

If every pair of left vertices of `H_d` had only `k^(o(1))` common right
neighbours, the Kővári--Sós--Turán argument would give

\[
 r(d)\le k^{3/2+o(1)}.                            \tag{3.2}
\]

This would not solve #1208, but it would be the first rigorous fixed-power
improvement on the local gate and would narrow the moment tail substantially.
For the selected row of the 120-point closure witness, the exact graph has

\[
 |E(H_d)|=948,\qquad C_4(H_d)=1869,
\]

and maximum left-pair codegree six.  These numbers support (3.2), but no
subpolynomial codegree theorem is proved.  The codegree condition is itself a
rotated triple-fibre problem, so applying it as a black box would be circular.

## 4. Exact 120-point calibration

The deterministic closure chain is distance-Sidon and has maximum
collinearity three.  At `k=120`, the exact profile is

\[
\begin{aligned}
 |D|&=14281,\\
 T&=2798384=1.61944\ldots k^3,\\
 \max r&=948,\\
 M_{\rm row}&=726091848=3.50160\ldots k^4,\\
 M_{\rm col}&=718246448=3.46377\ldots k^4,\\
 W&=361646732=1.74405\ldots k^4,\\
 |A+JA-JA|&=1011786=0.58552\ldots k^3.
\end{aligned}
\]

The formerly tempting sharp inequality `W<=(k-1)T` now fails by a factor
`1.08600...`.  This is irrelevant to the exponent: (2.2) allows any
`k^(o(1))` factor.  The data continue to support the exponent-critical moment
conjecture while warning against searching for a coefficient-one injection.

`verify_transverse_closure_witness.py` and
`verify_transverse_closure_global.py` check the complete 120-point profile in
exact integer arithmetic.

## 5. Remaining proof obligation

The cleanest target is now one of the equivalent statements

\[
 \sum_{d\in D}\binom{|X_d|}{2}\le k^{4+o(1)}
\]

or

\[
 \sum_{\{p,q\}\subset B}\mu(p,q)\le k^{4+o(1)}.
\]

A proof must use the unique `A x A` decoration of `B`, not merely that
`|B|=k^2`: arbitrary planar sets can have far more parallelograms.  It must
also retain the transverse deletion; the perpendicular-ruler construction
has a fourth-power family of parallel coordinate coincidences.  No known
translation-energy, BSG, or generic incidence theorem supplies this decorated
average-multiplicity estimate.
