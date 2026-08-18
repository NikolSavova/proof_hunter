# Gaussian-core height bound for arbitrary oblique lattice patches

## 1. Why this branch remains

An adaptive rich fibre contains both

\[
 u+Q\subset D,
 \qquad w-(I+J)Q\subset D.                       \tag{1.1}
\]

If `Q` is a complete patch of a lattice `Lambda`, (1.1) does **not** imply
`J Lambda=Lambda`; it merely gives a second patch in `(I+J)Lambda`.
Therefore `GAUSSIAN_IDEAL_COSET_HEIGHT.md` does not by itself close every
exact oblique lattice model.

There is nevertheless a universal partial theorem.  Every integral lattice
has a canonical finite-index Gaussian core, and the critical Gaussian height
bound can be applied to a square patch in that core.

## 2. Preliminary universal `r^(6/5)` height theorem

### Theorem 2.1

There are absolute constants `c>0` and `r_0` such that the following holds.
Let `v,w` be linearly independent vectors in `Z^2`, let `t in Z^2`, and put

\[
 \mathcal P={t+a v+b w:0\le a,b<r\}.            \tag{2.1}
\]

Suppose `r>=r_0`, `mathcal P subset [-M,M]^2`, and no two distinct
non-antipodal points of `mathcal P` have the same norm.  Then

\[
 \boxed{M\gg r^{6/5}.}                            \tag{2.2}
\]

This preliminary exponent is superseded by the sharp modular-midpoint
Theorem 7.1 below.  It is retained because the Gaussian-core argument is a
useful independent proof and explains why a direct treatment of arbitrary
oblique bases is necessary.

### Proof

Let `L` be the integer matrix with columns `v,w`, write

\[
 \Delta=|\det L|,
 \qquad B=\max\{|v|,|w|,1\}.                     \tag{2.3}
\]

The diameter of (2.1) immediately gives

\[
 M\gg rB.                                        \tag{2.4}
\]

The adjugate identity

\[
 L\,\operatorname{adj}(L)=(\det L)I             \tag{2.5}
\]

exhibits the Gaussian core

\[
 \Delta\mathbb Z^2\subseteq L\mathbb Z^2.       \tag{2.6}
\]

Every entry of `adj(L)` has magnitude at most `B`.  Choose a central
coefficient vector `x_0 in [0,r)^2` and let `y` run through a square integer
box of side

\[
 R=\left\lfloor c_0{r\over B}\right\rfloor       \tag{2.7}
\]

centred at zero, where `c_0` is a sufficiently small absolute constant.
Then

\[
 x_0+\operatorname{adj}(L)y\in[0,r)^2            \tag{2.8}
\]

throughout that box.  Equations (2.5) and (2.8) show that `mathcal P`
contains a complete square patch

\[
 t_0+(\det L)\{a+ib:0\le a,b<R\}                \tag{2.9}
\]

after harmless reflections and reindexing.

If `t_0` is a nonzero coset modulo `(det L)Z[i]`, Theorem 1.1 of
`GAUSSIAN_IDEAL_COSET_HEIGHT.md` gives

\[
 M\gg R^{3/2}.                                   \tag{2.10}
\]

If `t_0` belongs to that ideal, divide (2.9) by `Delta`.  Proposition 1.1 of
`UNIT_LATTICE_RICH_FIBRE_HEIGHT.md` gives the stronger estimate

\[
 {M\over\Delta}+R\gg R^2,
 \qquad\hbox{hence}\qquad M\gg R^{3/2}.          \tag{2.11}
\]

For large `R`, the first inequality gives `M/Delta>>R^2`; the displayed
weaker consequence uses `Delta>=1`.  If `R` is bounded,
(2.7) already makes `B` a constant multiple of `r`, and (2.4) is stronger
than (2.2).  Otherwise (2.4), (2.7), and (2.10)--(2.11) yield

\[
 M\gg\max\left\{rB,\left({r\over B}\right)^{3/2}\right\}.
                                                            \tag{2.12}
\]

The two terms balance at `B=r^(1/5)`, where both are `r^(6/5)`.
This proves (2.2).

## 3. Rectangular and rich-fibre form

For an `r`-by-`s` coefficient patch with `r>=s`, apply Theorem 2.1 to an
`s`-by-`s` subpatch.  It gives

\[
 s\ll M^{5/6}.                                    \tag{3.1}
\]

