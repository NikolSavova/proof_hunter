# Oriented radial entropy chain: arbitrary sparse families are paid

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

Inside one fixed-tangent radial containerization, the proposed replacement
is true for an arbitrary sparse family.  In fact explicit routing through
every prefix is unnecessary.  Merge all distinct source words, take their
coordinate supports, and use the ambient one-gap bank.  Correlation in the
sparse family appears as a nonnegative support-redundancy term and can only
make the bank stronger.

Let

\[
             \mathcal F\subseteq X_1\times\cdots\times X_q,
             \qquad M=|\mathcal F|,                       \tag{1}
\]

be the petal words in one radial cell.  Delete unused labels and put
`L_i=|X_i|`, `s_i=log L_i`.  For a uniform random word `Z in mathcal F`,
orient the cyclic list from the retained tangent cell and define

\[
 h_i=H(Z_i\mid Z_1,\ldots,Z_{i-1}),qquad
                 \sum_i h_i=\log M.                       \tag{2}
\]

Let `H_i` be the number of nonempty ordinary faces in cluster `i`, and let
`A_i,R_i` be its two directional chain-profile counts.  Thus
`A_iR_i>=H_i`.  If `B_j` is the ordinary one-gap bank which omits cluster
`j`, then

\[
 B_j=R_{j-1}A_{j+1}
       \prod_{i\notin\{j-1,j,j+1\}}L_i.                  \tag{3}
\]

The exact entropy-chain theorem is

\[
 \boxed{
 \max_j B_j\ge M,2^{\Gamma(\mathcal F)},\quad
 \Gamma(\mathcal F)=
 \sum_i(s_i-h_i)+{1\over q}\sum_i(\log H_i-3s_i).}       \tag{4}
\]

The first term is exactly

\[
             \sum_i(s_i-h_i)=log{\prod_iL_i\over M},     \tag{5}
\]

the support redundancy of the sparse family.  It vanishes on a Cartesian
product and is positive for every correlation or code constraint.  Thus a
sparse subfamily cannot defeat the radial bank by destroying rectangles;
the missing rectangles are already counted by (5).

Using the established planar reservoir in each cluster, there is an
absolute constant `C` such that

\[
                         \log H_i\ge {s_i^2\over9}-C.      \tag{6}
\]

For `q>=4`, `h_i<=s_i` and (4) imply the purely conditional-entropy bound

\[
 \boxed{
 \Gamma(\mathcal F)\ge
 {1\over9q}\sum_i h_i^2-{3\over q}\log M-C
 \ge { (\log M)^2\over9q^2}-{3\log M\over q}-C.}         \tag{7}
\]

Consequently, if `q<=kappa log D`, every `L_i<=D`, and
`log M>=a(log D)^2`, then

\[
 \log{\max_jB_j\over M}
 \ge {a^2\over9\kappa^2}(\log D)^2-O(\log D).            \tag{8}
\]

This is much larger than every fixed power of `D`.  It proves that there is
no sparse-family counterexample in a common radial cell.

The global decoder issue also closes at this scope.  Arbitrarily many
subfamilies on the same base and cyclic containers are first merged into
their union `mathcal F`; the bank is counted once.  Choose the least gap
`j` attaining the maximum in (4).  A bank output occupies exactly the macro
clusters `[q]-{j}`, so it recovers `j` and every local profile/point choice.
The decoder load is one, not the number of prefixes or subfamilies.

For weighted histories, let `mu` be the maximum aggregate weight on one
geometric source word.  If their total weight is `W`, then

\[
                 W\le\mu M\le\mu,2^{-\Gamma(\mathcal F)}V(P).    \tag{9}
\]

Thus any `mu=2^{o((log D)^2)}` is harmless in the quadratic regime.  Some
multiplicity condition is necessary: repeating the identical source word
with arbitrary history weight changes neither the configuration nor any
one-gap face.  Across genuinely different bases or unrecoverable cyclic
containerizations, (4) remains local and the previously identified
cross-base summation problem remains.

This theorem explains the KK regression precisely.  Its complete
transversal family has `h_i=s_i`, so (5) is zero; the large profile term in
(4) pays it.  A sparse code or prefix-correlated family lowers
`sum h_i` relative to `sum s_i`, and the lost source rectangles reappear
one-for-one as support redundancy.  There is no third sparse branch.

## 1. Exact cyclic identity

Put `P_0=prod_iL_i`.  Dividing (3) by `P_0` and multiplying cyclically
gives

\[
 \prod_{j=1}^q{B_j\over P_0}
       =\prod_{i=1}^q{A_iR_i\over L_i^3}
       \ge\prod_{i=1}^q{H_i\over L_i^3}.                 \tag{10}
\]

Every factor has a transparent origin.  Cluster `i` is absent once, is an
endpoint profile once from each side, and is an arbitrary singleton in the
remaining `q-3` banks.  Hence it contributes `A_iR_iL_i^(q-3)` before
division, exactly as (10) records.

Taking logarithms and a geometric mean,

