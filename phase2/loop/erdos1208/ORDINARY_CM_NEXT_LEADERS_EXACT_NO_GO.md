# Exact no-go for the next three ordinary CM leaders

## 1. Verdict

The three ordinary all-useful leaders immediately following
`D=821453` in the search through discriminant one million do **not**
improve the certified exponent

\[
 \alpha_0=0.49369313.
\]

This is not a floating-screen verdict.  The companion verifier certifies
the class and narrow class numbers, constructs an exact independent
S-unit squareclass basis, proves full rank for the sign/modulo-four ray
conditions, performs the exact CM modulo-three usefulness test, and then
excludes every continuous endpoint anchor for every integer
`205 <= T <= 250`.

Run

```text
python3 phase2/loop/erdos1208/verify_ordinary_cm_next_leaders_exact_no_go.py
```

PARI/GP is required for the certified number-field calculations.  All
prime-ideal enumeration, CM tests, local frontiers, and endpoint inequalities
are independently reconstructed in Python.

## 2. Exact arithmetic data

The fields and their defining integral bases are

\[
\begin{array}{c|c|c}
D&\mathcal O_E&\text{factorization}\\
\hline
979277&\mathbb Z[(1+\sqrt D)/2]&13\cdot75329\\
994733&\mathbb Z[(1+\sqrt D)/2]&619\cdot1607\\
544268&\mathbb Z[\sqrt{136067}]&4\cdot136067.
\end{array}
\]

PARI's `bnfcertify` succeeds in all three cases and gives

\[
\begin{array}{c|c|c}
D&h_E&h_E^+\\ \hline
979277&2&2\\
994733&1&2\\
544268&1&2.
\end{array}                                             \tag{2.1}
\]

For `D=979277`, the unique ideal above 13 has nonzero class in the
cyclic class group of order two.  Since it occurs before every audited
cutoff, localization kills the class group.  An independent S-unit
squareclass basis is obtained from

1. the two global unit squareclasses;
2. a generator of \(P_{13}^2\);
3. a generator of \(P\) for each principal \(S\)-prime \(P\); and
4. a generator of \(P P_{13}\) for every other nonprincipal \(S\)-prime.

The valuation vectors and the exact Kummer sequence prove independence.
For each class-number-one field the corresponding basis is simply the two
global unit squareclasses and one principal generator for each `S`-prime.
Thus every audited prefix of length `T` has `T+2` S-unit squareclasses.

The exact ray group for modulus `(4 O_E; both real places)` is `(C_2)^4`.
The ray image already has rank four at `T=205`; nesting proves rank four
for all `205 <= T <= 250`.  Consequently

\[
 d=(T+2)-4=T-2                                      \tag{2.2}
\]

throughout the audited interval.  This also shows that the class-number-two
field supplies no hidden generator bonus.

## 3. Exact CM usefulness screen

At the optimizing cutoffs, impose the safe base-relation charge `d+1`, one
inertia-square relation per member of `T`, and one Frobenius-square relation
per useful ideal.  The strict quadratic Golod--Shafarevich budget is

\[
 N=\left\lfloor {d^2-1\over4}\right\rfloor-(d+1)-T. \tag{3.1}
\]

For a candidate ideal of norm `Q = 1 mod 3`, the Eisenstein CM condition is
automatic.  If `Q = 2 mod 3`, the verifier evaluates the quadratic-residue
functional on every exact S-unit basis element and checks that adjoining
this row raises the rank of the four ray-condition rows.  This is precisely
the condition that the functional be nonzero on the safe Kummer kernel.

All three fields have **zero rejections** before the required useful prefix
is filled:

\[
\begin{array}{c|c|c|c|c|c}
D&T&d&N&\text{last }S\text{-ideal}&\text{last useful ideal}\\ \hline
979277&209&207&10295&(1217,\text{ root }776)&(111373,\text{ root }8825)\\
994733&211&209&10499&(1201,\text{ root }880)&(114217,\text{ root }75502)\\
544268&221&219&11549&(1117,\text{ root }567)&(127261,\text{ root }92720).
\end{array}                                             \tag{3.2}
\]

Thus none is killed by a hidden modulo-three rejection.  They are killed by
the endpoint inequality itself.

## 4. Rigorous endpoint exclusion

The verifier uses the safe rational CM packing constant

\[
 C\le {71603\over64935}
\]

and the complete first-three-depth local frontier

\[
 c(Q)={\log Q\over2},\qquad
 g_j(Q)={1\over4}\log A_j(Q^{-2}).                    \tag{4.1}
\]

For every `T` from 205 through 250 it grants the candidate the optimistic
assumption that every outside ideal is useful.  Hence a negative result here
also excludes the actual CM-screened sequence.  At each `T`, the code finds
the unique separator where the scale-one and scale-two endpoint margins
agree.  The margin functions are concave: the local frontier is piecewise
linear concave, while the subtracted log-sum-exp term is convex.  At the
separator the scale-one derivative is positive and the scale-two derivative
is negative.  Since the scale-one constraint is smaller to the left and the
scale-two constraint is smaller to the right, a negative separator value
excludes every anchor.

The strongest (least negative) separator for each field is

\[
\begin{array}{c|c|c|r|r|r}
D&T&w&\text{common margin}&M_1'(w)&M_2'(w)\\ \hline
979277&209&37173.50677&-0.41527431& 0.00523655&-0.01257978\\
994733&211&37868.05474&-0.50271502& 0.00520349&-0.01258144\\
544268&221&41501.06654&-0.75945505& 0.00492024&-0.01279740.
\end{array}                                             \tag{4.2}
\]

The maximum omitted fourth-depth slope is also strictly below the active
right-endpoint slope in every one of the 138 audited `(D,T)` cases, so no
deeper local role can repair the deficit.

## 5. Scope

This is a finite exact no-go for these three fields, the ordinary
square-inertia/Frobenius-square model, and every `205 <= T <= 250`.  It is not
an optimality theorem over all real quadratic fields, arbitrary ramification
assignments, mixed inertia orders, or class-group-enhanced candidates.  It
does show that the three next ordinary leaders from the million-discriminant
screen cannot improve the `D=821453` record, even though their exact CM
usefulness screens are perfect.
