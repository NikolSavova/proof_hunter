# Activity compensation: exact reductions and sharp structural barriers

**Date:** 2026-08-14  
**Verdict:** ACP is not proved or disproved for planar point sets.  There is,
however, a clean theorem-level reduction which identifies its real content:
the compensated peak is bounded above by the ordinary uniform-face mean
deficit.  Thus an additive (or merely logarithmic-logarithmic) uniform mean
theorem closes the problem.  A second exact identity turns the half-activity
mean into a weighted average of uniform means of restrictions.

The report also proves one multi-frame case of the final rooted-pocket Hall
gate: arbitrarily many frames may reuse the *same* ordinary pocket, provided
their boundary completions expose distinct root signatures.  For ears of
size at most `I` and `K` such frames, the congestion is
`2^{O(I+sqrt(log K))}`.  It is therefore subexponential at the exact hard
scales `I=o(r)` and `log K=o(r^2)`.  Thus literal repeated use of one pocket
is not the remaining obstruction; any counterexample must obtain its reuse
from a crossing family of genuinely different pockets (or erase the root
signature in the boundary completion).

A second capped Hall branch is also proved below.  Any selected incidence
subgraph with `2^{o(r^2)}` sources has `2^{o(r)}` congestion, regardless of
its geometry or codegrees.  In particular, a fixed retained boundary with
hidden rank `I=o(r)` is harmless, as is a `2^{o(r)}` cover by such boundary
cells.  Only quadratic source entropy dispersed over exponentially many
retained boundaries still needs the genuinely two-ended product expansion.

The final short-word recovery proposal has also been audited and does not
close that branch.  Its high/medium row inequality is correct under an
injective `b`-coordinate encoding, but `b=sqrt(r)` can encode only
`2^{O(r^(3/2))}` children, whereas the hard reuse class has quadratic
entropy.  The product grid realizes quadratically many retained child cores
with the same short batch word.  Encoding those cores forces `b=Theta(r)`
and a quadratic decoder fibre.  Moreover, the exact vertical-composition
classification shows that a comparable suffix cannot be retained after a
two-ended cup.  Thus the entropy-sensitive all-interval recovery gate
remains genuinely open.

There is, however, a new exact entry theorem for that gate.  Boundary-word
entropy supplies `S(S^{1/r}-r)` successor alternatives from any rank-`r`
source family of size `S`.  Angular ordering loses only the absolute factor
`e` while making every selected alternative exterior and outward.  On the
low-addable hard slice this produces
`S(n^{c/alpha-o(1)})` distinct repair records/nonfaces, exactly the RNP
factor because `c/alpha>=1-alpha`.  Each repaired hull canonically retains
the whole witness prefix and blocker; only one consecutive suffix interval
is forgotten.  The repair split also conserves entropy per rank exactly.
What remains is the mixed case where retained-target entropy and hidden-ear
entropy are both substantial: the product grid proves that these two terms
must be cross-multiplied by a two-ended target, while a one-component
entropy recursion loses a full coordinate factor.

The report also rules out two tempting shortcuts.  Gordon's entire planar
expected-rank polynomial, even together with `V`, does not determine ACP.
The Boolean hull-partition identity and ordinary shellability/Cohen--Macaulay
constraints permit ACP of order `n`; the missing input is genuinely the
rank-three oriented-matroid geometry.

Throughout,

