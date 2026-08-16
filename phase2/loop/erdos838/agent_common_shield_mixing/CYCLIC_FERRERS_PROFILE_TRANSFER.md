# Cyclic Ferrers transfer: the exact on-word invariant and an anti-alignment barrier

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

There is an exact cyclic one-face transfer theorem, but its input is the
profile mass seen by the **actual valid-word distribution**, not the
unweighted sizes of the local left and right reservoirs.

Let `Omega` be the valid full words in cyclic ear containers.  If
`a_i(x)` and `r_i(x)` count the left and right directional profiles anchored
at label `x` in container `i`, and a compatible marked seam really splices
to one recoverable ordinary face, then some cyclic seam has a bank of size

\[
 \boxed{
 \max_i B_i\ge |\Omega|\,
 \mathbb E_{X\in\Omega}
 \left[\prod_i a_i(X_i)r_i(X_i)\right]^{1/q}.}            \tag{1}
\]

In particular,

\[
 {\max_iB_i\over|\Omega|}
 \ge2^{\frac1q\sum_i
       \mathbb E\log(a_i(X_i)r_i(X_i))}.                 \tag{2}
\]

This is the correct cyclic Kraft/transfer invariant.  It is stronger than
a minimum-profile bound and needs no independence.  It also identifies the
remaining geometric obligation exactly: the marked profile splice must be
an ordinary face and the on-word geometric mean in (1) must be large.

Ferrers adjacency alone supplies neither fact.  There is a scalable even
cycle with alphabet size `L=2^d`, `q=d`, and alternating Ferrers thresholds

\[
 x_1\le x_2\ge x_3\le x_4\ge\cdots\ge x_1.              \tag{3}
\]

It has `M` valid full words with

