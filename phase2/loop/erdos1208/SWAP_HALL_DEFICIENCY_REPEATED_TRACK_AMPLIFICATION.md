# Hall deficiency amplifies to normalized repeated-track pairs

> **Status update.**  The theorem below is correct, but its normalized
> repeated-track target is no longer needed for the direct upper bound.
> `SWAP_LOW_WEIGHT_FIRST_MOMENT_COLLAPSE.md` observes that all low-weight
> occurrence mass is already at most a subpolynomial multiple of
> `Q_phys<=W_parallel`.  The live survivor is only the very-rich-cell tail.

## 1. Outcome

The capacitated-flow reduction leaves the Hall deficiency

\[
 D_L=\max_X\left(
  \sum_{o\in X}w(o)-L\sum_{\rho\in R(X)}b(\rho)
 \right)_+.                                      \tag{1.1}
\]

This note removes the quadratic rich-cell weight from its low-weight part.
Suppose

\[
 1\le w(o)\le W                                  \tag{1.2}
\]

for every retained occurrence.  If `a(rho)` is the number of occurrences
using row `rho`, define the normalized repeated-track energy

\[
 P_{norm}=\sum_\rho{1\over b(\rho)}
                    {a(\rho)\choose2}.            \tag{1.3}
\]

Then

\[
 \boxed{D_{2W}\le2W P_{norm}.}                   \tag{1.4}
\]

Thus, after splitting off occurrences with `w(o)>W`, the endpoint-pencil
mass satisfies

\[
 \boxed{
 {\mathcal P_\Lambda\over3}
 \le288Wk(k-1)^2+2WP_{norm}+M_{>W},}              \tag{1.5}
\]

where

\[
 M_{>W}=\sum_{w(o)>W}w(o).                        \tag{1.6}
\]

Without using the later first-moment collapse, it would be sufficient to prove

\[
 P_{norm},M_{>W}\le N^{o(1)}(k^3+m^2).           \tag{1.7}
\]

Every record in `P_norm` has a literal repeated physical track, exactly the
input of the rank-five quotient.  Its reciprocal coefficient `1/b(rho)` is
load-bearing: it is the exact capacity normalization created by the Hall
cut, not an ad hoc damping.  The second term is only the very-rich-cell
tail.

## 2. Normalized pair amplification

Fix `L>W` and a set `X` with positive deficiency.  Put

\[
 d_X(\rho)=|\{o\in X:\rho\in R(o)\}|,qquad
 I_X=\sum_{\rho\in R(X)}d_X(\rho),                \tag{2.1}
\]

and `B_X=sum_{rho in R(X)}b(rho)`.  Every occurrence has at least one row,
so `I_X>=|X|`.  Positive deficiency and (1.2) give

\[
 B_X<{W|X|\over L}.                               \tag{2.2}
\]

Weighted Cauchy now yields

\[
\begin{aligned}
 P_{norm}(X)
 &=\sum_{\rho\in R(X)}{1\over b(\rho)}
       {d_X(\rho)\choose2}\\
 &=\frac12\left(
   \sum_\rho{d_X(\rho)^2\over b(\rho)}
   -\sum_\rho{d_X(\rho)\over b(\rho)}\right)\\
 &\ge\frac12\left({I_X^2\over B_X}-I_X\right)\\
 &>{1\over2}\left({L\over W}-1\right)|X|.       \tag{2.3}
\end{aligned}
\]

Here `sum d_X/b<=I_X`, and the final expression is increasing for
`I_X>=|X|>B_X`.  At `L=2W`, equation (2.3) gives
`|X|<2P_norm(X)`.  Taking `X` to maximize (1.1),

\[
 D_{2W}\le\sum_{o\in X}w(o)
 \le W|X|<2WP_{norm}(X)\le2WP_{norm},            \tag{2.4}
\]

which proves (1.4).

For comparison, discarding the capacities and deduplicating occurrence
pairs gives the weaker bound `D_{2W}<=24W P_rep`, because two occurrences
share at most twelve rows.  Equation (1.4) is the correct theorem: it
discounts precisely the endpoints with many available partner tracks.

To include high weights, first leave all `w(o)>W` decorations unmatched and
route the low-weight subfamily.  This costs exactly `M_{>W}` and proves
(1.5) using the flow capacity bound.

## 3. Minimal cores

Choose an inclusion-minimal set `X` maximizing a positive deficiency.  For
`o in X`, let `U_o` be the rows used by `o` and by no other member of `X`.
Removing `o` gives

\[
 w(o)>L\sum_{\rho\in U_o}b(\rho).                \tag{3.1}
\]

If `L>W`, equations (1.2) and `b(rho)>=1` force `U_o` to be empty.  Thus
every row of a minimal low-weight deficient core is used at least twice.
The rank-five repeated-track relation is present everywhere in the core,
not merely on average.

This also explains why an ambient endpoint-degree bound is the wrong next
move.  The deficiency automatically peels all private rows; what remains is
a genuine repeated-track two-core with the reciprocal capacity weight from
(1.3).

## 4. Geometric content of `P_norm`

Each occurrence is an owner/parameter record with six directed `D` tracks.
If two occurrences share a row, they share the same physical directed edge
in the same role and orientation.  In the relative owner variables, one of
the six differences `d_j` is zero.  The rank-five theorem then says that any
four of the other five differences determine the complete transverse
quotient, with only the one-dimensional gauge

\[
 (U,C,A,B,E,Q)=(h,-Jh,0,0,0,h).                  \tag{4.1}
\]

Thus `P_norm` is precisely the normalized occurrence-pair aggregate to
which the existing rank theorem applies.  No decoration multiplicity or
endpoint-degree square remains.  The next theorem should bound these
anchored occurrence pairs by combining the four-direction quotient, the
reciprocal partner support, and the sharp `4k` physical gauge fibre.

The high-weight term is disjoint in nature.  Since
`w(o)=binom(r_C-1,2)`, it consists only of owner cells with
`r_C>sqrt(2W)`.  It should be attacked by the six synchronized translates
of the parameter set, not mixed back into `P_norm`.

## 5. Status

Equations (1.4)--(1.5) are unconditional.  Neither estimate in (1.7) is yet
proved globally.  The gain is that the weighted Hall obstruction has split
losslessly into the two exact geometric mechanisms already visible in the
cyclic analysis, while the repeated-track mechanism has lost its dangerous
quadratic cell weight and acquired its exact support normalization.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_hall_repeated_track_amplification.py
```

The verifier exhausts small row-incidence systems, compares deficiency with
the normalized row-pair energy, checks (2.3)--(2.4), and verifies the
private-row assertion for minimal maximizing cuts.
