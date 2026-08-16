# A simple Caratheodory-three convex geometry does not suffice

**Date:** 2026-08-14

The half-weight conjecture for planar point sets cannot be proved from
meet-distributivity, simplicity, and Caratheodory number three alone.  This
note gives an exact abstract counterexample.  Thus a successful closure-lattice
proof must use the rank-three oriented-matroid axioms (or an equivalent planar
condition such as the full Erdos--Szekeres phenomenon), not just abstract
convex-geometry axioms.

Let the ground set be `[n]={1,...,n}`.  Declare a set closed when it has the
form

\[
  [k]\cup B,\qquad 0\le k\le n,\quad
  B\subseteq\{k+1,\ldots,n\},\quad |B|\le2.                 \tag{1}
\]

Equivalently, after the first missing element of a proper closed set there
are at most two selected elements.

## Proposition

The family (1) is a simple finite convex geometry of Caratheodory number
three.  Its convexly independent sets are exactly the subsets of size at most
three.  Consequently

\[
 Z_n(z)=1+nz+\binom n2z^2+\binom n3z^3,                    \tag{2}
\]

and

\[
 \frac{nZ_n(1/2)}{Z_n(1)}=\frac n8+O(1),\qquad
 \mathbb E_1|A|=3+O(1/n).                                 \tag{3}
\]

In particular both the universal half-weight statement and the desired
logarithmic mean statement fail dramatically in this abstract class.

## Proof

The family contains the empty set and the ground set.  It is closed under
intersection: if `k<=l`, then

\[
 ([k]\cup B)\cap([l]\cup D)=[k]\cup(B\cap([l]\cup D)),
\]

and the part beyond `[k]` still has size at most two.  It also has the
one-point augmentation property.  For a proper closed set, add its first
missing element; after the new first missing element there are still at most
two selected elements.  The standard finite characterization (intersection
closure plus one-point augmentation) therefore makes this a convex geometry.

Every one- and two-element set is closed, so the geometry is simple.  If
`S={s_1<...<s_r}` and `r>=3`, then

\[
 \operatorname{cl}(S)=[s_{r-2}]\cup\{s_{r-1},s_r\}.        \tag{4}
\]

Indeed, the right side is closed.  Any closed superset of `S` must contain
the full prefix `[s_{r-2}]`, since otherwise its first missing element would
have at least three selected elements after it.  Formula (4) also shows that
every point in the closure of `S` already lies in the closure of a triple
from `S`, proving Caratheodory number at most three (and it is exactly three
for `n>=4`).

For a proper closed set in canonical form `[k] union B`, where `k+1` is its
first missing element and `b=|B|<=2`, every member of `B` is extreme.  A
prefix element `x<=k` is extreme precisely when

\[
 (k-x)+b\le2.
\]

Thus the number of extreme points is

\[
 b+\min(k,3-b)\le3.                                      \tag{5}
\]

The top set likewise has its last three elements extreme.  Conversely, for
every triple `a<b<c`, (4) has extreme set exactly `{a,b,c}`; the same is
immediate in ranks zero, one, and two.  Hence the independent sets are
exactly those of size at most three, which proves (2)--(3).

This example is necessarily non-planar once `n>=5`: it has no independent
four-set, whereas every five points in planar general position contain a
convex quadrilateral.  That is precisely the extra geometry that any future
lattice argument must retain.

## Verification

Run

```bash
python3 phase2/loop/erdos838/agent_root_followup/verify_abstract_barrier.py
```

The script enumerates the closure family through `n=12`, checks intersection
closure, augmentation, anti-exchange directly, computes every closure and
extreme set, verifies Caratheodory-three witnesses, and checks (2).
