# The 134-point menu: robust sampled spectrum and a finite W4 drop

**Date:** 2026-08-15. Counts are for nonempty convex subsets. This is
finite construction evidence only.

## Verdict

The explicit 134-point \(W_3\) parent from
*PARETO_TWO_LEVEL_RECURSIVE_MENU.md* can be rebuilt and queried robustly
without resolving its extremely small determinants in machine floating
point.

The three selected profiles of the 44-point parent are

\[
 (15121,102449),\qquad(44728,21566),\qquad(102449,15121), \tag{1}
\]

at chamber indices \(1873,791,1872\) in the deterministic 1884-chamber
enumeration. Unchecked exact rational strong glue with singleton endpoints
produces the intended 134-point parent with

\[
                         W_3=11358202734.                 \tag{2}
\]

Requesting 512 approximately equidistributed directions in one half-turn
produces 448 distinct exactly certified orders. Including reversals gives
894 distinct endpoint profiles. On this sampled menu,

\[
\min CU=2562123\cdot33305052
       =85331639745396,                                   \tag{3}
\]

and exact minimization of the next three-child recurrence gives

\[
\boxed{W_{4,\mathrm{sample}}
       =204331272672794}                                  \tag{4}
\]

on \(n_4=3\cdot134+2=404\) points. The witnesses are

\[
\begin{aligned}
 &(1118689,355504811),\\
 &(3842402,27715665),\\
 &(355504811,1118689).
\end{aligned}                                             \tag{5}
\]

The normalized coefficient is

\[
 {\log W_{4,\mathrm{sample}}\over(\log404)^2}
       =0.634137803896\ldots,                              \tag{6}
\]

down from \(0.669002\ldots\) at \(n=134\), but still well above \(1/2\).
Thus the W3 rebound is not monotone at the next sampled level. Equation
(4) is an upper bound from a sampled subset of the 134-point profile menu,
not the optimum over the full projection spectrum and not an asymptotic
construction theorem.

## 1. Why ordinary floating orientation is invalid

The exact rational 134-point gauge has minimum nonzero coordinate scale
about \(6.9\cdot10^{-22}\), minimum pair separation about
\(1.7\cdot10^{-32}\), and the smallest audited determinant is about
\(2.2\cdot10^{-72}\). Long-double orientation predicates therefore do not
certify its order type.

The sampler avoids this issue. The final parent is a five-block strong comb
with block sizes

\[
                         1,\ 44,\ 44,\ 44,\ 1.            \tag{7}
\]

Inside a 44-point block, orientation signs are the exact signs of the
certified parent, permuted by the selected chamber order. Across blocks,
the strong-glue signs are determined combinatorially:

* two points in an earlier block and one in a later block have negative
  sign in natural order;
* one point in an earlier block and two in a later block have positive
  sign;
* three points in three increasing blocks have negative sign.

The generator emits all \(\binom{134}{3}=392084\) signs from these exact
rules. Cap/cup dynamic programming in the C++ sampler therefore uses no
floating orientation test.

## 2. Robust direction sampling

Floating point is used only to propose quantile directions among the pair
walls. For each proposed direction \(s\), the generator replaces it by the
exact binary rational represented by the machine float and computes every
projection value

\[
                              x_i+s y_i                    \tag{8}
\]

with exact Fraction arithmetic. The resulting order is accepted only after
all 133 adjacent inequalities are strict. Thus every sampled order and
every reported \((C,U)\) pair is exact, although the sample is not claimed
to be uniformly distributed among the exact chambers.

The floating proposal stage sees 7438 distinct finite half-turn walls in
this very compressed gauge. Some nearly coincident exact walls coalesce,
and several requested probes repeat an already retained order. This
explains the 448 half-turn orders; it is not treated as an exhaustion
count.

## 3. Exact menu optimization

For a child profile \(p=(C,U)\), the dependence of the five-block
recurrence on the first of three children is a line

\[
                         U+C X,                            \tag{9}
\]

where, for the second and third profiles,

\[
             X=U_2+135U_3+135^2.                          \tag{10}
\]

The C++ checker stores these lines in an exact discrete Li Chao tree over
all query values (10). It then checks every ordered second/third pair in
\(O(p^2\log p)\) time, using unsigned 128-bit arithmetic for all recurrence
values. This replaces the original cubic profile loop and gives exactly
the same result on the 894-profile audit.

The convergence under evenly spread subsamples of the 448 retained
half-turn orders is:

\[
\begin{array}{c|c|c}
\text{orders}&\text{profiles}&W_{4,\mathrm{sample}}\\ \hline
16&30&393713912862751\\
32&62&282819571977086\\
64&126&239697020490560\\
128&254&239540884375093\\
256&510&219960016140312\\
384&766&204331272672794\\
448&894&204331272672794.
\end{array}                                               \tag{11}
\]

The last two samples agree, modest finite evidence that (4) is not a
single isolated direction. The subsamples are spread independently and
are not presented as a nested monotonic sequence.

## 4. Scope

This audit establishes only the following:

1. the exact 44-point parent and selected chambers reconstruct an explicit
   rational 134-point strong-comb candidate;
2. every one of the 894 sampled profiles is certified by exact signs and
   an exact projection order;
3. the scalar recurrence on that sampled menu has the exact minimum (4).

The final 134-point strong-glue coordinates are generated by the same
rational formula as the certified smaller construction, but its cubic
top-split assertion is intentionally not rechecked point by point.
Accordingly (4) should be cited as a sampled construction-side upper bound,
not as a new exact full-spectrum certificate.

The result is also gauge-specific. Other embeddings with the same
strong-glue chirotope can change disjoint-pair wall order and may have a
lower or higher sampled menu. Nothing here supplies a direction-spectrum
potential or a recursively closed decorated-state theorem.

## 5. Verification

A quick rerun using an already generated input is:

    python3 phase2/loop/erdos838/agent_root_followup/verify_level4_sampled_spectrum.py \
      --input /tmp/level4_sample512.in

To regenerate the exact combinatorial input from the 44-point certificate
and run the full audit:

    python3 phase2/loop/erdos838/agent_root_followup/verify_level4_sampled_spectrum.py

The fresh run takes several minutes because it reconstructs and exhausts
the 44-point spectrum before building the 134-point parent. Expected
output is:

    PASS: exact sampled profiles=894; W4_sample=204331272672794; n=404 coefficient=0.634137803896

The artifacts are:

* *generate_level3_parent_coordinates.py* -- exact rational W3 parent;
* *generate_level4_sampled_input.py* -- exact signs and certified sampled
  orders;
* *explore_level4_sampled_spectrum.cpp* -- chain DP and exact fast W4
  optimization;
* *verify_level4_sampled_spectrum.py* -- deterministic end-to-end checker.