The patch is also covered by `s` parallel lines.  In an adaptive rich fibre,
the collinear theorem gives `r<=sqrt(S)`.  Consequently

\[
 \boxed{|Q|=rs\ll M^{5/6}\sqrt S}.               \tag{3.2}
\]

For a `J`-stable lattice, the arbitrary-ideal theorem improves `5/6` to
`2/3`.  Theorem 7.1 below obtains the same improvement for every complete
exact integral oblique lattice, so (3.2) is now only the preliminary
Gaussian-core consequence.

## 4. Historical oblique gate

Let `G=L^T L`.  A collision between coefficient points `x` and `x+2n`
is equivalent to the linear Diophantine equation

\[
 (Gn)\mathbin\cdot x
 =-n^T L^Tt-n^TGn.                                \tag{4.1}
\]

Indeed the difference of their squared norms is four times the two sides of
(4.1).  The Gaussian-core argument restricts to
`n=adj(L)y`, for which `L n=(det L)y`; keeping only a square of such
directions loses the factor `B` in (2.7).

At this stage the critical exact-oblique theorem was:

> If the full `r`-by-`r` patch is radially unique, prove directly from
> (4.1) that `M>>r^(3/2)`, without first restricting to the Gaussian core.

Equivalently, one needs a short inhomogeneous solution of (4.1) whose two
coefficient points remain in the box.  The issue is simultaneous angular
approximation and the divisibility condition

\[
 \gcd((Gn)_1,(Gn)_2)\mid n^TL^Tt+n^TGn.         \tag{4.2}
\]

Section 7 solves this gate directly.  The key is to choose the midpoint
first modulo a prime `q` larger than `|det L|`; the perpendicular direction
then becomes integral automatically.  No extra rich-fibre copy is required.

## 5. Verification

`verify_oblique_lattice_gaussian_core.py` checks (2.5)--(2.9) for a family
of primitive, nonprimitive, anisotropic, and highly sheared integer bases.
It also checks the collision identity (4.1) on exact random coefficient
pairs and confirms the exponent optimization in (2.12) using rational
inequalities.

## 6. The critical exponent `3/2` is sharp

The desired improvement of Theorem 2.1 cannot go beyond `3/2`.  For every
integer `B>=2`, set `r=B^2` and consider the unimodular shear patch

\[
 \mathcal S_B=
 \{(B(a+b)+b,a+b):0\le a,b<r\}.                 \tag{6.1}
\]

It has `r^2` pairwise distinct squared norms.  To prove this, put

\[
 s=a+b,\qquad x=Bs+b.
\]

Suppose `(x,s)` and `(x',s')` have the same norm.  If `s=s'`, then
`x=x'`, hence `b=b'` and `a=a'`.  Otherwise orient the pair so that
`s'>s`.  Equality of norms forces `x'<x`.  Write

\[
 k=s'-s>0,
 \qquad h=x-x'=b-b'-Bk>0.                       \tag{6.2}
\]

Factoring the equality of squares gives

\[
 h(x+x')=k(s+s').                                \tag{6.3}
\]

Because `x+x'>=B(s+s')`, equation (6.3) gives `hB<=k`, so `k>=B`.
On the other hand, (6.2) and `b-b'<=r-1=B^2-1` give

\[
 Bk+1\le B^2-1,
\]

so `k<=B-1`, a contradiction.  Thus (6.1) is radially unique.

The basis vectors are `(B,1)` and `(B+1,1)`, with determinant `-1`, and

\[
 \mathcal S_B\subset
 [0,(2B+1)(r-1)]\times[0,2(r-1)].                \tag{6.4}
\]

Hence its containing height is `O(Br)=O(r^(3/2))`.  This proves that the
critical oblique theorem established in Section 7 has the best possible
exponent.  It also supplies the extremal model for the modular-midpoint
argument.

## 7. Sharp modular-midpoint theorem

### Theorem 7.1

There are absolute constants `c>0` and `r_0` such that the following holds.
Let `L` be any nonsingular matrix in `M_2(Z)`, let `t in Z^2`, and put

\[
 \mathcal P=\{t+Lx:x\in\{0,\ldots,r-1\}^2\}.
                                                        \tag{7.1}
\]

If `r>=r_0`, `mathcal P subset [-M,M]^2`, and no two distinct
non-antipodal points of `mathcal P` have the same norm, then

