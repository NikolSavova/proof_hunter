# Rank-heavy clouds: generalized KK descent and a four-local minimizer barrier

**Date:** 2026-08-15.  All logarithms are base two.  This continues
`THIRD_CLOUD_KK_SINGLETON_TERMINAL_GATE.md`.  Put

\[
 a=\log_2 3,
 \qquad \theta_*=2-a,
 \qquad \kappa_*={1\over a}=0.630929753\ldots .          \tag{1}
\]

## Verdict

The cutoff `q <= kappa_* log R` is not a genuine capacity obstruction.
Let a cloud on `R=2^d` labels have at least `H=F_C(R)` faces and choose a
largest rank layer `A subset binom(X,q)`.  If `q>kappa_* d`, then for every
fixed `eta in (0,kappa_*)` its rank

\[
                 t=\lfloor(\kappa_*-\eta)d\rfloor        \tag{2}
\]

shadow satisfies

\[
        |\partial_t\mathcal A|
          \ge 2^{c_\eta d\log d}
          =R^{c_\eta\log\log R}.                         \tag{3}
\]

Here `c_eta>0` depends only on `eta`; the estimate is uniform in `q`, even
when `q` is much larger than `d`.  Since the ambient/cloud target ratio is

\[
 {F_C(N)\over F_C(R)}=R^{a+o(1)},\qquad N=(3+o(1))R,      \tag{4}
\]

the ordinary candidates `partial_t A` times an opposite cloud bank have
quasipolynomial surplus.  Good unions close the target.  If they do not,
all but an `R^{-Omega(log log R)}` fraction form a bad face--face rectangle
of rank at most `(kappa_*-eta)d` on the first side.  Thus the rank-heavy
exception is replaced by the already isolated **terminal anti-alignment**.

Two cautions are load-bearing.

1.  The descended shadow in (3) need not have `H/polylog(R)` members.  It
    therefore does not literally satisfy the large-layer hypothesis of
    the earlier low-rank theorem.  Its product capacity is enough, but an
    all-bad rectangle can still delete the entire shadow trace.
2.  The ambient minimizer mean does not give a low mean inside one cloud.
    A cloud bank is only an `R^{-a+o(1)}` fraction of the ambient bank; even
    rank-`R` on every cloud face contributes only
    `R^{1-a+o(1)}=o(1)` to the ambient mean.

The obstruction after (3) is real at the level of exact four-local
downsets and of all scalar minimizer identities.  Section 4 constructs a
symmetric weighted four-local complex with almost all mass at rank
`kappa d` for any `kappa in (kappa_*,1)`, target entropy
`Phi_C(d)+O(d)`, and the exact per-point deletion ratio.  Three disjoint
copies may be made completely cross-bad.  The construction is not claimed
stretchable.  Consequently the missing input is specifically a planar
rank-three oriented-matroid/circuit-elimination theorem forcing mixed
faces or a separated profile bank across the modules.  Mean rank,
ordinary downshadows, and four-locality alone do not provide it.

No coefficient-half closure is claimed.

## 1. Uniform generalized-KK descent

Write

\[
 \Phi_C(d)={d^2\over2}-Cd\log d,
 \qquad H=2^{\Phi_C(d)}.                                \tag{5}
\]

There are at most `R+1` rank layers, so a largest layer obeys

\[
                 M:=|\mathcal A|\ge {H\over R+1}.        \tag{6}
\]

More generally, if a `p` fraction of an `H`-scale bank lies above the
threshold in (7), some high layer has `M>=pH/(R+1)`.  Everything below is
unchanged for fixed `p>0` (indeed for `log(1/p)=o(d^2)`, with the
corresponding term retained).  Thus the statement applies both to a
rank-heavy largest layer and to positive high-rank mass.

### Theorem 1 (rank-heavy to low-rank quasipolynomial shadow)

Fix `eta in (0,kappa_*)` and put `k_0=kappa_*-eta`.  For all sufficiently
large `d` (depending on `C,eta`), if (6) holds and

\[
                 \kappa_*d<q\le R,                      \tag{7}
\]

then, for `t=floor(k_0d)`,

\[
                 |\partial_t\mathcal A|
                    \ge 2^{(k_0/5)d\log d}.              \tag{8}
\]

**Proof.**  Choose the real `x>=q` with `M=binom(x,q)`.  Lovasz--KK gives

\[
                 |\partial_t\mathcal A|\ge {x\choose t}.\tag{9}
\]

The standard upper estimate `binom(x,q)<=(ex/q)^q` and (6) imply

