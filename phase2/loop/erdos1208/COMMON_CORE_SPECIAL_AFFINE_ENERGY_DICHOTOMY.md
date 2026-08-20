# Recursive derivative patches: common-core affine energy dichotomy

## 1. Outcome

The recursive child operation has an exact special-affine group structure.
It yields a genuine additive-growth theorem for clusters of derivative
patches sharing a tail core.

Let \(R\) be the \(k\) occupied transverse levels, let \(S\subset R\) have
\(|S|=L\ge3\), and augment a set \(Q\) of shifts by \(0\in Q\).  Suppose

\[
 f(r+q)-f(r)=\alpha_q+\lambda_qr
 \quad(r\in S,\ q\in Q),\qquad
 (\alpha_0,\lambda_0)=(0,0).                           \tag{1.1}
\]

Thus every nonzero \(q\) describes a derivative line whose tail set
contains the same core \(S\); \(q=0\) is the identity patch.  Put \(M=|Q|\)
and

\[
 \Gamma=\{(q,\lambda_q):q\in Q\}.
\]

If \(B\) is the maximum number of points of \(\Gamma\) on one affine line,
then

\[
 \boxed{LM\le kB.}                                    \tag{1.2}
\]

This common-core additive-energy dichotomy has two immediate consequences.

1. The core-supported record mass obeys
   \[
    (M-1){L\choose3}\le {1\over6}Bk^3.                \tag{1.3}
   \]
   Hence a full-support cluster is on the desired \(k^{3+o(1)}\) scale
   whenever its shift--slope parameter set has subpolynomial line
   richness.
2. A threatening common-core cluster forces a polynomially rich affine
   parameter block
   \[
    \lambda_q=\theta q+\eta.                           \tag{1.4}
   \]
   After quotienting by any anchor in this block, all child slopes become
   \(\theta h\): the block has one coherent quadratic curvature.

The intercepts are retained.  For a block (1.4), put

\[
 \beta_h(d)=\alpha_{d+h}-\alpha_d-\theta hd.           \tag{1.5}
\]

For each fixed \(h\ne0\), among all \(d,d+h\) in the block,

\[
 \boxed{|\{\beta_h(d)\}|\le k/L.}                     \tag{1.6}
\]

Distinct values give distinct parallel child lines in the same derivative
cell, and their translated \(L\)-point supports are disjoint.  If one
value persists along a shift progression, the corresponding
\(\alpha_d\)'s are exactly quadratic.

There is also a direction-uniform arithmetic restriction.  For
\(A\subset[m]^2\), every nonhorizontal derivative line of richness at
least \(L\) has reduced slope \(a/b\) satisfying

\[
 |a|(L-1)\le {2(m-1)\over \|w\|_\infty},\qquad
 b(L-1)\le2\|w\|_\infty(m-1).                         \tag{1.7}
\]

Consequently there are at most

\[
 \boxed{{8(m-1)^2\over(L-1)^2}}                       \tag{1.8}
\]

possible reduced slopes at richness \(L\).  Combining (1.8) with
same-slope tail-pair packing bounds the complete dyadic \(L\)-rich record
mass by

\[
 T_L\ll {m^2k^2\over L}.                              \tag{1.9}
\]

This closes the \(k^3\)-dominated range \(L\gtrsim m^2/k\).  After the
earlier Szemeredi--Trotter cutoff, the distributed-overlap band is therefore

\[
 \sqrt{k}<L\lesssim m^2/k,                             \tag{1.10}
\]

together with common-tail-triple clusters having no large common core.
The common-core part is reduced to a rich parameter line plus at most
\(k/L\) intercept defects per difference.

## 2. The special-affine quotient is exactly the child patch

Associate to (1.1) the affine shear

\[
 G_q(r,y)=(r+q,\ y+\alpha_q+\lambda_qr).               \tag{2.1}
\]

It maps every graph point \((r,f(r))\), \(r\in S\), to
\((r+q,f(r+q))\).  Its right quotient is

