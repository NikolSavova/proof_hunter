# Three-side invariant coupling and parabolic sharpness gate

## Status

For a fully transverse equal-signed triangle pair, let

\[
 e_1+e_2+e_3=f_1+f_2+f_3=0,
 \qquad \det(e_1,e_2)=\det(f_1,f_2)=d\ne0,
\]

let $f_i=Me_i$ with $M\in\operatorname{SL}_2(\mathbb Q)$, and put

\[
 K_{ij}=\det(e_i,f_j),\qquad q_i=K_{ii},
 \qquad t=K_{12}-K_{21}=d\operatorname{tr}M.           \tag{0.1}
\]

Using all three side values gives two real pieces of structure.

* Away from trace $\pm2$, the three products
  $(q_1q_2,q_2q_3,q_3q_1)$ determine the entire cross-determinant matrix
  $K$ up to $m^{o(1)}$ possibilities.
* At trace $\pm2$, the possible triples $(q_1,q_2,q_3)$ occupy only
  $O(m^2\log m)$ cells, and there is an exact displacement/sumset
  description of the records.

Neither statement closes the corrected
$m^{o(1)}(k^3+m^2)$ energy gate.  The obstruction is genuine: there are
distance-Sidon sets of polynomial height with one trace-$2$ map supporting
$\Theta(h^3)$ clean fully transverse records, and a **single fixed value
triple** supports $\Theta(h)$ of them.  Thus the diagonal $k^3$ term and a
linear fixed-cell load are both necessary in any direct parabolic theorem.

This also agrees with the empirical fact that most hard records have
overlap exactly three: the missing theorem must aggregate six endpoint
labels directly, rather than rely on rich-map tails.

## 1. The full matrix is determined by three diagonal values and trace-area

Since every row and column of $K$ sums to zero, (0.1) gives

\[
\begin{aligned}
 2K_{12}&=t-q_1-q_2+q_3,&
 2K_{21}&=-t-q_1-q_2+q_3,\\
 2K_{13}&=-t-q_1+q_2-q_3,&
 2K_{31}&=t-q_1+q_2-q_3,\\
 2K_{23}&=t+q_1-q_2-q_3,&
 2K_{32}&=-t+q_1-q_2-q_3.                             \tag{1.1}
\end{aligned}
\]

The leading Pluecker minor has determinant $d^2$.  Equivalently,

\[
 \boxed{
 D(q_1,q_2,q_3):=
 q_1^2+q_2^2+q_3^2-2q_1q_2-2q_2q_3-2q_3q_1
 =t^2-4d^2.}                                          \tag{1.2}
\]

This is the symmetric form of the Pell--Heron identity.

### Proposition 1.1 (joint-product cross-matrix fibre)

Suppose every $q_i$ is nonzero and $D(q_1,q_2,q_3)\ne0$.  Fix

\[
 P_{12}=q_1q_2,\qquad P_{23}=q_2q_3,
 \qquad P_{31}=q_3q_1.                                \tag{1.3}
\]

Then there are only $m^{o(1)}$ possible integer matrices $K$ arising from
records in $[m]^2$.

### Proof

The three products determine the $q_i$ up to simultaneous sign, since

\[
 q_1^2=\frac{P_{12}P_{31}}{P_{23}},
\]

and then $q_2=P_{12}/q_1$, $q_3=P_{31}/q_1$.  For either possible triple,
(1.2) factors as

\[
 (t-2d)(t+2d)=D(q_1,q_2,q_3)\ne0.                    \tag{1.4}
\]

Thus $(t,d)$ has at most $\tau(|D|)^{O(1)}=m^{o(1)}$
possibilities.  Formula (1.1) then determines $K$. $\square$

This is a genuine all-three-side compression: one does not need to fix
$M$.  It is nevertheless only a **cross-matrix cell theorem**.  The three
products themselves have a large ambient range, and a fixed $K$ does not
currently have a proved divisor-size endpoint load.  Simultaneous
$\operatorname{SL}_2$ changes of the source and target edge frames preserve
$K$, which is the exact residual orbit that an endpoint-sensitive theorem
must control.

### Proposition 1.2 (one source and one cross matrix)

Fix an ordered noncollinear source triangle and its first two cyclic edge
vectors as the columns of $E$.  For a prescribed leading $2\times2$ block
$K_0$ of $K$, the target edge frame $F$ is forced:

\[
 E^{\mathsf T}JF=K_0,
 \qquad
 \boxed{F=-J E^{-\mathsf T}K_0}.                       \tag{1.5}
\]

If those two target vectors occur in $A$ and share the required endpoint,
their directed-vector realizations are unique by distance-Sidonicity.
Thus a fixed ordered source triangle and fixed $K$ have at most one ordered
target triangle.

