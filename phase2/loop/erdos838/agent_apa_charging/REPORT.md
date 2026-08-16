# Arbitrary-point charging after the constant-two counterexample

**Date:** 2026-08-14  
**Verdict:** the uniform averaged inequality, the existential one-point
version, the deepest-onion version, and the finite bound `H(P)<=2` are all
false for exact planar configurations.  No proof of unrestricted Erdős 838
is claimed.  The surviving form is a variable-envelope deletion inequality;
an `n^o(1)` envelope would still close the problem.

Throughout, put

\[
 W=Z_P(1/2),\qquad V=Z_P(1),\qquad
 W_e=\sum_{A\ni e}2^{-|A|},\qquad
 V_e=|\{A:e\in A,\ A\text{ convex}\}|.
\]

## 1. The subset-sum charging form

For a restriction `X subseteq P`, let `V(X)` be its number of convex faces
and let `M(X)` be the sum of their sizes.  Double-counting pairs `(A,X)`
with `A subseteq X` gives

\[
 2^n Z_P(1/2)=\sum_{X\subseteq P}V(X),\qquad
 2^n\frac12 Z'_P(1/2)=\sum_{X\subseteq P}M(X).
\]

Consequently the proposed averaged arbitrary-point inequality

\[
 nZ(1/2)+\frac{n-1}{2}Z'(1/2)\le 2Z'(1)
\]

is exactly

\[
 n\sum_XV(X)+(n-1)\sum_XM(X)\le 2^{n+1}M(P).       \tag{1}
\]

This makes the intended injection transparent: low-rank faces in all
restrictions were to be charged to marked global convex faces.  The exact
44-point certificate in `../agent_apa_rank` disproves (1), so no such
two-copy charging can exist.

## 2. The stronger exact obstruction

The exact 58-point configuration in
`../agent_apa_rank/verify_half_weight_counterexample.py` has

\[
 (v_0,\ldots,v_{10})=
 (1,58,1653,30856,220958,428915,284982,76995,15100,2179,210)
\]

and

\[
 Z(1)=1061907,\qquad Z(1/2)=\frac{1172209}{32},
\]

so

\[
 H(P)=\frac{58Z(1/2)}{Z(1)}
 =\frac{33994061}{16990512}=2.0007673106\ldots>2.       \tag{2}
\]

Every one-point deletion has `H<2`, and every individual constant-two
deletion margin

\[
 2V_e-W-(n-1)W_e                                      \tag{3}
\]

is negative.  Thus (2) simultaneously kills:

* the finite half-weight conjecture `H<=2`;
* existential arbitrary-point rooted amortization;
* uniform averaging of the rooted margins; and
* the proposed deepest-onion rescue.

For the last point, the onion layers have sizes

```text
4,4,4,4,4,4,4,6,6,6,7,4,1
```

and the unique deepest point has margin `-1695735/512` in (3).

## 3. Exact generalized thresholds on the obstruction

For a constant `C`, define

\[
 \Phi_C(P)=C Z_P(1)-|P|Z_P(1/2).
\]

The deletion increment is exactly

\[
 \Phi_C(P)-\Phi_C(P-e)=CV_e-W-(n-1)W_e.              \tag{4}
\]

Hence the least constant for which **some** point works is

\[
 C_{\rm ex}(P)=\min_e\frac{W+(n-1)W_e}{V_e}.          \tag{5}
\]

On the exact 58-point set,

\[
 C_{\rm ex}(P)=\frac{223780817}{111243264}
 =2.01163476289225\ldots,                              \tag{6}
\]

attained at input label 37.  The uniform `V_e`-weighted average threshold is

\[
 C_{\rm av}(P)=
 \frac{nW+(n-1)(1/2)Z'(1/2)}{Z'(1)}
 =\frac{5935970545}{2824041984}
 =2.10194132333409\ldots.                              \tag{7}
\]

Thus merely replacing 2 by a slightly larger number repairs this finite
example, but there is presently no evidence that one universal constant
repairs every size.

## 4. Surviving variable-envelope induction

The useful remnant is the following exact lemma.

