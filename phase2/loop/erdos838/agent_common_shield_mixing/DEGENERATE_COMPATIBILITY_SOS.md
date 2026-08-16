# Degenerate compatibility certificate for the weighted `C4` inequality

## Result

Let `A` be a finite simple bipartite `0,1` matrix, with row degrees
`d_i`, column degrees `e_j`, and `m` ones.  On the edge set define

\[
 x_{ij}=\frac{d_i e_j}{m}.
\]

Let `R` be the compatibility matrix

\[
 R_{(i,j),(k,l)}=A_{il}A_{kj}.
\]

Thus `C=1^T R 1`, `W=m^2 x^T R x`, and the original conjecture is
`x^T R x <= 1^T R 1`.

This note proves the conjecture on the entire degenerate part of `R`
(pairs sharing a row or a column), by an edgewise nonnegative
certificate.  It follows in particular that the original conjecture is
true for every bipartite graph with no ordinary four-distinct-vertex
`C4`.

The remaining problem is reduced exactly to genuine rectangles:

\[
 \boxed{
 C-x^TRx=\sum_{ij\in E}\delta_{ij}
       +\sum_{\substack{ij,kl\in E:\ i\ne k,\ j\ne l\\
                         il,kj\in E}}(1-x_{ij}x_{kl}),}
                                                               \tag{1}
\]

where every `delta_ij` is nonnegative and has the explicit formula
below.  Hence only genuine opposite-edge pairs with
`d_i d_k e_j e_l>m^2` can remain unpaid.

## 1. The edgewise certificate

For an edge `ij`, put

\[
 h_i=\sum_{l\in N(i)}e_l,\qquad
 g_j=\sum_{k\in N(j)}d_k.
\]

Define

\[
 \delta_{ij}
 =d_i\left(1-\frac{h_i^2}{m^2}\right)
 +e_j\left(1-\frac{g_j^2}{m^2}\right)
 -1+\frac{d_i^2e_j^2}{m^2}.                                \tag{2}
\]

### Lemma

For every existing edge `ij`, `delta_ij >= 0`.

### Proof

Set `d=d_i`, `e=e_j`, `h=h_i`, and `g=g_j`.  Let
`S=N(j)` be the `e` rows meeting column `j`, and `T=N(i)` the `d`
columns meeting row `i`.  The set of edges whose column lies in `T`
has size `h`; the set whose row lies in `S` has size `g`.  Their
intersection lies in the `e` by `d` rectangle `S x T`, so it has at
most `de` edges.  Therefore

\[
 0\le h,g\le m,\qquad h+g\le m+de.                          \tag{3}
\]

After multiplying (2) by `m^2`, the desired inequality is

\[
 d(m^2-h^2)+e(m^2-g^2)\ge m^2-d^2e^2.                     \tag{4}
\]

If `de>=m`, the right side is nonpositive and (4) is immediate.  If
`de<=m`, use `d,e>=1` and (3).  Among `0<=h,g<=m` with
`h+g<=m+de`, convexity shows

\[
 h^2+g^2\le m^2+d^2e^2;
\]

the maximum is attained at `(m,de)` or `(de,m)`.  Consequently

\[
 d(m^2-h^2)+e(m^2-g^2)
 \ge 2m^2-h^2-g^2
 \ge m^2-d^2e^2.
\]

This proves the lemma.  Notice that the proof is a two-case elementary
sum-of-nonnegative-terms certificate; it uses no spectral estimate.

## 2. Summing the certificate

Let `R_0` contain exactly compatible ordered edge pairs that share a
left or right endpoint; a loop is included once.  Then

\[
 \mathbf1^TR_0\mathbf1=\sum_i d_i^2+\sum_j e_j^2-m.          \tag{5}
\]

Moreover

\[
 x^TR_0x
 =\frac1{m^2}\sum_i d_i^2h_i^2
  +\frac1{m^2}\sum_j e_j^2g_j^2
  -\sum_{ij\in E}x_{ij}^2.                                 \tag{6}
\]

In (2), sum the first term over the `d_i` edges in row `i`, and the
second over the `e_j` edges in column `j`.  Equations (5)--(6) give

\[
 \mathbf1^TR_0\mathbf1-x^TR_0x=\sum_{ij\in E}\delta_{ij}\ge0. \tag{7}
\]

Every compatible pair outside `R_0` has four distinct endpoints and
is precisely an ordered pair of opposite edges of an ordinary `C4`.
Adding those remaining terms to (7) gives the exact identity (1).

## 3. Consequences and sharp residual

1. **`C4`-free theorem.**  If the support graph has no ordinary
   four-distinct-vertex `C4`, the second sum in (1) is empty, so
   `W<=m^2C`.
2. More generally, the theorem holds whenever every genuine compatible
   pair satisfies `x_ij x_kl<=1`, equivalently
   `d_i d_k e_j e_l<=m^2`.
3. In full generality the exact remaining assertion is

   \[
   \sum_{\Gamma}(x_{ij}x_{kl}-1)\le\sum_{ij\in E}\delta_{ij}, \tag{8}
   \]

   where `Gamma` is the set of ordered genuine compatible pairs.  Terms
   on the left with product below one are automatically helpful, so one
   may retain them or discard them for a stronger sufficient condition.

This isolates the real obstruction more sharply than the raw
Dirichlet identity: all repeated-vertex homomorphisms are already paid
edgewise.  The unpaid object is only excess degree product on actual
four-distinct-vertex rectangles.

The `delta` slack is genuinely needed.  For

```
1 1 0 1
1 1 1 0
1 0 0 0
```

one has `m=7`, row degrees `(3,3,1)`, and column degrees `(3,2,1,1)`.
Its unique ordinary rectangle has degree product `3*3*3*2=54>49`.
The genuine ordered-pair sum in (1), after multiplication by `m^2`,
is `4*(49-54)=-20`; it fails by itself.  The edge certificate has
numerator sum `324` and pays this deficit, leaving total numerator
`304`.  Thus the degenerate and genuine pieces cannot be separated in
a full proof; (8) is the correct remaining interaction.

## 4. Stress families

The three main stress families from the audit are all `C4`-free and are
therefore covered outright:

* the three-edge `L`;
* the double-star family that refutes weak Ky--Fan majorization;
* one universal row plus any number of private degree-one rows at each
  column (the ratio approaches one).

Tensor products need not stay `C4`-free.  The verifier therefore checks
identity (1), rather than assuming the genuine residual vanishes, on
deterministic tensor products as well.

## 5. Verification

The companion verifier uses exact integer numerators.  It

* exhausts every matrix through `4 x 4`;
* checks `delta_ij>=0` on every edge;
* checks identities (7) and (1);
* proves the `C4`-free corollary computationally on every enumerated
  `C4`-free support;
* checks the `L`, double-star, universal-plus-private, and tensor-product
  stress families.

Run

```
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_degenerate_compatibility_sos.py
```
