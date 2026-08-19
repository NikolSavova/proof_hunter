# Linear full eight-corner cores: exact audit and surviving geometry

## 1. Outcome

The four-corner stopping-set barrier does not decide the full eight-corner
question.  This note audits the most natural full-core counterexamples:
translation-invariant systems over `F_2^m`.

There are genuine abstract full eight-corner cores whose relation equations
have injective point labels.  In the smallest exact model stored here,
however, the universal Gaussian solution forces sixteen repeated squared
distances.  The canonical 256-record cube forces ninety-six.  No
distance-Sidon realization follows.

An initially apparent zero-collision model was spurious: its 128 `F_2`
records collapse in pairs to only 64 distinct six-endpoint relations.  This
is now an explicit regression test in both search and verification code.

Thus full eight-corner peelability remains unproved and unfalsified for
distance-Sidon sets.  More importantly, any proof must use Euclidean norm
uniqueness; the abstract matching/core axioms alone already admit full
stopping sets.

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

## 3. Exact controls

### 3.1 A genuine 32-record full core

Take `m=5`, two-dimensional row spaces with bases

```text
(15,20) (8,20) (13,20) (1,20) (13,21) (7,8).
```

All eight mixed ranks are four, the total rank is five, and the 32 records
are distinct.  The system has 24 distinct formal point labels, but its
universal solution contains sixteen repeated squared-distance polynomials.
It is therefore a valid combinatorial full core and an invalid
distance-Sidon core.

### 3.2 Canonical cube

Index the eight coordinates of `F_2^8` by cube corners.  Let each endpoint
row space be spanned by the four coordinate vectors on the opposite face.
Every mixed triple spans a seven-dimensional space and the six roles span
all eight dimensions.  This gives 256 distinct records, 96 distinct point
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
2. Full eight-corner peelability is false as a purely combinatorial theorem,
   by the 32-record linear core above.
3. Full eight-corner peelability for **distance-Sidon realizations** remains
   open; every exact linear model tested forces a distance equality.

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