> **Envelope lemma.**  Let `C_n` be nondecreasing.  Suppose that for every
> `n`-point planar set `P` there is a point `e` such that
> \[
> C_nV_e\ge W+(n-1)W_e.                                \tag{8}
> \]
> Then `H(P)<=C_n` for every `n`-point `P`.

Indeed, (8) and (4) give
`Phi_(C_n)(P)>=Phi_(C_n)(P-e)`.  Induction gives
`Phi_(C_(n-1))(P-e)>=0`; monotonicity of the envelope gives
`Phi_(C_n)(P-e)>=0`, and hence `Phi_(C_n)(P)>=0`.

Uniform averaging supplies the point in (8) if

\[
 \boxed{
 nZ(1/2)+\frac{n-1}{2}Z'(1/2)\le C_n Z'(1).}          \tag{9}
\]

Therefore either of the following would still close Erdős 838:

\[
 \sup_{|P|=n}C_{\rm ex}(P)=n^{o(1)},                  \tag{10}
\]

or the stronger averaged estimate (9) with `C_n=n^o(1)`.  A fixed constant
would be more than enough, but (2) shows that the constant cannot be 2.

This is the right way to retain the half-weight strategy: the exact constant
has failed, while the asymptotic `n^o(1)` target needed for coefficient
one-half remains untouched.

## 5. Computation and reproduction

`search_existential_ra.cpp` anneals reduced words for the minimum individual
constant-two RA ratio.  It independently replays every wire deletion.  A
word obtained after arbitrary braid moves is only an allowable-sequence
certificate and still needs a stretchability proof; the embedded 58-point
coordinates provide that proof for the counterexample above.

Run the exact generalized-threshold audit from the repository root:

```bash
python3 phase2/loop/erdos838/agent_apa_charging/verify_generalized_deletion.py
```

The audit reconstructs every deletion profile from the rational coordinates
and verifies (2), (6), (7), and the unique-deepest failure.

## 6. Recommended next attack

Do not attempt another scalar constant-two deletion potential.  The viable
quantitative target is (9) with a slowly growing envelope.  A proof should
separate the first-switch-controlled nonmaximal boundary from maximal faces
and allow a `2^o(log n)=n^o(1)` tangent-pocket multiplicity.  This matches the
actual asymptotic requirement and avoids spending effort on a finite
strengthening that is now exactly false.

## 7. A sharper local-peak compensation target

There is a second surviving route which is weaker than a fixed generalized
deletion constant.  Put

\[
 \delta(P)=\mu_1(P)-\mu_{1/2}(P).
\]

The exact omitted-point recursion implies that the local-peak estimate

\[
 \boxed{H(P)[1-\delta(P)]_+\le K}                    \tag{11}
\]

with an absolute constant `K` would prove `H(P)=O(log n)`, and hence solve
Erdős 838.  A polylogarithmic `K` would still suffice.

Here is the complete argument.  Let `R_n=max H(P)` over `n`-point planar
sets and choose a maximizer `P`.  The exact deletion identity gives

\[
 R_{n-1}\ge
 \frac{n-1}{n}\frac{n-\mu_{1/2}}{n-\mu_1}R_n.
\]

Therefore

\[
 R_n-R_{n-1}
 \le R_n\frac{n(1-\delta)-\mu_{1/2}}
 {n(n-\mu_1)}
 \le \frac{R_n[1-\delta]_+}{n-\mu_1}.                \tag{12}
\]

For every downset, deleting a marked element injects faces containing it
into faces avoiding it.  Hence each uniform inclusion probability is at
most `1/2`, so `mu_1<=n/2`.  Equations (11)--(12) yield

\[
 R_n-R_{n-1}\le\frac{2K}{n},
\]

and summation gives `R_n=O(K log n)`.

This target lands exactly on the known geometric gate.  If `b(A)` is the
number of blocked additions, the cover identity gives

\[
 \mu_t=\frac{t}{1+t}\bigl(n-\mathbb E_t b\bigr).
\]

Consequently

\[
 1-\delta
 =\frac{6-n+3\mathbb E_1b-2\mathbb E_{1/2}b}{6}.  \tag{13}
\]

