# Macroscopic vertical jumps: exact mean transfer and the remaining escape

**Date:** 2026-08-14  
**Verdict:** no realizable coefficient below `1/2` is produced here.  There
is, however, a rigorous barrier covering arbitrary depth-dependent,
macroscopically large, possibly indecomposable macro templates in the
homogeneous vertical substitution model.  A macro jump cannot lower the
quadratic coefficient merely by having a favorable finite-activity
partition polynomial.  It can escape the `1/2` barrier only by importing a
positive-scale macro which already has either sub-`1/2` total convex mass or
a linear deficit in the uniform mean face rank.  Thus the upper-side escape
lands on the same mean-rank gate as the lower-side ACP attack.

The scalar theorem by itself does **not** cover genuinely heterogeneous
child blocks whose forward endpoint products are anti-aligned.  Sections
6--9 give the exact coloured recurrence and extend the barrier to every
heterogeneous jump having a scale-covering induced core with controlled skew.
Under a global low-count cap, joint size/skew bucketing forces such a core
automatically.  At every genuinely macroscopic effective split, what remains
is a hereditary count/mean problem for the induced macro on that adversarial
core.

All logarithms are base two.  Counts below are for nonempty faces.

## 1. The macro partition polynomial

For an `r`-point macro set `S`, write

\[
 P_S(x)=\sum_{j\ge2}v_j(S)x^{j-2},\qquad
 V_2(S)=\sum_{j\ge2}v_j(S),                         \tag{1}
\]

and let

\[
 \mu_2(S)=\frac{\sum_{j\ge2}jv_j(S)}{V_2(S)},
 \qquad h(S)=\max\{j:v_j(S)>0\}.                    \tag{2}
\]

The exact homogeneous vertical-composition formula is

\[
 W(S[Q])=rW(Q)+C(Q)U(Q)P_S(n),\qquad n=|Q|.         \tag{3}
\]

Every nonempty convex face has a unique upper cap and lower cup.  The map
from a face to this ordered pair is injective, because their union recovers
the face.  Therefore

\[
 \boxed{C(Q)U(Q)\ge W(Q).}                          \tag{4}
\]

The polynomial in (1) has two exact lower bounds.

> **Lemma 1 (mean and maximal-degree domination).**  For every integer
> `x>=1`,
> \[
> \boxed{
> P_S(x)\ge V_2(S)x^{\mu_2(S)-2},}                  \tag{5}
> \]
> and
> \[
> \boxed{
> P_S(x)\ge
> \frac{(1+x)^{h(S)}-1-h(S)x}{x^2}.}                \tag{6}
> \]

**Proof.**  Under the uniform law on the rank-at-least-two faces, Jensen's
inequality applied to the convex function `k -> x^(k-2)` gives (5).
For an entirely integer formulation, if

\[
 M_2=\sum_{j\ge2}jv_j(S),
\]

then (5) is equivalent to

\[
 P_S(x)^{V_2}\ge V_2^{V_2}x^{M_2-2V_2}.             \tag{7}
\]

For (6), choose a largest convex face `H`.  Every subset of `H` is convex,
so coefficientwise `v_j(S)>=binom(h,j)`.  Summing its Boolean subcube from
rank two upward proves (6).  QED.

Combining (3)--(5) gives the central exact transfer.

> **Theorem 2 (one-jump mean transfer).**
> \[
> \boxed{
> W(S[Q])\ge
> W(Q)V_2(S)n^{\mu_2(S)-2}.}                        \tag{8}
> \]

Thus a low-mean partition polynomial is not a free source of savings.  Its
total coefficient mass `V_2` is still present at activity one, and changing
the activity from one to `n` adds at least the tangent slope `mu_2 log n`.
At high activity the independent Boolean bound (6) also retains the
maximal-degree contribution.  The actual positive polynomial is bounded
below by the larger of these two mechanisms.

## 2. An exact deficit identity for arbitrary jump sizes

Let `Q_0` be a singleton and take an arbitrary depth-dependent homogeneous
vertical tower

