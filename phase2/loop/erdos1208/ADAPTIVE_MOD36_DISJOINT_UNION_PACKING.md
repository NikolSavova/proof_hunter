# Adaptive mod-36 mass: direct disjoint-union packing

## Status

This note gives a direct charge for the genuinely disjoint branch of
ADAPTIVE_MOD36_GLOBAL_DISJOINT_TRANSLATE_SATURATION.md. It does not pair
supports or ask for a Gaussian collision.

For a distinct selected source pair \(p\), let \(\mu(p)\) be the number of
tail translations in which it occurs, and let \(\Delta\) be the maximum
depth of the full Gaussian residual supports of the distinct source pairs.
If \(G(m)=m^{o(1)}\) is the Gaussian fixed-cell divisor bound, then

\[
\boxed{
X_{36}\le 153G(m)m^2\mu_{\max}\Delta,
\qquad
\mu_{\max}=\max_p\mu(p).
}
\tag{0.1}
\]

In particular, if distinct source-pair supports are globally disjoint, then
\(\Delta=1\). This is an ambient interval packing theorem: the full
residual \(a+18d\) has only \(O(m^2)\) possible integer values, regardless
of \(q\).

There is a useful dense-centroid consequence. Let \(H_{\rm all}\) be the
mass of all clean fibres and suppose the chosen collection carries
\(H_Q\ge m^{-o(1)}H_{\rm all}\). In the putative counterexample range
\(k\ge m^{2/3+\varepsilon}\), one has
\(H_Q\ge m^{2+6\varepsilon-o(1)}\). Thus (0.1) proves

\[
X_{36}\le m^{o(1)}H_Q
\tag{0.2}
\]

throughout the globally bounded-reuse branch
\(\mu_{\max}\Delta=m^{o(1)}\). With only the elementary isolation bound
\(\mu_{\max}\le k/2\), the same argument closes the disjoint-support branch
for \(k\ge m^{4/5+o(1)}\). Reaching \(2/3\) by interval packing alone
therefore requires a subpolynomial same-source translation multiplicity,
or a compensating estimate for large \(\mu(p)\).

The result is sharp at the \(H_Q\) scale and survives aggregation across
many translations. A polynomial-height family has \(\Theta(k)\) selected
records distributed over arbitrarily many literal \(q\)'s, with

\[
\mu_{\max}=\Delta=1,
\qquad
X_{36}=\Theta(H_Q),
\tag{0.3}
\]

and all selected full residual supports pairwise disjoint globally, not
merely inside one fibre. Hence a size-biased union argument cannot gain a
power below \(H_Q\), and the disjoint branch cannot be dismissed as one
exceptional translation. The family lies at polynomially sparse height,
so it does not refute (0.2) in the dense counterexample regime.

No counterexample to \(X_{36}\le m^{o(1)}H_Q\) is obtained. The exact
remaining disjoint-support gate is high same-source translation reuse, or
failure of \(Q\) to carry enough of the ambient centroid energy.

## 1. Use the full residual support

For a selected source pair \(p\), write

\[
a(p)=2\det(u_s,u_t),
\qquad
r=r(p).
\tag{1.1}
\]

For a determinant-qualified ordered target edge pair, put

\[
d(v,v')=2\det(v,v').
\tag{1.2}
\]

Define the full residual support

\[
\mathcal R(p)
=
\{a(p)+18d:n_r(d)>0,\ |d|>L\}.
\tag{1.3}
\]

If \(a(p)=c+36\lambda_p\) and \(d=2D\), then

\[
a(p)+18d=c+36(\lambda_p+D).
\tag{1.4}
\]

Thus \(\mathcal R(p)\) is exactly the residue-lift of the normalized support
\(\mathcal S(p)\) from the mod-36 note, and

\[
|\mathcal R(p)|=|\mathcal S(p)|.
\tag{1.5}
\]

Using the full support is important when summing different residue classes:
different classes are automatically disjoint modulo \(36\), while all of
them still occupy one short integer interval.

Every edge vector has both coordinates in
\([-(m-1),m-1]\). Therefore

\[
|\det(x,y)|\le 2(m-1)^2.
\tag{1.6}
\]

It follows that

\[
|a(p)|\le 4(m-1)^2,
\qquad
|d|\le 4(m-1)^2,
\tag{1.7}
\]

