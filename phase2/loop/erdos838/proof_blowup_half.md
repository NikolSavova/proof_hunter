# A \(1/2\) upper coefficient for Erdős problem 838

> Status, 2026-08-13: self-contained candidate proof, checked by two
> independent exact finite order-type audits. This supersedes the
> \(0.639326\ldots\) central-cell bound in proof_central.md. It has not yet
> been externally refereed or checked against a complete MathSciNet citation
> graph.

All logarithms in this note are base \(2\).

## Theorem

Let \(f(N)\) be the minimum, over all \(N\)-point sets \(P\) in general
position in the plane, of the number of subsets of \(P\) in convex position.
Then

\[
 \boxed{\qquad
 \limsup_{N\to\infty}
 \frac{\log f(N)}{(\log N)^2}\leq \frac12.
 \qquad}                                                    \tag{T}
\]

Including or excluding the empty set and sets of size at most two does not
affect the conclusion.

The construction is a directionally specified realization of an iterated
**order-type blow-up** of a large balanced cap--cup extremal configuration.
Generic order-type blow-ups and almost-vertical Erdős--Szekeres blow-ups
already occur in the literature; what is used here is the particular pair of
mixed-triple signs below. The key point is that the
number of caps and cups multiplies by a polynomial at every substitution;
the number of all convex subsets is then controlled by the product of those
two quantities.

For construction provenance, see Han--Kohayakawa--Sales--Stagni,
*SODA 2019*, for iterated order-type blow-ups, and Baek--Balko,
*SoCG 2025 / JCTA 2026*, for almost-vertical Erdős--Szekeres blow-ups. The
targeted search recorded in `agent_killsearch/SECOND_STAGE.md` found no
source containing the mixed-sign enumerator (2) or the resulting constant.

## 1. Vertical lexicographic composition

Put every point set in increasing \(x\)-order and write
\(\chi(a,b,c)\in\{-,+\}\) for the orientation of an ordered triple.
We use point sets whose \(y\)-coordinates also increase. This is no
restriction: the shear \((x,y)\mapsto(x,y+Mx)\), for sufficiently large
positive \(M\), preserves every orientation and makes the \(y\)-coordinates
increase with \(x\).

Let \(S=(s_1,\ldots,s_r)\) and \(Q=(q_1,\ldots,q_n)\) be two such point
sets. Replace each \(s_i=(X_i,Y_i)\) by

\[
 Q_i=\{(X_i+\varepsilon^2x_j,\;Y_i+\varepsilon y_j):q_j=(x_j,y_j)\}.
                                                               \tag{1}
\]

For all sufficiently small positive \(\varepsilon\), call the resulting
set \(S[Q]\). Its orientation signs, for points in increasing \(x\)-order,
are as follows.

* Three points in one block have their sign from \(Q\).
* Three points in distinct blocks have their sign from \(S\).
* If the first two points lie in one block, the sign is negative.
* If the last two points lie in one block, the sign is positive.

Indeed, the first two assertions follow by affine invariance and continuity.
For two points in a common block, their displacement is
\((\varepsilon^2\Delta x,\varepsilon\Delta y)\), with both coordinate
differences positive. Against a point in a later block the determinant is
negative for small \(\varepsilon\); against a point in an earlier block it
is positive. There are only finitely many determinants and strict coordinate
inequalities, so all the assertions hold throughout an interval
\(0<\varepsilon<\varepsilon_0\). Choosing a rational \(\varepsilon\) in this
interval gives an exact rational realization in general position. Its two
coordinates are again strictly increasing, so the construction can be
iterated without a limiting or compactness argument.

## 2. Exact substitution formulas

A nonempty **cap** has every triple negative, and a nonempty **cup** has
every triple positive. Singletons and pairs count as both. For a point set
\(R\), write

\[
 c_j(R),\quad u_j(R),\quad v_j(R)
\]

for the numbers of \(j\)-point caps, cups, and convex-position subsets.
Also put

\[
 C(R)=\sum_{j\geq1}c_j(R),\quad
 U(R)=\sum_{j\geq1}u_j(R),\quad
 W(R)=\sum_{j\geq1}v_j(R).
\]

### Lemma 1 (composition count)

If \(|S|=r\), \(|Q|=n\), then

