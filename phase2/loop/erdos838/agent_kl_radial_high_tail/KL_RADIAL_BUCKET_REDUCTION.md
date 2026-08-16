# Canonical KL as terminal radial distortion

**Date:** 2026-08-14; pointwise-target correction 2026-08-15  
**Verdict:** the two KL estimates needed for Erdős 838 are not proved.  This
note gives an exact reduction of the KL upper bound to an averaged radial
distortion bound, localizes every pointwise failure to a weighted cross-child
collision, and gives a scalable planar warning: canonical peeling KL can be
linear in `n` outside the low-mean branch.  The stronger pointwise statement
`RMC(C,b)` proposed below is now known to be false for every fixed `C,b`; see
`../agent_outer_internal_product/RMC_NESTED_CAP_COUNTEREXAMPLE.md`.

All logarithms are base two.  The notation `pi`, `mathsf P`, `mathsf Q`,
`lambda_ij`, and `d_j(S)` is that of
`../agent_unit_matrix_asymptotic/REPORT.md`.

## 1. Terminal radial buckets give an exact second decomposition

Sample a convex face `U` from the half-Gibbs law

\[
                 \pi(U)={2^{-|U|}\over F(1/2)}.
\]

Put `K=|U|`, `r=floor(K/2)`, and let `C(U)` be the core left after peeling
`r` endpoint pairs.  Thus `C(U)` is empty when `K` is even and is the median
singleton of `U` when `K` is odd.  Define the terminal bucket

\[
                       B(U)=(K,C(U)).                       \tag{1}
\]

If `B=(k,C)`, its cardinality is exactly the radial degree

\[
 d(B)=|\{V:B(V)=B\}|=d_{\lfloor k/2\rfloor}(C).           \tag{2}
\]

All faces in a bucket have the same Gibbs weight, so

\[
              \boxed{\pi(B)=d(B)\pi(U)\quad(U\in B).}     \tag{3}
\]

Let

\[
 L(U)=\prod_{s<\lfloor K/2\rfloor}\lambda_{e_s(U)}
      ={\mathsf Q(U)\over\mathsf P(U)}.                   \tag{4}
\]

The canonical-chain KL is `D=E_pi[-log L(U)]`.  Define the signed terminal
radial distortion

\[
             J=\mathbb E_\pi\log{\pi(B(U))\over L(U)}.     \tag{5}
\]

> **Theorem 1 (radial-bucket KL identity).**
> \[
> \boxed{D(\mathsf P\Vert\mathsf Q)=H(B)+J.}              \tag{6}
> \]
> Moreover
> \[
> \boxed{H(\mathsf P)=H(B)+\mathbb E_\pi\log d(B).}       \tag{7}
> \]

**Proof.**  Add and subtract `-log pi(B(U))` in `-log L(U)` and average;
the first average is `H(B)`, proving (6).  Conditional on `B`, the law of
`U` is uniform on its `d(B)` members, which proves (7).  QED.

There are fewer than `(n+1)^2` possible pairs `(K,C)`, hence

\[
                         H(B)\le2\log(n+1).                \tag{8}
\]

Thus all quadratic KL can only come from `J`; the enormous terminal radial
degrees themselves are already removed exactly by conditional entropy.

## 2. A constant-distortion switching theorem would close the KL upper bound

The following pointwise statement is sufficient but stronger than needed.

> **RMC(C,b) (radial multiplicity capture).**  For every convex face `U`,
> \[
> \boxed{\pi(B(U))\le C^{|U|}n^bL(U)}.                    \tag{9}
> \]

Here `C` and `b` are absolute constants.  Averaging (9), Theorem 1 gives

\[
 D\le H(B)+(\log C)\mu_{1/2}+b\log n.                    \tag{10}
\]

In the only dangerous branch `H(P)>=n^epsilon`, monotonicity gives
`mu_(1/2)<=(1-epsilon)log n`.  Therefore **any** fixed `C,b` in (9) gives

\[
                         D=O(\log n)=o((\log n)^2),        \tag{11}
\]