\[
 Q_i=S_i[Q_{i-1}],\qquad r_i=|S_i|,
 \quad \ell_i=\log r_i,
 \quad L_i=\sum_{t\le i}\ell_t=\log|Q_i|.            \tag{9}
\]

The macro order types `S_i` may all be new, growing, and indecomposable.
Put

\[
 A_i=\log V_2(S_i),\qquad m_i=\mu_2(S_i).
\]

Iterating (8) gives the exact logarithmic lower bound

\[
 \boxed{
 \log W(Q_d)\ge
 \sum_{i=1}^d A_i+
 \sum_{i=1}^d(m_i-2)L_{i-1}.}                       \tag{10}
\]

Since

\[
 \frac12L_d^2
 =\sum_i\frac12\ell_i^2+
   \sum_i\ell_iL_{i-1},                             \tag{11}
\]

(10) is equivalently

\[
\boxed{
 \frac12L_d^2-log W(Q_d)
 \le
 \sum_i\left(\frac12\ell_i^2-A_i\right)
 +\sum_i(\ell_i-m_i+2)L_{i-1}.}                     \tag{12}
\]

Negative summands are genuine surplus and need not be truncated.  Formula
(12) is the tropical accounting rule for macroscopic jumps.  It separates
three possible losses:

1. a macro already has fewer than `2^(ell_i^2/2)` faces;
2. its mean face rank is below `ell_i`;
3. the two endpoint blocks cost the lower-order term `2L_(i-1)`.

There is no additional “finite-activity” loss.

## 3. Macroscopic-jump barrier

The endpoint loss in (12) is negligible for genuinely macroscopic jumps.
For example, suppose for some fixed `epsilon>0` that every nontrivial level
satisfies

\[
 \ell_i\ge\epsilon L_i.                              \tag{13}
\]

Then the prefix sizes grow geometrically and

\[
 \sum_iL_{i-1}=O_\epsilon(L_d).                      \tag{14}
\]

> **Corollary 3 (heterogeneous-macro, homogeneous-child barrier).**  Under
> (13), suppose uniformly along the tower that
> \[
> A_i\ge(1/2-o(1))\ell_i^2,qquad
> m_i\ge(1-o(1))\ell_i,                              \tag{15}
> \]
> where the errors are uniform as `ell_i -> infinity`; bounded initial
> levels are harmless.  Then
> \[
> \boxed{
> \log W(Q_d)\ge(1/2-o(1))L_d^2.}                   \tag{16}
> \]

**Proof.**  Condition (13) makes the `ell_i` and `L_i` geometrically
increasing, so the sums of the uniform errors in (15) are `o(L_d^2)`.
Equation (14) makes the endpoint loss in (12) only `O_epsilon(L_d)`.
Substitution in (12) proves (16).  QED.

The same conclusion holds without (13) whenever the right side of (12) is
`o(L_d^2)`.  Fine-mesh towers require the sharper cap--cup accumulation
theorem already proved in `agent_growing_state_upper`; (12) is designed for
the complementary macroscopic-jump regime where its endpoint loss is small.

The contrapositive is the useful design constraint:

> A homogeneous vertical tower below coefficient `1/2` cannot obtain the
> saving from composition alone.  At positive logarithmic scale it must use
> macros with a quadratic count deficit, a linear mean-rank deficit, or both.

In particular, a finite child activity (`log n=O(1)`) cannot exploit low
mean at quadratic scale: the activity tilt is only `O(mu_2)`, while the
macro's own `A_i` term remains.  When `log n=Theta(log r)`, a low mean can
matter quadratically, but precisely through
`(log r-mu_2)log n` in (12).  Proving the planar mean estimate

\[
 \mu_2(S)\ge\log|S|-o(\log|S|)                      \tag{17}
\]

for the relevant low-count macros would therefore close this upper escape.
This is the same mean-size phenomenon isolated by the ACP/RNP lower attack.

## 4. What remains outside the scalar theorem

For genuinely heterogeneous blocks `Q_1,...,Q_r`, the exact cross term is