and hence

\[
|a(p)+18d|\le 76(m-1)^2.
\tag{1.8}
\]

All full residual supports are consequently contained in a common integer
interval of cardinality at most

\[
152(m-1)^2+1\le 153m^2.
\tag{1.9}
\]

No translation parameter \(q\) appears in this range bound.

## 2. Exact multiplicity-depth packing

Let \(\mathfrak T\) be the multiset of residue-refined tail occurrences
\((p,q)\), and let \(\mathcal P\) be the set of distinct source pairs that
occur in it. Put

\[
\begin{aligned}
\mu(p)&=|\{q:(p,q)\in\mathfrak T\}|,\\
\mu_{\max}&=\max_{p\in\mathcal P}\mu(p),\\
\Delta&=\max_g|\{p\in\mathcal P:g\in\mathcal R(p)\}|.
\end{aligned}
\tag{2.1}
\]

Gaussian factorization gives, uniformly in every determinant-qualified
cell,

\[
n_r(d)\le G(m)=m^{o(1)}.
\tag{2.2}
\]

Now swap the \(q\)-sum before doing any support pairing:

\[
\begin{aligned}
X_{36}
&=\sum_{p\in\mathcal P}\mu(p)U_L(r(p))\\
&\le G(m)\sum_{p\in\mathcal P}\mu(p)|\mathcal R(p)|\\
&\le G(m)\mu_{\max}\sum_{p\in\mathcal P}|\mathcal R(p)|\\
&=G(m)\mu_{\max}\sum_g
|\{p:g\in\mathcal R(p)\}|\\
&\le 153G(m)m^2\mu_{\max}\Delta.
\end{aligned}
\tag{2.3}
\]

This proves (0.1). In the globally disjoint branch the penultimate sum is
simply the size of a union; there is no collision energy or
Cauchy--Schwarz loss.

For an isolated source pair \(p\), its common translations have anchor
edges forming a matching. Hence

\[
\mu(p)\le |Q_p|\le \left\lfloor\frac{k}{2}\right\rfloor.
\tag{2.4}
\]

Equation (2.4) is sharp at the endpoint level, but it leaves a factor \(k\)
in (2.3). A useful continuation should attack \(\mu(p)\) specifically in
the determinant-rich selected tail, rather than return to support
intersections.

## 3. Why \(m^2\) is the right dense-range charge

Let

\[
M_3=\binom{k}{3},
\qquad
n_z=
\left|
\left\{
T\in\binom{A}{3}:\sum_{x\in T}x=z
\right\}
\right|.
\tag{3.1}
\]

There are fewer than \(9m^2\) possible triple sums. Pair-sum uniqueness
implies that distinct triples in one class are disjoint. Each unordered
pair of equal-sum triples supplies eighteen directed clean starts, so

\[
\begin{aligned}
H_{\rm all}
&=18\sum_z\binom{n_z}{2}\\
&=9\left(\sum_zn_z^2-M_3\right)\\
&\ge \frac{M_3^2}{m^2}-9M_3.
\end{aligned}
\tag{3.2}
\]

If \(M_3\ge 18m^2\), this gives

\[
H_{\rm all}\ge \frac{M_3^2}{2m^2}.
\tag{3.3}
\]

Suppose \(H_Q\ge\eta H_{\rm all}\), where
\(\eta=m^{-o(1)}\). If \(k\ge m^{2/3+\varepsilon}\), then (3.3) gives

\[
H_Q\ge m^{2+6\varepsilon-o(1)}.
\tag{3.4}
\]

Combining (2.3) and (3.4) proves the bounded-reuse claim in the status. If
only (2.4) and \(\Delta=m^{o(1)}\) are used, comparison of \(km^2\) with
\(k^6/m^2\) requires

\[
k^5\ge m^{4+o(1)},
\tag{3.5}
\]

which is the exponent \(4/5\). This calculation identifies the precise
power lost by allowing one source pair to survive in linearly many
translations.

The hypothesis \(H_Q\ge m^{-o(1)}H_{\rm all}\) is explicit and essential.
If the chosen low-codegree collection carries less mass, that loss must be
handled by the complementary high-codegree branch; interval packing alone
does not move mass into \(Q\).