Thus the only positive-growth regime is a precise compensation between the
uniform and half-weighted blocked boundaries.  The first-switch theorem
controls `sum b(A)u(A)` for nonmaximal faces, but maximal faces have `u=0`
and disappear from that transport.  Proving (11) is therefore a
block-smoothed maximal-pocket inequality, not a consequence of the existing
rank-one switch alone.

The link identity gives another exact form.  With
`L(A)=Z_(link A)(1/2)` and expectation under the half-weight face law,

\[
 \mathbb E_{1/2}L=\frac nH,\qquad
 \delta=2\frac{\mathbb E_{1/2}(|A|L)}{\mathbb E_{1/2}L}
          -\mathbb E_{1/2}|A|.                         \tag{14}
\]

Hence (11) asks for a lower bound on the average half-weight link precisely
when link size is strongly anticorrelated with face size.  Static edge
pockets cannot prove this because their factorization is false; the dynamic
two-tangent state remains necessary.

### Exact evidence for (11)

Every reflection-order commutation class through seven points satisfies
(11) with `K=1`.  The exact maxima of its left side are

| `n` | maximum |
|---:|---:|
| 2 | `3/4` |
| 3 | `81/128` |
| 4 | `26/45` |
| 5 | `85/162` |
| 6 | `331/600` |
| 7 | `47705/85264` |

The certified adversarial profiles give values

```text
n=20: 0.732930223952
n=24: 0.793631196094
n=30: 0.715625337663
n=44: 0.742419035809
n=58: 0.681952500614
```

In particular, the exact counterexamples to `APA`, existential RA, and
`H<=2` do not threaten local-peak compensation.  Fixed and nonstationary
central-Pascal vertical compositions have either `delta>=1` or exponentially
small `H`, so their compensation is zero or tiny.  This is evidence only;
generic complete-three-skeleton downsets violate (11) by an unbounded
factor, so planar pocket geometry is essential.

Run `verify_local_compensation.py` for the exact census and saved-profile
checks.  `search_local_compensation.cpp` performs a braid anneal for further
kill-search; as usual its post-braid words require a separate stretchability
certificate.

## 8. Exact KL domination by the uniform mean deficit

There is a clean relation between (11) and the mean-size conjecture which
does not use geometry.  Let `q_1(r)=v_r/Z(1)` and
`q_h(r)=2^{-r}v_r/Z(h)` be the two rank laws, and put

\[
 m=-\log_2\frac{Z(h)}{Z(1)}=\log_2\frac nH.
\]

The two relative entropies, measured in bits, are exactly

\[
 D_2(q_1\Vert q_h)=\mu_1-m,\qquad
 D_2(q_h\Vert q_1)=m-\mu_h.                         \tag{15}
\]

In particular both terms are nonnegative and their sum is `delta`.  If
`0<=delta<=1`, then

\[
\begin{aligned}
 H(1-\delta)
 &=2^{\log_2n-\mu_1}\,2^{\mu_1-m}(1-\delta)\\
 &\le 2^{\log_2n-\mu_1}\,2^\delta(1-\delta)
 \le 2^{\log_2n-\mu_1}.                              \tag{16}
\end{aligned}
\]

The last scalar inequality follows because `2^x(1-x)` decreases on
`[0,1]`.  Thus, for every downset,

\[
 \boxed{H[1-(\mu_1-\mu_h)]_+
 \le 2^{\log_2n-\mu_1}.}                            \tag{17}
\]

This answers the relation to the mean-size route exactly:

* `mu_1>=log_2 n-C` implies local compensation with `K=2^C`;
* `mu_1>=log_2 n-O(log log n)` implies polylogarithmic compensation and
  still closes Erdős 838;
* it is enough to prove either estimate only at positive-growth maximizers
  of `H`.

Indeed, if `P` is a strict size-`n` peak, comparison with every deletion
gives, pointwise in `e`,

\[
 n\Pr_1(e\in A)\le1+(n-1)\Pr_h(e\in A).
\]

Summing yields `delta<=1-mu_h/n<1`.  This is precisely the branch on which
(17) is active.  The mean-size conjecture is therefore not merely adjacent
to (11): its deficit pointwise dominates the local-peak obstruction.

## 9. A rank-summed first-switch localization