which is much stronger than the requested KL upper bound.  Pointwise (9)
may be replaced by the averaged statement

\[
                    J\le O(\mu_{1/2}+\log n);             \tag{12}
\]

this is the exact weakest target exposed by (6).

Conversely, the other requested inequality

\[
 \mu_{1/2}+D/\log n\ge(1-o(1))\log n                     \tag{13}
\]

is, up to the harmless `H(B)=O(log n)` term, the assertion

\[
 J\ge(\log n)(\log n-\mu_{1/2})-O(\log n).               \tag{14}
\]

Thus a fixed-power obstruction would force **quadratic positive radial
distortion**, while (9) or (12) limits radial distortion to `O(log n)`.
This cleanly separates the two still-unproved halves of the KL route.

## 3. First failure is an exact weighted cross-child collision

For `0<=j<=r`, let `S_j(U)` be the core after `j` peels and put

\[
 \beta_j(U)=\pi(U)d_j(S_j(U)).                             \tag{15}
\]

This is the total half-Gibbs mass of all rank-`K` faces whose `j`-peeled
core is `S_j(U)`.  In particular

\[
             \beta_0(U)=\pi(U),\qquad \beta_r(U)=\pi(B(U)).\tag{16}
\]

Write `L_j(U)=prod_(s<j)lambda_(e_s(U))` and

\[
                 X_j(U)={\beta_j(U)\over C^{2j}L_j(U)}.    \tag{17}
\]

If (9) fails (even with `b=0`), then `X_r>1`, while `X_0=pi(U)<1`.
At the first crossing `X_j<=1<X_(j+1)`, exact cancellation gives

\[
 \boxed{
 {d_{j+1}(S_{j+1})\over d_j(S_j)}
       >C^2\lambda_{e_j}.}                                \tag{18}
\]

There is no probabilistic or asymptotic loss here.  The radial degrees obey
the exact child recurrence

\[
 d_{j+1}(S)=\sum_{T:\,\operatorname{peel}_1(T)=S}d_j(T).  \tag{19}
\]

So (18) fixes one inner core `S`, one selected parent `T=S_j`, and a large
weighted family of alternative two-ended parents of `S`.  These are exactly
the common-core cross-children in the capped-EIC/shield attack.  The factor
`lambda_(e_j)` measures how much of the full interval face bank the selected
parent captures.  A small capture and a large child sum cannot both be
charged locally without either cross-splicing two parents or banking the
incompatible shield complex.

The standard high-tail identity is compatible with this localization.  If
`tau_j=Pr_pi(K>=2j)` and `rho_j` is the law of the `j`-peeled core conditional
on that event, then

\[
 \mathbb E_\pi d_j=4^j\tau_j,\qquad
 {\rho_j(S)\over\pi(S)}={d_j(S)\over4^j\tau_j},            \tag{20}
\]

and consequently

\[
 D(\rho_j\Vert\pi)=\mathbb E_{\rho_j}\log d_j-2j-\log\tau_j.\tag{21}
\]

Also

\[
 \rho_j\{d_j\ge M\}
 \le {\mathbb E_\pi d_j^2\over M\mathbb E_\pi d_j}.      \tag{22}
\]

The numerator in (22) is literally the weighted number of ordered pairs of
radial extensions sharing one core.  Hence a second-moment proof of the
needed tail bound is a product-face/cross-child collision theorem, not a
generic Markov argument.

## 4. The exact tangent-pocket tail condition that suffices

There is a more flexible averaged target than `RMC(C,b)`, and it interfaces
directly with the current collision theorem.  Fix `j` and a core `S` which
can occur after `j+1` peels.  Its immediate two-ended parents are

\[
 \mathcal P(S)=\{T:\operatorname{peel}_1(T)=S\},\qquad
 w_j(T)=d_j(T),\qquad W_j(S)=d_{j+1}(S)=\sum_Tw_j(T).       \tag{23a}
\]

Conditional on the event `S_(j+1)=S`, the actual parent has the exact law

\[
                       \Pr(T\mid S)={w_j(T)\over W_j(S)}.  \tag{23b}
\]

