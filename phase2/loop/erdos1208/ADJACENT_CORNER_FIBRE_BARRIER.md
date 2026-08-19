# The unfiltered adjacent-corner fibre barrier

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
unique.  It is therefore tempting to discard the transversality indicator
and bound the larger ambient intersection

\[
 \max_t |(A-A)\cap(t-(A+JA))|\ll |A|^{1+o(1)}.  \tag{1.2}
\]

That would charge a commutator witness using the two common endpoints and
one additional point.  The theorem below shows that this *unfiltered*
relaxation is false by a full power.  It does not, by itself, disprove the
same estimate after retaining the transverse condition.

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

## 3. Transversality correction

The large fibre in Theorem 2.1 is entirely non-transverse in the corner
relation which produced (1.1).  In the exact eight-point witness, the
unfiltered intersection has size `12`, while every transversality-filtered
adjacent cell is empty.  Thus the perpendicular-ruler family is a sharp
barrier to dropping the indicator, not an asymptotic counterexample to a
filtered pointwise theorem.

There is nevertheless a strong exact warning against a small filtered
maximum.  In the row--source graph `K_A` of
`TRANSVERSE_ROW_SOURCE_C4_GATE.md`, the degree of a right vertex is exactly
the transversality-filtered adjacent-corner load with the two shared
endpoints fixed.  The certified 45-point integral distance-Sidon set in
that note has

\[
 \deg_{K_A}\bigl((46,1)+J(24,29)\bigr)
 =250=0.82817\ldots\,45^{3/2}.                 \tag{3.1}
\]

This finite certificate is not an asymptotic counterfamily, so it does not
formally disprove a `k^(1+o(1))` maximum theorem.  It does show that the
filtered local load can already be strongly superlinear and that the
linear-looking behaviour of the perpendicular family was misleading.

## 4. Strategic consequence

The commutator stability theorem reduces a nonabelian corner core to failed
alternating squares.  For adjacent colours, the two corner keys share two
actual points, so (1.1) is the most economical pointwise endpoint charge.
Theorem 2.1 shows that its unfiltered relaxation can have quadratic load;
the exact source certificate (3.1) shows that restoring transversality does
not make every local cell small in the tested regime.

The barrier does not produce a counterexample to the desired cubic
size-biased tail.  As with every earlier perpendicular-ruler obstruction,
the quadratic fibre comes from two perpendicular one-dimensional arms and
is accompanied by cubic image support.  A successful curvature argument
should therefore aggregate over the shared endpoint pair and charge heavy
fibres to transverse support growth.  The rigorous surviving target is the
row--source four-cycle or second-moment bound, not the unfiltered maximum.
No asymptotic filtered maximum theorem or counterexample is currently
known.

Run

```bash
python3 phase2/loop/erdos1208/verify_adjacent_corner_fibre_barrier.py
```

for the exact eight-point distance-Sidon witness, the vanishing filtered
profile, and the independent 45-point transverse source certificate.