The first-switch theorem can be summed without losing a polynomial factor
provided one stops trying to move faces with only `O(r)` extensions.  Write

\[
 B_r^{\le\Lambda}=\sum_{\substack{|A|=r\\
 u(A)\le\Lambda(r+1)}}b(A),\qquad
 B_r^{>\Lambda}=B_r-B_r^{\le\Lambda}.
\]

For `r>=3`, the switch upper bound and the definition of the high-extension
part give

\[
 \Lambda(r+1)B_r^{>\Lambda}
 \le\sum_{|A|=r}b(A)u(A)
 \le(r+1)B_{r+1}.
\]

Consequently, for every `t>0` and `Lambda*t>1`,

\[
 \boxed{
 \sum_rt^rB_r
 \le {\Lambda t\over\Lambda t-1}
 \sum_rt^rB_r^{\le\Lambda}.}                       \tag{18}
\]

At the two activities needed here, the common choice `Lambda=4` gives

\[
 \sum_r2^{-r}B_r\le2\sum_r2^{-r}B_r^{\le4},\qquad
 \sum_rB_r\le\frac43\sum_rB_r^{\le4}.              \tag{19}
\]

Thus the entire integrated boundary is, up to constants, supported on
faces having at most `4(r+1)` addable points.  This is a genuine
block-smoothed maximal-pocket reduction: the uncontrolled class is not just
`u=0`, but it has only `O(r)` possible outer continuations.  At the critical
ranks `r=Theta(log n)`, remembering an arbitrary subset of these
continuations would still cost `2^{Theta(r)}=n^{Theta(1)}`.  The remaining
tangent-stack lemma must compress that history to `2^{o(r)}`; (18) shows
that no other boundary class needs a restart.

Summing both sides of the first-switch theorem also yields a useful exact
second-moment form.  The rank-three boundary must be retained separately,
because the at-most-three-repairs theorem begins at nonfaces of size five.
Put

\[
 \beta_{3,t}=\mathbb E_t[b\,1_{R=3}]={t^3B_3\over Z(t)}.
\]

Then, under the activity-`t` face law,

\[
 {1\over t}\{\mathbb E_t[b(R-2)]-\beta_{3,t}\}
 \le\mathbb E_t[bu]
 \le {1\over t}\{\mathbb E_t[bR]-3\beta_{3,t}\}.  \tag{20}
\]

Using `E_t(tu)=E_tR=mu_t` and double-counting marked covers,
`E_t(Ru)=t^{-1}E_t[R(R-1)]`, (20) is equivalent to

\[
\boxed{
 \mathbb E_tR^2-(1-t)\mu_t+3t\beta_{3,t}
 \le\mathbb E_t(tu)^2
 \le\mathbb E_tR^2-(1-t)\mu_t
        +2t\mathbb E_tb+t\beta_{3,t}.}              \tag{21}
\]

At activity one this says

\[
 \mathbb E_1R^2+3\beta_{3,1}\le\mathbb E_1u^2
 \le\mathbb E_1R^2+2\mathbb E_1b+\beta_{3,1}.      \tag{22}
\]

So the planar switch balances not only average up- and down-degree, but
their second moments.  This is still insufficient by itself: the complete
three-skeleton truncation stores the necessary up-degree second moment in a
tiny number of ranks below its maximal triples and obeys the same coarse
inequalities.  The near-maximal pocket reset in (18), not another scalar
moment manipulation, is the missing planar input.

## 10. What the planar antimatroid identities can prove

For the closure lattice, the Boolean-interval partition gives

\[
 (1+t)^n=\sum_{K\text{ closed}}t^{|\operatorname{ext}K|}
                  (1+t)^{|K|-|\operatorname{ext}K|}.           \tag{23}
\]

Together with cover double-counting, (23) proves
`E_1 u=E_1 R=mu_1`; the planar first-switch improves this to (21).  None of
these scalar identities bounds `mu_1` from below: rank-truncated abstract
downsets satisfy the cover and first-switch moment constraints while having
bounded mean.  The interval identity changes measure toward hulls with many
interior points, but supplies no bounded change-of-measure back to the
uniform closed-set law.

The viable mean theorem is therefore the following restricted form:

