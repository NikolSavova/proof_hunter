# Redundancy-charged semialgebraic retention

**Date:** 2026-08-15.  All logarithms and entropies are base two.

## Verdict

The retention version of the proposed statement is true.

> **Theorem (consecutive-sign retention).**  There is an absolute constant
> `A` with the following property.  Let
> 
> \[
>     E\subseteq X_1\times\cdots\times X_r
> \]
> 
> be nonempty with `r>=3`, where the `X_i` are finite planar point sets.
> Suppose that,
> for every `j=1,...,r-2`, all words in `E` have the same prescribed strict
> orientation on coordinates `(j,j+1,j+2)`.  Put
> 
> \[
>   M=|E|,\qquad
>   R=\log {\prod_i|\pi_iE|\over M}.                     \tag{1}
> \]
> 
> Then there are subsets `Y_i subseteq pi_i E` such that every transversal
> of `Y_1 times ... times Y_r` has all the prescribed consecutive signs and
> 
> \[
>    |E\cap(Y_1\times\cdots\times Y_r)|
>       \ge M\,2^{-A(r+R)}.                              \tag{2}
> \]

Thus a rank `r=O(log n)` source family with support redundancy
`R=o((log n)^2)` has a homogeneous radial/profile container retaining
`2^{-o((log n)^2)}` of its mass.  In particular, the quadratic loss in the
direct growing-arity Fox--Pach--Suk application is not intrinsic.

The stronger claim that all of `E` can be covered by `2^{O(r+R)}` such
product cells is false.  Already at `r=3` there are constant-redundancy
families requiring `Omega(N)` cells.  Retention, rather than bounded cover,
is the correct conclusion.

The proof has two exact ingredients:

1. a fixed-arity semialgebraic regularity partition, recursively applied
   only to its nonhomogeneous product cells;
2. a total-correlation telescope which pays for every recursion level on
   which selected mass is much larger than product-marginal mass.

The resulting transcript has entropy `O(1+TC)` for one orientation triple.
The sum of the total correlations of all consecutive triples is at most
twice the total correlation of the full word, which is at most `R`.

## 1. The fixed-arity regularity atom

Let

\[
  S=\{(x,y,z):\operatorname{orient}(x,y,z)=+1\}.         \tag{3}
\]