\[
 G_cG_d^{-1}(t,y)
 =\left(t+c-d,
 y+\beta_{c,d}+(\lambda_c-\lambda_d)t\right),         \tag{2.2}
\]

where

\[
 \beta_{c,d}=\alpha_c-\alpha_d-(\lambda_c-\lambda_d)d.\tag{2.3}
\]

For \(t=r+d\), \(r\in S\), this is precisely

\[
 d_{c-d}(t)=\beta_{c,d}+(\lambda_c-\lambda_d)t,
 \qquad t\in S+d.                                     \tag{2.4}
\]

Thus every ordered pair of common-core patches produces an \(L\)-point
child patch, with its shift, slope, intercept, and translated tail support
all explicit.  Formula (2.2) is the group form of the derivative cocycle.

## 3. Additive energy forces a parameter line

Equation (1.1) implies

\[
 S+Q\subset R.                                        \tag{3.1}
\]

Let \(E_+(S,Q)\) count ordered solutions

\[
 s+c=s'+q_0,
 \qquad s,s'\in S,\ c,q_0\in Q.                       \tag{3.2}
\]

Cauchy--Schwarz and (3.1) give

\[
 E_+(S,Q)\ge{L^2M^2\over|S+Q|}\ge{L^2M^2\over k}.    \tag{3.3}
\]

For each \((s,q_0)\in S\times Q\), define

\[
 A(s,q_0)=\{c\in Q:s+c-q_0\in S\}.                   \tag{3.4}
\]

Then

\[
 E_+(S,Q)=\sum_{s,q_0}|A(s,q_0)|.                     \tag{3.5}
\]

Every local neighborhood in (3.4) is collinear in the parameter plane.
Take \(c,d\in A(s,q_0)\).  The quotient maps

\[
 H_c=G_cG_{q_0}^{-1},\qquad H_d=G_dG_{q_0}^{-1}
\]

are defined on the common support \(S+q_0\).  Starting at \(s+q_0\), both
compositions \(H_dH_c\) and \(H_cH_d\) are defined, because
\(s+c,s+d\in S+q_0\), and both end at the graph point with transverse level
\(s+c+d-q_0\).  Equality of their longitudinal coordinates gives

\[
 (c-q_0)(\lambda_d-\lambda_{q_0})
 =(d-q_0)(\lambda_c-\lambda_{q_0}).                    \tag{3.6}
\]

This is the collinearity of
\((q_0,\lambda_{q_0})\), \((c,\lambda_c)\), and
\((d,\lambda_d)\).  Since \(q_0\in A(s,q_0)\), all parameter points indexed
by \(A(s,q_0)\) lie on one line.  Therefore

\[
 |A(s,q_0)|\le B,\qquad E_+(S,Q)\le LMB.              \tag{3.7}
\]

Combining (3.3) and (3.7) proves (1.2).  Moreover,

\[
 (M-1){L\choose3}\le {ML^3\over6}
 \le {kBL^2\over6}\le {Bk^3\over6},                  \tag{3.8}
\]

which proves (1.3).  Compression of the \(LM\) source--shift incidences
into \(k\) target levels forces additive energy, and exact commutation
turns every energy neighborhood into a parameter line.

## 4. Intercept defects and exact quadratic recurrence

Let \(Q_0\subset Q\) lie on the parameter line (1.4).  For
\(d,d+h\in Q_0\), (2.2) becomes

\[
 d_h(t)=\beta_h(d)+\theta h t,
 \qquad t\in S+d.                                     \tag{4.1}
\]

