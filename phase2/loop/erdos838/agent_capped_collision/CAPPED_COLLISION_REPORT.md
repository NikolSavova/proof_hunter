# Erdős 838: the crossing-trace-capped collision lemma is false

**Date:** 2026-08-13
**Verdict:** the proposed dichotomy with a cap on the balanced-cut crossing
trace `X` is false, strongly and stretchably.  There is an exact rational
family for which

\[
 \log_2 X=o((\log_2 N)^2),\qquad
 \frac{X E^2}{S_LS_R}=N^{-\Theta(\log\log N)}.
\]

Thus no dichotomy of the form

\[
 X\ge 2^{(c-o(1))(\log N)^2}
 \quad\hbox{or}\quad
 X\ge N^{-O(1)}\frac{S_LS_R}{E^2}                 \tag{D_X}
\]

can hold for **any fixed `c>0`**, in particular not for `c=1/2` or for a
version intended to yield the `1/3` incremental bound.  Polynomial tangent
mass is compatible with the counterfamily and does not repair `(D_X)`.

There is one critical qualification.  The family has `V(P)>=2^r`, so it does
**not** refute the stronger, correctly useful total-count-capped statement

\[
 V(P)\ge 2^{(c-o(1))(\log N)^2}
 \quad\hbox{or}\quad
 X\ge N^{-O(1)}\frac{S_LS_R}{E^2}.                \tag{D_V}
\]

`(D_V)` remains open and is the recommended replacement.  The earlier
alternating counterexample and the padded family here together explain why
the cap must see convex subsets away from the selected cut, not just `X`.

All logarithms below are base two.

## 1. A heterogeneous vertical composition

Fix even `h` and an integer `r`.  Start from the `2h`-point least-index
alternating order type

\[
 \chi(i,j,k)=(-1)^i\qquad(i<j<k).                 \tag{1}
\]

It is exactly realizable: take

\[
 (i,(-1)^iM^{2h-i})\quad(0\le i\le2h-3),
 \qquad (2h-2,0),(2h-1,0),
\]

with `M>4h`.  In every determinant the term from the least index dominates
the other two.  A sufficiently large shear makes both coordinates increase
without changing any orientation.

Replace four macro points by `r`-point blocks:

* blocks `0` and `h-1` are all-cups (every local triple is positive);
* blocks `2h-2` and `2h-1` are all-caps (every local triple is negative);
* all other blocks are singletons.

Use the vertical composition

\[
 (X_i,Y_i)[Q_i]
 =\{(X_i+\epsilon^2x,\,Y_i+\epsilon y):(x,y)\in Q_i\}.       \tag{2}
\]

The microsets can be sheared parabolic chains, hence have rational
increasing coordinates.  For sufficiently small rational `epsilon`, triples
in one block have their micro sign, triples in three blocks have (1), the
first two points in one block give a negative triple, and the last two in
one block give a positive triple.  These are finitely many strict determinant
conditions, so a rational interval of valid `epsilon` exists.  This proves
stretchability of every member, rather than only an abstract order-type
claim.

Cut between macro blocks `h-1` and `h`.  Both sides have exactly

\[
 \ell=2r+h-2
\]

points.  Thus `N=2 ell` and the number of cross edges is `E=ell^2`.

## 2. Why the crossing trace stays small

The usual endpoint-block classification for vertical composition works
unchanged with unequal blocks.  A convex set meeting at least two blocks has

* a cap in its first occupied block,
* a cup in its last occupied block, and
* one point in each intermediate occupied block.

Its occupied macro blocks form a convex subset of the macro order type.

An all-cup `r`-block has only

\[
 D(r)=r+\binom r2\le r^2
\]

nonempty caps; an all-cap block has only `D(r)` nonempty cups.  For a set
crossing the balanced cut, the two inflated left blocks together contribute
at most `r^3` (first-block cap and possibly one intermediate point), and the
two inflated right blocks contribute at most `r^3` (last-block cup and
possibly one intermediate point).  Hence each macro convex set has weight
at most `r^6`.

For the alternating macro order, fixing the extreme indices makes one of the
cap/cup path counts equal to one.  In the other path, the selectable internal
vertices have one parity; because signs alternate, each power of two occurs
at most twice in the sum over the penultimate vertex.  Therefore

\[
 W(S_{2h})\le 5h^2 2^h.
\]

Consequently the crossing trace satisfies

\[
 \boxed{X\le 5r^6h^2 2^h.}                       \tag{3}
\]

Notice the role of the one-sided blocks: although each has `2^r-1`
nonempty convex subsets internally, the statistic required at a left
endpoint is its small cap count and at a right endpoint its small cup count.
The huge local mass is invisible to this cut trace.

## 3. Boundary masses remain anti-aligned

Use the aggregate identities from the tangent-pruning report.  After
deleting internal-right edges, let `u_s^-` and `c_s^-` be the cup and cap
counts from a left source `s` into the right side.  Then

\[
 S_L=\sum_{s\in L}u_s^-c_s^-.
\]

