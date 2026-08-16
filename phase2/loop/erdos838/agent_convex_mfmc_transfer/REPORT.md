# Hachimori--Nakamura MFMC versus the half-weight pocket flow

**Date:** 2026-08-14  
**Verdict:** the Hachimori--Nakamura theorem is a useful *local integral
rounding theorem for one fixed root*, but it does not supply the weighted
Hall/pocket-restart theorem needed for Erdős 838.  There is an exact and
particularly strong barrier: the exponential apex/concave-chain family has
**no Pentagon obstruction for any root**--every fixed-root stem clutter has
MFMC--while any transport which remembers only one rooted circuit has
congestion

\[
 \Omega\!\left((3/2)^N/N^3\right).
\]

Thus decomposing or eliminating Pentagons cannot by itself prove either
`H(P)=n^{o(1)}` or the stronger polylogarithmic loss corresponding to
`X(pi)>=log_2 n-O(log log n)`.  A successful use of MFMC must first retain a
convex face inside the hidden pocket (or equivalent information carrying the
whole history); MFMC may then round the choice of a witness triangle without
additional loss.

No solution of Erdős 838 is claimed here.

## 1. Source audit

The published source is

* M. Hachimori and M. Nakamura, *The max-flow min-cut property of
  two-dimensional affine convex geometries*, Discrete Mathematics **308**
  (2008), 1674--1689, DOI
  [10.1016/j.disc.2006.10.018](https://doi.org/10.1016/j.disc.2006.10.018).

The journal and author pages expose the abstract and the three published
figures.  The journal PDF endpoint presented a CAPTCHA to automated access,
so I do not claim a line-by-line audit of the full 2008 proof.  I did read in
full the authors' directly related 17-page primary exposition

* M. Hachimori, *On the rooted circuits of affine point configurations with
  kernel*, RIMS Kokyuroku 1349 (2005), 187--203
  ([author PDF](https://www.sk.tsukuba.ac.jp/~hachi/archives/circuits3.pdf)).

That exposition gives the definitions, the deletion/contraction geometry,
and the same forbidden-minor MFMC theorem as the Hachimori--Nakamura
preprint.  It identifies the forbidden clutter explicitly as

\[
 C^3_5=\{123,234,345,451,512\}.                    \tag{1}
\]

The 2008 paper calls the corresponding planar realization a **Pentagon
configuration with center/root** `e`.  Its published Fig. 2 labels the five
points in ordinary circular order and draws the star order underlying (1).

## 2. What the theorem actually says

For a planar point configuration in general position and a fixed point `e`,
put

\[
 \mathcal C_e=
 \operatorname{Min}\{X\subseteq P\setminus\{e\}:e\in\operatorname{conv}X\}.
                                                               \tag{2}
\]

Every nonempty member of (2) is a triangle.  It is the **stem** of a rooted
four-circuit `(X,e)`.  Hachimori--Nakamura prove that this fixed-root clutter
has the MFMC property if and only if the configuration contains no Pentagon
centered at `e` (equivalently, no minor (1)).

For a clutter `C` with incidence matrix `A`, MFMC means that for every
integral nonnegative capacity/cost vector `w`, the point-cover and stem-pack
linear programs have integral optimal solutions and the same value:

\[
 \min\{w^Tx:Ax\geq\mathbf1,\ x\geq0\}
 =
 \max\{\mathbf1^Ty:A^Ty\leq w,\ y\geq0\}.            \tag{3}
\]

The rows of `A` are minimal stem triangles and its columns are **points**.
There is no face-lattice variable in (3).

The kernel formulation makes the minor operations especially clear.  If

\[
 \mathcal S(V\cup\{r\},T)
 =\operatorname{Min}\{X\subseteq V:r\in\operatorname{conv}(X\cup T)\},
                                                               \tag{4}
\]

then the primary exposition proves

\[
 \begin{aligned}
 \mathcal S(V\cup\{r\},T)\setminus A
   &=\mathcal S((V\setminus A)\cup\{r\},T),\\
 \mathcal S(V\cup\{r\},T)/B
   &=\mathcal S((V\setminus B)\cup\{r\},T\cup B).
 \end{aligned}                                                \tag{5}
\]

Deletion really removes points.  Contraction does **not** enter a geometric
pocket: it moves points into the kernel.  This distinction prevents the
forbidden-minor proof from automatically becoming a recursion for the
convex-subset partition function.

For reference, the obstruction (1) already fails packing at unit capacity:
its maximum integral packing is `1`, its minimum integral transversal is
`2`, and the common fractional optimum is `5/3`.

## 3. Translation to the half-weight attack

The half-weight residual flow for

\[
 nZ_P(1/2)\leq n^{o(1)}Z_P(1)                       \tag{6}
\]

has sources `(A,p)`, where `A` is a convex-position face and insertion of
`p` is bad, with demand

\[
 d(A,p)=2^{-|A|}.                                    \tag{7}
\]

Its targets are convex faces `B`, with residual capacities such as

\[
 c(B)=2-\frac{3|B|}{2^{|B|}}\geq\frac12.             \tag{8}
\]

The desired assertion is a Hall inequality for an exponentially large
**bad-incidence versus convex-face** bipartite graph.  This differs from (3)
in three essential ways.

1. **Fixed root versus varying hidden root.**  If `p` is interior to
   `conv(A)`, it is a root and a triangle in `A` witnesses the failure.  But
   for a blocked exterior insertion, `p` is not in `conv(A)` and its stem
   clutter may be empty.  The roots are the vertices of `A` hidden by `p`,
   and they vary along the visible chain.
2. **Minimal witness versus complete history.**  One rooted circuit records
   four points.  The source `(A,p)` can contain an arbitrarily large hidden
   subset.  The half-weight source mass depends on all those subsets.
3. **Point capacities versus face capacities.**  MFMC packs stem triangles
   under capacities on points.  The target in (6) is an actual convex face,
   and simultaneous reuse of overlapping pockets is the Hall issue.  An
   integral stem packing does not choose, or even certify the existence of,
   enough distinct target faces.

So (3) can at most round a *witness selection layer* inside a larger
history-preserving flow.

## 4. Exact Pentagon-free exponential barrier

Let `N>=4`, `L=N-1`, and take

\[
 q_i=(i,i(L-i))\quad(0\leq i<N),\qquad
 p=(-1,N^2).                                          \tag{9}
\]

These integral points are in general position.  The `q_i` form a strict
concave convex chain, and for every `i<j<k`,

\[
 q_j\in\operatorname{int}\operatorname{conv}\{p,q_i,q_k\}.     \tag{10}
\]

### Proposition 1 (all rooted clutters have MFMC)

The fixed-root stem clutter is empty for root `p`, `q_0`, or `q_(N-1)`.  For
an internal root `q_j`, it is exactly

\[
 \mathcal C_{q_j}
 =\{\{p,q_i,q_k\}:0\leq i<j<k<N\}.                  \tag{11}
\]

In particular, every edge contains `p`, and after contracting `p` the
clutter is the edge clutter of the complete bipartite graph between

\[
 L_j=\{q_i:i<j\},\qquad R_j=\{q_k:k>j\}.             \tag{12}
\]

For every integral capacity vector `w`,

\[
 \tau_w(\mathcal C_{q_j})=\nu_w(\mathcal C_{q_j})
 =\min\left\{w_p,\sum_{i<j}w_{q_i},\sum_{k>j}w_{q_k}\right\}.
                                                               \tag{13}
\]

Thus every root is MFMC, directly and hence also by the Hachimori--Nakamura
characterization: there is no centered Pentagon anywhere in (9).

**Proof.**  A subset of the `q_i` is always in convex position, so it cannot
contain another `q_j` in its hull.  Equation (10) then gives precisely (11).
For (13), a transversal either chooses `p`, or must cover every edge of the
complete bipartite graph in (12), forcing all of `L_j` or all of `R_j`.
Conversely, a capacitated integral packing is a bipartite `b`-matching, whose
size is the minimum of the two side capacities, additionally truncated by
the common apex capacity `w_p`.  QED.

### Proposition 2 (one-circuit compression is exponentially bad)

Put `I={q_1,...,q_(N-2)}`.  For each nonempty `C subset I`,

\[
 A_C=\{q_0,q_{N-1}\}\cup C                            \tag{14}
\]

is a convex face, while inserting `p` hides all of `C`.  These bad histories
have total half-weight demand

\[
 \sum_{\varnothing\ne C\subseteq I}2^{-|A_C|}
 =\frac14\left(\left(\frac32\right)^{N-2}-1\right).  \tag{15}
\]

The total number of possible fixed-root stem labels in the whole
configuration is only

\[
 \sum_{j=1}^{N-2}j(N-1-j)={N\choose3}.               \tag{16}
\]

Consequently any map or flow state which replaces a history by only one HN
rooted circuit has a fibre of half-weight at least

\[
 \frac{\frac14((3/2)^{N-2}-1)}{\binom N3}
 =\Omega\left((3/2)^N/N^3\right).                    \tag{17}
\]

This remains exponential despite complete absence of Pentagons.  Even
remembering a bounded number of rooted circuits leaves only polynomially
many states and has the same qualitative failure.  The Boolean family of
faces supported inside `I` is precisely the capacity that was discarded.

## 5. Why a Pentagon decomposition does not give an asymptotic escape

The asymptotic target permits `n^{o(1)}` congestion; the useful path form
`X(pi)>=log_2 n-O(log log n)` permits a polylogarithmic loss.  This does not
rescue a direct HN argument.

* The no-Pentagon family (9) already has exponential one-circuit congestion,
  so the number of Pentagon branches is not the relevant potential.
* HN's deletion/contraction operations (5) act on the **stem clutter** and
  change the kernel.  They do not give a decomposition identity for
  `Z_P(1/2)` or disjoint pools of convex faces.
* When a Pentagon is present, the theorem says MFMC is false; it does not
  provide a bounded-loss decomposition into MFMC pieces.  Paying even a
  fixed factor at every recursive obstruction is fatal on configurations
  with linear onion depth.  For a polylogarithmic final loss, the number of
  uncompensated constant-factor restarts would have to be `O(log log n)`;
  for `n^{o(1)}` it must be `o(log n)`.  No such bound follows from the
  theorem.
* The geometric contraction in (5) can merge many different tangent
  histories into the same kernel state, exactly the entropy loss measured
  by (15)--(17).

Hence a "delete/contract every Pentagon and restart" proof has an exact
barrier before one even reaches the Pentagon case.

## 6. A viable, narrower use of the theorem

HN can still be valuable after the hard part of the proof has been solved.
The correct lifted state would look like

\[
 (B;x,T),                                               \tag{18}
\]

where `B` is a convex target face retaining the pocket/history, and `(T,x)`
is a rooted circuit witnessing the local transition.  For each fixed `x`, a
fractional allocation among the witness triangles `T` could then be rounded
with no loss whenever `C_x` is Pentagon-free.  A Pentagon would be a
constant-size local rounding defect, to be paid by additional face capacity.

But the missing theorem remains the history layer:

> **History-preserving HN lift.**  Construct allowed lifted targets (18) and
> prove, for every source set `X`,
> \[
>   \sum_{s\in X}2^{-|A_s|}
>   \leq n^{o(1)}
>   \sum_{B\in\bigcup_{s\in X}\Gamma(s)}c(B),          \tag{19}
> \]
> while charging every Pentagon rounding defect to a distinct or
> telescoping unit of face entropy.

The MFMC theorem can handle the projection `(B;x,T)->(x,T)`; it supplies no
bound for the multiplicity of that projection.  Proposition 2 proves that
this multiplicity is the central issue.

## 7. Verification

Run from the repository root:

```bash
python3 -m py_compile \
  phase2/loop/erdos838/agent_convex_mfmc_transfer/verify_transfer_barrier.py

python3 \
  phase2/loop/erdos838/agent_convex_mfmc_transfer/verify_transfer_barrier.py \
  --chain-points 9
```

The verifier uses exact integer orientations, enumerates every rooted stem,
checks (11), records the closed-form MFMC certificate (13), and verifies the
half-weight identities (15)--(17) with exact rational arithmetic.

`vision_ocr.swift` is the reproducible macOS Vision OCR helper used to read
the scanned author exposition; it is not part of the mathematical checker.
