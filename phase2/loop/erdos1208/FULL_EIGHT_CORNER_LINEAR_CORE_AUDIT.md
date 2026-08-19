# Linear full eight-corner cores: exact audit and surviving geometry

## 1. Outcome

The four-corner stopping-set barrier does not decide the full eight-corner
question.  This note audits the most natural full-core counterexamples:
translation-invariant systems over `F_2^m`.

There are abstract full eight-corner cores whose relation equations have
injective point labels.  The smallest exact model stored here is already
non-linear as a corner hypergraph: its eight corner colours use only four
distinct perfect matchings.  It is therefore excluded by distance-Sidon
geometry before solving the Gaussian equations; consistently, its universal
Gaussian solution also forces sixteen repeated squared distances.  The
canonical 256-record cube has eight edge-disjoint matchings and is the first
serious linear control; it forces ninety-six repetitions.  No distance-Sidon
realization follows.

An initially apparent zero-collision model was spurious: its 128 `F_2`
records collapse in pairs to only 64 distinct six-endpoint relations.  This
is now an explicit regression test in both search and verification code.

Thus full eight-corner peelability remains unproved and unfalsified for
distance-Sidon sets.  More importantly, any proof must use the linearity and
Euclidean norm constraints together; unrestricted matching/core axioms
already admit full stopping sets.

## 2. Linear model

Let the relation records be `x in F_2^m`.  For each of the six endpoint roles

\[
 a_0,a_1,b_0,b_1,c_0,c_1
\]

choose a row space `U_s <= F_2^m`; the point label in role `s` is the value
of the corresponding linear quotient.  A corner `(i,j,k)` has fibres of
size two exactly when

\[
 \operatorname{rank}(U_{a_i}+U_{b_j}+U_{c_k})=m-1. \tag{2.1}
\]

The six endpoint labels jointly determine the record exactly when

\[
 \operatorname{rank}(U_{a_0}+U_{a_1}+U_{b_0}+U_{b_1}
                     +U_{c_0}+U_{c_1})=m.       \tag{2.2}
\]

Condition (2.2) is essential.  Omitting it created the false 128-record hit.

The geometric relation equation is

\[
 a_0-a_1-b_0+b_1-Jc_0+Jc_1=0.                 \tag{2.3}
\]

Fourier characters of `F_2^m` diagonalize (2.3).  For each character, the
six role coefficients satisfy one Gaussian-linear equation.  This gives the
complete universal solution space over `Q(i)`, rather than a numerical
sample.  Comparing exact Hermitian coefficient matrices then detects every
squared-distance identity forced in all realizations.

### 2.1 Linearity forced by distance-Sidon geometry

For a transverse relation, a corner key selects one endpoint from each of
the three directed difference pairs.  Two distinct relations in a
distance-Sidon set cannot share two different corner keys.

Indeed, in every role where the two corner masks differ, the two relations
share both endpoints of that directed edge.  If the masks differ in two or
three roles, the relation equation determines the remaining directed edge,
so the records coincide.  If they differ in exactly one role, that directed
edge is common and the two remaining roles each share one endpoint.
Subtracting the two relation equations says that the two pairs of nonshared
endpoints have displacement vectors related by a Gaussian unit `+/-J`.
They are distinct unordered pairs of equal length, contradicting the
distance-Sidon hypothesis.

Consequently the eight degree-two corner matchings of any distance-Sidon
full core are pairwise edge-disjoint.  This is an additional necessary
condition, not part of the bare stopping-set axioms.

## 3. Exact controls

### 3.1 A 32-record non-linear full core

Take `m=5`, two-dimensional row spaces with bases

```text
(15,20) (8,20) (13,20) (1,20) (13,21) (7,8).
```

All eight mixed ranks are four, the total rank is five, and the 32 records
are distinct.  In mask order `i+2j+4k`, the eight corner-fibre translations
are

```text
28, 2, 28, 2, 21, 21, 22, 22.
```

Thus there are only four distinct perfect matchings: every matched pair of
records shares two corner keys, contrary to the linearity lemma above.  The
system has 24 distinct formal point labels, and its universal solution also
contains sixteen repeated squared-distance polynomials.  It is a valid bare
stopping set but not a linear or distance-Sidon full core.

### 3.2 Canonical cube

Index the eight coordinates of `F_2^8` by cube corners.  Let each endpoint
row space be spanned by the four coordinate vectors on the opposite face.
Every mixed triple spans a seven-dimensional space and the six roles span
all eight dimensions.  Its corner-fibre translations are the eight distinct
standard basis vectors.  This gives 256 distinct records, 96 distinct point
labels, and exactly 96 forced squared-distance repetitions.

### 3.3 The deduplication regression

The six four-dimensional bases

```text
(3,24,36,65) (5,27,33,73) (3,8,16,101)
(14,16,39,68) (6,19,41,74) (6,24,34,65)
```

have all eight mixed ranks equal to six, but their total rank is only six,
not seven.  Hence 128 records collapse to 64 relations.  Each apparent
degree-two corner fibre consists of two copies of the same relation and
vanishes after deduplication.

## 4. Consequence for the proof search

There are now three distinct statements which must not be conflated:

1. Four fixed-role corner peelability is false, by the explicit 31-point
   distance-Sidon construction.
2. Full eight-corner peelability is false as a bare stopping-set theorem, by
   the 32-record non-linear core above.
3. Full eight-corner peelability for **distance-Sidon realizations** remains
   open; the canonical edge-disjoint linear model forces distance
   equalities, while the smaller model fails linearity already.

Even statement 3 would only close the transverse/wide branch.  The safer
aggregate target remains the size-biased tail

\[
 |R_{\ge t}|\le k^{3+o(1)}/t,                  \tag{4.1}
\]

which permits stopping sets provided their total population is cubic.

Run

```bash
python3 phase2/loop/erdos1208/verify_full_eight_corner_linear_core_audit.py
```

for the exact ranks, relation counts, formal solution equations, and norm
collision counts.
