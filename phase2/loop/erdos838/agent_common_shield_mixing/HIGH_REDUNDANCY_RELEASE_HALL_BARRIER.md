# High-redundancy release fibres: exact support Cauchy and the dense Hall barrier

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The high-`E R_U` branch of
`WEIGHTED_POSITION_RELEASE_ENTROPY.md` has an exact ambient-support charge,
but its global overlap can be quadratic-exponential.  For a release fibre
`u`, let

* `m_u` be its raw record weight;
* `J_u` be its deleted coordinate mask;
* `P_u=prod_(i in J_u)|X_i|`;
* `R_u=log P_u-H(D|U=u)`;
* `Q_u=union_(i in J_u)X_i`, `N_u=|Q_u|`; and
* `H_u=V(P|Q_u)-1`, the number of **nonempty** support faces.

If `Lambda_supp` is the actual overlap of the ambient face banks
`F(P|Q_u)`, then

\[
 \boxed{\quad
 \sum_um_u\le
   \sqrt{\Lambda_{\rm supp}\max_u(m_u^2/H_u)}\,V(P).
 \quad}                                                   \tag{1}
\]

The local factor has the unconditional rank-tax estimate

\[
 \boxed{\quad
 \log{m_u^2\over H_u}
 \le 2s_u\log{N_u\over s_u}-2R_u
       -(1/4-o(1))(\log N_u)^2,
 \quad}                                                   \tag{2}
\]

where `s_u=|J_u|` and the coordinate supports are disjoint.  Thus large
redundancy really does make each individual fibre cheap.

The overlap in (1) cannot be discarded or bounded from source rank.  An
exact rational common-guard construction has:

* an arbitrary sparse code of source words;
* a complete family of rich pocket words;
* every source--pocket pair blocked by a singleton loop at **every** source
  role;
* one released ordinary face `u` per pocket word;
* the same high-redundancy completion support in every `u`-fibre; and
* a literal complete source-face by released-face Hall core.

For a length-`q`, dimension-`k` MDS source code over an alphabet of size
`p` and an `h`-role pocket product,

\[
 M=p^k,\qquad K=p^h,\qquad R_u=(q-k)\log p,             \tag{3}
\]

and all `K` fibres use the same ambient source box of size `p^q`.  Hence

\[
                    \Lambda_{\rm supp}=K=p^h.           \tag{4}
\]

The Hall core has `MK=p^(k+h)` records but only `M+K` primary targets.
Choosing, for example,

\[
 q=(.4+o(1))L,\quad k=(.2+o(1))L,\quad h=(.3+o(1))L,
 \quad \log p=(1+o(1))L                                 \tag{5}
\]

gives quadratic redundancy `.2L^2`, record coefficient `.5`, and
individual ambient-bank coefficients only `.4` and `.3`.  Thus neither
high redundancy nor the two separate support banks pay the dense core.

This is a scalable **interface barrier**, not a sub-half construction or a
live minimizer regression.  Its ambient source box already has `p^q`
ordinary faces, so the selected source code has only a `2^{-R_u}` fraction
of that bank.  With the genuine per-source weight cap, one copy of the
tensor cannot carry `Theta(V(P))` marked source mass when `R_u` is
quadratic.  The full
point set may have additional cap/cup, one-gap, and recursive child faces.
Indeed proving that one of those extra banks always pays is exactly the
common-guard/profile problem.  What the construction rules out is an
automatic charge based only on `(B,F,J)`, `R_U`, the source/pocket face
banks, and Hall density.

The remaining invariant is now precise: either control the cap-weighted
support overlap `Lambda_supp`, or use planar cross-profile geometry to turn
the repeated support bank and the varying released faces into a third
one-face bank.

## 1. Exact global support Cauchy

For every nonempty fibre `u`, use two ordinary-face banks

\[
                     \mathcal A_u=\{u\},\qquad
       \mathcal S_u=\mathcal F(P|Q_u)\setminus\{\varnothing\}.       \tag{6}
\]

Different fibres have different actual release outputs, so the first-bank
load is one.  Define

\[
 \Lambda_{\rm supp}=
   \max_S|\{u:S\in\mathcal S_u\}|.                     \tag{7}
\]

> **Theorem 1 (support-reservoir Cauchy).**  Equation (1) holds.

**Proof.**  Put `K=max_u m_u^2/H_u`.  Then

