# Completion-corner metric inversion on every resonance

## 1. Outcome

The six-gap Jacobian for a repeated decorated endpoint key has three zero
factors.  Those factors are necessary if one asks the six metric gaps alone
to recover the whole centre.  They are not local multiplicity obstructions
once one completion corner of the reverse record is retained.

Fix nonzero `u,d`, a decorated collision displacement `s`, and put

\[
 \gamma=-Js-Ld,\qquad \beta=-J(s+d).              \tag{1.1}
\]

For one occurrence write

\[
 A=c-q,\qquad B=\ell+Jp,\qquad C_1=B+t,
 \qquad p=q+t.                                    \tag{1.2}
\]

The original metric gaps on the `B,C_1` pairs and the recursive gaps are

\[
\begin{aligned}
 g_1&=|B+\beta|^2-|B|^2,
 &h_1&=|B-Ju|^2-|B|^2,\\
 g_2&=|C_1+\gamma|^2-|C_1|^2,
 &h_2&=|C_1-Ju|^2-|C_1|^2.                       \tag{1.3}
\end{aligned}
\]

There are three exhaustive cases.

1. If `gamma dot u != 0`, the `p`-side completion corner
   `kappa_p=(p,A,ell)` determines `B`, and `(g_2,h_2)` recovers `C_1`
   and hence `t`.  The affine Jacobian in `t` has magnitude
   `4|gamma dot u|`.
2. If `gamma dot u=0` but `det(s+d,u)!=0`, the `q`-side corner
   `kappa_q=(q,A,W)`, `W=ell+Lt`, determines `C_1=W+Jq`, and
   `(g_1,h_1)` recovers `B` and hence `t`.  The affine Jacobian has
   magnitude `4|det(s+d,u)|`.
3. If both quantities vanish, `kappa_q` still determines
   `c=A+q` and `C_1`.  The value `h_1` fixes `t dot Ju`; adjoining the
   absolute metric label

   \[
      \nu_V=|c+t|^2                                  \tag{1.4}
   \]

   leaves at most two possible integer vectors `t`.

Thus

\[
\boxed{
 (\kappa_p,g_2,h_2)\quad\text{or}\quad
 (\kappa_q,g_1,h_1)\quad\text{or}\quad
 (\kappa_q,h_1,\nu_V)
}
                                                               \tag{1.5}
\]

recovers every resonant collision with multiplicity at most two.  The
choice is canonical from `(s,d,u)`.  In particular the small-star branch
left by the off-diagonal footprint theorem has no local metric degeneracy.
Its remaining difficulty is only the global packing of these
completion-corner metric keys.

## 2. Generic completion-corner inversions

The corner `kappa_p=(p,A,ell)` gives

\[
 B=\ell+Jp.                                        \tag{2.1}
\]

As affine functions of `t`, the two last-pair gaps have linear coefficient
rows `2gamma` and `-2Ju`.  Since

\[
 \det(\gamma,Ju)=\gamma\cdot u,                   \tag{2.2}
\]

their determinant has magnitude `4|gamma dot u|`.  This proves Case 1.

For Case 2, the corner `kappa_q=(q,A,W)` gives

\[
 C_1=W+Jq.                                         \tag{2.3}
\]

Now `B=C_1-t`.  The two middle-pair gaps have coefficient directions
`beta=-J(s+d)` and `-Ju`.  Their determinant has magnitude

\[
 4|\det(\beta,Ju)|=4|\det(s+d,u)|.                \tag{2.4}
\]

They recover `B`, and hence `t=C_1-B`.

## 3. The final double resonance is quadratically two-to-one

Assume

\[
 \gamma\cdot u=0,\qquad \det(s+d,u)=0.            \tag{3.1}
\]

Then `beta` is parallel to `Ju`, so the middle gaps retain only one linear
projection.  The nonzero recursive direction still makes `h_1` determine
`B dot Ju`, and therefore `t dot Ju` because `C_1` is fixed by (2.3).

The same `q`-corner gives `c=A+q`.  If two candidates `t,t'` have the same
`h_1`, then `t'-t=lambda u`.  Equality of the complementary-neighbour
lengths gives

\[
 |c+t+\lambda u|^2-|c+t|^2
 =\lambda\bigl(2(c+t)\cdot u+\lambda|u|^2\bigr)=0. \tag{3.2}
\]

There are at most two real, hence at most two integer, values of `lambda`.
This proves Case 3.  If the directed complementary label `c+t` rather than
only its squared norm is retained, the recovery is one-to-one.

The label (1.4) is always available: `c+t` is the other directed difference
of the same physical neighbour cell, whether or not the selected endpoint
lies on that side.  No new geometric object is introduced.

## 4. Exact classification of resonance intersections

Write, in the real basis `(u,Ju)`,

\[
 s=a u+bJu,\qquad d=c u+eJu.                      \tag{4.1}
\]

The three resonance equations become

\[
 q:\ b=0,\qquad
 p:\ b+e=0,\qquad
 D:\ b-c+e=0.                                    \tag{4.2}
\]

Since `d!=0`, no triple resonance is possible.  The three pairwise
intersections are exactly

\[
\boxed{
 q\cap p:\ d\parallel u,\qquad
 q\cap D:\ d\parallel Lu,\qquad
 p\cap D:\ d\parallel Ju.}                      \tag{4.3}
\]

The last line is precisely Case 3 above; it also shows that the remaining
quadratic fibre is geometrically one-dimensional rather than a hidden
rank-two exception.  These identities explain why the exact stored
resonance masks have no triple intersection.

## 5. Consequence for the direct program

The repeated-key branch now has a clean local partition.

* Stars of size at least four are charged by the off-diagonal quadratic
  footprint and its simple completion-edge graph.
* Stars of size at most three are refined by (1.5); every local fibre has
  multiplicity at most two.

Both pieces now fail only at the same global point: summing distinct
endpoint-labelled completion edges/metric keys without paying an ambient
boundary term once per centre.  There is no separate parabolic or resonant
local classification left to discover.

The next theorem should therefore be stated directly as a Carleson packing
estimate on `mathcal V_K`: low completion-edge reuse is paid by the existing
parallel-wedge reservoir, while high reuse forces a common four-corner link
rectangle.  Reverting to unlabelled line counts would discard the bounded
local inverse proved here.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_resonance_completion_corner_metric_inversion.py
```

The verifier exhausts the resonance intersection equations on integer
boxes, checks both affine Jacobians, reconstructs random records in Cases 1
and 2, and exhausts the two-to-one quadratic fibre in Case 3.
