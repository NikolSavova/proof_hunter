# Prior-art and live-status audit (2026-08-13)

## Current planar window

The April 2026 text on the Erdős Problems page is stale.  The live rigorous
window is

\[
 n^{1/3}\ll F_2(n)\ll n^{1/2-\varepsilon}
\]

for some absolute \(\varepsilon>0\).

1. F. C. Clemen, J. Führer and O. Roche-Newton, *Geometric Sidon Problems*,
   arXiv:2606.05841 (4 June 2026), prove \(F_2(n)\gg n^{1/3}\) using the
   Li--Postle hypergraph independence theorem and incidence geometry.
2. S. Lee, C. Pohoata and D. G. Zhu, *The Minkowski grid has robustly many
   repeated distances*, arXiv:2607.05374 (6 July 2026), prove a robust theorem
   implying \(F_2(n)\ll n^{1/2-\varepsilon}\).
3. The latter paper began from Sungchul Lee's independent 14 June manuscript,
   *Planar Point Sets with Small Distinct-Distance Subsets*.  It validates and
   strengthens that manuscript; no gap, correction, or rebuttal was found.

The upper construction uses the bounded-root-discriminant, completely-split
number-field tower from Alon--Bloom--Gowers--Litt--Sawin--Shankar--Tsimerman--
Wang--Wood, arXiv:2605.20695, whose underlying input is Hajir--Maire--
Ramakrishna, *Cutting towers of number fields* (2021).  Its local sieve comes
from the split-prime/large-sieve work of Pohoata--Sheffer and
Croot--Mao--Pohoata--Sheffer--Yip, arXiv:2606.17487.

## Novelty check for this attack

The following were searched directly:

- the exact titles and citation neighborhoods of arXiv:2607.05374,
  arXiv:2606.17487 and arXiv:2606.13619;
- their complete TeX sources for `prime power`, `valuation`, and modulus-power
  variants;
- web and scholarly searches combining prime powers, valuation patterns,
  split primes, Minkowski grids, repeated distances and distance-Sidon sets.

No source was found for the \(K+1\) valuation-pattern amplification in
`proof_prime_power.md`, or for any explicit numerical exponent in the bound
\(F_2(n)\ll n^{1/2-\varepsilon}\).  This is only a targeted public-web check,
not a MathSciNet or expert clearance.  The correct novelty label is
**apparently new, pending external review**.

The proposed spherical transfer in `spherical_lower_candidate.md` was also
not located in the literature.  The 2015 CFGHUZ induction explicitly starts
from the older \(s_2(t)=O(t^3\log t)\); the 2026 planar paper does not state a
spherical corollary.

## Primary links

- https://www.erdosproblems.com/1208
- https://arxiv.org/abs/2606.05841
- https://arxiv.org/abs/2607.05374
- https://arxiv.org/abs/2605.20695
- https://arxiv.org/abs/1901.04354
- https://arxiv.org/abs/2606.17487
- https://arxiv.org/abs/1401.6734
- https://arxiv.org/abs/1412.2909
- https://doi.org/10.1007/s003730200063
- https://doi.org/10.1002/rsa.10102
- https://doi.org/10.1007/BF02582925
