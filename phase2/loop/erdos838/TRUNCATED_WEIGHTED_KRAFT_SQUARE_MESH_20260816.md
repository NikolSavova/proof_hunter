# Truncated weighted Kraft removes the harmonic loss

**Date:** 2026-08-16. All logarithms are base two.

## Verdict

The false normalized inequality in
`WEIGHTED_NORMALIZED_KRAFT_BARRIER_20260816.md` is not needed.  Applying
ordinary hinged Kraft to one **mass-truncated** child alphabet gives a much
sharper heterogeneous square mesh than the earlier harmonic summation.

Let an ordered generic macro chart have child sizes

\[
 n_1,\ldots,n_m\geq1,\qquad N=\sum_i n_i,\qquad
 L=\log N,\quad q=\log m,\quad \ell_i=\log n_i.
\]

Let \(R_i=A_i+B_i\) be the exact weighted cap-plus-cup endpoint reward at
position \(i\), where using sibling \(j\) contributes \(\log(1+n_j)\), and
put

\[
                 \mathcal B=\max_i\left\{{\ell_i^2\over2}+R_i\right\}.
                                                               \tag{1}
\]

For every real \(s>0\), set

\[
                  \varepsilon_s=-\log(1-2^{-s}).              \tag{2}
\]

Then

\[
 \boxed{
 \mathcal B\geq {1\over2}(L-\varepsilon_s)^2
                 -{1\over2}(q+s)^2.}
                                                               \tag{3}
\]

If the right side is positive, the proof below is literal.  If the
truncation threshold is nonpositive, the right side is nonpositive and (3)
is automatic.

Taking

\[
                   s=\lceil\log L\rceil+2                    \tag{4}
\]

gives the explicit corollary

\[
 \boxed{
 \mathcal B\geq {L^2\over2}
 -{1\over2}\{\log m+\log L+3\}^2-{1\over3\ln2}.}
                                                               \tag{5}
\]

Thus the local loss is

\[
                     O\bigl((\log m+\log\log N)^2\bigr),      \tag{6}
\]

instead of the previous \(O(L\log\log(m+1))\) harmonic loss.
The improvement is exact and does not require the maximizing endpoint paths
at different weight thresholds to nest.

This is a construction-side/local Bellman theorem.  It does not promote an
arbitrary point set to a recursive chart and therefore does not improve the
unrestricted lower coefficient by itself.  It does, however, remove the
harmonic factor as a plausible obstruction whenever the macro arity is
subexponential on the logarithmic scale.

An arity-sensitive choice is slightly sharper.  If $L\geq2(q+1)$, take

\[
             s=\left\lceil\log{L\over q+1}\right\rceil+2.  \tag{7}
\]

Then

\[
 \mathcal B\geq {L^2\over2}
 -{1\over2}\left\{q+\log{L\over q+1}+3\right\}^2
 -{q+1\over3\ln2}.                                      \tag{8}
\]

This form makes clear that the loss is quadratic in the macro information
$q$, not linear in the ambient scale $L$.

## 1. Keep almost all mass in one alphabet

Assume first that

\[
                         t:=L-q-s>0.                         \tag{9}
\]

Retain the positions

\[
                         S=\{i:\ell_i\geq t\}.               \tag{10}
\]

Every discarded child has fewer than \(2^t\) points, so the discarded mass
is smaller than

\[
                         m2^t=N2^{-s}.                       \tag{11}
\]

Writing \(N_S=\sum_{i\in S}n_i\) and \(L_S=\log N_S\), we obtain

\[
                  N_S>N(1-2^{-s}),\qquad L_S>L-\varepsilon_s.
                                                               \tag{12}
\]

Also

\[
                         0\leq L_S-t\leq q+s.               \tag{13}
\]

## 2. Use the full Kraft sum

Restrict the macro chart to \(S\).  For \(i\in S\), let \(h_i\) be its
hinged cap-plus-cup code length in the induced chart.  The exact hinged
theorem gives

\[
                         \sum_{i\in S}2^{-h_i}\leq1.          \tag{14}
\]

The two induced endpoint paths remain valid in the full chart.  Every
nonanchor position on them lies in \(S\), and hence contributes at least
\(t\).  Therefore

\[
                              R_i\geq t h_i.                  \tag{15}
\]

Equation (15) does **not** assert the false pointwise normalization
\(R_i\geq\ell_i h_i\).  Its denominator is the one common truncation scale
\(t\), which is exactly why the counterexample to normalized Kraft does not
apply.

By (1), \(R_i\leq\mathcal B-\ell_i^2/2\).  Consequently

\[
\begin{aligned}
 1
 &\geq\sum_{i\in S}2^{-R_i/t}\\
 &\geq2^{-\mathcal B/t}
      \sum_{i\in S}2^{\ell_i^2/(2t)}.                       \tag{16}
\end{aligned}
\]

For \(\ell_i\geq t\),

\[
 {\ell_i^2\over2t}\geq\ell_i-{t\over2},                   \tag{17}
\]

because the difference is \((\ell_i-t)^2/(2t)\).  Substituting (17) into
(16) gives

\[
 \mathcal B
 \geq t\log\left(2^{-t/2}\sum_{i\in S}2^{\ell_i}\right)
 =tL_S-{t^2\over2}
 ={L_S^2\over2}-{(L_S-t)^2\over2}.                         \tag{18}
\]

Now use (12)--(13) in (18) to obtain (3).

If \(t\leq0\), then \(q+s\geq L>L-\varepsilon_s\), so the right side of
(3) is negative, whereas \(\mathcal B\geq0\).  Thus (3) holds in all cases.

## 3. The explicit logarithmic choice

Since \(N\geq m\geq2\), we have \(L\geq1\).  With (4),

\[
 2^{-s}\leq{1\over4L},\qquad
 \varepsilon_s
 \leq{2^{-s}\over(1-2^{-s})\ln2}
 \leq{1\over3L\ln2}.                                    \tag{19}
\]

Hence

\[
 {1\over2}(L-\varepsilon_s)^2
 \geq {L^2\over2}-{1\over3\ln2},                         \tag{20}
\]

and \(q+s\leq\log m+\log L+3\).  Equations (3), (19), and
(20) prove (5).  The same calculation with (7) uses
$2^{-s}\leq(q+1)/(4L)$ and proves (8).

## 4. Scope and next use

The theorem settles the local witness-switching issue to polylogarithmic
square loss.  Two genuinely global tasks remain:

1. charge the losses along a recursive history when macro arities and scale
   jumps both vary; and
2. in the unrestricted problem, obtain a configuration-specific recursive
   chart or bypass it with the fixed-rank mixed/profile bank.

In particular, (3) is not a fixed-size supersaturation theorem and is not
claimed to improve the rigorous coefficient window \([1/4,1/2]\).

## 5. Verification

Run

~~~text
python3 phase2/loop/erdos838/verify_truncated_weighted_kraft_square_mesh.py
~~~

The verifier reconstructs endpoint rewards and induced hinged profiles,
checks the exact dyadic Kraft inequality, checks (15) at the selected
truncation, and tests (3) and (5) on exhaustive four-position edge orders,
the normalized-Kraft counterexample, and deterministic heterogeneous random
instances.  The algebraic proof is Sections 1--3; floating-point tests are
regressions only.