\[
 m_u\le\sqrt{K|\mathcal A_u||\mathcal S_u|}.
\]

Sum and apply Cauchy.  Since the first outputs are distinct,
`sum_u|A_u|<=V(P)`, while (7) gives
`sum_u|S_u|<=Lambda_supp V(P)`.  This proves (1).  QED.

The weighted version replaces the cardinality in (7) by total fibre-bank
weight and is identical.  One may also dyadically bucket the local ratios
`m_u^2/H_u`; only the number of nonempty buckets is lost.

## 2. What high redundancy proves locally

The input record weights in the marked slice are at most one.  Therefore,
inside one fibre,

\[
                         H(D\mid U=u)\ge\log m_u.       \tag{8}
\]

Indeed every conditional atom has probability at most `1/m_u`.  It follows
from the definition of `R_u` that

\[
                         m_u\le P_u2^{-R_u}.            \tag{9}
\]

Because the coordinate supports are disjoint, AM--GM gives

\[
                         P_u\le(N_u/s_u)^{s_u}.         \tag{10}
\]

Finally the induced `N_u`-point order type contributes, after removing the
empty face,

\[
                   H_u\ge f(N_u)-1
                       \ge2^{(1/4-o(1))(\log N_u)^2}.  \tag{11}
\]

Squaring (9) and using (10)--(11) proves (2).

For example, if for some fixed `epsilon>0`

\[
 R_u\ge s_u\log(N_u/s_u)
          -(1/8-\epsilon)(\log N_u)^2,                 \tag{12}
\]

then `m_u^2/H_u<=2^{-(2epsilon-o(1))(log N_u)^2}`.  Such
fibres close through (1) whenever `Lambda_supp` is smaller than the
reciprocal gain.  Equation (12) is the sharp conclusion obtainable from
support entropy and the universal quarter theorem alone.

### 2.1 Conditional redundancy transfers to source redundancy

There is a second exact bound which uses the live source-mass hypothesis.
Let

\[
 P_0=\prod_{i=1}^r|X_i|,\qquad
 R_{\rm src}=\log P_0-H(A).                              \tag{12a}
\]

In the release law of the preceding report, `F` is uniform on an
`H`-face pocket family and independent of `A`.  The exact identity there
and the trivial bound `sigma<=log P_0` give

\[
 \boxed{\quad
 \mathbb E R_U
    \le R_{\rm src}+H(U)-\log H
    \le R_{\rm src}+\log V(P)-\log H.
 \quad}                                                   \tag{12b}
\]

Thus high conditional completion redundancy cannot appear from nowhere;
up to the pocket deficit, it is global source total correlation.

Let `Q=union_iX_i`, `N=|Q|`, and suppose the aligned source chart has
weight `W` with all source atoms of weight at most one.  If

\[
                         \log W\ge\log V(P)-\tau,        \tag{12c}
\]

then `H(A)>=log W`, while the induced support bank and disjoint-support
AM--GM give

\[
\begin{aligned}
 R_{\rm src}
   &=\log P_0-H(A)\\
   &\le r\log(N/r)-\log f(N)+\tau.                      \tag{12d}
\end{aligned}
\]

Indeed `log P_0<=r log(N/r)`, `H(A)>=log V-tau`, and
`log V>=log f(N)`.  Combining (12b)--(12d),

\[
 \boxed{\quad
 \mathbb E R_U\le
 r\log(N/r)-\log f(N)
 +\tau+\log(V/H).
 \quad}                                                   \tag{12e}
\]

On the fixed-gap slice, `tau=O((log n)log log n)` by position colouring
and `log(V/H)=O((log n)log log n)` by pocket induction.  Therefore the
low-redundancy product promotion is automatic whenever the rank tax

\[
                  r\log(N/r)-\tfrac14(\log N)^2         \tag{12f}
\]

is subquadratic.  In particular the critical window
`r=(1/4+o(1))log N` closes.  The only live high-redundancy window has source
rank genuinely above the quarter threshold.  This is stronger and more
specific than merely asking for a bound on `Lambda_supp`.

On the actual fixed-root chart one can replace the quarter coefficient by
the fixed-gap induction coefficient.  Every used source support is
disjoint from the deterministic pocket `X_T`, whose size is
`n/polylog n`.  Hence

\[
                         N\le n-|X_T|<n,                 \tag{12g}
\]

so least-counterexample minimality gives

\[
                         \log f(N)\ge c(\log N)^2,       \tag{12h}
\]

