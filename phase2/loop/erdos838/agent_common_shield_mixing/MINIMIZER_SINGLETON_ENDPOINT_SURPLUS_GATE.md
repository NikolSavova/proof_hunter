# Minimizer singleton endpoint surplus and the two-anchor circuit gate

## Verdict

The proposed minimizer consequence is correct in every generic affine chart,
and summing it retains an additional cap/cup rank moment.  If `P` is globally
minimal for the number `V(P)` of nonempty ordinary faces among all `n`-point
general-position sets, then, writing

\[
 \ell_x=V(P)-V(P-x),\qquad
 \mu V(P)=\sum_{F\in\mathcal V(P)}|F|,
\]

one has

\[
 \ell_x\le 1+C(P-x),\qquad
 \ell_x\le 1+U(P-x)                                      \tag{1}
\]

for every label `x`.  Consequently, if

\[
 M_C=\sum_{A\in\mathcal C(P)}|A|,qquad
 M_U=\sum_{B\in\mathcal U(P)}|B|,
\]

then

\[
 \boxed{\ \mu V\le n+nC-M_C,\qquad
          \mu V\le n+nU-M_U\ }                           \tag{2}
\]

and in particular

\[
 C,U\ge {\mu V-n\over n},\qquad
 {CU\over V}\ge { (\mu V-n)^2\over n^2V}.                \tag{3}
\]

This is projectively uniform: (1)--(3) hold in every generic chart.  Thus a
polylogarithmic-load cap-times-cup to ordinary-face converter would double
the leading face exponent.  At a quarter-coefficient input, it would give the
desired half coefficient.

What is **not** proved is that the abundant bad cap--cup pairs admit such a
converter.  The exact obstruction is now especially narrow: nonaddable
endpoint incidences carry rooted wrong-sign triples, hence, when an opposite
anchor is genuinely available, rooted `1+3` circuits.  One must use planar
circuit elimination to turn two such physical anchors into either a
decreasing bipartition mutation or a bounded-load ordinary output.  The
singleton inequalities alone do not do this.

## 1. Exact singleton mutation

Fix a generic chart and put `Q=P-x`.  Make a new copy of `Q` and add one
singleton by strong glue, on either side of `Q`.  The exact strong-glue face
formula gives

\[
 \begin{aligned}
 V(Q\prec\{s\})&=V(Q)+1+C(Q),\\
 V(\{s\}\prec Q)&=V(Q)+1+U(Q),                            \tag{4}
 \end{aligned}
\]

up to the harmless convention interchanging the names cap and cup.  Both are
realizable general-position `n`-point sets.  Global minimality of `P` and
`V(P)=V(Q)+\ell_x` prove (1).

The coefficientwise identity for the two mutations is also exact:

\[
 V_k(Q\prec\{s\})=V_k(Q)+\mathbf1_{k=1}+C_{k-1}(Q),       \tag{5}
\]

and analogously with `U`.  But minimality is for the **total** number of
faces, so it compares the sums of (5); it does not imply
`ell_{x,k} <= C_{k-1}(Q)` separately.  No coefficientwise claim is used here.

Summing (1) uses the exact deletion identities

\[
 \sum_x\ell_x=\mu V,
 \qquad
 \sum_x C(P-x)=\sum_{A\in\mathcal C(P)}(n-|A|)=nC-M_C,   \tag{6}
\]

and proves (2).  If `\bar r_C=M_C/C`, then the sharper implicit form is

\[
 C\ge {\mu V-n\over n-\bar r_C},                         \tag{7}
\]

with the symmetric cup statement.  Dropping the nonnegative moments proves
(3).

For a least fixed-gap counterexample the same argument is available after
choosing a globally `V`-minimal member at that cardinality: either singleton
mutation remains below the target and contradicts minimality, or (1) holds.

## 2. Exact bad-extension/slack ledger

There is a useful exact way to expose what (2) leaves unpaid.  Define the
singleton cap slack

\[
 s_C(x)=1+C(P-x)-\ell_x\ge0,qquad S_C=\sum_xs_C(x).
\]