## 4. Multi-translation sharpness construction

Fix an even record count \(R\) per block and a number \(J\) of blocks. Put

\[
E=JR,
\qquad
S=2E+1,
\tag{4.1}
\]

and choose a prime \(P\) with \(E\le P\le 2E\). For each block choose fresh
anchors \(a_j,b_j\) and \(q_j=a_j-b_j\). Install \(R\) source records in
that block. Across all blocks index the records by \(0\le t<E\), and use

\[
\begin{aligned}
z_t&=17+9t,\\
u_t&=(900S^2-z_t,z_t+1),\\
u'_t&=(900S^2-z_t-1,z_t).
\end{aligned}
\tag{4.2}
\]

As before,

\[
|u_t|^2-|u'_t|^2
=1800S^2
=-18(-100S^2)
\tag{4.3}
\]

and

\[
2\det(u_t,u'_t)=-1800S^2+70+36t.
\tag{4.4}
\]

The scaled perpendicular target pencil has every normalized target area in
\(S^2\mathbf Z\). Therefore all \(E\) normalized supports, even those in
different translations, occupy different residues modulo \(S^2\) and are
globally pairwise disjoint.

Each block consumes \(8R+2\) planted points. Take

\[
H=J(8R+2)+P+4
\tag{4.5}
\]

horizontal target points and four vertical points. After adjoining the
\(P\)-point filler, the total point count is

\[
k=2H,
\tag{4.6}
\]

while the two target records per horizontal point give

\[
U_N(-100S^2)=2H=k.
\tag{4.7}
\]

Finite avoidance makes every planted \(q_j\) the unique common translation
of its \(R\) records, forbids all other selected scalar-gap pairs,
preserves the filler rows, and makes the union distance-Sidon at polynomial
height. Within each block all \(2R\) centroid companion sets form a
singleton sunflower at \(b_j\).

Choose filler translations until the actual mass first reaches \(4k^2\).
Then every planted fibre has \(h_{q_j}=2R\) and

\[
b_{q_j}\le \frac{R}{2}.
\tag{4.8}
\]

At least \(JR/2=E/2\) records survive, so

\[
X_{36}\ge \frac{Ek}{2}
=\Theta(k^2)
=\Theta(H_Q).
\tag{4.9}
\]

Every source pair occurs in one translation and every full support has
depth one. Thus \(\mu_{\max}=\Delta=1\), even though the sharp mass is
spread over arbitrarily many active fibres. This proves (0.3).

## 5. Exact finite certificate

The verifier uses three planted translations, two records per translation,
a 47-point filler, and area scale \(S=13\). It constructs a 210-point
integral distance-Sidon set with

\[
\begin{array}{c|r}
k&210\\
N&21{,}945\\
\text{planted translations}&3\\
\sum_jh_{q_j}&12\\
U_N(-16{,}900)&210\\
\text{filler clean-start mass}&300{,}798\\
H_Q&176{,}425\\
b_{q_j}&1\\
X_{36}&630\\
\mu_{\max},\Delta&1,1.
\end{array}
\tag{5.1}
\]

All six selected full supports are pairwise disjoint. The verifier also
checks the exact fibres and common anchors, reconstructs the twelve
centroid companion sets, audits the actual adaptive denominator, and
exhausts randomized finite versions of (2.3).

Run:

    PYTHONPATH=phase2/loop/erdos1208 python3 \
      phase2/loop/erdos1208/verify_adaptive_mod36_disjoint_union_packing.py

## 6. Remaining gate

The direct disjoint-union branch is now reduced to two explicit quantities:

\[
\boxed{\mu_{\max}\Delta}
\qquad\text{and}\qquad
\boxed{\frac{H_Q}{H_{\rm all}}}.
\tag{6.1}
\]

When the distinct supports are truly disjoint, \(\Delta=1\). The metric
problem is then to show that a determinant-rich source pair cannot remain
in too many adaptive-tail translations, or to charge large \(\mu(p)\)
using its matching of anchor endpoints. This is structurally different
from the failed attempt to force equal Gaussian residuals.

If support depth is large, one has left the disjoint branch and obtained
global residual reuse across distinct source pairs. That branch may use
the full complex collision identity, but it is not needed for the packing
theorem proved here.