\[
\begin{aligned}
 C(S[Q])
   &=C(Q)\sum_{j\geq1}c_j(S)n^{j-1},\\
 U(S[Q])
   &=U(Q)\sum_{j\geq1}u_j(S)n^{j-1},              \tag{2}\\
 W(S[Q])
   &=rW(Q)+C(Q)U(Q)\sum_{j\geq2}v_j(S)n^{j-2}.
\end{aligned}
\]

#### Proof

Consider first a cap meeting at least two blocks. Only its first occupied
block can contain more than one point: two points in any later block,
together with an earlier point, form a positive triple. Its intersection
with the first block is an arbitrary nonempty cap of \(Q\); every other
occupied block contributes one arbitrary point. The occupied block indices
must form a cap of \(S\), and the four orientation rules show that these
conditions are also sufficient. Summing over a \(j\)-point macro-cap gives
the first formula. The cup formula is its reflection.

Now let \(X\subseteq S[Q]\) be convex and meet at least two blocks. Decompose
its boundary into the upper cap and lower cup. A lower cup that reaches a
later block can contain only the leftmost selected point of the first block,
since two first-block points followed by a later point form a negative
triple. Hence every selected point of the first block lies on the upper cap,
so that block intersects \(X\) in a cap. Reflection shows that the last block
intersects \(X\) in a cup. Every intermediate occupied block contains exactly
one point. To see the last assertion, suppose that \(a<b_1<b_2<c\) are
selected, with \(b_1\)
and \(b_2\) in the same intermediate block and \(a,c\) in earlier and later
blocks. The two points \(b_1,b_2\) have the same orientation relative to
the line \(ac\), while

\[
 \chi(a,b_1,b_2)=+,\qquad \chi(b_1,b_2,c)=-.
\]

If \(b_1,b_2\) lie above \(ac\), then a convex four-set would have both on
its upper chain, forcing \(\chi(a,b_1,b_2)=-\), a contradiction. If they
lie below \(ac\), both would lie on the lower chain, forcing
\(\chi(b_1,b_2,c)=+\), again a contradiction. Thus the four-set is not in
convex position.

Choose the unique selected point from every intermediate occupied block
and one representative from each endpoint block. These representatives
are a subset of \(X\), hence are in convex position; their order type is
the corresponding subset of \(S\). Thus the occupied block indices form a
convex subset of \(S\).

Conversely, let \(B\) be a convex \(j\)-subset of \(S\), \(j\geq2\). Choose
a nonempty cap in its first block, a nonempty cup in its last block, and one
point in every intermediate block. Take the upper macro-hull of \(B\),
insert the entire first-block cap, and use the rightmost point of the
last-block cup. This is a cap by the first part of the proof. Similarly,
the leftmost point of the first-block cap, the lower macro-hull, and the
entire last-block cup form a cup. These chains have the same left and right
endpoints and together contain every chosen point. A strict cap lies above
its endpoint chord and a strict cup lies below that chord. Hence the two
chains do not cross, and their union is the boundary of a convex polygon.
The choices are unique and contribute
\(C(Q)U(Q)n^{j-2}\). Convex subsets lying in a single block contribute
\(rW(Q)\), proving the final formula. \(\square\)

## 3. Iterating one template

Fix a point set \(S\) of size \(r\geq2\). Suppose its largest cap has size
\(a\) and its largest cup has size \(b\). Starting with a singleton \(Q_0\),
define

\[
 Q_d=S[Q_{d-1}],\qquad |Q_d|=r^d.                 \tag{3}
\]

Let \(C_d=C(Q_d)\), and define \(U_d,W_d\) analogously. The first two
polynomials in (2) have degrees \(a-1\) and \(b-1\), respectively, with
positive leading coefficients. Hence, with constants depending only on
\(S\),

\[
\begin{aligned}
 \log C_d
 &\leq (a-1)\log r\sum_{t=0}^{d-1}t+O_S(d)
  =\frac{a-1}{2}(\log r)d^2+O_S(d),\\
 \log U_d
 &\leq\frac{b-1}{2}(\log r)d^2+O_S(d).           \tag{4}
\end{aligned}
\]

The last polynomial in (2) has fixed degree at most \(r-2\). Unrolling its
recurrence and applying (4) at every level gives

\[
 \log W_d\leq
 \frac{a+b-2}{2}(\log r)d^2+O_S(d).              \tag{5}
\]

For clarity, the \(t\)-th cross-block summand has logarithm at most
\((a+b-2)(\log r)t^2/2+O_S(t)\); multiplication by the remaining powers of
\(r\), and summation over \(d\) levels, alter this by only \(O_S(d)\).
Since \(\log|Q_d|=d\log r\), (5) becomes

