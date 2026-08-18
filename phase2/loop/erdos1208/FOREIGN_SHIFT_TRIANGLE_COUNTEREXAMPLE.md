# Foreign-shift triangle energy: exact identity and pointwise counterexample

## 1. Outcome

The third-moment identity for the rotated-support problem is exact, but its
unrestricted cubic upper bound is false: the perpendicular-ruler family has
fourth-power second moment and hence at least fourth-power third moment.  The
viable statistic is the number of ordered, pairwise-distinct,
**non-collinear** triples inside the fibres, coupled to a separate line
branch.  Its tempting pointwise strengthening is false as strongly as
possible.

Let `A` be distance-Sidon, `k=|A|`, let `J(x,y)=(-y,x)`, and put

\[
 D=(A-A)\setminus\{0\},\qquad
 r(z)=|\{(a,d)\in A\times D:z=a+Jd\}|.
\]

For a finite set `X`, write

\[
 C_3(X;u,v)=|X\cap(X-u)\cap(X-v)|.
\]

Then

\[
 \boxed{\sum_z r(z)^3
 =\sum_{u,v} C_3(JA;u,v)C_3(D;u,v).}              \tag{1.1}
\]

The right side is a common three-point correlation, not the ordinary common
additive energy studied in the existing Shkredov literature.  Published
common-energy theorems are inverse/small-doubling statements for the
four-variable energy `E(X,Y)`; they do not provide the upper bound needed
here.  This was checked directly against arXiv:1405.3132, arXiv:2408.08113,
and arXiv:2502.20702.

For pairwise-distinct non-collinear `a,b,c`, the candidate pointwise lemma

\[
 C_3(D;J(b-a),J(c-a))\le k^{1+o(1)}              \tag{1.2}
\]

for non-collinear `a,b,c in A` is false.  There are arbitrarily large
distance-Sidon sets and a fixed non-collinear triangle in each set for which
the left side is `Omega(k^2)`.  The exact 129-point certificate in
`verify_foreign_shift_triangle_counterexample.py` has codegree 3,610, or
`0.2169... k^2`.

Thus no maximum-codegree bound can prove the desired transverse moment.  Any
successful theorem must average over the approximately `k^3` non-collinear
triangles of `A`, allowing a sparse exceptional family of quadratically
popular triangles, and then couple that estimate to the line-structured
branch.

## 2. Proof of the identity

Expand the left side as ordered triples `(a_i,d_i)`, `i=1,2,3`, with a common
value

\[
 a_1+Jd_1=a_2+Jd_2=a_3+Jd_3.
\]

Put

\[
 u=J(a_2-a_1),\qquad v=J(a_3-a_1).
\]

The common-value equations are equivalent to

\[
 Ja_2=Ja_1+u,\quad Ja_3=Ja_1+v,
 \qquad d_2=d_1+u,\quad d_3=d_1+v.
\]

Choosing `(Ja_1,d_1,u,v)` gives exactly the right side of (1.1).

Since

\[
 I:=\sum_zr(z)=|A||D|=k^2(k-1),
\]

Hölder gives

\[
 |A+JD|\ge \frac{I^{3/2}}
 {(\sum_zr(z)^3)^{1/2}}.                         \tag{2.1}
\]

Consequently the formally sufficient estimate

\[
 \sum_zr(z)^3\le k^{3+o(1)}                     \tag{2.2}
\]

would prove `|A+JD|>=k^(3-o(1))` and hence the expected square-grid upper
bound `F_2(n)<=n^(1/3+o(1))`.  It is not a viable conjecture: the
perpendicular-ruler obstruction already has `sum_z r(z)^2=Omega(k^4)`, so
its third moment is at least that large.  More generally, if such a full
moment bound `k^(3+alpha+o(1))` were available, it would give

\[
 F_2(n)\le n^{1/(3-\alpha/2)+o(1)}.             \tag{2.3}
\]

The identity must therefore be restricted before it can be used.

Let `L` be the maximum number of collinear points of `A`, let `F_z` be the
set of `A`-coordinates in the fibre over `z`, and let `t_z` be the number of
ordered, pairwise-distinct, non-collinear triples in `F_z`.  For `L>=2`,

\[
 r(z)^3\le 4t_z+9L^2r(z).                       \tag{2.4}
\]

Indeed, if `r(z)>=2L+2`, at most half of its distinct triples are collinear
and `(r)_3>=r^3/2`; if `r(z)<2L+2`, then `r(z)^3<=9L^2r(z)`.
Writing

\[
 T_{\rm nc}(A)=\sum_z t_z,
\]

we obtain the rigorous interface

\[
 |A+JD|\gg
 \frac{k^{9/2}}{(T_{\rm nc}(A)+k^3L^2)^{1/2}}. \tag{2.5}
\]

Thus `T_nc(A)<=k^(3+o(1))` proves cubic support in the genuinely wide regime
`L=k^o(1)`.  For larger `L`, (2.5) loses powers and must be coupled to the
parallel-line support lemma; this intermediate-range coupling remains open.

