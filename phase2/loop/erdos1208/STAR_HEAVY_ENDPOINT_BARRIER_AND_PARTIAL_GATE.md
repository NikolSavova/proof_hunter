# Star-heavy fibres: a genuine endpoint barrier and a partial gate

## 1. Outcome

Let `H_q` be a clean fibre of size `h`.  Its source graph and translated
target graph have the same edge set, with

\[
 \tau_q(\{c,d\})=\{e,f\},\qquad e+f=c+d+q.                \tag{1.1}
\]

The bi-matching reduction in `TRACE_AREA_BIMATCHING_BLOCK_GATE.md` closes
the balanced regime in which the largest endpoint degree satisfies
`Delta=O(h/k)`.  This note settles what can and cannot be obtained from a
source star in the complementary regime.

There are three durable conclusions.

1. **The degree imbalance is genuinely realizable.**  There is an
   infinite family of integral distance-Sidon configurations, of
   polynomial height, with a heavy clean fibre `h>k` and
   \[
    {\Delta\over h/k}\longrightarrow\infty.              \tag{1.2}
   \]
   Consequently common translation does not balance the endpoint degrees,
   and many records at a hub do not by themselves force a repeated
   Euclidean distance.  The abstract heavy obstruction in the preceding
   note can be made endpoint-realized.

2. **A source star can contain a genuine dense trace--area patch.**  An
   exact 30-point distance-Sidon certificate has `h_q=9`, all nine source
   edges through one point, pairwise-disjoint clean targets, and a
   `K_{3,3}` in its trace--area support.  Thus star-to-matching does not
   imply support acyclicity, two-degeneracy, or exact diagonal behavior.

3. **One whole Gaussian collision branch is automatically acceptable.**
   After splitting a source star into its two canonical-orientation halves,
   the number of off-diagonal Gaussian collisions in which the two
   ordinary edges meet is at most
   \[
    8ks^2                                                   \tag{1.3}
   \]
   for a star of size `s`.  Across edge-disjoint star pieces this is
   `O(k^2h)=O(Nh)`.  The only unbounded star-local Gaussian term uses four
   distinct ordinary-edge endpoints.

The star-heavy lane therefore does not collapse to a degree theorem.  Its
sharp remaining core is a four-distinct-endpoint resonance, just as in the
scalar lane.  A hybrid charge can finish any decomposition for which this
core and the residual bi-matching adaptive envelopes have diagonal-scale
total energy.

## 2. A genuine heavy fibre with an arbitrarily dominant hub

### 2.1 A dense clean-fibre core

Let `p` be prime and take the modular parabola

\[
 P_p=\{(x,x^2\bmod p):0\le x<p\}\subset\mathbb Z^2.       \tag{2.1}
\]

It is vector-Sidon.  Indeed, equality of two directed differences first
determines the nonzero difference of the first coordinates modulo `p`;
the difference of the second coordinates then determines their sum, and
hence both endpoints.

There are

\[
 T=\binom p3                                                \tag{2.2}
\]

unordered triples, and fewer than `9p^2` possible integer triple sums.
Pair sums are injective, so two distinct triples with the same sum are
disjoint.  If `r(z)` is the triple-sum load, the number `M` of unordered
equal-sum triple pairs satisfies

\[
 M=\sum_z\binom{r(z)}2
 \ge {T^2\over18p^2}-{T\over2}=\Omega(p^4).                \tag{2.3}
\]

Every such pair supplies 18 ordered choices of the two triples and their
distinguished endpoints.  These choices are distributed among fewer than
`p(p-1)` nonzero directed differences.  Hence some clean fibre has

\[
 h_0\ge {18M\over p(p-1)}=\Omega(p^2).                    \tag{2.4}
\]

The modular parabola need not yet be Euclidean distance-Sidon.  Apply the
integer shear

\[
 S_t(x,y)=(x+ty,y).                                        \tag{2.5}
\]

For two difference vectors `v` and `w` which are not equal up to sign,
the equation

\[
 |S_tv|^2=|S_tw|^2                                        \tag{2.6}
\]

is a nonzero polynomial of degree at most two in `t`.  There are
`O(p^4)` pairs to separate, so an integer `t=O(p^4)` avoids all bad roots.
The sheared set is an integral distance-Sidon set of height `O(p^5)`, and
all additive fibres, including (2.4), are unchanged.

### 2.2 Polynomial-avoidance star augmentation

The following elementary extension lemma is useful beyond this note.

**Lemma 2.1 (clean-star augmentation).**  Let `A` be a finite integral
distance-Sidon set and let `q=a-b` be a realized directed difference.  For
every `d>=1`, `A` has a polynomial-height distance-Sidon extension with
new points

