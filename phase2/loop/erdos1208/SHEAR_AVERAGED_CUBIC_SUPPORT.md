# Shear-averaged cubic support

## Status

The rotation-averaged theorem in `ROTATION_AVERAGED_CUBIC_SUPPORT.md` uses
radial uniqueness to show that a fixed collision can occur at only one
rotation.  There is a complementary affine statement.  Put

\[
 S_t=J+tI,\qquad t\in\mathbb R,
\]

where `J` is quarter-turn.  A fixed collision can now survive for several
parameters, but all of its realized edge vectors lie on one affine line in
the difference set.  Maximum collinearity of the original point set controls
that line section exactly.

The result does **not** control the prescribed value `t=0`, and the number of
shears required is too large for the ordinary square grid once denominator or
box expansion is included.  Its value is twofold:

1. it gives a second exact many-symmetry interface for a hostile
   construction; and
2. it proves that an exceptional quarter-turn cannot be removed merely by
   averaging over a bounded or linearly growing family of nearby affine
   deformations.

The finite identities are checked by `verify_shear_averaged_support.py`.

## 1. A line-section lemma for complete difference sets

Let `A` be a distance-Sidon set of `k` points in the plane, let

\[
 D=A-A,
\]

and let `L` be the maximum number of collinear points of `A`.  Then every
affine line `ell` in the vector plane satisfies

\[
 \boxed{|D\cap\ell|\le kL.}                     \tag{1.1}
\]

To prove this, write

\[
 \ell=\{v:n\mathbin\cdot v=c\}
\]

for a nonzero normal vector `n`, and group the points of `A` by their
projection `n dot a`.  If the occupancies of the projection fibres are
`k_h`, then every `k_h` is at most `L`.

When `c` is nonzero, every vector in `D cap ell` has a unique ordered
representation because `A` is vector-Sidon.  Therefore

\[
 |D\cap\ell|
 =\sum_h k_hk_{h-c}
 \le L\sum_hk_h=kL.                              \tag{1.2}
\]

When `c=0`, the zero vector is represented many times but occurs only once as
a member of `D`.  Hence

\[
 |D\cap\ell|
 =1+\sum_h k_h(k_h-1)
 \le1+(L-1)k\le kL.                              \tag{1.3}
\]

This proves (1.1).  The statement is sharp up to constants for unions of
parallel rulers.

## 2. The averaged shear theorem

For real `t`, define

\[
 \Phi_t(a,b,c)=a+S_t(b-c),
\]

and let

\[
 \mathcal E_t(A)
 =\#\{(a,b,c,a',b',c')\in A^6:
       \Phi_t(a,b,c)=\Phi_t(a',b',c')\}.
\]

If `mathcal T` is any finite set of `r` distinct real parameters, then

\[
 \boxed{
 \sum_{t\in\mathcal T}\mathcal E_t(A)
 \le r(2k^3-k^2)+k^5L.}                         \tag{2.1}
\]

Consequently some `t in mathcal T` satisfies

\[
 \mathcal E_t(A)
 \le2k^3-k^2+\frac{k^5L}{r},                    \tag{2.2}
\]

and therefore

\[
 \boxed{
 |A+S_t(A-A)|
 \ge\frac{k^6}{2k^3-k^2+k^5L/r}.}              \tag{2.3}
\]

In particular,

\[
 r\ge k^2L
 \quad\Longrightarrow\quad
 |A+S_t(A-A)|\ge\frac13k^3.                     \tag{2.4}
\]

### Proof

A collision is equivalent to

\[
 a-a'=S_tw,
 \qquad
 w=(b'-c')-(b-c).                                \tag{2.5}
\]

Every `S_t` is invertible, since its determinant is `1+t^2`.  If `a=a'`,
then (2.5) forces `w=0`.  The exact ordered difference energy of a
vector-Sidon set is

\[
 \#\{(b,c,b',c'):b-c=b'-c'\}=2k^2-k.            \tag{2.6}
\]

Thus the collisions with `a=a'` contribute exactly
`2k^3-k^2` for each parameter.

Now fix `(b,c,b',c')` with `w` nonzero and suppose `a!=a'`.  As `t` varies,
the vector on the right of (2.5) runs injectively along the affine line

\[
 \ell_w=Jw+\mathbb Rw.                           \tag{2.7}
\]

Every realized nonzero vector `a-a'` has one ordered representation.  By
(1.1), at most `kL` values of `t` from `mathcal T` can therefore solve (2.5),
including the choice of `(a,a')`.  There are `k^4` ordered quadruples, so all
non-diagonal collisions summed over `mathcal T` contribute at most `k^5L`.
This proves (2.1).  Equation (2.3) is the usual fibre Cauchy--Schwarz bound.

## 3. Hostile-box criterion

Let `P` be a finite planar set.  Suppose that for each `t in mathcal T` there
is a finite set `Omega_t` such that

\[
 P+S_t(P-P)\subseteq\Omega_t,
 \qquad |\Omega_t|\le M.                         \tag{3.1}
\]

If every distance-Sidon subset `A subseteq P` has maximum collinearity at
most `L`, then (2.3) gives

\[
 M\ge\frac{k^6}{2k^3-k^2+k^5L/r}.               \tag{3.2}
\]

In particular, `r>=k^2L` forces `k<=(3M)^(1/3)`.

Unlike exact unit rotations, integral shears of size `t` expand a square box
by a factor of order `1+t^2`; rationally packing many shears incurs the same
denominator-square cost.  Thus (3.2) is an exact construction interface, not
a square-grid solution.

## 4. Relation to the exceptional-quarter-turn gate

The theorem shows precisely what an averaging argument loses.  For rotations,
one fixed four-tuple contributes to at most two directed edges over the whole
family.  For shears, it may contribute at every point of an affine line
section of `D`, and (1.1) permits `kL` such points.  The certified heavy-row
examples have square-root-heavy affine structure, so replacing `kL` by a
subpolynomial quantity is false in the relevant regime.

The remaining full-resolution target is still a theorem about the prescribed
quarter-turn `S_0=J`, such as the global transverse fourth-moment estimate in
`TRANSVERSE_SECOND_MOMENT_GATE.md`, or an inverse theorem that sends its
exceptional energy into the parallel-line support lemma.
