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

## 2. Universal `r^(6/5)` height theorem

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

The exponent `6/5` is not claimed to be sharp.  The cube-root application
would require `3/2`; Section 4 identifies the exact conditioning loss.

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
`2/3`.  Thus (3.2) measures exactly the present cost of arbitrary
conditioning.

## 4. Exact remaining oblique gate

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

The critical exact-oblique theorem is therefore:

> If the full `r`-by-`r` patch is radially unique, prove directly from
> (4.1) that `M>>r^(3/2)`, without first restricting to the Gaussian core.

Equivalently, one needs a short inhomogeneous solution of (4.1) whose two
coefficient points remain in the box.  The issue is simultaneous angular
approximation and the divisibility condition

\[
 \gcd((Gn)_1,(Gn)_2)\mid n^TL^Tt+n^TGn.         \tag{4.2}
\]

The two forced copies in (1.1) may supply the extra congruence or averaging
needed to remove the conditioning loss.  This is now a precise arithmetic
gate rather than the vague phrase “approximate oblique lattice.”

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
critical oblique theorem isolated in Section 4, if true, has the best
possible exponent.  It also supplies a necessary extremal model for any
attempt to solve the inhomogeneous gate (4.1).