If \(\beta_h(d)\ne\beta_h(d')\), these are distinct parallel lines in
the same cell \(P_h\).  Their tail sets \(S+d\) and \(S+d'\) must be
disjoint: at a common tail, the single value \(d_h(t)\) would lie on both
parallel lines.  Choosing one support for each distinct intercept gives

\[
 L|\{\beta_h(d)\}|\le k,                              \tag{4.2}
\]

which proves (1.6).

On an arithmetic progression

\[
 d_j=d_0+jh\quad(0\le j<J),                            \tag{4.3}
\]

suppose the same intercept defect \(\beta_h\) occurs on every consecutive
transition.  Then

\[
 \alpha_{d+h}-\alpha_d=\theta hd+\beta_h,              \tag{4.4}
\]

and summation gives

\[
 \boxed{
 \alpha_{d_j}=\alpha_{d_0}+j\beta_h
 +\theta h\left(jd_0+{h j(j-1)\over2}\right).}         \tag{4.5}
\]

Together with \(\lambda_{d_j}=\theta d_j+\eta\), this is an exact
quadratic parameter block.  The missing step is to force a long
monochromatic transition path from the at most \(k/L\) cells in (1.6).

## 5. Arithmetic audit of the slope count

Write the adapted graph points as

\[
 x_r=r z_w+f(r)w,\qquad
 \det(w,z_w)=1,\qquad q_w=\|w\|_\infty.                \tag{5.1}
\]

Let a derivative line contain \(L\) points with ordered tails
\(r_1<\cdots<r_L\), and let its reduced slope be \(a/b\), \(b>0\).
Since the derivative values are integral,

\[
 {a\over b}(r_i-r_j)\in\mathbb Z.
\]

Coprimality implies

\[
 r_i\equiv r_j\pmod b,\qquad
 r_L-r_1\ge b(L-1).                                   \tag{5.2}
\]

For a fixed derivative shift \(c\),

\[
 \Delta_c(r)=c z_w+d_c(r)w,
\]

and hence

\[
 \Delta_c(r_L)-\Delta_c(r_1)
 =(d_c(r_L)-d_c(r_1))w.
\]

Every displacement coordinate lies in \([-(m-1),m-1]\).  On a coordinate
where \(|w_i|=q_w\),

\[
 |d_c(r_L)-d_c(r_1)|q_w\le2(m-1).                     \tag{5.3}
\]

Using (5.2) and the line slope gives

\[
 |a|(L-1)\le {2(m-1)\over q_w}.                       \tag{5.4}
\]

Also

\[
 |r_L-r_1|
 =|\det(w,x_{r_L}-x_{r_1})|
 \le(m-1)\|w\|_1\le2q_w(m-1),                        \tag{5.5}
\]

which proves the denominator half of (1.7).  There are at most

\[
 2\left\lfloor{2(m-1)\over q_w(L-1)}\right\rfloor
  \left\lfloor{2q_w(m-1)\over L-1}\right\rfloor
 \le {8(m-1)^2\over(L-1)^2}                           \tag{5.6}
\]

signed reduced fractions satisfying these bounds.  This proves (1.8)
without a divisor loss; the direction height cancels exactly.

For a dyadic family \(L\le L_\ell<2L\), same-slope packing gives

\[
 \sum_{\ell:\lambda_\ell=\lambda}{L_\ell\choose2}
 \le{k\choose2}.
\]

Since

\[
 {L_\ell\choose3}
 ={L_\ell-2\over3}{L_\ell\choose2}
 <{2L\over3}{L_\ell\choose2},
\]

summing (5.6) over possible slopes proves (1.9), quantitatively

\[
 T_L
 <{16(m-1)^2L\over3(L-1)^2}{k\choose2}.              \tag{5.7}
\]

## 6. Relation to the global reverse-multiplicity gate

For the full rich-line family, let

\[
 T=\sum_\ell {L_\ell\choose3},\qquad
 d_U=|\{\ell:U\subset S_\ell\}|
\]

for each tail triple \(U\subset R\).  Then

\[
 \sum_Ud_U=T,\qquad
 \sum_U {d_U\choose2}
 \ge {1\over2}\left({T^2\over{k\choose3}}-T\right).   \tag{6.1}
\]

Orient each unordered parent-patch pair in (6.1) so its first shift is
larger.  It produces the positive-shift child record (2.4) on the
translated triple \(U+d\).  The parent shifts are distinct, since two
different lines in one derivative cell cannot share three tails, and the
child is nonhorizontal by full-family same-slope packing.  For a fixed
child record, a reverse preimage
is indexed by the second shift \(d\): once \(d\) is fixed, the two parent
shifts and the two parent lines through their three derivative points are
determined.  Translating one fixed child tail back into \(R\) gives at most
\(k\) possible values of \(d\).  Hence

\[
 \sum_U {d_U\choose2}\le kT,\qquad
 T\le(2k+1){k\choose3}=O(k^4).                        \tag{6.2}
\]

The exact missing global gain is a sub-\(k\) reverse-multiplicity or height
theorem.  If one child quotient

\[
 (h,\mu,\beta)=G_{d+h}G_d^{-1}                        \tag{6.3}
\]

has many reverse shifts \(d\), its parameters obey

\[
 \lambda_{d+h}-\lambda_d=\mu,\qquad
 \alpha_{d+h}-\alpha_d=\mu d+\beta.                   \tag{6.4}
\]

Along every path \(d,d+h,\ldots,d+Jh\), this integrates to

\[
 \lambda_{d+jh}=\lambda_d+j\mu,
\]

\[
 \alpha_{d+jh}=\alpha_d+j\beta
 +\mu\left(jd+{h j(j-1)\over2}\right).                \tag{6.5}
\]

Thus high reverse multiplicity has the same exact quadratic-path versus
many-short-components dichotomy as (4.5).  The common-core theorem closes
the concentration in which many parent patches share a large tail core.
The survivor has reverse preimages distributed over many translated tail
triples and many short parameter paths.

## 7. Verified stresses and exact remaining gap

The verifier contains three complementary exact stresses.

1. **Coherent quadratic.**  For \(f(r)=r^2\),
   \(R=\{0,\ldots,10\}\), \(S=\{0,\ldots,7\}\), and
   \(Q=\{0,1,2,3\}\), one has
   \(\lambda_q=2q\), \(\alpha_q=q^2\).  The parameter block is collinear,
   every intercept defect is \(\beta_h=h^2\), and all 55 squared distances
   are distinct.
2. **Noncoherent disjoint-target barrier.**  There is a 24-point integral
   distance-Sidon graph with \(L=6>\sqrt{24}\), three nonhorizontal
   patches sharing all six tails, and parameter slopes \(37,101,250\) at
   shifts \(6,12,18\).  The target translates are disjoint, the additive
   energy is minimal \(LM\), and the augmented parameter set has no three
   collinear points.  Thus large tail overlap alone does not force a
   quadratic block; target compression is essential.  Its 60 core records
   are far below \(k^3\), as (1.2) predicts.
3. **Rational slope.**  An eight-point integral distance-Sidon graph has a
   four-point derivative line of reduced slope \(3/2\) on tails
   \(0,2,4,6\), checking the denominator congruence (5.2).

The unresolved configuration is now sharply specified: a dyadic family in
the band (1.10), with polynomial shift--slope line richness, near-maximal
distributed intercept behavior across many differences (up to the
\(k/L\) cells allowed by (1.6)), and large global reverse multiplicity
spread over translated tail triples so that neither a large common core
nor a long quotient path appears.  A full finish must rule out that
simultaneous distribution using the distance-Sidon metric, or construct it
at critical \(T\gg k^3+m^2\).

## 8. Verification

Run

    python phase2/loop/erdos1208/verify_common_core_special_affine_energy_dichotomy.py

The verifier checks every affine quotient identity, the additive-energy
lower and upper bounds, local parameter collinearity, (1.2), intercept-cell
disjointness, the quadratic recurrences, the rational-slope congruence and
finite slope-count inequality, the global reverse-child map and its exact
multiplicities, and all squared distances in the three certificates.