Indeed every parent `T` has exactly `d_j(T)` outer histories, and all the
resulting faces have the same rank and Gibbs weight.  Put

\[
 c(T)=-\log\lambda_T,qquad
 W_{j,m}(S)=\sum_{T:\lambda_T\le2^{-m}}w_j(T).             \tag{23c}
\]

> **Tangent-pocket capture tail `TPC(delta,A)`.**  Uniformly in `j,S,m`,
> \[
> \boxed{
> {W_{j,m}(S)\over W_j(S)}
> \le\min\{1,A(n)2^{-\delta m}\}}
> \quad(m\ge0),                                           \tag{23d}
> \]
> where `delta>0` is fixed and `A(n)=n^{o(1)}`.

> **Theorem 2 (TPC closes the KL upper bound).**  In the low-mean branch
> `mu_(1/2)=O(log n)`, (23d) implies
> \[
> \boxed{D(\mathsf P\Vert\mathsf Q)=o((\log n)^2).}        \tag{23e}
> \]
> If `A=O(1)`, it gives the stronger `D=O(mu_(1/2))`.

**Proof.**  The layer-cake identity and (23b)--(23d) give

\[
 \mathbb E[c(T)\mid S]
 \le1+\sum_{m\ge1}\min\{1,A2^{-\delta m}\}
 =O_\delta(1+\log A)=o(\log n).                           \tag{23f}
\]

There are `floor(K/2)` parent transitions, whose expectation is at most
`mu_(1/2)/2`.  Sum (23f) over the canonical chain.  QED.

Uniform `TPC` is stronger than the geometry permits outside the hard branch.
Put `N` rational points on a circle inside a large outer triangle.  For a
fixed outer tangent parent, compatible inner traces are supported on a
semicircle-type arc, so

\[
 Z(\mathcal C;1/2)\le N(3/2)^{N/2+O(1)},\qquad
 F_I(1/2)=(3/2)^N.                                      \tag{23f1}
\]

Thus this one parent has `c(T)=Theta(N)`.  At the empty core it has weight
only `Theta(N^-2)` among all two-point parents.  This violates every uniform
exponential tail (23d), but contributes only `O(N^-1)` to the conditional
mean cost.  It is the scalable version of the exact 63-point outer-triangle
tangent-arc barrier in `../agent_planar_tutte/REPORT.md`.  It shows that rare
bad tangent parents must be averaged before imposing a tail bound.

The branch-correct target is therefore activity-weighted.  The high-rank
part can first be removed completely.  Under a fixed-power obstruction,

\[
 \boxed{\mathbb E_\pi2^K={F(1)\over F(1/2)}={n\over H}
              \le n^{1-\epsilon}.}                         \tag{23f2a}
\]

Hence, for `L=log n`,

\[
                     \Pr_\pi\{K\ge4L\}\le n^{-3-\epsilon}.\tag{23f2b}
\]

This tiny probability may be multiplied by a completely crude pointwise
KL bound.  At one peeled endpoint cell with actual residual trace `S`,

\[
 C_e(1/2)\ge(3/2)^{|S|},\qquad
 F_I(1/2)\le(3/2)^{|I|},                                  \tag{23f2c}
\]

because every subtrace of the actual trace is compatible and the full
interval family is contained in the Boolean algebra.  Thus

\[
 -\log\lambda_e\le (|I|-|S|)\log(3/2)<n.                \tag{23f2d}
\]

There are at most `n/2` peels, so every face has total capture cost below
`n^2`.  Combining with (23f2b),

\[
 \boxed{
 \mathbb E_\pi[\mathbf1_{K\ge4L}(-\log L(U))]
 \le n^{-1-\epsilon}=o(1).}                               \tag{23f2e}
\]

Therefore the collision theorem only has to treat faces of rank below
`4log n`; every common core then has `O(log n)` labels, and fixing a core
witness pair really does cost only `O((log n)^2)=n^{o(1)}`.

Conditional on surviving through parent depth `j` **and** on `K<4L`, put

