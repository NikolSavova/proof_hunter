# Endpoint-switched charges for the two popular-pair moments

## 1. Outcome

Keep the notation of `POPULAR_PAIR_RECTANGLE_MOMENT_GATE.md`.  Thus

\[
 D=A-A,\qquad N=|D|,\qquad S=|D+D|,
\]

`P` is the support-adaptive popular set, and for an ordered distinct pair
`z=(q,q') in P^2` we have

\[
 A_z=\{a:a,a+q,a+q'\in D\},\qquad
 B_z=\{d:d,d-Jq,d+q-q',d+q-q'-Jq'\in D\}.
\]

Write `alpha_z=|A_z|` and `beta_z=|B_z|`.  The remaining moment product is

\[
 \left(\sum_z\alpha_z^2\right)
 \left(\sum_z\beta_z^2\right)
 \le N^{2+o(1)}S^2.                              \tag{1.1}
\]

This note gives each factor a canonical charge whose target has exactly the
size required by (1.1): `(D+D)^2` for the alpha factor and sixteen labelled
copies of `D^2` for the beta factor.  The resulting size-biased load product
is a sufficient theorem for the full cube-root order.

The load theorem is **not proved here**.  What is proved is the exact charge
factorization, its target size, its reconstruction formulas, and its formal
implication for (1.1).  Exact complete-difference stresses have constant
size-biased loads.  The stored radial impostor has rapidly growing beta load.

## 2. The endpoint midpoint decoration

Every nonzero `d in D` has a unique ordered representation

\[
 d=x_d-y_d,\qquad x_d,y_d\in A,                  \tag{2.1}
\]

because `A` is distance-Sidon.  Define

\[
 m(d)=x_d+y_d.                                   \tag{2.2}
\]

For zero, fix one `a_* in A` and put `m(0)=2a_*`.  In every case
`m(d) in A+A`.  Moreover

\[
 (A+A)-(A+A)=A+A-A-A=D+D.                       \tag{2.3}
\]

Thus every difference of two decorated midpoints belongs to the ordinary
support `D+D`.  Notice that the popular shifts `q,q'` need not themselves
belong to `D`; they are never decorated.  This avoids an invalid hidden
hypothesis in an earlier exploratory search.

## 3. Alpha: a diagonal midpoint charge into `(D+D)^2`

An ordered contribution to `alpha_z^2` is a pair `a,b in A_z`.  Arrange its
six differences as

\[
\begin{matrix}
 d_0=a&d_1=a+q&d_2=a+q'\\
 d_3=b&d_4=b+q&d_5=b+q'.
\end{matrix}                                     \tag{3.1}
\]

Define

\[
 \Theta_\alpha(z,a,b)
 =\bigl(m(d_0)-m(d_4),\ m(d_1)-m(d_5)\bigr)
 \in(D+D)^2.                                     \tag{3.2}
\]

Let `lambda_alpha(X,Y)` be its load.  Then, exactly,

\[
 A_2:=\sum_z\alpha_z^2
     =\sum_{X,Y}\lambda_\alpha(X,Y).             \tag{3.3}
\]

The diagonal choice in (3.2) is not cosmetic.  The same-column charges
`(m(d_0)-m(d_3),m(d_1)-m(d_4))` have polynomially larger loads on the
determinant-prime Costas stresses.  The crossed diagonal retains the two
switchings needed to distinguish the rows.

Put

\[
 Q_\alpha=\sum_{X,Y}\lambda_\alpha(X,Y)^2,
 \qquad L_\alpha=Q_\alpha/A_2.                   \tag{3.4}
\]

Since the target of (3.2) has at most `S^2` elements, Cauchy--Schwarz gives

\[
 A_2^2\le S^2Q_\alpha,
 \qquad A_2\le S^2L_\alpha.                     \tag{3.5}
\]

There is also a useful four-diagonal reconstruction.  If

\[
 e=d_4,\qquad f=d_5,
\]

then the four values `(d_0,e,d_1,f)` determine the missing two:

\[
 d_2=d_1+f-e,\qquad d_3=d_0+e-d_1.              \tag{3.6}
\]

Thus a fixed alpha charge is a coupled pair of endpoint-midpoint fibres,
with the two cross-memberships in (3.6) retained.  Dropping those two
memberships returns to the previously disproved unrestricted midpoint
charge.

## 4. Beta: a maximal-role charge into sixteen copies of `D^2`

Put `L=I+J`.  For `d in B_z`, write

\[
 x_0=d,\quad x_1=d+q-q',\quad x_3=d-Jq,
 \quad x_2=x_3+L(x_1-x_0).                       \tag{4.1}
\]

All four values lie in `D`.  An ordered contribution to `beta_z^2` is a
pair `d,e in B_z`; if `h=e-d`, put

\[
 y_i=x_i+h\quad(0\le i<4).                       \tag{4.2}
\]

Again all eight values lie in `D`.

Distance-Sidonicity makes the squared norms of the elements of `D` distinct
up to antipodes.  Break the harmless antipodal ties by choosing the smallest
role index.  Let

\[
 i=\operatorname*{argmax}_{0\le r<4}|x_r|,
 \qquad
 j=\operatorname*{argmax}_{0\le r<4}|y_r|.       \tag{4.3}
\]

Define the labelled charge

\[
 \Theta_\beta(z,d,e)=(i,j,x_i,y_j)
 \in\{0,1,2,3\}^2\times D^2.                   \tag{4.4}
\]

For a fixed `z` and fixed roles `(i,j)`, this charge is injective in `(d,e)`:
each `x_i` is an affine translate of `d`, and each `y_j` is the same affine
translate of `e`.  Hence every nontrivial load in (4.4) is purely
cross-`z`, just as in the opposite-endpoint charge.

Let `lambda_beta` be its load and put

\[
 B_2:=\sum_z\beta_z^2=\sum\lambda_\beta,
 \quad Q_\beta:=\sum\lambda_\beta^2,
 \quad L_\beta:=Q_\beta/B_2.                    \tag{4.5}
\]

The target in (4.4) has at most `16N^2` elements, so

\[
 B_2^2\le16N^2Q_\beta,
 \qquad B_2\le16N^2L_\beta.                    \tag{4.6}
\]

### 4.1 Exact fixed-key form

For example, take roles `(i,j)=(0,2)`, so the fixed charged values are
`u=x_0` and `v=y_2`.  Put

\[
 r=q-q',\qquad p=q'.                             \tag{4.7}
\]

The eight entries are exactly

\[
\begin{array}{llll}
 x_0=u,&x_1=u+r,&x_3=u-J(r+p),&x_2=u+r-Jp,\\
 y_0=v-r+Jp,&y_1=v+Jp,&y_2=v,&y_3=v-Lr.
\end{array}                                      \tag{4.8}
\]

The popularity restrictions are `p,r+p in P`.  Two preimages of the same
key with parameter offset `(rho,pi)` force the six nonzero form
displacements

\[
 \rho,\quad -J(\rho+\pi),\quad \rho-J\pi,
 \quad-(\rho-J\pi),\quad J\pi,\quad-L\rho.       \tag{4.9}
\]

Equations (4.8)--(4.9) give the exact endpoint for an aggregate proof.  The
maximal-role rule additionally retains the six inequalities saying that the
uncharged first-row entries are no longer than `u` and the uncharged
second-row entries are no longer than `v`.

## 5. A single sufficient load-product theorem

Combining (3.5) and (4.6) gives

\[
 A_2B_2\le16N^2S^2L_\alpha L_\beta.             \tag{5.1}
\]

Consequently the following statement is sufficient for (1.1), and hence
for the cube-root order of Erdős problem 1208:

> **Endpoint-switched two-load theorem.**  For every planar lattice
> distance-Sidon set, with the support-adaptive popular set `P`,
> \[
> L_\alpha L_\beta=N^{o(1)}.                    \tag{5.2}
> \]

The stronger pair `L_alpha=N^{o(1)}` and `L_beta=N^{o(1)}` also suffices,
but (5.2) allows compensation between the midpoint and rotated sides.  This
is strictly more flexible than proving the two raw moment bounds separately.

## 6. Exact stress profiles

`verify_endpoint_switched_two_moment_charge.py` checks all identities above.
The key exact profiles are

\[
\begin{array}{c|r|r|r|r}
&\text{mass}&\text{charge image}&\text{charge second moment}&\max\lambda\\ \hline
\alpha,\ \text{closure }40&2,744,348&1,290,420&8,846,328&254\\
\alpha,\ \text{Costas }23&2,294,322&954,020&7,596,972&242\\
\beta,\ \text{closure }40&104,948&82,756&320,912&41\\
\beta,\ \text{Costas }23&250,722&147,832&834,482&45
\end{array}                                      \tag{6.1}
\]

Thus the four size-biased loads in (6.1) are respectively

\[
 3.2235\ldots,quad3.3112\ldots,quad
 3.0578\ldots,quad3.3283\ldots.                \tag{6.2}
\]

The determinant-prime rows through `p=31` remain at the same constant scale.
The old dense Sidon-ruler midpoint obstruction has empty adaptive tail, so
it contributes no charge at all.  By contrast, the radial side-eight
impostor has beta mass `336,612`, charge second moment `13,215,740`, and
size-biased load `39.261...`; it has no endpoint midpoint decoration for the
alpha charge.  This is evidence that the two charges retain the missing
complete-difference input.  It is not a proof of (5.2).

## 7. Next proof target

The next useful theorem should not bound a maximum load: the Costas maximum
already grows while its size-biased load stays bounded.  It should instead
charge ordered collisions of either map to lower-radius endpoint switchings,
or prove the product form (5.2) directly.  For beta, the exact six-copy
system (4.8)--(4.9) and the maximal-radius inequalities must remain present.
For alpha, the cross-memberships (3.6) are load-bearing; deleting them is the
known Sidon-ruler failure mode.
