# Polynomial-height balanced sieve: the global directional gate is false even with an \(m^{o(1)}\) loss

## Status

This note strengthens `GLOBAL_DIRECTIONAL_SHORT_COMPENSATOR_NO_GO.md`.
The exponential-height CRT there is unnecessary.  A standard lower-bound
linear sieve gives a parameter \(t\) of polynomial size for which every
active transformed direction is primitive.  Consequently there is an
infinite family of genuine integer Euclidean distance-Sidon sets
\(A_p\subset[0,m_p]^2\), \(|A_p|=p\), such that

\[
 m_p=O(p^{17}),\qquad
 \sum_w H_w=\Omega(p^4),\qquad
 p\sum_w e_w+\sum_w M_w^2=O(p^3).                 \tag{0.1}
\]

In particular,

\[
 \frac{\sum_wH_w}{p\sum_we_w+\sum_wM_w^2}
 =\Omega(p)=\Omega(m_p^{1/17}).                    \tag{0.2}
\]

Thus for every function \(\eta(m)=m^{o(1)}\), the proposed global
directional compensation estimate

\[
 \sum_wH_w\ \le\ \eta(m)
 \left(p\sum_we_w+\sum_wM_w^2\right)              \tag{0.3}
\]

fails along this family.  This closes the exact remaining scope in
Section 5 of the earlier no-go note.

This does **not** disprove the ambient centroid target
\(|\mathcal H_A|\le m^{o(1)}(k^3+m^2)\): here the deliberately enlarged
height makes the \(m^2\) term enormous.  It proves that the ambient target
cannot be reached through (0.3), even after inserting an arbitrary
subpolynomial loss.

The only external input is the classical dimension-one lower-bound
fundamental lemma of the linear sieve, in the explicit specialization
stated in Section 2.  All algebraic and geometric steps are elementary.

## 1. Balanced transform and the content identity

Let \(P_p\) be the least-residue modular parabola on an odd prime \(p\),
and put

\[
 L_t=\begin{pmatrix}t&-1\\1&t+1\end{pmatrix},
 \qquad \Delta(t)=\det L_t=t^2+t+1.                \tag{1.1}
\]

For a primitive direction \(w=(a,b)\), write

\[
 L_tw=(X,Y)=(ta-b,\ a+(t+1)b),
 \qquad c_w(t)=\gcd(X,Y),                           \tag{1.2}
\]

and define the positive Eisenstein norm

\[
 Q(w)=a^2+ab+b^2.                                   \tag{1.3}
\]

Two exact identities are

\[
 \begin{aligned}
  (t+1)X+Y&=\Delta(t)a,\\
  -X+tY&=\Delta(t)b,\\
  aY-bX&=Q(w).
 \end{aligned}                                      \tag{1.4}
\]

It follows that

\[
 c_w(t)\mid\gcd(\Delta(t),Q(w)).                    \tag{1.5}
\]

Every active primitive direction of \(P_p\) has
\(|a|,|b|\le p-1\), hence

\[
 0<Q(w)\le3(p-1)^2<3p^2.                            \tag{1.6}
\]

Therefore the single roughness condition

\[
 \Delta(t)\text{ has no prime divisor below }4p^2  \tag{1.7}
\]

implies \(c_w(t)=1\) simultaneously for every active direction.  This
is stronger than the requested aggregate content estimate: it gives
exact simultaneous primitivity without CRT.

## 2. The rough-value sieve

We use the following standard specialization of the lower-bound
fundamental lemma.

**Linear-sieve lemma.**  There are absolute constants \(c>0\) and
\(X_0\) such that, whenever \(X\ge X_0\) and
\(2\le z\le X^{1/8}\),

\[
 \#\left\{X/2<t\le X:
   \gcd(t^2+t+1,\prod_{\ell<z}\ell)=1\right\}
 \ge {cX\over\log z}.                               \tag{2.1}
\]

Here and below \(\ell\) denotes a prime.  For completeness, the exact
sieve data are as follows.  If

\[
 \rho(d)=\#\{r\pmod d:r^2+r+1\equiv0\pmod d\}
\]

for squarefree \(d\), then \(\rho\) is multiplicative and

\[
 \rho(3)=1,qquad
 \rho(\ell)=
 \begin{cases}
  2,&\ell\equiv1\pmod3,\\
  0,&\ell\equiv2\pmod3.
 \end{cases}                                        \tag{2.2}
\]

On the interval \((X/2,X]\), the number of \(t\) in any of these
\(\rho(d)\) residue classes is

\[
 {X\over2}{\rho(d)\over d}+O(\rho(d)).              \tag{2.3}
\]

Mertens' theorem in the two reduced residue classes modulo \(3\) gives

\[
 \prod_{\ell<z}\left(1-\frac{\rho(\ell)}\ell\right)
 \asymp {1\over\log z},                             \tag{2.4}
\]