\[
 \limsup_{d\to\infty}
 \frac{\log W(Q_d)}{(\log|Q_d|)^2}
 \leq\frac{a+b-2}{2\log r}.                       \tag{6}
\]

In fact equality holds in (6). Each of the first two polynomials in (2)
has a positive leading coefficient, so the reverse inequalities in (4)
hold with the same quadratic terms. The two-point subsets of \(S\) make the
last polynomial in (2) nonzero, and the last cross-block summand alone gives

\[
 \log W_d\geq\log C_{d-1}+\log U_{d-1}+O_S(d).
\]

Consequently

\[
 \lim_{d\to\infty}
 \frac{\log W(Q_d)}{(\log|Q_d|)^2}
 =\frac{a+b-2}{2\log r}.                           \tag{7}
\]

## 4. A balanced cap--cup extremal template

The classical Pascal construction contains, for every \(k\geq3\), a point
set \(S_k\) with

\[
 |S_k|={2k-4\choose k-2},                         \tag{8}
\]

with no \(k\)-cap and no \(k\)-cup. For completeness, take the central cell
\(T_{2k-4,k-2}\) of the strong-glue construction. In the recurrence
\(T_{m,i}=T_{m-1,i-1}\prec T_{m-1,i}\), a cap uses a cap from the left child
and at most one point of the right child. Induction shows that the largest
cap of an interior cell \(T_{m,i}\) has size \(i+1\); reflection shows that
its largest cup has size \(m-i+1\). (The two boundary cells are singletons.)
Thus \(S_k\) has largest cap and cup both of size \(k-1\), as claimed.

Apply (6) with

\[
 r=r_k={2k-4\choose k-2},\qquad a=b=k-1.
\]

For every fixed \(k\), the iterated construction, followed when necessary
by deleting points from the least \(Q_d\) with \(|Q_d|\geq N\), gives

\[
 \limsup_{N\to\infty}
 \frac{\log f(N)}{(\log N)^2}
 \leq \frac{k-2}{\log {2k-4\choose k-2}}.         \tag{9}
\]

Deletion cannot create new convex subsets, and for fixed \(k\) the least
power \(r_k^d\geq N\) has logarithm \(\log N+O_k(1)\), so this passage from
powers to arbitrary \(N\) has no effect on the normalized coefficient.

Finally, Stirling's formula yields

\[
 \log {2k-4\choose k-2}=2k-O(\log k).
\]

Letting \(k\to\infty\) in (9) proves (T). \(\square\)

The constant \(1/2\) is also best possible within the class of iterated
vertical compositions using one fixed template. Indeed, the cap--cup
theorem applied with forbidden sizes \(a+1\) and \(b+1\) gives

\[
 r\leq {a+b-2\choose a-1}\leq2^{a+b-2}.
\]

Thus the exact coefficient in (7) is always at least \(1/2\), while the
balanced templates \(S_k\) make it tend to \(1/2\).

## 5. Verification artifact

The script lexicographic_blowup.py constructs the abstract order type
\(S[Q]\), independently counts its caps and cups by last-edge dynamic
programming, and independently counts all convex subsets by the exact
upper/lower endpoint factorization. A 9-point composition is also checked by
directly enumerating all \(2^9\) subsets. For
\(S=Q=T_{4,2}\), both the substitution formulas and the independent dynamic
program return

\[
 (C,U,W)=(14136,14136,441399)
\]

on the 36-point composition. This tests every case in Lemma 1 without
enumerating \(2^{36}\) subsets.

## 6. What remains open

The currently rigorous base-\(2\) window is now

\[
 \frac14\leq\liminf_{N\to\infty}
 \frac{\log f(N)}{(\log N)^2}
 \leq\limsup_{N\to\infty}
 \frac{\log f(N)}{(\log N)^2}
 \leq\frac12.                                     \tag{10}
\]

Closing the problem requires either a universal lower coefficient \(1/2\),
or a still better construction. The endpoint identity

\[
 V(P)=1+|P|+\sum_{s<t}c(s,t)u(s,t)
\]

shows the exact lower-bound target: prove that cap-path and cup-path mass
cannot avoid one another across their common endpoint pairs. The present
construction is useful evidence for that target—its total convex-subset
coefficient approaches \(1/2\)—but it does not prove it.
