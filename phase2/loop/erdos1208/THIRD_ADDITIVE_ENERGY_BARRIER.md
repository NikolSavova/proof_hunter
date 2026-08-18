# General-position barrier to ordinary third-additive-energy bounds

## 1. Result

A natural way to upper-bound the rotated triple energy is Hölder:

\[
 \frac1{|G|}\sum_\chi
 |\widehat{1_A}(\chi)|^2
 |\widehat{1_A}(J^*\chi)|^4
 \le E_3^+(A),                                  \tag{1.1}
\]

where

\[
 E_3^+(A)=\#\{a_1+a_2+a_3=b_1+b_2+b_3:
                  a_i,b_i\in A\}.               \tag{1.2}
\]

This cannot prove Erdős #1208 through a bound depending only on `|A|`.
There are arbitrarily large integer distance-Sidon sets in general position
with

\[
 E_3^+(A)\ge |A|^4/9.                            \tag{1.3}
\]

Thus even an estimate `E_3^+(A)<=|A|^(4-epsilon)` is false.  The obstruction
is the finite-field parabola, followed by a generic integral linear change of
coordinates.  The change makes the Euclidean lengths unique but preserves
every additive relation.

This does not disprove the rotated or transverse energy conjecture: the
quarter-turn in (1.1) is precisely the extra structure discarded by Hölder.
It shows that any successful Fourier proof must retain correlation between a
frequency and its quarter-turn, rather than bounding both by an ordinary
third energy.

## 2. The finite-field parabola as an integer set

Let `p` be an odd prime and take least nonnegative residues:

\[
 P_p=\{(x,[x^2]_p):0\le x<p\}\subset\mathbb Z^2. \tag{2.1}
\]

This is vector-Sidon.  Indeed, if two nonzero oriented differences agree over
the integers, reducing modulo `p` gives

\[
 x-y=u-v,\qquad x^2-y^2=u^2-v^2.                \tag{2.2}
\]

The first difference is nonzero, so division gives `x+y=u+v`; hence
`x=u,y=v` modulo `p`, and therefore as representatives in `[0,p-1]`.

No three points of `P_p` are collinear.  An integer collinearity would remain
a collinearity modulo `p`, while a nonvertical line over `F_p` meets the
parabola `y=x^2` in at most two points and a vertical line meets it in one.

The threefold sumset is small.  An exact coordinate sum is determined by
its two residues modulo `p` and the two carry digits, each of which belongs
to `{0,1,2}`.  Consequently

\[
 |3P_p|\le9p^2.                                  \tag{2.3}
\]

Cauchy--Schwarz now gives

\[
 E_3^+(P_p)
 =\sum_s r_{3P_p}(s)^2
 \ge {p^6\over |3P_p|}
 \ge {p^4\over9}.                               \tag{2.4}
\]

## 3. Separating all Euclidean lengths

Let `V` be the set of nonzero oriented differences of `P_p`.  For two
vectors `v,w` belonging to different unordered edges, vector-Sidonicity says
\(w\ne\pm v\).  For a real `2 by 2` matrix `T`, the unwanted equality

\[
 \|Tv\|^2=\|Tw\|^2                              \tag{3.1}
\]

is a polynomial equation in the four entries of `T`.  This polynomial is not
identically zero: identity for every `T` would imply
\(vv^T=ww^T\), and hence \(w=\pm v\).

Also exclude `det T=0`.  There are only finitely many nonzero polynomials to
avoid, and the integer matrices are Zariski dense in the four-dimensional
matrix space.  Hence there is an integral invertible `T` for which

\[
 A_p=T(P_p)                                      \tag{3.2}
\]

is distance-Sidon.  Invertibility preserves the absence of three collinear
points.  It also preserves all additive equalities and inequalities, so

\[
 |3A_p|=|3P_p|,qquad E_3^+(A_p)=E_3^+(P_p).     \tag{3.3}
\]

Equations (2.4) and (3.3) prove (1.3) for arbitrarily large `p`.

## 4. Exact finite certificate

For `p=127`, the matrix

\[
 T=\begin{pmatrix}-93&-83\\66&-1\end{pmatrix},
 \qquad\det T=5571,                              \tag{4.1}
\]

already works.  The resulting 127-point integer set has

* all 8,001 unordered squared distances distinct;
* no collinear triple;
* `|3A|=81,221`;
* `E_3^+(A)=86,658,955`;
* maximum ordered triple-sum multiplicity 168.

The contrast with the actual quarter-turn statistic is sharp.  For
`Phi(a,b,c)=a+J(b-c)` with `b!=c`, the same set has 2,031,882 image points,
maximum multiplicity two, and energy 2,032,998.  Thus its ordinary third
energy is `0.3331... k^4`, while its off-diagonal rotated energy is only
`0.9925... k^3`.  Hölder loses essentially a full factor of `k` on this
exact example.

Run

```text
python3 phase2/loop/erdos1208/verify_third_additive_energy_barrier.py
```

All checks use exact integer arithmetic.

## 5. Consequence for the live proof search

The high ordinary third energy is compatible with the strongest qualitative
geometric hypotheses available here: vector-Sidonicity, unique Euclidean
distances, and maximum collinearity two.  Therefore neither general position
nor a line-rich/wide split can justify replacing the rotated sixth moment by
`E_3^+(A)`.

An ambient-sensitive inequality can still survive: the integral matrix used
to separate the distances may enlarge the containing box.  More importantly,
the exact rotated and transverse moments can be much smaller than the Hölder
majorant.  The live target remains the restricted quarter-turn correlation,
equivalently the global decorated-parallelogram moment.  Ordinary additive
higher energy is now a closed surrogate.
