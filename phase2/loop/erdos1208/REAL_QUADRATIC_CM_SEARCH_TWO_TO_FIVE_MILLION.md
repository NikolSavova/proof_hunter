# Finite real-quadratic CM screen from two to five million

## 1. Search protocol

This is a reproducible finite search audit, not an asymptotic theorem.  The
optimized standalone scanner is

```text
phase2/loop/erdos1208/scan_cm_eisenstein_real_quadratic_bases_fast.cpp
```

It retains the arithmetic and ranking rules of the canonical scanner but
caches the discriminant-independent local frontier data by prime-ideal norm.
On the test interval `D<=10000`, it produced the same candidate order,
ideal-count choices, and anchors as the canonical implementation.  The sole
textual difference was one last displayed rounding digit in one negative
margin (`-4.26405261421` versus `-4.2640526142`).  Thus the cached evaluation
changes no screening decision in the audit, while no theorem relies on the
floating margins in any case.

For every positive fundamental discriminant in `2,000,001<=D<=5,000,000`,
the run reconstructed the actual odd prime-ideal norm sequence in
`Q(sqrt(D))`.  Each field was first tested at

```text
|T| = 215, 219, 223, 227, 231, 235, 239, 243.
```

The best 100 fields in each 250,000-discriminant interval were then rescanned
at every integer `205<=|T|<=250`.  The target was `alpha=0.49369313`, the
ordinary generator model was `d=|T|-2`, and every eligible outside ideal was
optimistically declared useful.  The latter is a favorable candidate filter:
an exact theorem still requires a class/S-class/ray calculation and the full
mod-3 usefulness test.

A representative interval is reproduced by

```text
c++ -O3 -std=c++20 -Wall -Wextra -Wpedantic \
  -DSCREEN_D_MIN=4000001 -DSCREEN_D_LIMIT=4250000 \
  -DSCREEN_ALPHA=0.49369313 \
  -DSCREEN_BROAD_T_MIN=215 -DSCREEN_BROAD_T_MAX=243 \
  -DSCREEN_BROAD_T_STEP=4 -DSCREEN_FINALISTS=100 \
  phase2/loop/erdos1208/scan_cm_eisenstein_real_quadratic_bases_fast.cpp \
  -o /tmp/cm_fast && /tmp/cm_fast
```

The twelve disjoint intervals contained 911,887 positive fundamental
discriminants in total.

## 2. Complete interval leaders

The leading dense-rescan field in each interval was as follows.  A margin is
the scanner's fixed-alpha endpoint slack at `alpha=0.49369313`; it is only a
ranking statistic, not the final optimized exponent.

\[
\begin{array}{c|r|r|r}
\text{interval}&D&|T|&\text{screen margin}\\ \hline
[2000001,2250000]&2041613&223&1.01749908\\
[2250001,2500000]&2278757&227&1.10624498\\
[2500001,2750000]&2554373&221&0.98970592\\
[2750001,3000000]&2774693&221&0.62852479\\
[3000001,3250000]&3200972&217&1.14470120\\
[3250001,3500000]&3461708&225&0.97719954\\
[3500001,3750000]&3705005&219&0.98185312\\
[3750001,4000000]&3914648&219&0.51426537\\
[4000001,4250000]&4108373&219&1.39631133\\
[4250001,4500000]&4390949&207&0.67683732\\
[4500001,4750000]&4684412&229&1.24278885\\
[4750001,5000000]&4906677&225&0.97836068
\end{array}                                             \tag{2.1}
\]

Thus no field in the stated two-to-five-million procedure screened above
`D=4108373`.  The independent one-to-two-million ordinary screen likewise
found no stronger candidate: its leading fields were

\[
\begin{array}{c|r}
D&\text{screen margin}\\ \hline
1162493&0.92309\\
1460213&0.86564\\
1809533&0.74309
\end{array}                                             \tag{2.2}
\]

The `D<=1,000,000` search and its exact `D=821453` record are documented in
`REAL_QUADRATIC_CM_SEARCH_TO_ONE_MILLION.md`.

## 3. Exact promotion of the leaders

The floating filter first promoted `D=2278757`; exact arithmetic moved its
best nearby ideal count from the screen's fixed-alpha choice to `|T|=223` and
certified the safe exponent `0.49368818`.

The interval `3,000,001..3,250,000` then produced the stronger
`D=3200972=4*800243`.  Its nontrivial odd class group survives the exact
audit cleanly: class group `C_15`, narrow class number 30, localized class
group trivial, exact ray rank four, `|T|=215`, `d=213`, and 10,913 useful
ideals with zero rejections.  Its certified threshold is

\[
 0.4936875853118874120085566171\ldots,                  \tag{3.1}
\]

giving the safe fallback theorem `F_2(n)<<n^0.49368759`.  Its verifier is
`verify_cm_eisenstein_real_quadratic_3200972.py`.

Finally `D=4108373` passed every exact gate.  The exact nearby optimization
selects `|T|=217`, not the fixed-alpha screen's `|T|=219`.  The certified
metadata are

\[
 h=2,\quad \mathrm{Cl}(E)=C_2,\quad \mathrm{Cl}_T(E)=1,
 \quad d=215,
\]

and the mod-3 scan accepts all 11,123 required ideals with zero rejections.
The exact all-depth threshold is

\[
 0.4936864598096758088590628661\ldots.                  \tag{3.2}
\]

The theorem-level safe headline is therefore

\[
 \boxed{F_2(n)\ll n^{0.49368647}}.                      \tag{3.3}
\]

The proof and canonical verifier are respectively
`REAL_QUADRATIC_4108373_CM_EISENSTEIN_RECORD.md` and
`verify_cm_eisenstein_real_quadratic_4108373.py`.

## 4. Scope and limitations

The finite statement proved by this audit is exactly the following:

1. the twelve enumerated intervals cover every positive fundamental
   discriminant between two and five million;
2. under the stated ordinary, all-useful broad-to-dense procedure, none of
   them outranks `D=4108373` at the screening target;
3. the promoted `D=4108373` configuration is subsequently certified without
   either the ordinary-rank or all-useful assumptions.

It does **not** prove that `D=4108373` is optimal over every ideal count, every
nonprefix assignment, fields above five million, genus-rank presentations,
or other base-field/tower constructions.  The screen is floating-point and
is used only to nominate candidates; (3.3) rests solely on exact arithmetic
and high-precision inequalities in the standalone verifier.  No asymptotic
claim is made from this bounded computation.
