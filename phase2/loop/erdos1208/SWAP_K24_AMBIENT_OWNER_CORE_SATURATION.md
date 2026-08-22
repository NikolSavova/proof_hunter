# High-load ambient K2,4 owners saturate the selected core

## 1. Outcome

The physical support in the selected K2,4 tensor has two logically
different parts:

1. the three swap cells and their physical endpoint geometry exist; and
2. all three cells lie in the chosen dyadic optimal-orientation core.

The second condition is automatic at high cell load.  Let `t` be the
dyadic core level and let an ambient matching owner consist of

\[
 C=(c,\ell),\qquad C_a=(c+a,\ell+La),\qquad
 C_b=(c+b,\ell+Lb),\qquad L=I+J.                 \tag{1.1}
\]

For one cross colour `e`, let `r` be the number of synchronized parameters
belonging to both edge bundles `CC_a` and `CC_b`.  Then

\[
 \boxed{r\ge \lceil3t/2\rceil\quad\Longrightarrow\quad
        C,C_a,C_b\in U_t.}                       \tag{1.2}
\]

Consequently every ambient matching owner of load at least `ceil(3t/2)` is already
a selected-core owner, with exactly the same parameter set.  The selected
support indicator can therefore be removed **losslessly on the high tail**.
All support loss is confined to cells below that threshold, whose third
mass is at most `(ceil(3t/2)-3)` times the already-paid physical pair
reservoir.

This is a genuine reduction.  It removes both the nested-core indicator and
the apparently necessary restriction to colours previously witnessed in
the core from the rich tail.  What remains there is a literal ambient
endpoint-incidence problem.

## 2. Parallel-bundle saturation lemma

Let a finite loopless multigraph be given a quadratic-optimal orientation,
and write `x_v` for the outdegree of `v`.  Suppose the unordered pair
`{u,v}` supports `mu` parallel edge copies.  Then for every integer `t>=1`,

\[
 \boxed{\mu\ge2t\quad\Longrightarrow\quad
        x_u,x_v\ge t.}                           \tag{2.1}
\]

To prove this, let `s` copies point from `u` to `v`.

* If `0<s<mu`, reversing one copy in either direction is an admissible
  one-edge variation.  Optimality gives `|x_u-x_v|<=1`.  The bundle itself
  contributes `mu` to `x_u+x_v`, so `min(x_u,x_v)>=floor(mu/2)>=t`.
* If `s=mu`, then `x_u>=mu`.  Reversing a copy gives
  `x_u<=x_v+1`, hence `x_v>=mu-1>=t`; the case `s=0` is symmetric.

The constant two is sharp: a bundle of `2t-1` copies may be split into
outdegrees `t` and `t-1`.

We also use the path form of the same optimality condition: if a directed
path runs from `u` to `v`, reversing one copy along the path changes only
the two endpoint loads and gives `x_u<=x_v+1`.

Each parameter in an ambient owner is one edge copy in each of the bundles
`CC_a` and `CC_b`.  Both multiplicities are therefore at least `r`.  Using
the two bundles simultaneously sharpens (2.1).  Suppose, for instance,
that `x_(C_a)<t`.  Since `r>=t`, at least one copy points from `C` to
`C_a`, so the path-reversal optimality condition gives `x_C<=t`.  Since
`r>t`, not all copies of the other bundle can point from `C` to `C_b`;
hence a copy points from `C_b` to `C`, and the directed path

\[
 C_b\longrightarrow C\longrightarrow C_a
\]

gives `x_(C_b)<=x_(C_a)+1<=t`.  Therefore

\[
 2r\le x_C+x_{C_a}+x_{C_b}\le3t-1,
\]

contradicting `r>=ceil(3t/2)`.  The other low-vertex cases are symmetric.
The constant `3/2` is sharp: the isolated two-bundle star distributes its
`2r` outgoing copies as evenly as possible across three vertices.
Equivalently, every ambient owner, without reference to a preselected
level, satisfies the natural-level bound

\[
 \boxed{
 \min\{x_C,x_{C_a},x_{C_b}\}\ge\lfloor2r/3\rfloor.} \tag{2.2}
\]

This is the form to use in a future level-raising argument: a very rich
owner automatically lives in a proportionally higher nested core.

## 3. The corrected ambient-owner support

Put

\[
 \ell=z-J(c+a),\qquad V=c+a,\qquad W=\ell+Lb.     \tag{3.1}
\]

