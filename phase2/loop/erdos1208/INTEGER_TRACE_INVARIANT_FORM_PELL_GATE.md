# Integer-trace invariant form and Pell fibre gate

## Status

Let $g(x)=Mx+t$ be a fully transverse special-affine map with integer trace

\[
 T=\operatorname{tr}M\in\mathbb Z.
\]

The binary quadratic form

\[
 Q_M(v)=\det(v,Mv)                                     \tag{0.1}
\]

is invariant under $M$ and has discriminant $T^2-4$.  On the compatibility
lattice of integer vectors sent to integer vectors, it is an integral binary
quadratic form.  For $T\ne\pm2$, every fixed nonzero value has only
$m^{o(1)}$ representations in the relevant polynomial box, by the standard
quadratic-order/Pell divisor bound.

For the three cyclic sides of a fully transverse triangle, the three
nonzero values $q_i=Q_M(e_i)$ satisfy an exact Pell--Heron identity:

\[
 \boxed{
 (q_1+q_3-q_2)^2+(4-T^2)d^2=4q_1q_3.}                 \tag{0.2}
\]

Consequently, for fixed $M,q_1,q_3$, only $m^{o(1)}$ source triangles can
occur.  This is a real fibre theorem, but it does not close the aggregate
energy: the pair $(q_1,q_3)$ has an $O(m^4)$ range.

Moreover, integer trace is not a negligible exceptional case.  Between 19%
and 29% of the fully transverse six-distinct energy in the tested modular
Costas certificates has denominator-one trace.  The exact two-copy
distance-Sidon certificate from `EQUAL_AREA_TRIANGLE_ENERGY_BARRIER.md`
contains an 11-point overlap map of integer trace $13058$.  Thus a pointwise
denominator or Pell-fibre estimate cannot finish the route; one needs an
aggregate tail across the two invariant-form values.

## 1. Compatibility lattice and invariant form

Define

\[
 \Lambda_M=\{v\in\mathbb Z^2:Mv\in\mathbb Z^2\}.       \tag{1.1}
\]

If $T\in\mathbb Z$, Cayley--Hamilton gives

\[
 M^2-TM+I=0,
\]

so $M\Lambda_M=\Lambda_M$.  In a $\mathbb Z$-basis of this rank-two lattice,
$M$ is represented by an integral determinant-one matrix

\[
 \begin{pmatrix}a&b\\c&e\end{pmatrix},qquad a+e=T.
\]

Apart from the fixed covolume factor of the lattice, (0.1) becomes

\[
 Q(x,y)=cx^2+(e-a)xy-by^2,                              \tag{1.2}
\]

whose discriminant is

\[
 (e-a)^2+4bc=(a+e)^2-4=T^2-4.                          \tag{1.3}
\]

The form is invariant because

\[
 Q_M(Mv)=\det(Mv,M^2v)
 =\det(Mv,TMv-v)=\det(v,Mv)=Q_M(v).                    \tag{1.4}
\]

It is nondegenerate exactly when $T\ne\pm2$.

## 2. Uniform nonzero representation bound

### Lemma 2.1

Suppose $T\in\mathbb Z\setminus\{\pm2\}$, the entries and relevant lattice
indices are polynomially bounded in $m$, and $n\ne0$ with $|n|\le2m^2$.
Then

\[
 \boxed{
 |\{v\in\Lambda_M\cap[-m,m]^2:Q_M(v)=n\}|
 \le m^{o(1)}.}                                        \tag{2.1}
\]

### Proof

After choosing a reduced lattice basis, coordinates of vectors in the box
are polynomially bounded in $m$.  Divide (1.2) by its content.  Completing
the square converts $Q(x,y)=n'$ into

\[
 X^2-(T^2-4)Y^2=N,                                     \tag{2.2}
\]

where $N\ne0$ and $|N|\le m^{O(1)}$.

If $|T|<2$, then $T\in\{-1,0,1\}$ and this is a fixed positive-definite
quadratic-order norm equation.  If $|T|>2$, the discriminant $T^2-4$ is
positive and nonsquare: the only integer solutions of $T^2-s^2=4$ have
$T=\pm2$.  Solutions of (2.2) split into at most
$\tau(|N|)^{O(1)}$ quadratic-order divisor classes, and each unit orbit has
$O(\log m)$ representatives in a polynomial box.  The divisor estimate
gives (2.1), uniformly for polynomial-size data.  QED.

The exclusion $n=0$ is essential.  Those vectors are precisely rational
eigendirections in the split/parabolic cases; full transversality removes
them for the three contributing sides.

## 3. Pell--Heron identity for a triangle

Let cyclic side vectors satisfy

