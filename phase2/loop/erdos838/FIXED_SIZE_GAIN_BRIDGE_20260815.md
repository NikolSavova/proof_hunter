# Erdős 838: exact fixed-size gain bridge

## Statement

Write `v_k(P)` for the number of convex `k`-subsets of a planar point set
`P`, and let

\[
        \mu_k(m)=\min_{|P|=m}v_k(P).
\]

Fix `eta>0`.  The following canonical fixed-size statement is sufficient for
an unconditional coefficient gain:

\[
 \mu_k(4^k)\geq 2^{(1+\eta-\varepsilon_k)k^2},
 \qquad \varepsilon_k\longrightarrow0.                 \tag{B1}
\]

Then every sufficiently large `N`-point set `P` satisfies

\[
 \log_2 V(P)\geq
 \left(\frac{1+\eta}{4}-o(1)\right)(\log_2 N)^2,        \tag{B2}
\]

where `V(P)` is the total number of nonempty convex subsets.

This formulation removes the quantifier ambiguity in the shorthand
`|P|=2^{2k+o(k)}`.  No limiting fixed-`k` density statement and no
uniformity outside the single canonical size `4^k` is required.

## Proof

Let

\[
        L=\log_2N,\qquad k=\lfloor L/2\rfloor,
        \qquad m=4^k.
\]

Then `m<=N`, `k=L/2+O(1)`, and every `m`-subset `S` of `P` contains at
least `mu_k(m)` convex `k`-subsets.  Double-count pairs `(A,S)` with `A` a
convex `k`-subset of `P` and `A subset S subset P`, `|S|=m`.  This gives

\[
 v_k(P){N-k\choose m-k}
 \geq {N\choose m}\mu_k(m),
\]

or equivalently

\[
 v_k(P)\geq
 \mu_k(m)\frac{{N\choose k}}{{m\choose k}}
 \geq\mu_k(m).                                      \tag{B3}
\]

Under (B1),

\[
 \log_2V(P)\geq\log_2v_k(P)
 \geq(1+\eta-\varepsilon_k)k^2
 =\left(\frac{1+\eta}{4}-o(1)\right)L^2.
\]

That is (B2).

## General interpolation formula

For comparison, suppose uniformly at a canonical scale

\[
 m_k=2^{\rho k+o(k)},\qquad
 \mu_k(m_k)\geq2^{\sigma k^2-o(k^2)}.
\]

Taking `k=beta log_2N` with `beta<=1/rho` in the same double count gives

\[
 \log_2v_k(P)\geq
 \bigl[\beta-(\rho-\sigma)\beta^2-o(1)\bigr](\log_2N)^2. \tag{B4}
\]

At `rho=2`, `sigma=1+eta`, the constrained maximum is attained at
`beta=1/2` and equals `(1+eta)/4`.

## Audit consequence

The primary target should therefore be stated as (B1), not merely with an
unquantified `2^{2k+o(k)}` point count.  A proof at `4^k` for every large
integer `k` is enough; a theorem only along an uncontrolled subsequence is
not.
