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

There is an even cleaner fixed-component version, which is now the preferred
gate.  Do not select a longest vector; simply put

\[
 \Psi(x,y,u,v)=(u,x+y)\in D\times(D+D),           \tag{1.5}
\]

and let

\[
 g(u,s)=|\Psi^{-1}(u,s)|.
\]

Then

\[
 \boxed{\mathcal M_{\rm fix}(D):=\sum_{u,s}g(u,s)^2
        \le N^{1+o(1)}S}                         \tag{1.6}
\]

also implies the energy--support gate, now without the factor two:

\[
 \mathcal E_\perp(D)^2
 \le NS\,\mathcal M_{\rm fix}(D).
\]

Unlike (1.2), (1.5) has no tie convention and its fibres admit the exact
formula

\[
 g(u,s)=\sum_x1_D(x)1_D(s-x)1_D(s+Ju-(I+J)x).    \tag{1.7}
\]

Thus (1.6) is a seven-incidence theorem.  After writing `x'=x+r`, a pair of
preimages contributes the seven conditions

\[
 x,x+r,y,y-r,v,v-(I+J)r,
 \quad u=x+Jy-Jv\in D.                           \tag{1.8}
\]

Dropping the last incidence reduces (1.8) to the raw dilation moment
`sum_r R_D(r)^2 R_D((I+J)r)`, which is far too large (already more than
`88 N S` on the transformed 31-point parabola).  The final membership
`u in D` is load-bearing and must not be relaxed.

The exact fixed-component profiles `(energy,image,max,moment)` are

\[
\begin{array}{c|r|r|r|r}
\text{closure }k=20&1,735,609&1,301,863&22&2,975,097\\
\text{parabola }k=31&866,761&866,761&1&866,761\\
\text{quadratic instance }k=18&101,801&99,129&25&112,689.
\end{array}                                      \tag{1.9}
\]

For the closure witness the last entry is `0.48509... N S`, substantially
smaller than the longest-selected moment in (1.3).  Formula (1.6), or a
summable tail for `g`, is therefore the preferred restart point.  The
longest-selected map remains useful as the route by which the endpoint
structure and the quadratic obstruction were discovered.

### 1.1 The diagonal is absorbable

There is no need to prove all of (1.6) directly.  Since every fibre is a set
of distinct `x` values,

\[
 \mathcal M_{\rm fix}=\mathcal E_\perp+\mathcal O,\qquad
 \mathcal O=\sum_{u,s}g(u,s)(g(u,s)-1).           \tag{1.10}
\]

The first term is the original energy, not a new error.  If

\[
 \boxed{\mathcal O\le N^{1+o(1)}S,}               \tag{1.11}
\]

then Cauchy gives

\[
 \mathcal E_\perp^2
 \le NS(\mathcal E_\perp+N^{1+o(1)}S),
\]

and solving this quadratic yields
`mathcal E_perp<=N^(1+o(1))S`.  Thus only genuinely distinct preimages must
be charged.  The exact off-diagonal values are `1,239,488` on closure-20,
zero on parabola-31, `12,604` on the perpendicular-ruler-40 witness, and
`10,888` on the 18-point quadratic instance.  Their respective ratios to
`NS` are `0.20210...`, zero, `1.88*10^(-5)`, and `0.001486...`.

More generally, fix `H=N^(o(1))`.  Fibres with `g(u,s)<H` contribute at most
`H mathcal E_perp` to (1.10), and this term is absorbed by the same quadratic
argument.  It is enough to charge pairs from the **heavy fibres**

\[
 \{(u,s):g(u,s)\ge H\}.                           \tag{1.12}
\]

This removes the misleading finite obstruction in which many unrelated
two-element fibres hit the same later key.

### 1.2 The endpoint midpoint charge

For a nonzero `d=a-b in D`, let

\[
 m(d)=a+b\in C:=A+A.                              \tag{1.13}
\]

The ordered endpoints are unique, so `m(d)` is canonical and
`m(-d)=m(d)`.  Give zero any fixed diagonal decoration `m(0)=2a_0`.
For two distinct preimages `x,x'` of one fixed-component key `(u,s)`, put

\[
 \Theta(u,s,x,x')=(u,m(x)-m(x'))
       \in D\times(C-C)=D\times(D+D).             \tag{1.14}
\]

Hence the following would be an exact sufficient endpoint theorem:

> For some `H=N^(o(1))`, the restriction of `Theta` to fibres of size at
> least `H` has average multiplicity `N^(o(1))`.

It implies (1.11), then (1.6), and finally the cube-root solution.  It uses
the unique endpoint decoration which the radial transversal lacks, retains
the original fibre label until small fibres are removed, and has exactly the
`D x (D+D)` target budget.  Section 1.3 records why the assertion is false
without also charging the ordinary support it creates.

On closure-20, threshold `H=6` leaves 2,399 heavy fibres and 120,056 ordered
off-diagonal pairs.  Their midpoint charge has 103,909 images, average load
`1.1554...`, and maximum load 12.  At `H=8` the corresponding figures are
483 fibres, 57,608 pairs, 53,749 images, average `1.0718...`, and maximum
12.  These are exact finite checks, not a proof of the asymptotic endpoint
theorem.

### 1.3 The unrestricted endpoint theorem is false

`ENDPOINT_MIDPOINT_SIDON_RULER_BARRIER.md` inserts a dense integer Sidon
ruler into the quadratic fibre from Section 3.  For every `h`, the resulting
distance-Sidon set has a fixed fibre of size `h^2=Theta(N)`.  The `Theta(h^4)`
ordered distinct pairs in that fibre occupy only `O(h^2)` endpoint-midpoint
charges, so their average charge multiplicity is `Omega(N)`.  The failure
persists after every subpolynomial heavy-fibre cutoff.

The same family has

\[
 |D+D|=\Omega(N^2),                               \tag{1.15}
\]

certified by a Cartesian product of two Sidon-ruler pair-sum sets.  It is
therefore already covered by the Ruzsa high-support branch.  The corrected
restart target is not a bare subpolynomial charge bound.  It is a summable
dichotomy: high midpoint-charge multiplicity must either be dispersed, or
must pay for enough new ordinary sums to force `|D+D|>=N^(5/3-o(1))`.

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
For the fixed-component map (1.5), the same intended family gives `h^2`
preimages of `(u,0)`, still `Omega(N)`.  Thus its maximum-fibre version is
equally false.

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