## 3. Infinite counterexample to the pointwise lemma

The construction has three steps.

### 3.1 A dense Costas difference core

Let `p>7` be prime, let `g` be a primitive root modulo `p`, and put

\[
 W_p=\{(i,[g^i]_p):0\le i<p-1\}\subset\mathbb Z^2.
\]

This is a Welch Costas array, hence vector-Sidon.  Let
`D_0=(W_p-W_p)\setminus{0}` and reduce its two coordinates modulo `p-1` and
`p`.  The reduction map is a bijection

\[
 D_0\longrightarrow
 (\mathbb Z_{p-1}\setminus\{0\})
 \times(\mathbb Z_p\setminus\{0\}).             \tag{3.1}
\]

Indeed, if `h=i-j` modulo `p-1`, then

\[
 g^i-g^j=g^j(g^h-1),
\]

so every pair of nonzero residues `(h,y)` determines `j`, and then `i`,
uniquely.

Take modular shifts

\[
 \bar u=(5,0),\qquad \bar v=(0,1).
\]

There are exactly `(p-3)(p-2)` residue points `x` for which
`x,x+bar u,x+bar v` all lie in the target of (3.1).  Lift these three points
uniquely to `d_0,d_1,d_2 in D_0` and record

\[
 U=d_1-d_0,\qquad V=d_2-d_0.
\]

Each coordinate has only a bounded number of possible carries, so there are
at most a fixed number of pairs `(U,V)`.  Pigeonhole therefore gives one pair
with

\[
 |D_0\cap(D_0-U)\cap(D_0-V)|\gg p^2.            \tag{3.2}
\]

Every such pair is nonparallel.  Modulo `p`, one has `U_2=0`, `V_2=1`, and
`det(U,V)=U_1`.  But `U_1` lies between `-2p+4` and `2p-4` and is congruent
to 5 modulo `p-1`; it therefore cannot be `-p,0`, or `p`.  Hence its residue
modulo `p` is nonzero.

The residues also show `U,V notin D_0`.  If `U-V in D_0`, delete one endpoint
of that unique directed edge.  This deletes at most `2(p-2)` difference
vectors, hence at most `6(p-2)` witnesses from (3.2).  We retain a
vector-Sidon core `W'_p` with a quadratic number of witnesses and with

\[
 U,V,U-V\notin W'_p-W'_p.                       \tag{3.3}
\]

### 3.2 Separate every Euclidean norm

There is an integral nonsingular linear map `T` for which all vectors in

\[
 (W'_p-W'_p)/\{\pm1\}\ \cup\ \{U,V,U-V\}
\]

have different squared norms after applying `T`.  For each two vectors not
equal up to sign, the equation `|Tx|^2=|Ty|^2` is a proper polynomial
hypersurface in the four entries of `T`.  A finite union of these
hypersurfaces, together with `det(T)=0`, cannot cover `Z^4`.

Thus `B=T(W'_p)` is distance-Sidon, and the three prospective anchor lengths
`|TU|,|TV|,|T(U-V)|` are distinct from one another and from every distance in
`B`.

### 3.3 Add one anchor triangle

Put `U'=TU`, `V'=TV`.  For an integer translate `t`, add

\[
 a=t,\qquad b=t-JU',\qquad c=t-JV'.             \tag{3.4}
\]

Only finitely many lines and circles in the `t`-plane cause a cross-distance
collision, so an integer `t` can be chosen outside them.  Then

\[
 A=B\cup\{a,b,c\}
\]

is distance-Sidon.  Moreover

\[
 J(b-a)=U',\qquad J(c-a)=V'.
\]

For every surviving `x` in (3.2), the output

\[
 z=a+J(Tx)
\]

has a fibre containing all three anchors, using the three core difference
vectors `Tx`, `Tx+U'`, and `Tx+V'`.  These outputs are distinct, proving the
quadratic fixed-triangle codegree.

## 4. The cubic averaged target is sharp

The construction can be repeated for a linear number of anchor triangles.
Choose `delta p` modular pairs

\[
 \bar u_i=(a_i,0),\qquad \bar v_i=(0,b_i)
\]

with the `a_i` and `b_i` distinct and confined to intervals avoiding their
negatives.  The same bounded-carry argument supplies shifts `U_i,V_i`, each
with `Omega(p^2)` witnesses.  Their residues make all vectors
`U_i,V_i,U_i-V_i` distinct up to sign.

For every `U_i-V_i` that is an actual core difference, delete one endpoint
of that edge.  At most `delta p` vertices are deleted.  For any one pattern,
these deletions destroy at most `O(delta p^2)` witnesses, so choosing `delta`
smaller than the absolute carry-pigeonhole constant preserves
`Omega(p^2)` witnesses for every pattern.