\[
 c,\ d_i,e_i,f_i\quad(1\le i\le d)                       \tag{2.7}
\]

such that

\[
 e_i+f_i=c+d_i+q,                                         \tag{2.8}
\]

the new `q`-starts are exactly the `d` edges `{c,d_i}`, and
their clean targets `{e_i,f_i}` form a matching.

### Proof

Choose `c,d_i,e_i` as independent integer variables and put

\[
 f_i=c+d_i+q-e_i.                                         \tag{2.9}
\]

Point coincidences, every unintended equality of two squared distances,
and every unintended pair-sum translation

\[
 x+y+q=z+w                                                \tag{2.10}
\]

are the zero sets of finitely many nonzero polynomials of degree at most
two.  Nonzeroness follows directly from a private variable in (2.9); the
only cancellations with no private variable are old distance equalities
or the prescribed relations (2.8).  There are `O(K^4)` bad polynomials
when the final set has `K` points.

On a scalar grid of side `R`, a nonzero polynomial of degree at most two
in any number of variables has at most `2R^(n-1)` zeros.  Taking
`R>C K^4` leaves a simultaneous good choice.  Equation (2.10) ensures that
the only new starts in `H_q` are the prescribed ones.  A final common
translation puts all points in a nonnegative square.  QED.

Apply Lemma 2.1 to the core above with

\[
 d=\lfloor p^{3/2}\rfloor.                                \tag{2.11}
\]

The extended fibre has

\[
 k'=p+3d+1=\Theta(p^{3/2}),\qquad
 h'=h_0+d=\Omega(p^2),\qquad
 \Delta\ge d.                                             \tag{2.12}
\]

For large `p`, it is heavy, and

\[
 {\Delta\over h'/k'}=\Omega(p).                          \tag{2.13}
\]

Every source-and-target bi-matching coloring needs at least `d` colors,
whereas `h'/k'=Theta(sqrt(p))`.  The construction has height polynomial in
`p` (the proof above gives `O(p^6)`, without optimization).

This is an existence theorem, not merely a role-hypergraph model.  It
rules out the proposed alternative that a sufficiently dominant clean
hub must force an equal Euclidean distance.

### Finite certificate

The verifier starts from the 43-point transformed parabola, whose fibre
`q=(396,-38)` has size 171, and adjoins a clean source star of degree 20.
The result has

\[
 k'=104,\qquad h'_q=191,\qquad\Delta\ge20,qquad
 {\Delta\over h'_q/k'}=10.89\ldots.                       \tag{2.14}
\]

All distances and all `q`-starts are checked exactly.  The newly adjoined
star itself has completely diagonal trace charge on the full set; this
finite example is a degree/block-count barrier, not a counterexample to
the adaptive envelope conjecture.

## 3. The star-local Gaussian overlap theorem

Let a source star have center `c` and leaves `d_i`.  Canonically orient
every edge by the fixed lexicographic order.  Split the leaves according
to whether the oriented source vector is

\[
 u_i=c-d_i\quad\hbox{or}\quad u_i=d_i-c.                  \tag{3.1}
\]

This costs only two star pieces.  Within either piece,

\[
 u_i-u_j=\pm(d_j-d_i)                                     \tag{3.2}
\]

is an actual directed point difference.

Put

\[
 \lambda=3(I+J),\qquad
 \Gamma(i,E)=u_i+\lambda v_E,                             \tag{3.3}
\]

where `v_E` is the canonically oriented vector of an arbitrary ordinary
edge.  An off-diagonal collision is

\[
 u_i-u_j=\lambda(v_F-v_E).                                \tag{3.4}
\]

Suppose `E` and `F` meet at `x`, and write their other endpoints as `y,z`.
There are signs `alpha,beta in {+1,-1}` such that

\[
 v_E=\alpha(x-y),\qquad v_F=\beta(x-z).                  \tag{3.5}
\]

If `alpha=beta`, then

\[
 v_F-v_E=\pm(y-z).                                        \tag{3.6}
\]

For fixed `(i,j)`, vector-Sidonicity determines the ordered pair `(y,z)`;
there are at most `k` choices of the common endpoint `x`.

If `alpha=-beta`, then

\[
 v_F-v_E=\pm(2x-y-z).                                     \tag{3.7}
\]

For fixed `x` and a fixed sign, (3.4) determines the pair sum `y+z`.
Pair-sum injectivity determines the unordered pair `{y,z}`.  Including
both signs and both orders costs at most `4k` possibilities.  Thus, with
a harmless uniform allowance for the first case,

\[
 \boxed{C_{\cap}(S)\le8ks^2.}                             \tag{3.8}
\]

Here ordered collisions are counted, so (3.8) directly bounds their
contribution to charge energy.

