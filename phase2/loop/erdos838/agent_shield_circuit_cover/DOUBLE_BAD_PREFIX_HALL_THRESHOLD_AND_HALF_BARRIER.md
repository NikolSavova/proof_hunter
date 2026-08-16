# Double-bad anchors plus prefix shields: the exact Hall threshold

**Date:** 2026-08-15. All logarithms are base two. This note combines
`agent_common_shield_mixing/TWO_ANCHOR_DOUBLE_CIRCUIT_ELIMINATION_GATE.md`
with `PREFIX_SHIELD_TWO_TARGET_HALL_AGGREGATE_GATE.md`.

## Verdict

The load-one decoder for a double-bad endpoint record is best viewed as an
incidence graph, not as a one-face injection. For a record

\[
                         r=(A,B,y,z),
\]

put

\[
 X_r=A\cup B,
 \qquad
 Y_r=\{a_*(A,y),y,z,b_*(B,z)\}.
                                                               \tag{1}
\]

Both are ordinary faces and the ordered pair \((X_r,Y_r)\) recovers the
record. Let \(M\) be the record mass, let \(p,q\) be the numbers of actual
detached and seam faces, and let

\[
 \kappa=\max_X d(X),\qquad
 \lambda=\max_Y d(Y),\qquad
 \delta=\max_{X,Y}d(X,Y).                                     \tag{2}
\]

The double-circuit theorem gives \(\delta=1\). If \(V=V(P)\) and
\(Q_4\) is the number of available rank-four anchor seams, then

\[
\boxed{
 M\le
 \min\left\{
   \kappa V,\ lambda Q_4,\ \delta VQ_4,
   {\kappa\lambda\over\kappa+\lambda}(V+Q_4)
 \right\}.}                                                   \tag{3}
\]

The last term is an exact fractional Hall routing bound. It assigns every
record to one of its two **ordinary one-face** targets, with tagged load at
most

\[
                         h_2={\kappa\lambda\over\kappa+\lambda}.
                                                               \tag{4}
\]

The two tags cost one bit; no geometric merger is asserted. The harmonic
constant is sharp for complete biregular incidence graphs.

Write

\[
                  \Sigma={C(P)U(P)\over V(P)}                  \tag{5}
\]

and suppose the double-bad records retain a fraction \(\theta\) of the
endpoint product, so \(M\ge\theta\Sigma V\). Then (3) becomes the exact
closure threshold

\[
\boxed{
 \theta\Sigma\le
 \min\left\{
  \kappa,\ {\lambda Q_4\over V},\ \delta Q_4,
  h_2\left(1+{Q_4\over V}\right)
 \right\}.}                                                   \tag{6}
\]

In the strong-glue endpoint state one always has \(\kappa\le n_Ln_R\le
n^2\), while \(Q_4\le\binom n4\). Thus the pair decoder alone closes only
above a polynomial endpoint surplus. At the half fixed gap, the minimizer
parent theorem gives only

\[
                         \Sigma>2^{3/2}(\log n)^K.              \tag{7}
\]

Consequently (6) closes that branch precisely if, for example,

\[
 \kappa<\theta,2^{3/2}(\log n)^K
 \quad\text{or}\quad
 \lambda<{	heta,2^{3/2}(\log n)^K V\over Q_4}.               \tag{8}
\]

There is no unconditional reason for either inequality. The balanced
Pascal substitution family gives a rational, rank-\(O(\log n)\),
coefficient-half saturation with

\[
 \theta=1-o(1),\qquad \Sigma=\Theta(n^2),\qquad
 \kappa=(1-o(1))n^2,
 \qquad {\lambda Q_4\over V}=\Omega(n^2).                     \tag{9}
\]

So the sharp exponent of the two-target Hall operation is two, not zero.
This is a leading-half calibration, not a strict fixed-gap counterexample.

Prefix shields do supply a third ordinary target, but they do not
automatically improve the exponent. At depth \(j\), for
\(S\subseteq K_j\subseteq A\), put

