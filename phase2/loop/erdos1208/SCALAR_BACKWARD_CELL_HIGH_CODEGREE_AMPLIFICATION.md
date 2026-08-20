# Scalar backward cells: a linear barrier and high-codegree amplification

## 1. Outcome

The target-star switch reduces the one-role term to records

\[
 (g,v,w,q),\qquad
 v\in P_g,\quad w\in B_g,\quad
 v,w\in X_{q,g},                                      \tag{1.1}
\]

with scalar label

\[
 z=\delta(v-q)-\delta(w-q).                            \tag{1.2}
\]

A tempting next lemma would say that fixed `(g,v,w,z)` has
`m^(o(1))` possible backward shifts `q`.  This is false by a full power:
there are genuine integral distance-Sidon sets with `k=\Theta(h)` points
and

\[
 \boxed{L(g,v,w,z):=
   |\{q:(1.1)\text{ and }(1.2)\}|\ge h=\Theta(k).}       \tag{1.3}
\]

The construction can have `w in H_g`, four distinct source endpoints in
every row, and a determinant-qualified scalar target wedge at `-z/18`.
Thus neither the star-to-clean endpoint switch, source-edge disjointness,
nor target determinant qualification gives a pointwise backward-cell
bound.

The high-codegree restriction is the one resource absent from this
barrier.  Retaining it gives an exact size-biased amplification.  Every
high-codegree backward record has at least `k` choices of a third clean
translation.  Consequently the high one-role mass is at most `1/k` times
an explicitly defined three-translation mass.  The replacement term has
an analogous two-translation amplification.

This identifies a smaller remaining theorem: bound the amplified masses
at scale `m^(o(1)) N k^4`.  Dividing by `k` then gives the required
`m^(o(1)) N k^3`.  Any pointwise attack that deletes the high-codegree
decoration cannot work because of (1.3).

## 2. Backward-cell algebra

For fixed `v,w`, put `d=v-w`.  A backward shift `q` gives source pair sums

\[
 s=v-q,\qquad t=w-q,qquad s-t=d.                       \tag{2.1}
\]

If the two source edges meet, write

\[
 E(s)=\{a,u\},\qquad E(t)=\{b,u\}.                     \tag{2.2}
\]

Then `a-b=d`.  Vector-Sidonicity fixes the ordered outer pair `(a,b)`, and

\[
 \delta(s)-\delta(t)
 =|a|^2-|b|^2-2(a-b)\mathbin\cdot u.                   \tag{2.3}
\]

Thus the meeting-edge part of one fixed scalar cell is exactly a subset
of one line in `A`; moreover `q=v-a-u` is injective in `u`.  In
particular

\[
 L_{\rm meet}(v,w,z)\le
 \max_{\ell\text{ a line}}|A\cap\ell|.                 \tag{2.4}
\]

This explains the perpendicular-ruler obstruction to a divisor bound.
It does not explain away the whole problem: Section 4 plants the same
linear multiplicity with four distinct source endpoints.

If the doubled signed source area

\[
 e=2\det(a-u,b-u)                                      \tag{2.5}
\]

is fixed as well, (2.3)--(2.5) determine the two coordinates of `u`
because `d` is nonzero.  Hence the meeting-edge multiplicity in a fixed
`(v,w,z,e)` cell is at most one.  For the four-distinct part, the Gaussian
factorization gives the familiar uniform bound

\[
 L_{\rm disj}(v,w,z,e)\le m^{o(1)}.                    \tag{2.6}

\]

The barrier therefore spreads over linearly many signed-area cells.  The
scalar weight fixes `z` but not `e`, so summing (2.6) over areas loses the
power seen in (1.3).

## 3. Exact high-codegree amplification

For a source pair `p=(s,t)`, retain

\[
 Q_p=\{q:s,t\in H_q\},\qquad c(p)=|Q_p|.                \tag{3.1}
\]

Let `\mathcal C` be the set of oriented one-role records in (1.1), with
the two source orientations accounted for by the weight as in the exact
switch.  For a record `C=(g,v,w,q)`, put

\[
 p_C=(v-q,w-q).                                         \tag{3.2}
\]

Define its third-translation extension set

\[
 \mathcal E(C)=Q_{p_C}.                                 \tag{3.3}
\]

For an arbitrary nonnegative weight `V`, define

\[
\begin{aligned}
 \widetilde D_{\rm one}(V)
 =\sum_{C\in\mathcal C:\ c(p_C)\ge k}
   \sum_{q_0\in\mathcal E(C)}
   \bigl(V(p_C)+V(p_C^{\rm op})\bigr).                 \tag{3.4}
\end{aligned}
\]

This is a literal three-translation endpoint system:

* `q,q+g` give the star-to-`B_g` reverse record;
* `q_0` gives the third pair of clean rows
  `v-q,w-q in H_(q_0)`; and