with `c=1/2-delta`.  The source entropy
`H(A)>=cL^2-O(L log L)` and `r=O(L)` force
`log N=Theta(L)`, but need not force `log N=L-o(L)`.  Substitution in
(12e) yields the sharper live bound

\[
 \boxed{\quad
 \mathbb E R_U
 \le r\log(N/r)-c(\log N)^2+O(L\log L)\\
 = (r-c\log N)\log N-r\log r+O(L\log L).
 \quad}                                                   \tag{12i}
\]

Consequently every rank slice with
`r<=c log N+O(log L)` is automatically in the recoverable low-redundancy
product branch.  The genuine high-redundancy residue is precisely an
**excess-rank** source slice

\[
                         r-c\log N=\Omega(L)             \tag{12j}
\]

(with intermediate `omega(log L)` excess tracked quantitatively by
(12i)).  A final high-redundancy theorem may therefore use rank compression
or source downshadows; it need not handle an arbitrary rank-safe family.

## 3. Exact common-guard Hall tensor

The finite geometry is the rooted all-loop chart already used in the
minimizer audit.  Put

\[
 a=(0,-1),\quad b=(4,-1),\quad c=(0,4),                 \tag{13}
\]

and, for `1<=t<=m`,

\[
 P_t=(2-\delta t^2,-1/5+\delta t),
 \qquad \delta={1\over100m^2}.                         \tag{14}
\]

Near the upper cap through `c`, place `q` disjoint source roles `Y_i`.
All supports may have a common alphabet size `p`.  Shrink them enough that
every source word

\[
                    A_y=\{a,b,c\}\cup\{y_i:y_i\in Y_i\}              \tag{15}
\]

is ordinary and, for every `i<j<k`, every upper label `y`,

\[
                    P_j\in\operatorname{int}
                             \operatorname{conv}\{P_i,P_k,y\}.       \tag{16}
\]

Replace the `P_t` by `h` sufficiently small ordered role clusters
`Z_1,...,Z_h`, also of size `p`.  Every one-point-per-role pocket word
`F_z` is ordinary, and (16) holds uniformly for one fixed triple of pocket
roles.

Select any source code `C subseteq prod_iY_i`; for (3), take Reed--Solomon.
For every `(y,z) in C times prod_jZ_j`, each selected source label `y_i`
is the singleton outer trace of a bad `1+3` circuit with three labels of
`F_z`.  Hence every source role is mandatory in a source-only release.
Deleting all source-role labels and the fixed point `c` leaves

\[
                         u_z=\{a,b\}\cup F_z,           \tag{17}
\]

which is ordinary.  Singleton fixed roles cost zero, so the minimum
alphabet deletion cost is exactly

\[
                         \sigma=q\log p.                \tag{18}
\]

For fixed `u_z`, the deleted completion distribution is precisely the
selected code.  Reed--Solomon has entropy `k log p` and full coordinate
supports, proving (3).  All `p^h` outputs use the same support union
`union_iY_i`, proving (4).

The two primary ordinary targets are the old source `A_y` and the released
face `u_z`.  Their incidence graph is the complete bipartite graph

\[
                         K_{p^k,p^h}.                   \tag{19}
\]

Its exact Hall density is

\[
                   \lambda_2={p^{k+h}\over p^k+p^h}.  \tag{20}
\]

Adding any bounded number of common circuit/signature targets changes the
denominator by only a constant and leaves the quadratic coefficient
unchanged.  Thus the face--face Hall core and the high-redundancy overlap
are the same obstruction, not two different branches.

## 4. Finite exact instance

Take the rational `m=5`, `q=3`, `p=2` chart.  Use the even-parity source
code

\[
                     \mathcal C=\{000,011,101,110\}.    \tag{21}
\]

There are four ordinary source faces.  The five local points have sixteen
rich faces of rank at least three.  Every one of the `4*16=64`
source--pocket pairs has all three source roles mandatory and releases to
`{a,b} union F`.  Each release output has load four.

The conditional completion entropy is two, its ambient box entropy is
three, and hence

\[
                            R_u=1                       \tag{22}
\]

in every fibre.  The eight ambient source transversals form an ordinary
support bank, reused by all sixteen release outputs.  Thus

\[
 m_u=4,\quad H_u\ge8,\quad m_u^2/H_u\le2,
 \quad\Lambda_{\rm supp}=16.                            \tag{23}
\]