For each of the `r` sources in block `0`, take a cup through an arbitrary
subset of the even singleton blocks `2,4,...,h-2`, one point of block `h-1`,
and any right endpoint.  Pair it with any direct cross cap.  This gives

\[
 \boxed{S_L\ge r^2\ell^2 2^{h/2-1}.}              \tag{4}
\]

For `S_R`, delete internal-left edges and fix a terminal point in block
`2h-1`.  A cup may start at any of the `r` points in block `0`, use an
arbitrary subset of the even singleton right blocks, and choose any of the
`r` points in block `2h-2` as penultimate vertex.  Independently, a cap may
start at any point in the negative macro block `h-1`, use the odd singleton
right blocks, and choose its penultimate point in block `2h-2`.  Summing over
the `r` terminal points yields

\[
 \boxed{S_R\ge r^5 2^{h-2}.}                      \tag{5}
\]

Combining (3)--(5) with `E=ell^2` gives the audited inequality

\[
 \boxed{
 \rho:=\frac{XE^2}{S_LS_R}
 \le 40h^2\frac{\ell^2}{r}\,2^{-h/2}.
 }                                                  \tag{6}
\]

## 4. Exponent audit

Let

\[
 r_j=2^j,\qquad h_j=2\lceil j\log_2j\rceil.
\]

For large `j`, `h_j<=r_j`, so `ell<=3r_j`, and

\[
 \log N=j+O(1),\qquad
 \log X\le h_j+6j+O(\log h_j)=O(j\log j)=o(j^2).  \tag{7}
\]

On the other hand, (6) gives

\[
 \log\rho
 \le -j\log_2j+O(j)
 =-(\log N)(\log\log N)+O(\log N).                \tag{8}
\]

Thus `X` is below `2^{(c-o(1))log^2 N}` for every fixed positive `c`, while
`rho<N^{-A}` for every fixed `A` along a tail of the family.  This is exactly
the simultaneous failure required to refute `(D_X)`.  The polynomial powers
of `r` in (3) and (6) have been retained; dropping them would give the wrong
conclusion at intermediate scales.

## 5. Tangent mass and the correct surviving cap

This is not a tangent-mass counterexample.  A crude count already gives the
polynomial form of `(T)` on the family.  In the left child, use the cap count;
in the right child, use the cup count.  The same endpoint-block rule and the
alternating macro path bound imply

\[
 \min(C_L,U_L)\le C_L\le O(r^3h^2 2^{h/2}),
 \qquad
 \min(C_R,U_R)\le U_R\le O(r^3h^2 2^{h/2}).       \tag{9}
\]

Equations (4)--(5) then give the left tangent ratio at least
`1/O(rh^2)` and the right ratio at least inverse-polynomial (in fact it grows
once `h` is moderately large).  The exact finite certificates below have
both tangent ratios greater than one.  Therefore adding polynomial `(T)` to
an `X`-capped collision statement does not save it.

But every inflated one-sided block is itself in convex position, so

\[
 \boxed{V(P)\ge 2^r-1.}                            \tag{10}
\]

For `r=2^j`, this is enormously larger than
`2^{(1/2-o(1))(log N)^2}`.  The family is consequently harmless to `(D_V)`.
Any next collision attack should assume a global cap on `V(P)` and exploit
that cap to forbid precisely these high-entropy one-sided padding blocks (or,
equivalently, charge large discarded-chain fibres directly to `V(P)`).

## 6. Exact rational certificates

`capped_counterfamily.py` is self-contained.  For each stored case it:

1. constructs rational macro and micro coordinates;
2. searches for a dyadic `epsilon`;
3. checks every orientation determinant against the heterogeneous
   composition rule;
4. sorts all exact rational slopes;
5. independently computes `X,S_L,S_R` by path-matrix products; and
6. checks (3)--(6).

Run

```bash
python3 phase2/loop/erdos838/agent_capped_collision/capped_counterfamily.py \
  --output phase2/loop/erdos838/agent_capped_collision/exact_certificates.json
```

The stored cases `(h,r)=(4,3),(6,4),(8,5)` have respectively `N=16,24,32`;
all `7,544` orientation determinants pass.  Their exact collision ratios are

\[
 \frac{10100}{54717},\qquad
 \frac{115128}{2044625},\qquad
 \frac{34952}{1903353}.
\]

These finite values are illustrations, not the asymptotic refutation; the
proof of superpolynomial decay is the uniform bound (6) with the parameter
choice in Section 4.

## Bottom line

The alternating obstruction cannot be repaired by capping only the crossing
trace: high-entropy convex mass can be parked inside one-sided endpoint
blocks where `X` does not see it, while its multiplicity sustains the two
anti-aligned boundary kernels.  Discard `(D_X)`.  The precise surviving target
is `(D_V)`, with a cap on the total convex-subset count.  Proving `(D_V)` plus
polynomial tangent mass would still recover the earlier `1/3` arithmetic;
this lane neither proves nor refutes that strengthened statement.