\[
 \begin{aligned}
 \log{\max_jB_j\over M}
 &\ge \log{P_0\over M}
       +{1\over q}\sum_i(\log H_i-3\log L_i)\\
 &=\sum_i(s_i-h_i)
       +{1\over q}\sum_i(\log H_i-3s_i),                 \tag{11}
 \end{aligned}

because the Shannon chain rule gives (2).  This is (4).  No independence,
uniform fibre size, density, or Cartesian subfamily is assumed.

The first-divergence orientation enters through the cyclic order and the
two endpoint profiles in (3).  Prefix nodes themselves should not be
routed separately: doing so can repeat the same untagged one-gap face many
times.  Equation (11) is the global telescope which sums those nodes before
measuring face reuse.

## 2. Reduction to conditional alphabet entropies

The universal planar face lower bound implies (6), after weakening its
asymptotic constant and absorbing finitely many small cluster sizes into
`C`.  Substitute it into (4):

\[
 \Gamma\ge
 \sum_i(s_i-h_i)+{1\over9q}\sum_i s_i^2
                         -{3\over q}\sum_i s_i-C.         \tag{12}
\]

Since `h_i<=s_i` and `q>=4`, the coefficient `1-3/q` of each linear `s_i`
is nonnegative.  Replacing `s_i` by `h_i` in the right side can only lower
it, giving

\[
 \Gamma\ge {1\over9q}\sum_i h_i^2
                       -{3\over q}\sum_i h_i-C.           \tag{13}
\]

Cauchy--Schwarz and (2) give (7).

For (8), write `d=log D`.  Then

\[
 { (\log M)^2\over9q^2}
       \ge {a^2\over9\kappa^2}d^2,
 \qquad
 {3\log M\over q}=O(d),                                  \tag{14}
\]

because `log M<=sum_i log L_i<=qd`, so
`3log M/q<=3d`.  This proves the claimed quadratic multiplier.

The sum of squares in (13) is useful when the entropy is uneven.  It is
strictly stronger than the final Jensen form whenever a few conditional
alphabets carry most of the information.

## 3. Recoverability and global consolidation

Every face in `mathcal B_j` has a unique macro active set
`[q]-{j}`.  Its intersections with the disjoint cluster neighbourhoods
recover the two endpoint chains and every retained singleton.  Therefore
the description in (3) is injective and `j` is visible from the face.
Choosing the least maximizing gap makes the bank canonical.

Suppose a collection of selected subfamilies `mathcal F_c` uses the same
fixed base, tangent state, repair mark/shield, cyclic cluster list, and
geometric word-to-source map.  Put

\[
                         \mathcal F=\bigcup_c\mathcal F_c. \tag{15}
\]

Apply (4) once to (15).  This loses no distinct source occurrence: equal
words are the same ordinary source face.  If histories give a word
multiplicity, aggregate them into a weight `w(D)` and put
`mu=max_Dw(D)`.  Then

\[
 W=\sum_Dw(D)\le\mu|\mathcal F|,                          \tag{16}
\]

which together with `V(P)>=max_jB_j` proves (9).

This consolidation is the promised global load control.  It is stronger
than tagging every first-divergence prefix: the same ambient bank is never
spent twice.  If `mu` is unbounded, no theorem using ordinary faces can
control `W`; arbitrary repeated histories are invisible to geometry.

The argument does not merge cells with different bases when adding the
base to a detached bank can destroy convexity, nor does the detached output
identify an unrelated containerization.  Such cells require the existing
source-pair/Cauchy decoder or a separate cross-base theorem.  Equation (4)
settles exactly the common fixed-tangent radial atom asked for here.

## 4. Sharpness tests

Three families show why every term in (4) is correctly placed.

1. **Full tensor.**  For `mathcal F=prod_iX_i`, `h_i=s_i` and support
   redundancy is zero.  The theorem reduces exactly to the cyclic profile
   identity (10).
2. **Diagonal code.**  If all coordinates equal one symbol, then
   `log M=s_1` in a suitable chain order while every marginal support has
   size `M`.  The redundancy `(q-1)log M` records the entire ambient
   cross-completion bank missed by the selected diagonal.
3. **Disjoint parity cosets.**  Several dense subfamilies can have the same
   full coordinate supports and therefore the same one-gap bank.  Merging
   their distinct words before applying (4) counts that bank once and
   exactly removes the artificial context overlap.

Thus support redundancy cannot be discarded, while paying a bank once per
prefix or coset is unnecessary and can be sharply wasteful.

## 5. Exact verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_oriented_radial_entropy_chain.py
```

The checker uses the rational five-cluster projectively universal radial
order type.  It verifies all 1,024 transversals, the five disjoint
400-face one-gap banks, the exact cyclic product identity, and the local
profile inequality `25>=14`.  For full-product, diagonal, linear-code,
and prefix-correlated sparse families it checks the Shannon chain rule in
the exact exponentiated integer form

\[
 \prod_i 2^{M h_i}=M^M,                                  \tag{17}
\]

as well as (4) without floating point.  It also audits parity-coset
consolidation, weighted multiplicity (9), and the quadratic asymptotic
exponent in (7).