> **Peak mean target.**  Every planar positive-growth maximizer of `H` has
> `mu_1>=log_2 n-O(log log n)`.

By (17) this alone completes the local-peak induction.  Equations
(18)--(19) reduce it further to a history-preserving restart for
`u(A)=O(|A|)` faces.  The known tangent localization says all such failed
continuations live in a three-pocket, two-orientation stack.  What remains
unproved is the rank-gain/Hall statement that converts the capacity inside
those pockets into the uniform average down-degree without polynomial
history congestion.

Run `verify_rank_summed.py` for exact checks of (15)--(22) on the saved
profiles and exact small planar face tables.

## 11. A block-smoothed near-maximal inequality sufficient for ACP

The preceding localization suggests a particularly concrete theorem.  Put
`ell=ceil(log_2 n)` and

\[
 N_r=|\{A\in F_r:u(A)\le4(r+1)\}|.
\]

Consider the weighted near-maximal mass

\[
 \mathcal N(P)=\sum_{r<\ell}(\ell-r)N_r.             \tag{24}
\]

> **Near-maximal mean lemma.**  If
> \[
>  \mathcal N(P)\le C_n Z_P(1),                     \tag{NPM}
> \]
> then
> \[
>  \mu_1(P)\ge\log_2n-2C_n-\frac12.                \tag{25}
> \]

**Proof.**  Let `H_r=v_r-N_r` count the remaining, high-extension faces.
Cover double-counting gives

\[
 \sum_{A\in F_r}u(A)=(r+1)v_{r+1},
\]

so `H_r<=v_(r+1)/4`.  Define the total rank deficit below `ell` by

\[
 D=\sum_{r<\ell}(\ell-r)v_r.
\]

The high-extension contribution is at most

\[
 {1\over4}\sum_{s=1}^{\ell}(\ell-s+1)v_s
 \le {D\over2}+{v_\ell\over4},
\]

because `sum_(s<ell)v_s<=D`.  Hence

\[
 D\le\mathcal N(P)+{D\over2}+{v_\ell\over4},
 \qquad
 D\le2\mathcal N(P)+{v_\ell\over2}.                \tag{26}
\]

The ranks above `ell` only increase the mean, and therefore

\[
 \ell-\mu_1
 \le {D\over Z(1)}
 \le2C_n+\frac12.
\]

Since `ell>=log_2n`, (25) follows.  QED.

Combining (17) and (25) gives the explicit implication

\[
 \boxed{H[1-\delta]_+\le2^{,2C_n+1/2}.}             \tag{27}
\]

Thus `(NPM)` with bounded `C_n` proves constant ACP, while
`C_n=O(log log n)` proves polylogarithmic ACP and closes Erdős 838.  This is
the cleanest block-smoothed maximal-pocket target produced by the charging
attack.  It has three advantages:

1. it is an unweighted count under the uniform face law, so it directly
   controls the average down-degree;
2. the ordinary cover map disposes of every face with more than `4(r+1)`
   continuations, with no planarity assumption;
3. all geometric work is confined to the deficit-weighted family having
   only `O(r)` outer continuations.

The complete-three-skeleton barrier fails `(NPM)` by a factor
`Theta(log n)`: almost all of its faces are maximal triples and each carries
deficit `ell-3`.  A planar proof must show that the pockets behind a large
population of such low-rank near-maximal faces create enough distinct
higher-rank faces to keep (24) at `O(V log log n)`.  The tangent localization
and tagged pocket decoder prove this for the known one-pocket exponential
fibre, but the simultaneous overlapping-pocket Hall inequality remains
open.

There is a more injection-friendly rankwise statement which is already
enough.  Write `g=ell-r`.  Suppose that for some `K_n>=2`,

\[
 \boxed{N_{\ell-g}\le K_n2^{-g}V\quad(g\ge1).}        \tag{RNP}
\]

Since also `sum_g N_(ell-g)<=V`, splitting at
`G=2 ceil(log_2(2K_n))` gives

\[
 {\mathcal N(P)\over V}
 =\sum_{g\ge1}g{N_{\ell-g}\over V}
 \le G+K_n\sum_{g>G}g2^{-g}
 =O(\log K_n).                                      \tag{28}
\]

