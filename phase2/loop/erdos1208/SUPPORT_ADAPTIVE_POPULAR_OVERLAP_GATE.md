# The support-adaptive popular-overlap gate

## 1. Exact tail reduction

Let `A` be a planar distance-Sidon set, put

\[
 D=A-A,\qquad N=|D|,
 \qquad S=|D+D|,
\]

and let `J(x,y)=(-y,x)`.  Write

\[
 R(q)=|D\cap(D+q)|,
 \qquad
 \mathcal E_\perp(D)=\sum_q R(q)R(Jq).
 \tag{1.1}
\]

The full cube-root upper bound follows from

\[
 \mathcal E_\perp(D)\le N^{1+o(1)}S.
 \tag{1.2}
\]

There is an exact support-adaptive reduction of (1.2).  Set

\[
 K={S\over N}
 \quad\hbox{and}\quad
 \mathcal P_K=
 \{q\ne0:R(q)>K\hbox{ and }R(Jq)>K\}.
 \tag{1.3}
\]

Then

\[
 \boxed{
 \mathcal E_\perp(D)
 \le 3NS+\sum_{q\in\mathcal P_K}R(q)R(Jq).}
 \tag{1.4}
\]

Indeed the zero shift contributes `R(0)^2=N^2<=NS`.  Among the nonzero
shifts with `R(q)<=K`, the contribution is at most

\[
 K\sum_qR(Jq)=KN^2=NS.
\]

Of the remaining shifts, those with `R(Jq)<=K` contribute at most another
`NS`.  This proves (1.4).

Consequently the full problem is reduced to the rich-tail estimate

\[
 \boxed{
 \sum_{q\in\mathcal P_K}R(q)R(Jq)
 \le N^{1+o(1)}S.}
 \tag{1.5}
\]

This is strictly sharper than merely asking for a global common-energy
bound: the cutoff changes with the ordinary support.  A set with nearly
maximal support has `K` near `N`, so its structured energy peaks disappear
from the tail automatically.

## 2. Dyadic form

For dyadic `lambda,mu>K`, define

\[
 \mathcal P_{\lambda,\mu}
 =\{q\ne0:\lambda<R(q)\le2\lambda,
                 \ \mu<R(Jq)\le2\mu\}.
 \tag{2.1}
\]

Up to `N^{o(1)}` logarithmic factors, (1.5) is equivalent to

\[
 |\mathcal P_{\lambda,\mu}|
 \le {N^{1+o(1)}S\over\lambda\mu}
 \qquad(\lambda,\mu>K).
 \tag{2.2}
\]

The generic estimates

\[
 |\{q:R(q)>\lambda\}|\le {N^2\over\lambda},
 \qquad
 |\{q:R(q)>\lambda\}|\le {E_+(D)\over\lambda^2}
\]

do not prove (2.2).  The required saving must come from simultaneously
popular quarter-turned shifts and from the fact that `D` is the complete
difference set of a distance-Sidon endpoint set.

## 3. Calibration and barriers

The exact verifier computes the decomposition in (1.4).

* On the transformed finite-field parabola, the dense perpendicular ruler,
  and the 18-point quadratic fibre gadget, the nonzero rich tail is empty.
* On the stored complete-difference closure chain, the normalized nonzero
  tail remains below `0.007 NS` through 70 points.
* On the abstract radially unique transversals which are not complete
  difference sets, the normalized tail grows rapidly: it is already above
  `2 NS` at side 8 and above `16 NS` at side 30.

Thus the adaptive cutoff removes every presently known genuine obstruction
while retaining the same separation between complete differences and
abstract radial sets as the full product conjecture.

Dense perpendicular Golomb rulers are the decisive correction to the false
energy-product gate.  They have both ordinary and orthogonal energy on the
`N^3` scale, but also `S` on the `N^2` scale.  Hence `K` is on the `N` scale
and their nonzero popular tail is empty.  This is precisely the compensation
that a support-free uncertainty inequality missed.

## 4. The remaining mathematical task

The useful live regime may assume both

\[
 S<N^{5/3-o(1)}
 \tag{4.1}
\]

by the Ruzsa high-support branch, and that `A` is not covered by
`N^{o(1)}` parallel lines, by the parallel-cover theorem.

A proof of (1.5) should therefore establish one of the following equivalent
types of inverse statement for every dyadic class (2.1):

1. **support creation:** the uniquely decorated endpoints of the popular
   overlaps create at least `lambda*mu*|P|/N^(1+o(1))` ordinary sums;
2. **parallel concentration:** a violation of (2.2) puts a large fraction of
   `A` on subpolynomially many parallel lines; or
3. **forbidden rotation-stable model:** a violation produces a structured
   rank-two component of `D` stable enough under `J` to force two equal
   Euclidean norms.

The natural technical entry points are a simultaneous Katz--Koester
transform for `D_q=D\cap(D+q)`, the seven-incidence endpoint-switching
identity from `ORTHOGONAL_SWITCHING_RICH_TAIL_GATE.md`, and small-doubling
structure applied only after the adaptive cutoff.  Global ordinary energy,
maximum-fibre, and pointwise overlap estimates have all been disproved and
must not be reintroduced.

`SUPPORT_ADAPTIVE_RICH_FIBRE_GATE.md` gives the sharpest physical-space
form.  It factors the tail exactly over labels `(u,s) in D x (D+D)`.  One
rich fibre `Q` places three affine copies of `Q` inside `D`; popularity and a
pigeonhole step place two further copies of a subset
`Q'` of size greater than `|Q|K^2/N^2`.  A subpolynomial first or second
moment for these adaptive loads would finish the proof.

Run `verify_support_adaptive_popular_overlap_gate.py` for the exact
decomposition and calibration profiles.