One integral map can separate the norms of all surviving core differences
and all `3 delta p` special vectors.  Add the anchor triangles one at a time;
at each step a generic integer translate avoids the finitely many new
distance-collision curves.  The resulting distance-Sidon set still has
`Theta(p)` points and contains `Theta(p)` non-collinear triangles, each with
`Omega(p^2)` fibre codegree.

Thus even the contribution from pairwise distinct, non-collinear fibre
triples can be `Omega(k^3)`.  The proposed transverse bound
`T_nc(A)<=k^(3+o(1))`, if true in the needed wide regime, is sharp in
exponent; it cannot be improved to `o(k^3)` and it must permit a linear
family of quadratically popular triangles.

## 5. Exact finite certificate

The verifier uses `p=127`, `g=3`, and

\[
 T(x,y)=(x+93y,94y).
\]

It takes `U=T(5,0)=(5,0)`, `V=T(0,4)=(372,376)` and adds the anchors

\[
 (100,10000),\quad(100,9995),\quad(476,9628).
\]

It checks, using integer arithmetic only:

* all 8,256 unordered distances among the 129 points are distinct;
* all nonzero directed core differences are distinct;
* the anchor triangle is non-collinear and induces shifts `U,V`;
* exactly 3,610 core differences `x` also have `x+U,x+V` in the core
  difference set;
* the resulting 3,610 outputs are distinct fibres containing the anchor
  triangle.

Run:

```text
python3 phase2/loop/erdos1208/verify_foreign_shift_triangle_counterexample.py
```

## 6. General anchor-lifting lemma

The single triangle is an instance of a reusable transfer principle.

**Anchor-lifting lemma.**  Let `B,U subset Z^2` be finite vector-Sidon sets
such that

\[
 ((B-B)\setminus\{0\})\cap
 ((U-U)\setminus\{0\})=\varnothing.             \tag{6.1}
\]

There are an integral nonsingular linear map `T` and an integer translate
`t` for which

\[
 A=T(B)\ \cup\ \{t-JT(u):u\in U\}              \tag{6.2}
\]

is distance-Sidon.  Moreover, for every ordered triple `u_0,u_1,u_2 in U`,
the corresponding anchor triangle has at least

\[
 C_3(D_B;u_1-u_0,u_2-u_0),\qquad
 D_B=(B-B)\setminus\{0\},                      \tag{6.3}
\]

fibres in `A+J(A-A)`.

To prove the metric assertion, choose `T` outside the finitely many proper
quadratic hypersurfaces that equate the norms of two vectors in
`(B-B) union (U-U)` not equal up to sign.  Condition (6.1) and the two
vector-Sidon hypotheses ensure that all these vectors are distinct up to
sign.  Then choose `t` outside the finitely many lines and circles that cause
a cross-distance collision.  Both choices can be integral.  Finally,

\[
 J((t-JT(u_j))-(t-JT(u_i)))=T(u_j-u_i),
\]

so applying `T` to every witness counted in (6.3) proves the fibre claim.

This lemma is an important limitation on purely qualitative uses of radial
uniqueness: any vector-Sidon core and disjoint vector-Sidon shift model can be
converted into a genuine Euclidean distance-Sidon example.  A successful
upper theorem must use quantitative ambient height or a global tail/line
tradeoff; radial uniqueness alone cannot suppress a prescribed finite family
of foreign-shift correlations.

### A 139-point simultaneous stress test

The file `verify_foreign_shift_anchor_constellation.py` applies the lemma to
the same `p=127` Welch core and a 13-point shift set.  The resulting integer
set has:

* 139 points and all 9,591 unordered distances distinct;
* maximum collinearity seven;
* 231 non-collinear anchor triangles;
* between 2,281 and 3,464 core witnesses for every one of those triangles;
* total ordered non-collinear moment contribution 3,918,648, which is
  `1.459... times 139^3`.

The anchors lie principally on two lines.  The example therefore does not
falsify a `k^(3+o(1))` wide-regime moment bound, but it is a sharp finite
benchmark for the missing line/transverse coupling.  It also demonstrates
that many popular triangles can coexist; the single-triangle obstruction is
not an isolated local gadget.

## 7. Correct restart target

Do not pursue a uniform upper bound for
`C_3(D;J(b-a),J(c-a))`; even `k^(2-epsilon)` is false.

For an ordered non-collinear triangle `tau=(a,b,c)`, put

\[
 q(\tau)=C_3(D;J(b-a),J(c-a)).
\]

The clean live statement is the rich-triangle tail estimate

\[
 |\{\tau:q(\tau)\ge\lambda\}|
 \le \frac{k^{3+o(1)}}{\lambda},                \tag{7.1}
\]

uniformly over dyadic `1<=lambda<=k^2`, first for sets with
`L=k^o(1)`.  Dyadic summation gives `T_nc(A)<=k^(3+o(1))`.  The many-anchor
construction is sharp for (6.1) at `lambda` of order `k^2`: it supplies
`Theta(k)` such triangles.  A full solution must then couple this tail bound
to the existing line-support theorem through the intermediate-collinearity
range.