Let `E_C` count ordered dominant-pair tests `(A,x)` for which `A+x` is a cap,
with `x` allowed already to belong to `A` (this is the convention in which a
spanning record retaining `A` and the marked anchor `x` is tested).  Downward
closure gives

\[
 E_C=2M_C-n.                                              \tag{8}
\]

Indeed incidences with `x in A` contribute `M_C`; genuinely new-anchor
extensions contribute `M_C-n`, by deleting one label from every cap of rank
at least two.  Their sum is (8).  If `B_C=nC-E_C` is the number of
nonaddable cap-anchor incidences, then

\[
 \begin{aligned}
 S_C&=n+nC-M_C-\mu V,\\
 \boxed{\ B_C=2\mu V+2S_C-nC-n\ }.                       \tag{9}
 \end{aligned}
\]

The identical formulas hold for cups.  Independently, if cap rank is at
most `R`,

\[
 {E_C\over nC}\le {2R\over n},                           \tag{10}
\]

apart from the favorable singleton correction.  Thus in the live
rank-`O(log n)` slice almost every physical anchor is nonaddable.

For a nonaddable `(A,y)`, some `x`-ordered triple of `A+y` has the wrong cap
sign.  In a genuine two-block/common-guard normal form, adjoining any
available label on the prescribed opposite side makes this a literal rooted
`1+3` bad four-set.  This last implication needs the physical opposite-side
anchor.  It is not a statement about an arbitrary endpoint alphabet.

### 2.1 Two bad anchors still leave both endpoint reservoirs

There is an exact concentration-free strengthening under the same maximum
rank hypothesis.  Put

\[
 b_C(y)=|\{A\in\mathcal C(P):A+y\notin\mathcal C(P)\}|,
 \qquad
 b_U(z)=|\{B\in\mathcal U(P):B+z\notin\mathcal U(P)\}|.  \tag{10a}
\]

Thus `sum_y b_C(y)=B_C`, `sum_z b_U(z)=B_U`, and
`b_C(y)<=C`, `b_U(z)<=U`.  Write

\[
 C_{yz}=C(P-\{y,z\}),\qquad U_{yz}=U(P-\{y,z\}).
\]

If every cap and cup has rank at most `R`, then

\[
 \begin{aligned}
 \sum_{y,z}(C-C_{yz})&\le2nRC,\\
 \sum_{y,z}(U-U_{yz})&\le2nRU.                           \tag{10b}
 \end{aligned}
\]

Indeed a rank-`k` cap is destroyed by exactly
`n^2-(n-k)^2<=2nk` ordered anchor pairs.  Consequently

\[
 \begin{aligned}
 &\sum_{\substack{y,z:\ C_{yz}\ge C/2\\U_{yz}\ge U/2}}
       b_C(y)b_U(z)\\
 &\hspace{25mm}\ge B_CB_U-8nRCU\\
 &\hspace{25mm}\ge (\max\{n-2R,0\}^2-8nR)CU.           \tag{10c}
 \end{aligned}
\]

For the first inequality, weight the cap deficit in (10b) by
`b_C(y)b_U(z)<=CU`.  Anchor pairs with `C_{yz}<C/2` have weighted mass at
most `4nRCU`; the cup-deficient pairs obey the same bound.  For the second,
use `B_C>=max{n-2R,0}C` and `B_U>=max{n-2R,0}U` from (8).
When `R<n/2`, the last expression is the simpler
`(n^2-12nR+4R^2)CU`.

Thus when `R=o(n)`, almost every weighted pair of bad physical anchors still
has at least half of **both** endpoint reservoirs avoiding the two anchors.
This rules out mere anchor concentration as the converter obstruction.  It
does not reattach `y,z`: the surviving cap/cup faces are ordinary faces of
`P-{y,z}`, and their union with the rooted circuits need not be ordinary.
The remaining operation is precisely a three-profile circuit-elimination or
same-configuration reset.

## 3. What a two-anchor converter would immediately give

