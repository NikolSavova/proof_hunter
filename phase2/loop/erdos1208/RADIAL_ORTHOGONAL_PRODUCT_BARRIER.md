# Radial uniqueness does not imply the orthogonal product gate

## 1. Result

Let `J(x,y)=(-y,x)`.  There are arbitrarily large finite sets

\[
  D\subset\mathbb Z^2
\]

with all three of the following properties:

1. `D=-D` and `0 in D`;
2. every nonzero origin-centred circle meets `D` in at most one
   antipodal pair;
3. `D intersect JD={0}`;

but nevertheless

\[
 |D+D|=|D|^{1+o(1)},\qquad
 |D+JD|=|D|^{1+o(1)}.                         \tag{1.1}
\]

Consequently

\[
 \boxed{|D+D|\,|D+JD|=|D|^{2+o(1)},}          \tag{1.2}
\]

which misses the proposed `|D|^(3-o(1))` product theorem by a full
power.  Thus the live Erdős 1208 proof cannot use only radial uniqueness,
central symmetry, or the disjointness `D intersect JD={0}`.  It must use
that

\[
 D=A-A
\]

is the complete decorated difference set of a single point set.

## 2. Construction

For every positive integer represented by `x^2+y^2` with
`|x|,|y|<=m`, choose exactly one representative modulo sign.  Concretely,
among the representatives in the right half-plane choose the
lexicographically largest one.  Include that vector and its antipode, and
also include zero.  Call the resulting set `D_m`.

By construction, every occupied nonzero norm fibre contains exactly two
points.  The quarter-turn of the chosen antipodal pair is the other
antipodal pair on the same circle, and hence was not chosen.  Therefore

\[
 D_m\cap JD_m=\{0\}.                            \tag{2.1}
\]

All points lie in `[-m,m]^2`, so both sumsets in (1.1) lie in
`[-2m,2m]^2`.  Hence

\[
 |D_m+D_m|,\ |D_m+JD_m|\le (4m+1)^2.           \tag{2.2}
\]

The Landau--Ramanujan theorem says that the number of positive integers at
most `m^2` representable as a sum of two squares is

\[
 \Theta\!\left(\frac{m^2}{\sqrt{\log m}}\right).
\]

Every such representation automatically has both coordinates at most
`m`, so

\[
 |D_m|\gg \frac{m^2}{\sqrt{\log m}}
        =m^{2-o(1)}.                             \tag{2.3}
\]

Equations (2.2)--(2.3), together with the trivial lower bound
`|X+Y|>=|X|+|Y|-1` in a torsion-free group, prove (1.1)--(1.2).

## 3. Why this is stronger than the earlier radial-triple barrier

`RADIAL_ADDITIVE_TRIPLE_AUDIT.md` showed that the same radial transversals
can have far too many additive triples.  The present observation closes a
stronger possible escape: passing from a one-support triple count to the
two-support product does not make radial uniqueness sufficient.  The
canonical transversals simultaneously compress the ordinary and
quarter-turned supports.

They cannot be complete difference sets of distance-Sidon point sets in the
range relevant to the problem.  That failure is now the load-bearing datum.
Any proof of the orthogonal energy--support gate must invoke at least one of
the following equivalent pieces of extra structure:

* every nonzero `d in D` has a unique ordered endpoint decoration
  `d=a-b`;
* the nonzero elements of `D` split into the `|A|` translated stars
  `A-b`;
* the weighted function
  `|A| delta_0 + 1_(D minus {0})` is the exact autocorrelation of a
  zero--one set.

An argument stated only for symmetric radial transversals cannot prove the
cube-root theorem.

## 4. Exact finite profiles

`verify_radial_orthogonal_product_barrier.py` checks the construction,
radial uniqueness, (2.1), and both support sizes by exact integer
enumeration.  Selected profiles, with `N=|D_m|`, are

\[
\begin{array}{c|r|r|r|c}
m&N&|D_m+D_m|&|D_m+JD_m|&
 |D_m+D_m||D_m+JD_m|/N^3\\ \hline
3&19&73&109&1.16008\ldots\\
5&39&181&281&0.85741\ldots\\
8&83&431&685&0.51633\ldots\\
12&165&935&1509&0.31408\ldots\\
20&395&2515&4101&0.16735\ldots\\
30&815&5569&9141&0.09403\ldots
\end{array}
\]

The decreasing normalized product is the finite shadow of the full-power
asymptotic obstruction (1.2).