so this is a dimension-one sieve.  Apply the lower-bound fundamental
lemma with level \(D=X^{1/2}/(\log X)^4\).  Since
\(\log D/\log z>3\) for all sufficiently large \(X\) when
\(z\le X^{1/8}\), its lower sifting function is positive.  The total
remainder is bounded by

\[
 \sum_{d<D}\rho(d)\le D(1+\log D)=o(X/\log z),       \tag{2.5}
\]

where the displayed elementary upper bound can harmlessly be replaced
by \(D(1+\log D)^2\); either is more than sufficient.  Equations
(2.3)--(2.5) give (2.1).  Thus the invoked sieve theorem is being used
only in its routine fixed-dimension, fixed-sifting-ratio range.

Now take

\[
 z=4p^2,qquad X=z^8=(4p^2)^8.                       \tag{2.6}
\]

The lemma supplies \(\gg X/\log p\) parameters \(t\in(X/2,X]\)
satisfying (1.7).

## 3. Avoiding all Euclidean distance collisions

For a base difference \(q=(x,y)\),

\[
 |L_tq|^2
 =t^2(x^2+y^2)+2ty^2+(x^2+2xy+2y^2).              \tag{3.1}
\]

The three coefficients in (3.1) determine \(q\) up to sign: equality
first gives \(y^2=y'^2\) and \(x^2=x'^2\), and the constant term then
gives \(xy=x'y'\).  The modular parabola is integer vector-Sidon, so
two distinct unordered edges have differences not equal up to sign.
Consequently each pair of distinct unordered edges forbids at most two
integer values of \(t\).  There are fewer than \(p^4/4\) such pairs, so
fewer than \(p^4/2\) bad parameters altogether.

Since \(X/\log p\gg p^{16}/\log p\), for every sufficiently large prime
\(p\) one may choose a sifted \(t\in(X/2,X]\) outside all distance-bad
values.  Then

\[
 A_p=L_tP_p                                           \tag{3.2}
\]

is genuinely Euclidean distance-Sidon, and (1.5)--(1.7) show that every
active transformed direction is primitive.

After translation into the positive quadrant, its coordinate height is

\[
 m_p\le(t+2)p=O(p^{17}).                             \tag{3.3}
\]

## 4. Directional budget and centroid mass

Let \(s=\|w\|_\infty\).  If \(|a|=s\), then
\(|ta-b|\ge(t-1)s\); if \(|b|=s\), then
\(|a+(t+1)b|\ge ts\).  Because \(L_tw\) is primitive and
\(m_p\le(t+2)p\),

\[
 M_{L_tw}\le {4p\over s}.                            \tag{4.1}
\]

There are at most \(4s\) primitive unoriented directions of sup-norm
\(s\).  Therefore

\[
 \sum_wM_w^2\le64p^2\sum_{s\le p}{1\over s}
 =O(p^2\log p).                                      \tag{4.2}
\]

The invertible linear map preserves direction occupancies, so

\[
 \sum_we_w=\binom p2.                                \tag{4.3}
\]

The exact integer triple sums of \(P_p\) occupy fewer than \(9p^2\)
cells.  The established clean-collision count therefore gives
\(|\mathcal H_{P_p}|=\Omega(p^4)\), and an invertible linear map
preserves this hypergraph.  Finally the exact directional identity
\(\sum_wH_w=3|\mathcal H_A|\) yields

\[
 \sum_wH_w=\Omega(p^4).                              \tag{4.4}
\]

Combining (3.3) and (4.2)--(4.4) proves (0.1)--(0.2).
For an arbitrary \(m^{o(1)}\) function \(\eta\),
\(\eta(m_p)=p^{o(1)}\), while the ratio in (0.2) is \(\Omega(p)\).
This proves the failure of (0.3).

## 5. What this rules out

The polynomial-height construction rules out every proof architecture
whose final global step is a bound of the form

\[
 \sum_wH_w\le m^{o(1)}
 \left(k\sum_we_w+\sum_wM_w^2\right),               \tag{5.1}
\]

even if directions absent from most hyperedges are allowed to pay.  In
particular, neither a canonical assignment to a constituent direction
nor a nonlocal search for a hidden active short direction can repair the
directional midpoint lane.

What remains logically possible is an endpoint-sensitive ambient charge
that uses information lost by the summaries \((e_w,M_w)\), or a charge
directly to the ambient \(m^2\) term.  The present construction is not a
counterexample to such a theorem.

## 6. Verification

Run

    python3 phase2/loop/erdos1208/verify_polynomial_height_balanced_sieve_no_go.py

The verifier checks the exact transform/content identities, the local
root counts (2.2), symbolic separation, the roughness-to-primitivity
implication, and explicit genuine sifted certificates for
\(p=7,11,13,17\).  The asymptotic lower-bound fundamental lemma itself
is a classical analytic theorem and is not replaced by finite testing.