\[
                         Z_{r,S}=B\cup S.                       \tag{10}
\]

It is ordinary. However

\[
 X_r\cup Z_{r,S}=X_r,
 \qquad X_r\cup Y_r\notin\mathcal F(P),
 \qquad Y_r\cup Z_{r,S}\notin\mathcal F(P),                  \tag{11}
\]

because the last union retains the noncup trace \(B\cup\{z\}\). Thus the
third target is genuinely separated; it is not a literal one-face splice.
There is an exact three-target Hall inequality below. It helps only when
the actual shield marginal or a new pair projection has small load.

The maximum-child role regression from the preceding prefix-shield report
has aggregate expansion only \(O(\log n)\) relative to the entrance mass.
Hence prefix entropy by itself does not bridge the polynomial threshold in
(9). The remaining positive operation is now exact: prove a
subpolynomial bound for one of the loads in (6) or (17) below by using
minimum-cell/tangent history, rather than the two circuits or the prefix
trie alone.

## 1. Two-target Hall theorem

Let \(\mathcal R\) be a finite weighted record family. Each record has two
tagged targets \(X_r\in\mathcal X\) and \(Y_r\in\mathcal Y\). For every
subfamily \(\mathcal R'\), write \(x',y'\) for the numbers of incident
targets. The marginal load bounds give

\[
 \operatorname{mass}(\mathcal R')\le\kappa x',
 \qquad
 \operatorname{mass}(\mathcal R')\le\lambda y'.               \tag{12}
\]

If the left side is \(m'\), then \(x'\ge m'/\kappa\) and
\(y'\ge m'/\lambda\). Therefore

\[
 {m'\over x'+y'}
 \le {1\over \kappa^{-1}+\lambda^{-1}}
 ={\kappa\lambda\over\kappa+\lambda}.                         \tag{13}
\]

The weighted record-to-target max-flow/min-cut theorem now routes every
record to one incident target with tagged maximum load at most \(h_2\).
This proves the last term of (3). The first two terms follow by grouping
records by one target. The pair-load term follows from

\[
                         M\le\delta pq.                         \tag{14}
\]

Finally \(p\le V\) and \(q\le Q_4\), proving (3).

Equivalently, the separated pair decoder gives only the Cauchy conclusion

\[
                         \max\{p,q\}\ge\sqrt{M/\delta}.         \tag{14a}
\]

Unless one support is already known to be small, (14a) is the fatal
square-root loss. The rank-four fact supplies exactly the extra bound
\(q\le Q_4\), producing \(M\le\delta VQ_4\), but \(Q_4\) is polynomial
rather than polylogarithmic.

The theorem is sharp from the stated data. In \(K_{\lambda,\kappa}\),
the left maximum degree is \(\kappa\), the right maximum degree is
\(\lambda\), and

\[
 {M\over p+q}={\kappa\lambda\over\kappa+\lambda}.              \tag{15}
\]

No circuit information beyond the actual two targets can improve this
abstract constant.

For the double-bad records, \(X=A\cup B\) recovers \(A,B\). Only \(y,z\)
remain, so

\[
                         \kappa\le n_Ln_R.                      \tag{16}
\]

The seam load \(\lambda\) has no comparable circuit-theoretic bound. The
exact twelve-point Pascal cell already has \(\lambda=108\), although its
pair load is one.

## 2. Exact prefix-expanded three-target inequality

Take any collection of prefix nodes. Expand a record at depth \(j\) by all
\(2^j\) subsets of its common prefix, and let \(E\) be the total expanded
mass. Use the three ordinary targets \(X,Y,Z\) from (1) and (10). Let

\[
 K_X,K_Y,K_Z
\]

be their aggregate marginal loads; let

\[
 \Delta_{XY},\Delta_{XZ},\Delta_{YZ}
\]

be the three pair loads; and let \(T_{XYZ}\) be the triple load. Put

\[
 h_3=\left(K_X^{-1}+K_Y^{-1}+K_Z^{-1}\right)^{-1}.              \tag{17a}
\]

Exactly the same Hall argument, now with three targets per expanded
record, gives

\[
\boxed{
\begin{aligned}
E\le\min\{&K_XV,\ K_YQ_4,\ K_ZV,\ h_3(2V+Q_4),\\
           &\Delta_{XY}VQ_4,\ \Delta_{XZ}V^2,
             \Delta_{YZ}VQ_4,\ T_{XYZ}V^2Q_4\}.
\end{aligned}}                                                \tag{17}
\]

For one fixed node, the triple \((X,Y,Z)\) decodes \((r,S)\) with load
one in the unweighted record family. Along a nested path, the same subset
\(S\) can occur at at most the rank many depths, so \(T_{XYZ}\le R\) after
all nongeometric history has been fixed. In contrast, a depth-\(j\) record
of weight \(w_r\) contributes

\[
               d^+_{XY}(X_r,Y_r)\ge 2^j w_r                    \tag{18}
\]

on a depth-\(j\) record, because the pair \((X,Y)\) erases \(S\).
Therefore the original pair projection cancels the prefix multiplier.

If the entrance mass satisfies \(M_0\ge\theta\Sigma V\) and

\[
 {E\over M_0}=\mathfrak B,
\]

then (17) is equivalently

\[
\boxed{
\theta\Sigma\mathfrak B\le
\min\left\{
 K_X,{K_YQ_4\over V},K_Z,
 h_3\left(2+{Q_4\over V}\right),
 \Delta_{XY}Q_4,\Delta_{XZ}V,\Delta_{YZ}Q_4,T_{XYZ}VQ_4
\right\}.}                                                   \tag{19}
\]

This is the exact test for a useful third target. In particular, the shield
marginal closes if

\[
                         K_Z<\theta\Sigma\mathfrak B.           \tag{20}
\]

The trie theorem does not imply (20): many different erased tails can have
the same rooted shield \(B\cup S\). The half-scale ordered-role regression
has \(\mathfrak B=O(\log n)\), and its shield collisions realize precisely
this failure.

Equation (11) rules out the most direct repair of those collisions. Since
\(B\cup\{z\}\) is not a cup, adjoining the rank-four seam to any one-sided
shield which retains all of \(B\) is nonordinary. Deleting enough of \(B\)
can make a merged face, but then the erased cup tail becomes a second source
coordinate and the same two-target problem returns on the other side.

There is an exact characterization of this possible two-sided deletion.
For \(S\subseteq A\) and \(T\subseteq B\), the strong-glue face theorem
gives

\[
 Y_r\cup S\cup T\in\mathcal F(P)
 \quad\Longleftrightarrow\quad
 S\cup\{a_*(A,y),y\}\in\mathcal C(L)
 \ \text{and}\ 
 T\cup\{z,b_*(B,z)\}\in\mathcal U(R).                \tag{20a}
\]

Neither factor has a universal exponential lower bound. For a rational
left-child representative, take

\[
 p_i=(i,-i^2)\quad(1\le i\le m),
 \qquad y=(-1,M)
\]

with \(M\) sufficiently large and fix \(a=p_1\). Then

\[
                         \chi(y,p_1,p_i)>0\qquad(i>1),           \tag{20b}
\]

whereas a cap triple has negative sign. Hence a downface retaining
\(a,y\) may add no other \(p_i\). The reflected upward parabola with a far
lower guard gives the same statement for \(z,b\). Thus (20a) has only one
actual merged output, although the two prefix cubes have \(2^{2m}\) formal
choices. Rational lexicographic composition places these two child order
types in a genuine strong-glue chart. This is a scalable local barrier to a
universal merged-prefix theorem. Its convex parabolic child clouds pay
ambient Boolean faces, so it is not a low-\(V\) counterexample.

## 3. Exact finite Pascal audit

For \(Q=T(4,2)\) and \(P=Q\prec Q\), the exact double-bad family has

\[
\begin{array}{c|c}
\text{quantity}&\text{value}\\ \hline
M&3600\\
p&625\\
q&121\\
\kappa&9\\
\lambda&108\\
\delta&1\\
V(P)&1061.
\end{array}                                                    \tag{21}
\]

The harmonic Hall value is \(h_2=108/13\). The four right sides of (3),
using the actual supports where appropriate, are

\[
 5625,\qquad13068,\qquad75625,\qquad{80568\over13};             \tag{22}
\]

all above \(3600\). Thus the finite seam load \(108\) is real but does not
behave like the pair load one.

There is also an exact rank-three prefix stress inside the same rational
configuration. One may take

\[
 A=\{0,1,3\},\ y=2,\qquad B=\{6,7,8\},\ z=9,
\]

with the canonical seam witnesses \(a=0,b=6\). All eight one-sided shields
\(B\cup S\), \(S\subseteq A\), are ordinary, but none of their unions with
the seam is ordinary. Among all \(64\) two-sided subset choices, only eight
formal choices survive with the seam. This is a small exact warning that
even two-sided downfaces need not retain a constant fraction of the local
Boolean product.

## 4. Stretchable coefficient-half saturation

Let \(Q=Q_{k,d}\) be the balanced rational Pascal substitution family from
`agent_common_shield_mixing/PARENT_UPPER_ENDPOINT_RESET_THRESHOLD.md`.
Write

\[
 |Q|=N,\qquad C(Q)=U(Q)=H_1,\qquad V(Q)=H,
\]

and let every cap and cup have rank at most \(R=O_k(\log N)=o(N)\). Its
two-copy parent is

\[
                         P=Q\prec Q,
\]

with

\[
 V(P)=2H+H_1^2\le3H_1^2,
 \qquad C(P)U(P)=(N+2)^2H_1^2.                                 \tag{23}
\]

The number of addable cap-anchor incidences in one child is

\[
 E_C=2\sum_{A\in\mathcal C(Q)}|A|-N\le2RH_1.                  \tag{24}
\]

Hence the number \(D_C\) of nonaddable cap-anchor incidences satisfies

\[
                         D_C\ge(N-2R)H_1,                       \tag{25}
\]

and the reflected statement holds for cups. Their Cartesian product is an
actual double-bad family of size

\[
 M=D_CD_U\ge(N-2R)^2H_1^2.                                    \tag{26}
\]

Consequently

\[
 {M\over C(P)U(P)}
 \ge\left({N-2R\over N+2}\right)^2=1-o(1),
 \qquad
 {M\over V(P)}\ge{(N-2R)^2\over3}.                            \tag{27}
\]

There are exactly \(H_1^2\) detached sources. Therefore their average
load is at least \((N-2R)^2\), while (16) bounds the maximum by \(N^2\):

\[
                         \kappa=(1-o(1))N^2.                    \tag{28}
\]

There are at most \(N^4\) rank-four seams, so

\[
                         \lambda\ge {M\over N^4}
                                  \ge {H_1^2\over N^{2+o(1)}}. \tag{29}
\]

The square-root structure is physical, not just averaging over four-sets.
On the left, the canonical map \((A,y)\mapsto(a_*(A,y),y)\) has at most
\(N^2\) outputs. Hence one fixed left anchor pair has fibre

\[
 L_*\ge {D_C\over N^2}\ge {H_1\over N^{1+o(1)}}.              \tag{29a}
\]

The reflected right map has a fibre \(R_*\) of the same size. Since the
two endpoint choices are independent in a genuine strong glue, their
fixed rank-four seam has load

\[
                         L_*R_*\ge {H_1^2\over N^{2+o(1)}}.     \tag{29b}
\]

Each physical one-sided fibre has logarithmic coefficient
\(\rho_k/2\to1/4\), while their detached source rectangle has coefficient
\(\rho_k\to1/2\). This is the exact quarter-by-quarter square-root barrier
which the prefix aggregate would have to beat.

Since \(H_1^2=2^{\Theta((\log N)^2)}\), one has
\(\lambda\gg N^2\), and hence

\[
                         h_2=(1-o(1))N^2.                       \tag{30}
\]

This is not merely an upper-bound artefact. The exact fractional Hall load
of the two-target record graph is at least its full-family density:

\[
 \eta_2\ge {M\over H_1^2+N^4}=(1-o(1))N^2.                    \tag{30a}
\]

Thus every routing to either the detached source or the rank-four seam has
load \(N^{2-o(1)}\). If prefix expansion has relative mass
\(\mathfrak B\), then even after allowing all three target types its Hall
load is at least

\[
 \eta_3\ge {M\mathfrak B\over 2V+N^4}
            =\Omega(N^2\mathfrak B).                           \tag{30b}
\]

The extra target alphabet therefore scales the demand and the unavoidable
one-face load together. A useful third target must have additional decoder
structure, not merely be another ordinary face in the same universe.

Equations (27)--(30) saturate the source and Hall thresholds in (6) at
exponent two. The seam marginal is saturated as well at the level of its
average load. The pair-load-one bound is weaker because the seam alphabet
has polynomial rank-four capacity.

The exact substitution theorem gives

\[
 {\log V(P)\over(\log(2N))^2}\longrightarrow\rho_k,
 \qquad
 \rho_k\downarrow{1\over2},                                   \tag{31}
\]

and all the relevant ranks are \(O_k(\log N)\). Thus this is a stretchable
coefficient-half barrier with the correct dense double-bad phenotype. It is
not a least fixed-gap counterexample: it does not have the negative
\(-K(\log n)\log\log n\) correction. Its purpose is to show that the
square-root/two-target loss and the exponent-two marginal loads are genuine,
not artefacts of a nonstretchable tensor.

## 5. Exact exponent menu

For quick use, suppose

\[
 \Sigma=n^{s+o(1)},\quad \theta=n^{-t+o(1)},\quad
 \kappa=n^{k+o(1)},\quad \lambda=n^{\ell+o(1)},
 \quad Q_4=n^{q+o(1)},\quad V=n^{v+o(1)}.
\]

The base record family is impossible if any one of

\[
\begin{aligned}
s-t&>k,\\
s-t&>\ell+q-v,\\
s-t&>q+\log_n\delta,\\
s-t&>\min\{k,\ell\}+\max\{0,q-v\}
\end{aligned}                                                  \tag{32}
\]

holds with a fixed positive margin. In the quasipolynomial regime
\(v\gg q\), the Hall line is simply \(s-t>\min\{k,\ell\}\). The balanced
half construction has \(s=2,t=0,k=2\) and equality at the live line. The
strict half fixed-gap surplus (7) has \(s=0\), so it needs a genuinely
subpolynomial marginal or shield-pair load.

For the prefix-expanded family, replace \(s-t\) by
\(s-t+\log_n\mathfrak B\) and compare with the eight loads in (19). This
is the promised exact decoder threshold; no unrecorded chronology entropy
is being counted.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_double_bad_prefix_hall_threshold_and_half_barrier.py
```

The checker:

1. exhausts the sharp two-target and three-target Hall examples;
2. reproduces all six actual Pascal loads in (21) and the bounds (22);
3. verifies the one-sided and two-sided prefix nonmerge stress exactly on
   rational coordinates; and
4. verifies the parabolic common-guard collapse (20a)--(20b); and
5. checks the dense half-scale inequalities and the balanced Pascal
   coefficient sequence.

Expected output:

```text
PASS: double-bad Hall threshold; hall2=12/7 hall3=4/3; Pascal=(3600, 625, 121, 9, 108, 1); prefix=(8, 0, 8); guard=(8, 2, 2, 4); half=(1024, 20, 968256, 322752/1)
```