Consequently, a fixed nonparabolic joint-product cell and a fixed source
triangle have only $m^{o(1)}$ targets.  In the parabolic case, fixing the
sign of the trace, the source triangle, and $(q_1,q_2,q_3)$ fixes
$t=\pm2d$, hence fixes $K$ through (1.1), and therefore fixes at most one
target.  This turns the remaining parabolic problem into a **simple
bipartite incidence graph** between at most $k^3$ ordered source triangles
and $O(m^2\log m)$ value cells.  The desired estimate is precisely a
near-linear edge bound for this endpoint-realized graph; simplicity alone,
of course, is not enough.

## 2. Parabolic value triples have an $\boldsymbol{m^2\log m}$ range

If $T=\operatorname{tr}M=\pm2$ and $M\ne\pm I$, the invariant form is

\[
 Q_M(v)=\det(v,Mv)=cL(v)^2                            \tag{2.1}
\]

for one rational linear form $L$ and one $c\in\mathbb Q^*$.  Hence the
three nonzero integers $q_i$ have one sign and one rational squareclass.
There is a signed squarefree integer $s$ and nonzero integers $r_i$ such
that

\[
 q_i=s r_i^2.                                         \tag{2.2}
\]

After choosing signs of the $r_i$, the cyclic vector relation gives

\[
 r_1+r_2+r_3=0.                                       \tag{2.3}
\]

Conversely, (2.2)--(2.3) imply the degenerate Pell--Heron identity.

Since $|q_i|\le2m^2$, for a fixed $s$ there are
$O(m^2/|s|)$ choices of $(r_1,r_2)$, and then $r_3$ is fixed.  Summing over
squarefree $s$ gives

\[
 \boxed{
 \#\{(q_1,q_2,q_3)\text{ from parabolic records}\}
 \ll m^2\log m.}                                      \tag{2.4}
\]

Thus the parabolic side has the desired ambient number of **value cells**.
The next sections show why their loads cannot be treated as uniformly
divisor-small.

## 3. Displacement and sumset characterizations

Consider three noncollinear source points $x_i$ and their targets $y_i$.
They determine a special-affine map $g(x)=Mx+a$.

### Trace $+2$

Set $\delta_i=y_i-x_i$.  Then

\[
 \delta_j-\delta_i=(M-I)(x_j-x_i).                    \tag{3.1}
\]

Because $\det M=1$, trace $M=2$ is equivalent to $M-I$ having rank at
most one.  Therefore

\[
 \boxed{\operatorname{tr}M=2
 \quad\Longleftrightarrow\quad
 \delta_1,\delta_2,\delta_3\text{ are collinear}.}     \tag{3.2}
\]

The scalar case $M=I$ is excluded by full transversality.

### Trace $-2$

Set $\sigma_i=y_i+x_i$.  Since

\[
 \sigma_j-\sigma_i=(M+I)(x_j-x_i),                    \tag{3.3}
\]

the identical argument gives

\[
 \boxed{\operatorname{tr}M=-2
 \quad\Longleftrightarrow\quad
 \sigma_1,\sigma_2,\sigma_3\text{ are collinear}.}    \tag{3.4}
\]

Thus trace $2$ is a collinearity problem in the labelled difference set,
and trace $-2$ is its labelled sumset analogue.  These are direct
three-correspondence descriptions, not rich-overlap estimates.

## 4. Clean level rigidity and its exact limit

For trace $2$, write $M-I=w\otimes L$.  On an overlap,

\[
 g(x)-x=a+L(x)w.                                      \tag{4.1}
\]

If two nonfixed overlap points have the same $L$-level, (4.1) gives two
distinct ordered edges of $A$ with the same displacement vector.  This
contradicts distance-Sidonicity.  Fixed points cannot be vertices of a
clean source/target pair.  Hence $L$ is injective on the usable part of a
trace-$2$ overlap.

For trace $-2$,

\[
 g(x)+x=a+L(x)w.                                      \tag{4.2}
\]

A distance-Sidon set is also additive Sidon: if $a+b=c+d$, then comparing
$a-c=d-b$ shows that the unordered pairs $\{a,b\}$ and $\{c,d\}$ are the
same.  Thus two points on one $L$-level in (4.2) must form a swapped
two-cycle under $g$.  A clean triangle and its disjoint image can use at
most one of them.

Consequently, for a **fixed parabolic map** and a fixed ordered nonzero
triple $(q_1,q_2,q_3)$, there are only $O(h)$ clean source triangles in an
overlap of size $h$: (2.1) fixes the three absolute $L$-level gaps up to
constantly many sign choices, and choosing the first level fixes the other
two.  The next construction shows that this linear factor is sharp.