\[
 \boxed{M\gg r^{3/2}.}                            \tag{7.2}
\]

Together with Section 6, the exponent `3/2` is best possible.

### Proof

Write the columns of `L` as `v,w` and set

\[
 B=\max\{|v|,|w|\},\qquad G=L^TL.               \tag{7.3}
\]

Comparing the two patch points with coefficient vectors `(0,0)` and
`(r-1,0)`, and then `(0,0)` and `(0,r-1)`, gives

\[
 B\le {2\sqrt2 M\over r-1}\le {6M\over r}       \tag{7.4}
\]

for `r>=2`.

Suppose, for a contradiction, that

\[
 M<c r^{3/2},                                    \tag{7.5}
\]

where `c>0` is a sufficiently small absolute constant.  For all sufficiently
large `r`, Bertrand's postulate supplies a prime

\[
 {r\over100}<q<{r\over40}.                       \tag{7.6}
\]

By (7.4),

\[
 0<|\det L|\le B^2<36c^2r<q                     \tag{7.7}
\]

once, for example, `c<=1/100`.  Therefore `G` is invertible modulo `q`,
because `det G=(det L)^2`.

Put `d=L^Tt`.  There is a unique residue class `m_0 in (Z/qZ)^2` satisfying

\[
 Gm_0\equiv-d\pmod q.                           \tag{7.8}
\]

Choose an integer representative `m` of this class with both coordinates
in the central interval `[r/3,2r/3]`.  The interval has length `r/3` while
`q<r/40`, so there are many such representatives in each coordinate.  Since
`L` is nonsingular, at most one of the resulting coefficient vectors can
satisfy `t+Lm=0`; choose one for which

\[
 p:=t+Lm\ne0.                                    \tag{7.9}
\]

Now

\[
 a:=L^Tp=d+Gm\in q\mathbb Z^2.                  \tag{7.10}
\]

Let `J(x,y)=(-y,x)` and define

\[
 n=J(a/q)\in\mathbb Z^2.                        \tag{7.11}
\]

The choice (7.9) and nonsingularity of `L^T` imply `a\ne0`, hence `n\ne0`.
Moreover, because `p in [-M,M]^2`, each coordinate of `a` has magnitude at
most `sqrt(2)BM`.  Equations (7.4)--(7.6) therefore give

\[
 \|n\|_\infty
 \le {\sqrt2BM\over q}
 < {100\sqrt2BM\over r}
 \le {600\sqrt2M^2\over r^2}
 <600\sqrt2c^2r.                                \tag{7.12}
\]

For `c<=1/100`, the last quantity is less than `r/10`.  Thus both `m+n`
and `m-n` lie in `{0,...,r-1}^2` when `r` is sufficiently large.

The corresponding patch points are

\[
 p_+=p+Ln,\qquad p_-=p-Ln.                      \tag{7.13}
\]

Since `n` is perpendicular to `a`,

\[
 |p_+|^2-|p_-|^2
 =4p\mathbin\cdot Ln
 =4(L^Tp)\mathbin\cdot n
 =4a\mathbin\cdot J(a/q)=0.                    \tag{7.14}
\]

They are distinct because `L` is nonsingular and `n\ne0`.  They are not
antipodal, since `p_+=-p_-` would imply `p=0`, contrary to (7.9).  This
contradicts radial uniqueness and proves (7.2).  QED.

### Corollary 7.2 (rectangular rich-fibre form)

Let an adaptive rich fibre contain a complete integral `r`-by-`s` lattice
patch, with `r>=s`, inside `[-M,M]^2`, and write `S=|D+D|`.  Applying
Theorem 7.1 to an `s`-by-`s` subpatch gives `s<<M^(2/3)`.  The patch is a
union of `s` parallel lines, while the collinear rich-fibre theorem gives
at most `sqrt(S)` points on each line.  Hence

\[
 \boxed{|Q|=rs\ll M^{2/3}\sqrt S.}              \tag{7.15}
\]

This closes the complete exact integral oblique-lattice branch at the
cube-root-critical local exponent.  What remains for the full problem is
to extract such complete structure, or a stable substitute, from a general
large seven-incidence fibre and to aggregate the resulting bounds over all
fibres.

`verify_oblique_lattice_modular_midpoint.py` constructs the midpoint and
perpendicular displacement exactly for varied integral bases and
translations, and verifies (7.8)--(7.14) using integer arithmetic.