* all target pair sums in that third row are
  `v-q+q_0,w-q+q_0`.

Since every retained record has `|E(C)|=c(p_C)>=k`, the exact identity is

\[
 \widetilde D_{\rm one}(V)
 =\sum_{C:c(p_C)\ge k}c(p_C)
   \bigl(V(p_C)+V(p_C^{\rm op})\bigr),                  \tag{3.5}
\]

and hence

\[
 \boxed{D_{\rm one}^{\ge k}(V)
       \le {1\over k}\widetilde D_{\rm one}(V).}       \tag{3.6}

\]

Here `D_one^(>=k)` means the exact one-role switch restricted to source
pairs with codegree at least `k`.  No maximum or dyadic replacement has
been made.

For the replacement records let `R_p subset Q_p` and `rho(p)=|R_p|` be as
in the completion theorem.  Define

\[
 \widetilde D_{\rm rep}(V)
 =\sum_{p:c(p)\ge k}\sum_{q\in R_p}\sum_{q_0\in Q_p}V(p)
 =\sum_{p:c(p)\ge k}\rho(p)c(p)V(p).                   \tag{3.7}
\]

Then exactly

\[
 \boxed{D_{\rm rep}^{\ge k}(V)
       \le {1\over k}\widetilde D_{\rm rep}(V).}       \tag{3.8}

\]

Combining (3.6)--(3.8), a sufficient endpoint theorem for the completed
high-codegree route is

\[
 \boxed{
 \widetilde D_{\rm one}(V)+\widetilde D_{\rm rep}(V)
 \le m^{o(1)}Nk^4.}                                    \tag{3.9}

\]

Unlike the false pointwise statement, (3.9) retains the only decoration
that separates the barrier from the live branch: at least `k` clean
third-translation extensions for every source pair.

## 4. A four-distinct star-to-clean planted cell

Fix distinct target points `x,y,z,a,b,c,d` satisfying

\[
 g=y-x,\qquad v=x+z,\qquad w=a+b,\qquad c+d=w+g.         \tag{4.1}
\]

Then `v in P_g`.  Choose the seven points so that

\[
 E(w)=\{a,b\},\qquad E(w+g)=\{c,d\}                   \tag{4.2}
\]

form a clean `g`-row; hence `w in H_g`.

Put `D_0=v-w`.  For `1<=i<=h`, choose four new source endpoints with pair
sums and displacements

\[
 S_i-T_i=D_0,qquad |U_i|^2-|V_i|^2=Z,                 \tag{4.3}

\]

where all `4h` endpoints are distinct and all individual squared lengths
are distinct.  For distinct odd `e_i`, the elementary family

\[
 M_i={Z+1+e_i^2\over2},\qquad
 U_i=(M_i,0),\qquad V_i=(M_i-1,-e_i)                    \tag{4.4}
\]

has the common gap `Z`; both `U_i-V_i=(1,e_i)` and the signed
areas vary with `i`.

Set

\[
 q_i=v-S_i.                                             \tag{4.5}

\]

Introduce fresh anchor pairs realizing `q_i` and `q_i+g`.  Then the four
identities

\[
 S_i+q_i=v,\quad T_i+q_i=w,\quad
 S_i+q_i+g=v+g,\quad T_i+q_i+g=w+g                     \tag{4.6}

\]

give one reverse record in the *same* cell `(g,v,w,Z)` for every `i`.
All source edges are four-distinct.  There are only `8h+O(1)` points
before installing a separate determinant-qualified target wedge at
`-Z/18`.

The affine identities in (4.1)--(4.6) force no equality between two
unoriented edge vectors.  The common norm-gap equations force differences
of norms, not equality of norms.  Consequently finite avoidance gives an
integral specialization in which all pair sums and all nonzero squared
distances are distinct and every displayed row is clean.  Adding `Theta(h)`
target-wedge records still leaves `k=Theta(h)` and makes the cell's scalar
weight `Theta(h^2)`.

Each planted source pair has only the two certified translations
`q_i,q_i+g`; it lies below the live `c(p)>=k` cutoff.  This is why the
construction disproves the pointwise backward-cell lemma but not (3.9).

## 5. Verification

`verify_scalar_backward_cell_high_codegree_amplification.py` performs a
deterministic finite-avoidance specialization and checks:

* global pair-sum and squared-distance injectivity;
* the four clean rows in (4.6) for every planted shift;
* `v in P_g`, `w in H_g`, and four-distinct source endpoints;
* one fixed `(g,v,w,Z)` cell with four distinct backward shifts;
* distinct signed source areas across the planted cell;
* a determinant-qualified scalar target wedge at `-Z/18`; and
* the finite forms of (3.5)--(3.8) on the certificate.
