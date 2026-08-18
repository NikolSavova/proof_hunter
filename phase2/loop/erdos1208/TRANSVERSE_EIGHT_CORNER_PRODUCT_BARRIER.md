# Product barrier to the adaptive eight-corner gate

## 1. Result

The adaptive eight-corner condition in `TRANSVERSE_EIGHT_CORNER_GATE.md` is
false by the largest possible power scale.

Let `K(A)` denote the maximum, over transverse relations `rho`, of the
minimum of the eight corner-projection degrees through `rho`.  There are
arbitrarily large integer distance-Sidon sets `A` for which

\[
 K(A)\ge \frac{|A|+18}{24}.                     \tag{1.1}
\]

In particular, `K(A)<=|A|^{o(1)}` is false.  The obstruction is not merely
the finite greedy closure: one may take independent generic copies of all
eight affine completion families through a single transverse relation.

The exact finite inputs and the linear-algebra table used below are checked
by

```text
python3 phase2/loop/erdos1208/verify_transverse_eight_corner_product_barrier.py
```

The same verifier checks the exploratory 120-point integer witness, whose
eight degrees through the fixed relation are

\[
 (43,56,54,43,43,54,56,43).                    \tag{1.2}
\]

The theorem below supersedes that numerical evidence.

## 2. One base relation and eight seed completions

Use the exact 60-point distance-Sidon set from
`verify_transverse_closure_witness.py`.  Inside it take

\[
\begin{array}{lll}
 a_0=(-64,-16),&a_1=(20,18),\\
 b_0=(-33,-5), &b_1=(18,19),\\
 c_0=(35,7),   &c_1=(45,-26).
\end{array}
\]

They obey

\[
 a_0-a_1=(b_0-b_1)+J(c_0-c_1),                 \tag{2.1}
\]

and

\[
 (a_0-a_1)\mathbin\cdot(c_0-c_1)=-282\ne0,     \tag{2.2}
\]

so they define a transverse relation `rho_0`.  The six points themselves
are distance-Sidon.

For every corner `epsilon in {0,1}^3`, the 60-point witness contains a second
transverse relation having the same selected triple

\[
 (a_{\epsilon_0},b_{\epsilon_1},c_{\epsilon_2}). \tag{2.3}
\]

Its three complementary endpoints are outside the six base points and are
pairwise distinct.  In the index order of the verifier, one choice for each
corner is

\[
\begin{array}{c|c}
\epsilon&\text{complementary endpoint indices}\\ \hline
(0,0,0)&(25,22,10)\\
(1,0,0)&(25,47,38)\\
(0,1,0)&(10,17,33)\\
(1,1,0)&(0,21,3)\\
(0,0,1)&(16,10,21)\\
(1,0,1)&(39,15,10)\\
(0,1,1)&(32,31,41)\\
(1,1,1)&(43,23,31).
\end{array}                                      \tag{2.4}
\]

Here the displayed binary order follows the verifier's bit convention.  For
each row, the base six points together with the three complementary points
are still a subset of the 60-point distance-Sidon witness.  This finite fact
will certify that no equality between two labelled distances inside one
completion family is forced identically.

## 3. The affine completion families

Fix a corner `epsilon`.  Keep the three selected base endpoints in (2.3),
and replace the three complementary endpoints by new points

\[
 x_0,x_1,x_2.
\]

Requiring the six endpoints to satisfy (2.1) imposes two independent affine
linear equations on the six coordinates.  Thus the completion space
`V_epsilon` is a rational affine four-space.

It is useful to subtract the original complementary base endpoints.  If the
three deviations are `X_0,X_1,X_2`, the homogeneous equation is

\[
 s_0X_0+s_1X_1+s_2JX_2=0,\qquad s_i\in\{-1,1\}. \tag{3.1}
\]

Taking `u=X_1` and `v=X_2` as free variables gives

\[
 X_0=\alpha u+\beta Jv,\qquad
 X_1=u,\qquad X_2=v,\qquad \alpha,\beta\in\{-1,1\}. \tag{3.2}
\]

Write the linear parts of these three coordinate maps as

\[
 L_0=[\alpha I\ \ \beta J],\qquad
 L_1=[I\ \ 0],\qquad
 L_2=[0\ \ I].                                  \tag{3.3}
\]

