# Mixed-inertia and rank-aware assignment lock for D=821453

## 1. Verdict

The certified construction

\[
 E=\mathbb Q(\sqrt{821453}),\qquad
 |T|=219,\qquad d=217,\qquad N=11335
\]

remains optimal after jointly allowing:

1. any mixture of order-two, order-four, and uncapped tame inertia at the
   219 ramified-role ideals;
2. arbitrary nonprefix assignment of prime ideals to ramified and useful
   roles; and
3. a change of sign/dyadic ray rank, raising the generator rank to 218 or
   219.

Thus none of these variations improves

\[
 \boxed{F_2(n)\ll n^{0.49369313}}.                    \tag{1.1}
\]

The proof crosses every mixed cap count with every ray-color subspace and
uses an all-depth assignment dual plus an all-anchor concavity certificate.
Run

```text
python3 phase2/loop/erdos1208/verify_quadratic821453_cm_mixed_inertia_lock.py
```

with PARI/GP available.  The script first reruns the independent hostile BNF,
Kummer, usefulness, endpoint, and all-square assignment audit.

## 2. Exact weighted Golod--Shafarevich budget

Let `s_2`, `s_4`, and `s_0` count inertia generators capped at orders two,
four, and no finite order, respectively.  Then

\[
 s_2+s_4+s_0=219.
\]

For canonical rank 217, with `N` Frobenius-square relations, use

\[
 P(z)=1-217z+(218+s_2+N)z^2+s_4z^4.                  \tag{2.1}
\]

For every `s_2` and every `0<=s_4<=219-s_2`, the largest certified integer
useful count is

\[
 \boxed{N=11554-s_2}.                                \tag{2.2}
\]

Indeed the quadratic coefficient is 11,772.  At `z=2/217`, its quadratic
part equals `-1/217^2`, while

\[
 16\cdot219<217^2,                                   \tag{2.3}
\]

so every allowed quartic total retains strict negativity.  One more
quadratic relation gives discriminant

\[
 217^2-4\cdot11773=-3,                               \tag{2.4}
\]

and a nonnegative quartic term cannot recover negativity.

An uncapped inertia generator contributes exponent `1/2` to its local
root-discriminant factor, whereas an order-four cap contributes `3/8`.
Equation (2.2) shows that inserting a fourth-power relation consumes no
Frobenius-square slot.  Hence every uncapped ideal is strictly dominated by
an order-four cap.  Put

\[
 j=219-s_2.
\]

At an optimum all `j` nonsquare caps are fourth-power caps and the useful
count is `11335+j`.

The verifier repeats the exact polynomial calculation for the rank-changing
cases `d=218,219`.  If

\[
 M_d=\left\lfloor{d^2-1\over4}\right\rfloor,
\]

their all-square useful counts are 11,442 and 11,551, and upgrading one
square cap again adds exactly one formal useful slot.  Every allowed quartic
total remains strictly GS-negative at `z=2/d`.

## 3. Fixed-prefix all-depth lock

For an ideal of norm `Q`, put

\[
 c(Q)={\log Q\over2},\qquad
 g_k(Q)={1\over4}\log A_k(Q^{-2}).                   \tag{3.1}
\]

At frontier slope `lambda`, the all-depth useful-role dual value is

\[
 V_\lambda(Q)=\sum_{k\ge1}
       \left(g_k(Q)-\lambda c(Q)\right)_+.            \tag{3.2}
\]

Only finitely many summands are positive.  The field-independent exchange
lemma proves that `V_lambda(Q)` is nonincreasing in `Q`; when `K` depths are
active,

\[
 {d\over d\log Q}V_\lambda(Q)>-{1\over4\log Q}.       \tag{3.3}
\]

The verifier rechecks the strict rational inequality behind this result for
all `Q>=9`, rather than truncating the useful frontier heuristically.

At the certified all-square anchor, the active slopes are

\[
 \lambda_L=0.0306151017446977\ldots,
 \qquad
 \lambda_R=0.0190556890839508\ldots.                  \tag{3.4}
\]

