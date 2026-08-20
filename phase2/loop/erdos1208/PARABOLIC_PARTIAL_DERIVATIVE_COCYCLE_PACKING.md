# Partial derivative lines: cocycle packing and the many-slope residual

## 1. Outcome

The exact derivative cocycle closes a nontrivial part of the graph-like
parabolic residual, including matching-like rich lines which have no long
shift paths.

Let \(\mathcal L\) be any family of nonhorizontal rich lines in the
derivative graphs

\[
 P_c=\{(r,d_c(r)):r,r+c\in R\},\qquad
 d_c(r)=f(r+c)-f(r).                                    \tag{1.1}
\]

In particular, \(\mathcal L\) may be the full family of rich lines, with
many lines at the same shift.  For \(\ell\in\mathcal L\), write its shift
as \(c_\ell\) and its patch as

\[
 d_{c_\ell}(r)=\alpha_\ell+\lambda_\ell r
 \quad(r\in S_\ell),\qquad L_\ell=|S_\ell|\ge3.        \tag{1.2}
\]

The main new theorem is:

**Same-slope packing.**  Any two distinct patches of the same slope obey

\[
 \boxed{|S_\ell\cap S_{\ell'}|\le1.}                   \tag{1.3}
\]

More precisely, distinct lines at the same shift meet in at most one
tail, and parallel distinct lines at the same shift have disjoint tail
sets.  At different shifts, (1.3) follows from the derivative cocycle.

Consequently, if the full chosen line family uses \(J\) distinct slopes,
then

\[
 \boxed{
 \sum_{\ell\in\mathcal L}n_{c_\ell}L_\ell^2
 < {3\over2}Jk^3,}                                     \tag{1.4}
\]

where \(n_c=|P_c|\le k\).  In particular every direction whose exceptional
partial lines have \(J=m^{o(1)}\) slope entropy contributes only
\(m^{o(1)}k^3\), regardless of how many short components those lines have.
This is inside the required \(m^{o(1)}(k^3+m^2)\) scale.

The unequal-slope, different-shift case also has an exact closure law.  If
\(c_\ell>c_{\ell'}\), then the overlap
\(S_\ell\cap S_{\ell'}\), translated by \(c_{\ell'}\), lies on a
derivative line in \(P_{c_\ell-c_{\ell'}}\) of slope

\[
 \boxed{\lambda_\ell-\lambda_{\ell'}.}                  \tag{1.5}
\]

Thus two partial rich patches with at least three common tails either have
equal slope, which is impossible by (1.3), or generate another
nonhorizontal rich derivative patch.  This is the precise cocycle
supersaturation mechanism missing from the path-curvature argument.

There is a second clean consequence.  Suppose all patches in
\(\mathcal L\) have \(L_\ell\ge T\ge4\), and no two of their tail sets
meet in three points.
Then

\[
 \boxed{
 \sum_{\ell\in\mathcal L}n_{c_\ell}L_\ell^2
 <{2k^4\over T-2}.}                                    \tag{1.6}
\]

Hence very rich matching-like patches with \(T\ge k/m^{o(1)}\) are already
closed unless they generate child patches through (1.5).

The theorem does not yet control a family with polynomially many distinct
slopes and recursively abundant child patches.  That is now the exact
survivor.  A genuine polynomial-height distance-Sidon construction in
Section 5 shows that one pure matching derivative line may have
\(\Theta(k)\) points and nonzero slope, so curvature of a single path
cannot replace the cocycle argument.

## 2. Adapted coordinates and vector uniqueness

Fix a primitive graph-like direction \(w\), choose \(z_w\) with
\(\det(w,z_w)=1\), and write

\[
 x_r=r z_w+f(r)w.                                      \tag{2.1}
\]

The displacement at shift \(h\) and tail \(r\) is

\[
 \Delta_h(r)=x_{r+h}-x_r
 =h z_w+d_h(r)w.                                       \tag{2.2}
\]

Distance-Sidonicity implies vector-Sidonicity: two equal nonzero directed
displacement vectors have equal squared length, hence arise from the same
ordered endpoint pair.  Therefore, for every fixed nonzero \(h\),

\[
 \boxed{d_h(r)=d_h(s)\Longrightarrow r=s.}              \tag{2.3}
\]

This elementary injectivity is what converts the cocycle into the packing
theorem.

There is also a useful richness cutoff before the cocycle is needed.  If
all relevant lines in every cell have occupancy at most \(L\), the standard
cellwise Szemeredi--Trotter estimate and

\[
 \sum_c n_c=k(k-1),\qquad \sum_c n_c^2\le k^3
\]

give

\[
 T_w\ll k^3\log k+k^2L^2.                              \tag{2.4}
\]

Thus, up to the harmless logarithm, the range \(L\le\sqrt{k}\) is already
on the desired \(k^3\) scale.  The cocycle analysis is only needed for the
dyadic richness bands \(L>\sqrt{k}\).

## 3. Proof of full-family same-slope packing

The cocycle and its difference form are

\[
\begin{aligned}
 d_{c+d}(r)&=d_c(r)+d_d(r+c),\\
 d_c(r)-d_d(r)&=d_{c-d}(r+d)\qquad(c>d).                \tag{3.1}
\end{aligned}
\]

First consider two distinct patches at the same shift.  They are distinct
geometric lines in the \((r,d_c(r))\)-plane, hence have at most one common
point and therefore at most one common tail.  If their slopes are equal,
the lines are distinct and parallel, so their tail sets are disjoint.

Now consider patches \(\ell,\ell'\) at distinct shifts.  Relabel them so
that \(c=c_\ell>d=c_{\ell'}\).  Suppose
\(r\in S_\ell\cap S_{\ell'}\).  Substituting (1.2) into the second identity
gives

\[
 d_{c-d}(r+d)
 =(\alpha_\ell-\alpha_{\ell'})
  +(\lambda_\ell-\lambda_{\ell'})r.                    \tag{3.2}
\]

If \(\lambda_\ell=\lambda_{\ell'}\), the right side is independent of \(r\).
Two distinct common tails would therefore give two distinct tails
\(r+d\) in the same shift-\((c-d)\) cell with equal derivative value,
contradicting (2.3).  This proves (1.3).

For a fixed slope \(\lambda\), (1.3) says that every unordered pair of
tail levels belongs to at most one \(S_\ell\), even when the family has
many lines at one shift.  Hence

\[
 \sum_{\ell:\lambda_\ell=\lambda}{L_\ell\choose2}
 \le{k\choose2}.                                      \tag{3.3}
\]

Since \(L\ge3\) implies \(L\le {L\choose2}\),

\[
 \sum_{\ell:\lambda_\ell=\lambda}L_\ell^2
 =\sum_\ell\left(2{L_\ell\choose2}+L_\ell\right)
 \le3{k\choose2}.                                      \tag{3.4}
\]

Bounding each line's weight by \(n_{c_\ell}\le k\), then summing over
the \(J\) slopes, proves (1.4).  Thus (1.4) controls the actual full
rich-line family rather than a one-line-per-shift surrogate.

This argument never joins two line points whose tails differ by the
original shift \(c\).  It therefore applies unchanged when every selected
line is a union of isolated matching edges.

## 4. Unequal-slope propagation and triple packing

For patches at distinct shifts and without assuming equal slopes, rewrite
(3.2) at \(t=r+d\):

\[
 d_{c-d}(t)
 =\alpha_\ell-\alpha_{\ell'}
  -(\lambda_\ell-\lambda_{\ell'})d
  +(\lambda_\ell-\lambda_{\ell'})t.                   \tag{4.1}
\]

Thus the translated overlap

\[
 (S_\ell\cap S_{\ell'})+d                             \tag{4.2}
\]

is contained in a line of \(P_{c-d}\) with slope
\(\lambda_\ell-\lambda_{\ell'}\).  This proves (1.5), including the intercept and
tail translation.  Equal slopes would make the child horizontal, and
(2.3) limits that overlap to one point.

Now suppose every pair of tail sets in the full family \(\mathcal L\) has
intersection at most two.  Every unordered triple of levels then belongs
to at most one \(S_\ell\), so

\[
 \sum_{\ell\in\mathcal L}{L_\ell\choose3}
 \le{k\choose3}.                                      \tag{4.3}
\]

For \(L_\ell\ge T\ge4\),

\[
 L_\ell^2\le {12\over T-2}{L_\ell\choose3}.           \tag{4.4}
\]

Indeed the right side is
\(2L_\ell(L_\ell-1)(L_\ell-2)/(T-2)\), which is at least
\(2L_\ell(L_\ell-1)\ge L_\ell^2\).  Bounding
\(n_{c_\ell}\le k\), summing, and using (4.3) gives (1.6).

For the full family, a same-shift pair already intersects in at most one
tail.  Therefore any forbidden overlap of three tails necessarily occurs
at distinct shifts and creates the child patch (4.1).  Within each cell,
three collinear derivative points determine their line uniquely, so the
actual record count of the chosen lines is
\(\sum_\ell {L_\ell\choose3}\).  The global low-overlap hypothesis then
packs their three-tail supports as in (4.3), even across different cells.

Equations (1.5)--(1.6) give an exact dichotomy for very rich partial lines:
either their triple supports pack and are cheap, or a pair creates a new
rich line at the difference shift and difference slope.  A continuation
must control iteration of this child operation.

For clarity, the actual record count of a dyadic line family is even more
direct than the weighted envelope (1.6).  If all its tail sets meet
pairwise in at most two points, then uniqueness of the line through three
points and (4.3) give

\[
 \sum_{\ell\in\mathcal L}{L_\ell\choose3}
 \le {k\choose3}=O(k^3).                               \tag{4.5}
\]

Consequently every low-overlap dyadic family is closed, including the
only nontrivial incidence range \(L>\sqrt{k}\).  In that range a surviving
family must have many pairs with at least three common tails, and every
such pair is necessarily at distinct shifts and produces the child line
(4.1).

## 5. A genuine pure-matching derivative patch

The path-curvature lemma cannot see an isolated matching, and this
configuration is genuinely realizable.

For every \(t\), take levels \(0,\ldots,2t-1\), shift \(c=t\), and impose

\[
 f(r+t)-f(r)=\alpha+\lambda r\qquad(0\le r<t),           \tag{5.1}
\]

with \(\lambda\ne0\).  The \(t\) displayed correspondences are pairwise
vertex-disjoint, so their tail shift graph has \(t\) singleton components.
Nevertheless all \(t\) derivative points lie on one nonhorizontal line.

There are integral specializations of polynomial height for which the
resulting \(2t\) points \((r,f(r))\) are distance-Sidon.  Treat
\(f(0),\ldots,f(t-1),\alpha,\lambda\) as independent variables and define
the upper values by (5.1).  Every unintended equality between two squared
distances is a polynomial of degree at most two.  No such polynomial is
identically zero: the independent lower endpoint variables distinguish
the two unordered edges, while two displayed matching edges have distinct
fixed vertical differences when \(\lambda\ne0\).  The grid nonvanishing
lemma therefore supplies an integral point outside the union of the
polynomially many forbidden hypersurfaces, at polynomial height.

The verifier contains the explicit \(t=8\) certificate

\[
\begin{split}
f={}&(7432,17624,170957,101948,127007,102246,73129,165089,\\
    &1007435,1017664,1171034,1102062,1127158,1102434,
      1073354,1165351).
\end{split}                                             \tag{5.2}
\]

It has \(c=8\), \(\lambda=37\), eight isolated matching
correspondences, and all \({16\choose2}=120\) squared distances distinct.
This is a barrier to local path curvature, not to the desired aggregate:
one such line contributes only \(O(k^3)\).

## 6. Exact remaining route

The graph-like derivative residual now splits further.

1. The generic Szemeredi--Trotter contribution is \(O(k^3\log k)\), and
   (2.4) closes every richness band \(L\le\sqrt{k}\), up to logarithms.
2. Long path components are paid by the curvature-height theorem.
3. Partial rich lines using only \(m^{o(1)}\) slopes are paid by (1.4),
   even if they are entirely matching-like.
4. Every dyadic family with pairwise tail overlap at most two contributes
   only \(O(k^3)\) actual triples by (4.5); (1.6) also controls its weighted
   Szemeredi--Trotter envelope.
5. Every remaining overlap of at least three tails generates a child patch
   under the exact
   difference map
   \[
   (c,d,\lambda_c,\lambda_d)\longmapsto
   (c-d,\lambda_c-\lambda_d).                           \tag{6.1}
   \]

The unresolved mass is therefore confined to richness
\(L>\sqrt{k}\), polynomial slope entropy, and abundant three-tail overlaps
with substantial closure under (6.1).  This is strictly smaller than the
former collection of arbitrary partial/matching rich lines.  A full proof
needs an additive-growth or height theorem for this derivative-patch
closure system, or a critical distance-Sidon counterexample realizing it.

## 7. Verification

Run

    python phase2/loop/erdos1208/verify_parabolic_partial_derivative_cocycle_packing.py

The verifier checks the cocycle, same-shift line geometry, full-family
same-slope packing, exact child intercept and slope, pair/triple packing,
the finite inequalities behind (1.4) and (1.6), integer-parabola closure,
and genuine distance-Sidon certificates for a pure matching, two
same-slope lines at different shifts, and two parallel lines at one shift.
