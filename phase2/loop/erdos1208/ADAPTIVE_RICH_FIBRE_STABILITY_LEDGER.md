# Stability ledger for adaptive rich fibres

## 1. A proved collinear-support branch

Let `D=A-A`, put `S=|D+D|`, and let `Q=Q_K(u,s)` be one of the adaptive
rich fibres from `SUPPORT_ADAPTIVE_RICH_FIBRE_GATE.md`.  Write `w=s-u`.
The defining incidences give

\[
 u+Q\subseteq D,
 \qquad
 w-(I+J)Q\subseteq D.                            \tag{1.1}
\]

### Proposition 1.1

If `Q` contains `ell` points on one affine line, then

\[
 \boxed{S\ge\ell^2.}                            \tag{1.2}
\]

### Proof

Restrict to the collinear subset and write it as

\[
 Q_0=\{q_0+t v:t\in T\},
 \qquad |T|=\ell,
\]

where `v` is nonzero.  By (1.1), `D+D` contains all

\[
 (u+q_0+t v)+
 \bigl(w-(I+J)(q_0+t'v)\bigr),
 \qquad t,t'\in T.                              \tag{1.3}
\]

The two direction vectors `v` and `(I+J)v` are linearly independent, since

\[
 \det(v,(I+J)v)=\det(v,Jv)=|v|^2\ne0.           \tag{1.4}
\]

Thus (1.3) is injective in `(t,t')`, proving (1.2).  QED.

In particular every adaptive rich fibre satisfies

\[
 \max_L|Q\cap L|\le\sqrt S.                     \tag{1.5}
\]

If `Q` is covered by `r` parallel lines, its largest line has at least
`|Q|/r` points, so

\[
 |Q|\le r\sqrt S.                               \tag{1.6}
\]

This is a genuine proved branch, but not the whole stability theorem:
`S>=N` and `|Q|<=N`, so (1.5) still permits polynomial-size wide fibres.

## 2. Exact aggregate second moment

The full proof needs an aggregate result, not merely the maximum-fibre
statement.  For brevity write `P=mathcal P_K` and `g=g_K`.  Define `Z_K(r)`
to be the number of triples `(x,y,v) in D^3` satisfying

\[
\begin{gathered}
 x+r\in D,
 \qquad y-r\in D,
 \qquad v-(I+J)r\in D,\\
 u:=x+J(y-v)\in D,                              \tag{2.1}\\
 q:=-J(y-v)\in P,
 \qquad q+r\in P.
\end{gathered}

Then

\[
 \boxed{\sum_{u,s}g(u,s)^2=\sum_r Z_K(r).}       \tag{2.2}
\]

Indeed, two shifts `q,q'=q+r` in the same label `(u,s)` give

\[
\begin{array}{lll}
 x=u+q, & x'=x+r,\\
 y=s-u-q, & y'=y-r,\\
 v=s-u-(I+J)q, & v'=v-(I+J)r.
\end{array}                                      \tag{2.3}

Conversely (2.1) recovers `q,u,s=x+y`, and then (2.3) recovers the two
preimages.  The diagonal is exactly

\[
 Z_K(0)=\sum_{q\in P}R_D(q)R_D(Jq),              \tag{2.4}
\]

the adaptive tail itself.  Hence the unresolved part of the moment theorem
is the off-diagonal seven-incidence estimate

\[
 \sum_{r\ne0}Z_K(r)\le N^{1+o(1)}S.             \tag{2.5}

Dropping the condition `u=x+J(y-v) in D` gives the raw upper bound

\[
 Z_K(r)\le R_D(r)^2R_D((I+J)r),                 \tag{2.6}

but this relaxation is unusable: the transformed parabola makes the
corresponding unrestricted dilation moment too large by a fixed power-scale
factor.  The seventh complete-difference incidence in (2.1) is load-bearing.

## 3. Why the five-copy pigeonhole is not yet enough

The translate-amplification lemma produces a subset

\[
 |Q'|>{|Q|K^2\over N^2}.                        \tag{3.1}

In the live high-support cutoff `K<=N^(2/3+o(1))`, (3.1) is guaranteed to be
nontrivial only when `|Q|>N^(2/3-o(1))`.  A violation of the desired
`N^(o(1))` average-load bound, however, may consist of fibres of size merely
`N^epsilon` for arbitrarily small fixed `epsilon`.  Therefore the five-copy
lemma is a valid large-fibre inverse statement but cannot by itself close
the full tail.

The correct next target is (2.5).  A successful proof must use the popularity
of both `q` and `q+r` before pigeonholing away the shifts, or establish a
weighted stability theorem for all seven incidences simultaneously.

## 4. Exact verification

`verify_adaptive_rich_fibre_stability_ledger.py` checks:

1. the Cartesian injection in Proposition 1.1 on exact integer families;
2. the bijection (2.2) on the 30-point closure witness;
3. all seven incidences in (2.1) for every ordered pair in every nonempty
   adaptive rich fibre; and
4. the raw majorant (2.6), while retaining the warning that it is too weak
   for a proof.

`ALGEBRAIC_CURVE_RICH_FIBRE_BRANCH.md` extends Proposition 1.1: if `h`
fibre points lie on a real degree-`d` algebraic curve, then Bezout gives
`S>=h^2/d^2`.  Hence a cover by `r` bounded-degree curves gives
`|Q|<=rd sqrt(S)`.  The remaining wide fibres must have genuinely growing
algebraic complexity, as a rank-two lattice model does.

`UNIT_LATTICE_RICH_FIBRE_HEIGHT.md` begins that remaining rank-two case.
A translated unit `r`-by-`r` lattice patch with pairwise distinct radii must
have coordinate height `Omega(r^2)`.  Thus such a patch inside
`D subset [-m,m]^2` has at most `O(m)` points.  The proof intersects two
explicit arithmetic progressions of shifted-square differences by CRT.

`RECTANGULAR_LATTICE_HEIGHT_DICHOTOMY.md` proves that the square theorem is
sharp in its aspect-ratio dependence.  An `r`-by-`s` patch needs translation
height `Theta(min(r,s)^2)`, not `Omega(rs)`: translating the long coordinate
by `s^2` separates every radius for arbitrary `r`.  The thin escape is a
union of `s` parallel lines, so the next aggregate theorem must couple the
height and curve-cover branches.

`GAUSSIAN_IDEAL_COSET_HEIGHT.md` treats the full exact quarter-turn-stable
rank-two model beyond the unit lattice.  Such a lattice is a Gaussian ideal.
For every nonzero integral coset of every Gaussian ideal, a radially unique
`r`-by-`r` patch in `[-M,M]^2` satisfies

\[
 r\ll M^{2/3},\qquad |Q|=r^2\ll M^{4/3}.         \tag{4.1}
\]

The proof balances physical diameter against a denominator-sensitive CRT
collision.  For an `r`-by-`s` rectangle, `r>=s`, it gives

\[
 |Q|\ll M^{2/3}\sqrt S,                          \tag{4.2}
\]

by combining `s<<M^(2/3)` with the parallel-line bound `r<=sqrt(S)`.
This closes the entire exact Gaussian-ideal patch branch at the cube-root-
critical height.  Approximate-module extraction and aggregate-fibre control
remain open.