## 5. Polynomial-height sharpness construction

### Proposition 5.1

For every $h$ there is a distance-Sidon set $A_h\subset[m]^2$ with
$m=O(h^4)$ and a trace-$2$ special-affine map $g$ such that:

1. $g$ maps $h$ points of $A_h$ to another disjoint set of $h$ points;
2. all $h(h-1)(h-2)$ ordered source triples give clean fully transverse
   equal-area records with their images;
3. at least $h-2$ of those records have the same ordered value triple
   \[
     (q_1,q_2,q_3)=(-1,-1,-4).                         \tag{5.1}
   \]

### Proof

Choose integers $C=10h$, $H=20h$ and variables $X_1,\ldots,X_h$.  Put

\[
 p_i=(X_i,i),\qquad
 g(x,y)=(x+y+C,y+H),\qquad p_i'=g(p_i),                \tag{5.2}
\]

and $A_h=\{p_i,p_i':1\le i\le h\}$.  The linear part of $g$ is

\[
 \begin{pmatrix}1&1\\0&1\end{pmatrix},               \tag{5.3}
\]

which has determinant one and trace two.  The two copies are disjoint.

We choose the $X_i$ from $\{1,\ldots,L\}$ with $L\asymp h^4$.  Equality
of the squared distances of two distinct unordered pairs in $A_h$ is a
nonzero polynomial of degree at most two in the $X_i$.  To see
nonvanishing, a pair joining indices $i\ne j$ has horizontal difference

\[
 X_i-X_j+s(i+C)-t(j+C),\qquad s,t\in\{0,1\}.           \tag{5.4}
\]

Different index sets have different quadratic support.  For the same
index set the four constants in (5.4) are
$0,i-j,i+C,-(j+C)$, which are distinct.  The pairs $p_iq_i$ have the
strictly increasing deterministic squared lengths
$(i+C)^2+H^2$.

Noncollinearity of a source triple, and nonvanishing of each of its nine
cross determinants with the image triple, are likewise nonzero
polynomials of degree at most two.  Indeed, if $r_i$ is the vertical
component of a cyclic side, then

\[
 \det(e_i,Me_j)=\det(e_i,e_j)-r_ir_j,                  \tag{5.5}
\]

whose diagonal value is $-r_i^2\ne0$ and whose off-diagonal value is a
nonconstant area polynomial minus a constant.

There are $O(h^4)$ bad polynomials altogether.  Schwartz--Zippel and a
union bound show that some choice in a box of side $L=Ch^4$ avoids all of
them.  This proves distance-Sidonicity and full transversality for every
ordered triple.  All coordinates are $O(h^4)$.

Finally, the cyclic vertical side differences of
$(p_i,p_{i+1},p_{i+2})$ are $(1,1,-2)$.  Since
$Q_M(x,y)=-y^2$, every one of these $h-2$ records has (5.1). $\square$

This construction does not violate the corrected ambient estimate—its
height is deliberately only polynomial, and the $k^3$ term is present.
It does rule out two tempting intermediate claims:

* a fixed parabolic value triple need not have $m^{o(1)}$ load;
* the parabolic contribution need not be smaller than the diagonal cubic
  term.

## 6. Exact remaining gate

The three-side algebra now separates the problem cleanly.

* **Nonparabolic integer trace:** a joint-product cell has only
  $m^{o(1)}$ possible cross matrices, but a fixed cross matrix still has an
  uncontrolled endpoint-realized simultaneous-$\operatorname{SL}_2$
  orbit.
* **Parabolic trace:** there are only $O(m^2\log m)$ value triples, but
  their loads have an unavoidable linear diagonal component.  Since the
  dominant empirical maps have overlap exactly three, summing per-map rich
  tails cannot remove it.

Equivalently, Proposition 1.2 has reduced the parabolic branch to proving
that its simple source-triangle/value-cell incidence graph has
$m^{o(1)}$ degeneracy after the unavoidable planted stars are charged to
the $k^3$ diagonal term.  The construction in Section 5 shows why a
uniform bound on the degree of a value-cell vertex is false.

What is still needed is a global six-label estimate of the form

\[
 \sum_{\text{three-side cells}}
   \bigl(\text{load}-\text{diagonal allocation}\bigr)_+
 \le m^{2+o(1)},                                      \tag{6.1}
\]

or an equivalent endpoint incidence theorem.  The invariant values give
the correct parabolic range, but the construction proves that the
diagonal allocation must be retained explicitly.

## 7. Verification

Run:

```bash
python phase2/loop/erdos1208/verify_three_side_invariant_coupling_parabolic_sharpness.py
```
