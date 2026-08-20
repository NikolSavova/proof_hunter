# Gaussian norm-gap/area cells: divisor rigidity and support equivalence

## 1. Outcome

Let \(A\subset[0,M]^2\cap\mathbb Z^2\) be distance-Sidon, and let
\(\mathcal H_A\) be the endpoint-labelled zero-sum difference hypergraph.
For an ordered version of a hyperedge, write its three directed differences
as

\[
 q_1+q_2+q_3=0                                      \tag{1.1}
\]

and identify \(\mathbb Z^2\) with \(\mathbb Z[i]\).  Define

\[
 \boxed{z=q_1\overline{(q_2-q_3)}.}                 \tag{1.2}
\]

If

\[
 n_j=|q_j|^2,
 \qquad D=\det(q_1,q_2),                             \tag{1.3}
\]

then the exact joint invariant is

\[
 \boxed{z=(n_3-n_2)-2iD.}                           \tag{1.4}
\]

Every fixed nonzero Gaussian cell has divisor multiplicity:

\[
 \boxed{
 r_A(z)\le d_{\mathbb Z[i]}(z)
 \le4\tau(N(z))^2
 \le G(M)=M^{o(1)}.}                                \tag{1.5}
\]

Here \(r_A(z)\) counts ordered endpoint-labelled hyperedges in the cell,
\(d_{\mathbb Z[i]}(z)\) counts Gaussian divisors including associates,
and one may take

\[
 G(M)=4\max_{1\le n\le16M^4}\tau(n)^2.             \tag{1.6}
\]

The six endpoints are fully retained in (1.5): after the Gaussian factors
recover the three directed vectors, distance-Sidonicity recovers their
three directed endpoint edges uniquely.

There is, however, no size-biased aggregate gain hidden in (1.5).  Let

\[
 \Omega_A=\{z:r_A(z)>0\}.                            \tag{1.7}
\]

Reversing all three endpoint edges preserves \(z\) and has no fixed point.
Therefore every occupied cell has multiplicity at least two, while (1.5)
gives the upper bound:

\[
 \boxed{
 2|\Omega_A|
 \le6|\mathcal H_A|
 =\sum_zr_A(z)
 \le G(M)|\Omega_A|.}                               \tag{1.8}
\]

Thus, up to the allowed divisor factor, the endpoint-hypergraph theorem is
**equivalent** to the support theorem

\[
 \boxed{
 |\Omega_A|\le M^{o(1)}(k^3+M^2).}                  \tag{1.9}
\]

The fixed-cell theorem does not by itself make (1.9) easier.  It proves
that a counterexample must occupy too many distinct joint norm-gap/area
cells, rather than overloading a few cells.

One genuine new aggregate branch does follow.  If a family of hyperedges
uses only \(S_D\) signed determinant values, at arbitrary magnitudes, then

\[
 \boxed{
 |\mathcal F|
 \le {G(M)\over6}(4M^2+1)S_D.}                      \tag{1.10}
\]

In particular, every branch supported on \(M^{o(1)}\) signed determinant
values is ambient-paid by \(M^{2+o(1)}\), even if all determinants are
large.  The same statement holds with determinant values replaced by norm
gaps.  Combined with the low-determinant lattice-coset theorem, this leaves
only a large-area family with polynomial determinant entropy.

The Euclideanized finite-field parabola shows that (1.8) is sharp.  At
\(p=43\), \(M=1175\), its \(126852\) endpoint hyperedges give \(761112\)
ordered cells, but the joint support already has size \(375096\).  The
maximum cell multiplicity is eight and the full histogram is

\[
 \begin{array}{c|rrrr}
 r_A(z)&2&4&6&8\\ \hline
 \#z&369934&4886&254&22.
 \end{array}                                        \tag{1.11}
\]

After removing \(|D|\le10\), the large-determinant tail still has
\(727104\) ordered records on \(358868\) cells, an average load
\(2.026\ldots\).  Thus the divisor theorem is almost exactly the forced
reversal pairing on the principal stress.  Any successful aggregate proof
must genuinely bound the number of occupied cells.

