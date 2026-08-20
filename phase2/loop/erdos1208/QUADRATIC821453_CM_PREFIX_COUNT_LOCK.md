# The `D=821453` all-square prefix count is uniquely `T=219` on `50<=T<=600`

## Result

Consider the bounded-inertia, Eisenstein-CM construction over

\[
K=\mathbf Q(\sqrt{821453}).
\]

Restrict to norm-prefix ramification sets, impose square relations on all
ramified tame inertia generators, and give every unramified prime ideal the
benefit of being useful.  Among every integer ramified-ideal count

\[
50\le T\le 600,
\]

the endpoint calculation at

\[
\alpha=0.4936931245
\]

has exactly one feasible count: `T=219`.  Thus the field record is not an
artifact of the previously checked local window.  The closest other count is
`T=217`, and it already fails under a packing constant deliberately favorable
to the competitor.

This is a finite prefix-count lock, not a theorem about `T<50`, `T>600`, or
arbitrary nonprefix ramification sets.  The fixed-`T=219` nonprefix and mixed
inertia directions are treated separately in
`QUADRATIC821453_CM_MIXED_ASSIGNMENT_LOCK.md`.

## Exact rank and relation bookkeeping

The certified sign/mod-4 ray quotient has dimension four and the two unit
columns span dimension two.  The exact PARI/GP ray columns reach full rank four
by the tenth odd prime ideal.  Rank is monotone under adding columns, and the
verifier also checks every prefix explicitly, so throughout `50<=T<=600`

\[
d=T+2-4=T-2.
\]

For all-square inertia caps, the Shafarevich plus inertia relation cost before
useful Frobenius caps is

\[
(d+1)+T.
\]

At the strict quadratic Golod--Shafarevich ceiling

\[
R_{\max}=\left\lfloor\frac{d^2-1}{4}\right\rfloor,
\]

the favorable useful-prime budget is therefore exactly

\[
N_T=R_{\max}-(d+1)-T.
\]

The verifier checks the strict weighted GS inequality at `y=2/d` for all 551
counts.  It then declares the next `N_T` prime ideals useful.  This can only
strengthen a competing count; no mod-3 rejection is charged in the exclusion.

## Endpoint audit

For the norm-prefix ramification set the root-discriminant term is

\[
\log \operatorname{rd}
=\frac12\log 821453+\frac14\sum_{j\le T}\log N\mathfrak p_j.
\]

The broad verifier constructs the placewise marginal frontier through depth
eight.  At both active endpoints it checks that every omitted depth-nine
marginal has smaller slope.  Monotonicity in the local depth then makes this
the full all-depth frontier, rather than a depth truncation.

For exclusions it uses

\[
\frac{11978}{10863}<\frac{2\sqrt3}{\pi}.
\]

The endpoint right-hand side is `log(C+exp(x))`, hence is increasing in `C`.
Replacing the true constant by this lower rational bound makes the right-hand
side smaller and the margin larger: it favors every competitor.

At the equality of the two endpoint margins, the verifier checks that the
left derivative is positive and the right derivative is negative.  Each
endpoint margin is concave (a concave fractional-knapsack frontier minus a
log-sum-exp term), so these signs certify the global maximum of the lower
envelope.  The leading broad cells are

| rank | `T` | `d` | `N_T` | favorable margin |
|---:|---:|---:|---:|---:|
| 1 | 219 | 217 | 11335 | `+5.29131e-5` |
| 2 | 217 | 215 | 11123 | `-1.26665e-3` |
| 3 | 221 | 219 | 11549 | `-1.01891e-2` |
| 4 | 218 | 216 | 11228 | `-1.06616e-2` |

All remaining counts are worse than the fourth row.

The Python wrapper independently rebuilds the two closest cells with
90-digit Decimal arithmetic.  It retains `T=219` using the adverse rational
upper bound

\[
\frac{2\sqrt3}{\pi}<\frac{71603}{64935},
\]

with equal-endpoint margin greater than `1.18e-5`.  It excludes `T=217` using
the favorable lower bound with margin less than `-1.2666e-3`.  This separates
the finite broad sweep from its only numerically close decision.

## Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_quadratic821453_cm_prefix_count_lock.py
```

The wrapper certifies the exact ray ranks and rational constant inequalities,
compiles and runs the exhaustive C++ sweep over all 551 counts, and performs
the high-precision leader/runner-up audit.  Expected final line:

```text
D=821453 broad prefix-count lock: CERTIFIED
```

The broad enumerator is also independently runnable as
`verify_quadratic821453_cm_prefix_count_lock.cpp`.

## Scope and implication

This closes the plausible ramified-count fluctuation inside a window nearly
three times wider than the winning count.  It does **not** improve the record
exponent and does not by itself solve Erdos 1208.  Its value is robustness: the
current `0.49369313` certificate over this field is now locked against every
all-square norm-prefix count from 50 through 600, even after granting the
competitors the optimistic all-useful prime stream.
