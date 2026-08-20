# Universal-matrix and ruler-arm stress for the metric scalar charge

## 1. Outcome

The proposed finite-field-parabola counterexample based on collisions

\[
 uu^T+18vv^T=u'u'^T+18v'v'^T                 \tag{1.1}
\]

does not work.  In fact (1.1) has only subpolynomially many representations
per matrix key, for completely elementary positive-definite reasons.  Exact
counts on the largest clean fibres of the integer finite-field parabola are
within `0.07%` of the diagonal through `p=61`.

There is a stronger conclusion.  An explicit polynomial-height integral
linear map simultaneously

1. separates all Euclidean edge lengths of the finite-field parabola, and
2. separates every two *different* matrix keys in (1.1).

Thus the resulting genuine integral distance-Sidon sets have quadratic
clean fibres but metric-scalar energy

\[
 \mathcal M_{q,18}=m^{o(1)}|H_q|N.             \tag{1.2}
\]

The finite-field parabola therefore passes, rather than kills, the scalar
gate after a suitable metric separation.

The natural two-, three-, and four-ruler-arm extensions were also tested,
including arm scales growing with the family size.  No polynomial excess
appears.  Two rigorous no-go theorems explain this:

* all internal-arm versus internal-arm blocks have subpolynomial load,
  uniformly in polynomially growing arm directions and scales;
* for a subpolynomial number of parallel ruler lines, the *entire* scalar
  charge has near-diagonal energy, including cross-line edges.

The remaining ruler-based counterexample lane is sharply isolated: ordinary
edges crossing two genuinely transverse arms.  That block leads to a
ternary positive quadratic form rather than a binary one.  It is not settled
by the present argument, although the necessary Golomb span removes the
naive lattice-point gain and every exact test remains essentially diagonal.

## 2. Universal matrix collisions are divisor-scale

Fix a positive integer `C` and define

\[
 K_C(u,v)=uu^T+Cvv^T,
 \qquad u,v\in[-M,M]^2\cap\mathbb Z^2.         \tag{2.1}
\]

**Proposition 2.1.**  Every fibre of `K_C` has size `M^(o(1))`, uniformly in
the choice of subsets from which `u` and `v` are drawn.

Write `u=(x,y)` and `v=(z,w)`.  If

\[
 K_C(u,v)=\begin{pmatrix}a&b\\b&d\end{pmatrix},
\]

then its diagonal entries give

\[
 x^2+Cz^2=a,\qquad y^2+Cw^2=d.                 \tag{2.2}
\]

For fixed `C`, each positive binary quadratic form in (2.2) has
`M^(o(1))` representations by the standard divisor bound in the fixed
imaginary quadratic order of discriminant `-4C`.  The two equations together
still have only `M^(o(1))` choices; the off-diagonal equation only filters
them.  The zero diagonal cases are smaller.

Consequently, for arbitrary finite vector sets `U_1,U_2` in the box,

\[
 \sum_K r_{K_C}(K)^2
 \le M^{o(1)}|U_1||U_2|.                        \tag{2.3}
\]

This also diagnoses the failed `p^5` dimension heuristic.  The three matrix
entries have scale `p^2`, not scale `p`; already the two positive diagonal
equations are divisor-rigid.  Universal metric collisions can never supply a
fixed-power excess, on the parabola or on any other family.

## 3. An explicit parabola lift which realizes exactly the universal energy

Let

\[
 P_p=\{(x,x^2\bmod p):0\le x<p\}\subset\mathbb Z^2.        \tag{3.1}
\]

As in `FINITE_FIELD_PARABOLA_DILATED_CHARGE_BARRIER.md`, this is
vector-Sidon and some clean fibre has `h=Omega(p^2)`.  Put

\[
 Q=(C+1)(p-1)^2,\qquad B=2Q+1,
 \qquad
 L=\begin{pmatrix}1&B\\0&3B\end{pmatrix}.       \tag{3.2}
\]

The Gram matrix is

\[
 G=L^TL=\begin{pmatrix}1&B\\B&10B^2\end{pmatrix}.          \tag{3.3}
\]

Every entry of `K_C(u,v)` for differences of `P_p` has diagonal entries in
`[0,Q]` and off-diagonal entry in `[-Q,Q]`.  The scalar charge after applying
`L` is the integer encoding

\[
 \operatorname{tr}(G K_C)
 =K_{11}+2B K_{12}+10B^2K_{22}.                 \tag{3.4}
\]

This encoding is injective on distinct matrix keys.  If two keys have equal
`K_22` but different `K_12`, then `2B>|Delta K_11|`; if both coordinates
agree, `K_11` decides.  If their `K_22` coordinates differ, then

\[
 10B^2>Q+4BQ
\]

makes the last term dominate both lower terms.  The same argument, with
`C=0`, separates the rank-one matrices `uu^T` belonging to distinct edges.
Vector-Sidonicity says two different unordered edges never have the same
rank-one matrix.  Therefore