\[
 e_1+e_2+e_3=0,qquad d=\det(e_1,e_2)\ne0,
\]

and put $q_i=Q_M(e_i)$.  Take $u=e_1$ and
$w=-e_3=e_1+e_2$.  Since $q_i$ is unchanged by sign,

\[
 Q_M(u)=q_1,quad Q_M(w)=q_3,quad Q_M(w-u)=q_2.        \tag{3.1}
\]

Because $q_1=\det(u,Mu)\ne0$, $(u,Mu)$ is a basis.  Write

\[
 w=\alpha u+\beta Mu.
\]

Then

\[
 d=\det(u,w)=\beta q_1,
\]

and the invariant form has the canonical expression

\[
 Q_M(w)=q_1(\alpha^2+T\alpha\beta+\beta^2).            \tag{3.2}
\]

Polarization also gives

\[
 q_1+q_3-q_2=q_1(2\alpha+T\beta).                     \tag{3.3}
\]

Eliminating $\alpha,\beta$ from (3.2)--(3.3) proves (0.2).

### Corollary 3.1

For fixed $M$ and fixed nonzero $q_1,q_3$, the number of ordered source
triangles in a distance-Sidon set whose first and third invariant-form
values are $q_1,q_3$ is $m^{o(1)}$.

Indeed, Lemma 2.1 gives only $m^{o(1)}$ choices for each of the two directed
edge vectors.  A directed difference vector has at most one realization in
$A$, since two realizations would repeat its Euclidean norm.  Identity (0.2)
gives the equivalent Pell compression of the remaining $d,q_2$ coordinates.

## 4. Parabolic exception

For $T=\pm2$, the discriminant vanishes and $Q_M$ is the square of a linear
form after scaling.  Nonzero value fibres are unions of parallel affine
lines rather than divisor-size Pell orbits.  Full transversality removes the
zero eigenline but does not control the nonzero fibres.  The parabolic maps
therefore require the same kind of longitudinal line aggregation that was
needed in the corresponding-parallel branch; Lemma 2.1 must not be applied
to them.

## 5. Genuine integer-trace barriers

### 5.1 Modular Costas stress

For the transformed Costas certificates with $k=p-1$, the verifier counts
fully transverse, six-distinct, equal-signed ordered triangle pairs and
groups them by the reduced denominator of the associated affine trace:

| prime $p$ | $k$ | fully transverse records | trace denominator 1 | fraction |
|---:|---:|---:|---:|---:|
| 11 | 10 | 1,260 | 360 | 0.286 |
| 13 | 12 | 6,876 | 1,308 | 0.190 |
| 17 | 16 | 32,292 | 6,108 | 0.189 |

Thus integer trace carries a positive finite-scale fraction of the hard
core.  The denominator-$\le4$ fractions are respectively 0.638, 0.365, and
0.339.

### 5.2 Exact planted overlap

In the exact two-copy certificate, the determinant-one matrices are

\[
 T_1=\begin{pmatrix}339&-652\\13&-25\end{pmatrix},qquad
 T_2=\begin{pmatrix}-17&312\\-3&55\end{pmatrix}.
\]

The affine map carrying the first 11-point copy to the second has linear
part

\[
 M=T_2T_1^{-1}
 =\begin{pmatrix}-3631&94684\\-640&16689\end{pmatrix},
 \qquad \det M=1,qquad \operatorname{tr}M=13058.       \tag{5.1}
\]

Its discriminant is nonsquare, so no nonzero rational edge is an
eigenvector; every corresponding side is nonparallel.  This is a genuine
distance-Sidon, endpoint-realized overlap of size 11 with denominator-one
trace.  Its large height means that it does not refute the corrected
$k^3+m^2$ target, but it decisively rules out any pointwise claim that
integer-trace overlaps must be small.

## 6. Verdict

The invariant quadratic form gives divisor/Pell control of every fixed
nonzero fibre, and the pair $(q_1,q_3)$ nearly labels triangles inside a
fixed nonparabolic integer-trace overlap.  The unresolved loss is exactly
the two-dimensional range

\[
 (q_1,q_3)\in[-2m^2,2m^2]^2.                           \tag{6.1}
\]

The modular and planted stresses show that denominator one cannot be
discarded.  To finish the equal-area route one needs an aggregate theorem
coupling these two form values across many endpoint-realized maps, or a new
metric invariant reducing (6.1) to $m^{2+o(1)}$ effective mass.  Per-map
Pell bounds alone bottom out before the required energy estimate.

## 7. Verification

Run:

```bash
python phase2/loop/erdos1208/verify_integer_trace_invariant_form_pell_gate.py
```
