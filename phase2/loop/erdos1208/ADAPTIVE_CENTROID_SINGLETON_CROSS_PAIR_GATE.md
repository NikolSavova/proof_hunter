# Adaptive paired mass: centroid singleton structure and the quota-cross repair

## Status

The all-pairs functional

\[
 \mathcal P_{\rm ad}
 =\sum_q{1\over h_q}\sum_{i<j}\min(U_{q,i},U_{q,j})       \tag{0.1}
\]

is a valid sufficient majorant for the adaptive tail, but it is not the
right object for an endpoint-structure inverse theorem.  This note proves
three exact statements.

1. **Quota-cross identity.**  If
   \(U_{q,1}\ge\cdots\ge U_{q,e_q}\) and the first \(b_q\) occurrences are
   discarded, then

   \[
    \boxed{
    \sum_{j>b_q}U_{q,j}
    ={1\over b_q}
      \sum_{\substack{1\le i\le b_q\\b_q<j\le e_q}}
          \min(U_{q,i},U_{q,j})}                         \tag{0.2}
   \]

   whenever the tail is nonempty; both sides are zero when \(b_q\ge e_q\).
   Thus the adaptive lift has an **exact** top-versus-tail witness expansion.
   The top--top and tail--tail pairs inserted by (0.1) are unnecessary.

2. **Centroid singleton theorem.**  Equal-sum triple classes are matchings.
   For a fixed anchor \(q=a-b\), every clean start is a centroid class
   containing \(a\) and \(b\) in different triples.  If
   \(p=(s,t)\) is head-isolated at \(a\), the two associated companion
   point sets intersect in exactly the singleton \(\{b\}\).  Hence the
   isolated occurrence graph in one fibre is an induced subgraph of an
   explicit disjointness graph.

3. **Genuine endpoint barrier.**  For every \(n\) there is a
   polynomial-height integral distance-Sidon set with

   \[
      k=2n+4,\qquad h_q=n,                               \tag{0.3}
   \]

   in which **every pair** of the \(n\) displayed starts has \(q\) as an
   isolated common translation.  Its companion sets form a sunflower with
   core \(\{b\}\), so the singleton-intersection graph is \(K_n\).  The
   unweighted analogue of (0.1) is \(\Theta(k^3)\), one full factor \(k\)
   above the desired \(k^2\) scale.

The construction in item 3 does **not** make every source pair selected by
one determinant-rich metric wedge.  It is therefore not a counterexample
to the adaptive estimate.  It is a rigorous no-go for the proposed
endpoint-only dichotomy: dense isolated common-\(q\) mass need not contain a
multi-translation separable block, and genuinely nonseparable endpoint
designs can already be complete at polynomial height.  Any continuation
must retain the metric loads and the quota-cross distinction in (0.2).

## 1. Exact quota-cross pairing

Fix \(q\), abbreviate \(b=b_q\), and suppose first that \(b<e_q\).  For
every \(i\le b<j\), monotonicity gives

\[
 \min(U_{q,i},U_{q,j})=U_{q,j}.                          \tag{1.1}
\]

Each tail load occurs once for each of the \(b\) top indices, proving
(0.2).  If \(b\ge e_q\), the tail and the displayed cross sum are both
empty.

Summing gives the exact identity

\[
 \boxed{
 X_{\rm ad}
 =\sum_q{1\over b_q}
   \sum_{\substack{i\le b_q\\j>b_q}}
      \min(U_{q,i},U_{q,j}).}                            \tag{1.2}
\]

By contrast, the all-pairs sum in (0.1) decomposes as

\[
 \sum_{i<j}\min(U_i,U_j)
 =\sum_{i<j\le b}\min(U_i,U_j)
   +b\sum_{j>b}U_j
   +\sum_{b<i<j}\min(U_i,U_j).                          \tag{1.3}
\]

The first term can be arbitrarily large while the adaptive tail is empty.
Consequently an inverse theorem for (0.1) is required to explain structure
which the desired charge never needed.  Formula (1.2) identifies the
minimal decorated object: one retained occurrence, one quota occurrence
above it, and their common literal translation.

There is an equivalent layer form.  Put

\[
 E_q(t)=|\{i:U_{q,i}\ge t\}|.                           \tag{1.4}
\]

At height \(t\), the number of top--tail pairs is

\[
 b_q(E_q(t)-b_q)_+,                                      \tag{1.5}
\]

so division by \(b_q\) and summation over \(t\) recovers
\(\sum_t(E_q(t)-b_q)_+\), exactly the tail load.

## 2. Equal-centroid representation of clean fibres

For an integer vector \(z\), let