Let `R_C` and `R_U` be recoverable sets of physical bad cap-anchor and
cup-anchor records in one actual configuration.  Suppose a repair rule maps
at least `delta |R_C||R_U|` composable record pairs to ordinary faces plus
`T` recoverable tags, with decoder load at most `Lambda`.  Then exactly

\[
 V(P)\ge {\delta |R_C||R_U|\over T\Lambda}.               \tag{11}
\]

No Cauchy or geometry is hidden in (11); it is just double counting.  Under
the additional live-branch hypothesis that the full relevant cap and cup
complexes have rank `O(log n)`, (9)--(10) make `R_C,R_U` essentially the full
endpoint rectangles.  Therefore `T Lambda=2^{o((log n)^2)}` would turn the
endpoint product (3) into the required coefficient reset.  Without that rank
hypothesis one must first rank-slice, and (8)--(10) do not by themselves say
that the slice retains the minimizer surplus.

There are two plausible exits:

1. the rooted circuits align with a physical bipartition `R union B` for
   which
   \[
   V(R)+V(B)+C(R)U(B)<V(P),                               \tag{12}
   \]
   contradicting global minimality; or
2. circuit elimination supplies the converter (11).

Neither follows from the scalar endpoint ledger.  They require the actual
rank-three oriented matroid and preservation of both physical anchors.

## 4. Exact calibrations

### 4.1 A true five-point minimizer

The verifier uses

\[
 (6,15),(18,22),(13,4),(12,17),(20,29).
\]

It has `V=26`: the `25` subsets of ranks at most three plus one convex
four-set.  Every five-point general-position set has a convex four-set, so
`26` is globally minimal.  All five singleton inequalities and the moment
identities (2), (6), and (9) hold exactly.

### 4.2 The balanced Pascal wrapper is rejected by singleton minimality

For the exact twelve-point set `T(4,2) prec T(4,2)`, one has

\[
 (C,U,V)=(248,248,1061).
\]

Nevertheless every label violates at least one proposed minimizer inequality.
For the four position classes, `ell_x` is `394,332,332,394`, whereas the
smaller of `1+C(P-x),1+U(P-x)` is respectively `165,179,179,165`.  Thus a
singleton strong-glue mutation already decreases the face number.  This is
stronger and more local than the previously found arbitrary bipartition
mutation of size `688`.

This is important: the balanced half-coefficient Pascal calibration is a
sharp converter barrier, but it is not a counterexample to the
minimizer-specific endpoint theorem.

### 4.3 Scalar sharpness and its limitation

For integers `r>=2`, `q>=3`, let `n=rq-1`, and take `T=1 mod r`.  The formal
uniform ledger

\[
 \begin{gathered}
 C=U=Tn,\quad M_C=M_U=rTn,\\
 \ell_x=1+T(n-r),\quad C(P-x)=U(P-x)=T(n-r),\\
 \mu=r,\quad V={n[1+T(n-r)]\over r}                       \tag{13}
 \end{gathered}
\]

is integral and has equality in every singleton inequality and in (2).
Yet a proportion `1-O(r/n)` of endpoint-anchor incidences are nonaddable,
and any all-pairs converter into at most `V` outputs has average load at least
`C U/V`, which grows linearly with `T` (for fixed `r,q`).

This is deliberately only a scalar/deletion-profile barrier, not a planar
set system.  It proves that no manipulation of (1)--(10) alone can construct
the converter.  A positive next theorem must use circuit elimination,
physical anchor coexistence, or the decreasing mutation (12).

## 5. Scope

Proved here:

- exact singleton minimizer inequalities in every chart;
- exact cap/cup moment strengthening and endpoint-product lower bound;
- exact slack versus bad-extension identities;
- exact two-anchor avoidance of both low-rank endpoint reservoirs;
- exact finite minimizer and nonminimal Pascal calibrations;
- the precise conditional two-anchor decoder inequality.

Not proved here:

- a coefficientwise minimizer inequality;
- that arbitrary wrong endpoint triples share an opposite physical anchor;
- a bounded-load two-anchor converter;
- the global half-coefficient theorem.