The verifier checks every statement with exact rational arithmetic.

## 5. Exact conclusion

High conditional support redundancy has two valid uses:

1. the local rank-tax saving (2); and
2. the global support Cauchy theorem (1), when its actual overlap is small.

The common-guard tensor proves that `Lambda_supp` may equal the entire
released-face alphabet, even with rank-`O(log n)` sources, a fixed root,
fixed insertion edge, singleton circuit traces at every role, and a dense
two-target Hall core.  It is stretchable at every scale and accepts
arbitrary sufficiently small projective children in its macro roles.

The source-mass qualification is essential.  In this tensor
`W=p^k` but `V(P)>=p^q=W2^{R_u}`.  It therefore violates (12c) by exactly
the quadratic redundancy when `q-k=Theta(log n)`.  The example kills a
local/two-bank implication, but it does not survive the global minimizer
source cap.  A genuine live barrier would need either nonhomogeneous
geometry which suppresses the ambient `p^q` box, or many distinct
base-retaining source families whose support reservoirs overlap while
their actual sources remain distinct.  No such low-face planar regression
is claimed here.

### 5.1 Live fixed-gap parameter audit

The preceding qualification can be quantified exactly.  Put `d=log p` and
suppose a common-guard tensor were the chart selected by the rank-safe
entrance.  Then

\[
              W\ge V(P)2^{-\tau},\qquad
              \tau=O((\log n)\log\log n).              \tag{24}
\]

But its ambient source box gives `V(P)>=p^q`, while the selected code has
`W=p^k`.  Therefore

\[
              (q-k)d=R_u\le\tau.                       \tag{25}
\]

So a live tensor is automatically in the low-redundancy branch of
Theorem 3 in the preceding report.  The parameter choice (5) fails (24)
by the exact factor

\[
                         {W\over V(P)}\le2^{-.2L^2+o(L^2)}.           \tag{26}
\]

The pocket scale sharpens the audit.  In a least fixed-gap counterexample,
strong induction on a pocket of size `n/polylog n` gives

\[
 \log H=cL^2-O(L\log L),\qquad
 \log V(P)<cL^2,\qquad c=1/2-\delta.                  \tag{27}
\]

Equations (24) and (27) imply `log W=cL^2-O(L log L)`.  In the product
model `H=p^h`, hence

\[
                  k=(c+o(1))L,\qquad
                  h=(c+o(1))L,\qquad
                  q-k=O(\log L).                       \tag{28}
\]

Thus the live normalization is not `(q,k,h)=(.4,.2,.3)L`; it is
`q=k+o(L)` and `k=h=(c+o(1))L`.  Its complete Hall record mass is `WH`,
but after division by the ambient face count its exact obvious multiplier
obeys

\[
              {WH\over V(P)}\le H2^{-R_u}.             \tag{29}
\]

For quadratic `R_u` this multiplier loses the same quadratic coefficient
as the source slice and cannot be the rank-safe `Theta(V)` entrance.  For
the live bound (25), the loss is only `2^{O(L log L)}`; the low-redundancy
promotion preserves the quadratic coefficient and returns precisely to
the homogeneous all-loop/common-guard branch.

The support Cauchy parameters tell the same story.  Every release fibre has

\[
 m_u=W,\qquad H_u\ge p^q=W2^{R_u},\qquad
 {m_u^2\over H_u}\le W2^{-R_u},qquad
 \Lambda_{\rm supp}=H.                                 \tag{30}
\]

At (25) these quantities are coefficient-neutral; at quadratic `R_u` the
local saving is exactly accompanied by the forbidden source-mass deficit
(26).  Hence the tensor is a sharp applicability barrier, not the actual
fixed-gap high-redundancy residue.

It does not prove an upper bound on the full face complex.  Accordingly
the exact remaining high-redundancy statement is:

> in the above-quarter rank-tax window of a low-`V` minimizer, a common
> support bank reused by a quadratic released-face alphabet must create a
> cap/cup, one-gap, chronology, or mixed source--release bank whose overlap
> is smaller than (4).

That is a planar profile-composition theorem.  No entropy, downshadow, or
Hall argument which treats the two face alphabets separately can prove it.

## Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_high_redundancy_release_hall_barrier.py
```

Expected output:

```text
PASS: common-guard sources=4 rich=16 records=64 R=1 support=8 overlap=16; coefficients=(1/2,2/5,3/10)
```
