# Double detached endpoint circuits have a polylogarithmic signature

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The double-incompatible branch of
`MULTIROLE_ENDPOINT_POCKET_TRANSFER.md` can be normalized with only a
polylogarithmic loss on the live low-rank pocket slice.

Let `F` be a convex face of rank `r` and let `e={a,b}` be a matching edge
such that both detached unions `F union {a}` and `F union {b}` are
nonconvex.  A canonical witness for one endpoint consists of that endpoint,
one triple from `F`, and one of four choices for the hidden label.  Thus one
endpoint has at most

\[
                              4{r\choose3}               \tag{1}
\]

signed signatures, and the ordered pair has at most

\[
                             16{r\choose3}^2.            \tag{2}
\]

Consequently a matching of `m` double-incompatible pairs contains a
submatching of size at least

\[
                    {m\over16{r\choose3}^2}              \tag{3}
\]

with one common ordered double-circuit signature.  At `r=O(log n)`, the
loss is `O((log n)^6)`, invisible both at quadratic coefficient scale and
at the `n^{Theta(log log n)}` recovery scale.

Applied separately to every retained pocket face and every poor role, the
choice of signature is recoverable from `(F,role)` and costs no global
context factor beyond (2).  Therefore the final unpaid multirole tensor is
not an arbitrary family of bad pairs: in each cell it is one of finitely
many common-cage/fan types over two fixed triples of the actual pocket face,
with both endpoint marks retained.

This is a normalization, not a release theorem.  If both endpoints are the
hidden labels, the selected submatching can lie inside two fixed pocket
triangles, a genuine common cage.  If a pocket label is hidden, the
endpoints form a rooted fan which pushes that fixed label behind a triangle.
No counting theorem based only on the number of signatures can distinguish
those realizable geometries.

## 1. Canonical endpoint signature

Let `F` be in strictly convex position and let `v` be a label outside its
support.  Suppose `F union {v}` is not convex.  Since `F` itself is convex,
every bad four-set witnessing this failure contains `v`.  Planar
Caratheodory gives

\[
                         Q(v)=\{v\}\cup T(v),
              \qquad T(v)\in{F\choose3},                \tag{4}
\]

with one point of `Q(v)` strictly inside the triangle of the other three.
Choose the lexicographically first such triple in one fixed global label
order.  Record also which of the four labels is hidden.  This is the
canonical signed signature

\[
                         \sigma_F(v)=(T(v),h(v)).         \tag{5}
\]

There are at most (1) choices.  Notice that (4) is wholly detached: no
root, source carrier, released guard, or omitted base point is present.

The four signed types have the following exact meanings.

* `v` hidden: the endpoint lies in one fixed pocket triangle.
* A label `x in T(v)` hidden: `x` lies in the triangle formed by `v` and
  the other two pocket labels, a fixed-root fan circuit.

The remaining three-set is an ordinary triangle and retains all labels of
the circuit except the optional hidden-point deletion used by a later
release operation.

## 2. Matching pigeonhole

Orient every matching pair `e={a,b}` canonically by the global label order
and put

\[
                         \Sigma_F(e)=(\sigma_F(a),\sigma_F(b)).     \tag{6}
\]

> **Theorem 1 (double-signature matching).**  If `M` is a matching of `m`
> pairs and every endpoint is detached-incompatible with `F`, then some
> value of (6) occurs on at least the number of pairs in (3).

**Proof.**  There are at most the square of (1) possible ordered values of
(6).  Partition `M` by that value and take a largest class.  Because it is
a subfamily of a matching, all endpoint labels and pair marks remain
disjoint.  QED.

The exact integer form is

\[
                   |M'|\ge
            \left\lceil{m\over16{r\choose3}^2}\right\rceil.       \tag{7}
\]

If only `m_0` edges of `M` are double-incompatible, replace `m` by `m_0`.
Combining with (10c) of the multirole report gives, for every low-entropy
`(c,F)`, a total normalized matching mass at least

\[
 {1\over16{r\choose3}^2}
 \left(q-{S(c,F)\over\alpha\log m}\right)_+
                   (m-m^\alpha),                         \tag{8}
\]

distributed over the poor roles, with one fixed signature in each role.

## 3. Weighted, varying-face form

The triple labels in (5) vary with `F`; globally pigeonholing their ambient
names would cost up to `n^6` and is unnecessary.  For each marked cell
`(c,F,i)`, choose its largest signature class canonically.  The actual
output in a later bank retains `F` and the role support, so it recovers the
two triples and the signed type.

If `d_(c,F,i)` is the number (or total edge weight) of
double-incompatible pairs in that cell, the retained normalized mass is at
least

\[
              {d_{c,F,i}\over16{|F|\choose3}^2}.         \tag{9}
\]

Summing (9) over arbitrary context weights is legitimate because the
selection is pointwise.  Only the eventual ordinary-face output needs a
global decoder; the normalization itself introduces no additional overlap.

If `|F|<=R=O(log n)`, then

\[
               \log\left(16{R\choose3}^2\right)=O(\log\log n).    \tag{10}
\]

This is much smaller than the `Theta((log n)log log n)` scale which the
multirole transfer is designed to recover.

## 4. Exact barrier and next operation

The endpoint-hidden class can be realized with an arbitrary number of
endpoints inside one fixed pocket triangle.  A source-side base on the
other side of that triangle can still expose every endpoint separately;
retaining the pocket triangle hides all of them.  Thus (3) does not force
an endpoint shield by itself.

In the pocket-label-hidden classes, all endpoints push the same fixed
pocket label behind triangles using the other fixed two pocket labels.
This is a rooted fan, but the endpoint order can still be projectively
universal away from the witness signs.  A positive next step must use one
of:

1. a small common guard which deletes one of the fixed pocket triples and
   releases a large endpoint alphabet;
2. a cross-role fan/chain product retaining the pocket trace; or
3. a high-codegree common cage charged to a detached pocket shield.

Theorem 1 ensures that this operation may assume fixed triples and signed
types in every cell without losing the required scale.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_double_endpoint_pocket_signature.py
```

The checker realizes all four signed endpoint types over exact rational
coordinates, verifies that every witness contains the endpoint and three
pocket labels, exhausts abstract double-signature matchings, and checks the
ceiling and polylogarithmic bounds in (7)--(10).
