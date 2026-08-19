# A four-corner stopping-set barrier for the transverse theorem

## 1. Outcome

The strongest-looking simplification of the eight-corner gate is false.
Fixing one endpoint role and retaining the other four corner projections does
**not** make the transverse relation hypergraph peelable, even for an
integral planar distance-Sidon set.

There is an explicit 31-point integer distance-Sidon set `A`, a point
`p in A`, and sixteen distinct transverse relations

\[
 a_0-a_1=(b_0-b_1)+J(p-c_1)                 \tag{1.1}
\]

such that every one of the four keys

\[
 (a_i,b_j,p),\qquad i,j\in\{0,1\},           \tag{1.2}
\]

occurring in the sixteen relations occurs **exactly twice**.  Consequently
these relations form a nonempty simultaneous 2-core for the four projections
with the `c_0=p` endpoint fixed.

The other four corner keys `(a_i,b_j,c_1)` are singletons in this subsystem.
Thus the example does not kill the full eight-corner peeling conjecture.  It
shows that all eight corners are load-bearing: no argument may freeze one
endpoint role and hope to recover the cubic bound from four projections.

## 2. What the false shortcut would have proved

For a family `R` of transverse relations and a collection `M` of corner
projections, repeatedly delete a relation which is alone in one of its
current corner fibres.  If this deletes every relation, charge each deleted
relation to the singleton corner key used at its deletion.  A key is charged
at most once, so

\[
 |R|\le |M|k^3.                               \tag{2.1}
\]

For four fixed-role corners this would give `|R|<=4k^3`; for all eight it
would give `|R|<=8k^3`, hence the desired transverse cubic estimate.  The
construction below disproves the four-corner premise, not the charging
argument.

## 3. Exact finite construction

Index the sixteen relation records by `0,...,15`.  Their four repeated
corner fibres are the following four perfect matchings, in corner order
`00,01,10,11`:

```text
1 0 3 2 5 4 7 6 9 8 11 10 13 12 15 14
10 12 14 9 7 6 5 4 15 3 0 13 1 11 2 8
8 9 12 13 10 11 14 15 0 1 4 5 2 3 6 7
3 4 11 0 1 15 8 12 6 10 9 2 7 14 13 5
```

The `a_0,a_1,b_0,b_1` labels are the connected components of the appropriate
two-colour matching unions.  Use one independent Gaussian variable for each
such component and one for `p`, and define

\[
 c_r=p+J(a_{0,r}-a_{1,r}-b_{0,r}+b_{1,r}).    \tag{3.1}
\]

This gives 31 formal point labels.  Their 465 squared-distance polynomials
are pairwise distinct.  Hence a generic rational, and therefore an integral,
specialization is distance-Sidon.  The verifier checks this formal statement
by comparing the exact Hermitian coefficient matrices.

One concrete specialization is stored in
`verify_four_corner_stopping_set_barrier.py`.  Its coordinates have magnitude
below `3.9*10^7`; all 465 positive squared distances are distinct, all sixteen
instances of (1.1) hold, and all are transverse.

On the complete transverse relation set of this 31-point witness, the exact
profiles are

\[
 |R(A)|=584,\qquad
 |\operatorname{core}_{0,1,2,3}|=32,\qquad
 |\operatorname{core}_{4,5,6,7}|=32,
 \qquad |\operatorname{core}_{0,\ldots,7}|=0. \tag{3.2}
\]

The factor two in the four-corner cores is the reverse orientation.

## 4. Structural interpretation

In a distance-Sidon set, two distinct transverse relations cannot share two
different corner keys.  If the keys differ in one role, subtraction leaves
two nontrivial point differences equal up to a Gaussian unit, contradicting
distance uniqueness.  If they differ in two or three roles, the shared full
edges and the relation equation determine all remaining endpoints.  Thus the
corner hypergraph is linear.

Linearity alone is insufficient: the sixteen-record subsystem is a linear
4-uniform, 2-regular stopping set.  Its existence is best viewed as a
positive-genus finite trade.  Small exhaustive and annealing searches had
misleadingly bottomed out above zero through fourteen records; the first
generic collision-free system occurs at sixteen.

The surviving proof target is therefore genuinely eight-sided.  Either prove
that every full eight-corner stopping set forces a repeated distance, or keep
the weaker size-biased tail

\[
 |R_{\ge t}|\le k^{3+o(1)}/t.                 \tag{4.1}
\]

The present example strongly warns against replacing (4.1) by any theorem
that sees only four corners with one endpoint role fixed.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_four_corner_stopping_set_barrier.py
```

It checks the perfect matchings, the formal Gaussian certificate, the
integral distance-Sidon specialization, every transverse relation, all eight
subsystem degrees, and the three complete-relation core sizes in (3.2).

