# The opposite-representation switching gate and its quadratic fibre barrier

## 1. The surviving averaged gate

Let `A` be a distance-Sidon set, put

\[
 D=A-A,\qquad N=|D|=|A|(|A|-1)+1,
 \qquad S=|D+D|,
\]

and write `J(x,y)=(-y,x)`.  The common orthogonal energy

\[
 \mathcal E_\perp(D)
 =|\{(x,y,u,v)\in D^4:x+Jy=u+Jv\}|
 \tag{1.1}
\]

is the second moment of the representation function of `D+JD`.

For each collision in (1.1), order the four oriented vectors by squared
length, breaking the possible antipodal/zero ties by a fixed lexicographic
rule.  Let `delta` be the largest vector and retain one bit recording whether
it is the unrotated or rotated component of its representation.  If `delta`
belongs to `(x,y)`, record the ordinary sum `u+v` of the *other*
representation; if it belongs to `(u,v)`, record `x+y`.  This defines

\[
 \Phi(x,y,u,v)=(\text{role},\delta,s_{\rm other})
 \in\{0,1\}\times D\times(D+D).                 \tag{1.2}
\]

Let `f(lambda)=|Phi^(-1)(lambda)|` and

\[
 \mathcal M_{\rm sw}(D)=\sum_\lambda f(\lambda)^2. \tag{1.3}
\]

Since `|supp(f)|<=2NS`, Cauchy gives the exact implication

\[
 \boxed{\mathcal M_{\rm sw}(D)\le N^{1+o(1)}S}
 \quad\Longrightarrow\quad
 \mathcal E_\perp(D)\le N^{1+o(1)}S.             \tag{1.4}
\]

Indeed,

\[
 \mathcal E_\perp(D)^2
 =\left(\sum_\lambda f(\lambda)\right)^2
 \le 2NS\,\mathcal M_{\rm sw}(D).
\]

The conclusion in (1.4) is exactly the orthogonal energy--support gate, and
hence implies

\[
 |D+D|\,|D+JD|\ge N^{3-o(1)}.
\]

For a distance-Sidon subset of `[m]^2`, this would give
`|A|<=m^(2/3+o(1))` and settle the order of magnitude of Erdos problem 1208.

The choice of the *other* representation in (1.2) matters.  Recording the
sum of the representation containing `delta` merely ranks representations
of one element of `D+JD`; it cannot exploit the full `D x (D+D)` target.

## 2. Exact fibre equation

Suppose the largest vector is the unrotated member `u` of the second
representation, and the key records `s=x+y`.  Put `L=I+J`.  The collision
equation is equivalent to

\[
 y=s-x,\qquad v=s+Ju-Lx.                         \tag{2.1}
\]

Thus the physical fibre is the triple intersection

\[
 \{x\in D:s-x\in D,\ s+Ju-Lx\in D,\
              |x|,|s-x|,|s+Ju-Lx|\le |u|\}.     \tag{2.2}
\]

The two orderings of a non-diagonal collision deliberately receive the same
key.  Consequently fibre two is normal; the excess above two is the actual
endpoint-switching ambiguity.

Finite exact profiles support the averaged, not pointwise, formulation.  On
the 20-point relation-closure witness, (1.2) has energy `1,735,609`, image
`777,087`, average occupied fibre `2.23348...`, and maximum fibre `25`.
On the 31-point transformed parabola it is injective because the common
energy is purely diagonal.  On the 40-point perpendicular-ruler witness its
average occupied fibre is `1.75914...` and its maximum fibre is `4`.
These figures are evidence only; the next section gives the rigorous
asymptotic obstruction to every maximum-fibre theorem.

## 3. A quadratic switching fibre is compatible with distance-Sidonicity

For every `h` there is a distance-Sidon set `A_h` of

\[
 k=4h+2                                                     \tag{3.1}
\]

points for which one key of (1.2) has at least

\[
 2h^2=\Omega(k^2)=\Omega(N)                                \tag{3.2}
\]

ordered preimages.  Hence the trivial power scale for the maximum fibre is
sharp.  In particular, neither an `N^(o(1))` maximum-fibre bound nor any
pointwise route to the cube-root theorem can be true.

Identify the plane with the complex numbers and write `L=1+i`.  Choose two
disjoint generic `h`-point sets

\[
 P_I=\{p_i:i\in I\},\qquad P_J=\{p_j:j\in J\}
\]

in two small separated discs.  All differences
`x_ij=p_i-p_j` may therefore be placed in one open cone.  Choose a long
vector `c` positive on `L x_ij`, put `u=-ic` (so `iu=c`), and take arbitrary
generic translations `T,W`.  Adjoin

\[
 q_i=T+c-Lp_i,\qquad r_j=T-Lp_j,\qquad W,\ W+u.              \tag{3.3}
\]

Thus

\[
 A_h=P_I\cup P_J\cup\{q_i:i\in I\}\cup\{r_j:j\in J\}
       \cup\{W,W+u\}.
\]

For every `(i,j) in I x J`, set

\[
 x=x_{ij},\qquad y=-x,\qquad
 v=q_i-r_j=c-Lx.                                            \tag{3.4}
\]

Then all four vectors belong to `D=A_h-A_h`, and

\[
 u+iv=x+iy.                                                  \tag{3.5}
\]

Taking `c` sufficiently long inside the prescribed cone ensures
`|u|>|x|,|y|,|v|`.  Therefore `u` is selected by (1.2), while the other
ordinary sum is always `x+y=0`.  The `h^2` physical collisions and their
reversals all map to the single key `(unrotated,u,0)`, proving (3.2).

It remains to justify that the parameters may be chosen distance-Sidon.
Every point in (3.3) is a complex-linear form in the independent variables
`p_i,c,T,W`.  Two squared edge lengths are identically equal precisely when
the Hermitian outer products of their coefficient vectors agree.  Any
candidate identity involves at most four indices from each of `I,J`.
`verify_orthogonal_switching_rich_tail.py` performs the complete side-four
symbolic check and finds no repeated edge signature.  Hence all unwanted
equalities are proper polynomial hypersurfaces.  The cone and strict-length
conditions are open, so one may avoid the finitely many hypersurfaces with
rational parameters and then scale to the integer lattice.

The same verifier contains an 18-point integral instance (`h=4`) with
`N=307`.  It checks all 153 pairwise squared distances, the 16 physical
solutions, and the resulting 32 ordered preimages of one switching key.

## 4. What the barrier does and does not kill

The construction is intentionally generic away from its one heavy key, so
`|D+D|` is essentially maximal.  A single fibre of size `Theta(N)`
contributes only `Theta(N^2)` to (1.3), while the permitted right side
`NS` is on the `N^3` scale.  Thus it does **not** threaten the averaged gate
(1.4).

What it kills is the tempting shortcut

\[
 \max_\lambda f(\lambda)\le N^{o(1)}.
\]

The live statement must instead be a rich-tail or global charge: quadratic
fibres are allowed, but a large population of them must force ordinary
support.  A convenient exact target is (1.4), or equivalently a summable tail
for the keys of (1.2).  This is strictly more endpoint-aware than the raw
common-energy gate and is the correct restart point for the switching lane.
