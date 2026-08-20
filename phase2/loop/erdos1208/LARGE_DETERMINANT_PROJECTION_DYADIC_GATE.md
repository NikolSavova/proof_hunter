# Large-determinant matching hyperedges: a projection-energy dyadic gate

## Status

Let \(A\subset[m]^2\) be distance-Sidon, \(k=|A|\), and let
\(\mathcal H_A\) be the endpoint-labelled matching hypergraph from
AMBIENT_CENTROID_ENDPOINT_DIFFERENCE_HYPERGRAPH_GATE.md.  Thus a
hyperedge consists of three endpoint-disjoint directed differences
\(q_1,q_2,q_3\in(A-A)\setminus\{0\}\) with
\(q_1+q_2+q_3=0\).

For \(D\ge1\), let

\[
 \mathcal H_A[D,2D)
 =\{h\in\mathcal H_A:D\le|\det(q_1,q_2)|<2D\}.          \tag{0.1}
\]

This note proves the following determinant-band theorem.

\[
 \boxed{
 |\mathcal H_A[D,2D)|
 \le {2\sqrt{2D}\over3}\,
       \mathcal Z(A)
 \le {\sqrt{6D}\over3}\,[k(k-1)]^{3/2},}               \tag{0.2}
\]

where the endpoint-sensitive directional functional is

\[
 \mathcal Z(A)=\sum_{w\in\mathcal W(A)}\sqrt{e_wE_w}.   \tag{0.3}
\]

Here \(\mathcal W(A)\) is the set of primitive unoriented directions of
edges of \(A\), \(e_w\) is the number of unordered \(A\)-edges parallel
to \(w\), and

\[
\begin{aligned}
 B_w(r)&=|\{q\in(A-A)\setminus\{0\}:\det(w,q)=r\}|,\\
 E_w&=\sum_rB_w(r)^2.                                  \tag{0.4}
\end{aligned}
\]

The proof is a genuine determinant lattice-coset/projection argument.  It
also retains the complete endpoint structure:

\[
 B_w(r)=\sum_s a_w(s)a_w(s+r)-k\,1_{r=0},              \tag{0.5}
\]

where \(a_w(s)=|\{a\in A:\det(w,a)=s\}|\).

Two consequences are useful.

* A **fixed nonzero determinant** has load \(O(k^3)\).
  More generally, every union of \(m^{o(1)}\) bands with
  \(D\le m^{o(1)}\) has the required
  \(m^{o(1)}(k^3+m^2)\) load.
* A union of dyadic bands \(\mathscr B\) is closed whenever

  \[
   \mathcal Z(A)\sum_{D\in\mathscr B}\sqrt D
   \le m^{o(1)}(k^3+m^2).                              \tag{0.6}
  \]

This is a rigorous dyadic reduction, but not a full solution.  The
universal estimate \(\mathcal Z(A)\ll k^3\) makes (0.2) grow like
\(k^3\sqrt D\), so it does not by itself sum through determinants of
polynomial size in the hard low-height regime.

That limitation is sharp.  Integral finite-field parabola lifts, followed
by determinant-one Euclideanizing shears, give genuine polynomial-height
distance-Sidon sets for which some dyadic band with \(D\le O(k^2)\)
contains \(\Omega(k^4/\log k)\) matching hyperedges.  Since
\(k^3\sqrt D\le O(k^4)\), no uniform improvement by a fixed power of \(k\)
is possible without introducing an additional ambient-height input.

Thus the remaining theorem is now precise: control the high-\(D\) bands
by coupling \(\mathcal Z(A)\), or its band-restricted version, to \(m^2\).
Projection energy alone bottoms out at the sheared-parabola scale.

## 1. Active directions and determinant fibres

Put

\[
 \mathscr D=(A-A)\setminus\{0\},\qquad N=|\mathscr D|=k(k-1). \tag{1.1}
\]

For \(w\in\mathcal W(A)\), let

\[
 T_w=\{g\ge1:gw\in\mathscr D\}.
\]

Because \(\mathscr D\) is symmetric, its elements parallel to \(w\) are
exactly \(\{\pm gw:g\in T_w\}\), and

\[
 |T_w|=e_w,\qquad \sum_we_w={N\over2}.                 \tag{1.2}
\]

For a dyadic band, define the multiplicative interval load

\[
 \alpha_{w,D}(r)
 =|\{g\in T_w:D\le g|r|<2D\}|.                         \tag{1.3}
\]

The number \(P_D\) of ordered pairs \((q_1,q_2)\in\mathscr D^2\) with
determinant in the band is exactly

\[
 P_D
 =2\sum_{w\in\mathcal W(A)}\sum_r
       \alpha_{w,D}(r)B_w(r).                          \tag{1.4}
\]