\[
 \Phi_j(m)=\Pr_\pi\{-\log\lambda_{e_j}\ge m
              \mid 2j+2\le K<4L\}
 ={
 \sum_S2^{-|S|}W^{<4L}_{j,m}(S)
 \over
 \sum_S2^{-|S|}W^{<4L}_j(S)}.                            \tag{23f2}
\]

Here the superscript simply restricts the outer histories counted by
`d_j` to total rank below `4L`; the parent law and child recurrence remain
exact after this truncation.

> **Activity-weighted TPC (the live target).**  Under a fixed-power
> obstruction `H>=n^epsilon`, prove
> \[
> \boxed{
> \sup_{j:\Pr(K\ge2j+2)>0}
> \left(1+\sum_{m\ge1}\Phi_j(m)\right)=o(\log n).}       \tag{23f3}
> \]

Exactly the same layer-cake proof, followed by (23f2e), gives

\[
 D\le o(1)+
 \left(\sum_{j\ge0}\Pr(2j+2\le K<4L)\right)o(\log n)
 \le o(1)+{\mu_{1/2}\over2}o(\log n)=o((\log n)^2).     \tag{23f4}
\]

Unlike uniform `TPC`, (23f3) automatically discounts the outer-triangle
parent by its `N^-2` radial weight.  Unlike merely writing `D=o(log^2 n)`,
it is a per-scale tail statement with the exact sources, common cores, and
collision weights exposed.

There is an exact fixed-power bridge to EIC'.  On the truncated law define

\[
 N_j=\sum_S2^{-|S|}W_j(S),\qquad R_T={1\over\lambda_T},    \tag{23f5}
\]

and split parents into dyadic bands

\[
 \mathcal A_{j,m}=\{T:2^m\le R_T<2^{m+1}\},\qquad
 \mathcal D_{j,m}=\sum_{T\in\mathcal A_{j,m}}
             2^{-|S(T)|}d_j(T)R_T.                         \tag{23f6}
\]

> **Theorem 3 (normalized fixed-power band bridge).**  If the
> mixed-product/common-blocker theorem supplies one fixed `delta>0` such
> that, uniformly in `j,m`,

\[
 \boxed{
 \mathcal D_{j,m}
 \le n^{o(1)}2^{(1-\delta)m}N_j,}                          \tag{23f7}
\]

> then activity-weighted TPC (23f3) holds, and hence
> `D(mathsf P||mathsf Q)=o((log n)^2)`.

**Proof.**  Because every term in the band has `R_T>=2^m`, the exact
normalization by `N_j` gives

\[
 {1\over N_j}\sum_{T\in\mathcal A_{j,m}}
       2^{-|S(T)|}d_j(T)
 \le n^{o(1)}2^{-\delta m}.                               \tag{23f8}
\]

Summing the geometric tail proves (23f3) (the `n^{o(1)}` factor costs only
`o(log n)` initial dyadic levels).  In (23f6) every source parent has record
load below `2^(m+1)`, while (23f7) asks for a fixed power saving over that
cap.  This is exactly the form of the fixed-power EIC' gate, now with the
canonical radial weight `2^(-|S|)d_j(T)` and no ambiguous history erasure.
The KL conclusion is (23f4).  QED.

For reference, the exact unconditioned expansion behind this proof is

\[
 D=\sum_{j\ge0}\sum_S{2^{-|S|}\over4^{j+1}F(1/2)}
       \sum_{T\in\mathcal P(S)}d_j(T)(-\log\lambda_T).     \tag{23g}
\]

This is not a reformulation with hidden overlap: every full face occurs
once at each of its peeling depths.

### Why `TPC` is exactly a mixed-product/common-blocker problem

Write a parent as `T=S union {x,y}`, with `x<min S<=max S<y` (with the
obvious conventions for empty or singleton `S`).  Its capture is

\[
 \lambda_T={Z(\mathcal C_{xy};1/2)\over F((x,y);1/2)},     \tag{23h}
\]

where `mathcal C_xy` is the family of interval traces `W` for which
`W union {x,y}` is convex.  Therefore `lambda_T<=2^{-m}` says that all but
a `2^{-m}` fraction of the interval face bank is blocked by the two-ended
parent.

