# Generic-segment barrier to fixed-row fibre expansion

## 1. Result

Let `A` be a planar distance-Sidon set, put `D=A-A`, and for a target
`t in D+JD` define

\[
 E_t=\{e\in D:t-e\in JD\}.                     \tag{1.1}
\]

The proposed local expansion estimate

\[
 |E_t-JE_t|\ge |E_t|^{2-o(1)}                  \tag{1.2}
\]

is false by essentially a full power.  There are arbitrarily large integral
distance-Sidon sets and targets `t` for which

\[
 |E_t|=M^{2-o(1)},\qquad |E_t-JE_t|=O(M^2)
       =|E_t|^{1+o(1)}.                         \tag{1.3}
\]

Thus the conditional `F_2(n)<=n^(2/5+o(1))` route in Section 6 of
`ORTHOGONAL_TWO_SUPPORT_GATE.md` cannot be used.  The full two-support target

\[
 |D+D|\,|D+JD|\ge |D|^{3-o(1)}                 \tag{1.4}
\]

is not contradicted: the generic translations below make the global
difference set highly expanding.  The obstruction says that a single fixed
row may be an arbitrary dense radially unique planar model even when the
ambient point set is distance-Sidon.

## 2. A large radially unique set in a square

For an integer `M`, consider all nonzero lattice points in `[0,M]^2`.
The number of representations of one integer as `x^2+y^2` is at most
`4 tau(n)=M^{o(1)}` uniformly for `n<=2M^2`.  Selecting one representative
of every occurring positive norm gives a set

\[
 E\subset[0,M]^2,\qquad |E|=M^{2-o(1)},          \tag{2.1}
\]

whose vectors have pairwise distinct lengths.  The sharper
Landau--Ramanujan theorem would give `|E| asymp M^2/sqrt(log M)`, but the
elementary divisor bound is enough here.

Put

\[
 B=2M+1,qquad T=2M^2+1,qquad t=(T,BT),          \tag{2.2}
\]

and define

\[
 F=J(E-t),\qquad W=E\mathbin\dot\cup F.          \tag{2.3}
\]

All vectors in `W` have pairwise distinct lengths.  The lengths inside `E`
are distinct by construction.  For `e=(x,y)` and `e'=(x',y')`,

\[
 \begin{split}
 \|e-t\|^2-\|e'-t\|^2
  ={}&\|e\|^2-\|e'\|^2\\
    &-2T\bigl((x-x')+B(y-y')\bigr).              \tag{2.4}
 \end{split}
\]

The integer in parentheses is nonzero for `e!=e'`, since `B>2M`; its
second term has magnitude greater than `4M^2`, whereas the first has
magnitude at most `2M^2`.  Hence the lengths inside `F` are distinct.
They are also much larger than every length inside `E`, so the two spectra
are disjoint.

Finally, if `f=J(e-t)`, then

\[
 e+Jf=e+J^2(e-t)=t.                              \tag{2.5}
\]

Thus every `e in E` is intended to lie in the target fibre.

## 3. Generic disjoint-segment realization

For every `w in W`, introduce an independent translation `z_w in R^2` and
the two labelled points

\[
 z_w,\qquad z_w-w.                               \tag{3.1}
\]

Let `A(z)` be the union of these `2|W|` points.  There is a rational choice
of all translations with the following two properties:

1. `A(z)` is distance-Sidon;
2. every representation `d+Jg=t` with `d,g in A(z)-A(z)` has both directed
   edges internal to individual segment blocks.

Both assertions follow by deleting finitely many proper algebraic loci.
Here are the needed nonidentity checks.

For distance equality, an edge joining blocks `u,v` has vector

\[
 z_u-z_v+c,                                      \tag{3.2}
\]

where `c` records the two endpoint choices.  Edges with different block
supports depend on different independent translations.  For a fixed pair
of blocks, the four offsets are distinct because the nonzero vectors in
`W` are distinct.  Therefore two different labelled cross edges cannot have
identical squared-length polynomials.  Internal segment lengths are the
pairwise distinct values `||w||`, and a cross-edge length is nonconstant.

For a row identity

\[
 d+Jg=t,                                         \tag{3.3}
\]

the coefficient of each block translation is `aI+bJ`, with
`a,b in {-1,0,1}`.  Since `I,J` are linearly independent over the reals,
this coefficient vanishes only when `a=b=0`.  Hence (3.3) can be an identity
only if each of `d,g` is internal to one segment block.  Every other proposed
row relation is a proper affine subspace.

The complement of the finitely many bad loci is a nonempty Zariski-open
subset of a rational affine space, so it contains a rational point.  Scaling
by a common denominator gives an integral distance-Sidon set and scales `t`
by the same factor.

## 4. Size of the exceptional fibre and its support

Let

\[
 U=W\cup(-W).
\]

By Section 3, every directed edge occurring in the target fibre is an
internal segment vector, so

\[
 E\subset E_t\subset U.                          \tag{4.1}
\]

In particular

\[
 |E_t|=M^{2-o(1)}.                               \tag{4.2}
\]

The set `U` is the union of four translates of rotations or reflections of
`E`: namely `E,-E,JE-Jt,-JE+Jt`.  Consequently `U-JU` is contained in a
fixed number of translates of boxes of side `O(M)`.  Therefore

\[
 |E_t-JE_t|\le |U-JU|=O(M^2).                   \tag{4.3}
\]

Equations (4.2)--(4.3) prove (1.3), and hence disprove (1.2).

## 5. Exact calibration and restart rule

`verify_fixed_row_fibre_expansion_barrier.py` checks the lattice-vector
construction for `M` through 100.  At `M=100` it finds `2,749` intended
vectors and only `20,633` orthogonal support values.  It also constructs a
concrete 116-point distance-Sidon set at `M=8` with

\[
 |D|=13,341,qquad |E_t|=29,qquad |E_t-JE_t|=123, \tag{5.1}
\]

and verifies that the target fibre contains exactly the intended vectors.
All arithmetic in the finite check is integral.

The six-biclique family was not the obstruction: its heavy row has perfect
quadratic expansion in the tested generic instances.  The obstruction is
more basic—independently translated prescribed segments allow a fixed row to
carry an almost two-dimensional radially unique vector set.

**Restart rule.**  Do not seek a theorem about one maximum fibre in
isolation.  Any viable proof of (1.4) must charge a structured row to the
global expansion created by its independent segment translations, or average
over enough rows that this generic freedom becomes visible.  The direct
two-support product remains the live full-resolution gate.
