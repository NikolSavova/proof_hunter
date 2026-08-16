# Counterexample to positive-part genuine-rectangle charging

## Statement refuted

In the notation of `DEGENERATE_COMPATIBILITY_SOS.md`, let

\[
 x_{ij}=d_i e_j/m
\]

and let `Gamma` be the ordered pairs `((i,j),(k,l))` of opposite
edges of genuine four-distinct-vertex rectangles.  The tempting
strengthening

\[
 \sum_{\Gamma}(x_{ij}x_{kl}-1)_+
 \le \sum_{ij\in E}\delta_{ij}                         \tag{P}
\]

is false.  Consequently a proof of the original weighted `C4`
inequality cannot discard the helpful genuine rectangles with
`x_ij x_kl<1`; cancellation inside the genuine-rectangle sum is
essential.

## Exact `4 x 4` counterexample

Take

\[
 A=\begin{pmatrix}
 1&1&1&1\\
 1&1&1&1\\
 1&1&1&1\\
 1&0&0&0
 \end{pmatrix}.
\]

Thus `m=13`, the row degrees are `(4,4,4,1)`, and the column degrees
are `(4,3,3,3)`.

Every genuine rectangle uses two of the first three rows.  For an
ordered pair of such rows there are:

* six ordered distinct-column pairs involving column zero and one of
  columns one, two, three.  Their degree-product numerator is
  `4*4*4*3=192`, so each has excess `192-13^2=23`;
* six ordered distinct-column pairs wholly among columns one, two,
  three.  Their numerator is `4*4*3*3=144`, so each has helpful
  deficit `13^2-144=25`.

There are six ordered pairs of the first three rows.  Hence, after
multiplication by `m^2=169`,

\[
 \sum_{\Gamma}(x_ex_f-1)_+=6\cdot6\cdot23=828,             \tag{1}
\]

whereas the helpful negative part has numerator

\[
 \sum_{\Gamma}(1-x_ex_f)_+=6\cdot6\cdot25=900.             \tag{2}
\]

The edge certificates have the following exact numerators
`m^2 delta_e`:

* `87` on each of the three edges from a degree-four row to column
  zero;
* `50` on each of the nine edges from a degree-four row to columns
  one, two, three;
* `0` on the leaf edge.

Therefore

\[
 m^2\sum_e\delta_e=3\cdot87+9\cdot50=711<828,              \tag{3}
\]

which refutes (P).

## Why the original inequality survives

The signed genuine residual is helpful:

\[
 m^2\sum_{\Gamma}(1-x_ex_f)=900-828=72.
\]

The exact decomposition from the degenerate certificate gives

\[
 m^2(C-x^TRx)=711+72=783>0.
\]

Directly, `(C,W)=(151,24736)` and

\[
 m^2C-W=169\cdot151-24736=783.
\]

This example rules out every charging proof that first replaces the
signed genuine residual by its positive excess.  A valid proof must
retain cancellation among rectangles of different column/row degree
profiles, or find a different source of slack beyond the present
`delta_e` certificates.

## Verification

Run

```
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_positive_genuine_counterexample.py
```

The verifier uses integer arithmetic only and checks every displayed
quantity as well as the full compatibility identity.

