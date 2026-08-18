# The Sidon-ruler barrier to the unrestricted endpoint midpoint charge

## 1. Verdict

The endpoint midpoint theorem proposed in
`ORTHOGONAL_SWITCHING_RICH_TAIL_GATE.md` is false without an ordinary-support
hypothesis.  There are distance-Sidon sets `A_h`, with

\[
 |A_h|=4h+2,\qquad N=|A_h-A_h|=\Theta(h^2),
\]

for which one fixed-component fibre has `h^2=Theta(N)` elements and its
ordered midpoint charge has average multiplicity `Omega(N)`.  This remains
true after deleting every fibre below any threshold `H=N^(o(1))`.

The same construction has

\[
 |D+D|=\Omega(N^2).                              \tag{1.1}
\]

Thus it lies in the already-proved Ruzsa high-support branch.  It does not
threaten the orthogonal product conjecture.  Instead it proves that the next
lemma must **trade midpoint-charge multiplicity against ordinary support**;
one cannot ask for subpolynomial charge multiplicity on all distance-Sidon
sets.

## 2. A dense integer Sidon ruler

Let `p` be a prime and put

\[
 t_j=2pj+(j^2\bmod p),\qquad 0\le j<p.            \tag{2.1}
\]

The set `T_p={t_0,...,t_{p-1}}` is Sidon in the integers.  Indeed, if
`t_i+t_j=t_k+t_l`, reduction modulo `2p` first gives equality of the two
least residues in `[0,2p-2]`; division of the remaining equality by `2p`
then gives

\[
 i+j=k+l.
\]

Reduction modulo `p` also gives `i^2+j^2=k^2+l^2`.  Hence `ij=kl mod p`, so
the two unordered pairs agree in `F_p`, and therefore agree as pairs of
indices in `[0,p-1]`.

Given `h`, take a prime `2h<=p<4h` and retain the first `2h` values.  We get a
Sidon ruler

\[
 P=\{p_1,\ldots,p_{2h}\}\subset[0,O(h^2)]e,
 \qquad e=(1,0).                                  \tag{2.2}
\]

Split it into `P_I={p_i:i in I}` and `P_J={p_j:j in J}`, each of size `h`.

## 3. Insert the ruler into the quadratic switching fibre

Identify the plane with the complex numbers, let `L=1+i`, choose a generic
vector `c`, and put `u=-ic`.  For generic translations `T,W`, define

\[
 q_i=T+c-Lp_i,\qquad r_j=T-Lp_j                   \tag{3.1}
\]

and

\[
 A_h=P_I\cup P_J\cup\{q_i:i\in I\}
       \cup\{r_j:j\in J\}\cup\{W,W+u\}.          \tag{3.2}
\]

For every `(i,j) in I x J`, set

\[
 x_{ij}=p_i-p_j,\qquad y_{ij}=-x_{ij},\qquad
 v_{ij}=q_i-r_j=c-Lx_{ij}.                        \tag{3.3}
\]

Then

\[
 u+iv_{ij}=x_{ij}+iy_{ij}.                        \tag{3.4}
\]

All `h^2` values `x_ij` are distinct because `P` is Sidon.  Consequently the
fixed-component fibre `g(u,0)` contains `h^2` elements.

### 3.1 Generic distance-Sidonicity

The parameters `c,T,W` may be chosen rationally so that (3.2) is
distance-Sidon.  Here is a direct non-identity check.

* Inside `P`, all squared lengths are distinct by the ruler property.
* Inside either the `q`- or `r`-copy, the squared lengths are twice the
  corresponding ruler squares.  The two copies cannot collide with each
  other because their index sets are disjoint and the ruler differences are
  unique; they cannot collide with a ruler square because
  `a^2=2b^2` has no nonzero integer solution.
* A `q_i-r_j` edge is `c-L(p_i-p_j)`.  Distinct cross differences give
  distinct affine offsets, so two such squared lengths are not identical
  polynomials in `c`.  Nor is one identically a constant internal length or
  `|u|^2=|c|^2`.
* An edge from `P` to a `q`- or `r`-point has the form `T-alpha`.  Its affine
  offset records both base indices: in coordinates,
  `p_a-Lp_i=(p_a-p_i,-p_i)`.  Hence distinct edges have distinct offsets,
  and their squared lengths are distinct polynomials in `T`; the `q` and
  `r` types are separated by their coefficient of `c`.
* Finally, all edges incident to `W` have the form `W-alpha`.  After generic
  `c,T` are fixed, their offsets are distinct unless two already-constructed
  points differ by `u`, another proper condition already avoided.

Thus every unwanted equality of squared edge lengths is a proper polynomial
hypersurface in `(c,T,W)`.  Its finite union has empty interior, so rational
parameters exist outside it; scaling gives an integral example.

## 4. Polynomial midpoint-charge multiplicity

The canonical midpoint decoration of `x_ij` is

\[
 m(x_{ij})=p_i+p_j.                               \tag{4.1}
\]

All `h^2` such sums are distinct.  But they lie on the integer segment
`[0,O(h^2)]e`, so

\[
 |\{m(x)-m(x'):x,x'\in g(u,0)\}|=O(h^2).          \tag{4.2}
\]

There are `h^2(h^2-1)=Theta(h^4)` ordered distinct pairs in the fibre.
Therefore their charge

\[
 (u,m(x)-m(x'))\in D\times(D+D)
\]

has average multiplicity

\[
 \Omega(h^2)=\Omega(N).                          \tag{4.3}
\]

This disproves the unrestricted subpolynomial-average assertion, including
its heavy-fibre version.

## 5. The obstruction pays with maximal ordinary support

For `i,i' in I` and `a,a' in I union J`, the set `D+D` contains

\[
 (q_i-p_a)+(q_{i'}-p_{a'})
 =2T+2c-L(p_i+p_{i'})-(p_a+p_{a'}).               \tag{5.1}
\]

The directions `e` and `Le` are linearly independent.  Equality between two
expressions in (5.1) therefore forces equality of the two `I`-pair sums and
of the two full-`P` pair sums.  The Sidon property then recovers both
unordered pairs.  Hence (5.1) supplies

\[
 \binom{h+1}{2}\binom{2h+1}{2}=\Theta(h^4)
   =\Theta(N^2)                                   \tag{5.2}
\]

distinct elements of `D+D`, proving (1.1).

This is precisely the compensation missing from the raw midpoint charge:
compressing the midpoint differences requires a dense Sidon ruler, while
the two independent ruler directions create a Cartesian square inside the
ordinary support.

## 6. Correct restart target

The unconditional endpoint-average target is closed.  The viable statement
must be restricted to the unresolved regime

\[
 |D+D|<N^{5/3-o(1)}                               \tag{6.1}
\]

and must still allow the proved few-parallel-line branch.  Equivalently, one
should seek a dichotomy of the following form:

> Either the heavy midpoint charges have total `N^(1+o(1))|D+D|`, or their
> high-multiplicity part generates enough independent ordinary sums to put
> `|D+D|` in the Ruzsa high-support branch.

The Sidon-ruler family shows the desired compensation at the strongest
possible scale: charge load `Theta(N)` is accompanied by ordinary support
`Theta(N^2)`.  Proving a global summable version of this tradeoff is now the
sharpest version of the switching route.

Run `verify_endpoint_midpoint_sidon_ruler_barrier.py`.  It checks the
Erdos--Turan ruler, exact distance-Sidonicity for five integral instances,
the `h^2` intended fibre, the midpoint-charge compression, and the Cartesian
ordinary-support witnesses.