\[
 Z(t)=\sum_kv_kt^k,\qquad
 \mu_t={tZ'(t)\over Z(t)},\qquad
 H={nZ(1/2)\over Z(1)},\qquad
 \Delta=\mu_1-\mu_{1/2}.
\]

## 1. ACP is a one-sided derivative

Set

\[
 F(t)=nt{Z(t/2)\over Z(t)}.
\]

Differentiating with respect to `log t` gives the exact identity

\[
 {dF\over d\log t}
 =F(t)\bigl(1+\mu_{t/2}-\mu_t\bigr).                 \tag{1}
\]

In particular,

\[
 \left.{dF\over d\log t}\right|_{t=1}
 =H(1-\Delta),                                       \tag{2}
\]

so ACP is precisely an upper bound on the positive endpoint slope of this
two-scale quotient.

Under the uniform law on convex faces, with `K=|A|`, (2) is also

\[
 H(1-\Delta)
 =n\,\mathbb E_1\bigl[(K+1-\mu_1)2^{-K}\bigr].       \tag{3}
\]

This exposes the required cancellation: the positive half-weight mass below
the uniform mean must be paid for by faces above the mean.

## 2. A universal mean-deficit upper bound for ACP

The following lemma uses no geometry.

> **Lemma 1 (mean-deficit domination).**  For every polynomial with
> nonnegative coefficients,
> \[
> \boxed{
> H[1-\Delta]_+\le n2^{-\mu_1}.}                     \tag{4}
> \]

**Proof.**  The function `mu_t` is nondecreasing in `log t`, since

\[
 {d\mu_t\over d\log t}=\operatorname{Var}_t(K)\ge0.
\]

Consequently

\[
 \log_2{Z(1)\over Z(1/2)}
 =\int_{1/2}^1\mu_t\,d\log_2t\ge\mu_{1/2},
\]

and hence

\[
 H\le n2^{-\mu_{1/2}}=n2^{-\mu_1+\Delta}.           \tag{5}
\]

If `Delta>=1`, the left side of (4) is zero.  For `0<=Delta<=1`,
`2^Delta(1-Delta)<=1` (its derivative is negative already at zero), so
multiplying (5) by `1-Delta` proves (4).  QED.

There is an equivalent information-theoretic factorization which is often
more useful.  Let `q_1,q_h` be the two rank laws and put
`D_1=D(q_1||q_h)`.  Directly from exponential tilting,

\[
 D_1=\log(H/n)+(\log2)\mu_1,
\]

and the Jeffreys divergence is

\[
 D(q_1||q_h)+D(q_h||q_1)=(\log2)\Delta.
\]

Hence

\[
 H(1-\Delta)
 =n2^{-\mu_1}e^{D_1}(1-\Delta)
 \le n2^{-\mu_1}2^\Delta(1-\Delta),                 \tag{5a}
\]

which is Lemma 1.  Thus the only possible large compensated peak is a
uniform face law whose mean lies substantially below `log_2 n`; closeness of
the two tilted laws itself costs no additional factor.

This yields the cleanest sufficient target found in this lane.

> **Corollary 2 (low-variance mean criterion).**  It is enough to prove
> \[
> \Delta(P)<1\quad\Longrightarrow\quad
> \mu_1(P)\ge\log_2n-O(\log\log n).                  \tag{6}
> \]
> Then ACP has a polylogarithmic envelope, hence the deletion argument gives
> `H(P)=n^o(1)` and closes Erdős 838.  An `O(1)` error in (6) proves ACP with
> an absolute constant.

The point of (6) is that no mean estimate is required in the high-variance
branch: there `Delta>=1` already kills the positive local peak.  In the hard
branch, the two exponential-family rank laws are close and the uniform rank
must be shown to sit at `log_2 n-O(log log n)`.

This is stronger information than the mere existence of a large convex
subset.  A sharply concentrated rank distribution below `log n` is exactly
the abstract three-skeleton obstruction in Section 6.

## 3. Half activity is an exact average over restrictions

For `X subseteq P`, let

\[
 V(X)=Z_X(1),\qquad M(X)=Z'_X(1),\qquad
 \mu_1(X)=M(X)/V(X).
\]

Double counting pairs `(A,X)` with `A` a convex face and `A subseteq X`
gives

\[
 2^{-n}\sum_{X\subseteq P}V(X)=Z_P(1/2),\qquad
 2^{-n}\sum_{X\subseteq P}M(X)={1\over2}Z'_P(1/2). \tag{7}
\]

Therefore

\[
 \boxed{
 \mu_{1/2}(P)=
 {\sum_XV(X)\mu_1(X)\over\sum_XV(X)}.}             \tag{8}
\]

There is a useful probabilistic description.  Under the law

\[
 \nu(X)={V(X)\over\sum_YV(Y)},
\]

first sample `A` from the half-activity face law, then take

\[
 X=A\cup Y,
\]

where every point of `P-A` is put in `Y` independently with probability
`1/2`.  This produces exactly `nu`.

> **Corollary 3 (restriction mean criterion).**  Suppose every planar
> `m`-point restriction `Q` satisfies
> \[
> \mu_1(Q)\ge\log_2m-c\log_2\log_2(m+2)-C.           \tag{9}
> \]
> Then
> \[
> \mu_{1/2}(P)\ge
> \log_2n-c\log_2\log_2(n+2)-O_C(1),                \tag{10}
> \]
> and consequently
> \[
> H(P)\le O_C((\log n)^c).                            \tag{11}
> \]

**Proof.**  Conditional on any `A`, Hoeffding gives

\[
 \Pr(|X|<n/4\mid A)\le e^{-n/8}.                    \tag{12}
\]

(If `|A|>=n/4` this is zero; otherwise the deviation of
`Bin(n-|A|,1/2)` below `n/4-|A|` is at least `n/4`.)  Apply (9) inside
(8), discard the exponentially small bad event, and use monotonicity of the
right side of (9).  Finally,

\[
 \log_2{Z(1)\over Z(1/2)}\ge\mu_{1/2}
\]

as in Lemma 1.  QED.

Thus an all-restrictions mean theorem with an `O(log log n)` deficit proves
the half-weight target directly, without first passing through deletion.
This is the most economical positive route produced here.

## 4. The hull-partition identity in this language

Let `C` be a closed set of the affine convex geometry and write

\[
 h(C)=|\operatorname{ext}C|,\qquad i(C)=|C|-h(C),
\]

and

\[
 B(u,v)=\sum_Cu^{h(C)}v^{i(C)}.
\]

The Boolean intervals `[ext(C),C]` partition `2^P`, so

\[
 B(x,1+x)=(1+x)^n.                                  \tag{13}
\]

Our quantities are off this universal curve:

\[
 Z(t)=B(t,1),\qquad
 \mu_t={tB_u(t,1)\over B(t,1)}.                     \tag{14}
\]

In particular ACP is

\[
 {nB(1/2,1)\over B(1,1)}
 \left[1-{B_u(1,1)\over B(1,1)}
       +{B_u(1/2,1)\over2B(1/2,1)}\right]_+.        \tag{15}

Equation (13) controls `B` only on `v=1+u`, whereas (15) uses `v=1` at two
different `u` values.  The gap is substantive, not algebraic bookkeeping;
Section 6 gives a family satisfying (13) with ACP of order `n`.

## 5. Gordon's planar expected-rank polynomial does not determine ACP

The exact two rational eight-point configurations in
`../agent_planar_tutte/expected_rank_collision_certificate.json` have the
same Gordon polynomial

\[
 \operatorname{er}(p)=
 4p+3p^2+4p^3+p^4-p^5-4p^6-3p^7+4p^8
\]

and the same `V=133`, but profiles

\[
 (1,8,28,56,33,6,1),\qquad
 (1,8,28,56,33,7,0).
\]

Their ACP values are different, exactly

\[
 {47583\over141512}=0.336247\ldots,qquad
 {185\over532}=0.347744\ldots.                      \tag{16}
\]

Thus even all of Gordon's cyclic expected-rank data together with the total
number of faces loses information needed for ACP.  The cyclic minimal-stem
formula can still be useful locally, but it must be retained before the
one-variable aggregation.

## 6. Sharp abstract and commutative-algebra barrier

The simple Caratheodory-three convex geometry from
`../agent_root_followup/ABSTRACT_LATTICE_BARRIER.md` has free-set profile

\[
 v_k=\binom nk\quad(0\le k\le3),\qquad v_k=0\quad(k>3).       \tag{17}
\]

It is worth noting that its free complex is the complete two-dimensional
skeleton of the `(n-1)`-simplex.  In particular it is pure, shellable, and
Cohen--Macaulay, much stronger than the local topological conclusions one
might try to extract from the general free-set-complex theory.  It is also a
simple convex geometry of Caratheodory number three, and its bivariate
closed-set polynomial satisfies the exact hull identity (13).

Nevertheless

\[
 H[1-\Delta]_+={n\over8}+O(1).                       \tag{18}
\]

Indeed

\[
\begin{aligned}
 V&={n^3+5n+6\over6},\\
 Z(1/2)&={n^3+3n^2+20n+48\over48},\\
 \mu_1&={3n^3-3n^2+6n\over n^3+5n+6},\\
 \mu_{1/2}&={3n^3+3n^2+18n\over n^3+3n^2+20n+48}.
\end{aligned}                                       \tag{19}
\]

So `Delta=3/n+O(1/n^2)` and (18) follows.

This proves that none of the following can imply ACP by itself:

* the convex-geometry axioms and hull partition;
* simplicity plus Caratheodory number three;
* completeness of the three-skeleton of the free complex; or
* shellability, Cohen--Macaulayness, and the usual resulting `f`-vector
  constraints.

This also locates the limit of the Edelman--Reiner--Welker free-complex
theory (*Discrete Comput. Geom.* 27 (2002), 99--116).  Their global and
local homotopy results are important structural information, but topology
alone is quantitatively weaker than what is already satisfied by the
uniform-matroid skeleton (17).  In particular, importing those results via
ordinary Stanley--Reisner `h`-vector nonnegativity cannot yield (20).

The family is nonplanar for `n>=5` because it has no free four-set, while
every five points in planar general position contain a convex quadrilateral.
Any proof of (6) must use the rank-three oriented-matroid circuit-elimination
and cyclic tangent-pocket structure, not only topology of the free complex.

## 7. Scalable planar counterexample search

Three natural amplification mechanisms were checked and do **not** produce
an ACP counterexample.

1. Exact homogeneous vertical iterates of central Pascal templates: ACP
   decays to zero (or the positive part eventually vanishes) for the small
   templates, and also decays for all larger templates tested.
2. Repeated radial nesting of two or three copies of the exact `n=20,24,30`
   hard records: mixed convex faces increase `Delta` to about one before `H`
   can amplify.  At two layers the largest tested ACP was below `0.25`; at
   three layers it was zero in the positive-part convention.
3. A million-step allowable-sequence anneal from the `n=30` hard record
   reached `0.79955` but not one.  A separate `n=58` run starting at the
   exact `H>2` counterexample also remained below one.

These are only negative computational evidence.  They do explain why the
obvious "nearly disjoint nested copies" construction fails: the cross-layer
faces broaden the uniform rank law, and this extra tilt gap is exactly what
ACP records.

## 8. Recommended attack

The most focused remaining target is no longer the full scalar ACP formula.
Prove the following planar low-variance mean dichotomy:

\[
 \boxed{
 \mu_1(P)\le\log_2n-C\log_2\log n
 \quad\Longrightarrow\quad
 \mu_1(P)-\mu_{1/2}(P)\ge1.}                         \tag{20}
\]

By Lemma 1, any fixed `C` already yields a polylogarithmic ACP envelope.
The exact tangent-pocket theorem suggests how (20) might be attacked.  A
small tilt gap means the rank law is narrow.  Near its mode the average
extension count is only `Theta(r)`; if the extension mass is dispersed,
the nonadjacent-pocket theorem forces rank curvature and broadens the law.
Thus a counterexample to (20) must have most second-moment extension mass in
three adjacent pockets through a whole `Theta(log n)` rank window.  The
remaining task is a two-tangent stack theorem showing that such persistent
concentration itself creates enough ranks/faces to put the mean at
`log n-O(log log n)`.

This formulation uses exactly the planar input absent from (17), and it is
stable under the finite `H>2` counterexample.

### The hard branch has bounded rank width

The hypothesis `Delta<1` has a useful consequence stronger than an
integrated-variance slogan.  Put

\[
 m=\mu_1,\qquad m_0=\log_2{Z(1)\over Z(1/2)}.
\]

Since `m-m_0=D_2(q_1||q_h)<1`, the uniform rank `K` satisfies

\[
 \mathbb E_1 2^{m-K}=2^{m-m_0}<2.                 \tag{21}
\]

Consequently, for every real `s>=0`,

\[
 \Pr_1(K\le m-s)<2^{1-s}.                         \tag{22}
\]

Integrating the tail and using
`E(K-m)_+=E(m-K)_+` gives

\[
 \mathbb E_1(m-K)_+\le1+{1\over\ln2},\qquad
 \boxed{\mathbb E_1|K-m|\le2+{2\over\ln2}<4.886.} \tag{23}
\]

Thus a counterexample to the peak-mean gate is forced to look almost like
a rank-truncated complex: a constant fraction of all its faces lies in a
fixed-width window about a rank `m` well below `log_2 n`.

There is a precise connection to the near-maximal-face target of the
arbitrary-point charging lane.  The cover identity gives
`E_1 u=E_1K=m`.  If `m>=40`, (23), Markov's inequality, and a union bound
show that more than `0.27` of all faces satisfy

\[
 |K-m|\le20,\qquad u\le4(K+1).                     \tag{24}
\]

A slightly different cutoff will be useful below: more than `0.25` of all
faces satisfy `|K-m|<=20` and `u<=2m`.  Indeed the two exceptional
probabilities are at most `(2+2/ln 2)/20` and `1/2`, respectively.

Hence at least one of the at most 42 integer ranks in this window has

\[
 N_r\ge c_0Z(1)                                    \tag{25}
\]

for an absolute `c_0>0`.  If `ell=ceil(log_2 n)` and `d=ell-m`, that rank
also has `ell-r>=d-20`.  Therefore the proposed rankwise Hall estimate

\[
 N_{\ell-g}\le K_n2^{-g}Z(1)                       \tag{26}
\]

would force

\[
 2^d\le O(K_n).                                    \tag{27}

In particular a planar Hall map with `K_n=(log n)^O(1)` proves exactly the
requested conclusion `d=O(log log n)`.  Conversely, any falsification must
produce a planar family with a constant fraction of all convex faces
near-maximal at ranks `log_2 n-omega(log log n)`.

The direct map from a blocked pair `(A,p)` to `ext(A union {p})` has superb
one-step geometry (a singleton or one consecutive ear, with at most three
repairs), but its inverse fibre is the full convex-subset problem inside a
retained two-tangent pocket.  Thus the unresolved statement really is the
polynomial-congestion version of (26); neither scalar moments nor the
Boolean hull identity control that recursive fibre.

**Current verdict.**  The gate (20) is neither proved nor falsified.  The
new theorem (21)--(23) and reduction (24)--(27) identify the exact required
weighted Hall statement: a rank-`r=Theta(log n)` near-maximal source must
generate `Theta(n/2^r)` target-face units with only `r^O(1)` inverse
congestion.

### A local QuickHull-capacity lemma

There is no local shortage of target faces.  The following elementary
statement handles both kinds of blocked point and is useful for auditing a
proposed Hall map.

> **Lemma 4 (half-face local capacity).**  Let `A` be a convex `r`-face and
> let `p` be blocked for `A`.
>
> * If `p` is interior to `conv(A)`, there is a set `J subset A` with
>   `|J|>=ceil(r/2)` such that `D union {p}` is convex for every `D subset J`.
> * If `p` is exterior and hides the consecutive interval `I subset A`,
>   then `D union {p}` is convex for every `D subset A-I`, while every
>   subset of `I` is convex.  Thus one of these two Boolean face pools has
>   dimension at least `r/2`.

For the interior assertion, take a line through `p`, avoiding `A`, and let
`J` be the larger of its two vertex sides.  Every `D subset J` is strictly
separated from `p`, so `p` is extreme in `D+p`.  Each member of `D` remains
extreme because its supporting line as a vertex of `conv(A)` has the
interior point `p` on the same strict inner side as all other vertices.
For the exterior assertion,

\[
 (A-I)\cup\{p\}=\operatorname{ext}(A\cup\{p\})
\]

is a convex face, and heredity gives all its subsets; the hidden interval
is a subset of `A`, so heredity also gives its whole Boolean cube.  QED.

In fact the interior pool has an exact circular description:

\[
 D\cup\{p\}\text{ is convex}
 \quad\Longleftrightarrow\quad
 p\notin\operatorname{conv}D
 \quad\Longleftrightarrow\quad
 D\text{ lies in an open half-plane through }p.    \tag{28}
\]

The first equivalence again uses the old supporting line at every vertex
of `D`; the second is strict separation.  Equivalently, the radial
directions of `D` lie in one open semicircle.  Thus the interior restart is
not an arbitrary set system: it is the union of cyclic Boolean intervals.
What remains nonlocal is that many different enclosing polygons can induce
the same semicircle targets.

When `r>=2log_2(n)/3+O(log log n)`, Lemma 4 already provides at least as
many local targets per blocked incidence as the rankwise Hall demand
`n/2^r`, up to polynomial factors.  At smaller ranks it still supplies an
exact `2^{r/2}` local pool, but this need not by itself meet that demand.
In either case the unaccounted difficulty is simultaneous overlap.  This is
also why a pointwise short endpoint code is the wrong target: the exact
common-ear/common-onion construction in `../agent_onion_hall/REPORT.md`
has exponentially many sources with identical endpoint and pocket data.
The selected face itself must carry the source code, and the codes must be
allocated globally across crossing pockets.

### The hull partition forces polynomially many exterior labels

The interior/onion branch cannot absorb almost all blocked labels on the
hard rank mass.  For a convex face `A`, write

\[
 i(A)=|P\cap\operatorname{int}(\operatorname{conv}A)|,
 \qquad e(A)=\#\{p\notin\operatorname{conv}A:A+p\text{ is nonconvex}\}.
\]

Then

\[
 n=|A|+i(A)+u(A)+e(A).                              \tag{29}
\]

> **Lemma 5 (exterior mass from hull entropy).**  Let `S` be any family of
> rank-`r` faces with `u(A)<=4(r+1)` for every `A in S`.  Then
> \[
>  {1\over|S|}\sum_{A\in S}e(A)
>  \ge\log_2|S|-5r-4.                              \tag{30}
> \]

**Proof.**  The Boolean hull intervals give

\[
 \sum_{A\in\mathcal F(P)}2^{i(A)}=2^n.
\]

Thus Jensen's inequality on the uniform law on `S` gives

\[
 \mathbb E_S i
 \le\log_2\mathbb E_S2^i
 \le n-\log_2|S|.
\]

Average (29) and use `u<=4(r+1)`.  QED.

Apply this to the hard family supplied by (24)--(25).  There
`|S|>=c_0Z(1)` and `r=mu_1+O(1)`; in a counterexample to the peak-mean gate
one also has `r<=log_2n+O(1)`.  The established unrestricted lower bound

\[
 \log_2Z(1)\ge(1/4-o(1))(\log_2n)^2
\]

therefore yields the stronger scale-correct estimate

\[
 \boxed{\mathbb E_Se(A)\ge(1/4-o(1))(\log_2n)^2,
        \quad\text{and hence }\mathbb E_Se(A)=\Omega(r^2).}    \tag{31}
\]

Using the `u<=2m` refinement after (24), the lower-order term in (30) can
in fact be improved from `-5r-O(1)` to `-3r-O(1)` on a possibly different
constant-density rank slice.

This is a genuine reduction of the Hall problem.  A rank-concentrated
counterexample cannot consist mainly of faces whose `n-O(r)` blocked points
all fall into deep common onion pockets: on average it has quadratically
many exterior ear-replacement labels per near-maximal source.  The remaining
unproved step is to convert these `Omega(r^2)` labels, together with the
Boolean capacity in Lemma 4, into distinct target units across crossing ear
pockets.  The endpoint-only decoder is still insufficient, but a future
Hall proof no longer has to obtain its first polynomial factor from the
interior branch.

## 9. Identical-pocket blocks satisfy the rooted Hall bound

The multi-frame gate in
`../agent_circuit_hardcore/ROOTED_OMISSION_AND_EIC.md` appears to allow the
same unrooted `V_Q` credit to be spent once for every repaired boundary.  For
an exact repeated pocket, however, the boundary-completed rooted faces and
the ordinary Erdős--Szekeres supply give a sharp dichotomy which removes
this apparent obstruction.

Here is a precise version.  Let `Q` be an `m`-point pocket and let
`F(Q)` be its convex-subset complex, of size `V_Q`.  Consider `K` rooted
frames `f`.  All frames have the same ground pocket `Q`, but have distinct
signatures `sigma_f` outside `Q` (for the two-root application,
`sigma_f={u_f,v_f}`).  For each `f`, let

\[
 r_{f,i}=\#\{C\subseteq Q:|C|=i,\
                   \sigma_f\cup C\text{ is convex}\}.        \tag{32}
\]

Assume that the boundary-completed target class contains every
`sigma_f union C` counted in (32).  Distinct signatures then give disjoint
target classes: intersecting either set with the complement of `Q` recovers
`sigma_f`.  These classes are also disjoint from `F(Q)`.

For `I>=0`, give every rooted `i`-history, `i<=I`, the coefficient-extraction
demand `m`.  Thus the total unbalanced demand and the visible target union
are

\[
 D_G=m\sum_{f=1}^K\sum_{i=0}^I r_{f,i},\qquad
 U_G\ge V_Q+\sum_{f=1}^K\sum_{i=0}^I r_{f,i}.       \tag{33}
\]

> **Theorem 6 (identical-pocket Hall theorem).**  Fix any absolute
> `c<1/4`.  For all sufficiently large `m`, put
> `kappa=log_2(max(K,1))`.  The universal planar convex-subset lower bound
> `V_Q>=2^{c(log_2m)^2}` implies
> \[
>  \boxed{
>  {D_G\over U_G}
>   \le 2^{T},\qquad
>  T={a+\sqrt{a^2+4c(\kappa+\log_2(I+1))}\over2c},
>  \quad a=I+1.}                                   \tag{34}
> \]
> In particular, if `I=o(r)` and `log_2K=o(r^2)`, then
> \[
>                  D_G\le2^{o(r)}U_G.              \tag{35}
> \]

**Proof.**  Write `S=sum_(f,i)r_(f,i)` and `y=log_2m`.  From (33),

\[
 {D_G\over U_G}\le\min\left(m,{mS\over V_Q}\right).          \tag{36}
\]

No rooted theorem is being assumed here.  The coefficient bound
`r_(f,i)<=binom(m,i)<=m^i` gives

\[
 S\le K(I+1)m^I.
\]

Consequently, with `b=kappa+log_2(I+1)`,

\[
 \log_2^+{D_G\over U_G}
 \le\min\{y,b+(I+1)y-cy^2\}.                      \tag{37}
\]

Let `T` be the positive zero of `b+ay-cy^2`.  If `y<=T`, the first
entry of the minimum is at most `T`; if `y>=T`, the second entry is
nonpositive.  This proves (34).  Since
`T=O_c(I+1+sqrt(log K+log(I+1)))`, (35) follows.  The finitely many smaller
values of `m` only alter the absolute factor.  QED.

The same proof is stronger for the half-weighted marked histories, since a
rank-`i` history then has the extra factor `2^{-i}`.  It also allows any
subquadratic-entropy number of exact copies, not merely the `O(n^2)` root
pairs available in a single point set.

There is a useful capped form, matching the fact that the RNP argument need
not route every exterior incidence.  In every frame choose an arbitrary
collection of marked pairs `(C,q)` with `|C|<=I` and `q in Q-C`.  Let `S_*`
be the number of distinct base histories `(f,C)` which occur.  There are at
most `d` selected marks above any base history when the selector is capped
at `d<=m` marks per frame, so the selected demand is at most `dS_*`.  If the
target system exposes the completed face
`sigma_f union C` for each occurring base history, then (33)--(37), with
`S_*` in place of `S`, sharpen to

\[
 {D_*\over U_*}
 \le\min\left\{d,{K(I+1)d,m^I\over V_Q}\right\}. 
                                                               \tag{37a}
\]

Put `delta=log_2d<=y`.  The logarithm of the second entry is at most
`kappa+log_2(I+1)+(I+1)y-cy^2`, exactly the expression in (37).  Thus
Theorem 6 holds for **every capped selection**, including a choice of only
the required `d=n/2^r` blockers per source (whenever the marked pocket is
the pool from which those blockers are selected).  No bound on all exterior
incidences is being assumed.

The theorem records exactly how the unrooted credit is reused.  If the
pocket is small, the raw loss `m` in (36) is already subexponential.  If it
is large, `V_Q` has quadratic logarithmic entropy and overwhelms both the
`m^I` possible short ears and all `2^{o(r^2)}` frame copies.  Hence the
literal common-pocket examples cannot violate `(RPH)`.  The unresolved
case must have many different pockets whose convex-face sets overlap
heavily, so that no single `V_Q` can be placed in the denominator of (36).
It must also defeat recovery of the outside signature from a completed
target.  This is a substantially narrower, genuinely crossing-pocket Hall
problem.

The argument is stable under a subexponential fringe, so even slightly
different pockets are harmless.

> **Corollary 7 (common-core Hall theorem).**  Let the pocket of frame `f`
> be `Q_f=Q union E_f`, where `|Q|=m`, `|E_f|<=J`, and all outside
> signatures remain exposed by boundary completion.  Put `M=m+J`.  If
> every selected history has rank at most `I` and the cap is `d<=M`, then
> its capped Hall
> congestion is at most
> \[
>  \min\left\{d,
>   {K(I+1)dM^I\over V_Q}\right\}.                  \tag{38}
> \]
> Consequently, at `I=o(r)`, `log_2K=o(r^2)`, and
> `log_2(J+1)=o(r)`, the congestion is `2^{o(r)}`.

**Proof.**  There are at most `K(I+1)M^I` occurring base histories and at
most `d` selected marks above each.  The target union contains both their distinct
boundary completions and every face of the common core `Q`, proving (38).
If `m<J`, then `M<2J`, so the first entry in (38) is `2^{o(r)}`.  If
`m>=J`, then `M<=2m`.  With `y=log_2m`, the logarithm of (38) is at most

\[
 \min\{y+1,\ \log_2K+\log_2(I+1)+(I+1)(y+1)-cy^2\},
\]

The same positive-root argument as (37) bounds this by
`O_c(I+1+sqrt(log K+log(I+1)))=o(r)`.  QED.

Thus a counterexample to capped `(RPH)` cannot consist of a
subquadratic-entropy collection of pockets obtained from one common pocket
by adding only `n^{o(1)}` labels.  Its reused capacity must come from a
family with large ground-set variation even after every such common core is
removed.  This is the precise remaining role for a frame-entropy or
crossing-pocket theorem.

One cannot finish by bounding the raw overlap multiplicity of different
pockets.  That multiplicity is exponentially too large even for a
singleton target.

> **Lemma 8 (quadratic crossing-pocket reuse).**  For every `N>=3` there is
> an `(N+1)`-point general-position set, a convex singleton face `{q}`, and
> `binom(N,2)` distinct two-root side pockets which all contain `{q}` as an
> ordinary target face.

**Proof.**  Take `q` and `N` further points in general position.  For every
pair `u,v` of the latter points, choose the open side of the line `uv` which
contains `q`, and let `Q_(uv)` be the points in that side.  Then
`q in Q_(uv)`, hence `{q} in F(Q_(uv))`.  The root pairs, and therefore the
pockets as rooted frames, are distinct.  QED.

At `N=2^r` the reuse is `2^{2r-O(1)}`, not `2^{o(r)}`.  This does not
contradict Theorem 6: these side pockets are genuinely different, and their
root-completed targets expose `binom(N,2)` different signatures.  Nor does
it refute capped `(RPH)`, since a selector may avoid charging the common
singleton.  It does rule out the proposed shortcut

\[
 \text{``sum the singleton-pocket inequalities and bound target overlap.''}
\]

The crossing theorem must use the selection freedom or transfer repeated
ordinary credit to the many distinct boundary completions; no pointwise
pocket multiplicity estimate can have the required scale.

## 10. Capped source-cloud entropy and boundary cells

The capped selection gives a general entropy discharge before any DRC or
geometric argument is needed.  Let `S` be any family of `s` distinct convex
source faces.  Let `Y` be the set of `t` blocker labels occurring on a
selected incidence from `S`.  The selected incidences may form an arbitrary
bipartite graph between `S` and `Y`.  If its maximum source degree is `d`,
then `d<=t` and its edge count `E` is at most `ds`.

> **Theorem 9 (capped source-cloud entropy).**  Fix `c<1/4`, put
> \[
>  b=\log_2s,\qquad
>  T={1+\sqrt{1+4cb}\over2c}.                       \tag{39}
> \]
> Apart from an absolute factor covering bounded `t`, every selected graph
> above satisfies
> \[
>                       \boxed{E\le2^T V(P).}       \tag{40}
> \]

**Proof.**  Both the `s` source faces and all convex subsets of `Y` are
global convex faces.  Hence `V(P)>=s`, while the universal planar lower
bound gives `V(P)>=V(Y)>=2^{c(log_2t)^2}` for sufficiently large `t`.
Writing `x=log_2t`,

\[
 {E\over V(P)}
 \le\min\left\{d,{ds\over V(Y)}\right\}
 \le2^{\min\{x,b+x-cx^2\}}.                       \tag{41}
\]

The number `T` is the positive zero of `b+x-cx^2`.  If `x<=T`, the first
entry of the minimum is at most `T`; if `x>=T`, the second is nonpositive.
This proves (40).  QED.

> **Corollary 10 (only quadratic source entropy can obstruct Hall).**  If
> `r=Theta(log n)` and `log_2s=o(r^2)`, then
> \[
>                             E\le2^{o(r)}V(P).     \tag{42}
> \]

This is stronger than a DRC conclusion: every subquadratic-entropy source
subfamily is harmless, independently of its codegrees, pocket overlap, or
blocker order type.  Thus every subfamily capable of violating the global
capped capacity bound must itself have `Omega(r^2)` source bits.

Here “Hall” is used in the global EIC sense: every ordinary convex face of
`P` is an admissible capacity unit.  If one insists on the narrower local
neighborhoods `T_f` from the provisional RPH formulation, the common target
pool `F(Y)` must be added to the neighborhood of this source-cloud cell.
That enlargement is legitimate for EIC, but Theorem 9 by itself does not
show that each face of `F(Y)` occurs inside one of the original discarded
pockets.

The common-boundary result follows immediately.  Fix a retained set `R`
and let the sources be `A_J=R union J`, where `J` is a hidden convex face of
size at most `I`.  Then, with `L=log_2n`,

\[
 s\le\sum_{i=0}^I\binom ni\le(I+1)n^I,
 \qquad \log_2s\le IL+\log_2(I+1).                 \tag{43}
\]

> **Corollary 11 (subexponential boundary cover).**  At
> `r=Theta(L)` and `I=o(r)`, every fixed-retained-boundary cell has capped
> congestion
> \[
>             2^{O(\sqrt{IL+\log(I+1)})}=2^{o(r)}. \tag{44}
> \]
> If the selected graph is covered by `M_r=2^{o(r)}` such cells, then its
> whole edge count is `2^{o(r)}V(P)`.

**Proof.**  Equation (43) and Theorem 9 give (44).  Sum over the `M_r`
cells; repeated use of global target capacity costs only the factor `M_r`.
QED.

There is a sharp quantitative converse at the established universal
coefficient.  Suppose `r=Theta(L)`, every source selects the full cap
`d=2^{L-r+O(1)}`, and all hidden ears have size at most `I=o(r)`.  If a
selected family satisfies

\[
                         d|S|>2^{o(r)}V(P),         \tag{45}
\]

then the universal lower bound
`log_2V(P)>=(1/4-o(1))L^2` gives

\[
 \log_2|S|\ge\log_2V(P)-\log_2d-o(r)
             \ge(1/4-o(1))L^2.                    \tag{46}
\]

One retained boundary supports at most `(I+1)n^I=2^{o(L^2)}` such sources
by (43).  Therefore the number `N_R` of distinct retained boundaries in any
counterexample to the global capped bound obeys

\[
                 \boxed{\log_2N_R\ge(1/4-o(1))L^2.} \tag{47}
\]

Thus the residual is not merely “many frames”: it has the full known
coefficient-`1/4` of retained-boundary entropy.  Any DRC/concentration step
which loses a fixed fraction of those quadratic bits cannot close the
problem; the dispersed branch really must convert boundary entropy into a
forward two-ended face pool.

The proof uses neither pairwise completeness nor the repair geometry once
the source family has been counted.  If the blocker cloud is small, the cap
pays directly; if it is large, its own Erdős--Szekeres entropy pays.  After
support-interval batching, a surviving graph must therefore have quadratic
source entropy spread across exponentially many retained boundaries.  The
exact product-grid example in `../agent_two_ended_hall/REPORT.md` has this
dispersed coordinate information; its forward cap--cup pool gives the other
known discharge.  The missing global theorem is a dichotomy between that
two-ended expansion and the entropy discharges above.

## 11. A two-ended retained-core entropy inequality

There is an exact Bollobás-type inequality for the final quadratic branch.
Let `E` be any finite selected family of exterior repair incidences with
rank-`r` sources.  For an edge `e=(A,p)`, write

\[
 I=A-\operatorname{ext}(A+p),\qquad
 R=A-I,\qquad B=R+p.                               \tag{48}
\]

Thus `A=R union I` and `B=R union {p}` are convex faces.  Give `E` the
uniform law and regard `R,I,p,A,B` as random variables.  Let `H_2` denote
base-two Shannon entropy.

> **Theorem 12 (retained-core entropy subtraction).**
> \[
> \boxed{
>  \log_2|E|+H_2(R)
>  \le2\log_2V(P)+3\log_2(r+1).}                   \tag{49}
> \]
> Equivalently,
> \[
> \boxed{
>  |E|\le(r+1)^{3/2}V(P)
>       2^{H_2(I,p\mid R)/2}.}                     \tag{50}
> \]

**Proof.**  Entropy submodularity for the variable sets `(R,I)` and
`(R,p)` gives

\[
 H_2(R,I,p)+H_2(R)\le H_2(R,I)+H_2(R,p).          \tag{51}
\]

The triple `(R,I,p)` identifies the repair edge, so its entropy is
`log_2|E|`.  Given the face `A=R union I`, the hidden set `I` is a cyclic
interval of `A`; there are fewer than `(r+1)^2` possibilities.  Therefore

\[
 H_2(R,I)\le H_2(A)+2\log_2(r+1)
             \le\log_2V(P)+2\log_2(r+1).          \tag{52}
\]

Given `B=R+p`, the marked vertex `p` has at most `r+1` possibilities, so

\[
 H_2(R,p)\le H_2(B)+\log_2(r+1)
             \le\log_2V(P)+\log_2(r+1).           \tag{53}
\]

Equations (51)--(53) prove (49).  Finally
`H_2(R)=log_2|E|-H_2(I,p|R)`, because the conditional law inside an
`R`-cell is uniform on its repair pairs.  Substitute this in (49) and
divide by two to obtain (50).  QED.

Formula (49) is the desired two-ended expansion in entropy form:

\[
 V(P)\ge {\sqrt{|E|\,2^{H_2(R)}}\over(r+1)^{3/2}}. \tag{54}
\]

If retained boundaries carry almost all edge entropy, the two convex
endpoint families `A` and `B` pay the repair edges with polynomial
congestion.  Otherwise entropy is preserved inside the smaller fixed-`R`
cells.  More explicitly, if `E_R` is the number of repair pairs with
retained boundary `R`, then

\[
 H_2(I,p|R)=\sum_R{E_R\over|E|}\log_2E_R.          \tag{55}
\]

Thus the residual term in (50) is the edge-weighted geometric mean of the
recursive cell loads, not a worst-case or unweighted loss.  This is the
precise weighted “expand or recurse” dichotomy requested by capped Hall.

The cap enters cleanly.  If every source selected at most
`d=2^{ell-r+O(1)}` blockers, then, conditional on `(R,I)` (equivalently on
the source together with one of only polynomially many interval tags),

\[
 H_2(p|R,I)\le\log_2d=\ell-r+O(1).
\]

Consequently

\[
 \boxed{
 \log_2{|E|\over V(P)}
 \le {1\over2}H_2(I|R)+{\ell-r\over2}+O(\log r).} \tag{56}
\]

The boundary encoding has therefore halved the full cap exponent.  A
completion would iterate (56) down the rooted hidden pocket while proving
that the accumulated conditional hidden entropies are `o(r)`.  What is now
missing is not the outer two-ended inequality—it is (49)—but a theorem that
the recursive pocket can inherit the weighted law in (55) without paying
the hidden label entropy anew.  The product-grid construction shows that
this inheritance must retain forward cap--cup orientation.

There is an exact limit to this iteration.  The source faces themselves
give `|E|<=dV(P)`.  Combining that bound with (56), and writing
`q=ell-r`, gives the sharp one-step recurrence

\[
 \boxed{
 \log_2{|E|\over V(P)}
 \le\min\left\{q,{q+H_2(I|R)\over2}\right\}
       +O(\log r).}                                \tag{57}
\]

Thus Shannon halving improves the cap only when the hidden conditional
entropy is below `q`.  It cannot be iterated formally by replacing that
entropy with another copy of the same inequality.  The following abstract
cell makes this obstruction exact.  Let `R,I,p` range independently over
sets of sizes `N,M,M`, and take every triple as a repair record.  Encode its
two endpoints by

\[
                         A=(R,I),\qquad B=(R,p).
\]

Then

\[
 |E|=NM^2,quad |\mathcal A|=|\mathcal B|=NM,quad
 H_2(R)=\log_2N,quad H_2(I|R)=H_2(p|R,I)=\log_2M. \tag{58}
\]

Entropy submodularity (51) is equality, and both entries of the minimum in
(57) equal `log_2M` when `q=log_2M`.  Nesting another independent copy in
the `I` coordinate merely reproduces the same equality; the geometric
series of formal half-factors sums back to the original cap exponent.

This is not an artificial pattern.  A vertical product cell contains the
same local rectangle: fix every microblock except one, let `I` choose a
lower point in that block, and let `p` choose an upper point.  Every upper
choice replaces every lower choice, while the choices in the other blocks
form the retained word `R`.  The endpoint families have exactly the product
form (58).  What prevents a capped counterexample is not (49), but the
extra forward two-ended faces counted in
`../agent_two_ended_hall/REPORT.md`.  Hence a successful iteration theorem
must assert:

\[
 \boxed{H_2(I|R)\gtrsim q
 \quad\Longrightarrow\quad
 \text{a forward two-ended face pool, or an ES-large child cloud}.}       \tag{59}
\]

Without a geometric implication of the form (59), repeated Shannon
submodularity is exactly saturated and cannot close the proof.

### Delta systems do not by themselves recover the lost entropy

The quadratic retained-boundary count does force a large sunflower, but
the elementary bound loses almost all of the quadratic entropy.  If a
uniform `k`-set family has no `t`-sunflower, the maximal-sunflower argument
gives

\[
                         |\mathcal R|\le k!(t-1)^k. \tag{60}
\]

Consequently, from
`|\mathcal R|>=n^{gamma k}` and `log k=o(log n)` one can force, for example,
a sunflower of size

\[
                              t=n^{\gamma/2}.       \tag{61}
\]

This is exponential in `r=Theta(log n)`, but has only `Theta(r)` bits,
whereas the original boundary family has `Theta(r^2)` bits.  Covering the
family by such sunflowers may still require `2^{Theta(r^2)}` pieces, so
Theorem 6 cannot simply be summed over them.

There is also an exact planar obstruction to turning the petals into a
Boolean face product.  In a vertical product cell, fix the selected point
in every microblock except one.  Let the retained boundaries vary over the
`M` possible points in that block.  They form a sunflower with the fixed
points as core and singleton petals.  The union of any two petals with the
core is nonconvex: an intermediate occupied microblock may contribute only
one point.  Thus even the strongest possible disjoint-petal conclusion does
not imply that petal unions are target faces.

The sunflower is nevertheless harmless in the full product cell because
the cap--cup pool uses two *oriented endpoint blocks*, not unions of petals
in one block.  This again points to (59): delta-system extraction must be
coupled to forward orientation.  Set-pair disjointness alone cannot supply
the missing face multiplication.

### A common support edge preserves the quadratic entropy

There is a stronger geometric concentration than a delta system.  Let
`mathcal R` be `F` convex retained boundaries, all of size `k=Theta(r)`.
Counting polygon edges gives `kF` incidences with unordered pairs of ambient
points.  Hence some pair `u,v` is an edge of at least

\[
                         {2kF\over n(n-1)}          \tag{62}
\]

members.  Split once according to the side containing the rest of the
polygon.  If `log_2F=Omega(r^2)` and `r=Theta(log n)`, the resulting oriented
root-edge subfamily still has

\[
                  \log_2F-2\log_2n+O(\log r)
                  =\log_2F-O(r)                    \tag{63}
\]

bits.  Unlike the elementary sunflower, it preserves the full quadratic
leading term.

For the repair graph one can fix the relevant edge directly.  In (48), the
new point `p` is addable to the retained polygon `R`, so it replaces one
unique support edge `uv` of `R`.  Partitioning the selected repair edges by
this pair leaves a common-root group of size at least `|E|/binom(n,2)`.
Thus fixing the actual rooted pocket also costs only `2L+O(1)` entropy bits;
it does not incur the quadratic loss of sunflower extraction.

However, a common support edge does **not** by itself give a rooted product.
The naive opposite-side gluing assertion is false already for two
triangles.  Take

\[
 u=(0,0),\quad v=(1,0),\quad p=(100,1),\quad q=(-100,-2).       \tag{64}
\]

Both `{u,v,p}` and `{u,v,q}` are convex triangles on opposite sides of
`uv`, with `uv` a hull edge.  But

\[
 v=.97u+.02p+.01q,                                  \tag{65}
\]

so `v` is strictly inside `conv{u,p,q}` and the four-point union is not
convex.  Thus even rooted faces on opposite sides can anti-align their
tangent slopes.

This exact counterexample explains why the product theorem in
`../agent_two_ended_hall/REPORT.md` is *forward oriented*: a cap on the
first side must be paired with a cup on the second.  Root membership and a
common chord do not record that orientation.  Support-edge concentration
therefore preserves the quadratic entropy, but a completion still needs a
four-corner/tangent-order theorem which extracts a large forward-compatible
subfamily without losing `Theta(r)` bits.

The conclusion is sharper than the sunflower audit.  Delta-system entropy
loss can be avoided by fixing a support edge, but the hoped-for automatic
face multiplication is exactly false.  The surviving obstruction may put
quadratically many boundaries on one root chord while anti-aligning the two
endpoint directions; that is the same mixed forward term isolated in
`ROOTED_OMISSION_AND_EIC.md`.

## 12. Exact tangent rectangles, with no ambient partition loss

Recording both endpoint tangents repairs the false common-chord gluing
claim.  More importantly, doing so does **not** cost a factor `n^4` when the
resulting completed targets are summed globally.

Orient a chord `uv`.  An upper rooted chain is a set `X` in the positive
open half-plane of `uv` for which `X union {u,v}` is convex and `uv` is one
of its hull edges.  Define lower rooted chains analogously.  If `R` is a
lower rooted chain including the roots, let `a(R)` and `b(R)` be the
neighbours of `u` and `v`, respectively, on the lower arc of `R`; the other
neighbour of each root is the other root.  A **tangent cell** is specified
by `(u,v,a,b)`.

> **Theorem 13 (exact tangent rectangle).**  Let `mathcal R` be any family
> of lower rooted chains in one tangent cell `(u,v,a,b)`.  If an upper
> rooted chain `X` has `R_0 union X` in convex position for one
> `R_0 in mathcal R`, then
> 
> \[
>                         R\mathbin\cup X
> \quad\hbox{is convex for every }R\in\mathcal R.    \tag{66}
> \]
> 
> Hence every compatible upper family `mathcal X` produces the full
> rectangle of `|mathcal R||mathcal X|` distinct convex targets.
> If tangent rectangles over arbitrary directed chords are all counted, a
> convex `k`-set is counted at most `k(k-1)` times.

**Proof.**  Traverse the polygon obtained by concatenating the upper arc
from `u` to `v` and the lower arc from `v` back to `u`.  The arcs lie in
opposite open half-planes, so the traversal is simple.  Every turn internal
to either arc is already a strict convex turn.  The only two turns not
certified by rooted convexity are the turns at `u` and `v`; they involve,
respectively, only `a,u` and the first upper point, and the last upper point
and `v,b`.  Thus their signs depend on `a,b,X`, but on no other member of
`R`.  They have the correct signs for `R_0 union X`, and hence for every
`R union X`.  A simple polygon all of whose turns have the same strict sign
is convex, proving (66).

For fixed directed `uv`, the two open half-planes recover `R-{u,v}` and
`X` from the target, and then recover `a,b`; thus the rectangle map is
injective inside the cell.  Across cells, a target can choose its directed
chord `uv` in at most `k(k-1)` ways, after which the cell is forced.  QED.

Apply this to exterior repairs.  In the notation (48), let `u,v` be the
endpoints of the hidden interval.  Both the hidden chain `I` and the
singleton chain `{p}` are compatible with the retained lower chain `R`.
For a fixed tangent cell `c`, write

\[
 \mathcal R_c=\{R\},\qquad
 \mathcal J_c=\{I\},\qquad Y_c=\{p\},
 \quad s_c=|\mathcal J_c|,\quad t_c=|Y_c|.          \tag{67}
\]

Let `E_c` be any selected set of repair triples in the cell, with at most
`d` selected blockers above one source `(R,I)`.  Theorem 13 supplies all
cross-completions

\[
 \mathcal T_c=
 \{R\cup X:R\in\mathcal R_c,\
      X\in\mathcal J_c\cup\{\{p\}:p\in Y_c\}\}.   \tag{68}
\]

Consequently

\[
 |\mathcal T_c|\ge |\mathcal R_c|\max\{s_c,t_c\},
 \qquad
 |E_c|\le\min\{d|\mathcal R_c|s_c,
                 |\mathcal R_c|s_ct_c\},          \tag{69}
\]
and therefore

\[
 \boxed{|E_c|\le\min\{d,s_c,t_c\}|\mathcal T_c|.} \tag{70}
\]

If all hidden intervals have size at most `I_0`, the targets in (68) have
rank at most `K=r+I_0`.  The last assertion of Theorem 13 gives the global
bounded-overlap inequality

\[
 \boxed{
 |E|\le K(K-1)V(P)\max_c\min\{d,s_c,t_c\}.}        \tag{71}
\]

This is the requested two-dimensional tangent-dominance rectangle with no
ambient-label partition penalty.  Merely pigeonholing `(u,v,a,b)` would
lose `O(r)` bits; completing the whole rectangle writes those labels into
the target and reduces the loss to `O(log r)` congestion.  In particular,
every cell with either `s_c=2^{o(r)}` hidden chains or
`t_c=2^{o(r)}` blocker labels is discharged.  A surviving cell must have
exponentially many objects on **both** upper coordinates.

The conclusion is sharp and also identifies the next gate.  In the vertical
product construction, fix a hidden microblock, the two root points in its
adjacent macroblocks, and the other retained neighbour of each root.  Let
all more distant retained coordinates vary.  The lower and upper halves of
the hidden microblock give
`s_c=t_c=M/2`, every upper point replaces every lower point, and the
tangent cell is a complete product

\[
 |E_c|=|\mathcal R_c|s_ct_c,
 \qquad |\mathcal T_c|=|\mathcal R_c|(s_c+t_c).    \tag{72}
\]

Thus (70) is tight within a constant factor.  The extra `M` which pays the
cap comes from varying the *adjacent tangent cells*: it is exactly the
two-ended `binom(M,2)^2` pool in the product theorem, and it disappears if
the two endpoint neighbours are frozen.  Therefore no theorem confined to
one exact tangent rectangle can close the hard branch.  The remaining
stability statement must compare many neighbouring tangent cells and show
that either their endpoint ranks form a forward cap--cup pool, or the
anti-aligned mass descends into a smaller rooted pocket with the weighted
fibre bound (17) of the two-ended report.

This also kills the strongest proposed one-cell DRC conclusion: even a
complete incidence rectangle with fixed endpoint tangent data may retain
the full cap loss.  What DRC must extract is not density inside one
rectangle, but forward variation **between** rectangles.

## 13. The precise weighted ordered-array gate

The adjacent-cell variation can be stated without any entropy notation.
Fix a directed root chord `uv`, a lower inner chain/signature `S`, and one
upper hidden chain `I`.  A retained boundary with this data is obtained by
choosing a left endpoint neighbour `a` and a right endpoint neighbour `b`;
write `ab` for the resulting boundary when it is convex.  The occurring
choices form a simple bipartite support graph

\[
                         G\subseteq A\times B.      \tag{73}
\]

Two distinct choices `a,a'` are **left-forward** if both survive in the
corresponding lower endpoint cap.  Define **right-forward** analogously,
with the cup orientation.  If `ab,a'b'` are vertex-disjoint edges and both
endpoint pairs are forward, then

\[
 T(aa';bb')=\{u,v\}\cup S\cup I
              \cup\{a,a',b,b'\}                   \tag{74}
\]

is a convex target.  This is just the same two-ended concatenation used in
Theorem 13, now with a two-point cap at one end and a two-point cup at the
other.  Conversely, for a fixed state `(u,v,S,I)`, the target (74) recovers
the unordered endpoint pairs.  At most the two perfect matchings of their
`2 by 2` rectangle can have generated it.  Across all states, a target of
rank at most `K` has at most `2K^6` descriptions: choose the directed roots
and the four special endpoint vertices, after which the two half-planes
recover `S` and `I`.

Here is the exact unweighted array calculation.  Put `m=|E(G)|`, let
`Delta_A,Delta_B` be the two maximum degrees, and let `D(G)` be the number
of unordered pairs of vertex-disjoint support edges.  Then

\[
 \begin{split}
 D(G)
 &=\binom m2-\sum_{a\in A}\binom{d(a)}2
                 -\sum_{b\in B}\binom{d(b)}2,\\
 &\ge {m\over2}\{m+1-\Delta_A-\Delta_B\}.          \tag{75}
 \end{split}
\]

If every endpoint pair appearing in (75) is forward, the number `F(G)` of
distinct targets (74) obeys

\[
                         F(G)\ge {D(G)\over2}.       \tag{76}
\]

Suppose the fixed hidden source has capped demand `d` for each of the `m`
boundary variants.  Equations (75)--(76) give the sharp dichotomy

\[
 \boxed{
 F(G)\ge dm
 \quad\hbox{or}\quad
 \Delta_A+\Delta_B>m+1-4d.}                        \tag{77}
\]

Thus, unless the forward targets already pay all `dm` selected repairs,
one endpoint value occurs on at least

\[
                  {m+1-4d\over2}                  \tag{78}
\]

of the source boundaries.  When `m` is large compared with `d`, this is
essentially half of the mass.  Fix that endpoint and peel it into the
frame.  The retained rank drops by one, so the new cap is `2d`; retaining
half the sources is exactly weight-neutral:

\[
       d\,m\quad\longleftrightarrow\quad
       (2d)\,{m\over2}.                             \tag{79}
\]

This is the promised weighted recurse alternative; the factor two in
(78) is not an uncompensated loss.  The additive `O(d)` fringe in (78) is
the only residual in the fully forward ordered-array model.  If `m=O(d)`,
the state has only `O(d)` endpoint variants and must be absorbed by the
one-cell pocket theorem or passed to the blocker/hidden child cloud.

**Proof of (75)--(77).**  A pair of distinct edges either is disjoint,
shares its unique left endpoint, or shares its unique right endpoint.  The
three cases are disjoint and give the identity in (75).  Also
`sum_a binom(d(a),2)<=m(Delta_A-1)/2`, and similarly on the right, proving
the lower bound.  A target endpoint rectangle has at most two perfect
matchings, proving (76).  If `F(G)<dm`, then `D(G)<2dm`; substitute the
lower bound in (75) and cancel `m` to obtain the second alternative in
(77).  QED.

The unrestricted geometric gate is now exact.  Not every disjoint edge
pair need be forward.  Let `D_bad^A` and `D_bad^B` count disjoint edge pairs
whose left, respectively right, endpoint pair is nested rather than
forward.  Then

\[
                  D(G)\le2F(G)+D_bad^A+D_bad^B.     \tag{80}
\]

A bad endpoint pair has a canonical direction: one endpoint lies in the
rooted triangle/pocket of the other.  It therefore defines a smaller
one-ended child state, rather than an unexplained collision.  What remains
to prove is the weighted allocation

\[
 d\sum_\sigma |E(G_\sigma)|
 \le r^{O(1)}\left(
      \sum_\sigma F(G_\sigma)
      +\sum_\tau 2d\,|E(G_\tau)|\right),           \tag{OAI}
\]

where a nested pair is first offered to its one-endpoint-peeled child
`tau`, and no child is meant to receive more than its doubled cap.  The
recovery bound above shows that the first sum has only polynomial global
overlap.  The displayed inequality is the clean desired invariant, but the
next proposition shows that the word “child” cannot mean one automatic
rank-one repair: a nested endpoint may remain hidden through an arbitrarily
long peeled prefix.  The open content is to pay that prefix before the
second sum can be iterated.

This formulation also makes anti-alignment precise.  A sequence of support
edges with increasing left endpoints and decreasing right endpoints is not
by itself an obstruction: its edge pairs still yield distinct endpoint
rectangles whenever both marginal pairs are forward.  The genuine
anti-aligned case is when one marginal sequence is *nested*, so that its
two-point cap or cup disappears.  Such a sequence is exactly a chain of
smaller rooted triangles and belongs in the recursive term of `(OAI)`.
The vertical product array has all marginal pairs forward, so (76) produces
the `binom(M,2)^2` pool directly.

### A nested pair need not repair after one rank drop

The tempting rank-one implementation of `(OAI)` is false, by a scalable
exact configuration.  For `s>=1`, put `N=2s+4` and

\[
 \begin{array}{lll}
 u=(0,0),&c=(N,0),&w_j=(j,j(j-N))\quad(1\le j\le s),\\
 a=(N/2,1),&&A=(N/2,N^2).                           \tag{84}
 \end{array}
\]

The points `u,w_1,...,w_s,c` lie on a strict parabola and form a convex
lower chain `Q_s` with hull edge `uc`.  Both `Q_s union {a}` and
`Q_s union {A}` are convex.  On the other hand, `a` is interior to
`conv{u,c,A}`, so the pair of endpoint alternatives is nested.  More
strongly, for every `1<=j<=s`,

\[
 a\in\operatorname{int}\operatorname{conv}\{w_j,c,A\}.        \tag{85}
\]

Consequently `a` remains nonextreme after deleting successively
`u,w_1,...,w_(j-1)`.  It becomes exposed only after the entire prefix
`u,w_1,...,w_s` has been deleted, a rank drop of `s+1`.  All points in (84)
are in general position: a chord through two selected parabola points has
negative height at `x=N/2`, whereas `a,A` have positive heights, and no
selected parabola point has `x=N/2`.

Thus the bad term in (80) cannot be sent immediately to a rank-`r-1`
convex target, even with fixed tangent data.  Repeated endpoint peeling is
geometrically necessary.  The example is not a Hall obstruction: the
discarded parabolic prefix is itself in convex position and supplies
`2^{s+1}` ordinary faces, exactly the scale by which the cap grows after
`s+1` rank drops.  It gives the corrected recursive target:

\[
 \boxed{
 \text{forward target, or expose the nested endpoint, or charge the
        whole peeled-prefix face complex}.}          \tag{86}
\]

Carrying only the most recently peeled endpoint label is insufficient;
the invariant must carry the entire prefix pocket until its convex-face
capacity is released.  The unresolved global issue is again reuse: the
same prefix face may occur below many outer frames.  The common-core and
source-cloud theorems above discharge this when the frame family has
subquadratic entropy; the quadratic crossing case is precisely the final
weighted prefix-packing problem.

### The multilevel entropy accounting

There is an exact reason the nested term cannot be discarded.  For a
uniform family of lower rooted `k`-chains, list the lower arc as
`x_1,...,x_(k-2)` from `u` to `v` and reveal it in endpoint pairs

\[
 W_j=(x_j,x_{k-1-j})
 \quad(1\le j\le\lfloor(k-2)/2\rfloor),            \tag{81}
\]

with the middle singleton revealed last when necessary.  These variables
determine the retained boundary, so Shannon's chain rule is the identity

\[
 H_2(R)=\sum_j H_2(W_j\mid W_1,...,W_{j-1}).        \tag{82}
\]

Every summand is at most `2L`, where `L=log_2n`.  Hence if
`H_2(R)>=gamma L^2`, and `N_theta` summands are at least `theta L`, then

\[
 N_\theta\ge
 {\gamma L^2-m\theta L\over(2-\theta)L},
 \qquad m=\lceil(k-2)/2\rceil.                     \tag{83}
\]

For `k=Theta(L)` and sufficiently small fixed `theta>0`, there are
`Omega(L)` high-entropy adjacent-cell interfaces.  Peeling a pair lowers
rank by two and permits only fourfold weighted fibre, while a high interface
has `2^{Omega(L)}` choices.  Therefore pure nested descent cannot telescope
quadratic boundary entropy; linearly many interfaces must be paid by the
forward term in `(OAI)` or by ES-large child clouds.  A product grid
saturates (82): essentially every pair contributes `2log_2M`, and its
forward two-ended pools pay exactly at those levels.

Equations (73)--(83) are a precise potential for the final attack.  They
prove the full adjacent-cell statement when all marginal pairs are forward,
and reduce the general case to capped reuse of canonically nested one-ended
children.  No entropy-halving or sunflower step remains hidden in the
formulation.

## 14. High prefix-cloud reuse: an exact threshold and tangent trichotomy

The fixed-terminal-child theorem in `../agent_two_ended_hall/REPORT.md`
reduces a `sqrt(r)` nested batch to the reuse multiplicity of ordinary
prefix faces.  There is an immediate but useful correction to the scale of
that gate.  Exponential-in-`r` reuse is not yet hard; the obstruction must
have quadratic child entropy.

Fix one nonempty ordinary prefix face `X`, and let `mathcal C_X` be `M`
distinct terminal child faces to which the local allocation reuses `X`.
Above each child select at most `d` next nested labels, and let `e_X` be the
number of selected child--label incidences.  Let `Y` be the union of those
labels.  The geometry of `X` is irrelevant for the following bound.

> **Theorem 14 (subquadratic high-reuse discharge).**  For every fixed
> `c<1/4`,
> \[
>  \boxed{
>  e_X\le 2^{T_X}V(P),\qquad
>  T_X={1+\sqrt{1+4c\log_2M}\over2c}.}              \tag{87}
> \]
> Consequently, if `r=Theta(log n)` and
> `log_2M=o(r^2)`, then `e_X<=2^{o(r)}V(P)`.

**Proof.**  The terminal children are themselves `M` distinct convex
faces.  The selected pairs form an arbitrary bipartite graph from these
faces to the point set `Y`, with maximum child degree `d<=|Y|`.  Apply
Theorem 9 with `s=M`.  QED.

Thus the phrase “a prefix face is reused by `2^{Omega(r)}` children” is too
weak for the final gate.  A fixed prefix face capable of obstructing capped
Hall must be reused by

\[
                         M=2^{\Omega(r^2)}          \tag{88}
\]

terminal children.  The same conclusion holds for any
`2^{o(r)}`-sized family of fixed prefix faces, by summing (87).

The 2D tangent geometry gives an exact next split.  At any rooted merge
state, record for each prefix chain its two endpoint tangent ranks and do
the same for the terminal child on the opposite side of the active chord.
As in Theorem 13, their union is convex exactly when the two junction turns
have the correct signs.  After reversing one of the rank orders if needed,
this is a two-coordinate dominance condition

\[
                 \lambda_1(X)\le\rho_1(C),qquad
                 \lambda_2(X)\le\rho_2(C).         \tag{89}
\]

For a fixed `X`, the compatible children therefore form one orthant in the
ordered array.  Its complement is the union of the two canonical slabs

\[
 \rho_1(C)<\lambda_1(X)
 \quad\hbox{or}\quad
 \rho_2(C)<\lambda_2(X).                           \tag{90}
\]

The first slab is exactly left-end nesting and the second is right-end
nesting.  If `Gamma` is any multiset of prefix--child incidences at this
state, (89)--(90) partition it into completed, left-nested, and right-nested
parts.  Hence either at least one third of `Gamma` is already represented
by a completed convex target, or at least one third enters one fixed
marginal child.  Repeating through a batch of length
`s=ceil(sqrt(r))` costs at most

\[
                            3^s=2^{o(r)}.           \tag{91}
\]

Completed targets have subexponential recovery multiplicity.  Without
using the rooted arc structure, a target of rank `K=O(r)` and a prefix of
size at most `s` have at most

\[
                   \sum_{j\le s}\binom Kj
                   \le K^{s+1}=2^{o(r)}            \tag{92}
\]

possible decompositions.  With the active chord retained, Theorem 13
improves this to `O(K^2)`.

Combining (87)--(92), every surviving prefix-reuse class can be localized,
with total `2^{o(r)}` loss, to the following much stronger state:

* one prefix face `X` is shared by `2^{Omega(r^2)}` terminal children;
* all completed tangent incidences have already been charged; and
* every remaining child follows the same length-`sqrt(r)` word of left/right
  marginal nestings.

This is a quantitative theorem, not yet the full reuse gate.  The remaining
claim would have to show that such a quadratic-entropy, fixed-word child
family either releases an opposite-marginal ordered-array pool or has an
induced child cloud whose ordinary convex mass pays the cap.  The deep
parabolic family (84) shows why one cannot replace that claim by automatic
exposure at the next rank.  A product grid shows the other extreme: the
fixed-word fibres can be large, but their opposite marginal supplies the
two-ended pool.  No scalable planar family is known which defeats both
alternatives.

## 15. An entropic split-sequence theorem, and its exact limit

The fixed marginal word in the preceding section can be modeled by an
ordered array.  Let

\[
 \mathcal W\subseteq Q_1\times\cdots\times Q_b,
 \qquad |Q_i|=m_i,                                  \tag{93}
\]

where each `Q_i` is put in its tangent order.  For two distinct words, sort
them lexicographically as `x<y`.  Call the pair **forward** if for some
`i<j`

\[
                         x_i<y_i,qquad x_j>y_j.     \tag{94}
\]

Geometrically, (94) is a cap-coordinate followed by a cup-coordinate after
the appropriate reversal of one marginal order.  It is the abstract
pattern which releases a two-ended target.

> **Theorem 15 (single-crossing split theorem).**  If `F` is the graph on
> `mathcal W` whose edges are the forward pairs, then
> \[
>  \alpha(F)\le B:=1+\sum_{i=1}^b(m_i-1),           \tag{95}
> \]
> and, writing `M=|mathcal W|`,
> \[
>  \boxed{
>  |E(F)|\ge {M\over2}\left({M\over B}-1\right).}  \tag{96}
> \]
> In particular, for every `d>=1`,
> \[
>  \boxed{
>  M>(2d+1)B\quad\Longrightarrow\quad
>  |E(F)|>dM.}                                     \tag{97}
> \]

**Proof.**  Let `mathcal A` contain no forward pair and list its words in
lexicographic order.  For two consecutive words `x<y`, let `i` be their
first unequal coordinate.  Then `x_i<y_i`.  Absence of (94) forces
`x_j<=y_j` at every later coordinate, while earlier coordinates are equal.
Thus the lexicographic list is a chain in the coordinatewise product order.
The rank potential

\[
                  \phi(x)=\sum_i\operatorname{rank}_{Q_i}(x_i)
\]

strictly increases along this chain and ranges over an interval of length
`sum_i(m_i-1)`, proving (95).  The standard greedy independent-set bound
`alpha(F)>=M^2/(2|E(F)|+M)`, together with (95), gives (96), and (97)
follows immediately.  QED.

When the coordinate pools are disjoint subsets of the ambient point set,
`B<=n+1`.  Since both `d` and `n` have only `O(r)` logarithmic bits, (97)
shows that every `2^{Omega(r^2)}` fixed-word child family supplies far more
than `dM` abstract forward pairs.  Thus a quadratic family cannot consist
mostly of genuine cup--cap threshold sequences.  In the zero-forward case
it is not merely “clustered around a threshold”: it is one product-order
chain of size at most `n+1`.

This theorem is the desired entropic split statement, but it does not alone
finish the geometric charge.  A two-ended target for a forward pair keeps
the two endpoint alternatives and the intervening boundary word; it may
forget the common coordinates outside the forward interval.  Many word
pairs can consequently yield the same target.  The product-grid regression
realizes an inverse fibre of `M_0^{Theta(b)}` even though essentially every
word pair has two separated differing coordinates.  Thus the implication

\[
              |E(F)|\gg dM
              \quad\Longrightarrow\quad
              \text{that many distinct convex targets}        \tag{98}
\]

is false without an outside-signature or prefix-capacity term.

Theorem 15 nevertheless kills the purely anti-aligned counterexample.  The
remaining high-reuse gate is now a **target-recovery theorem**: allocate the
abundant forward pairs in (96) while charging the forgotten common
prefix/suffix word either to its Boolean prefix faces or to the induced
terminal-child cloud.  The exact product family shows that this allocation
is possible through the sum over all forward intervals, but also that no
single-interval bounded-fibre map can prove it.

## 16. Conditional high/medium recovery, and the short-word obstruction

The split theorem does give a useful global lemma, but only after stating
an injectivity hypothesis which was missing from the first version of this
report.  This distinction is load-bearing.

Let `mathcal X` be a family of ordinary prefix faces of size at most `s`.
For each `X`, let `mathcal C_X` be a row of terminal children.  Suppose that
there is an **injective** encoding

\[
 w:\bigcup_X\mathcal C_X\longrightarrow
 Q_1\times\cdots\times Q_b,                       \tag{99}
\]

with the tangent orders of Theorem 15, and put

\[
 B=1+\sum_{i=1}^b(|Q_i|-1).                        \tag{100}
\]

Suppose also that every forward pair in one row, with a choice of its
forward interval, produces a convex target.  No bounded recovery is assumed.
A deliberately wasteful decoder guesses the order of the pair, its interval,
the prefix `X`, and both complete words.  Hence its global fibre is at most

\[
 \boxed{K_{b,s}=2b^2(s+1)n^{2b+s}.}                \tag{101}
\]

Indeed there are at most `2b^2` order/interval tags,
`sum_(j<=s)binom(n,j)<=(s+1)n^s` choices for `X`, and at most `n^(2b)`
ordered word pairs.  Injectivity in (99) then reconstructs the two children.
This proves (101) even when the target itself forgets every word label.

> **Theorem 16 (conditional high/medium row dichotomy).**  Suppose every
> prefix--child incidence carries load at most `a`, and put
> \[
>              T=4aBK_{b,s}.                       \tag{102}
> \]
> If `M_X=|mathcal C_X|`, then all rows with `M_X>=T` produce at least
> \[
>                   a\sum_{M_X\ge T}M_X            \tag{103}
> \]
> distinct convex targets.  The total loaded mass in the remaining rows is
> at most
> \[
> 4a^2BK_{b,s}(s+1)n^s.                            \tag{104}
> \]

**Proof.**  For `M_X>=T>=2B`, (96) gives

\[
 F_X\ge {M_X^2\over4B}
       \ge aK_{b,s}M_X.                            \tag{105}
\]

Sum over the high rows and divide by the global fibre (101), proving
(103).  There are at most `(s+1)n^s` possible prefix rows, and every medium
row has size less than `T`; multiplying their total size by `a` proves
(104).  QED.

If `log n=Theta(r)`, `log a=O(r)`, and `b,s=o(r)`, the logarithm of (104)
is

\[
              (2b+2s)\log_2n+O(r+\log(bs))=o(r^2). \tag{106}
\]

Thus the universal Erdos--Szekeres face reservoir absorbs **all** medium
rows at once, while (103) pays all high rows.  This would close the reuse
gate if the hard terminal children admitted the injective short encoding
(99).

They do not.  The elementary cardinality obstruction is

\[
 \boxed{
 |\bigcup_X\mathcal C_X|\le\prod_i|Q_i|\le n^b.}  \tag{107}
\]

For `b=sqrt(r)` and `log n=Theta(r)`, the right side has only
`O(r^(3/2))` bits.  The unresolved branch, by contrast, has
`Omega(r^2)` bits of terminal-child entropy.  If the word records only the
length-`sqrt(r)` nesting batch and omits the retained child core, many
different children receive the same word.  Theorem 15 is a theorem about a
**set** of distinct words; after replacing one word by arbitrarily many
child copies its forward graph is edgeless and its independence number is
unbounded.  Thus (95)--(96) cannot be applied to those copies.

This is realized by the standard vertical product configuration.  Take
`q=Theta(log n)` ordered microblocks of size `M`, with
`n=qM+O(1)`.  Choosing one point in every block gives `M^q` convex child
cores.  Fix all labels seen by any `s=o(q)`-long batch and vary the remaining
blocks.  Then

\[
                   M^{q-s}=2^{Theta((\log n)^2)}  \tag{108}
\]

distinct terminal children have the same batch word.  Hence this is not
merely a formal encoding objection.

One can restore injectivity by encoding the retained core, but then
`b=Theta(r)`.  Formula (101) has

\[
                  \log_2K_{b,s}=Theta(r\log n)=Theta(r^2),    \tag{109}
\]

so neither (103) nor (104) is absorbed by the coefficient-`1/4` universal
reservoir.  In the product example, `K_{b,s}` can even exceed the total
number of children.  The short decoder and the quadratic child entropy
cannot be had simultaneously.

## 17. Comparable suffixes cannot repair the decoder

There is a tempting way to try to reduce (109).  Canonicalize a forward
pair by its first cap coordinate `i` and its last later cup coordinate `j`.
Before `i` the two words agree, and after `j` they are coordinatewise
comparable.  One might hope to retain this comparable suffix as a one-ended
chain.  The vertical product classification kills that proposal exactly.

> **Proposition 17 (endpoint cup forbids a retained suffix).**  In a
> vertical composition, a convex face spanning at least two occupied blocks
> has a cap in its first occupied block, a cup in its last occupied block,
> and exactly one point in every intermediate occupied block.  Consequently,
> if a two-ended target contains a two-point cup in block `j`, adjoining
> even one point from a later block makes the target nonconvex: block `j`
> becomes an intermediate occupied block containing two points.

This remains true when the later coordinate is equal in the two source
words, so coordinatewise comparability gives no help.  If the target moves
its last endpoint farther right, it may retain both labels in at most one
later block and at most one label in every intervening block.  For `t`
comparable suffix coordinates with `M` possible labels, there are
`binom(M,2)^t` ordered comparable input-pair signatures, whereas all convex
targets cut from those signatures number at most

\[
 O(t^2)\binom M2^2(M+1)^{t-2}.                    \tag{110}
\]

The average recovery fibre is therefore at least

\[
 {1\over O(t^2)}
 \left({\binom M2\over M+1}\right)^{t-2},         \tag{111}
\]

which is exponential in `t log M`.  The outside-word loss in (101) is a
real geometric information loss, not an artefact of choosing a noncanonical
interval.

The load-bearing geometric premise is also proved only in a common rooted
state: Theorem 13 and (74) construct the two-ended target when the root
chord and inner chain/signature are fixed.  High reuse of a discarded prefix
face does not by itself fix the retained terminal-child core.  No argument
currently shows that an inversion of their short batch words glues two
varying cores to a convex target.  The vertical product supplies targets by
using the **full** block word, which is exactly the quadratic-length decoder
regime (109).

Thus the high/medium split is a correct conditional lemma but does **not**
prove capped RPH, RNP, or Erdos 838.  The remaining statement is the original
entropy-sensitive all-interval gate:

\[
 \boxed{
 \text{charge the labels forgotten by all forward intervals to their
 actual convex prefix/suffix faces, with only }2^{o(r)}\text{ reuse}.}
                                                               \tag{KIC}
\]

The long parabolic prefix and the product grid remain the two sharp tests.
The first delays all exposure to the last depth but supplies its Boolean
prefix cube.  The second has quadratic child entropy and exponential
single-interval fibre, but its sum of all two-ended block intervals pays.
Any proof of `(KIC)` must use both sources of capacity; a short-word
second-moment argument alone cannot close the gate.

## 18. Entropy forces the exact successor expansion factor

There is a rigorous way to enter the all-interval recursion at precisely
the factor requested by capped Hall.  Fix a total order on `P`.  Encode each
rank-`r` convex source by listing its vertices counterclockwise, starting at
its least vertex.  (Fix either orientation once.)  This is an injective word

\[
                         X=(X_1,\ldots,X_r).        \tag{112}
\]

Let `mathcal S` be a family of `S` sources and make `X` uniform on it.  Put

\[
 h_i=H_2(X_i\mid X_1,\ldots,X_{i-1}).              \tag{113}
\]

Then `sum_i h_i=log_2S`, so some `i` has `h_i>=log_2S/r`.  For an occurring
prefix `u=(X_1,\ldots,X_(i-1))`, let `N_u` be the number of sources above
`u`, let `Y_u` be the support of their next vertex, and let `H_u` be the
entropy of that next-vertex distribution.

> **Theorem 18 (successor-entropy repair dichotomy).**  For some boundary
> position `i`, the number `Gamma_i` of pairs `(A,p)` such that
> `A in mathcal S`, `p notin A`, and `p` occurs as the `i`th vertex of a
> source with the same `(i-1)`-prefix as `A`, satisfies
> \[
>  \boxed{
>  |\Gamma_i|\ge S\{S^{1/r}-r\}.}                  \tag{114}
> \]
> Moreover, either
>
> 1. there are at least
>    \[
>       {S(S^{1/r}-r)\over2(r+1)}                  \tag{115}
>    \]
>    distinct convex `(r+1)`-faces of the form `A+p`; or
> 2. there are at least `S(S^{1/r}-r)/2` nonconvex repair incidences
>    `(A,p)`, each tagged by a witness source `B` which shares the whole
>    preceding prefix with `A` and has `B_i=p`.

**Proof.**  Conditional on prefix `u`, the next-vertex support has size
`m_u=|Y_u|>=2^{H_u}`.  Jensen and (113) give

\[
 \begin{split}
 \sum_uN_um_u
 &\ge\sum_uN_u2^{H_u}\\
 &\ge S2^{\sum_u(N_u/S)H_u}
   =S2^{h_i}
 \ge S^{1+1/r}.                                   \tag{116}
 \end{split}
\]

For each source above `u`, at most its `r` own labels belong to `Y_u`; all
other labels give pairs in `Gamma_i`.  Subtracting `rS` proves (114).

Split `Gamma_i` according as `A+p` is convex or nonconvex.  In the first
case the target `T=A+p` has at most `r+1` preimages, because a preimage is
specified by the deleted label `p in T`.  Thus if at least half the pairs
are convex, (115) follows.  Otherwise the nonconvex half has the asserted
size.  Deleting `p` repairs `A+p` by definition, and `p in Y_u` supplies a
witness source with the common prefix.  QED.

At a quadratic source scale one may, with only a lower-order change in
(114), insist that `i>=3`.  Indeed
`H_2(X_1,X_2)<=2log_2n`, while `log_2S=Theta((log n)^2)`, so one of the
remaining `r-2` conditional entropies is at least

\[
                  {\log_2S-2\log_2n\over r-2}.     \tag{116a}
\]

This makes the common prefix contain a genuine boundary edge.  It yields a
useful exact geometric improvement in the exterior branch.

> **Lemma 19 (the witness prefix survives exterior repair).**  Let `A,B`
> be two canonical source polygons sharing the consecutive boundary prefix
> `U=(x_1,\ldots,x_(i-1))`, where `i>=3`, and put `p=B_i`.  If `p` is
> exterior to `conv(A)` and `A+p` is nonconvex, then
> \[
>             U\cup\{p\}\subseteq\operatorname{ext}(A+p).     \tag{116b}
> \]
> Consequently the vertices hidden by `p` form one consecutive interval
> entirely in the complementary suffix `A-U`.  From the repaired target,
> the directed endpoint pair `(x_1,x_(i-1))`, and one arc bit, the whole
> common prefix `U` is recovered.  Thus global recovery of `U` costs at most
> `2k(k-1)` descriptions for a target of rank `k`.

**Proof.**  Every directed edge `x_jx_(j+1)` of `U` is a hull edge of both
`A` and `B`.  Hence all points of `A union B`, and in particular `p`, lie
strictly in its inner open half-plane.  The edge remains a support edge of
`conv(A+p)`.  Every vertex of `U` is an endpoint of at least one such edge,
so every one remains extreme.  Since `p` is exterior to `conv(A)`, it too is
extreme after insertion.  The singleton/ear repair classification now puts
the hidden interval in `A-U`.  Given its two endpoints as roots, `U` is one
of the two boundary arcs of the convex target, proving the recovery claim.
QED.

The interior branch can in fact be removed from the entropy selection.
For each fixed prefix `u`, let `q,v` be its last directed edge and order
the possible successor rays `vp`, from outermost to innermost, inside the
open left half-plane of `qv`.  If a source uses successor `a`, every earlier
ray `vp` is **outward** from `a`:

\[
                       \operatorname{orient}(v,a,p)<0.         \tag{116c}
\]

We need one elementary entropy fact.  If a random variable `J` takes values
in the nonnegative integers and has mean `mu`, comparison with the geometric
distribution of mean `mu` gives

\[
 H_2(J)\le(\mu+1)\log_2(\mu+1)-\mu\log_2\mu
          \le\log_2(e(\mu+1)).                    \tag{116d}
\]

Thus `mu>=2^{H_2(J)}/e-1`.

> **Theorem 20 (outward-successor entry theorem).**  At the quadratic
> source scale, choose `i>=3` satisfying (116a), and put
> \[
>          h={\log_2S-2\log_2n\over r-2}.
> \]
> The family of fresh outward successor pairs `(A,p)` has size at least
> \[
> \boxed{
>       S\left({2^h\over e}-r-1\right).}           \tag{116e}
> \]
> Every such `p` is exterior to `conv(A)`.  Hence either their convex
> additions give at least
> \[
>       {S\over2(r+1)}\left({2^h\over e}-r-1\right)             \tag{116f}
> \]
> distinct targets, or there are at least half as many exterior-ear repair
> incidences.  In every repair incidence the hidden interval starts at
> `A_i`, and the repaired target has canonical boundary prefix
> \[
>                       (X_1,\ldots,X_(i-1),p).     \tag{116g}
> \]
> Thus the target itself recovers the common prefix and blocker without an
> ambient-label decoder.

**Proof.**  Conditional on prefix `u`, let `J_u` be the outward rank of the
random successor.  It counts exactly the number of outward successor labels
available before removing labels already in the source.  By (116d), Jensen,
and the choice of `i`,

\[
 \begin{split}
 \sum_uN_u\mathbb E J_u
 &\ge {1\over e}\sum_uN_u2^{H_u}-S\\
 &\ge {S\over e}2^{h_i}-S
 \ge {S\over e}2^h-S.                             \tag{116h}
 \end{split}
\]

At most `r` outward labels already belong to any one source; subtracting
`rS` proves (116e).  Equation (116c) says that `p` violates the hull support
edge `vA_i`, so `p` is exterior.  Convex additions have target multiplicity
at most `r+1`, as in Theorem 18, proving (116f).

In the nonconvex case, `p` satisfies every support edge in the common prefix
because it is itself the next vertex of a witness source with that prefix.
It violates `vA_i`, so the cyclic violated-edge interval begins there and
cannot enter the prefix.  The ear-repair classification says precisely that
the hidden chain begins at `A_i`; after replacement, `p` immediately follows
`v`.  Finally `X_1` remains the least label of the target, since it is least
in both witness sources.  This proves the canonical recovery (116g).  QED.

If every source in `mathcal S` has addable degree at most `u_0`, then at
most `u_0S` pairs in (116e) are convex additions.  Therefore Theorem 20
immediately gives

\[
 \boxed{
 E_{\rm repair}\ge
 S\left({2^h\over e}-r-1-u_0\right)}.             \tag{116g'}
\]

In the near-maximal hard slice one has `u_0<=4(r+1)`, so the subtraction is
negligible compared with `2^h=n^{c/alpha-o(1)}`.  Moreover, a nonconvex
`(r+1)`-set has at most three convex one-point deletions.  Thus the repair
records in (116g') represent at least `E_repair/3` **distinct** nonfaces,
all with the canonical prefix/blocker signature (116g).  The only remaining
collision is the many-to-one hull map from those nonfaces to repaired convex
targets.

The blocked branch has an exact entropy/rank recurrence, although this
recurrence alone does not yet supply the required compatible products.  Let
`mathcal G` be any family of the exterior repair records in Theorem 20.  For
`g=(A,p)`, put

\[
 T_g=\operatorname{ext}(A+p),\qquad
 I_g=A-T_g.                                         \tag{116i}
\]

The canonical recovery (116g) identifies `p` from `T_g`, and then
`A=(T_g-p) union I_g`.  Hence `g mapsto(T_g,I_g)` is injective.  Moreover,

\[
                         |T_g|+|I_g|=r+1.           \tag{116j}
\]

> **Proposition 21 (entropy-density conservation).**  Under the uniform law
> on `mathcal G`, put `tau=E|T_g|` and `kappa=E|I_g|`.  Then
> \[
> \boxed{
> \log_2|\mathcal G|=H_2(T)+H_2(I\mid T),\qquad
> \tau+\kappa=r+1.}                                \tag{116k}
> \]
> Consequently at least one component has entropy per expected rank at
> least the record density:
> \[
> \boxed{
> \max\left\{{H_2(T)\over\tau},
>             {H_2(I\mid T)\over\kappa}\right\}
> \ge {\log_2|\mathcal G|\over r+1}.}              \tag{116l}
> \]

**Proof.**  Injectivity gives `H(T,I)=log_2|mathcal G|`, and the entropy
chain rule gives the first equality in (116k).  Equation (116j) gives the
second.  If both ratios in (116l) were smaller than the right side,
weighting by `tau,kappa` and adding would contradict (116k).  QED.

When `|mathcal G|` has the lower-bound scale in (116e), its record density
in (116l) is

\[
                    {\log_2S\over r}-O(1).         \tag{116m}
\]

Thus a recursive step can always preserve the critical entropy density:
either the retained-target family has it, or the conditional hidden-interval
family has it.  What (116l) does **not** justify is discarding the other
component.  In the product grid, `T` and `I` both have essentially the same
critical density; their two-ended cross-product is the capacity.  Choosing
only one loses a full coordinate factor.  In the long parabolic prefix,
almost all residual entropy is in `I`, and descent to `I` is the correct
move.  These are the two equality tests for the desired recurrence.

Accordingly, a full Kraft potential must strengthen (116k) from an entropy
split into a compatible-face multiplication: when both terms carry
substantial entropy, release a forward two-ended rectangle; when one term
is negligible, recurse into the other while retaining the canonical prefix
tag.  Proposition 21 proves that such an iteration would not lose entropy
density, but the compatible multiplication in the mixed case remains the
unproved geometric step.

At the exact hard scale, write `L=log_2n`,
`r=(alpha+o(1))L`, and `log_2S>=(c-o(1))L^2` with `c>=1/4`.  Then

\[
 S^{1/r}\ge n^{c/alpha-o(1)}
             \ge n^{1-alpha-o(1)},                \tag{117}
\]

because `alpha(1-alpha)<=1/4<=c`.  The last expression is the capped RNP
factor `2^{L-r-o(L)}`.  Hence alternative 1 of Theorem 18 closes the desired
rankwise estimate, with only the harmless polynomial recovery factor.

Alternative 2 does not yet close RNP, but Theorem 20 makes it much narrower
than an arbitrary capped repair graph.  Every selected repair is an
**outward successor of a witness source with a common boundary prefix**;
there is no interior case.  Its completed target canonically retains the
whole common prefix and the blocker, and only one consecutive suffix
interval loses information.  A recursive all-interval theorem only has to
route these prefix-correlated hidden intervals.  The product grid saturates
(116): each level has effective
branching `M=S^{1/r}`, and its full two-ended interval completions pay.  The
deep parabolic example concentrates the repair alternative in a nested
successor chain and pays through the discarded prefix faces.

Thus (112)--(117) prove the proposed `S^{1/r}` expansion at the entropy
level and completely discharge its addable half.  The still-open geometric
statement is: prefix-correlated blocked successors must either release the
same expansion through two-ended intervals, or recurse while charging the
discarded prefix complex with `2^{o(r)}` global reuse.  This is a sharper
form of `(KIC)` and avoids the invalid short-word encoding.

## 19. Boolean thinning retains the full hidden-ear entropy

There is one exact way to recurse on the hidden component without reducing
it to atomic endpoint labels.  It gives a rank-sensitive strengthening of
Proposition 21, but the product cell shows that it still needs the
two-ended term.

Keep the notation of (116i), and put

\[
             R_g=T_g-\{p_g\},\qquad A_g=R_g\mathbin\cup I_g.
                                                               \tag{118}
\]

For `0<=theta<=1`, independently retain each point of `I_g` with
probability `theta`; call the resulting random subset `J_g` and put

\[
                         F_g=R_g\mathbin\cup J_g.               \tag{119}
\]

Every `F_g` is an ordinary convex face, since it is a subset of the source
face `A_g`.

> **Theorem 22 (hidden-ear thinning).**  Under an arbitrary law on exterior
> repair records,
> \[
> \boxed{
> H_2(F)\ge H_2(R\mid p)+\theta H_2(I\mid R,p).}                \tag{120}
> \]
> Moreover
> \[
> \boxed{
> \mathbb E|F|=\mathbb E|R|+\theta\mathbb E|I|,\qquad
> \log_2 Z_P(1/2)\ge H_2(F)-\mathbb E|F|.}                     \tag{121}
> \]
> In particular some rank slice of the ordinary convex-face complex has
> size at least `2^{H_2(F)}/(r+1)`.

**Proof.**  Let `S` be an independent Bernoulli-`theta` subset of the
ambient ground set, so `J=I intersection S`.  For any random subset `X` and
side information `Z`, the chain rule in a fixed order of the ground set
gives

\[
 \begin{split}
 H_2(X\cap S\mid Z)
 &\ge H_2(X\cap S\mid S,Z)\\
 &=\mathbb E_S H_2(X_S\mid Z)\\
 &\ge\theta H_2(X\mid Z).                                      \tag{122}
 \end{split}
\]

For the last inequality, expose the selected coordinates in ground-set
order.  Conditional on fewer preceding coordinates, the entropy of the
current coordinate is at least its entropy conditional on all preceding
coordinates; each coordinate is selected with probability `theta`.

Apply (122) conditionally on `(R,p)`.  More geometry is retained than the
inequality itself records.  Since every point of `I` is hidden by `p`,

\[
                    \operatorname{ext}(F+p)=R+p.                \tag{123}
\]

Thus `(F,p)` recovers `R=ext(F+p)-p` and then `J=F-R`.  Consequently

\[
 \begin{split}
 H_2(F)&\ge H_2(F\mid p)=H_2(R,J\mid p)\\
       &=H_2(R\mid p)+H_2(J\mid R,p)\\
       &\ge H_2(R\mid p)+\theta H_2(I\mid R,p),
 \end{split}
\]

which proves (120).  The rank identity in (121) is immediate.  For the
partition-function bound, nonnegativity of relative entropy against the
law assigning mass `2^{-|Q|}/Z_P(1/2)` to a convex face `Q` gives
`H_2(F)-E|F|<=log_2 Z_P(1/2)`.  Finally `|F|` has at most `r+1` values, so
`H(F)<=log_2(r+1)+max_s log_2 f_s(P)`.  QED.

This theorem really does retain the **entire** internal hidden-ear law: no
alphabet size, endpoint marginal, or maximum fibre replaces
`H(I|R,p)`.  It is also exactly compatible with a multilevel descent,
because thinning a hidden convex face again produces an ordinary convex
face and the expected rank drops by `(1-theta)E|I|`.

Nevertheless, retained-core thinning alone cannot close the mixed branch.
The obstruction is already the genuine one-microblock repair rectangle in
a vertical product.  Let `R` have `N` possible retained words, let the
hidden point `I={x}` have `M` lower choices in one block, and let the
outward blocker `p` have `M` upper choices in the same block.  Take all
`NM^2` repair triples.  These are actual exterior singleton-ear repairs;
the witness source obtained by using `p` shares the full preceding boundary
prefix, so they satisfy the correlation in Theorem 20.

For this rectangle

\[
 \log_2|\mathcal G|=\log_2N+2\log_2M,\qquad
 H_2(T)=\log_2N+\log_2M.                                      \tag{124}
\]

The thinned `J` is empty with probability `1-theta` and is each one of the
`M` singleton choices with probability `theta/M`.  Hence

\[
 H_2(F)=\log_2N+h_2(\theta)+\theta\log_2M
       \le\log_2\{N(M+1)\}.                                  \tag{125}
\]

The last bound is sharp, at `theta=M/(M+1)`.  Thus all thinned retained-core
faces together with all repaired targets still have only `NM+O(N)`
entropy capacity against `NM^2` records.  The missing factor `M` is exactly
the adjacent-cell/two-ended pool.  Equations (120)--(125) therefore kill a
pure Shannon-thinning solution while isolating the remaining requirement:
the hierarchical tangent recurrence must multiply the retained-core
thinning law by a compatible blocker law before the blocker is forgotten.

## 20. Entropy-density stability gives weighted repair rectangles

The near-equality case of Proposition 21 has an exact information-theoretic
form.  It supplies the dense rectangles suggested by DRC with only the
desired subexponential loss.  It does **not** by itself turn them into
two-ended convex targets; the singleton product cell is a sharp correlated
counterexample to that last implication.

Regard the injective record image as a simple bipartite support graph

\[
              \mathcal G\subseteq\mathcal T\times\mathcal I             \tag{126}
\]

and put the uniform law on its edges.  Write

\[
 R_0=r+1,\quad \rho={\log_2|\mathcal G|\over R_0},\quad
 \tau=\mathbb E|T|,\quad\kappa=\mathbb E|I|,
 \qquad \tau+\kappa=R_0.                                      \tag{127}
\]

> **Theorem 23 (near-product stability).**  Suppose neither marginal
> component has entropy density more than `epsilon` above the record
> density:
> \[
> H_2(T)\le(\rho+\epsilon)\tau,
> \qquad H_2(I)\le(\rho+\epsilon)\kappa.                       \tag{128}
> \]
> Then
> \[
> \boxed{I(T;I)\le\epsilon R_0.}                              \tag{129}
> \]
> If `T'` and `I'` are sampled independently from the two edge marginals,
> then
> \[
> \boxed{
> \Pr\{(T',I')\in\mathcal G\}\ge2^{-\epsilon R_0}.}          \tag{130}
> \]
> Moreover, for two independent marginal samples on each side, the
> probability that all four cross pairs belong to `mathcal G` is at least
> \[
> \boxed{2^{-4\epsilon R_0}.}                                 \tag{131}
> \]

**Proof.**  By injectivity and (116k),

\[
 \begin{split}
 I(T;I)&=H_2(T)+H_2(I)-H_2(T,I)\\
 &\le(\rho+\epsilon)(\tau+\kappa)-\rho R_0
 =\epsilon R_0,
 \end{split}
\]

proving (129).  Let `P` be the uniform-edge joint law, let
`Q=P_T tensor P_I`, and let `E` be the event that a pair lies in the support
graph.  Then `P(E)=1`, while `Q(E)=q` is the probability in (130).
Data processing of relative entropy through the indicator of `E` gives

\[
 I(T;I)=D_2(P\Vert Q)\ge D_2(1\Vert q)=\log_2(1/q),            \tag{132}
\]

so (129) proves (130).

For completeness, the weighted `C_4` inequality loses no additional
structure.  If `a(t,i)` is the support indicator and expectations use the
two marginal laws, then

\[
 \begin{split}
 &\mathbb E_{i_1,i_2}
    \left(\mathbb E_t a(t,i_1)a(t,i_2)\right)^2\\
 &\quad\ge
 \left\{\mathbb E_t\left(\mathbb E_i a(t,i)\right)^2\right\}^2
 \ge q^4.                                                       \tag{133}
 \end{split}
\]

The left side is exactly the probability that all four edges of the
sampled rectangle occur.  Equations (130) and (133) prove (131).  QED.

The component-surplus alternative in (128) really can be fed back into the
rankwise argument without an unproved regularization step.

> **Lemma 24 (density-preserving rank slice).**  Let `X` be any random
> convex face of rank at most `r`, and put `m=E|X|>0`.  Then some positive
> rank `k` in its support satisfies
> \[
> \boxed{
> {\log_2|\operatorname{supp}(X\mid |X|=k)|\over k}
> \ge {H_2(X)-\log_2(r+1)\over m}.}                         \tag{134}
> \]

**Proof.**  Put `K=|X|` and let the maximum on the left be `D`.  The entropy
chain rule gives

\[
 H_2(X)=H_2(K)+\sum_k\Pr(K=k)H_2(X\mid K=k)
       \le\log_2(r+1)+D\mathbb E K.                         \tag{135}
\]

Rearrange.  QED.

Thus a marginal density at least `rho+epsilon` yields a genuine uniform
rank family of essentially that density.  When its expected rank is
`Theta(r)`, the loss is `O(log r/r)=o(1)` density.  Even along at most `r`
nested descents, all rank-slicing losses total only `O(r log r)` bits,
which is `o((log n)^2)` when `r=Theta(log n)`.  The component-surplus branch
is therefore stable at the leading-coefficient scale; it is not the source
of a constant entropy leak.

Thus taking `epsilon=o(1)` gives an entropy-near-product support and
compatible repair rectangles with only `2^{o(r)}` weighted loss.  This is
the strongest conclusion available from entropy-density stability alone.
It already eliminates unstructured sparse support as the final
obstruction: a hard family must either have a component-density surplus to
recurse on, or contain subexponentially dense repair rectangles.

The remaining geometric implication is exactly false without adjacent-cell
variation.  In the outward singleton-ear product rectangle used in
(124), the variables

\[
                         T=(R,p),\qquad I=\{x\}                 \tag{136}
\]

are independent under the full `N times M times M` record law.  Hence
`I(T;I)=0`, (130) and (131) both hold with equality one, and all records
lie in a single rooted tangent replacement cell.  The records also satisfy
the full Theorem 20 correlation: `p` is an outward successor, the source
using `p` is a common-prefix witness, and `p` hides precisely `x`.
Nevertheless its two direct projection families in (124) have only `NM`
source faces and `NM` repaired faces.  No multiplication follows inside
that exact cell; in the full product construction the missing factor `M`
comes from forward pairs between neighbouring endpoint cells.

Consequently neither mutual-information stability, weighted DRC, nor a
common exact tangent cell proves compatible two-ended multiplication.  The
rigorous residual after Theorem 23 is narrower:

\[
 \boxed{
 \begin{minipage}{0.84\linewidth}
 Route the weighted `C_4` rectangles of (131) across their ordered tangent
 cells.  Cross-cell rectangles must spend as forward two-ended targets;
 mass trapped in one cell must descend to its rooted child with the full
 thinning law (120), and the total child reuse must be `2^{o(r)}`.
 \end{minipage}}                                                \tag{137}
\]

The ramp--plateau profile is the multilevel equality test for (137): it
keeps resetting the dense rectangle into a neighbouring nested cell.  The
long parabolic prefix is the other equality test: it keeps one cell but
releases the Boolean prefix complex.  Theorem 23 proves the entropy/DRC
half of (137); ordered tangent recovery and global child reuse remain open.

### Linear complete fans at quadratic entropy scale

The weighted rectangle conclusion can be amplified to a complete fan of
linearly many distinct ears without regularizing either marginal.  The
price is only `2^{-o(r^2)}` in the near-product regime, so no leading
source entropy is lost.

> **Theorem 25 (weighted DRC/fixed-component dichotomy).**  Let `G` be a
> bipartite support graph with probability measures `mu,nu` on its two
> sides and product edge density
> \[
>                         q=\Pr_{\mu\times\nu}\{(X,Y)\in G\}.  \tag{138}
> \]
> For every integer `t>=2`, at least one of the following holds:
>
> 1. some right vertex has `nu`-mass at least
>    \[
>                    {q^t\over2\binom t2};                    \tag{139}
>    \]
> 2. there are `t` distinct right vertices whose common left neighborhood
>    has `mu`-mass at least `q^t/2`.
>
> The reflected alternative holds with left and right exchanged.

**Proof.**  For a left vertex `x`, let
`d(x)=nu(N(x))`.  If `Y_1,...,Y_t` are independent `nu`-samples, then

\[
 \mathbb E\,\mu\{N(Y_1)\cap\cdots\cap N(Y_t)\}
 =\mathbb E_\mu d(X)^t\ge q^t.                               \tag{140}
\]

Put `c=sum_y nu(y)^2`.  If
`c>=q^t/(2 binom(t,2))`, then `max_y nu(y)>=c`, proving alternative 1.
Otherwise the union bound shows that the sampled `t`-tuple has a repeated
entry with probability less than `q^t/2`.  Its contribution to (140) is at
most that probability.  Distinct tuples therefore contribute at least
`q^t/2`, so one of them has common-neighborhood mass at least `q^t/2`.
This is alternative 2.  Reflection proves the last assertion.  QED.

Apply this after Theorem 23.  If `q>=2^{-epsilon r}` with
`epsilon=o(1)` and `t=floor(eta r)` for fixed `eta>0`, every mass in
(139)--(140) is at least

\[
                 2^{-\eta\epsilon r^2-O(\log r)}=2^{-o(r^2)}. \tag{141}
\]

For the actual uniform record law, a marginal mass is exactly the fraction
of repair records incident with that component.  Thus alternative 1 fixes
one hidden ear (or, after reflection, one retained target) while retaining
`log|G|-o(r^2)` record bits.  Alternative 2 gives `Theta(r)` **distinct**
hidden ears and a left subfamily of the same quadratic record scale such
that every retained target in that subfamily repairs with every selected
ear.  Because a target in Theorem 20 canonically contains its prefix and
blocker, each row of this complete fan has a common outward-successor
prefix/blocker and `t` interchangeable hidden suffix intervals.  No
ambient-label decoder is reintroduced.

The theorem is sharp against both equality tests.  A product-grid cell
falls in alternative 2: its coordinate ears have a large common retained
word neighborhood, and the eventual payment is the forward pair of two
coordinate fans.  A long nested parabolic prefix may repeatedly fall in
alternative 1; fixing the ear/target preserves the nested prefix, whose
Boolean face complex is the required recursive credit.  Therefore weighted
DRC itself loses no quadratic entropy.  A tempting next statement would be
“forward outer-cell targets or a nested marginal prefix.”  The following
ACP-correlated construction shows that this is still too strong.

> **Proposition 26 (fixed-outer-cell long-ear product).**  For arbitrary
> integers `a,b,M>=2`, there is a planar outward-successor repair family
> with
> \[
> |\mathcal R|=M^a,\qquad |\mathcal I|=M^b,qquad
> |Y|=M,qquad |\mathcal G|=M^{a+b+1},             \tag{142}
> \]
> such that every triple `(R,I,p)` in the full product is a repair record,
> the record map has
> \[
>                         T=(R,p),\qquad T\perp I,              \tag{143}
> \]
> and all variation in `R` and `I` is internal: the root chord and the two
> immediate endpoint neighbours on both arcs are fixed.  If `a,b` tend to
> infinity, then, up to `O(1)` fixed vertices,
> \[
> \begin{split}
> r&=a+b+O(1),& |T|&=a+O(1),& |I|&=b+O(1),\\
> H_2(T)&=(a+1)\log_2M,&H_2(I)&=b\log_2M,&
> {\log_2|\mathcal G|\over r+1}&=(1+o(1))\log_2M. \tag{144}
> \end{split}
> \]
> Thus both marginal entropy densities saturate the record density and the
> mutual information is exactly zero, while no endpoint-neighbour variation
> is available at the outer cell.

**Construction.**  Start with a strict convex polygon written as two arcs
between fixed roots `u,v`.  On the retained arc keep the roots and their
immediate neighbours fixed, and replace `a` internal macrovertices by
sufficiently small disjoint `M`-point clusters.  Do the same with `b`
internal macrovertices of the opposite, hidden arc.  Choose the macrogeometry
so the entire hidden arc lies strictly inside the triangle cut off by one
outer apex `p_0`, while the retained arc lies on the other boundary of the
polygon.  Replace `p_0` by a sufficiently small `M`-point cluster `Y`.

For an explicit macrogeometry take

\[
 u=(-1,0),\qquad v=(1,0),\qquad p_0=(0,4),          \tag{142a}
\]

put the hidden macrovertices on the strict upper arc
`y=1-x^2`, and the retained macrovertices on the strict lower arc
`y=x^2-1`, with `-1<x<1`.  These arcs form the boundary of a strictly
convex lens.  Also

\[
        1-x^2<4(1-|x|)\qquad(-1<x<1),              \tag{142b}
\]

so every hidden macrovertex is strictly inside
`conv{u,v,p_0}`, whereas every retained internal macrovertex lies below
the chord `uv`.  Hence `p_0` replaces the entire upper arc and retains the
entire lower arc.

Use the anisotropic microclusters from the vertical lexicographic
composition, small enough to lie in those neighborhoods.  Strictness and
finiteness ensure that **every** transversal has the same required signs.
Consequently every choice of one point in each retained cluster and each
hidden cluster gives a convex source `A=R union I`; every `p in Y` gives a
convex repaired target `T=R union {p}`; and in `A union {p}` the point `p`
hides the whole consecutive arc `I`.  Rational points in the neighborhoods,
followed by generic perturbation, give a general-position realization.

The same mixed-triple rule makes two selected points in any occupied
internal microblock nonconvex once the fixed preceding and following
macrovertices are present.  Thus unused labels in the `a+b` product blocks
are not convex additions.  Apex labels are repairs, and the witness tail
below has only `O(r)` points, so these sources may also be taken in the
low-addable-degree `O(r)` slice used after (116g').

Finally attach a fixed outer witness tail in the open continuation wedge
after `p_0`.  For every `p in Y`, the polygon consisting of the common fixed
prefix, `p`, and that tail is convex.  Label the first prefix vertex least.
Then `p` is an outward successor of a witness source with the same canonical
prefix, exactly as in Theorem 20.  The immediate neighbours of `u,v` were
not blown up, so all `M^{a+b+1}` records stay in the same outer rooted
tangent cell.  The choices of `R`, `I`, and `p` are independent, proving
(142)--(144).  QED.

This proposition is not an ACP or HTR counterexample.  Its internal
microblocks create precisely the descendant two-ended faces seen in the
product grid; if the clusters themselves carry difficult order types, the
recursion must enter those order types.  What it kills is the claim that
near-product support plus the outward prefix forces **outer** tangent-cell
variation or a one-sided nested chain.  There is a third exact equality
case: both components retain their critical density inside a fixed outer
cell.

The corrected residual theorem must therefore be genuinely hierarchical:

\[
 \boxed{
 \begin{minipage}{0.84\linewidth}
 A near-product complete fan must either spend in a forward rectangle at
 its current tangent scale, release a nested prefix complex, or recurse
 into the internal product coordinates of both components.  Across the
 resulting recursion tree, tangent/prefix descriptions and ordinary target
 reuse must total only `2^{o(r)}` at the capped scale (or `2^{o(r^2)}` for
 a direct coefficient proof).
 \end{minipage}}                                                \tag{145}
\]

Theorems 23 and 25 prove the information-theoretic and DRC part of (145).
Proposition 26 proves that the two-component internal recursion is
indispensable.  Controlling its global target reuse is the remaining gate.

## 21. Two-record uncrossing: an exact local theorem and the nested obstruction

There is a useful way to spend two repair records at once.  It completely
removes blocker degree in a fixed retained cell whenever the two hidden ears
can be uncrossed in one onion layer.

> **Theorem 27 (fixed-core two-record onion uncrossing).**  Fix a retained
> face `R`, and let `G_R` be a family of exterior repair records `(I,p)` with
> source `R union I`, repaired target `R union {p}`, and `|I|<=s`.  For two
> records `g=(I,p)` and `h=(J,q)`, put
> \[
> U(g,h)=ext(I union J),\qquad
> D(g,h)=(I union J)\setminus U(g,h).                 \tag{146}
> \]
> Suppose that
> \[
>                    D(g,h) union \{p,q\}\in F(P)     \tag{147}
> \]
> for every ordered pair in `G_R^2`.  Then, writing `V=|F(P)|`,
> \[
> |G_R|^2\le
> 4(2s+2)^2 3^{2s}V^2.                               \tag{148}
> \]
> In particular the loss is `2^{o(r)}` for ears of size `s=o(r)`.
> For singleton ears no hypothesis is needed and the sharper estimate is
> \[
>                         |G_R|^2\le4V^2.             \tag{149}
> \]

**Proof.**  The extreme-point set of any finite point set is in convex
position, so `U(g,h)` is an ordinary face.  The second component in
(147) is a face by hypothesis.  Map the ordered record pair to these two
faces.

Fix an output `(U,W)`.  There are at most `|W|^2<=(2s+2)^2` ordered choices
for `(p,q)`.  Because blocker labels may also occur in the other record's
ear, there are at most four choices for which of `p,q` also belong to the
hidden remainder `D`; every other element of `W` must belong to `D`.
This reconstructs `S=U union D=I union J`.  Each point of `S` is in `I`
only, `J` only, or both, giving at most `3^{|S|}<=3^{2s}` ordered ear pairs.
The fixed `R` then reconstructs the records, and invalid assignments only
decrease the fibre.  This proves (148).

If both ears are singletons, `I union J` is already a face and `D` is
empty.  The map is simply
`((x,p),(y,q)) -> ({x,y},{p,q})`.  Assigning the two unordered sets to the
two ordered records gives fibre at most four, proving (149).  QED.

There is a complementary result for variable retained cores.  It is the
exact terminal version of the desired forward two-ended splice.

> **Theorem 28 (singleton repair-rectangle forward splice).**  Consider an
> ordered repair `K_{2,2}` with sources
> `A=R_A union {x}`, `B=R_B union {y}` and common blockers `p,q`, where
> each blocker hides the displayed singleton from its source.  Suppose one
> of the two blocker matchings, say `(A,p),(B,q)`, satisfies
> \[
> F=R_A union\{p,y\}\in F(P),\qquad
> G=R_B union\{q,x\}\in F(P),                         \tag{149a}
> \]
> with `y notin R_A union {p}` and `x notin R_B union {q}`.  For any
> family of rank-at-most-`r` rectangles satisfying (149a), the canonical
> choice of a valid matching gives a map to `F(P)^2` of fibre at most
> \[
>                              2(r+1)^4.               \tag{149b}
> \]

**Proof.**  Output `(F,G)` and one implicit bit selecting the first valid
matching.  From `F` guess the ordered distinguished pair `(y,p)`, and from
`G` guess `(x,q)`.  There are at most `(r+1)^4` guesses.  The records are
then forced:

\[
 A=(F\setminus\{y,p\}) union\{x\},\qquad
 B=(G\setminus\{x,q\}) union\{y\}.                   \tag{149c}
\]

Checking the four repair relations and the canonical matching discards all
false guesses.  The matching bit gives (149b).  QED.

Thus a forward terminal-child rectangle has only polynomial global target
reuse even when its two retained cores vary independently.  This is the
two-record analogue of the forward pair pool: the other hidden singleton
is written into each repaired target, so neither prefix/core is forgotten.

The matching count gives a precise terminal dichotomy.  Fix an ordered pair
of sources as in Theorem 28 and a common blocker pool `Q`, and assume that
the hidden singletons `x,y` do not depend on the blocker.  In the separated
case `y notin R_A` and `x notin R_B`, define

\[
\begin{split}
 C_A&=\{p\in Q:R_A union\{p,y\}\in F(P)\},\\
 C_B&=\{p\in Q:R_B union\{p,x\}\in F(P)\}.             \tag{149d}
\end{split}
\]

> **Theorem 29 (terminal forward-or-rotate dichotomy).**  Across any
> collection `Sigma` of such rank-at-most-`r` source-pair states,
> \[
> \sum_{sigma\in Sigma}
> \bigl(|C_A(sigma)||C_B(sigma)|-|C_A(sigma)\cap C_B(sigma)|\bigr)
>       \le (r+1)^4V^2.                                \tag{149e}
> \]
> For each individual state with `d=|Q|` and every `0<tau<1`, either it
> supplies at least `tau^2d^2-d` forward ordered blocker pairs, or one of
> the two directions has at least `(1-tau)d` incompatible blockers.

**Proof.**  The expression in (149e) counts ordered distinct pairs
`p in C_A`, `q in C_B`.  Apply the map in Theorem 28 with this fixed
matching.  Given its two output faces, guessing `(y,p)` in the first and
`(x,q)` in the second gives at most `(r+1)^4` preimages globally, including
the source-pair state.  This proves (149e).  If both compatibility degrees
are at least `tau d`, their product minus the diagonal is at least
`tau^2d^2-d`; otherwise the deficient direction has the asserted number of
incompatible blockers.  QED.

The incompatible alternative has an exact recursive meaning.  If, for
example, `p notin C_A`, put `T=R_A union {p}`.  Then `T` is a face but
`T union {y}` is not.  Either `y in conv(T)` (the interior-containment
branch), or `y` is exterior and

\[
                  T\longmapsto ext(T union\{y\})       \tag{149f}
\]

is a new exterior repair step with blocker fixed to the other ear.  Every
exterior step strictly increases its convex hull by inclusion:

\[
 conv(T)\subsetneq conv(T union\{y\})
          =conv(ext(T union\{y\})).                    \tag{149g}
\]

Consequently exterior rotations cannot cycle.  Along a rotation chain each
new blocker is a fresh ambient label, because a point inside an earlier
hull remains inside every later hull and can never again be exterior.  A
chain therefore has length at most `n`.  This proves the needed monotone
potential, but `n` is exponential at the ACP rank scale; acyclicity alone
does not give the required subexponential global reuse bound.

Rank-preserving singleton rotations nevertheless release an exact amount
of ordinary downclosure mass.  If

\[
 T_0\longmapsto T_1\longmapsto\cdots\longmapsto T_m,
 \qquad |T_i|=r,                                      \tag{149h}
\]

is such a chain, then

\[
 \left|\bigcup_{i=0}^m2^{T_i}\right|
              \ge 2^r+m2^{r-1}.                      \tag{149i}
\]

Indeed the label added in step `i` belongs to no earlier `T_j`, so every
one of the `2^{r-1}` subsets of `T_i` containing that label is new.  The
bound is sharp when all targets share an `(r-1)`-point core and have fresh
tips.  At `r>= (log_2 n)/2`, one fresh layer already has the order of the
capped demand `n/2^r`.  What remains nonlocal is reuse between different
rotation chains; (149i) by itself cannot multiply this credit by the number
of incoming sources.

There is an important scale distinction.  Let `G_{<=s}` be **all** repair
records of rank at most `r` whose hidden ear has size at most `s`.  Sending
a record to its repaired target gives the unconditional global estimate

\[
 |G_{\le s}|\le
 r\left(\sum_{j=1}^s\binom nj\right)V.                \tag{149j}
\]

Indeed, from a target choose its blocker in at most `r` ways and its hidden
ear in the displayed number of ways; the source is then forced and can be
verified.  In particular singleton terminal records satisfy
`|G_{<=1}|<=rnV`.  If `log_2 n=Theta(r)` and `s=o(r)`, the logarithm of the
loss in (149j) is `o(r^2)`.  Thus short terminal ears are already harmless
for the direct quadratic-entropy proof of the Erdős 838 coefficient.  They
remain nontrivial only for the stronger capped Hall/ACP goal, which needs a
`2^{o(r)}` rather than a `2^{o(r^2)}` decoder.

The fresh-tip argument has a useful global bounded-multiplicity form.

> **Lemma 30 (marked downface reuse).**  Let `E` be a multiset of exterior
> rotation edges with target faces `U_e`, marked inserted labels
> `a_e in U_e`, and `k<=|U_e|<=r`.  If every ambient label is the mark of at
> most `M` edges (counting multiplicity), then
> \[
>                  |E|\le rM2^{1-k}V.                 \tag{149k}
> \]

**Proof.**  Edge `e` supplies at least `2^{k-1}` downfaces of `U_e`
containing `a_e`.  If an ordinary face `S` is supplied by an edge, its mark
lies in `S`; hence `S` is counted at most
`sum_{a in S}m(a)<=rM` times.  Double counting these incidences proves
(149k).  QED.

Thus light inserted labels have no cross-chain reuse problem.  The only
obstruction is a label used by exponentially many different bases, which
is exactly a fixed-blocker/component recursion.  The qualification is
essential: in a quadratic-entropy family there are only `n=2^{Theta(r)}`
labels, so large absolute mark multiplicity is unavoidable.  Lemma 30
closes the light part of a heavy/light split but does not itself give the
Kraft inequality for repeated heavy labels across a prefix tree.

The correct statement must count the discarded history attached to a bare
insertion incidence.  Let `Omega` be a multiset of histories, and suppose
each `omega` projects to `(B_omega,x_omega)`, where `|B_omega|=k` and
`x_omega notin B_omega` and `B_omega union {x_omega}` is a face.  For
`0<=t<=k` and `|S|=k-t`, define

\[
 \lambda_t(x,S)=|\{\omega:x_\omega=x, S\subseteq B_\omega\}|,
 \quad \Lambda_t=\max_{x,S}\lambda_t(x,S),\quad W=|\Omega|.   \tag{149l}
\]

> **Theorem 31 (weighted codimension shadow or common prefix).**  The
> ordinary faces
> \[
>       (B_\omega\setminus D) union\{x_\omega\},
>                    \qquad |D|=t,                   \tag{149m}
> \]
> include at least
> \[
>       {W\binom kt\over(k-t+1)\Lambda_t}             \tag{149n}
> \]
> distinct sets.  Moreover, for every `theta>0`, the number of pairs
> `(x,S)` with `lambda_t(x,S)>=theta W` is at most
> \[
>                         {\binom kt\over\theta}.      \tag{149o}
> \]

**Proof.**  Counting histories with multiplicity, (149m) has
`W binom(k,t)` incidences.  From an output face `F`, choose its distinguished
label `x` in at most `k-t+1` ways.  The remaining set is `S=F-x`, and the
total attached-history weight of compatible bases is at most
`lambda_t(x,S)<=Lambda_t`.  This proves (149n).  Finally

\[
        \sum_{x,S}\lambda_t(x,S)=W\binom kt,
\]

because every history contains exactly `binom(k,t)` eligible prefixes.
Markov's inequality gives (149o).  QED.

The count has an integral routing form.  In the bipartite graph from
histories to their faces (149m), every history has degree `binom(k,t)` and
every face has degree at most `(k-t+1)Lambda_t`.  Hall's theorem after
duplicating each face therefore gives a map from histories to ordinary
faces of maximum fibre

\[
 K_t=\left\lceil{(k-t+1)\Lambda_t\over\binom kt}\right\rceil . \tag{149n'}
\]

Thus the weighted-shadow branch really closes whenever `K_t=2^{o(r)}`;
it is not merely an absolute face count.  Failure fixes a label-prefix atom
whose attached-history weight is large compared with the complete
codimension-`t` reservoir.

For the long-chain branch one should use the whole insertion alphabet as a
code.  Suppose history `omega` has an allowed set `X_omega`, with
`B_omega union {z}` a face for every `z in X_omega`, and put
`z notin B_omega` for these labels, and put `h=min_omega|X_omega|`.  Define

\[
 \lambda_t(z,S)=|\{\omega:z\in X_\omega, S\subseteq B_\omega\}|,
 \qquad\Lambda_t=\max_{z,S}\lambda_t(z,S).            \tag{149n''}
\]

Connecting `omega` to every face
`(B_omega\setminus D) union {z}` with `|D|=t` and `z in X_omega` gives
left degree at least `h binom(k,t)` and right degree at most
`(k-t+1)Lambda_t`.  The same duplicated-Hall proof therefore gives a map
of fibre

\[
 K_t^{\rm alph}\le
 \left\lceil{(k-t+1)\Lambda_t\over h\binom kt}\right\rceil .   \tag{149n'''}
\]

This is the precise contribution of a long insertion-poset chain: although
two comparable labels cannot occur together over `B`, its `h` singleton
alternatives are `h` valid code symbols.  The light branch closes whenever
the product `h binom(k,t)` absorbs the attached blocker/history load.
Failure fixes a common admissible insertion label `z` and a common prefix
`S`, which is exactly the heavy nested state rather than an uncontrolled
target collision.

In the strongest DRC-fan localization the alphabet is common:
`X_omega=X` for every history.  Then `lambda_t(z,S)` is independent of
`z`; choose one canonical `z_0 in X`.  Also

\[
             \sum_S\lambda_t(z_0,S)=W\binom kt.       \tag{149n''''}
\]

Consequently the number of prefixes with
`lambda_t(z_0,S)>=theta W` is at most `binom(k,t)/theta`, with **no factor
`h`**.  The light histories route with

\[
       K_t^{\rm alph}\le { (k-t+1)\theta Wover
                                      h\binom kt}+1,  \tag{149n'''''}
\]

while a heavy prefix retains `theta W` histories, fixes the canonical
insertion label at no entropy cost, and descends with (149r)'s exact cap
compensation.  Thus (149n''''--149n''''') close the long-chain branch if
the complete fan really localizes to one common insertion alphabet and
`W/(h binom(k,t))=2^{o(r)}`.  Verifying those two hypotheses for the
attached two-record blocker rows is the remaining interface, not a further
prefix-tree counting problem.

The single-mark form has the right heavy-state iteration.  At rank `k`, take

\[
 t=\lceil\sqrt k\rceil,
 \qquad\theta_k=2^{-k^{2/3}}.                         \tag{149p}
\]

The histories which lie in a heavy atom may be assigned canonically to at
most

\[
 2^{k^{2/3}+O(\sqrt k\log k)}=2^{o(k)}              \tag{149q}
\]

states, each fixing an insertion label and a common prefix of size `k-t`.
Repeating only the heavy alternative changes ranks as
`k,sqrt(k),k^{1/4},...`; the logarithms of all state counts sum to
`O(r^{2/3}+sqrt(r)log r)=o(r)`.  Thus the entire all-heavy recursion has
only `2^{o(r)}` tags.

The geometric cap compensation is exact **while the recursion stays in the
same insertion edge**.  If `x<=_e y`, then
`ext(B union {x,y})=B union {y}`: every vertex of `B`, and hence the fixed
prefix `S`, survives.  Every residual child face
`C subseteq (B\setminus S) union {y}` therefore produces the `2^{|S|}`
distinct ordinary faces

\[
                         C union S',\qquad S'\subseteq S.       \tag{149r}
\]

The multiplier is `2^{k-t}`, exactly the increase from the rank-`k` cap to
the rank-`t` cap.  Consequently the heavy part of the long insertion-chain
branch is closed, conditional only on carrying the insertion-edge state.
The remaining part of Theorem 31 is the light weighted-shadow branch: its
outputs have controlled history congestion, but they still must be coupled
to the second record's blocker code rather than used as an absolute face
reservoir.

The same-edge qualification cannot be dropped.  Let

\[
\begin{split}
 B&=\{(-2,0),(2,0),(0,-2)\},\\
 x&=(1/10,1),\qquad y=(-1/10,3),\qquad z=(-5,1/5).     \tag{149s}
\end{split}
\]

Both `B+x` and `B+y` are convex, and `x<=_e y` across the upper edge of
`B`; adding `y` hides only `x` and retains all of `B`.  But the next
insertion `z` is at a different edge:

\[
 ext(B union\{y,z\})=(B\setminus\{(-2,0)\}) union\{y,z\}.       \tag{149t}
\]

Thus a prefix containing `(-2,0)` is destroyed and cannot be tensored back
into the child face.  The six points are in general position.  A global
proof must either spend when the insertion edge changes or carry the
eroded-prefix labels in the two-record state.

The tempting way to avoid that edge switch is to put two antichain
reservoirs on the two edges adjacent to a deleted corner.  That statement
is false in the strongest possible local sense.  Take

\[
 B=\{u=(0,0),v=(10,0),w=(10,10)\},
 \quad X=\{x=(9,-5)\},
 \quad Y=\{y=(19,3),z=(15,1)\}.                    \tag{149u}
\]

Here `x` inserts across `uv`; both `y,z` insert across `vw`; and `B union Y`
is convex, so `Y` is an antichain in that insertion cell.  Nevertheless

\[
 ext((B\setminus\{v\})\mathbin\cup X\mathbin\cup Y)
                         =\{u,x,y,w\},              \tag{149v}
\]

because

\[
             z={6\over61}u+{13\over61}x+{42\over61}y.          \tag{149w}
\]

All six integer points are in general position.  More strongly, adjoining
**any two** of `x,y,z` to `B-v` gives a convex face.  Thus the residual is
not a missed comparison in the new-edge insertion poset: it is a genuine
three-way rank-three circuit.  In particular, pairwise antichain data are
not a flag condition after an adjacent corner is removed.

There is a clean repair which makes adjacency completely irrelevant.  The
two endpoint reservoirs should be put in two **different output faces**.
The following weighted statement includes the discarded histories, rather
than silently treating a bare base as recoverable.

> **Theorem 32 (separated-reservoir symmetric Hall code).**  For
> `i=1,2`, let `Omega_i` be a multiset of histories.  History `omega` has a
> convex `k_i`-set `B_omega` and a `q_i`-set `X_omega`, disjoint from
> `B_omega`, such that
> \[
>        B_omega\mathbin\cup E\quad\hbox{is a face for every}
>        \quad E\subseteq X_omega,\quad |E|\le2.     \tag{149x}
> \]
> Fix `0<=t_i<=k_i`, put
> \[
> d_i=\binom{k_i}{t_i}s(q_i),\qquad
> s(q)=1+q+\binom q2,                                \tag{149y}
> \]
> and let `Delta_i` be the maximum, over ordinary faces `F`, of the number
> of histories `omega` for which
> \[
> F=(B_omega\setminus D)\mathbin\cup E,qquad
> |D|=t_i,quad E\subseteq X_omega,quad |E|\le2.     \tag{149z}
> \]
> Then there is a map from `Omega_1 times Omega_2` to ordered pairs of
> ordinary faces with maximum fibre
> \[
>       K=\left\lceil{\Delta_1\Delta_2\over d_1d_2}\right\rceil,
> \qquad |\Omega_1||\Omega_2|\le K V(P)^2.          \tag{149z'}
> \]

**Proof.**  Join a history to all the faces in (149z).  The choices are
distinct because `B_omega` and `X_omega` are disjoint, so every left degree
is exactly `d_i`; every right degree is at most `Delta_i`.  In the product
of the two graphs, left degree is `d_1d_2` and right degree is at most
`Delta_1Delta_2`.  Hence for every set `A` of left vertices,

\[
 d_1d_2|A|\le \Delta_1\Delta_2|N(A)|
                         \le Kd_1d_2|N(A)|.
\]

Hall's theorem after replacing every right vertex by `K` copies gives the
claimed routing.  Every output in (149z) is a subset of the face in (149x),
so it is an ordinary convex face.  QED.

The theorem deliberately permits **variable** alphabets `X_omega`; their
actual target collision is exactly what `Delta_i` measures.  In a common
factorized row, it specializes to the proposed four-symbol code.  Namely,
suppose side `i` consists of base histories `h`, an original endpoint
symbol `x in X_i`, and a blocker `p in Y`, where `|X_i|=q_i`, `|Y|=y`, and
put

\[
 \Lambda_i=\max_S|\{h:S\subseteq B_h,\ |S|=k_i-t_i\}|.        \tag{149z''}
\]

Then `Delta_i=q_i y Lambda_i`, and (149z') becomes

\[
 K=\left\lceil
 {q_1q_2y^2\Lambda_1\Lambda_2\over
  s(q_1)s(q_2)\binom{k_1}{t_1}\binom{k_2}{t_2}}
 \right\rceil .                                     \tag{149z'''}
\]

For retained/recoverable bases take `t_i=0,Lambda_i=1`.  Equivalently,
enumerate a code

\[
 (x_1,x_2,p_1,p_2)\longmapsto(E_1,E_2),
 \quad E_i\in\binom{X_i}{\le2}.                     \tag{149z''''}
\]

Its optimal maximum fibre is the ceiling of
`q_1q_2y^2/[s(q_1)s(q_2)]`.  If `q_1=q_2=y`, this is at most four.  The first
output is `B_{h_1} union E_1` and the second is
`B_{h_2} union E_2`; no convex face ever contains labels from both endpoint
cells.  Thus adjacent, nonadjacent, or even unrelated insertion edges are
handled identically.

This is also the exact normalized-light closure of Theorem 31.  A
same-edge antichain supplies (149x), codimension prefixes supply the two
binomial factors, and the definition

\[
              \Delta_i\le 2^{o(r)}d_i              \tag{149z'''''}
\]

immediately gives a `2^{o(r)}` two-record fibre.  Splitting by the two
boundary edges and dyadic size classes costs only `r^{O(1)}`.  The former
nonadjacency restriction was solely an artefact of trying to put both
reservoirs in one output face.

One must not replace the actual collision parameter `Delta_i` by an
unproved common-alphabet pigeonhole.  There is a scalable planar obstruction
to doing so.  Let `N=2^k`, `q=2^{\lfloor k/2\rfloor}`, and put the `N`
points `(j,j^2)`, `0<=j<N`, in convex position.  Fix a `(k-2)`-set `S` of
points in the last quarter.  For every start `a` in the first quarter with
`a+q+1<N/2`, put

\[
 B_a=S\mathbin\cup\{(a,a^2),(a+q+1,(a+q+1)^2)\},
 \quad
 X_a=\{(j,j^2):a<j<a+q+1\}.                         \tag{149z''''''}
\]

The two displayed endpoints are consecutive in `B_a`, and `X_a` is the
entire `q`-point insertion interval across their edge.  Every subset of it
is compatible.  After deleting the two endpoints, however, every history
has the same retained prefix `S`.  A row having a common reservoir of size
at least `q/2` can contain at most `q/2+1` consecutive starts, since

\[
 \left|\bigcap_{a\in A}X_a\right|
                  =\max\{0,q-(\max A-\min A)\}.      \tag{149z'''''''}
\]

Covering the `Theta(N)` starts therefore needs
`Omega(N/q)=2^{k/2-O(1)}` rows.  All points are rational and no three are
collinear.  This is not an ACP counterexample--the ambient set itself is
convex--but it proves that planar insertion geometry alone cannot
commonize variable endpoint alphabets with `2^{o(k)}` loss.  Theorem 32
avoids commonization in the light branch; a heavy value of `Delta_i` is the
precise remaining recursive state.

There is an important protected-frame correction.  For an **actual maximal
insertion cell** across the edge `uv` of a convex base, retain the local
boundary frame

\[
                         (a,u,v,w),                 \tag{149z0}
\]

where `a,u,v,w` are consecutive base vertices.  The region in which `uv`
is the unique violated support edge is determined by these adjacent tangent
halfplanes.  Moreover, for two points in that cell,

\[
                  x\le_{uv}y\quad\Longleftrightarrow\quad
                  x\in\operatorname{conv}\{u,y,v\}.            \tag{149z1}
\]

Thus the full insertion poset, and any canonical Mirsky antichain
partition of it, is determined by the protected frame and the ambient
labelled point set.  In Theorem 32 one may forbid deletion of the at most
four frame vertices, replacing `binom(k,t)` by `binom(k-4,t)`.  At
`t=ceil(sqrt(k))` this costs only a constant factor.  Use only nonempty
endpoint codewords; their capacity is still

\[
                 s_+(q)=q+\binom q2={q(q+1)\over2}\ge{q^2\over2}.       \tag{149z2}
\]

Any endpoint label then identifies its canonical antichain class, while
the cyclic neighbors of the one- or two-point inserted block recover the
frame with at most `k^{O(1)}` guesses.  Consequently the sliding-interval
example above kills **unprotected common-prefix commonization**, but not
recoverability of the canonical maximal-cell reservoir after constant
frame protection.  The remaining heavy state is a genuine long chain or
large actual target collision, not an exponential alphabet tag.

At the weaker quadratic-coefficient scale, there is now a complete and
purely combinatorial conversion from the near-product law to **counted**
repair rectangles.  It avoids the unjustified step from a degree-weighted
`C_4` probability to an unweighted count.

> **Theorem 33 (information-bucket counted rectangles).**  Let `G` be a
> simple bipartite graph with `m>=2` edges.  Under its uniform-edge law let
> the endpoint degrees be `d_X,e_Y`, put `M=log_2m`, and put
> \[
> J=I(X;Y)=\mathbb E\log_2{m\over d_Xe_Y}.           \tag{149za}
> \]
> Define
> \[
> a=J+\sqrt{(J+1)M},\qquad
> \delta={a-J\over a+M}.                            \tag{149zb}
> \]
> Then the ordered `C_4` homomorphism count, with repeated vertices
> allowed, satisfies
> \[
> \boxed{
> \operatorname{hom}(C_4,G)\ge
> {m^2\delta^4,2^{-2a-4}\over(M+1)^8}.}            \tag{149zc}
> \]
> In particular, if `J=o(M)`, then
> \[
>             \operatorname{hom}(C_4,G)
>                         \ge m^2,2^{-o(M)}.        \tag{149zd}
> \]

**Proof.**  Write `Z=log_2(m/(d_Xe_Y))`.  Then `-M<=Z<=M` and
`E Z=J`.  If `gamma=Pr(Z<=a)`, bounding `Z` below by `-M` on this event
and by `a` on its complement gives

\[
 J\ge-\gamma M+(1-\gamma)a,
 \qquad \gamma\ge\delta.                            \tag{149ze}
\]

Thus at least `delta m` edges satisfy `d_Xe_Y>=m2^{-a}`.  Bucket those
edges by the two integer dyadic degree classes.  There are at most
`(M+1)^2` classes, so one resulting subgraph `H` has

\[
 m'=|E(H)|\ge{\delta m\over(M+1)^2}.                \tag{149zf}
\]

If the lower endpoints of its degree buckets are `D,E`, every selected
edge has `d_X<2D,e_Y<2E`, and therefore

\[
                         DE\ge m2^{-a-2}.           \tag{149zg}
\]

Every active left vertex of `H` has original degree at least `D`, so there
are at most `m/D` such vertices; similarly there are at most `m/E` active
right vertices.  The standard two Cauchy--Schwarz proof of Sidorenko for
`C_4` gives, for a bipartite graph with `L,R` active vertices,

\[
 \operatorname{hom}(C_4,H)\ge{m'^4\over L^2R^2}.
\]

Using `L<=m/D,R<=m/E` and (149zf)--(149zg) gives exactly (149zc).
If `J=o(M)`, then `a=o(M)`, while `delta=2^{-o(M)}` (indeed it is at
worst inverse-polynomial when `J=O(1)`).  This proves (149zd).  QED.

Apply this to a fixed-rank repair split `G subseteq T times I`.  Every
ordered support rectangle has two cross-sources

\[
 A_{12}=R_1\mathbin\cup I_2,
 \qquad A_{21}=R_2\mathbin\cup I_1,                 \tag{149zh}
\]

and both are ordinary convex faces.  From their ordered pair, guess the two
blockers in at most `n^2` ways and the two set partitions in at most
`2^{2r}` ways.  Hence

\[
 \#C_4(G)\le n^2 2^{2r}V(P)^2.                     \tag{149zi}
\]

Consequently, when `log n=Theta(r)`, `log m=Theta(r^2)`, and
`I(T;I)=o(r^2)`, Theorem 33 and (149zi) give

\[
                         m\le 2^{o(r^2)}V(P).        \tag{149zj}
\]

This rigorously closes global target reuse in the **near-product branch**;
no degree regularization and no geometric tangent decoder remain there.
It does not, by itself, close the full recursion.  If a component has an
entropy-density surplus, replacing the record family by that one marginal
can discard a constant fraction of the record entropy.  The injection
`G -> (T,I)` uses two faces for one record, while the desired square bound
has only two faces for two records.  Neither Theorems 23--25 nor the bucket
argument supplies the missing pair-valued component recursion.  Thus the
honest coefficient-scale boundary is now:

\[
 \boxed{\text{near-product repair laws are discharged by (149zj); the
 component-surplus branch still needs a two-slot entropy-preserving
 recursion.}}                                      \tag{149zk}
\]

This distinction also explains why (149zi) cannot prove capped RNP: its
`n^2 2^{2r}=2^{Theta(r)}` fibre is negligible compared with `r^2` but can
consume the entire required blocker factor at the `2^{o(r)}` scale.

### The component-surplus branch is genuinely pair-valued

The obstruction can be stated without any asymptotic ambiguity.  The proof
of Theorem 33 works with **any** threshold `a>J`, with
`delta=(a-J)/(a+M)`.  Taking `a=J+1` makes `delta` inverse-polynomial in
`M`, and the cross-source decoder gives, at the coefficient scale,

\[
                    \log_2V(P)\ge M-J-o(M).          \tag{149zl}
\]

On the other hand the two marginal supports are themselves ordinary face
families, so

\[
 \log_2V(P)\ge\max\{H(T),H(I)\}
                    \ge{M+J\over2}.                 \tag{149zm}
\]

These two purely information-theoretic estimates imply only

\[
                    \log_2V(P)\ge(2/3-o(1))M.       \tag{149zn}
\]

The constant `2/3` is sharp for the abstract data.  Take the disjoint union
of `q` copies of `K_{q,q}`.  Then

\[
 m=q^3,qquad H(T)=H(I)=2\log_2q,qquad
 J=\log_2q=M/3.                                    \tag{149zo}
\]

Both (149zl) and (149zm) equal `2M/3`.  Hence no argument using only the
split entropies, marginal face supports, and counted rectangles can produce
a one-face-per-record bound.  It must use additional faces forced by planar
repair geometry.

There is an exact realizable equality test for that additional step.  In a
vertical lens product take `a` retained microblocks of size `M`, `b` hidden
microblocks of size `Q=M^h` with `0<h<1`, and an `M`-point outward blocker
cloud.  The complete repair cell has

\[
 |\mathcal G|=M^{a+1}Q^b,quad
 |\mathcal T|=M^{a+1},quad |\mathcal I|=Q^b,        \tag{149zp}
\]

and split ranks `a+1,b`.  Its target marginal has the strict density
surplus

\[
 {\log|\mathcal T|\over a+1}=\log M
   >{(a+1+b h)\log M\over a+b+1}=ho.              \tag{149zq}
\]

The common prefix, outward successor, and fixed tangent frame are all
present.  Nevertheless, using only source faces, target faces, and
one-occupancy component downfaces leaves an exponential pair deficit:

\[
 \begin{array}{c|c}
 \text{two output types}&|\mathcal G|^2/\text{output-pair capacity}\\ \hline
 \text{source--source}&M^2\\
 \text{target--target}&Q^{2b}\\
 \text{source--target}&M Q^b.
 \end{array}                                         \tag{149zr}
\]

The actual planar complex is harmless precisely because descendant
two-ended faces may occupy two labels in suitable endpoint blocks.  Their
quadratic subset capacity is the symmetric code of Theorem 32.  If the
active endpoint is nested rather than an antichain, the same information is
released only after descending to the next tangent cell.  Thus (149zp)--
(149zr) are not a counterexample to Erdős 838; they are a realizable
counterexample to a **marginal-only** component-surplus recursion.

This identifies the exact theorem still missing.  A valid pair-valued
recursion must retain one open tangent slot in each of its two eventual
faces and prove that every surplus descent either

1. reaches two recoverable antichain reservoirs and invokes Theorem 32, or
2. fixes a protected frame and descends a nested insertion chain without
   allowing histories from different outer cores to merge with
   `2^{Omega(r)}` multiplicity.

The second alternative is the same inter-chain history-reuse gate isolated
by Theorem 31 and the marked-downclosure lemma.  Entropy conservation alone
cannot prove it: the skew product (149zp) satisfies every entropy and prefix
hypothesis while postponing payment to its internal two-ended coordinates.

The correct summation invariant for a future recursion is at least exact.

> **Lemma 34 (recoverable-cell Cauchy telescope).**  Suppose a record family
> is partitioned as `G=disjoint_union_c G_c`.  For every cell there are two
> ordinary face families `A_c,B_c` and
> \[
>                    |G_c|^2\le K|A_c||B_c|.         \tag{149zs}
> \]
> If every ordinary face belongs to at most `L_A` of the families `A_c` and
> at most `L_B` of the families `B_c`, then
> \[
>                    |G|\le\sqrt{K L_A L_B}\,V(P).  \tag{149zt}
> \]

**Proof.**  Sum the square roots in (149zs) and apply Cauchy--Schwarz:

\[
 |G|\le\sqrt K\sum_c\sqrt{|A_c||B_c|}
 \le\sqrt{K\sum_c|A_c|\sum_c|B_c|}
 \le\sqrt{K L_A L_B}\,V(P).                       \tag{149zu}
\]

QED.

Thus an exponential number of entropy cells causes **no** loss if both
eventual output faces recover their cell with subexponential ambiguity.
A protected boundary prefix or a marked consecutive ear has only
`r^{O(1)}` cut ambiguity in the output which retains it.  The unresolved
failure is precisely the other output after a nested repair erases that
ear/prefix.  Theorem 32 supplies both recoverable outputs in an antichain
cell; same-edge chain descent preserves them by (149r); an insertion-edge
switch can erase one, as (149s)--(149t) shows.  Lemma 34 therefore turns the
informal phrase “carry two open slots” into the quantitative target
`K L_A L_B=2^{o(r)}`.

One last exact calculation shows why fixing only one side is insufficient.
Let `d(A)` be the number of selected blockers attached to a fixed source
face `A`.  Two records `(A,p),(A,q)` map to the two ordinary faces

\[
                              (A,\{p,q\}),           \tag{149zv}
\]

with fibre at most two (use the singleton `{p}` when `p=q`).  Therefore

\[
                   \sum_A d(A)^2\le2V(P)^2.         \tag{149zw}
\]

Since the number of active sources is at most `V(P)`, Cauchy--Schwarz gives
only

\[
                         |G|\le\sqrt2,V(P)^{3/2}.   \tag{149zx}
\]

Thus every fixed-source star is completely harmless, but summing the stars
loses exactly one half-power of the source family.  Recovering that power
requires pairing **different** sources while coding both blocker labels
into the same two output faces--precisely the symmetric/two-ended problem,
not another one-sided degree estimate.

Theorem 27 also applies whenever every pairwise ear union is convex,
since then `D` is empty.  Thus it rigorously discharges fixed-core
singleton ears, union-compatible short ears, and any other cell for which
the first onion remainder joins the two blockers convexly.  Unfortunately
(147) is not a consequence of ACP repair correlation.  Two exact failures
show why a multilevel state is unavoidable.

First, even one ear need not join its blocker convexly.  Let

\[
\begin{split}
 R&=\{(-2,0),(2,0),(0,-2)\},\\
 I&=\{(-1,1),(0,3/2),(1,1)\},\qquad p=(0,4).
                                                               \tag{150}
\end{split}
\]

Then `R union I` is a strict convex hexagon and
`ext(R union I union {p})=R union {p}`.  But `(0,3/2)` is strictly inside
`conv{(-1,1),(1,1),p}`, so `I union {p}` is not a face.

More importantly, the first-onion remainder in (146) can itself be a
nested repair pocket.  The following rational, general-position example
has a common retained core.  Put

\[
 R=\{(-3,-9),(3,-9),(0,-12)\}.                         \tag{151}
\]

Let `I` consist of the five points `(x,-x^2)` with

\[
 x\in\{-11/5,-11/10,0,11/10,11/5\},\qquad p=(3/20,20),
                                                               \tag{152}
\]

and let `J` consist of `(x,2-x^2/2)` with

\[
 x\in\{-2,-1,1/10,21/20,41/20\},\qquad q=(-1/5,50).    \tag{153}
\]

Both `R union I` and `R union J` are strict convex octagons, while

\[
 ext(R union I union\{p\})=R union\{p\},\qquad
 ext(R union J union\{q\})=R union\{q\}.              \tag{154}
\]

The hull of `I union J` contains the two endpoints of `I` and all five
points of `J`.  Hence its hidden remainder is

\[
 D=\{(-11/10,-121/100),(0,0),(11/10,-121/100)\}.       \tag{155}
\]

But the hull of `D union {p,q}` consists only of the two endpoints in
(155) and `q`; both the middle point and `p` are hidden.  Thus (147) fails
strictly.  No three of the fifteen displayed points are collinear.

This is the exact two-record form of the long parabolic-prefix obstruction.
Peeling `ext(I union J)` does not release the information: the remainder
and the two blockers reproduce a smaller nested pocket.  Therefore a
successful two-record proof must iterate (146), carrying the blocker pair
through successive onion layers, and prove a Kraft-type bound on reuse of
the terminal two faces.  Stopping after one uncrossing layer is false even
inside one fixed retained cell.

Nor is the forward splice (149a) automatic for a singleton repair `C_4`.
Here is an exact integer, general-position obstruction.  Index the points
`0,...,7` in the following order:

\[
\begin{split}
 &(32400,407678),(33685,283524),(905544,11856),\\
 &(703904,203346),(635399,149950),(640980,67396),\\
 &(138202,791563),(826473,830732).                    \tag{156}
\end{split}
\]

Take `A={2,3,6}`, `B={4,5,7}` and common blockers `0,1`.  Either blocker
hides exactly `x=3` from `A` and exactly `y=4` from `B`.  For both blocker
matchings the augmented `B`-target accepts `x`, but the augmented `A`-target
does not accept `y`: its hull omits `4`.  Hence neither matching satisfies
(149a), despite the sources being disjoint.  The remaining terminal gate
is consequently precise: prove that a large family in which both forward
matchings fail releases nested/common-prefix face mass, or recurse while
retaining enough of the two tangent states to prevent this `C_4` from being
reused exponentially.

A stronger possible shortcut is also false: after one exterior rotation,
the two failed targets need not become comparable.  Take the seven integer
points

\[
\begin{split}
 &(329428,573254),(231876,518007),(756242,536954),\\
 &(969122,458917),(363787,577409),(468465,889102),\\
 &(989247,449299),                                      \tag{157}
\end{split}
\]

indexed `0,...,6`.  Let `A={3,5,6}`, `B={0,1,5}` and use common blockers
`2,4`.  Either blocker hides exactly `x=3` from `A` and exactly `y=0` from
`B`.  For the matching `(2,4)` the repaired targets are

\[
 T=\{2,5,6\},\qquad U=\{1,4,5\}.                       \tag{158}
\]

Both cross additions fail with the added point exterior, and one rotation
gives

\[
 T'=ext(T union\{0\})=\{0,5,6\},\qquad
 U'=ext(U union\{3\})=\{1,3,5\}.                       \tag{159}
\]

None of the four pairs `(T,U),(T',U),(T,U'),(T',U')` has comparable convex
hulls.  The other blocker matching also fails in both directions.  Thus
the complement of the forward-splice graph is not a union of containment
chains, even after one rotation.  The remaining recursion must retain both
tangent directions; a scalar hull-inclusion depth loses essential
two-dimensional state.

## 22. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_acp_proof/acp_proof_audit.py
```

The audit uses exact rational arithmetic.  It checks (1)--(3) coefficientwise
on saved profiles, verifies the two Gordon-collision ACP values in (16), and
checks the exact formulas and linear growth in (18)--(19).  It also performs
99,696 integer exponent checks for Theorem 6, exact parabola certificates
for Lemma 8, and 33,852 integer exponent checks for Theorem 9.  It also
checks 400 exact log-free forms of entropy submodularity and an exact
vertical-product realization of both the saturation (58) and the sunflower
barrier.  It additionally enumerates exact upper and lower rooted chains and
checks the all-or-nothing tangent rectangles in Theorem 13, as well as the
ordered-array identities (75)--(77) on exact finite bipartite graphs and
the arbitrarily deep nested-prefix family (84)--(85).  It also checks the
split-sequence independence and edge bounds (95)--(97) on finite ordered
word families.  Finally, it checks 144 exact integer regimes of the
conditional high/medium row theorem, the quadratic short-word cardinality
barrier, the exponential suffix-trace fibre, and an exact vertical-product
instance in which adjoining one common suffix point destroys a two-ended
target.  It also verifies the exact integer form of the successor
entropy/mean inequality on 27,125 empirical laws and an exact outward
successor which hides the first suffix vertex while preserving the full
common prefix.  Finally it exhausts 589 small bipartite support graphs and
checks the exact support-event KL inequality, the weighted `C_4` lower
bound in Theorem 23, and both orientations of the fixed-component/complete-
fan dichotomy in Theorem 25.  It also exhausts the singleton-ear pair map
on those support graphs, checks its fibre-four bound, and verifies all
strict hull assertions and the absence of collinear triples in
(149s)--(149w) and (151)--(159).  It additionally checks 216 exact symmetric
endpoint codes, the sliding-interval commonization barrier, and the
information-bucket counted-rectangle theorem on 627 small support graphs.
The analytic inequalities
themselves are proved above rather than
inferred from these finite audits.
