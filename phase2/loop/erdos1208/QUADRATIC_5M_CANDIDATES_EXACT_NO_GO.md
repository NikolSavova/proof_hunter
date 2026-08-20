# Exact finite no-go for the remaining 5--6 million quadratic screen candidates

## Verdict

The three remaining screen candidates

\[
 D\in\{5872397,5182973,5963613\}
\]

do not improve the current exponent `0.49368416` in the all-square
norm-prefix construction.  The exact audit covers every integer count

\[
 205\leq T\leq250.
\]

For each field, PARI certifies the localized class arithmetic and exact
sign/mod-4 ray rank.  In all 138 cells the resulting generator rank is

\[
 d=T-2.
\]

Every candidate is then granted the optimistic assumption that all available
CM prime ideals are useful.  Even with a packing constant moved in the
candidate's favor, the best endpoint margins are

| discriminant | best `T` | `d` | best favorable margin |
|---:|---:|---:|---:|
| 5,872,397 | 217 | 215 | `-0.2499649349929508...` |
| 5,182,973 | 207 | 205 | `-0.3622712784553856...` |
| 5,963,613 | 219 | 217 | `-0.6578842690721046...` |

Thus no exact CM usefulness scan is needed: a rejection could only make these
margins smaller.

## Exact class and Kummer arithmetic

The discriminants and certified class data are

\[
\begin{array}{c|c|c|c}
D&\text{factorization}&\operatorname {Cl}(E)&\operatorname {Cl}^+(E)\\ \hline
5872397&5872397&C_1&C_1\\
5182973&59\cdot107\cdot821&C_{10}&C_{10}\times C_2\\
5963613&3\cdot53\cdot37507&C_2&C_2\times C_2.
\end{array}
\]

All three are positive fundamental discriminants.  For `D=5182973`, the
second prime ideal in norm order, of norm 11, generates `C_10`.  For
`D=5963613`, the first prime ideal, of norm 3, generates `C_2`.  Localization
at any audited prefix therefore kills the entire ordinary class group.

For a cyclic even class group `C_H` with reference ideal `R`, the verifier
constructs the following nested pre-ray squareclass basis:

1. the two global unit classes;
2. a compact generator of the principal ideal `R^H`; and
3. for every other selected ideal `P` of class coordinate `a`, a compact
   generator of `P R^e`, where `a+e[R]=0` in `C_H`.

The item-3 valuation vectors are independent on their non-`R` coordinates.
Item 2 supplies the extra squareclass arising from `Cl(E)[2]`; it cannot be a
unit times a square, since that would make `R^{H/2}` principal.  Together with
the two unit classes this gives exactly `T+2` pre-ray squareclasses.  In class
number one the basis is simply the two units and one principal generator per
selected ideal, again of size `T+2`.

The full sign/mod-4 quotient is `(C_2)^4`.  Exact ideal logarithms give row
rank four at every prefix from 205 through 250 in every field, so

\[
 d=(T+2)-4=T-2.                                    \tag{2.1}
\]

This kills the tempting genus-bonus relaxation for the two three-factor
discriminants: their extra narrow genus structure is consumed by the exact
localized ray constraints and does not increase `d`.

### Compact-unit safeguard

The fundamental unit of `Q(sqrt(5182973))` is prohibitively large if expanded.
The verifier never expands it.  PARI's `bnfunits` and flag-5
`bnfisprincipal` output compact factorizations.  The sign/mod-4 logarithm is
computed factor by factor and combined with the exact integer exponents.
Thus the rank certificate neither truncates nor numerically approximates the
large unit.

## Favorable all-useful endpoint exclusion

For every audited count the all-square relation budget is

\[
 R_{\max}=\left\lfloor{d^2-1\over4}\right\rfloor,
 \qquad
 N_T=R_{\max}-(d+1)-T.                              \tag{3.1}
\]

The verifier checks the strict quadratic Golod--Shafarevich inequality at
`y=2/d` and then takes the next `N_T` prime ideals without any CM rejection.
The root-discriminant term is

\[
 \log\operatorname {rd}
 ={1\over2}\log D+{1\over4}\sum_{j\leq T}\log N\mathfrak p_j.
\]

For the exclusion it uses the rigorous lower bound

\[
 {11978\over10863}< {2\sqrt3\over\pi}.              \tag{3.2}
\]

The endpoint right side increases with this packing constant.  Replacing the
true constant by the lower rational bound therefore increases the margin and
is favorable to a candidate.

The local marginal at depth `j` and norm parameter `x=Q^{-2}` is

\[
 g_j={1\over4}\log\left({j+1\over j}{S_{j-1}\over S_j}\right),
 \qquad S_j=1+x+\cdots+x^j.
\]

These marginals strictly decrease with depth.  Indeed,

\[
 S_{j-1}S_{j+1}=S_j^2-x^j,
\]

and `g_j>g_{j+1}` is equivalent to
`S_j^2>(j+1)^2x^j`, which follows strictly from AM--GM applied to
`1,x,...,x^j`.  The verifier retains depths one through three and checks that
the largest depth-four slope is below both active slopes.  This certifies the
complete all-depth frontier.

At the crossing of the two endpoint margins, the first derivative is positive
and the second is negative in every cell.  Their concavity then makes this
crossing the global maximum of the lower envelope.  The table in the verdict
therefore excludes every anchor, not merely the displayed optimizing scale.

## Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_quadratic_5m_candidates_exact_no_go.py
```

The verifier checks the discriminant factorizations, runs `bnfcertify`, builds
the exact compact localized bases, proves ray rank four at all 138 counts,
checks the rational packing bound, and evaluates the favorable all-useful
endpoint with 100-digit arithmetic.  Expected final line:

```text
5--6m quadratic candidates exact finite no-go: CERTIFIED
```

## Scope

This is a finite no-go for the all-square norm-prefix family on
`205<=T<=250`.  It does not exclude counts outside this interval, nonprefix
ramification sets, mixed inertia orders, or other presentations.  Within the
screen that produced these candidates, however, the result is exact: the
genus-rank loophole is closed and the optimistic all-useful model already
misses the current record by a wide margin.
