# The `D=4108373` all-square norm-prefix count is uniquely `T=217` on `50<=T<=600`

## Result

Consider the bounded-inertia, Eisenstein-CM construction over

\[
K=\mathbf Q(\sqrt{4108373}).
\]

Restrict to norm-prefix ramification sets, impose square relations on every
ramified tame inertia generator, and grant every unramified prime ideal the
optimistic benefit of being useful.  At

\[
\alpha=0.49368647,
\]

the endpoint calculation was exhaustively checked for every integer count

\[
50\leq T\leq600.
\]

Exactly one count is feasible: `T=217`.  The closest excluded count is
`T=215`; it fails even with a rational packing constant chosen in its favor.
Thus the new field record is not an artifact of the previously tested local
count window.

This is a finite **norm-prefix, all-square** lock.  It does not treat `T<50`,
`T>600`, or arbitrary nonprefix ramification sets.  Fixed-`T=217` nonprefix
class/ray cells and all square/fourth/uncapped inertia assignments are handled
separately in `QUADRATIC4108373_CM_STRUCTURAL_LOCK.md`.

## Exact class/ray rank

The certified field data are

\[
h_K=2,\qquad \mathrm{Cl}(K)\simeq C_2,
\]

and the full sign/mod-4 ray quotient has dimension four.  The first
nonprincipal prime ideal is the second ideal in the norm stream, of norm 11.
Consequently every audited prefix kills `Cl_S[2]`.

Fix this norm-11 ideal as `R_0`.  The exact PARI/GP basis used by the verifier
consists of the two global-unit columns, a generator of `R_0^2`, generators of
principal selected ideals, and generators of `P R_0` for the other
nonprincipal selected ideals.  This is a basis of the `T+2` dimensional
pre-ray positive squareclass space.  Its ray columns reach rank four already
at `T=6`; rank is monotone thereafter, and the verifier explicitly checks all
551 prefixes.  Hence throughout the audited range

\[
d=(T+2)-4=T-2.
\]

## Weighted Golod--Shafarevich budget

For all-square inertia caps, the quadratic relation cost before useful
Frobenius caps is

\[
(d+1)+T.
\]

At the strict quadratic ceiling

\[
R_{\max}=\left\lfloor\frac{d^2-1}{4}\right\rfloor,
\]

the optimistic useful-prime budget is

\[
N_T=R_{\max}-(d+1)-T.
\]

The verifier checks the strict weighted Golod--Shafarevich inequality at
`y=2/d` for every count.  It then declares the next `N_T` prime ideals useful,
without applying any mod-3 rejection.  This all-useful relaxation can only
help an excluded competing count.

## Endpoint certificate

For the norm-prefix ramification set,

\[
\log\operatorname{rd}
=\frac12\log 4108373+\frac14\sum_{j\leq T}\log N\mathfrak p_j.
\]

The broad C++ verifier constructs the placewise marginal frontier through
depth eight.  At both active endpoints, for every count, it checks that the
largest omitted depth-nine slope is smaller than the active slope.  Since the
local marginal slopes decrease with depth, this certifies the full all-depth
frontier.

For every exclusion the calculation uses

\[
\frac{11978}{10863}<\frac{2\sqrt3}{\pi}.
\]

The endpoint right-hand side is increasing in this packing constant, so the
lower rational bound decreases the right-hand side and increases the margin:
it is favorable to a competitor.  At the equality of the two endpoint
margins, the left derivative is positive and the right derivative is
negative.  Concavity of each endpoint margin then certifies the global maximum
of their lower envelope.

The leading cells in the exhaustive sweep are:

| rank | `T` | `d` | `N_T` | favorable margin |
|---:|---:|---:|---:|---:|
| 1 | 217 | 215 | 11123 | `+0.0021562564` |
| 2 | 215 | 213 | 10913 | `-0.0032151838` |
| 3 | 219 | 217 | 11335 | `-0.0104791964` |
| 4 | 216 | 214 | 11017 | `-0.0134270767` |
| 5 | 213 | 211 | 10705 | `-0.0141354720` |

All other counts are worse than the fifth row.

The Python wrapper independently rebuilds the closest excluded cell with
100-digit Decimal arithmetic and the favorable lower constant.  Its common
endpoint margin is less than `-0.00321518`.  It retains `T=217` using the
adverse rational upper bound

\[
\frac{2\sqrt3}{\pi}<\frac{71603}{64935},
\]

with common endpoint margin greater than `0.00211516`.  This cleanly separates
the broad floating-point enumeration from its only close numerical decisions.

## Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_quadratic4108373_cm_prefix_count_lock.py
```

The wrapper certifies the exact class/ray ranks and rational constant bounds,
compiles and runs the exhaustive C++ sweep over all 551 counts, checks weighted
GS and all-depth optimality, and recomputes the winner and runner-up at high
precision.  Expected final line:

```text
D=4108373 broad prefix-count lock: CERTIFIED
```

The broad enumerator is also independently runnable as
`verify_quadratic4108373_cm_prefix_count_lock.cpp`.

## Scope and implication

This does not further lower the exponent and does not solve Erdos 1208.  It
does make the `0.49368647` theorem robust against every all-square,
all-useful norm-prefix ramified count in a window almost three times as wide as
the winner.  Together with the separate fixed-count structural lock, it closes
the two most dangerous local optimization loopholes around the current record.