We use the following fixed-parameter consequence of Fox--Pach--Suk,
[*A polynomial regularity lemma for semi-algebraic hypergraphs and its
applications in geometry and property testing*](https://arxiv.org/abs/1502.01730),
Theorem 4.1.  This is the non-equitable, product-volume version in Section
4 from which the paper derives its introductory polynomial regularity
Theorem 1.3; the product-volume form of Theorem 4.1 is the one needed here.

> **Regularity atom.**  There is an absolute integer `K` such that, for
> every product probability measure `Q=Q_1 times Q_2 times Q_3` on three
> finite planar point sets, after harmless splitting of atoms, each
> coordinate space has a partition into at most `K` parts for which the
> union `N` of nonhomogeneous product cells satisfies
> 
> \[
>                         Q(N)\le {1\over4}.              \tag{4}
> \]

Here homogeneous means entirely contained in `S` or entirely disjoint
from `S`.  Atom splitting means replacing a point by finitely many labeled
copies on which the orientation relation ignores the label.  A homogeneous
copy rectangle therefore projects to a genuine homogeneous rectangle in
the original planar point sets.

For completeness, this is an exact consequence of the primary theorem,
not an assumed weighted regularity principle.  For rational `Q_i`, replace
each point by a number of labeled copies proportional to its mass.  Give
the three color classes equal total numbers of copies.  Encode color and
copy labels in extra coordinates which the orientation polynomial ignores,
and symmetrize the relation by color.  Apply Theorem 4.1 with error
`1/108`.  That theorem gives at most

\[
                         K\le108^c                       \tag{5}
\]

parts, where `c=c(3,d_0,t_0,D_0)` is the fixed constant in the theorem for
this fixed color-encoded orientation relation.  Restricting the partition
back to the three colors, an ordered one-from-each-color product has weight
`1/27` in the union cube.  Hence its nonhomogeneous mass is at most
`27/108=1/4`, proving (4).  The paper does not give a numerical value for
`c`; none is claimed here.  Irrational measures follow by approximation,
although all measures arising from the uniform law on a finite `E` are
rational.

The use of split atoms is important but innocuous.  It is equivalent to
adjoining independent private randomness to each coordinate.  If
`U_1,U_2,U_3` are conditionally independent given `X_1,X_2,X_3`, with
`U_i` depending only on `X_i`, then

\[
 TC((X_1,U_1),(X_2,U_2),(X_3,U_3))
                    =TC(X_1,X_2,X_3).                    \tag{6}
\]

The conditional label entropies cancel from the definition of total
correlation.  Moreover, a transcript event in the split space implies
membership in its projected original-coordinate rectangle.  Consequently
a mass lower bound obtained in the split space is also a mass lower bound
for an ordinary planar rectangle.

## 2. Entropy-sensitive monochromatic transcript

Let `P` be any probability distribution on three planar coordinates
supported on `S`, and write

\[
 T=TC_P(X,Y,Z)=H(X)+H(Y)+H(Z)-H(X,Y,Z).                  \tag{7}
\]

> **Lemma 1 (local transcript).**  There is a possibly privately randomized
> transcript `C`, each value of which certifies a positive homogeneous
> product rectangle, such that
> 
> \[
>             H(C)\le \log(K^3)\left(2+{T\over c_0}\right),
> \qquad c_0={1\over2}\log{4\over3}.                    \tag{8}
> \]

**Proof.**  At a node `v`, condition `P` on the current split-coordinate
product cell and call the conditional distribution `P_v`.  Form the
product `Q_v` of its three marginals and apply the regularity atom.  Positive
homogeneous cells terminate.  Negative homogeneous cells have zero
`P_v`-mass.  Recurse on every nonhomogeneous cell.

Let `theta_v` be the `P_v`-mass of the union of recursive cells and let
`q_v` be its `Q_v`-mass.  Equation (4) gives `q_v<=1/4`.  Call a node high
if `theta_v>1/2`.  If `L=(L_1,L_2,L_3)` is the triple of partition labels,
data processing gives

\[
 TC(L_1,L_2,L_3)
   =D(P_L\|P_{L_1}P_{L_2}P_{L_3})
   \ge d(\theta_v\|q_v).                                \tag{9}
\]

At a high node the last expression is at least

\[
 d(1/2\|1/4)={1\over2}\log{4\over3}=c_0.               \tag{10}

\]

The following entropy decomposition is the exact telescope:

\[
 TC(P_v)\ge TC(L_1,L_2,L_3)
        +\sum_\ell P_v(L=\ell),TC(P_v\mid L=\ell).      \tag{11}
\]

Indeed, expand both sides using entropy and use
`H(X_i|L_i)>=H(X_i|L_1,L_2,L_3)`.  Iterating (11) down the tree shows that
the total `P`-weighted mass of high internal nodes is at most `T/c_0`.

Let `I`, `I_low`, and `I_high` be the sums of the global `P`-masses of all
internal, low internal, and high internal nodes.  The children of a low
node have total mass at most half their parent's mass; those of a high node
have total mass at most their parent's mass.  Therefore

\[
 I\le1+{1\over2}I_{low}+I_{high}.
\]

Since `I=I_low+I_high`, this gives

\[
                         I\le2+{T\over c_0}.              \tag{12}
\]

Applying this argument first to every finite truncation and then using
monotone convergence makes the infinite-tree bookkeeping formal.  In
particular the recursion terminates almost surely.  A terminal path is
a prefix-free word over an alphabet of size at most `K^3`.  Its expected
length is `I`, so the source-coding inequality gives (8).  QED.

The private randomness only implements rational atom splitting.  Each
terminal copy rectangle projects to an ordinary positive planar rectangle,
and the probability of the terminal event is no larger than the `P`-mass
of that projected rectangle.

## 3. Global consecutive-chain theorem

Give `E` the uniform law and denote the random word by
`X=(X_1,...,X_r)`.  Its full total correlation is

\[
 \begin{aligned}
 T_*&=\sum_{i=1}^r H(X_i)-H(X_1,...,X_r)\\
    &\le\sum_i\log|\pi_iE|-\log M=R.                    \tag{13}
 \end{aligned}

Let `T_j=TC(X_j,X_{j+1},X_{j+2})`.  Put

\[
 a_i=I(X_i;X_1,...,X_{i-1}),\qquad
                         T_*=\sum_{i=2}^r a_i.           \tag{14}

By monotonicity of mutual information,

\[
 \begin{aligned}
 T_j
  &=I(X_{j+1};X_j)+I(X_{j+2};X_j,X_{j+1})\\
  &\le a_{j+1}+a_{j+2}.
 \end{aligned}                                          \tag{15}

Every `a_i` occurs at most twice on summing (15), hence

\[
                         \sum_{j=1}^{r-2}T_j\le2T_*\le2R.\tag{16}

Apply Lemma 1 independently to every consecutive triple, using independent
private atom-splitting labels conditional on the full word.  Let
`C=(C_1,...,C_(r-2))` be the joint transcript.  Entropy subadditivity,
(8), and (16) give

\[
 \begin{aligned}
 H(C)&\le\sum_jH(C_j)\\
 &\le\log(K^3)\left(2(r-2)+{2R\over c_0}\right)\\
 &\le A(r+R),                                           \tag{17}
 \end{aligned}

for the absolute constant

\[
              A=\log(K^3)\max\{2,2/c_0\}.              \tag{18}

Some transcript value `c` has probability at least `2^{-H(C)}`.  Each
local value `c_j` projects to three coordinate subsets on which the `j`th
orientation has the prescribed sign.  Intersect all subsets assigned to
the same coordinate, obtaining `Y_1,...,Y_r`.  The intersection of these
overlapping cylinder rectangles is exactly a global coordinate product,
and every one of its transversals has all prescribed local signs.  The
event `C=c` implies `X_i in Y_i` for every `i`, so

\[
 P(X\in Y_1\times\cdots\times Y_r)
       \ge P(C=c)\ge2^{-A(r+R)}.                         \tag{19}

Multiplying by `M` proves (2).

## 4. Why bounded cover is false

Take three disjoint color classes on the parabola `p(s)=(s,s^2)`:

\[
 X_1=\{p(3a):0\le a<N\},\quad
 X_2=\{p(3b+1):0\le b<N\},\quad
 X_3=\{p(3c+2):0\le c<N\}.                              \tag{20}

Let

\[
 E_N=\{(p(3a),p(3b+1),p(3c+2)):0\le a\le b\le c<N\}.  \tag{21}

All triples are positive, and

\[
 |E_N|={N+2\choose3},\qquad
 R_N=\log{N^3\over {N+2\choose3}}<\log6.               \tag{22}

For `i=0,...,N-2`, consider

\[
 e_i=(p(3i),p(3i+1),p(3N-1)).                           \tag{23}

These are members of `E_N`.  If a positive homogeneous product rectangle
contained both `e_i` and `e_j`, `i<j`, it would contain the mixed triple

\[
                    (p(3j),p(3i+1),p(3N-1)).            \tag{24}

Its parameter order is middle, first, third, so its orientation is
negative.  This is impossible.  Hence each homogeneous cell contains at
most one of the `N-1` distinguished triples, and every cover needs at least
`N-1` cells although `r+R_N=O(1)`.

This does not contradict retention: a box using three separated index
intervals captures a constant fraction of `E_N`.

## 5. Sharpness against the diagonal barrier

In the diagonal parabola family of
`SEMIALGEBRAIC_CONSECUTIVE_TRIPLE_AUDIT.md`,

\[
 M=2^{d^2},\qquad r=3d,\qquad R=2\log M.                \tag{25}

Every homogeneous product cell contains at most one selected word.  Thus
no retention theorem can remove the `R` term from (2).  The present bound
becomes deliberately vacuous on that maximally correlated family, while
it is subquadratic precisely in the surviving regime `R=o(r^2)`.

## 6. Scope

The theorem is a container-retention result, not yet a convex-face count.
It says that prescribed local planar chain constraints can be promoted to
one ambient Cartesian container at the exact `2^{O(r+R)}` cost.  Any
remaining obstruction must therefore come from one of the following:

* the relevant directional/profile relation is not expressible by a fixed
  finite list of local semialgebraic signs;
* the selected source family has quadratic projection redundancy, which
  must be paid by a separate face bank;
* the ambient homogeneous container does not itself yield the required
  ordinary convex faces.

It cannot be blamed on cross-base retention for consecutive orientation
constraints.

## Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_redundancy_charged_retention.py
```

The verifier checks the exact parabola cover obstruction, the redundancy
scale, the binary-KL constant, the total-correlation decomposition on
finite distributions, the consecutive-triple inequality, and the abstract
tree mass accounting used in (12).
