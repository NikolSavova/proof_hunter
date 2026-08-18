# Foreign-shift averaging barrier in general position

## 1. Result

Let `J(x,y)=(-y,x)`.  For a finite distance-Sidon set `A` put

\[
 D_A=(A-A)\setminus\{0\},\qquad
 q_A(a,b,c)=C_3(D_A;J(b-a),J(c-a)),
\]

where

\[
 C_3(X;u,v)=|\{x\in X:x+u,x+v\in X\}|.
\]

The proposed rich-triangle estimate in
`FOREIGN_SHIFT_TRIANGLE_COUNTEREXAMPLE.md` is false by a polynomial factor,
even in general position.

**Theorem (compact-anchor averaging barrier).**  There are arbitrarily large
integer distance-Sidon sets `A` with no three points collinear such that

\[
 \sum_{\substack{(a,b,c)\in A^3\\
                  a,b,c\text{ distinct and non-collinear}}}
 q_A(a,b,c)\gg |A|^{7/2}.                       \tag{1.1}
\]

More strongly, for `Omega(|A|^(3/2))` ordered non-collinear triangles one
has

\[
 q_A(a,b,c)\gg |A|^2.                           \tag{1.2}
\]

Consequently the hoped-for tail

\[
 |\{(a,b,c):q_A(a,b,c)\ge\lambda\}|
 \le |A|^{3+o(1)}/\lambda                       \tag{1.3}
\]

fails at `lambda` of order `|A|^2`: its left side can have order
`|A|^(3/2)`, whereas the proposed right side has order `|A|^(1+o(1))`.

The proof does not use a correlation estimate for Welch permutations.  It is
an exact third-moment averaging argument valid for every dense difference
core and every compact anchor set.

## 2. The averaging identity

Let `D,U subset Z^2` be finite.  For `y in Z^2` put

\[
 N_y=|\{u\in U:y+u\in D\}|.
\]

Changing variables `x=y+u_0` gives the exact identity

\[
 \boxed{
 \sum_{(u_0,u_1,u_2)\in U^3}
 C_3(D;u_1-u_0,u_2-u_0)=\sum_y N_y^3.}          \tag{2.1}
\]

Also

\[
 \sum_yN_y=|D||U|,
 \qquad |\{y:N_y>0\}|=|D-U|.
\]

Hölder therefore gives

\[
 \boxed{
 \sum_{u_0,u_1,u_2\in U}
 C_3(D;u_1-u_0,u_2-u_0)
 \ge {(|D||U|)^3\over |D-U|^2}.}               \tag{2.2}
\]

If `D` has order `p^2` and lies in a box of side `O(p)`, while `U` has
order `sqrt(p)` and diameter `O(sqrt(p))`, the right side is
`Omega(p^(7/2))`.  This is the source of the extra square-root factor.

## 3. Compact Sidon sets in general position

For an odd prime `r`, let

\[
 P_r=\{(x,[x^2]_r):0\le x<r\}\subset[0,r-1]^2, \tag{3.1}
\]

where `[x^2]_r` is the least nonnegative residue.

The set `P_r` is vector-Sidon.  Indeed, equality of two directed difference
vectors implies modulo `r` that

\[
 x_1-x_2=x_3-x_4=:d,
 \qquad d(x_1+x_2)=d(x_3+x_4).
\]

The difference is nonzero, so the two sums agree; since `2` is invertible,
the ordered endpoint pairs agree.

The set also has no three collinear points.  Integer collinearity would imply
collinearity modulo `r`, but a nonvertical line over `F_r` meets the parabola
`y=x^2` in at most two points.  A vertical line contains only one point.

## 4. Make the two difference spectra disjoint

Let `p` tend through odd primes.  By Bertrand's postulate, for every
sufficiently large `p` there is a prime `q` with

\[
 {\sqrt p\over16}\le q\le {\sqrt p\over4}.     \tag{4.1}
\]

Start with the core `P_p` and anchors `U=P_q`.  Every nonzero undirected
difference of `U` can coincide with at most one undirected edge of `P_p`,
because `P_p` is vector-Sidon.  For every coincident edge choose and delete
one core endpoint.  There are at most

\[
 {q(q-1)\over2}\le {p\over32}
\]

such edges.  The remaining core `B subset P_p` therefore satisfies

\[
 |B|\ge31p/32,
 \quad D=(B-B)\setminus\{0\},
 \quad |D|=|B|(|B|-1)\asymp p^2,               \tag{4.2}
\]

and

\[
 D\cap((U-U)\setminus\{0\})=\varnothing.       \tag{4.3}
\]

Both `B` and `U` remain vector-Sidon and in general position.

## 5. The supercubic non-collinear moment

The set `D` lies in `[-p+1,p-1]^2`, and `U` lies in `[0,q-1]^2`.  Hence

\[
 |D-U|\le(2p+q-2)^2=O(p^2).                    \tag{5.1}
\]

Equations (2.2), (4.1), and (4.2) give

\[
 \sum_{u_0,u_1,u_2\in U}
 C_3(D;u_1-u_0,u_2-u_0)\gg p^{7/2}.            \tag{5.2}
\]

