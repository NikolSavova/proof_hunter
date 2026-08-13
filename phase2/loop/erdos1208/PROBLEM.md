# Erdős problem 1208

For fixed \(d\ge 2\), let \(F_d(n)\) be the largest integer such that every
\(n\)-point set in \(\mathbb R^d\) has an \(F_d(n)\)-point subset in which all
unordered pairwise distances are distinct.  Estimate \(F_d(n)\).

## Live status on 2026-08-13

The public Erdős Problems text is stale.  Two 2026 preprints change both ends of
the planar window:

\[
  n^{1/3}\ll F_2(n)\ll n^{1/2-\varepsilon}
\]

for some absolute \(\varepsilon>0\).

- Clemen--Führer--Roche-Newton, *Geometric Sidon Problems*,
  arXiv:2606.05841, remove the logarithmic loss in the lower bound.
- Lee--Pohoata--Zhu, *The Minkowski grid has robustly many repeated
  distances*, arXiv:2607.05374, prove the polynomial upper saving, validating
  and strengthening Sungchul Lee's 2026-06-14 independent draft.

Consequently, neither \(F_2(n)\gg n^{1/3}\) nor the bare assertion
\(F_2(n)\ll n^{1/2-\varepsilon}\) is new.

## This attack

`proof_prime_power.md` gives a candidate quantitative strengthening of the
upper construction.  Replacing the two isotropic choices at each split prime
by \(K+1\) valuation patterns modulo a prime power yields an explicit local
amplification lemma.  A rank-17 Golod--Shafarevich tower with 55 certified
split primes, together with an adaptive portfolio of 27 depth vectors, gives
the checkable numerical statement

\[
  F_2(n)\ll n^{0.49815}.
\]

`verify_adaptive_rank17.py` checks every finite arithmetic datum in the
stronger tower and the interval/exponent certificate.  The independent
rank-16 fallback is checked by `verify_explicit.py` and `verify_adaptive.py`.
The remaining non-computational inputs are stated explicitly in the proof.

`FULL_ATTACK.md` records the subsequent attempt to close the entire power
gap.  It proves a sharp local-lattice entropy barrier for the current upper
method and a conditional lower theorem: an \(n^{3-\delta}\) bound for the
all-distinct equal-distance quadruples would imply a distance-Sidon subset of
size

\[
 n^{\min\{(1+\delta)/3,\,0.431767\ldots\}-o(1)}.
\]

`verify_barriers.py` checks the numerical exponents.  The high distance-energy
case remains open, so the full asymptotic problem is not solved.

This is a candidate new partial result, not a solution of Problem 1208 and not
yet externally refereed.  Prior-art searches found the squarefree split-prime
sieve but no prime-power valuation-pattern version.