Therefore `(RNP)` with `K_n=(log n)^O(1)` proves `(NPM)` with
`C_n=O(log log n)` and closes the problem.  This is exactly the normalization
for a weighted Hall theorem: a rank-`r` near-maximal source must generate

\[
 2^{\ell-r}=\Theta(n/2^r)
\]

target-face units, with only polynomial-in-`r` congestion.  A polynomial
loss in the tangent state is harmless here: it becomes an additive
`O(log r)=O(log log n)` loss in the mean, rather than a multiplicative
polylogarithmic loss in (24).

For a proposed interior-versus-tangent proof of `(RNP)`, a source `A` has
at most `4(r+1)` addable points and hence `n-O(r)` blocked points.  Split the
blocked set into

* points in `int(conv A)`, which require an onion/interior restart; and
* exterior points, whose two supporting tangents cut out a consecutive
  visible chain and hence a two-orientation ear replacement.

The required number `n/2^r` is deliberately modest.  Locally, either half
of the blocked points already supplies that many labels, and a tangent class
with fixed endpoints supplies a canonical replacement pocket.  The hard
part is global: an interior point can lie in many cages, and visible
intervals from different sources can cross.  The target face must retain the
source identity through an onion or tangent stack.  The repair
classification shows that every exterior step is a singleton/ear
replacement and has at most three one-step inverse repairs; what remains is
to prove that after recursively keeping the larger retained/discarded arc,
the endpoint stack is recoverable with `r^O(1)` total ambiguity.  Such a
statement would prove `(RNP)` with `K_n=r^O(1)`.

One exact random-restriction identity is useful for testing a proposed Hall
map.  If `M(X)` is the number of maximal faces of a restriction `X`, then

\[
 \boxed{
 \mathbb E_{X\sim\operatorname{Ber}(\alpha)}M(X)
 =\sum_{A\in\mathcal F(P)}
   \alpha^{|A|}(1-\alpha)^{u(A)}.}                  \tag{29}
\]

Indeed, `A` is maximal in `X` exactly when all its points are retained and
all its addable points are omitted; blocked points are arbitrary.  The
trivial upper bound `M(X)<=V(X)` yields

\[
 \sum_A\alpha^{|A|}(1-\alpha)^{u(A)}\le Z_P(\alpha). \tag{30}
\]

This disposes of very low ranks but cannot prove `(RNP)`: on
`u<=4(r+1)` its optimized loss is still exponential in `r`.  Geometry has
to replace the factor `(1-alpha)^u` by a polynomial tangent/onion tag.  Thus
(29) is a precise regression test for the desired history compression, not
the compression itself.

## 12. A hereditary restriction identity at record peaks

There is one further exact all-subset consequence worth recording.  Suppose
`P` is a record maximizer, so every nonempty restriction `X subseteq P`
satisfies `H(X)<=R=H(P)`.  Summing

\[
 RZ_X(1)\ge |X|Z_X(1/2)
\]

with weight `s^|X|`, and putting `alpha=s/(1+s)`, gives

\[
 \boxed{
 RZ_P(\alpha)\ge
 \alpha n Z_P(\alpha/2)
 +(1-\alpha){\alpha\over2}Z'_P(\alpha/2)
 \quad(0\le\alpha\le1).}                            \tag{31}
\]

Indeed, a fixed face of rank `r` is contained in supersets of weighted total
`s^r(1+s)^(n-r)`, while their weighted size sum introduces the factor
`r+(n-r)alpha`.  At `alpha=1`, (28) is equality.  Its left derivative at
one recovers `delta<=1-mu_h/n`; at smaller activities it records every
restriction size simultaneously.  Dropping the derivative term and
iterating yields

\[
 Z_P(1)\ge(n/R)^k2^{-k(k-1)/2}Z_P(2^{-k}),           \tag{32}
\]

which is the expected quadratic face-count growth conditional on `R`.
This does not by itself bound `R`, but it is a useful exact interface for a
future multiscale pocket proof: any restart theorem can be averaged at the
activity `alpha` where its pocket scale is visible, rather than paid at
activity one in a single step.
