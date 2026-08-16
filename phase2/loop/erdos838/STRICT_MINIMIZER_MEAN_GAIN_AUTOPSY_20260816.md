# Erdős 838: strict minimizer mean-gain autopsy

**Date:** 2026-08-16
**Verdict:** no unconditional coefficient gain; park M4 after the two-step
reduction limit.

The active target was deliberately weaker than the full mean conjecture.  A
fixed bound

```text
mu(P_n) >= (1/2+epsilon)log_2 n
```

on global minimizers would improve the lower coefficient from `1/4` to
`1/4+epsilon/2`.  Two exact interfaces were tested.

## 1. Blocked exterior points: the minimizer qualifier is essential

For a uniformly random closed hull, with `H` extreme, `I` interior, and `B`
blocked exterior labels, the exact identities are

```text
E H=mu,       E O=mu+E B,       log_2 V<=2mu+E B.       (1)
```

The candidate `E B<=(1-delta)mu^2` would give a strict gain.  The new exact
stress verifier reconstructs every face and every closure in the certified
44- and 58-point rational records.  It obtains

```text
 n     V          mu          E B/mu^2
44   237229    4.850477...     1.100265...
58  1061907    5.194152...     1.350137....             (2)
```

Thus even `E B<=mu^2` is false for arbitrary planar configurations.  The
exact `n=8,9` minimizers have ratios `0.247736...` and `0.297417...`, so the
minimizer-only statement is not refuted.

However, global minimality puts each physical label in a **minimum**
one-point extension chamber of the arrangement of the other labels.  Moving a
blocked point into an ear repairs faces and normally increases the extension
count; the first-order mutation sign is anti-converting.  The previously
proved self-minimal-cell and three-ear examples show that neither one-point
relocation nor Helly intersection turns (2) into a minimizer inequality.
Doing so requires a genuinely multi-point interaction, already the open
minimizer-mutation problem.  This is not a strict reduction of M4.

## 2. Variance: a clean threshold, but the hereditary step is P1 again

The exact deletion law gives the variance ladder

```text
mu(P)=E sum_m Var(|A_m|)/(m-mu(P_m)).                  (3)
```

An average variance above

```text
1/(2 ln 2)=0.7213475204...                              (4)
```

would force `mu>(1/2)log_2 n`; any fixed margin in (4) gives a strict
coefficient gain.  The threshold is numerically plausible on the low-mean
records, whose variances include `0.7073,0.7554,0.7633,0.9122,1.0257`.

A pointwise theorem is false.  Exact graded Pascal evaluation gives

```text
 T_(16,8):   variance 0.549611...
 T_(32,16):  variance 0.316446...
 T_(64,32):  variance 0.182617...
 T_(128,64): variance 0.102342....                      (5)
```

These cells lie in the safe high-mean branch.  Restricting (4) to the
low-mean branch is formally possible, but the deletion descendants are not
global minimizers.  Making the dichotomy hereditary requires showing that a
low-variance rank-concentrated interval has enough convex extensions.  This
is precisely the parked positive-rank-interval/fixed-size gate P1d, not a new
route.

## 3. Two apparent detours do not change the endpoint

The temporal-path decomposition gives one literal Boolean cube in every
endpoint cell.  Summing the first moments of only those cubes is exact, but
far too weak: on the certified 58-wire record,

```text
sum B_e=55,221,       sum (rank B_e)B_e=313,576,
```

so the resulting cell-moment lower bound is only `2.147902...`, below
`(1/2)log_2 58=2.928990...`.  Using the remaining path-downset mass requires
the same cross-endpoint compensation that the half-weight campaign isolated;
maximum-bank disjointness alone does not supply it.

Nor does the abstract-convex-geometry terminology hide a rank theorem.
The literature's *free sets* are closed and independent (empty convex
polygons).  Here `V` counts all closed hulls, equivalently all convexly
independent extreme-point sets, including hulls with omitted interior labels.
The NBC/Moebius identities for free sets therefore recover alternating
identities already present in the bivariate hull enumerator, not a positive
uniform-rank estimate.

## 4. Why the branch stops here

The two plausible reductions therefore terminate at already known hard
interfaces:

1. a multi-point minimizer mutation with signed circuit correlation; or
2. the averaged positive-rank-interval supersaturation theorem P1d.

Neither contains a new quantitative `epsilon` or `delta`.  Continuing with a
half-weight reformulation would add a third equivalent target: an upper bound
`n Z_P(1/2)/Z_P(1)<=n^(1/2-epsilon)` implies the same mean bound by Jensen and
returns to the existing literal-history decoder gap.

Under the difficulty-ledger stop rule, M4 is therefore parked.  The exact
stress theorem and the variance threshold remain useful diagnostics; they are
not a claimed improvement to the rigorous `1/4` lower coefficient.

## 5. Verification

Run

```text
python3 phase2/loop/erdos838/verify_strict_minimizer_mean_gain_stress.py
```

The large rows use exact rational slope orders and exact integer half-plane
masks; no face or closure is sampled.