The factor two chooses \(q_1=gw\) or \(q_1=-gw\).  Every hyperedge in
\(\mathcal H_A[D,2D)\) supplies six ordered choices of two of its three
vertices, all with the same absolute determinant.  Hence

\[
 6|\mathcal H_A[D,2D)|\le P_D.                         \tag{1.5}
\]

Notice that (1.5) only discards the forced condition
\(-q_1-q_2\in\mathscr D\) and the six-endpoint matching decoration.  All
arithmetic before that discard remains exact.

## 2. Multiplicative interval packing

### Lemma 2.1

For every finite \(T\subset\mathbb Z_{>0}\) and \(D\ge1\), if

\[
 \alpha_D(r)=|\{g\in T:D\le g|r|<2D\}|,
\]

then

\[
 \boxed{\sum_{r\in\mathbb Z}\alpha_D(r)^2\le8D|T|.}     \tag{2.1}
\]

### Proof

Expand the square and fix \(g,h\in T\).  A common positive \(|r|\)
requires

\[
 D\le g|r|,h|r|<2D.
\]

It follows that \(\max(g,h)<2\min(g,h)\).  The number of signed nonzero
integers \(r\) is at most \(4D/\max(g,h)\).

Assign an ordered comparable pair to its larger member \(g\).  There are
at most \(g\) positive integers \(h\le g\), and reversing unequal pairs
costs at most a factor two.  Therefore

\[
 \sum_{\substack{g,h\in T\\
                  \max(g,h)<2\min(g,h)}}
 {1\over\max(g,h)}
 \le2|T|.
\]

Multiplying by \(4D\) proves (2.1). \(\square\)

Applying Lemma 2.1 to \(T_w\) and Cauchy--Schwarz in (1.4) gives

\[
\begin{aligned}
 P_D
 &\le2\sum_w
   \left(\sum_r\alpha_{w,D}(r)^2\right)^{1/2}
   \left(\sum_rB_w(r)^2\right)^{1/2}\\
 &\le4\sqrt{2D}\sum_w\sqrt{e_wE_w}
 =4\sqrt{2D}\,\mathcal Z(A).                           \tag{2.2}
\end{aligned}
\]

Combining (2.2) with (1.5) proves the first inequality in (0.2).

For one fixed \(d\ne0\), replace (1.3) by

\[
 \alpha_{w,d}(r)=|\{g\in T_w:g|r|=|d|\}|.
\]

For each signed \(r\), there is at most one possible \(g\), and summing
over \(r\) gives

\[
 \sum_r\alpha_{w,d}(r)^2\le2e_w.                       \tag{2.3}
\]

The same proof yields

\[
 |\{h\in\mathcal H_A:|\det h|=|d|\}|
 \le{\sqrt2\over3}\mathcal Z(A)=O(k^3).                \tag{2.4}
\]

Thus the obstruction is aggregation over many determinant cells, not
pointwise multiplicity of one cell.

## 3. The global projection-energy identity

The endpoint formula (0.5) is immediate.  A vector \(q=b-a\) satisfies
\(\det(w,q)=r\) exactly when the two endpoint levels differ by \(r\).
For \(r=0\), the \(k\) diagonal choices \(a=b\) must be removed.

There is also an exact geometric interpretation of \(E_w\).  Since
\(\sum_rB_w(r)=N\),

\[
 E_w=N+2L_w,                                           \tag{3.1}
\]

where \(L_w\) is the number of unordered pairs of distinct points of
\(\mathscr D\) lying on a common line parallel to \(w\).  Every unordered
pair of points of \(\mathscr D\) has one difference direction, so

\[
 \sum_{w\in\mathcal W(A)}L_w\le{N\choose2}.             \tag{3.2}
\]

Also \(|\mathcal W(A)|\le\sum_we_w=N/2\).  Consequently

\[
 \boxed{
 \sum_{w\in\mathcal W(A)}E_w
 \le {N^2\over2}+N(N-1)<{3N^2\over2}.}                 \tag{3.3}
\]

Cauchy--Schwarz, (1.2), and (3.3) now give

\[
 \mathcal Z(A)
 \le\left(\sum_we_w\right)^{1/2}
      \left(\sum_wE_w\right)^{1/2}
 <{\sqrt3\over2}N^{3/2}.                               \tag{3.4}
\]

Substituting (3.4) into the first half of (0.2) proves the universal
determinant-band estimate.

The standard endpoint convolution bound supplies another check:

\[
 E_w\le k^2(k+2e_w).                                   \tag{3.5}
\]

Indeed the full level autocorrelation is \(a_w*\widetilde a_w\), and
Young's inequality gives
\(\|a_w*\widetilde a_w\|_2\le\|a_w\|_1\|a_w\|_2\), with
\(\|a_w\|_1=k\) and \(\|a_w\|_2^2=k+2e_w\).  Removing the diagonal at
zero cannot increase the \(L^2\) norm.  Formula (3.5) can improve
\(\mathcal Z(A)\) in direction-heavy subfamilies, but its universal sum
does not beat (3.4).

