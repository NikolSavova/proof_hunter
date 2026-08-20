# Finite real-quadratic CM screen from six to ten million

## 1. Search protocol

This note records a finite ordinary real-quadratic base-field screen, not an
asymptotic theorem.  The reproducible scanner is

```text
phase2/loop/erdos1208/scan_cm_eisenstein_real_quadratic_bases_fast.cpp
```

Every positive fundamental discriminant in
`6,000,001<=D<=10,000,000` was enumerated.  For each field the scanner built
its actual sequence of odd prime-ideal norms and tested the ordinary model
`d=|T|-2`, the conservative base relation charge `d+1`, and the optimistic
assumption that every eligible outside prime ideal is useful.  The target was
the then-current safe exponent

\[
 \alpha=0.49368647.                                     \tag{1.1}
\]

Every field was tested first at

```text
|T| = 215, 219, 223, 227, 231, 235, 239, 243,
```

and the best 100 fields in each half-million interval were then rescanned at
every integer `205<=|T|<=250`.  The current `D=4108373` record field has
fixed-target scanner margin

\[
 0.00214193178545                                        \tag{1.2}
\]

at `|T|=217`, providing the nomination baseline.

The first four intervals used the default norm cap 250,000.  The last four
used `SCREEN_NORM_LIMIT=200000`.  This does not truncate a tested
configuration: the executable asserts for every enumerated field that at
least 16,000 prime ideals are present, while the largest dense-window
configuration needs only 15,126.  The ordered prefix used by the score is
therefore identical to the prefix under the default cap.

A representative last-wave interval is reproduced by

```text
c++ -O3 -std=c++20 -Wall -Wextra -Wpedantic \
  -DSCREEN_D_MIN=9000001 -DSCREEN_D_LIMIT=9500000 \
  -DSCREEN_NORM_LIMIT=200000 \
  -DSCREEN_ALPHA=0.49368647 \
  -DSCREEN_BROAD_T_MIN=215 -DSCREEN_BROAD_T_MAX=243 \
  -DSCREEN_BROAD_T_STEP=4 -DSCREEN_FINALISTS=100 \
  phase2/loop/erdos1208/scan_cm_eisenstein_real_quadratic_bases_fast.cpp \
  -o /tmp/cm_fast && /tmp/cm_fast
```

The eight disjoint intervals contain 1,215,889 positive fundamental
discriminants in total.

## 2. Complete interval leaders

A margin is the dense rescan's optimized lower-endpoint slack at the fixed
target (1.1).  It is a candidate-ranking statistic, not a theorem-level
exponent.

\[
\begin{array}{c|r|r|r|r}
\text{interval}&\#D&D&|T|&\text{margin}\\ \hline
[6000001,6500000]&152003&6209045&219& 0.107582679\\
[6500001,7000000]&152000&6999893&221& 0.491174956\\
[7000001,7500000]&151953&7286093&221&-0.327003811\\
[7500001,8000000]&151979&7882637&213&-0.300291068\\
[8000001,8500000]&151999&8305653&217&-0.093370430\\
[8500001,9000000]&151967&8904053&217& 0.158732885\\
[9000001,9500000]&151982&9490373&217& 0.258889440\\
[9500001,10000000]&152006&9622077&217&0.297846260
\end{array}                                             \tag{2.1}
\]

Thus `D=6999893` is the unique leader of this bounded procedure.  In
particular, none of the four later interval leaders reaches its fixed-target
margin.  The broad-grid counts of fields already nonnegative before dense
rescanning were respectively

\[
 1,1,0,0,0,2,2,1.                                      \tag{2.2}
\]

The complete top-30 output for each interval was retained in the run
transcript; (2.1) lists every interval winner.

## 3. Exact promotion of `D=6999893`

The filter's fixed-target choice was `|T|=221`.  Exact high-precision
reoptimization over `216<=|T|<=223` instead selects

\[
 |T|=219,qquad d=217,qquad N=11335.                    \tag{3.1}
\]

This candidate then passed every theorem-level arithmetic gate:

\[
 \operatorname{Cl}(E)=C_4,qquad
 \operatorname{Cl}^{+}(E)=C_4\times C_2,qquad
 \operatorname{Cl}_T(E)=1,                              \tag{3.2}
\]

the explicit 221-column S-unit model has exact sign/dyadic ray rank four,
and all 11,335 required mod-3 useful ideals pass with zero rejections.  The
Golod--Shafarevich relation budget is

\[
 r\le11772,qquad 4r=217^2-1.                           \tag{3.3}
\]

The all-depth 100/150-digit product-disk verifier gives

\[
 \alpha_*=0.4936841573736362558301044898\ldots,         \tag{3.4}
\]

and therefore the certified theorem

\[
 \boxed{F_2(n)\ll n^{0.49368416}}.                      \tag{3.5}
\]

The proof and standalone verifier are
`REAL_QUADRATIC_6999893_CM_EISENSTEIN_RECORD.md` and
`verify_cm_eisenstein_real_quadratic_6999893.py`.

## 4. Scope

The finite statement is exactly that the stated broad-to-dense ordinary,
all-useful procedure enumerated all positive fundamental discriminants in
the interval six through ten million and found no field with a larger
fixed-target margin than `D=6999893`.  The winning field was then certified
without either the ordinary-rank or all-useful assumptions.

This does not prove global optimality over:

1. the separately searched interval five through six million;
2. discriminants above ten million;
3. every possible nonprefix ramified-ideal assignment;
4. extra class/genus-rank presentations; or
5. other base fields and arithmetic towers.

The broad screen uses floating point only to nominate fields.  The exponent
in (3.5) rests solely on exact PARI arithmetic, exact integer finite-field
tests, and high-precision inequalities in the standalone verifier.