\[
 \log{x\over t}
 \ge {\log M\over q}+\log{q\over t}-\log e.             \tag{10}
\]

Put `y=q/d`.  Uniformly for `y>=kappa_*`, the right side of (10) is

\[
 {d\over2y}-{C\log d\over y}+\log{y\over k_0}-\log e-O(1/y).
                                                                    \tag{11}
\]

If `y<=d/log d`, the first two terms in (11) are at least
`(1/3)log d` for large `d`; the remaining terms are bounded below.  If
`y>=d/log d`, the logarithmic term is at least
`log d-log log d-O_eta(1)`, while the only negative `y`-dependent term is
`o(1)`.  Hence (11) is at least `(1/5)log d` in both cases.

For real `x>=t`,

\[
 {x\choose t}=\prod_{i=0}^{t-1}{x-i\over t-i}
                 \ge (x/t)^t.                            \tag{12}
\]

Equations (9)--(12), and `t=(k_0+o(1))d`, prove (8). `square`

The two ranges in (11) explain why no upper mean-rank cutoff is needed.
For `q=Theta(d)`, the entropy of `A` forces `x` exponentially large.  For
`q` much larger than `d`, the elementary `x>=q` term alone supplies the
large shadow.  The least favorable scale is `q=Theta(d^2)`, where the
shadow is still `R^{Theta(log d)}`.

### Corollary 2 (what a cloud-internal mean bound would give)

Suppose, in addition, that the **uniform face law of the induced cloud**
has mean at most `beta d`, where `beta` is fixed.  Markov gives at least
`H/2` cloud faces of rank at most `2 beta d`, so some such layer has

\[
                  M\ge {H\over 2(2\beta d+1)}.           \tag{12a}
\]

Write `q=kappa d`, so `kappa<=2 beta`.  For any fixed `epsilon>0`, choose

\[
                  t=\lceil2\kappa(a+2\varepsilon)\rceil.\tag{12b}
\]

Then `t=O_beta,epsilon(1)`, and the same estimates give

\[
 \log|\partial_t\mathcal A|
   \ge {t\over2\kappa}d-O_{C,\beta,\varepsilon}(\log d)
   \ge(a+\varepsilon)d.                                 \tag{12c}
\]

Thus a genuine cloud-internal `O(d)` mean would reduce the survivor to a
constant-depth terminal anti-alignment.  Section 3 explains why the known
**ambient** mean bound does not supply this hypothesis.

## 2. Exact cloud splice

Let `B` be the full face family of a disjoint second cloud, with
`|B|>=H`.  Every member of `partial_t A` is an actual ordinary face.
Moreover the union map

\[
        (T,B)\longmapsto T\cup B,
        \qquad T\in\partial_t\mathcal A,\ B\in\mathcal B,\tag{13}
\]

has load one on its good pairs, because the two physical clouds are
disjoint.  By (3)--(4), if the good-pair density is at least

\[
 {F_C(N)\over |\partial_t\mathcal A|H}
       \le R^{-c_\eta\log d+a+o(1)},                    \tag{14}
\]

then these ordinary unions already meet the target.  Otherwise a
`1-R^{-Omega(log d)}` fraction of (13) is bad.  Applying the exact
cross-circuit deletion forest to this rectangle gives the existing
singleton/empty terminal branch, now with starting rank at most
`(kappa_*-eta)d`.

This is a capacity reduction, not a proof that the all-bad branch pays.
The deletion-mask denominator through depth `t` can be
`2^{Theta(d^2)}`, much larger than (3).

## 3. Why the global mean cannot remove the branch

Let `V` be the ambient face count.  In the nested-triangle scale,

\[
                 V=H R^{a+o(1)}.                        \tag{15}
\]

Even if all `H` faces in each of three cloud banks have the maximum
possible rank `R`, their total contribution to the ambient uniform mean is
at most

\[
            {3RH\over V}=3R^{1-a+o(1)}=o(1),             \tag{16}
\]

because `a>1`.  Thus the global deletion consequence `mu=O(log N)` is
fully compatible with an arbitrary rank distribution on the three cloud
banks.  The inference

> `mu=O(log N)`, hence half of each induced cloud bank has rank
> `O(log R)`

is invalid without an additional charge comparing the cloud law to the
ambient uniform face law.

The same issue prevents a Boolean-shadow mean argument.  A lower shadow
is an ordinary bank, but its outputs may have enormous multiplicity across
the original high faces; KK gives the correct distinct capacity.  Theorem
1 is the resulting sharp unconditional use of that capacity.