## 4. Sharpness up to logarithms

Let \(p\) be an odd prime and use least nonnegative representatives

\[
 P_p=\{(x,[x^2]_p):0\le x<p\}\subset[0,p-1]^2.          \tag{4.1}
\]

This is integer vector-Sidon.  Indeed, equality of two directed
differences gives, modulo \(p\), both the difference and the sum of the
two first coordinates; since \(p\) is odd, it recovers both ordered
endpoints.  There are \(R=\binom p3\) unordered
triples and fewer than \(9p^2\) exact integer sum cells, so

\[
 \sum_st_s(t_s-1)\ge {R^2\over9p^2}-R=\Omega(p^4).      \tag{4.2}
\]

Different triples in one sum cell are disjoint: after cancelling a
shared point, equality of the remaining pair sums would contradict
vector-Sidonicity unless those pairs, and hence the triples, were equal.
Choose one canonical matching between every ordered pair of distinct
triples in a sum cell.  Its three directed endpoint differences form a
hyperedge and recover the ordered triple pair.  Hence the endpoint
matching hypergraph has \(\Omega(p^4)\) hyperedges.

Only \(O(p^2\log p)\) of these can have determinant zero.  To see this,
let \(e_w\) count the unordered \(P_p\)-edges parallel to primitive \(w\),
with \(q=\|w\|_\infty\).  Vector-Sidonicity makes the positive scalar
multiples distinct, so \(e_w\le(p-1)/q\).  There are at most \(4q\)
directions of sup-norm \(q\), and the collinear argument gives

\[
 |\mathcal H_{P_p}^{\rm col}|
 \le {2\over3}\sum_we_w^2=O(p^2\log p).                \tag{4.3}
\]

Every nonzero determinant has absolute value at most \(2(p-1)^2\).
There are \(O(\log p)\) dyadic bands.  By pigeonhole, one band
\([D,2D)\), with \(D\le2p^2\), contains

\[
 \Omega\left({p^4\over\log p}\right)                   \tag{4.4}
\]

matching hyperedges.

Finally apply the determinant-one shear

\[
 S_t(x,y)=(x+ty,y).
\]

For every two distinct unordered edges, equality of their squared
lengths after applying \(S_t\) is a nonzero polynomial of degree at most
two in \(t\).  (If it vanished identically, their vectors would agree up
to sign.)  There are \(O(p^4)\) edge pairs, hence only \(O(p^4)\) bad
integer values of \(t\).  Choosing a nonnegative integer
\(t=O(p^4)\) outside them makes \(S_tP_p\) Euclidean distance-Sidon.  The shear
preserves exact centroid equalities, endpoint cleanliness, and every
determinant.  Thus (4.4) holds for genuine distance-Sidon sets of
polynomial height.

For that band, \(k=p\), \(D\le2k^2\), and

\[
 k^3\sqrt D=O(k^4).                                    \tag{4.5}
\]

Therefore the power dependence in (0.2) is sharp up to a logarithm within
the genuine endpoint-realized category.  Any completion must use the
actual height of the Euclideanizing metric, not just the determinant
projection incidence.

## 5. The exact remaining large-area gate

The new live target is a height-sensitive improvement of (0.2).  One
sufficient form is

\[
 \sum_{\text{dyadic }D}
 \sqrt D\,\mathcal Z_D(A)
 \le m^{o(1)}(k^3+m^2),                                \tag{5.1}
\]

where \(\mathcal Z_D\) may retain the band-restricted projection energies
instead of the full \(E_w\).  The unrestricted choice
\(\mathcal Z_D=\mathcal Z\) is what was proved above and is sharp without
height.

Three facts constrain a continuation:

1. fixed determinant cells are already \(O(k^3)\);
2. the complete active-direction projection budget is already
   \(O(k^4)\), by (3.3);
3. finite-field/Singer-type endpoint designs can place fourth-order mass
   into determinants \(D\le O(k^2)\).

Thus neither polynomial partitioning of the raw projection incidences nor
an unweighted sum of (0.2) can finish.  A successful theorem must show
that simultaneous saturation across many large determinant bands forces
the Euclideanizing transformation, and hence the ambient box, to be large
enough to pay through \(m^2\).

## 6. Verification

Run

    python3 phase2/loop/erdos1208/verify_large_determinant_projection_dyadic_gate.py

The verifier checks (0.5), the exact projection-energy identities,
the global energy budget, multiplicative interval packing, every dyadic
band on genuine small certificates, and the full determinant/profile
audit for the sheared \(p=43\) parabola.