## 2. Exact signs in the joint invariant

For Gaussian integers \(u,v\),

\[
 u\overline v=u\cdot v-i\det(u,v).                  \tag{2.1}
\]

Put \(w=q_2-q_3\).  Since \(q_1=-(q_2+q_3)\),

\[
 \begin{aligned}
 \Re(q_1\overline w)
 &=-(q_2+q_3)\cdot(q_2-q_3)
 =|q_3|^2-|q_2|^2,\\
 \det(q_1,w)
 &=\det(-(q_2+q_3),q_2-q_3)
 =2\det(q_2,q_3)\\
 &=2\det(q_1,q_2).
 \end{aligned}                                      \tag{2.2}
\]

Equation (2.1) now proves (1.4).  Swapping \(q_2,q_3\) changes \(z\) to
\(-z\); cyclically changing the distinguished vector changes the real
norm gap but retains the common signed doubled area with the corresponding
orientation.

For a clean hyperedge, \(z\ne0\).  Indeed, \(q_1\ne0\), while
\(q_2=q_3\) would give two equal nonzero directed differences.  Directed-
vector injectivity would then identify their endpoint edges, contradicting
six-endpoint cleanliness.

## 3. Fixed-cell reconstruction with all endpoints

Fix \(z\ne0\).  For any ordered record in its cell, (1.2) is a Gaussian
factorization

\[
 q_1\,\overline w=z.                                \tag{3.1}
\]

Thus \(q_1\mid z\) in \(\mathbb Z[i]\).  Conversely, after choosing a
Gaussian divisor \(u\mid z\), put

\[
 q_1=u,
 \qquad
 w=\overline{z/u},
 \qquad
 q_2={w-u\over2},
 \qquad
 q_3={-w-u\over2}.                                  \tag{3.2}
\]

The parity condition in (3.2) may fail, and the resulting vectors may fail
to be realized differences or to have six distinct endpoints.  But if a
record exists, (3.2) recovers its three directed vectors uniquely.

Distance-Sidonicity makes the directed difference map

\[
 (a,b)\longmapsto b-a\ne0                            \tag{3.3}
\]

injective.  Hence each recovered \(q_j\) has at most one directed endpoint
edge.  The map from records in the fixed \(z\)-cell to their first factor
\(q_1\) is injective, proving the first inequality in (1.5).

For completeness, let \(N=N(z)\).  Every Gaussian divisor \(u\mid z\)
has \(N(u)\mid N\).  For a fixed rational divisor \(d\mid N\), the number
of Gaussian integers of norm \(d\) is

\[
 r_2(d)\le4\tau(d)\le4\tau(N).                     \tag{3.4}
\]

Summing (3.4) over the \(\tau(N)\) choices of \(d\) gives

\[
 d_{\mathbb Z[i]}(z)\le4\tau(N)^2.                 \tag{3.5}
\]

Every endpoint difference has coordinates in \([-M,M]\), while
\(w=q_2-q_3\) has coordinates in \([-2M,2M]\).  Therefore

\[
 N(z)=N(q_1)N(w)\le(2M^2)(8M^2)=16M^4.              \tag{3.6}
\]

The standard divisor bound makes (1.6) \(M^{o(1)}\), completing the proof
of (1.5).

No representation multiplicity of a vector or endpoint pair has been
discarded in this argument.  The only losses are Gaussian divisors which
fail parity, realization, or endpoint cleanliness.

## 4. Why support and hypergraph mass are equivalent

Every hyperedge has six orderings of its three directed-edge vertices, so

\[
 \sum_zr_A(z)=6|\mathcal H_A|.                      \tag{4.1}
\]

Given one ordered record, reverse all three directed endpoint edges without
changing their order.  Its vector triple becomes
\((-q_1,-q_2,-q_3)\), and

\[
 (-q_1)\overline{((-q_2)-(-q_3))}
 =q_1\overline{(q_2-q_3)}=z.                        \tag{4.2}
\]

