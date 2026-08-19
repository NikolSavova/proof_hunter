# Three-projection linearity still does not force cubic support

## 1. The exact property of real fibres

Let `A subset R^2` be distance-Sidon, let `J` be quarter-turn, and for every
output `x` define its nonzero representation fibre

\[
 \mathcal F_x=
 \{(p,r,q)\in A^3:r\ne q,\ x=p+J(r-q)\}.        \tag{1.1}
\]

Every `F_x` is a three-coordinate matching: no two records have the same
`p`, the same `r`, or the same `q`.  More strongly, if `x!=y`, then for each
of the three pair projections

\[
 \pi_{pr},\qquad\pi_{pq},\qquad\pi_{rq},
\]

one has

\[
 \boxed{
 |\pi(\mathcal F_x)\cap\pi(\mathcal F_y)|\le1.} \tag{1.2}
\]

For example, suppose `(p_i,r_i)` is shared for two different indices
`i=1,2`.  Let the corresponding third coordinates in the two fibres be
`q_i` and `q'_i`.  Subtracting the two output equations gives

\[
 q'_i-q_i=J(y-x),                                \tag{1.3}
\]

the same nonzero difference for both `i`.  Vector-Sidonicity of `A` allows
only one ordered endpoint pair with a prescribed nonzero difference, which
proves (1.2) for `pi_pr`.  The `pi_pq` proof is identical, and the `pi_rq`
case uses the fixed difference between the two first coordinates.

This property is genuinely stronger than saying that each individual fibre
is a matching.  It destroys the parallel classes in the affine block model
of `AFFINE_DOUBLE_ENDPOINT_ORIENTATION_BARRIER.md`.

## 2. A sharp finite-field countermodel

Unfortunately, (1.2) is still not enough.  Let `q` be an odd prime and put

\[
 S=\{1,2,\ldots,(q-1)/2\}\subset F_q^*.
\]

For `a in S` and `b in F_q`, start with the matching

\[
 \mathcal L_{a,b}=
 \{(t,at+b,a^2t+(a+1)b):t\in F_q\}.             \tag{2.1}
\]

Its three pair projections are affine lines:

\[
\begin{aligned}
 r&=ap+b,\\
 q&=a^2p+(a+1)b,\\
 q&=ar+b.
\end{aligned}                                    \tag{2.2}
\]

The first and third line parameters are visibly `(a,b)`.  In the second,
`a^2` is injective on `S` and `a+1` is nonzero.  Therefore two distinct
matchings have at most one common cell in every pair projection.

The only triples repeated between different matchings are the diagonal
triples `(t,t,t)`.  Indeed, eliminating `a,b` from (2.1) gives

\[
 q-r=a(r-p).                                     \tag{2.3}
\]

If `r!=p`, the triple determines `a`, and then `b=r-ap`.  If `r=p`, (2.3)
forces `q=r`, and every permitted `a` supplies the same diagonal triple.

Keep each diagonal triple only in `L_(1,0)` and delete it from the other
matchings.  The resulting family consists of

\[
 |S|q={q(q-1)\over2}=\Theta(q^2)                 \tag{2.4}
\]

fibres, still obeys (1.2), and has pairwise disjoint triples.  Its total
mass is

\[
 |S|q^2-(|S|-1)q
 ={q^3\over2}+O(q^2)=\Theta(q^3).                \tag{2.5}
\]

Every fibre has size `q` or `q-1`.  Thus the abstract data in Sections 1--2
have exactly the forbidden efficient scale: cubic representation mass on
only quadratic output support.

## 3. Consequence for the live proof

Neither of the following can establish the cubic support theorem:

1. fibrewise injectivity in the three endpoint coordinates;
2. linearity of all three pair projections across different fibres.

The finite-field system satisfies both with sharp parameters.  What it does
not supply is a point `x in Z^2` for each fibre satisfying the same literal
equation

\[
 x=p+J(r-q)                                      \tag{3.1}
\]

for all of its records, with all three label copies equal to one Euclidean
distance-Sidon set.  This characteristic-zero compatibility is now the
minimum remaining input.  The contraction lemma in the affine endpoint
barrier is one exact example of how (3.1) kills an efficient finite-field
pencil.

## 4. Verification

`verify_three_projection_fibre_barrier.py` checks the real-fibre lemma on
integral Golomb sets and checks (2.1)--(2.5) by exact finite-field
enumeration for `q=5,7,11,13,17,19`.  It verifies disjointness of the
deduplicated triples and the intersection-at-most-one property in all three
pair projections.