If edge-disjoint star pieces have sizes `s_j` and contain at most `h`
records in total, then `s_j<=k` gives

\[
 \sum_jC_{\cap}(S_j)
 \le8k\sum_js_j^2
 \le8k^2h=O(Nh).                                         \tag{3.9}
\]

Therefore the only uncontrolled Gaussian star collisions have

\[
 E\cap F=\varnothing.                                    \tag{3.10}
\]

They use the two star leaves and four distinct ordinary-edge endpoints.
This is a genuine six-label linear equation; it is not removed by the
star-to-matching decoration.

On the resonant two-arm stress at side 50, the largest source star splits
as `7+2`.  Its Gaussian energy decomposes exactly as

\[
 44550\quad\text{diagonal}
 \ +124\quad\text{intersecting-edge}
 \ +4208\quad\text{disjoint-edge}.                       \tag{3.11}
\]

Thus the proven term is small there, while the four-distinct endpoint term
is genuinely active.

## 4. A genuine source-star `K_{3,3}`

The local trace--area support is not forced to be a forest.  The verifier
contains a 30-point distance-Sidon set and a clean fibre with nine source
edges through one center.  The nine target edges form a matching.  After
dividing out one common scale, the nine paired source/target vectors have
the following trace and signed area table:

\[
\begin{array}{c|ccc}
 &A=4&A=204&A=444\\ \hline
T=7489 &(1;20,4)&(17;16,12)&(37;14,12)\\
T=11326&(2;25,2)&(34;23,6)&(74;17,6)\\
T=22084&(4;35,1)&(68;31,3)&(148;1,3).
\end{array}                                               \tag{4.1}
\]

As before, `(x;y,z)` records the relative data

\[
 |u|=x,\qquad v=(y,z),\qquad
 T=x^2+18(y^2+z^2),\quad A=xz.                            \tag{4.2}
\]

Unlike the earlier 38-point certificate, the nine source edges here share
one endpoint.  Different equal-norm Gaussian rotations are applied to the
nine records, so the source leaves form a Golomb set in the plane while
all traces and areas in (4.1) are retained.  A generic translation vector
then separates the source and target clusters.

All nine source norms, all nine target norms, and the two norm sets are
mutually injective as required.  On the Cartesian product of the nine
source vectors and the nine clean-target vectors, the adaptive profile is

\[
 Q=81,\qquad E_T=E_A=\mathcal B=99.                       \tag{4.3}
\]

This does not violate a diagonal-*scale* conjecture, but it is an exact
endpoint-realized obstruction to exact injectivity, bounded-tree support,
or a fixed-biclique exclusion in the star-heavy regime.

The projective-plane support model from the preceding note remains
abstract.  The new certificate shows that fixed bicliques survive all
endpoint constraints; it does not yet realize polynomial minimum degree
or high girth.  Hence DRC alone still does not close the support patch, and
an endpoint theorem at growing degree remains logically possible.

## 5. Hybrid star/matching sufficient gate

The positive lemma has a clean use.  Suppose a heavy fibre is decomposed
into `P=O(h/k)` pieces of two types:

* canonically oriented source-star halves, charged by (3.3); and
* source-and-target bi-matchings, charged by the adaptive trace--area rule.

Put the piece type and index into the charge key.  Every piece has
`O(m^2)` possible keys.  Assume

\[
 \sum_{\text{bi-matchings}}\mathcal B_i
 +C_{\rm dis}
 \le m^{o(1)}N(h+k),                                      \tag{5.1}
\]

where `C_dis` is the total number of the disjoint-edge Gaussian collisions
in the star pieces.  The diagonal Gaussian term and (3.9) are `O(Nh)`, so
the total selected energy is `m^{o(1)}N(h+k)`.  Cauchy gives

\[
 (hN)^2\le O(Pm^2)m^{o(1)}N(h+k).                         \tag{5.2}
\]

Using `h>k` and `P=O(h/k)` again yields

\[
 kN\le m^{2+o(1)}.                                        \tag{5.3}
\]

Thus the exact restart target is no longer “handle source stars.”  It is:

> control the four-distinct ordinary-edge Gaussian collisions across a
> small star cover, together with the adaptive envelopes on the balanced
> residual blocks.

The genuine augmentation theorem shows that the number of star colors
cannot be repaired from endpoint degree alone.  The proof must either find
a small *cover* adapted to the fibre, or pool the hard collisions without
paying one `m^2` universe per hub.

Run

```text
python3 phase2/loop/erdos1208/verify_star_heavy_endpoint_barrier.py
```

for the 104-point heavy augmentation, the 30-point source-star `K_{3,3}`,
the exact overlap/disjoint Gaussian decomposition, and all distance and
clean-fibre checks.