Two elementary planar facts make the collision state canonical.

1. For every blocked interval face `W`, choose an inclusion-minimal
   `Y subseteq W` such that `{x,y} union Y` is nonconvex.  Since `{x,y}` is
   a nonempty closed set in general position, the rooted-cluster reduction
   gives `2<=|Y|<=3`.  Since the shared core `S` is compatible with `x,y`,
   `Y` is not contained in `S`; it contains a genuine pocket blocker.
2. Take two parents `S union {x,y}` and `S union {a,b}`.  If the mixed parent
   `S union {x,b}` is nonconvex, then there are `p,q in S` such that
   `{x,b,p,q}` is a four-circuit.  Indeed `S union {x}` and `S union {b}`
   are convex by deletion.  A minimal nonconvex subset of their union is a
   four-circuit in planar general position and must contain both `x,b`;
   its other two labels lie in `S`.  The same holds for the other mix.

Consequently the ordered weighted parent-pair mass `W_{j,m}(S)^2` has only
three destinations:

* both mixed parents exist, giving a genuine two-by-two product rectangle;
* many pairs share a left or right endpoint, giving a common-endpoint
  tangent child; or
* a mixed parent fails, and a four-circuit witness `(p,q)` in the common
  core is fixed.

In the low-rank branch `|S|=O(log n)`, there are only `O((log n)^2)=n^{o(1)}`
choices for `(p,q)` and only constantly many circuit orientations.  Thus a
positive fraction of incompatible pair mass fixes a canonical common
blocker at subpower loss.  This is precisely the input expected by the
common-blocker/shield alternative in
`../agent_heavy_prefix_rotation/HEAVY_PREFIX_ROTATION_DESCENT.md` and
`../agent_quadratic_cross_core/QUADRATIC_CROSS_CORE_SHIELD.md`.

What is still missing is the quantitative last arrow: use those product
rectangles or the fixed shield child to prove the exponential capture tail
after the activity-weighted sum over `S`, as required by (23f3).  Cores with
`|S|<4log n`, so fixing `(p,q)` loses only `O((log n)^2)=n^{o(1)}`.  The
high-rank contribution is already rigorously negligible by (23f2e).  The
classification above is exact; the remaining global bounded-reuse estimate
on the low-rank activity-weighted parent law is not yet proved.

As a finite stress test, the largest conditional mean in (23f), over every
visited `(j,S)`, is `6.63511` bits in n58, `4.37121` bits in Pascal36, and
`2.24700` bits in alternating30.  These bounded values are consistent with
`TPC`, but the first two are too large for a naive one-bit-per-peel claim.

## 5. The multiplicity-one strengthening is false

It is tempting to strengthen the previously audited planar inequality
`L(U)>=pi(U)` by the whole radial multiplicity and conjecture

\[
                         L(U)\ge\pi(B(U)).                 \tag{23}
\]

This is false in the principal exact tests.  In the saved 58-wire record,
the face

\[
                     U=(3,5,6,53,56,57)
\]

has terminal bucket size `284024`,

\[
 L(U)=3.91284\cdot10^{-6},\qquad
 \pi(B(U))=0.121271,
\]

so `log(pi(B)/L)=14.9197` bits.  The largest audited gaps are `10.7354`
bits in Pascal36 and `4.6540` bits in the alternating family at `n=30`.
Thus the constant-per-vertex allowance in (9) is load-bearing.

On the other hand `RMC(8,0)` holds exactly in all of the following finite
audits:

* all `2,8,62,908` packet-sign reflection classes through `n=6`;
* 100 deterministic random straight-line configurations at `n=14`;
* every face in the 58-wire record and Pascal36; and
* every face of the stretchable alternating family at `n=30`.

This is evidence and not a theorem.  The value `8` has not been optimized.

These finite audits do not extend universally.  Two vertically separated
concave caps give a rank-four face whose two nested endpoint cells both
charge essentially the same Boolean reservoir.  For `m` low-cap points the
exact ratio `pi(B)/L` is `Omega((3/2)^m/m^2)`, so it defeats every fixed
`C^4n^b`; exact evaluation already defeats `RMC(8,0)` at `m=21` (`n=27`).
The face has exponentially small
half-Gibbs probability, so this kills only pointwise capture, not the
activity-weighted average target (12).