For fixed endpoint roles, let `H^epsilon_{a,b}` be the set of `(z,c)` such
that

\[
 c,c+a,c+b,\ell,\ell+La,\ell+Lb\in D,            \tag{3.2}
\]

the two physical edges `V,W` meet at the prescribed endpoint, and both
swap edges `CC_a,CC_b` lie in the endpoint-disjoint matching category.
This is the true ambient owner support.  It is independent of `e`.

The two middle conditions in (3.2),

\[
 c+b\in D,\qquad \ell+La\in D,                   \tag{3.3}
\]

are load-bearing.  Keeping only `V,V-a,W,W-Lb in D` records a physical
wedge but not necessarily the other two coordinates of the three swap
cells.  That weaker relaxation is much larger and does not support the
bundle argument.

With the three factor sets from
`SWAP_K24_ADAPTIVE_POPULAR_THREE_FACTOR_GATE.md`, the ambient owner load is

\[
 r_{a,b,e}(z,c)
 =|\{f\in S_e:z-Jf\in Y_{a,b,e},\ c-f\in Q_{a,b,e}\}|. \tag{3.4}
\]

Thus, using falling factorial notation `(r)_3=r(r-1)(r-2)`,

\[
 \boxed{
 \sum_{\epsilon,a,b,e}
 \sum_{(z,c)\in H^\epsilon_{a,b}\,:\,
       r\ge\lceil3t/2\rceil}(r)_3
 =2C_{\rm center}^{\ge\lceil3t/2\rceil}.}       \tag{3.5}
\]

The factor two is only a convention: the selected mass uses
`3 binom(r,3)=(r)_3/2`, whereas the tensor analyzer reports `(r)_3`.

For the complementary selected cells,

\[
 \boxed{
 C_{\rm center}^{<\lceil3t/2\rceil}
 \le(\lceil3t/2\rceil-3)_+Q_{\rm phys}.}        \tag{3.6}
\]

Equations (3.5)--(3.6) are exact for every dyadic level.  In particular,
when `t=N^{o(1)}`, the low term is already at target scale and the only
remaining theorem is the high-tail ambient endpoint tensor (3.5), with no
core-selection weight left inside the summand.

## 4. Genuine stress

The optimal-core analyzer now constructs `H^epsilon_{a,b}` directly,
checks both underlying multigraph bundle multiplicities, and asserts (3.5)
cell by cell above the threshold.  The first three transformed Costas
stresses give

\[
\begin{array}{c|c|c|c|c|c}
 &t& C_{\rm center}&\sum_H(r)_3&\max_H r&k^3+m^2\\ \hline
p=23&2&204&408&3&28{,}072\\
p=29&4&4{,}857&10{,}212&5&128{,}228\\
p=31&2&5{,}058&10{,}116&6&307{,}900.
\end{array}                                      \tag{4.1}
\]

At `p=23,31`, the threshold is three, so every positive cubic ambient cell
is recovered in the selected core with identical load.  At `p=29`, the
threshold is six and the ambient maximum is five, so its modest excess over
twice the selected mass lies entirely in the already-paid low branch.

The earlier physical-edge-only counts (`7,248`, `195,828`, `128,856`) are
superseded: they omitted (3.3).  They remain valid upper envelopes but are
not the sharp continuation.

## 5. Remaining boundary

This theorem does not itself bound the high tail.  It makes its support
canonical:

* six actual swap-cell coordinates;
* two endpoint-disjoint matching edges sharing one centre;
* one common physical endpoint between the selected incident coordinates;
* the six synchronized `D` tracks and four adaptive-popular corners; and
* load at least `2t`.

The next proof should attack this ambient endpoint incidence directly.
For subpolynomial `t`, no optimal-core or active-colour bookkeeping remains.
For polynomial `t`, one must additionally exploit the dyadic core density
`t|U_t|<=|E|`; (3.6) alone then loses a power.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_k24_ambient_owner_core_saturation.py
python3 phase2/loop/erdos1208/analyze_swap_optimal_nested_cores.py --k24-prime=31 --k24-physical-tensor-fast
```

The standalone verifier exhausts small multigraph orientations and checks
the parallel-bundle lemma on every optimum, including the sharp
`2t-1` example.  The genuine analyzer independently verifies the owner
coordinate conditions, both bundle multiplicities, core saturation, and
the exact high-tail equality.
