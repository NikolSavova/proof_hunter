# Genus-bonus real-quadratic CM search from ten to twelve million

## 1. Search protocol

This note records the mandatory genus-aware finite screen over every positive
fundamental discriminant

\[
 10000001\leq D\leq12000000
\]

at the live exponent

\[
 \alpha=0.49368416.
\]

The interval was divided into four disjoint half-million blocks.  In each
block, the fast scanner tested

```text
T = 215, 219, 223, 227, 231, 235, 239, 243
```

and then rescanned the top 100 fields at every integer `205<=T<=250`.  It
used the actual ordered sequence of odd prime-ideal norms, the conservative
base relation cost `d+1`, and the optimistic assumption that every available
outside prime ideal is useful.  Most importantly, it granted the full genus
allowance

\[
 d=T-2+(\omega(D)-1).                                \tag{1.1}
\]

This is deliberately an overgenerous nomination screen.  A positive margin
must survive exact localized class and ray arithmetic before it can support a
construction.

The norm cap was 200,000.  The scanner asserts that every field supplies at
least 16,000 prime ideals, while every tested cell uses a shorter prefix, so
the cutoff does not truncate any configuration.

## 2. Complete interval results

The four blocks contain 607,918 positive fundamental discriminants.  Their
complete summaries are:

| interval | number of fields | broad-grid nonnegative | relaxed leader | `T` | relaxed `d` | margin |
|---|---:|---:|---:|---:|---:|---:|
| 10,000,001--10,500,000 | 151,974 | 3,153 | 10,078,365 | 207 | 209 | `+6.4318049749` |
| 10,500,001--11,000,000 | 151,970 | 3,181 | 10,737,573 | 214 | 217 | `+7.86033508636` |
| 11,000,001--11,500,000 | 151,984 | 3,246 | 11,352,572 | 214 | 217 | `+7.25993014655` |
| 11,500,001--12,000,000 | 151,990 | 3,231 | 11,897,340 | 206 | 209 | `+6.56086952831` |

There are 12,811 broad-grid nonnegative relaxed fields in total.  The large
margins are not numerical near-ties: each leader has five or six distinct
prime-discriminant factors, so (1.1) grants four or five extra generators.
The default verifier reproduces and prints the complete top-30 transcript for
each interval and asserts the displayed counts and leaders exactly.

## 3. Exact localization kills all four leaders

The four leader factorizations are

\[
\begin{aligned}
10078365&=3\cdot5\cdot11\cdot17\cdot3593,\\
10737573&=3\cdot7\cdot11\cdot23\cdot43\cdot47,\\
11352572&=4\cdot7\cdot11\cdot29\cdot31\cdot41,\\
11897340&=4\cdot3\cdot5\cdot7\cdot13\cdot2179.
\end{aligned}
\]

PARI certifies the following exact class data:

| `D` | `Cl(E)` | `Cl^+(E)` |
|---:|---|---|
| 10,078,365 | `C6 x C2 x C2` | `C6 x C2 x C2 x C2` |
| 10,737,573 | `C8 x C2 x C2 x C2` | `C8 x C2 x C2 x C2 x C2` |
| 11,352,572 | `C4 x C2 x C2 x C2` | `C4 x C2 x C2 x C2 x C2` |
| 11,897,340 | `C2 x C2 x C2 x C2` | `C2 x C2 x C2 x C2 x C2` |

In every field, localization at the first 205 prime ideals kills the entire
ordinary class group.  The compact `S`-unit basis then contains exactly

\[
 207=205+2
\]

pre-ray squareclasses, and its image in the full sign/mod-4 quotient
`(C_2)^4` has exact rank four.  Triviality of the localized class group and
full ray rank persist when more prime ideals are added.  Therefore throughout
the dense window

\[
 \boxed{d=T-2},                                      \tag{3.1}
\]

not the genus-relaxed value (1.1).  At the four advertised cells the rank
losses are respectively four, five, five, and five generators.

### Compact-unit handling

The verifier uses PARI's compact factored `S`-unit representation.  For odd
discriminants, every factor is a dyadic unit and its exact sign/mod-4
logarithm can be accumulated factor by factor.  In the two even-discriminant
fields, individual compact factors can have nonzero dyadic valuation that
cancels only in the complete `S`-unit.  Applying `ideallog` separately would
therefore be invalid.  The verifier instead reconstructs each whole element
exactly with `nffactorback` before taking its ray logarithm.  Both routes give
a certified rank-four matrix without numerical unit approximations.

## 4. Favorable all-useful no-go after the rank correction

After replacing the false genus ranks by (3.1), the verifier recomputes every
count `205<=T<=250` with

\[
 N_T=\left\lfloor{d^2-1\over4}\right\rfloor-(d+1)-T
\]

and grants all `N_T` useful roles.  It also replaces the Eisenstein packing
constant by the rigorous favorable lower bound

\[
 {11978\over10863}<{2\sqrt3\over\pi}.
\]

Lowering this constant increases a candidate's endpoint margin.  The exact
100-digit all-depth results are:

| relaxed leader | corrected best `T` | corrected `d` | best favorable margin |
|---:|---:|---:|---:|
| 10,078,365 | 209 | 207 | `-0.9434834995497257...` |
| 10,737,573 | 217 | 215 | `-1.3454597927258276...` |
| 11,352,572 | 217 | 215 | `-1.9886337283871262...` |
| 11,897,340 | 205 | 203 | `-2.6757061008385199...` |

For each of the 184 audited cells, the two endpoint margins are equalized,
the scale-one derivative is positive, and the scale-two derivative is
negative.  Concavity therefore certifies the global maximum of the lower
envelope.  The retained local depths also dominate the first omitted slope;
the elementary strict decrease of the local marginal sequence then makes the
calculation all-depth.

These margins are so negative that no exact CM usefulness scan is necessary:
any rejected ideal would only weaken a leader.

## 5. Verification

Run the complete finite scan and exact leader audit with

```bash
python3 phase2/loop/erdos1208/verify_quadratic_cm_genus_search_10_to_12m.py
```

This compiles four scanner instances, runs the half-million blocks
concurrently, prints their complete top-30 outputs, checks all finite counts,
and then executes the four certified PARI and 100-digit endpoint audits.  The
expected final line is

```text
10--12m genus-bonus screen and leader no-go: CERTIFIED
```

For a shorter independent rerun of only the theorem-level leader checks, use

```bash
python3 phase2/loop/erdos1208/verify_quadratic_cm_genus_search_10_to_12m.py --exact-only
```

The complete four-block enumeration was run successfully; the exact-only
mode was then rerun separately and passed.

## 6. Scope

This is a complete finite **relaxed nomination screen** on the stated
discriminant interval and count filter, followed by exact no-go audits of all
four interval leaders.  It does not assert that all 12,811 relaxed-positive
fields have the same localized rank as their leader.  Nor does it cover
counts outside `205..250`, nonprefix ramification sets, mixed inertia orders,
or discriminants above twelve million.

The durable conclusion is narrower but decisive for this search wave: the
four strongest genus-relaxed interval leaders are false positives, none
approaches the current record after exact localization, and the mandatory
10--12 million genus kill-search has produced no certifiable improvement.