## 6. Canonical KL itself has a scalable linear planar barrier

The low-mean hypothesis in (10) cannot be dropped.  Consider the stretchable
alternating family with

\[
                         \chi(i,j,k)=(-1)^i.
\]

For endpoint distance `d`, one temporal direction is direct and the other
has polynomial

\[
 R_d(t)=t+t^2\sum_{s=1}^{d-1}(1+t)^{\lfloor(s-1)/2\rfloor}.\tag{24}
\]

At `t=1/2`, with `q=3/2`,

\[
 R_{2k}={5\over4}q^{k-1}-{1\over2},\qquad
 R_{2k+1}=q^k-{1\over2}.                                 \tag{25}
\]

The full interval partition functions are

\[
\begin{aligned}
 F_{2k}(1/2)&=10q^k-{k^2\over2}-{13k\over4}-9,\\
 F_{2k+1}(1/2)&={49\over4}q^k-{k^2\over2}-{15k\over4}-{43\over4}.
\end{aligned}                                             \tag{26}
\]

Since the endpoint cell is `(1/2)R_d(1/2)`, its capture is

\[
                     \lambda_d={2R_d(1/2)\over F_{d-1}(1/2)}.\tag{27}
\]

Equations (25)--(27) give

\[
 \lambda_1=\lambda_2=1,\qquad
             {1\over5}\le\lambda_d\le{8\over9}\quad(d\ge3).\tag{28}
\]

A rank-`K` face has at least `floor(K/2)-1` peeled endpoint pairs of label
span at least three.  Therefore

\[
 \log(9/8)\left({\mu_{1/2}\over2}-{3\over2}\right)
 \le D(\mathsf P\Vert\mathsf Q)
 \le {\log5\over2}\mu_{1/2}.                              \tag{29}
\]

The exact sums in (24) also give

\[
                         \mu_{1/2}={n\over6}+O(1).          \tag{30}
\]

Hence canonical peeling KL is `Theta(n)` on a straight-line, once-per-root
reflection family.  This is a counterexample to every unconditional
`D=o((log n)^2)` claim.  It does not obstruct (10): the same family is in a
linear-mean, exponentially benign branch.  In fact (28) gives
`L(U)>=5^{-K/2}`, so it satisfies `RMC(sqrt(5),0)` trivially because
`pi(B)<=1`.

## 7. What remains

The KL upper target is reduced to proving the averaged bound (12) from
planar reflection signs; the stronger pointwise target (9) is unavailable.
Equivalently it is enough to prove the explicit activity-weighted
capture-tail statement (23d).  The first-crossing formula (18)--(19) and the
parent-pair classification after (23h) say exactly where to use geometry: a
violating face fixes a heavy weighted family of two-ended parents around one
common core.  Compatible parent pairs should cross-splice; persistent
incompatibility fixes a core witness pair and should create the quadratic
shield bank already isolated in
`../agent_quadratic_cross_core/QUADRATIC_CROSS_CORE_SHIELD.md`.

The separate lower target (13) is still open.  By (6), it is equivalent to
the quadratic lower bound (14) on the same radial distortion.  Thus a full
KL closure now has a sharp contradiction format: a power-law obstruction
must make `J=Omega((log n)^2)`, while a constant-distortion cross-child
switching theorem makes `J=O(log n)`.

## 8. Verification

Run

```bash
python3 \
  phase2/loop/erdos838/agent_kl_radial_high_tail/verify_kl_radial_bucket.py
```

The verifier uses exact rational face weights and capture products.  It
checks (3), (6), (7), (15)--(22), the parent law (23b), the expansion (23g),
the failure of the multiplicity-one statement, and `RMC(8,0)` on
the finite families listed above.  It separately verifies the closed forms
(25)--(28), reconstructs the alternating graded polynomial, and checks the
linear-mean asymptotic in (30).