\[
 \mathscr T_z
 =\{T\in{A\choose3}:\sum_{x\in T}x=z\}.                \tag{2.1}
\]

### Lemma 2.1 (centroid classes are matchings)

Distinct triples in \(\mathscr T_z\) are disjoint.

Indeed, if two equal-sum triples shared a point, cancellation would give
two equal unordered pair sums.  A distance-Sidon set has unique unordered
pair sums: an equality \(x+y=u+v\) gives
\(x-u=v-y\), and vector/distance uniqueness forces the pairs to agree.
Thus the original triples would be equal.

In particular, a point \(a\) belongs to at most one triple of a fixed
class.  When it belongs, denote that triple by \(T_z(a)\) and define its
companion set

\[
 C_z(a)=\bigcup_{T\in\mathscr T_z\setminus\{T_z(a)\}}T. \tag{2.2}
\]

If \(m_z=|\mathscr T_z|\), then

\[
 |C_z(a)|=3(m_z-1).                                      \tag{2.3}
\]

### Lemma 2.2 (clean-row parametrization)

Fix distinct \(a,b\) and \(q=a-b\).  There is a bijection

\[
 \boxed{
 H_q\longleftrightarrow
 Z_{a,b}:=\{z:b\in C_z(a)\},\qquad s\longmapsto z=s+a.} \tag{2.4}
\]

Under this bijection,

\[
 E(s)=T_z(a)\setminus\{a\},\qquad
 E(s+q)=T_z(b)\setminus\{b\}.                          \tag{2.5}
\]

To prove this, a clean row

\[
 a+E(s)=b+E(s+q)                                        \tag{2.6}
\]

is precisely a pair of disjoint equal-sum triples, with distinguished
points \(a\) and \(b\).  Conversely such a triple pair gives (2.6) and all
six cleanliness conditions.

### Proposition 2.3 (head isolation is singleton intersection)

Let \(p=(s,t)\), let \(q=a-b\in Q_p\), and put

\[
 z=s+a,\qquad z'=t+a.                                   \tag{2.7}
\]

Then the number of common translations in \(Q_p\) with directed head
\(a\) is exactly

