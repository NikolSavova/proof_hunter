# Quadratic adjacent-corner fibres in distance-Sidon sets

## 1. The tempting commutator charge

Two adjacent corner masks differ in one endpoint role and agree in the other
two.  Fixing their two common selected endpoints reduces a transverse
relation to

\[
 d+b+Jc=t,
 \qquad d\in(A-A)\setminus\{0\},\quad b,c\in A, \tag{1.1}
\]

for a fixed translation `t` (signs can be changed by replacing `A` with
`-A`).  Since a distance-Sidon set is vector-Sidon and

\[
 (A-A)\cap J(A-A)=\{0\},
\]

both the representation of `d` and the representation of `b+Jc` are
unique.  It is therefore tempting to bound every adjacent-corner fibre by

\[
 \max_t |(A-A)\cap(t-(A+JA))|\ll |A|^{1+o(1)}.  \tag{1.2}
\]

That would charge a commutator witness using the two common endpoints and
one additional point.  The theorem below shows that (1.2) is false by a
full power.

## 2. Sharp barrier

**Theorem 2.1.**  There are arbitrarily large integral planar
distance-Sidon sets `A`, with `k=|A|`, and translations `t` such that

\[
 \boxed{|(A-A)\cap(t-(A+JA))|\gg k^2.}          \tag{2.1}
\]

### Proof

Use the perpendicular-ruler construction from
`PERPENDICULAR_RULER_OBSTRUCTION.md`.  Take a `2s`-mark integral Golomb ruler
`S subset [0,L]`, `L=O(s^2)`, partition it into `R_1,R_2` of size `s`, and
choose an integral offset `C=s^(2+o(1))` for which

\[
 A=H\cup V,
\]

\[
 H=\{(u,0):u\in R_1\},\qquad
 V=\{(0,C+v):v\in R_2\}                       \tag{2.2}
\]

is distance-Sidon.  Thus `k=2s`.

For distinct `r,r' in R_1`, put

\[
 d=(r-r',0)\in A-A.
\]

For `u in R_1`, `v in R_2`, take

\[
 b=(u,0)\in H,\qquad c=(0,C+v)\in V.
\]

Then

\[
 d-(b+Jc)=(r-r'-u+C+v,0).                     \tag{2.3}
\]

There are

\[
 s(s-1)s^2=s^3(s-1)                            \tag{2.4}
\]

ordered choices in (2.3), while its first coordinate occupies an interval
of at most `4L+1=O(s^2)` integer values.  Some translation `t` therefore has
at least

\[
 {s^3(s-1)\over4L+1}\gg s^2\gg k^2            \tag{2.5}
\]

representations.

These representations give distinct intersection elements.  The Golomb
property makes every nonzero oriented difference `r-r'` unique, while
distance-Sidonicity makes `A+JA` a direct sum.  Once `t` is fixed, either
side of `d=t+(b+Jc)` therefore recovers the other.  Hence the number in
(2.5) is exactly a lower bound for the set intersection in (2.1).  This
proves the theorem.

## 3. Strategic consequence

The commutator stability theorem reduces a nonabelian corner core to failed
alternating squares.  For adjacent colours, the two corner keys share two
actual points, so (1.1) is the most economical pointwise endpoint charge.
Theorem 2.1 shows that this charge can have quadratic load.

The barrier does not produce a counterexample to the desired cubic
size-biased tail.  As with every earlier perpendicular-ruler obstruction,
the quadratic fibre comes from two transverse one-dimensional arms and is
accompanied by cubic image support.  A successful curvature argument must
therefore aggregate over the shared endpoint pair and charge heavy fibres
to transverse support growth.  Bounding each defect cell separately cannot
work.

Run

```bash
python3 phase2/loop/erdos1208/verify_adjacent_corner_fibre_barrier.py
```

for the exact eight-point distance-Sidon witness and its complete overlap
profile.
