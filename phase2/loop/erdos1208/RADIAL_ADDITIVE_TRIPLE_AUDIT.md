# Radial additive triples: a clean reduction and a decisive counterexample

Let (A\subset[m]^2\) be distance-Sidon and put

\[
  D=(A-A)\setminus\{0\}.
\]

Then (D) is symmetric, contains exactly one antipodal pair on every
occupied origin-centred circle, and contains at least

\[
  |A|(|A|-1)(|A|-2)
\]

ordered nonzero additive triples (x+y=z): take

\[
  x=a-b,\qquad y=b-c,\qquad z=a-c.
\]

This suggests the attractive statement

\[
  \#\{(x,y,z)\in D^3:x+y=z\}\ll m^{2+o(1)}.       \tag{1}
\]

If (1) held for every symmetric lattice set meeting each norm fibre in at
most two points, it would imply (|A|\ll m^{2/3+o(1)}), and hence settle the
power-law order in Erdős 1208.

That general statement is false by a large margin.

## Canonical radial representatives

For every integer represented as (x^2+y^2) in the square
`[-m,m]^2`, choose the representative in the right half-plane having largest
lexicographic coordinates, and include its antipode.  Call the resulting
symmetric set (D_m).  It has exactly two points on each occupied circle.

An exact two-dimensional convolution counts its additive triples.  The
following values were obtained by `analyze_radial_triples.py`:

| `m` | `|D_m|` | additive triples | triples / `m^2` |
|---:|---:|---:|---:|
| 20 | 394 | 38,460 | 96.15 |
| 40 | 1,372 | 399,840 | 249.90 |
| 80 | 4,920 | 4,494,258 | 702.23 |
| 120 | 10,500 | 19,114,650 | 1,327.41 |
| 200 | 27,574 | 121,750,500 | 3,043.76 |
| 500 | 158,266 | 3,565,411,080 | 14,261.64 |
| 800 | 390,226 | 20,593,660,362 | 32,177.59 |

Thus radial uniqueness alone does not give anything resembling (1).  The
chosen directions are heavily biased toward one angular sector, and this
creates enormous additive closure despite perfect uniqueness of norms.

## What survives

The reduction is still useful, but the missing hypothesis is now exact:

* (D) is not an arbitrary radial transversal; it is the *complete directed
  difference set* of one point set (A).
* The relevant additive triples are the transitive triples coming from paths
  (a\to b\to c), not merely arbitrary triples in (D).
* Non-transitive additive triples can occur even for a distance-Sidon set, so
  they cannot simply be declared absent.  Equivalently, vector-Sidon does not
  imply (B_3).

Any successful additive proof must therefore use a realizability or
stability theorem for radial transversals which are complete difference sets.
The two separate facts

1. at most one antipodal pair on each circle, and
2. many additive triples,

are insufficient.  This falsification prevents a future attack from losing
the most important piece of structure in the passage from (A) to (A-A).