\[
 A_p=L(P_p)                                      \tag{3.5}
\]

is distance-Sidon.

The map is linear, so it preserves every clean pair-sum relation and the
quadratically large fibre.  Equations (2.3)--(3.4) show that the scalar
energy on `A_p` is *exactly* the universal matrix energy and hence satisfies
(1.2).  Finally, `B=O_C(p^2)`, so `A_p` has coordinate width

\[
 m=O_C(p^3).                                    \tag{3.6}
\]

Thus all exponent conversions are legitimate: `p^(o(1))=m^(o(1))`.

## 4. Why a planted local gadget is qualitatively different

For finite integer sets `B,D_0`, put

\[
 E_C(B,D_0)=\#\{b_1+Cd_1=b_2+Cd_2\}.
\]

Fixing `(b_1,b_2,d_1)` determines `d_2`, and symmetrically, so

\[
 E_C(B,D_0)
 \le\min\bigl(|B|^2|D_0|,\ |B||D_0|^2\bigr).   \tag{4.1}
\]

A fixed clean gadget has `|B|=O(1)`, even after adding an arbitrary cloud of
`N` other distance labels; (4.1) gives only `O(N)` energy.  More generally,
a construction controlling only `O(k)` clean labels and `O(k)` ordinary
edge labels supplies at most `O(k^3)`, exactly the scale already paid for by
the weak target `N(h+k)`.

An asymptotic attack must therefore provide either a genuinely heavy clean
fibre, or superlinearly many coherently structured ordinary edge labels.
The two-arm construction does provide `h=Omega(k^2)`; the point of the next
section is that positivity nevertheless destroys its internal-arm
resonance.

## 5. Uniform no-go for internal ruler-arm blocks

The needed representation bound is uniform even when the arm scales grow.

**Lemma 5.1.**  If positive integers `A,B,n` are at most `m^O(1)`, then

\[
 \#\{(x,y)\in\mathbb Z^2:Ax^2+By^2=n\}=m^{o(1)}.            \tag{5.1}
\]

If `g=gcd(A,B)` does not divide `n`, there are no solutions.  Otherwise put
`a=A/g`, `b=B/g`, and `c=n/g`.  A solution gives the
algebraic integer

\[
 \alpha=ax+y\sqrt{-ab},\qquad N(\alpha)=ac
\]

in the imaginary quadratic field `Q(sqrt(-ab))`.  The number of integral
ideals of norm `ac` is at most `tau(ac)`: at each rational prime the local
coefficient is at most one plus its exponent.  Each principal ideal has at
most six generators of a prescribed norm, since an imaginary quadratic
field has at most six units.  Hence the left side of (5.1) is at most
`6 tau(ac)=m^(o(1))`, uniformly in the discriminant.

Now let `A` be a distance-Sidon union of `r` affine ruler arms

\[
 T_i+R_i v_i,\qquad 1\le i\le r,               \tag{5.2}
\]

where all coordinates and direction norms are polynomial in `m`.  Restrict
the scalar-charge records to those for which the clean source edge is
internal to arm `i` and the ordinary edge is internal to arm `j`.  Their
labels have the form

\[
 |v_i|^2x^2+C|v_j|^2y^2.                       \tag{5.3}
\]

Lemma 5.1 makes every `(i,j)` block `m^(o(1))`-to-one.  Summing the `r^2`
blocks and using Cauchy gives

\[
 E_{\rm internal/internal}
 \le r^2m^{o(1)}\,|\mathcal R_{\mathrm{internal/internal}}|.    \tag{5.4}
\]

In particular, any subpolynomial number of arms is near-diagonal on the
entire mechanism which killed the vector charges.  This includes variable
integer scalings and arbitrary polynomially large direction norms.

## 6. Complete no-go for parallel multi-line rulers

For parallel arms one can include every cross-line edge as well.

**Theorem 6.1.**  Suppose a distance-Sidon set lies on `r=m^(o(1))`
parallel integral lines of primitive direction `v`, with polynomially
bounded parameters.  Then for every clean fibre and fixed positive `C`,

\[
 \mathcal M_{q,C}\le m^{o(1)}|H_q|N.           \tag{6.1}
\]

Write `V=|v|^2`.  An edge joining line `i` to line `j` has displacement

\[
 T_{ij}+wv.
\]

Put `P=T_ij dot v` and
`Delta=V|T_ij|^2-P^2=det(T_ij,v)^2`.  Completing the square gives

\[
 V|T_{ij}+wv|^2=(Vw+P)^2+\Delta.               \tag{6.2}
\]

Partition a scalar-charge fibre by the unordered line pair of its source
edge and the unordered line pair of its ordinary edge.  For a fixed pair of
types, (6.2) turns the charge equation into

\[
 X^2+CY^2=M                                     \tag{6.3}
\]