\[
 \sum_{B\text{ convex macro}}
 C(Q_{\min B})U(Q_{\max B})
 \prod_{i\in B\setminus\{\min B,\max B\}}|Q_i|.    \tag{18}

The diagonal injection `C(Q)U(Q)>=W(Q)` no longer controls the forward
products `C(Q_i)U(Q_j)`.  Cup-heavy children can be placed before cap-heavy
children, and exact examples show exponential anti-alignment.  Thus (18)
requires the coloured analysis below; the scalar result alone must not be
cited as a barrier to that class.  Nonvertical mixed-triple rules remain
outside every theorem in this note.

## 5. Exact and tropical audit

Run

```bash
python3 phase2/loop/erdos838/agent_upper_jump/macro_jump_audit.py
```

The audit reads the exact stretchable macros in
`agent_growing_state_upper/LARGE_MACRO_CERTIFICATE.json`.  For every saved
size and activities `1,2,r,r^2`, it checks the integer Jensen form (7), the
Boolean max-degree bound (6), `CU>=W`, and the exact composition formula.
It also reports the macro mean ratio, the two competing partition lower
bounds, and the resulting one-jump normalized coefficients.  All theorem
checks use integers; floating point is used only for displayed logarithms.

## 6. Exact heterogeneous support calculus

The anti-aligned case admits a useful exact refinement.  Let `S` have
ordered positions `1,...,r`, and replace position `i` by an arbitrary block
`Q_i` of size `n_i`.  Write `C_i,U_i,W_i` for its three nonempty-subset
counts.  Define the multivariate endpoint-support polynomials

\[
 \begin{aligned}
 A_i(\mathbf n)&=
  \sum_{\substack{B\text{ a nonempty macro cap}\\\min B=i}}
       \prod_{j\in B\setminus\{i\}}n_j,\\
 B_j(\mathbf n)&=
  \sum_{\substack{B\text{ a nonempty macro cup}\\\max B=j}}
       \prod_{i\in B\setminus\{j\}}n_i,\\
 P_{ij}(\mathbf n)&=
  \sum_{\substack{B\text{ macro-convex},\ |B|\ge2\\
                    \min B=i,\ \max B=j}}
       \prod_{q\in B\setminus\{i,j\}}n_q .       \tag{19}
 \end{aligned}
\]

The endpoint-block classification gives the exact identities

\[
 \boxed{
 \begin{aligned}
 C(S[Q_1,\ldots,Q_r])&=\sum_i C_iA_i(\mathbf n),\\
 U(S[Q_1,\ldots,Q_r])&=\sum_j U_jB_j(\mathbf n),\\
 W(S[Q_1,\ldots,Q_r])&=\sum_iW_i+
               \sum_{i<j}C_iU_jP_{ij}(\mathbf n).
 \end{aligned}}                                   \tag{20}
\]

This is the correct object for a heterogeneous variational search.  In the
equal-size, typed case, colour the macro positions by `tau(i)` and put

\[
 \begin{aligned}
 A_a(x)&=\sum_{B\text{ cap},\ \tau(\min B)=a}x^{|B|-1},\\
 B_b(x)&=\sum_{B\text{ cup},\ \tau(\max B)=b}x^{|B|-1},\\
 P_{ab}(x)&=\sum_{\substack{B\text{ convex},\ |B|\ge2\\
                 \tau(\min B)=a,\tau(\max B)=b}}x^{|B|-2}.
                                                               \tag{21}
 \end{aligned}
\]

If every position of type `a` receives the same `Q_a`, and `m_a` is its
multiplicity, then

\[
 \boxed{
 C=\sum_a C_aA_a(n),\quad U=\sum_bU_bB_b(n),\quad
 W=\sum_am_aW_a+\sum_{a,b}C_aU_bP_{ab}(n).}       \tag{22}
\]

Consequently (22) is also an exact max-plus recurrence at quadratic scale.
If `L=log(rn)`, the logarithm of each displayed sum differs from the largest
summand by at most `log(r^2+r)=O(L)`, even if every block has its own type.
Thus, with zero terms omitted,

\[
 {\log W\over L^2}=
 \max\left\{
 {\log(m_aW_a)\over L^2},
 {\log C_a+\log U_b+\log P_{ab}(n)\over L^2}
 \right\}+o(1),                                  \tag{23}
\]

and there are analogous formulae for `C,U`.  Equation (23), rather than a
single scalar partition polynomial, is the promised heterogeneous
variational recurrence.

For two mirror types, take `A` cup-heavy and put it on the left, and take
`B` cap-heavy on the right.  The `A -> B` term can indeed have two small
endpoint factors.  But the diagonal terms use
`C_AU_A>=W_A` and `C_BU_B>=W_B`.  A sub-half fixed point must therefore make
both `P_AA` and `P_BB` quadratically small at the child activity while
putting its large macro-support mass into the anti-aligned `P_AB` class.
Endpoint anti-alignment alone is not a construction.

## 7. A broad heterogeneous barrier: common-skew cores

There is a stronger way to measure anti-alignment than requiring each child
to be two-sided.  Define the directional skew of block `i` by

\[
 \sigma_i={1\over2}\log{U_i\over C_i}.             \tag{24a}
\]

Since `C_iU_i>=W_i`, for every ordered pair `i<j`,

\[
 \begin{aligned}
 \log(C_iU_j)
 &=\tfrac12\log(C_iU_i)+\tfrac12\log(C_jU_j)
      +\sigma_j-\sigma_i\\
 &\ge\tfrac12(\log W_i+\log W_j)+\sigma_j-\sigma_i.
                                                               \tag{24b}
 \end{aligned}
\]

Thus absolute one-sidedness is harmless on a set of blocks having almost
the same skew.  Only *variation* of skew across the ordered endpoints can
create a quadratic saving.

> **Theorem 4a (common-skew induced core).**  Let `I` be any set of at least
> two macro positions, and put
> \[
> W_*=\min_{i\in I}W_i,\quad n_I=\min_{i\in I}n_i,
> \quad D_I=\max_{i\in I}\sigma_i-\min_{i\in I}\sigma_i.     \tag{24c}
> \]
> Then
> \[
> \boxed{
> W(S[Q_1,\ldots,Q_r])\ge
> W_*2^{-D_I}P_{S[I]}(n_I).}                      \tag{24d}
> \]

**Proof.**  Equation (24b) gives
`C_iU_j>=W_*2^(-D_I)` for every ordered endpoint pair in `I`.  Restrict (20)
to macro supports contained in `I`, bound every internal size below by
`n_I`, and sum.  QED.

This core is forced under the low-total-count hypothesis relevant to an
upper construction, even when child sizes are wildly dispersed.  Put
`N=sum_i n_i` and `L=log N`, and form the dyadic size classes

\[
 J_t=\{i:2^t\le n_i<2^{t+1}\},\qquad 0\le t\le\lfloor L\rfloor.
\]

Since

\[
 N<2(L+1)\max_t |J_t|2^t,                         \tag{24e}
\]

some `J_t` satisfies `log|J_t|+t=L-O(log L)`.  Moreover
`C_i,U_i<=W_i<=W`, so if `log W<=M L^2`, every `sigma_i` lies in an interval
of length at most `M L^2`.  Choose any `epsilon_L -> 0` with
`log(1/epsilon_L)=o(L)` and partition the skews in this `J_t` into
`O(M/epsilon_L)` windows of width `epsilon_L L^2`.  One window contains a
set `I` such that

\[
 \boxed{
 \log|I|+t=L-o(L),\quad
 2^t\le n_i<2^{t+1}\ (i\in I),\quad D_I=o(L^2).}   \tag{24f}
\]

Thus arbitrary size dispersion, child-type growth, and cap/cup
anti-alignment always leave a scale-covering comparable common-skew core.
If both `log|I|` and `t` are `Theta(L)`, this is a genuinely macroscopic
effective split and the fixed-point gain below is strict.  If one is
`o(L)`, the level is effectively a one-scale/fine-mesh step rather than the
macroscopic-jump escape studied here.  To defeat (24d) at a genuine jump,
the construction must make the *induced macro on this adversarial core* fail
the needed count/mean property, or already pay a large local `W`.

For comparison, a simpler pointwise form is sometimes convenient and needs
no skew bucketing.

> **Theorem 4b (balanced induced core).**  In the heterogeneous vertical
> composition above, let `I` be any set of at least two macro positions and
> put
> \[
> b_I=\min_{i\in I}\min(C_i,U_i),\qquad
> n_I=\min_{i\in I}n_i.                            \tag{24}
> \]
> If `S[I]` is the induced macro configuration, then
> \[
> \boxed{
> W(S[Q_1,\ldots,Q_r])\ge b_I^2P_{S[I]}(n_I).}    \tag{25}
> \]
> Hence, writing `V_2,mu_2,h` for the parameters of `S[I]`,
> \[
> \boxed{
> W\ge b_I^2\max\left\{
> V_2n_I^{\mu_2-2},
> { (1+n_I)^h-1-hn_I\over n_I^2}
> \right\}.}                                      \tag{26}
> \]

**Proof.**  Restrict (20) to supports lying in `I`.  Each endpoint product
is at least `b_I^2`, and every internal block size is at least `n_I`.
Summing gives (25).  Apply Lemma 1 to `S[I]` for (26).  QED.

This can be stated directly in terms of the price of endpoint imbalance.
Put `W_*=min_(i in I)W_i` and

\[
 \Delta_I=\max\left\{0,
 \max_{i\in I}\left({1\over2}\log W_*-\log C_i\right),
 \max_{i\in I}\left({1\over2}\log W_*-\log U_i\right)
 \right\}.                                       \tag{27}
\]

Then `b_I^2>=W_*2^(-2Delta_I)`, so

\[
 \boxed{W\ge W_*2^{-2\Delta_I}
              V_2(S[I])n_I^{\mu_2(S[I])-2}.}      \tag{28}
\]

> **Corollary 5 (heterogeneous macroscopic-jump barrier).**  Consider a
> sequence of heterogeneous jumps with total log-size `L`.  Suppose each has
> an induced core `I`, with `ell=log|I|` and `t=log n_I`, such that
> \[
> \ell+t=L-o(L),\quad
> \log W_*\ge\tfrac12t^2-o(L^2),\quad
> \log V_2(S[I])\ge\tfrac12\ell^2-o(L^2),         \tag{29}
> \]
> \[
> \mu_2(S[I])\ge\ell-o(L),                         \tag{30}
> \]
> and suppose either `Delta_I=o(L^2)` or, more generally,
> `D_I=o(L^2)`.  Then
> \[
> \boxed{\log W\ge(1/2-o(1))L^2.}                \tag{31}
> \]

Indeed, (28), or the stronger (24d), gives

\[
 \log W\ge\tfrac12t^2+\tfrac12\ell^2+ell t-o(L^2)
 =\tfrac12(\ell+t)^2-o(L^2).                      \tag{32}
\]

More generally, replace both `1/2` assumptions in (29) by the same
coefficient `c`.  If `ell/L -> alpha`, `t/L -> beta`, with
`alpha+beta=1`, then exactly the same calculation gives the fixed-point
inequality

\[
 \boxed{c_{\rm out}\ge
 c(\alpha^2+\beta^2)+\alpha\beta
 =c+(1-2c)\alpha\beta.}                           \tag{32a}
\]

For every `c<1/2` and genuinely macroscopic split `alpha beta>0`, the output
coefficient is strictly larger than `c`.  Hence no sub-half coefficient can
be a closed fixed point of comparable, high-mean, two-sided heterogeneous
jumps.  A putative sub-half tower must pay a quadratic skew/count/mean loss
at every macroscopic regeneration step; it cannot merely recycle components
having its target coefficient.

The common-skew theorem removes “two-sided” from that last conclusion.  To
make the reduction explicit, let `F(N)` be the minimum possible `W` over all
`N`-point planar configurations and put

\[
 c_*:=\liminf_{N\to\infty}{\log F(N)\over(\log N)^2}.          \tag{32b}
\]

Every child in the dyadic core then has
`log W_i >= (c_*-o(1))t^2`, and the induced macro has
`log V_2(S[I]) >= (c_*-o(1))ell^2`; these follow directly from the
definition of `F` and require no structural theorem (subtracting the
singletons is negligible because the known lower bounds give `c_*>0`).
Therefore:

> **Corollary 6 (conditional closure of all heterogeneous vertical
> macroscopic jumps).**  Suppose a sequence of low-`W` heterogeneous
> vertical compositions has automatic cores (24f) with
> `ell/L -> alpha`, `t/L -> beta`, where `alpha,beta>0`.  If
> \[
> \mu_2(S[I])\ge\ell-o(L),                         \tag{32c}
> \]
> then the sequence cannot attain the global coefficient `c_*<1/2`.

Indeed (24d), Lemma 1, and the two universal `F` bounds give (32a) with
`c=c_*`; its right side exceeds `c_*` by the fixed amount
`(1-2c_*)alpha beta`.  Thus a global mean-rank theorem of the form (32c)
would close **every** genuinely macroscopic heterogeneous vertical escape,
not merely finite-state or homogeneous ones.  The only nonautomatic input
is the mean of the adversarial induced macro core.

There is also a quantitative converse which identifies the exact mean
deficit a counterconstruction would need.  If such a composition attains

\[
 \log W\le(c_*+o(1))L^2
\]

with a genuine automatic core, (24d) and Jensen force

\[
 \boxed{\mu_2(S[I])\le(2c_*+o(1))\ell.}           \tag{32d}
\]

To see this, insert the universal child and induced-macro lower bounds into
(24d):

\[
 c_*L^2\ge c_*t^2+c_*\ell^2+(\mu_2-2)t-o(L^2).
\]

Since `L=ell+t+o(L)` and `t=Theta(L)`, division by `t` gives (32d).  More
generally a hereditary mean lower bound `mu_2 >= (kappa-o(1))ell` changes
the fixed-point inequality to

\[
 c_{\rm out}\ge c+(\kappa-2c)\alpha\beta.         \tag{32e}
\]

Thus it already proves the vertical lower coefficient `c>=kappa/2`.
For a hypothetical `c=1/3` construction, the adversarial induced macros
must have uniform mean rank at most `(2/3+o(1))log|I|`; reaching the full
half is exactly the endpoint `kappa=1`.

This covers arbitrary growing type complexity and, by (24e)--(24f), arbitrary
child-size dispersion at every genuine macroscopic effective split.  Endpoint
anti-alignment is no longer an independent escape under a global low-`W`
cap.  On the automatic scale-covering common-skew core, a heterogeneous
sub-half tower must instead have a quadratic induced-macro count deficit or
a linear induced-macro mean deficit.  These are hereditary versions of the
same ACP mean gate exposed by the homogeneous argument.

The `Delta_I` condition is not cosmetic.  The injection `CU>=W` controls the
sum of the two endpoint logarithms, whereas anti-alignment exploits their
difference.  The theorem says that an `Omega(L^2)` directional skew is
necessary to get an `Omega(L^2)` saving from that difference.

## 8. Exact adversarial stress tests

Run

```bash
python3 phase2/loop/erdos838/agent_upper_jump/heterogeneous_jump_audit.py
```

It writes `heterogeneous_certificate.json`.  Besides the three geometric
stress tests below, it checks the dyadic scale-cover inequality (24e) and the
fixed-point identity (32a) over exact rational scale splits.

### 8.1 One-sided guard blocks make the theorem sharp, but are fatal locally

An all-cup `n`-block has

\[
 C=D(n):=n+{n\choose2},\qquad U=W=E(n):=2^n-1,    \tag{33}
\]

and an all-cap block has the reflected triple.  Put the all-cup block first
and the all-cap block second.  The two-block spanning term is exactly

\[
 C_{\rm cup}U_{\rm cap}=D(n)^2.                   \tag{34}
\]

For the two-position core, `b_I=D(n)` and `P_S(n)=1`, so (25) is attained
with equality on the spanning term.  Thus the endpoint-deficiency loss in
(28) cannot be improved in general.  The two positions have opposite skew,
so this example has no two-position common-skew core and does not make
(24d) sharp.  But the parent already contains the two local families of
size `E(n)`, and

\[
 W_{\rm parent}=2E(n)+D(n)^2.                     \tag{35}
\]

Since its total size is `2n`, this is vastly above the desired
`2^{O((log n)^2)}` scale.  This exactly diagnoses the guard construction:
it is a sharp anti-alignment witness, not a low-convex-set construction.

### 8.2 A stretchable 16-block low-count macro does not align its supports

The verifier exhaustively enumerates every subset of the saved stretchable
16-point macro from `LARGE_MACRO_CERTIFICATE.json`, for all 15 contiguous
two-colour cuts.  It recovers the saved uncoloured cap, cup, and convex
profiles coefficientwise.  With 16-point all-cup blocks on the left and
all-cap blocks on the right, the best cut is after position 10.  Its exact
activity-16 support values are

\[
 P_{AA}=274093,\quad P_{AB}=8585852,\quad
 P_{BB}=6991.                                     \tag{36}
\]

Although most raw support weight is cross-coloured, the large endpoint
factor on the diagonal classes makes them dominate: the deliberately
anti-aligned contribution is only `5.961%` of the exact spanning count.
The resulting exact normalized coefficient is

\[
 {\log_2W\over(\log_2 256)^2}=0.644949257\ldots.  \tag{37}
\]

This is only a finite stress test, not a universal theorem, but it falsifies
the most direct “split a low-count macro and mirror the children” candidate.

### 8.3 Canonical Baek--Balko cells evade balance but not total mass

For the canonical Pascal cell `T_(d,i)`, the exact recurrences give

\[
 \log C=(A(\theta)+o(1))d^2,\quad
 \log U=(A(1-\theta)+o(1))d^2,
\]

\[
 \log W=(A(\theta)+A(1-\theta)+o(1))d^2.          \tag{38}
\]

Therefore its endpoint deficiency is

\[
 \Delta=\left(\tfrac12|A(\theta)-A(1-\theta)|+o(1)\right)d^2, \tag{39}
\]

which is genuinely quadratic away from the central cell.  The
balanced-core theorem correctly does **not** rule out a Baek--Balko schedule
by itself.

However, the exact macro-support formula contains the layer-transversal
family from `BAEK_BLOWUP_COUNT.md`.  Singleton endpoints make this family
independent of cap/cup anti-alignment.  Its limiting coefficient `T(theta)`
and the convex subsets internal to a score-two canonical cell, with
coefficient `I(theta)`, satisfy

\[
 \max\{T(\theta),I(\theta)\}\ge
 0.5049925589\ldots>\tfrac12                      \tag{40}
\]

for `0<=theta<1/2` (with the documented canonical endpoint repair at
`theta=1/2`).  The verifier independently checks the exact transversal
products and Pascal recurrences at `k=40,80`.  Thus the canonical
Baek--Balko construction uses the only remaining quadratic-skew loophole,
but its macro-support/local-mass alternative still keeps it above one half.

## 9. Updated verdict

No realizable heterogeneous tower below coefficient `1/2` was found.  The
new exact conclusion is stronger than the homogeneous barrier:

* under a low-total-`W` cap, arbitrary heterogeneous children have a
  near-full-log common-skew core; they are blocked whenever that induced
  macro has the half-count/high-mean profile and comparable child sizes
  cover the total scale;
* one-sided guards show the quadratic endpoint-deficiency term is real and
  sharp for the pointwise balance theorem, but their local convex mass is
  exponentially too large;
* canonical Baek--Balko cells have the requisite quadratic endpoint skew,
  yet an endpoint-independent transversal or one large microcell restores a
  coefficient strictly above `1/2`.

Accordingly, within the logarithmically comparable macroscopic-jump regime,
cap/cup anti-alignment is no longer the essential escape.  The remaining
vertical task is to build a macro for which an adversarial near-full-size
induced subset has a quadratic convex-count deficit or a linear mean-rank
deficit.  That is precisely a hereditary form of the ACP/RNP mean gate.
Joint bucketing shows that wildly dispersed child scales do not evade this
at a genuine macroscopic effective split; nonvertical mixed-triple rules do
remain separate.  Formulae (19)--(23) are the exact optimization interface
for a future search, while (24d)--(24f) reduce its endpoint-state dimension
to the induced-macro gate.
