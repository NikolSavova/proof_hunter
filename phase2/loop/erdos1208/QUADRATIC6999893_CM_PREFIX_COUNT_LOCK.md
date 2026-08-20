# The `D=6999893` all-square norm-prefix count is uniquely `T=219` on `50<=T<=600`

## Result

Consider the bounded-inertia, Eisenstein-CM construction over

\[
 E=\mathbf Q(\sqrt{6999893}).
\]

Restrict to norm-prefix ramification sets, impose square relations on every
ramified tame inertia generator, and grant every eligible unramified prime
ideal the optimistic benefit of being useful.  At

\[
 \alpha=0.49368416,
\]

the endpoint calculation was exhaustively checked for every integer count

\[
 50\leq T\leq600.
\]

Exactly one count is feasible: `T=219`.  The closest excluded count is
`T=217`; it fails even with a rational packing constant chosen in its favor.
Thus the new record is not an artifact of the initial `215<=T<=227` search.

This is a finite **norm-prefix, all-square, all-useful** lock.  It does not
treat `T<50`, `T>600`, arbitrary nonprefix ramification sets, mixed inertia
orders, or a different pro-2 presentation.

## Exact `C_4` class and ray rank

The certified field data are

\[
 6999893=31\cdot349\cdot647,\qquad
 \operatorname {Cl}(E)\simeq C_4,\qquad
 \operatorname {Cl}^+(E)\simeq C_4\times C_2.
\]

The second odd prime ideal in norm order is the norm-13 ideal

\[
 R=(13,13,\text{split root }6),
\]

and its class generates `C_4`.  Hence every audited prefix kills the full
ordinary class group.  The exact PARI/GP basis used by the verifier consists
of

1. the two global-unit squareclasses;
2. a generator of `R^4`, retaining the `Cl(E)[2]` kernel class; and
3. for each other selected ideal `P` of class coordinate `a`, a generator of
   `P R^e`, where `a+e=0 mod 4`.

For a prefix of length `T` these are exactly `T+2` independent pre-ray
squareclasses.  The verifier constructs the entire nested basis through
`T=600`, computes its sign/mod-4 columns with PARI, and independently rebuilds
the same row space from exact embedding signs and arithmetic in
`O_E/4O_E`.  The local row rank first reaches four at `T=7` and is exactly
four for all 551 audited prefixes.  Therefore

\[
 d=(T+2)-4=T-2\qquad(50\leq T\leq600).
\]

## All-square, all-useful Golod--Shafarevich relaxation

With all ramified inertia generators squared, the safe base-plus-inertia
relation charge before useful Frobenius caps is

\[
 (d+1)+T.
\]

At the strict quadratic ceiling

\[
 R_{\max}=\left\lfloor{d^2-1\over4}\right\rfloor,
\]

the optimistic useful budget is

\[
 N_T=R_{\max}-(d+1)-T.
\]

For every count, the verifier checks the strict weighted
Golod--Shafarevich inequality at `y=2/d`.  It then treats the next `N_T` prime
ideals as useful without applying the CM mod-3 rejection test.  This can only
improve a competing count.  At the surviving count,

\[
 T=219,\qquad d=217,\qquad N_T=11335,
\]

and the independent exact CM audit already proves that this relaxation is
attained: there are zero rejections through the last useful ideal

\[
 (124951,124951,\text{split root }98332).
\]

## All-depth endpoint certificate

For a norm-prefix ramification set,

\[
 \log\operatorname {rd}
 ={1\over2}\log6999893
 +{1\over4}\sum_{j\leq T}\log N\mathfrak p_j.
\]

The exhaustive C++ verifier builds the placewise marginal frontier through
depth eight.  At both active endpoints and for every count it checks that the
largest omitted depth-nine slope is below the active slope.  Since each local
marginal stream decreases with depth, this certifies the complete all-depth
frontier.

For every exclusion the computation uses the rigorous favorable bound

\[
 {11978\over10863}< {2\sqrt3\over\pi}.
\]

The endpoint right side increases with the packing constant, so lowering the
constant increases the margin and helps a competing count.  At the equality
of the two endpoint margins, the left derivative is positive and the right
derivative is negative.  Concavity of both endpoint margins therefore
certifies the maximum of their lower envelope.

The leading cells in the exhaustive sweep are:

| rank | `T` | `d` | `N_T` | favorable margin |
|---:|---:|---:|---:|---:|
| 1 | 219 | 217 | 11335 | `+0.0005942020` |
| 2 | 217 | 215 | 11123 | `-0.0017335205` |
| 3 | 221 | 219 | 11549 | `-0.0033895125` |
| 4 | 218 | 216 | 11228 | `-0.0118526016` |
| 5 | 220 | 218 | 11441 | `-0.0128870793` |

All other counts are worse than the fifth row.  A separate 100-digit Decimal
calculation gives the closest exclusion `T=217` the favorable common margin

```text
-0.001733520391756904643525815625647...
```

For the survivor it instead uses the adverse rigorous upper bound

\[
 {2\sqrt3\over\pi}<{71603\over64935}
\]

and obtains the common margin

```text
+0.000553113536032347488070759915303...
```

Thus the long-double sweep is separated from zero on both sides by exact
high-precision checks.

## Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_quadratic6999893_cm_prefix_count_lock.py
```

The wrapper certifies the BNF/class data, explicitly constructs and checks the
`C_4`-aware nested ray basis, verifies the rational constant bounds and every
GS cell, compiles and runs the exhaustive C++ sweep, and recomputes the winner
and closest exclusion with 100-digit arithmetic.  Expected final line:

```text
D=6999893 broad prefix-count lock: CERTIFIED
```

The broad enumerator is independently runnable as
`verify_quadratic6999893_cm_prefix_count_lock.cpp`.

## Scope and implication

This does not further lower the exponent and does not solve Erdős problem
1208.  It proves that, within the stated 551-cell family, the record exponent

\[
 F_2(n)\ll n^{0.49368416}
\]

is supported by the unique count `T=219`, even after every excluded count is
given the all-useful relaxation.  The surviving cell is not merely
optimistic: its separate exact CM audit shows that all 11,335 useful slots are
actually realized.