with a type-dependent constant `M`.  Distance-Sidonicity makes the map from
records to `(X,Y)` injective, while the fixed binary form has `m^(o(1))`
representations.  There are `O(r^4)` type pairs.  Cauchy across them gives
`r^4m^(o(1))|H_q|N`, which is (6.1).

Thus adding parallel lines, offsets, or variable scalar dilations to a
ruler cannot defeat the positive scalar charge.

## 7. Genuine multi-arm constructions and the transverse bottleneck

For fixed `r`, split a dense `rs`-mark Golomb ruler among `r` arms.  Each
arm lies in an interval of length `O_r(s^2)`, so the equal-triple-sum
argument from `GAUSSIAN_EDGE_VECTOR_TWO_ARM_BARRIER.md` gives an internal
clean subfibre of size `Omega_r(s^2)` on some arm.

These can be made genuine integral distance-Sidon families of polynomial
height.  Give the arm translations and direction coordinates independent
integer parameters.  Every unwanted equality between two different
squared distances is a nonzero polynomial in those parameters; the only
identically equal internal cases are excluded by the global Golomb ruler.
The product of the `O_r(s^4)` forbidden polynomials is nonzero.  Evaluating
on an integer grid whose side exceeds its total degree supplies polynomially
bounded integral parameters avoiding all collisions.  Internal clean
relations on each arm are affine identities and survive this choice.

For an ordinary edge crossing two nonparallel arms, however, its squared
length is an inhomogeneous positive binary quadratic polynomial in two ruler
marks.  Adding an internal source square produces a ternary quadratic form.
Ternary forms can have polynomial representation numbers, so Lemma 5.1 no
longer applies.

There is an exact height loss in the naive version of this idea.  An
`s`-mark integral ruler with distinct internal distances has at least
`binom(s,2)` distinct positive integer gaps, hence span at least
`binom(s,2)=Omega(s^2)`.  Its transverse squared-distance form therefore
lives naturally on scale `s^4`.  The candidate block has only `s^4`
records, so a range count or the usual full-box ternary representation
heuristic gives no compression at all.  Producing a counterexample would
require special additive concentration beyond generic lattice-point
counts, while retaining injectivity of every individual distance label.

This transverse cross-arm block is the precise unresolved construction
lane, not the internal ruler resonance and not a finite planted gadget.

## 8. Exact profiles

The verifier reports the following universal-matrix profiles on the largest
finite-field-parabola clean fibre:

\[
\begin{array}{c|r|r|r|r|r}
p&hN&|\operatorname{im}K_{18}|&E(K_{18})&\max r&E/(hN)\\ \hline
17&1{,}904&1{,}904&1{,}904&1&1.000000\\
31&39{,}990&39{,}982&40{,}006&2&1.000400\\
43&154{,}413&154{,}363&154{,}513&2&1.000648\\
61&614{,}880&614{,}754&615{,}132&2&1.000410
\end{array}
\]

It also applies the explicit map (3.2), checks distance-Sidonicity, and
checks that the transformed scalar energy equals the matrix energy exactly.

There is a useful second matrix audit.  Regard a symmetric matrix as the
three-vector `(K_11,2K_12,K_22)`.  A primitive direction which already
occurs between two single-edge rank-one keys is forbidden: any Gram vector
orthogonal to it would make those two edge lengths equal.  At `p=13`, the
78 edges determine 2,417 such forbidden directions.  Among all 164,639
remaining directions between distinct charge-matrix keys, the largest
multiplicity is only four.  This does not prove the needed inverse theorem,
because many different directions can lie in one Gram-orthogonal plane, but
it shows exactly why the most frequent resonances disappear once distance
uniqueness is imposed.

For genuine finite distance-Sidon ruler-arm sets, the full scalar profiles
are:

\[
\begin{array}{c|r|r|r|r}
\text{family}&k&h& E/(hN)&\max r\\ \hline
\text{two perpendicular}&80&72&1.002444&3\\
\text{two scaled, heavy fibre}&100&114&1.000620&2\\
\text{three fixed arms}&96&31&1.000453&2\\
\text{three arms, scale }s&96&31&1.000368&2\\
\text{four fixed arms}&96&15&1.000292&2\\
\text{four arms, scale }s&96&15&1.000146&2
\end{array}
\]

The `k=100,h=114` row is already in the heavy-fibre regime; its energy is
still only `1.00062` times the unavoidable diagonal.

Run

```text
python3 phase2/loop/erdos1208/verify_metric_scalar_universal_matrix_and_ruler_stress.py
```

## 9. Consequence

The positive scalar gate survives all present asymptotic attacks.  The new
parabola matrix proposal is ruled out in full generality, and the exact
two-arm vector obstruction cannot be revived by adding internal ruler arms,
variable scales, or parallel offsets.  A future counterexample must exploit
cross-distances between genuinely transverse arms (or a still less
one-dimensional geometry) and must create additive concentration not forced
by ordinary quadratic-form representation counts.