\[
                   2^{d^2-d}\le M\le2^{d^2}.             \tag{4}

Every label occurs in a valid word.  Nevertheless put all rich profiles on
the upper half of every odd container and the lower half of every even
container.  Every rich right--left pair is incompatible at every seam.  If
each rich anchor carries `T=2^{d^2}` profiles in each direction, then every
container has formal local two-ended reservoir

\[
              A_iR_i=\left({LT\over2}\right)^2
                    =2^{2d^2+2d-2},                      \tag{5}
\]

but

\[
                              B_i=0\qquad\text{for all }i. \tag{6}

Thus no lower bound for a one-face seam bank can depend only on `M`, the
Ferrers property, and the totals `A_i,R_i` or `A_iR_i`.  The obstruction is
not unused support, sparse entropy, or a non-Ferrers `2K2`: every threshold
matrix is Ferrers, all source labels occur, and the source entropy has
coefficient one.  It is pure directional anti-alignment.

There is a conditional easy branch worth recording.  If a directional
profile is itself compatible with the fixed base, and profiles on
nonadjacent ears commute, then a proper coloring of the ear cycle gives an
ordinary independent-ear bank

\[
 \max_c|\mathcal I_c|
 \ge\left(\prod_i A_iR_i\right)^{1/(2\chi(C_q))}
 \ge\left(\prod_iH_i\right)^{1/(2\chi(C_q))}.             \tag{7}
\]

Here `chi(C_q)=2` for even `q` and `3` for odd `q`.  With the established
local planar reservoirs, quadratic source entropy makes (7)
super-quadratic-exponential.  The intended hard geometry is outside this
branch: its cap/cup profiles are detached and not individually compatible
with the fixed base.  The rational circuit in
`DOMINANCE_CELL_SEPARATED_ONE_GAP.md` is an actual planar witness to that
failure.

Accordingly, the missing planar theorem cannot be “Ferrers plus large
local reservoirs.”  It must force one of:

1. a fixed-power lower bound for the on-word profile mean in (1);
2. a monotone alignment of profile-rich anchors with the Ferrers
   thresholds; or
3. an independent-ear/base-compatible profile branch covered by (7).

## 1. The marked cyclic splice model

Let `q>=3` and let `X_1,...,X_q` be finite label sets.  For every cyclic
seam `i`, let

\[
                         E_i\subseteq X_i\times X_{i+1}   \tag{8}
\]

be the adjacent-ear compatibility relation.  Indices are modulo `q`.  A
full word is valid when

\[
 \Omega=\{x=(x_1,\ldots,x_q):(x_i,x_{i+1})\in E_i
                                      \text{ for all }i\}.          \tag{9}
\]

This is the exact abstract meaning of “nonadjacent ears commute”: there are
no constraints beyond adjacent seams.  Ferrers geometry says that after
ordering the two alphabets at each seam, the row neighborhoods of `E_i`
are nested.  The transfer theorem below does not need Ferrers; Ferrers is a
possible geometric mechanism for certifying the splice.

For `x in X_i`, let

\[
 a_i(x),r_i(x)\in\mathbb Z_{\ge0}                         \tag{10}
\]

be the numbers of distinguishable left and right directional profiles
anchored at `x`.  Make the following explicit one-face hypothesis at seam
`i`:

> for every `x in Omega`, every right profile counted by `r_i(x_i)`, and
> every left profile counted by `a_(i+1)(x_(i+1))`, the marked replacement
> together with the retained traces in the other containers is one ordinary
> face; the resulting face recovers the word and the two profile choices.

Under this hypothesis the seam bank has the exact size

\[
 B_i=\sum_{x\in\Omega}r_i(x_i)a_{i+1}(x_{i+1}).           \tag{11}

If the output decoder has load `Lambda_i` rather than one, replace `B_i`
by `B_i/Lambda_i` in every global face-count conclusion.  Formula (11)
keeps the geometric splice and the overlap issue visible; neither is
hidden inside the word “Ferrers.”

## 2. Exact cyclic profile-transfer theorem

Put

\[
                  h_i(x)=a_i(x)r_i(x),\qquad M=|\Omega|.  \tag{12}
\]

> **Theorem 1 (cyclic on-word profile transfer).**  In the marked splice
> model, (1) holds.  With the convention `log 0=-infinity`, (2) also holds.

**Proof.**  For a valid word `x`, set

\[
                     w_i(x)=r_i(x_i)a_{i+1}(x_{i+1}).     \tag{13}
\]

Cyclic cancellation gives

\[
                         \prod_iw_i(x)=\prod_ih_i(x_i).   \tag{14}
\]

Therefore AM--GM, followed by averaging over the uniform valid word, gives

\[
\begin{aligned}
 {1\over qM}\sum_iB_i
 &=\mathbb E{1\over q}\sum_iw_i(X)\\
 &\ge\mathbb E\left(\prod_iw_i(X)\right)^{1/q}
  =\mathbb E\left(\prod_ih_i(X_i)\right)^{1/q}.          \tag{15}
\end{aligned}
\]

The maximum `B_i/M` is at least their average, proving (1).  Applying
Jensen to the exponential in the last expectation gives (2).  QED.

This theorem is distributional but completely explicit.  For example, if

\[
 {1\over q}\sum_i\mathbb E\log h_i(X_i)
                          \ge(1+\epsilon)\log D+\log\Lambda,        \tag{16}
\]

where every seam bank has decoder load at most `Lambda`, then

\[
                  V(P)\ge D^{1+\epsilon}M.                \tag{17}

Equivalently, it pays `D^2M<=D^{1-epsilon}V(P)`.  Thus (16), not an
unweighted reservoir product, is the exact fixed-power gate.

Two useful sufficient versions are immediate.

* If every label used by `Omega` satisfies `h_i(x)>=eta_i`, then
  `max_iB_i>=M(product_i eta_i)^(1/q)`.
* More generally, it suffices that a subfamily `Omega'` of weight `theta M`
  has on-word geometric mean at least `K`; then some seam bank has size at
  least `theta MK`.

The second version is the natural output of a high-energy localization or
a monotone Ferrers layer cake.  The theorem says exactly what that
localization must preserve.

## 3. Alternating Ferrers-cycle anti-alignment

Take even `q` and an even alphabet size `L`.  Let every `X_i=[L]`.  Define

\[
 E_i=\begin{cases}
       \{(x,y):x\le y\},&i\text{ odd},\\
       \{(x,y):x\ge y\},&i\text{ even}.
     \end{cases}                                         \tag{18}
\]

Every row neighborhood is an initial or final interval, and the
neighborhoods are nested.  Hence every `E_i` is Ferrers in the strongest
threshold sense.

The valid words are cyclic alternating sequences (3).  All words with odd
coordinates in `[1,L/2]` and even coordinates in `[L/2+1,L]` are valid.
Consequently

\[
                         (L/2)^q\le M\le L^q.             \tag{19}
\]

There is also an exact transfer-matrix formula.  Write `q=2m` and let

\[
                         K_{ab}=L-\max(a,b)+1
                         \qquad(1\le a,b\le L).            \tag{19a}
\]

After fixing the `m` odd-coordinate valleys, the even coordinate between
valleys `a,b` has exactly `K_ab` choices.  Hence

\[
                              M=\operatorname{tr}(K^m).   \tag{19b}
\]

The verifier evaluates (19b) exactly using the nested-row structure of
`K`, in `O(mL^2)` integer operations.

Moreover `(t,t,...,t)` is valid for every `t in[L]`, so no alphabet label
can be removed as unused.

Fix any positive integer `T`.  Define the rich anchor set and profile
multiplicities by

\[
 S_i=\begin{cases}
       [L/2+1,L],&i\text{ odd},\\
       [1,L/2],&i\text{ even},
     \end{cases}
 \qquad
 a_i(x)=r_i(x)=T\,1_{x\in S_i}.                          \tag{20}
\]

The two unweighted directional totals in every container are

\[
                    A_i=\sum_xa_i(x)={LT\over2},\qquad
                    R_i=\sum_xr_i(x)={LT\over2}.          \tag{21}
\]

At an odd seam, a rich left anchor is in the upper half and the next rich
right anchor is in the lower half, so `x<=y` fails.  At an even seam the
halves are reversed and `x>=y` fails.  Thus no compatible seam has both
profile multiplicities positive, proving (6) directly from (11).

Equivalently every valid word has

\[
                              \prod_ih_i(x_i)=0.           \tag{22}

The right side of the true transfer theorem (1) is therefore zero, exactly
as it must be.  On the other hand the false totals-only analogue would see

\[
 \left(\prod_i{A_iR_i\over L^2}\right)^{1/q}
                              ={T^2\over4}.               \tag{23}

This can be made arbitrarily large without changing a single Ferrers
matrix or source word.

Now put `L=D=2^d`, take even `q=d`, and choose `T=2^{d^2}`.  Equations
(19), (21), and (23) become (4)--(6).  The source entropy is genuinely
quadratic, while the formal profile multiplier is itself
quadratic-exponential.  Still every adjacent one-face profile bank is
empty.  This is the requested scalable Ferrers-cycle anti-alignment.

The example is an abstract transfer obstruction, not a planar EIC
counterexample.  It proves that the listed abstract data are insufficient.
An actual planar theorem may rule it out, but only by using a relation
between the two directional profile orders of the same ear around the
cycle.  That relation is the missing history coordinate.

## 4. Conditional independent-ear branch

For completeness, suppose instead that every profile in `mathcal A_i` or
`mathcal R_i` is individually compatible with the fixed base, and arbitrary
choices on a set of pairwise nonadjacent ear positions commute.  Let
`A_i=|mathcal A_i|`, `R_i=|mathcal R_i|`, and suppose `A_iR_i>=H_i`.

Color the cycle properly with `chi=chi(C_q)<=3` colors.  In each position
choose the larger of its two directional families.  For a color class
`C`, commuting gives a one-face bank of size

\[
                              I_C=\prod_{i\in C}\max(A_i,R_i).       \tag{24}
\]

Multiplying over color classes,

\[
 \prod_CI_C=\prod_i\max(A_i,R_i)
       \ge\prod_i\sqrt{A_iR_i}
       \ge\left(\prod_iH_i\right)^{1/2}.                 \tag{25}
\]

Taking a geometric mean proves (7).

If `L_i` is the used point alphabet in container `i`, `s_i=log L_i`,
`prod_iL_i>=M`, and the local reservoir bound has the form

\[
                         \log H_i\ge c s_i^2-C,            \tag{26}
\]

then (7) and Cauchy give

\[
 \log\max_CI_C
 \ge {c\over2\chi}\sum_i s_i^2-O(q)
 \ge {c(\log M)^2\over2\chi q}-O(q).                    \tag{27}
\]

For `log M=Omega((log D)^2)` and `q=O(log D)`, this is
`Omega((log D)^3)`.  Hence this branch is far stronger than the desired
fixed-power gain.  Its failure in the hard geometry must be recorded
explicitly: detached cap/cup profiles need not remain ordinary after the
base is adjoined.  Ferrers compatibility of the selected rooted ears does
not change that fact.

## 5. Exact remaining planar statement

The cyclic Ferrers route is reduced to the following honest target.

> In a fixed convex-base ear cycle with quadratic entropy, prove that a
> fixed-power fraction of valid words has large on-word profile geometric
> mean, as in (16), or prove that one directional profile family becomes
> individually base-compatible on an independent set of ear positions.

A mere bound on `A_iR_i`, even one of quadratic-exponential size in every
container, cannot imply the target.  Nor can one apply the complete cyclic
profile identity from the strong radial model: that identity assumes every
endpoint profile pair cross-splices, precisely what (18)--(23) destroy.

The useful new invariant to carry through the planar history is

\[
 \boxed{\quad
 \Gamma(\Omega)=
 \mathbb E_{X\in\Omega}
       \left[\prod_i a_i(X_i)r_i(X_i)\right]^{1/q}.
 \quad}                                                   \tag{28}
\]

Theorem 1 converts `Gamma` directly into one ordinary-face mass.  The
alternating Ferrers cycle proves that any attempt to replace `Gamma` by
unweighted local totals loses the entire quadratic coefficient.

## Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_cyclic_ferrers_profile_transfer.py
```

The checker verifies Theorem 1 on exact random integer systems, computes
the alternating-cycle word count by an exact structured transfer matrix,
checks every Ferrers nesting and zero profile seam, verifies the
quadratic-entropy coefficients through `d=8`, and audits the independent
ear coloring bound.