This is a distinct record because every directed edge is nonzero.  It is
an involution without fixed points inside each cell, so \(r_A(z)\ge2\).
Equations (1.5), (4.1), and (4.2) prove (1.8).

Consequently (1.9) implies the desired endpoint-hypergraph bound, and that
bound implies (1.9) with an absolute factor three.  A second-moment or
size-biased argument based only on large fixed-cell loads cannot help on a
family for which almost all loads equal two.

## 5. Sparse determinant entropy is closed

Let \(\mathcal F\subseteq\mathcal H_A\) be any family,
and let \(\Omega_{\mathcal F}\) be the support of the ordered cells coming
from \(\mathcal F\).  Suppose its signed determinant projection has size
\(S_D\).

For each fixed signed \(D\), (1.4) says that the imaginary part is fixed at
\(-2D\), while the real part is a difference of two distinct squared edge
lengths.  Both lengths lie in \([1,2M^2]\), so there are at most
\(4M^2+1\) possible real parts.  Therefore

\[
 |\Omega_{\mathcal F}|\le(4M^2+1)S_D.               \tag{5.1}
\]

Using (4.1) and (1.5) on this subfamily proves (1.10).  The proof for a
fixed set of norm-gap values is identical, with the two coordinates of
\(z\) interchanged and \(|D|\le2M^2\).

This branch is complementary to the low-determinant lattice-coset theorem:

- small determinant magnitude is paid even when every small value occurs;
- sparse determinant entropy is paid even when the values are arbitrarily
  large;
- the survivor has both large magnitude and polynomially many occupied
  determinant values.

More exactly, if

\[
 \nu(D)
 =|\{r:r-2iD\in\Omega_A\}|,                         \tag{5.2}
\]

then the exact aggregate support gate is

\[
 \boxed{
 \sum_D\nu(D)
 \le M^{o(1)}(k^3+M^2).}                            \tag{5.3}
\]

The divisor theorem supplies no further factor in (5.3); the parabola
stress confirms that most occupied summands already correspond to the
minimum possible cell load.

## 6. Verified Euclidean stress

Take the least-residue parabola

\[
 \{(x,x^2\bmod43):0\le x<43\}
\]

and apply the integral shear \((x,y)\mapsto(x+28y,y)\).  It is a genuine
distance-Sidon set of height \(M=1175\), and has \(126852\) endpoint
hyperedges.

Expanding every hyperedge into all six ordered vector triples gives the
profile (1.11).  In particular,

\[
 {761112\over375096}=2.02910\ldots.                 \tag{6.1}
\]

The nonzero-determinant part has \(758772\) ordered records on \(374220\)
cells.  The tail \(|D|>10\) has \(727104\) records on \(358868\) cells,
with maximum load eight.  Hence removing both the collinear and low-area
branches does not create a high-multiplicity Gaussian core.

The joint support itself is already a constant fraction of the ambient
budget:

\[
 {375096\over1175^2}=0.27168\ldots.                 \tag{6.2}
\]

This is the correct equality behavior: the fourth-order endpoint mass is
paid by \(M^2\), through many almost-injective Gaussian cells.

## 7. Verification

Run

    python phase2/loop/erdos1208/verify_gaussian_joint_cell_divisor_support_equivalence.py

The verifier checks:

1. the signs in (1.4) for every ordered record;
2. the reconstruction formulas (3.2), including Gaussian divisibility and
   parity;
3. fixed-cell injection by the first factor \(q_1\);
4. the explicit bound \(r_A(z)\le4\tau(N(z))^2\) on the exact \(p=7\)
   Euclidean certificate;
5. reversal pairing and both inequalities in (1.8);
6. the full \(p=43\) histogram (1.11), nonzero-area support, and
   large-determinant tail;
7. the sparse determinant and norm-gap support envelopes.

This note proves a fixed-cell theorem and a sparse-entropy aggregate
branch.  It also gives a sharp no-go: Gaussian divisor multiplicity alone
cannot prove the remaining support estimate (5.3).
