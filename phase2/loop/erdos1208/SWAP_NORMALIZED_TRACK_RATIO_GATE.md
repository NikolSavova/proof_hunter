# Low normalized track ratio is paid by the parallel pencil

> **Status update.**  Equation (1.3) remains valid, but the whole normalized
> track-energy branch is now bypassed by
> `SWAP_LOW_WEIGHT_FIRST_MOMENT_COLLAPSE.md`.  After truncating cell weight,
> first moment alone pays all occurrences from `Q_phys`; the only live direct
> obstruction is the very-rich-cell physical-wedge tail.

## 1. Outcome

The Hall-deficiency theorem reduces the low-cell-weight branch to

\[
 P_{norm}=\sum_\rho{1\over b(\rho)}{a(\rho)\choose2}, \tag{1.1}
\]

where `a(rho)` is the occurrence degree of one endpoint-labelled physical
track and `b(rho)` is its partner-token capacity.  This note closes every
row whose occurrence degree is at most a subpolynomial multiple of that
capacity.

For `R>=1`, put

\[
 P_{\le R}=\sum_{\rho:a(\rho)\le Rb(\rho)}
              {1\over b(\rho)}{a(\rho)\choose2}.  \tag{1.2}
\]

Then

\[
 \boxed{P_{\le R}\le6R Q_{phys}\le6R W_{parallel}.} \tag{1.3}
\]

The same-centre second moment `Q_phys` is already a subfamily of the
parallel-pencil reservoir.  Consequently every subpolynomial-ratio row is
target-paid.  The exact repeated-track survivor is

\[
 \boxed{
 P_{>R}=\sum_{\rho:a(\rho)>Rb(\rho)}
              {1\over b(\rho)}{a(\rho)\choose2}.} \tag{1.4}
\]

A row in (1.4) is one fixed physical directed edge, role, orientation, and
endpoint whose occurrence multiplicity is polynomially larger than the
entire partner-track diversity available at that endpoint.  This is much
narrower than a generic repeated-edge energy.

## 2. First-moment proof

If `a(rho)>=2`, then the same token is itself an allowed partner and hence

\[
 b(\rho)=s_x,                                    \tag{2.1}
\]

where `s_x` is the full token support at its endpoint.  Singleton rows have
zero contribution to (1.1).  On a row in (1.2),

\[
 {1\over b(\rho)}{a(\rho)\choose2}
 \le {R\over2}(a(\rho)-1)
 \le {R\over2}a(\rho).                           \tag{2.2}
\]

Every occurrence has six directed tracks and hence at most twelve
endpoint-track rows.  Therefore

\[
 \sum_\rho a(\rho)\le12|O_{hi}|.                 \tag{2.3}
\]

The occurrence cells all have load `r>=3`, and each cell contributes `r`
occurrences but `binom(r,2)` units to `Q_phys`.  Thus

\[
 |O_{hi}|\le\sum_Cr_C
 \le\sum_C{r_C\choose2}=Q_{phys}.                \tag{2.4}
\]

Combining (2.2)--(2.4) proves (1.3).

## 3. Consequence for the endpoint pencil

Choose subpolynomial cutoffs `W,R`.  The Hall and ratio theorems give

\[
 {\mathcal P_\Lambda\over3}
 \le N^{o(1)}(k^3+W_{parallel})
    +2W P_{>R}+M_{>W}.                            \tag{3.1}
\]

At this stage the Hall route appears to leave two objects:

1. `M_{>W}`, the very-rich owner-cell tail;
2. `P_{>R}`, the high-concentration normalized fixed-track energy.

Every pair in the second branch satisfies one zero coordinate in the exact
rank-five map.  The density condition `a>Rb` supplies the missing inverse
input: many owner occurrences reuse one track without generating comparable
endpoint-track diversity.  However the later first-moment identity pays the
entire low-weight population before this split, so no estimate for
`P_{>R}` is required for closure.

## 4. Scope

Equation (1.3) is unconditional.  No bound for (1.4) is claimed.  In
particular, polynomial-avoidance plantings can make linearly many low-load
owner blocks share one physical edge; this creates high ratio but is still
well below the `k^3+m^2` allowance.  The live theorem is an aggregate bound
for all such high-ratio rows, not a constant pointwise ratio.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_normalized_track_ratio.py
```

The verifier checks (1.3) on exhaustive load multisets and seeded random
row-incidence systems, including repeated roles and singleton rows.