At most `3q^2` ordered triples have a repeated anchor, and each contributes
at most `|D|=O(p^2)`.  Their total is `O(p^3)`, negligible in (5.2).  Every
three distinct points of `U` are non-collinear, so

\[
 \sum_{\substack{u_0,u_1,u_2\in U\\\text{distinct}}}
 C_3(D;u_1-u_0,u_2-u_0)\gg p^{7/2}.            \tag{5.3}
\]

There are `Theta(q^3)=Theta(p^(3/2))` ordered distinct triples, every
correlation is at most `|D|=O(p^2)`, and their average is `Omega(p^2)`.
A fixed positive proportion must therefore have correlation `Omega(p^2)`.
This proves the quantitative tail assertion before the metric lift.

## 6. Lift to Euclidean distances

Apply the anchor-lifting lemma from
`FOREIGN_SHIFT_TRIANGLE_COUNTEREXAMPLE.md` to `B` and `U`.  Condition (4.3)
and vector-Sidonicity allow an integral nonsingular linear map `T` and an
integer translate `t` for which

\[
 A=T(B)\cup\{t-JT(u):u\in U\}                  \tag{6.1}
\]

is distance-Sidon.  The finitely many additional bad translates that put a
core point and two anchors, or an anchor and two core points, on one line may
also be avoided.  Since both components already have no three collinear,
the resulting `A` is in general position.

For every ordered anchor triple, each witness in (5.3) gives a distinct
fibre containing those three anchors.  Therefore (5.3) is a lower bound for
the non-collinear fibre moment of `A`.  Finally

\[
 |A|=|B|+|U|=\Theta(p),
\]

which proves (1.1) and (1.2).

For completeness, the generic choice of `T` in the lifting lemma should also
avoid a finite family of identities

\[
 T(b-b')=-JT(u-u'),                            \tag{6.2}
\]

so distinct core-anchor pairs have distinct centres.  Cross-distance
collisions are then proper affine lines in the `t`-plane, cross/internal
collisions are proper circles, and cross-component collinearities are proper
lines.  A finite union of these curves cannot cover `Z^2`.

## 7. Exact finite certificate

`verify_foreign_shift_averaging_barrier.py` uses `p=127` and `q=7`.
Deleting 17 of the 127 parabola-core points makes its difference spectrum
disjoint from the seven-point anchor spectrum.  It verifies

* a 110-point vector-Sidon core and a seven-point vector-Sidon anchor set;
* no three collinear points in either set;
* the exact identity (2.1), with both sides equal to `880874`;
* ordered distinct-anchor contribution `317592`, with individual
  correlations between `1386` and `1591`;
* an explicit integral metric lift with 117 points, all 6786 unordered
  distances distinct, and maximum collinearity two;
* all 210 ordered anchor triangles and every one of their lifted fibres.

Run

```text
python3 phase2/loop/erdos1208/verify_foreign_shift_averaging_barrier.py
```

## 8. Consequence for the full problem

The global `T_nc<=k^(3+o(1))` route and its rich-tail strengthening are now
closed, even for sets with maximum collinearity two.  The obstruction is not
Welch-specific, a carry phenomenon, or hidden line structure.  It is the
elementary fact that a dense difference set has a large third moment against
every compact set of `sqrt(k)` anchors.

The generic metric lift gives no useful control of the side length of the
smallest containing square.  Thus it does **not** refute a theorem that uses
the ambient side `m` quantitatively.  One exponent-compatible third-moment
successor would be

\[
 \boxed{
 T_{\rm nc}(A)\ll k^{3+o(1)}+m\,k^{3/2+o(1)}}  \tag{8.1}
\]

for distance-Sidon `A subset [m]^2`, at least first in general position.
Indeed, the exact Hölder support inequality

\[
 |A+J(A-A)|\gg {k^{9/2}\over T_{\rm nc}(A)^{1/2}}
\]

combined with either term of (8.1) gives `k<=m^(2/3+o(1))`.  The first term
gives cubic support directly; the second gives

\[
 m^2\gg k^{15/4}/m^{1/2},
\]

again equivalent to `k<=m^(2/3)`.  Unlike the falsified global estimate,
(8.1) permits large foreign-shift moments when the algebraic metric lift has
large height.

However, (8.1) is not now the primary route.  The same compact-anchor family
has the expected **cubic second-moment** scale: roughly `p^2` fibres contain
roughly `sqrt(p)` anchors, contributing `p^3` to `sum r(z)^2` but `p^(7/2)`
to `sum r(z)^3`.  It therefore separates the two approaches sharply.

The viable full-resolution target remains the transverse second-moment
estimate

\[
 E_{\rm trans}(A)\le k^{3+o(1)},                 \tag{8.2}
\]

or equivalently the fourth-power decorated-parallelogram gate in
`TRANSVERSE_SECOND_MOMENT_GATE.md`.  Together with Elekes's trapezoid bound,
(8.2) proves cubic rotated support in the wide regime.  The present theorem
closes the tempting third-moment detour and sends the attack back to (8.2),
where this new family is sharp rather than obstructive.  An ambient theorem
such as (8.1) remains a secondary option if the second-moment gate fails.