\[
 \boxed{d^+_{Q_p}(a)=|C_z(a)\cap C_{z'}(a)|.}           \tag{2.8}
\]

Indeed, a point \(c\) lies in this intersection exactly when both starts
are clean under the anchor \(a-c\), by Lemma 2.2.  The map
\(c\mapsto a-c\) is injective.  Since \(b\) belongs to the intersection,
head isolation of \(q\) is equivalent to

\[
 \boxed{C_z(a)\cap C_{z'}(a)=\{b\}.}                   \tag{2.9}
\]

Thus, for fixed \(q=a-b\), the head-isolated source-pair graph has vertex
set \(Z_{a,b}\), with a possible edge \(zz'\) only when the two petals

\[
 C_z(a)\setminus\{b\},\qquad C_{z'}(a)\setminus\{b\}   \tag{2.10}
\]

are disjoint.  The metric selector and tail condition take a subgraph of
this exact singleton-intersection graph.

One immediate sharp capacity fact is worth recording.  A clique of size
\(r\) in this graph has pairwise-disjoint petals.  Every petal has at least
two points, namely the two other points in the triple containing \(b\).
Therefore

\[
 \boxed{r\le\left\lfloor{k-2\over2}\right\rfloor.}    \tag{2.11}
\]

This is only linear, not subpolynomial.  The next section shows that linear
cliques are genuinely realizable at polynomial height.

## 3. A genuine complete singleton-intersection design

Fix free vector parameters

\[
 A,B,C,X_0,\ldots,X_n                                  \tag{3.1}
\]

and define formal points

\[
 a=A,\qquad b=B,\qquad
 x_i=X_i,\qquad y_i=C+i(A-B)-X_i\quad(0\le i\le n).    \tag{3.2}

Put \(E_i=\{x_i,y_i\}\).  Their pair sums are

\[
 \sigma_i=x_i+y_i=C+i(A-B).                             \tag{3.3}

Consequently, for \(q=a-b=A-B\),

\[
 \sigma_i+q=\sigma_{i+1}\quad(0\le i<n),              \tag{3.4}
\]

and hence

\[
 a+E_i=b+E_{i+1}.                                       \tag{3.5}

All formal point labels in (3.5) are distinct.  Thus

\[
 H_q=\{E_0,\ldots,E_{n-1}\}                            \tag{3.6}

at the level of formal identities.

The corresponding centroid class has exactly the two triples

\[
 \{a,x_i,y_i\},\qquad\{b,x_{i+1},y_{i+1}\}.           \tag{3.7}

Therefore

\[
 C_{z_i}(a)=\{b,x_{i+1},y_{i+1}\},                     \tag{3.8}
\]

and these companion sets meet pairwise exactly in \(\{b\}\).  Proposition
2.3 says that \(q\) is head-isolated for every pair of displayed starts.
A direct coefficient comparison also shows that no other common anchor
shares the head \(a\) or tail \(b\); hence \(q\) is fully isolated.  In
fact, the only other formal common translation for an internal pair is the
reverse \(-q\), whose anchor is \((b,a)\), so it does not spoil either
isolation degree of \((a,b)\).

### 3.1 Formal Sidonicity

The point forms in (3.2) are vector-Sidon over the free module: all ordered
differences are distinct.  This follows by first comparing the coefficient
of \(C\), which is \(-1,0\), or \(1\).  Within a fixed value, the signed
\(X_i\)-support recovers the ordered indices; the remaining coefficients of
\(A,B\) recover the type.  The same comparison shows that all unordered
pair sums are distinct.

It follows that an equality of two squared edge lengths is not a formal
identity unless the unordered edges agree.  Indeed, the coefficient vectors
of two formal directed edges are not equal up to sign, so the difference of
their squared norms is a nonzero quadratic polynomial in the scalar
coordinates of the free vector parameters.

Exclude all unintended point collisions, pair-sum identities, triple-sum
identities, and squared-distance identities.  There are only \(n^{O(1)}\)
nonzero polynomials, of degree at most two.  Applying the elementary grid
nonvanishing lemma to their product gives an integral specialization with
coordinates \(n^{O(1)}\).  A final translation puts the points in an
integer square of polynomial side length.  The intended identities (3.5)
remain, while the coefficient audit ensures that (3.6) and the isolation
claims acquire no accidental additions.

The resulting set has

\[
 k=2+2(n+1)=2n+4,qquad h_q=n.                           \tag{3.9}
\]

Its graph of unordered isolated source pairs in the fibre is \(K_n\), with

\[
 e_q={n\choose2}.                                       \tag{3.10}
\]

Thus the unweighted all-pairs proxy is

\[
 {1\over h_q}{e_q\choose2}=\Theta(n^3)=\Theta(k^3).    \tag{3.11}
\]

This is an actual distance-Sidon endpoint realization of the factor-\(k\)
incidence barrier.  It improves the abstract \(K_{n,n}\) warning in
`ADAPTIVE_AREA_CELL_CARTESIAN_REUSE_GATE.md`: no failure of endpoint
realizability is needed to create a complete singleton-intersection graph.

What is absent is equally precise.  The squared lengths \(\delta(E_i)\)
are generic, so (3.10) is not asserted to lie in the shift set of one fixed
determinant-rich physical wedge.  The surviving restriction is metric,
not combinatorial.

## 4. Consequence for the adaptive route

The target

\[
 \mathcal P_{\rm ad}\le m^{o(1)}k^2                   \tag{4.1}
\]

may still conceivably follow from the full metric selector, but it cannot
follow from a dichotomy between separable endpoint blocks and sparse
nonseparable designs.  Section 3 is dense, nonseparable in the required
multi-translation sense, integral, distance-Sidon, and polynomial-height.

The exact restart is (1.2).  A witness now consists of

\[
 (p_{\rm top},p_{\rm tail},q),                          \tag{4.2}
\]

where both source pairs are singleton-intersection edges in the centroid
set system of Section 2, while the tail pair carries a determinant-rich
scalar gap.  A useful next theorem must exploit at least one of:

1. the four centroid classes attached to the two singleton-intersection
   edges;
2. the two scalar gaps and their signed-area supports;
3. the fact that the top set has the adaptive size
   \(b_q\asymp k^2h_q/H_Q\); or
4. aggregation across many comparable fibres, which the single-chain
   construction does not provide.

Ordinary dependent random choice on the occurrence graph, or an endpoint
sunflower bound without the metric labels, cannot distinguish the genuine
chain barrier from a forbidden adaptive tail.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_adaptive_centroid_singleton_cross_pair_gate.py
```

The verifier:

* exhausts the formal coefficient model for \(2\le n\le12\), checking
  vector-Sidonicity, pair-sum uniqueness, the exact forward and reverse
  clean fibres, and isolation of every displayed source pair;
* constructs every formal triple-sum class and verifies the companion
  sunflower and singleton intersections;
* exhausts the quota-cross identity on all load sequences of length at most
  seven with entries at most five; and
* gives a deterministic 16-point integral distance-Sidon certificate with
  a six-start fibre and all fifteen source pairs isolated at the displayed
  anchor.