Changing the `i`th cheapest square-capped inertia ideal to a fourth cap adds
the `i`th post-frontier ideal to the formal useful list.  The all-depth dual
useful value is smaller than its root-discriminant penalty by at least

\[
 0.2746530721670\ldots\quad(L),
 \qquad
 0.2129953296934\ldots\quad(R).                       \tag{3.5}
\]

Thus every nonzero `j` worsens both endpoint margins at the certified anchor.
To exclude repair by moving the anchor, the verifier evaluates a separator
near the crossing of the two endpoint margins for every `1<=j<=219`.  At
each separator the two margins are negative, the left derivative is positive,
and the right derivative is negative.  Concavity then excludes every anchor.
The worst fixed-prefix slacks are

\[
\begin{array}{c|c|c}
 &\text{margin}&\text{anchor derivative}\\ \hline
L&-0.2005569548\ldots&>0.0045891236\ldots\\
R&-0.3988303733\ldots&<-0.0128270200\ldots.
\end{array}                                           \tag{3.6}
\]

## 4. Full rank-aware assignment cross-product

The exact ray quotient for `(4O_E; both real places)` is `C_2^4`.  The two
unit columns span a two-dimensional subspace.  After quotienting by them,
prime-ideal columns have four colors in `F_2^2`.  If the ramified set spans
a quotient subspace of dimension `r`, then

\[
 d=219-r,\qquad r\in\{0,1,2\}.                        \tag{4.1}
\]

There are three quotient lines and one zero subspace.  The all-depth exchange
theorem applies separately in each subspace: for fixed `j`, the optimistic
assignment uses the `j` smallest allowed ideals as fourth-capped inertia, the
next `219-j` as square-capped inertia, and the first remaining formal useful
ideals.  Every remaining ideal is declared useful, including any ideal whose
actual Eisenstein/Kummer condition could fail, so this favors competitors.

The exact all-square rows are

\[
\begin{array}{c|c|c|c|c}
r&d&N_0&\text{last ramified norm}&\log D_L\\ \hline
2&217&11335&1213&322.2254902582\ldots\\
1&218&11442&3089&366.7277906748\ldots\\
1&218&11442&3389&371.7135811311\ldots\\
1&218&11442&3467&373.8461656742\ldots\\
0&219&11551&8009&422.2268227717\ldots.
\end{array}                                           \tag{4.2}
\]

The verifier crosses all five rows with all 220 values of `j`.  For every
case except the canonical `r=2,j=0` winner, a 100-digit separator has negative
left and right margins and derivatives of opposite sign.  Across the complete
cross-product the worst certified values are

\[
\begin{array}{c|c|c}
 &\text{margin}&\text{anchor derivative}\\ \hline
L&-0.2005569548\ldots&>0.0042749501\ldots\\
R&-0.3988303733\ldots&<-0.0128270200\ldots.
\end{array}                                           \tag{4.3}
\]

All depths down to slope `0.01` are retained in rank-changing rows, and the
active slopes are checked to exceed the first omitted slope.  In the
canonical row the maximum fourth-depth slope is

\[
 0.0157124493071841\ldots<\lambda_R.                  \tag{4.4}
\]

Decreasing local marginal gains excludes all deeper items.

## 5. Numerical diagnostic

The optimized threshold worsens strictly with `j` in the canonical row:

\[
\begin{array}{c|c|c}
j&\alpha_*&w_*\\ \hline
0&0.493693124444&40752.90\\
1&0.493694341339&40767.53\\
2&0.493695774683&40784.16\\
10&0.493709019387&40933.90\\
50&0.493803925492&41967.21\\
100&0.493948628487&43570.47\\
150&0.494105376433&45386.96\\
200&0.494262810553&47320.68\\
219&0.494321568607&48074.68.
\end{array}                                           \tag{5.1}
\]

The floating thresholds are diagnostics.  The exact GS identities,
all-depth dual inequalities, and 100-digit concavity separators are the proof.

## 6. Scope

This locks mixed tame inertia powers and arbitrary prime-ideal assignment for
the fixed `D=821453`, 219-ideal presentation.  It does not exclude a different
base field, a non-Shafarevich presentation with a better relation excess, or a
different geometric packing mechanism.