## 4. A symmetric four-local weighted minimizer barrier

The following construction shows that the remaining issue is geometric,
not a missing scalar inequality.

Fix

\[
             \kappa\in(\kappa_*,1),\qquad c={1\over2\kappa}.      \tag{17}
\]

For an asymptotic parameter `m`, take

\[
 D=2^{cm+O(1)},\qquad
 q=\kappa m-2\kappa C\log m+O(1),\qquad
 t={2^{(1-c)m+O(1)}\over q},                             \tag{18}
\]

rounded on a subsequence so these are positive integers, and put
`R=tqD`, `d=log R=m+o(1)`.  Partition the `R` labels into `t` modules and
each module into `q` roles of size `D`.

The bounded `O(1)` term in `q` may be chosen so that `Z>=F_C(R)`:
changing `q` by one changes the dominant logarithm by
`log D=(c+o(1))d`, whereas the rounding uncertainty in (21) is only
`O_C(d)`.  We use such a choice below, so the final common formal face
weight is at most one.

Define a hereditary complex `K` by declaring `F` ordinary exactly when

* `|F|<=3`; or
* `F` lies in one module and meets every role in at most one label.

This rule is exactly four-local: a set of size at least four satisfies it
if and only if each of its four-subsets satisfies it.  Indeed a set using
two modules has a cross-module four-subset, while a set repeating a role
has a four-subset containing that repeated pair.  The converse is
immediate.

Let

\[
 P=(D+1)^q-\sum_{r=0}^3{q\choose r}D^r.                 \tag{19}
\]

Then its exact face count and total rank incidence are

\[
 \begin{aligned}
 Z&=\sum_{r=0}^3{R\choose r}+tP,\\
 I&=\sum_{r=0}^3r{R\choose r}
   +t\left(qD(D+1)^{q-1}
       -\sum_{r=0}^3r{q\choose r}D^r\right).            \tag{20}
 \end{aligned}
\]

Consequently

\[
 \begin{aligned}
 \log Z&={d^2\over2}-Cd\log d+O_C(d)=\Phi_C(d)+O_C(d),\\
 \mu:={I\over Z}&=q-o(1)=\kappa d-2\kappa C\log d+O_C(1).       \tag{21}
 \end{aligned}
\]

In particular `1-o(1)` of the uniform face law lies in the rank-`q`
transversal layer, strictly above `kappa_*d`.

All vertices are symmetric.  If `Z_v` is the number of faces after any
one vertex is deleted, the exact deletion identity therefore gives

\[
                  {Z_v\over Z}=1-{\mu\over R}.           \tag{22}
\]

On the other hand

\[
 {F_C(R-1)\over F_C(R)}
 =1-{d-C(\log d+\log e)+o(1)\over R}.                    \tag{23}
\]

Since `kappa<1`, (21)--(23) imply

\[
                  {Z_v\over Z}>{F_C(R-1)\over F_C(R)}    \tag{24}
\]

for all large `R`.  If every face is assigned the same formal weight
`gamma=F_C(R)/Z<=1`, then the total weighted mass is exactly `F_C(R)`, every
one-point deletion has weighted mass at least `F_C(R-1)`, and (22) is the
exact weighted deletion identity.  Thus this law is consistent with the
full one-step minimizer normalization, not merely with `mu=O(d)`.

Finally take three disjoint copies and declare every set meeting two
copies bad once its rank is at least four.  This remains hereditary and
four-local.  Each induced cloud retains the bank (20), while every union
of a nonempty transversal trace from one cloud and a rank-at-least-four
face from another is bad.  The deletion forest must erase one whole side.
The large shadows asserted by Theorem 1 are present, but they do not pay
as ordinary mixed unions.

This last object is an exact abstract four-local regression, not an order
type.  A planar closure must therefore use an axiom absent from arbitrary
bad-four hypergraphs: signed rank-three circuit elimination, tangent-order
coherence, or a minimizer mutation showing that the three-module
anti-alignment can be replaced by a lower-face order type.  That is the
precise additional input left after generalized KK.

## 5. Verification

`verify_rank_heavy_generalized_kk_four_local.py` checks:

1. the constants `a,theta_*,kappa_*`;
2. the uniform analytic lower bound in (11) over a wide finite parameter
   grid;
3. exact formulae (19)--(22), including the per-vertex deletion count;
4. by exhaustive subset enumeration, heredity and four-locality of a
   finite module complex; and
5. the entropy and mean asymptotics along a growing exact sequence.