Each `L_r` has rank two, and every difference `L_r-L_s`, `r\ne s`, is
nonzero.  Consequently every moving point ranges over the whole plane and
every within-block edge has nonconstant squared length.

The seed in (2.4) is a rational point of `V_epsilon` at which the base points
and the three moving points have all their unordered distances distinct.
It follows that any equality between two distinct labelled squared-distance
polynomials involving only the base and one completion block is a nonzero
polynomial on `V_epsilon`.  Its transversality polynomial is also nonzero,
because the seed relation is transverse.

## 4. Independent blocks do not introduce an identity

Take any finite product of completion spaces, all sharing the same six base
points.  Blocks may have any of the eight corner types.  We claim that no two
distinct labelled edges have identically equal squared length on this
product.

Associate to an edge the set of completion blocks containing its endpoints.
This support has size zero, one, or two.

* If two edges have different supports, choose a block appearing in only one
  support.  The squared length of that edge depends nontrivially on the free
  variables of the chosen block, by (3.3), while the other length does not.
* If both supports are empty, the claim is the distance-Sidon property of the
  six base points.
* If the common support is one block, both edges lie among the base and that
  block.  The seed-completion argument in Section 3 says their difference is
  a nonzero polynomial.
* It remains to consider two edges joining the same two independent blocks.
  Order the blocks.  If the endpoint roles are `(r,s)`, the mixed quadratic
  coefficient in the squared length is `-2L_r^T L'_s`.  The nine matrices
  `L_r^T L'_s`, `0<=r,s<=2`, are pairwise distinct for every choice of the
  four signs in the two blocks.

For completeness, the last assertion can be read directly from the `2 by 2`
block-zero patterns.  The maps `L_1=[I,0]` and `L_2=[0,I]` select one block
row or column, while `L_0=[alpha I,beta J]` has both blocks nonzero.  Hence
the location of the nonzero blocks first identifies whether each role is
zero, one, or two; the signs then do not create a new coincidence.  The
verifier checks all `8*8*9=576` integer matrices exactly.

The same support argument shows that equality of two labelled points is not
an identity: coordinate projections have rank two, within-block differences
are nonzero, and different blocks have independent variables.

## 5. Generic rational product and the linear lower bound

Fix `t>=1`.  For each of the eight corners take `t` independent copies of
its completion space.  Their product is a rational affine space of dimension
`32t`.

Remove the following bad loci:

1. equality of two labelled points;
2. equality of two distinct unordered squared distances;
3. failure of transversality for one of the new relations.

Sections 3--4 show that every bad condition is the zero set of a nonzero
polynomial.  A finite union of proper algebraic hypersurfaces cannot cover an
affine space over an infinite field.  Rational points are Zariski dense, so
there is a rational configuration outside all the bad loci.

It consists of the six base points and `3t` new points for each of eight
corners.  Therefore

\[
 |A_t|=6+24t.                                    \tag{5.1}
\]

The set is distance-Sidon.  Each new block gives a transverse relation whose
`epsilon`-corner is the same selected base triple as `rho_0`.  Including
`rho_0` itself,

\[
 \deg_\epsilon(\pi_\epsilon(\rho_0))\ge t+1
 \quad\text{for every }\epsilon.                \tag{5.2}
\]

Thus

\[
 K(A_t)\ge\delta(\rho_0)\ge t+1
 =\frac{|A_t|+18}{24},                           \tag{5.3}
\]

which proves (1.1).

Finally multiply by a common denominator and translate.  This converts
`A_t` into a subset of `Z^2` without changing any vector relation, distance
equality, or transversality.  Hence the counterexamples are genuine lattice
sets and can be placed in a sufficiently large integer square.

## 6. Consequence for #1208

The adaptive eight-corner gate was stronger than the desired global
transverse estimate.  This note kills only that local strengthening, not the
transverse second-moment conjecture itself.  As in the earlier heavy-row and
foreign-shift obstructions, the construction concentrates many relations
through one distinguished object while leaving open the possibility that the
total relation count or fourth moment remains on the required scale.

The live target returns to the genuinely global statements:

\[
 E_{\rm trans}(A)\le |A|^{3+o(1)},
\]

or the equivalent decorated-parallelogram / row-moment gate.  Any next local
replacement must be tested against the product construction above before it
is treated as a viable proof route.
