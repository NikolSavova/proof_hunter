# Physical-wedge dyadic Carleson gate

## 1. Purpose

The repeated mixed same-centre term is already a sum of triangle loads of
four-line completion blocks.  This note adds the physical endpoint that was
implicit in that formulation and separates, with no loss, the part paid by
the `k^3` allowance from the part that must use height.

The result is a sharper restart for the direct `1/3` attack.  It is not a
proof of Erdős 1208: one endpoint-sensitive high-wedge estimate remains.

Throughout, `A` is a `k`-point distance-Sidon set.  The notation for the
same-centre fibres and their cross-translate cells is that of
`SWAP_MIXED_SAME_CENTRE_TRIPLE_INTERSECTION_GATE.md` and
`SWAP_COMPLETION_DIAGONAL_FOUR_LINE_GATE.md`.

## 2. The physical-wedge partition

Every mixed `V`--`W` pair used in the same-centre sum has a unique common
physical endpoint `x`.  Retain

1. `x`;
2. the incident directed `V`-edge label;
3. the incident directed `W`-edge label; and
4. the two endpoint roles, one in `{0,1}` and one in `{2,3}`.

Call this five-tuple an oriented physical wedge `w`.  For each translate
cell `S` over `w`, put `r(S)=|S|` and define

\[
 M(w)=3\sum_{S\mapsto w}{r(S)\choose3},\qquad
 Q(w)=\sum_{S\mapsto w}{r(S)\choose2}.             \tag{2.1}
\]

The assignment is lossless:

\[
 \boxed{\displaystyle
 C_{\rm center}=\sum_w M(w).}                      \tag{2.2}
\]

For fixed `x` and fixed endpoint roles, each other endpoint determines the
directed incident edge uniquely.  Hence

\[
 \#\{w\}\le 4k(k-1)^2.                             \tag{2.3}
\]

The same-edge subfamily has at most `4k(k-1)` wedges; the genuine
one-common-endpoint subfamily has at most `4k(k-1)(k-2)`.

## 3. Exact two-threshold decomposition

Fix a wedge threshold `P>=0` and an integer cell threshold `R>=3`.  Put

\[
 M_R(w)=\sum_{\substack{S\mapsto w\\r(S)\ge R}}
 3{r(S)\choose3},
 \qquad
 H_{P,R}=\sum_{w:M_R(w)>P}M_R(w).                 \tag{3.1}
\]

Since

\[
 3{r\choose3}=(r-2){r\choose2},                    \tag{3.2}
\]

every cell with `r<R` has third mass at most
`(R-3) binom(r,2)`.  Moreover, every wedge with `M_R(w)>0` contains a
cell of load at least `R`, so it consumes at least `binom(R,2)` units of
`Q_phys`.  Splitting first by cell load and then by the *rich-cell mass* of
its wedge gives

\[
 \boxed{\displaystyle
 C_{\rm center}
 \le \left(R-3+{P\over {R\choose2}}\right)
       Q_{\rm phys}+H_{P,R}.}                       \tag{3.3}
\]

where `Q_phys=sum_w Q(w)` is precisely the same-centre part of the existing
second-generation parallel pencil, and in particular is bounded by the
full `W_parallel` reservoir.  This removes the ambient wedge-count loss
altogether and is stronger than thresholding the total `M(w)`: already-paid
low-load cells cannot falsely promote a wedge into `H_{P,R}`.

Independently, if `low` means the older total-mass condition `M(w)<=P`,
there are classwise bounds

\[
 C_{\rm same\ edge}^{\rm low}\le4Pk(k-1),\qquad
 C_{\rm one\ endpoint}^{\rm low}\le4Pk(k-1)(k-2). \tag{3.4}
\]

The classwise form is retained because its different `k^2`/`k^3`
capacities may still help in a refined argument.  But for
`P,R=N^{o(1)}`, (3.3) already pays *all* non-heavy mass directly by
`N^{o(1)}W_parallel`.  Only `H_{P,R}` remains.

## 4. The direct high-wedge theorem

The clean theorem to attack is

\[
 \boxed{\displaystyle
 H_{P,R}\le N^{o(1)}m^2}                            \tag{4.1}
\]

for some subpolynomial thresholds `P,R`.  Thus every surviving wedge carries
more than `P` mass *from cells of load at least `R`*.  The statement is
substantially narrower than a pointwise bound on every wedge or every
four-line cell.  It allows the lifted modular-parabola equality model to
spend the entire ambient `m^2` allowance.

Each cell in (4.1) is simultaneously:

- a four-line intersection in the diagonal completion reservoir;
- a clique of synchronized two-completion squares;
- a set whose translates `-S` and `JS` lie in the directed-difference set;
  and
- a block with perpendicular footprint `JS-S`.

The existing footprint dichotomy says that such a cell either has large
metric support, or it contains many differences popular in both directions
`u` and `Ju`.  Consequently a proof of (4.1) must do one of two genuinely
endpoint-sensitive things:

1. Carleson-pack the large footprints into determinant/height cells; or
2. turn perpendicular popularity into a reusable completion core and run a
   density increment with a decreasing endpoint resource.

Ambient representation depth alone cannot prove (4.1): the separated
parabola model in the same-centre note has a factor-`|S|` pointwise depth
loss.  The common physical endpoint and the four completion lines are
load-bearing.

## 5. Finite stress

The augmented optimal-core analyzer gives:

\[
\begin{array}{c|r|r|r|r|r}
\text{family}&C_{\rm center}&\#w&\max M(w)&
 C_{\rm same\ edge}&C_{\rm one\ endpoint}\\ \hline
\text{Costas }23&204&68&3&24&180\\
\text{Costas }29&4857&945&48&774&4083\\
\text{Costas }31&5058&418&123&1992&3066
\end{array}
\]

At `p=31`, the top same-edge wedge has mass `123`, and the top genuine
one-endpoint wedge has mass `108`.  In both cases a single load-six cell
contributes `60`; the remaining mass comes from only a handful of load-three
and load-four cells.  This supports the two-threshold formulation: high
wedge mass is already concentrated into genuinely rich four-line cells.

The same two wedges have resonant/transverse splits `93+30` and `87+21`.
The resonant branch is therefore a worthwhile first subproblem, but it does
not exhaust the obstruction.

There is one further lossless inverse audit.  For an unordered parameter
triple `T`, let `mu(w,T)` be the number of four-line cells over `w` which
contain `T`.  Then

\[
 \boxed{\displaystyle
 C_{\rm center}=3\sum_{w,T}\mu(w,T).}             \tag{5.1}
\]

The tempting claim `mu<=1` is false.  Exact profiles are

\[
\begin{array}{c|r|r|r}
\text{family}&\#\{(w,T):\mu>0\}&\max\mu&
 \sum_{w,T}{\mu\choose2}\\ \hline
\text{Costas }23&68&1&0\\
\text{Costas }29&1583&2&36\\
\text{Costas }31&1386&4&366\\
\text{Costas }37&1604&2&28
\end{array}
\]

At the multiplicity-four rows the owners form small two-by-two translation
rectangles: two centre choices combine with two cross shifts.  Thus a
physical wedge plus three parameters does not determine the cell.  Any
inverse theorem must either retain one completion corner or control these
translation rectangles in aggregate; literal triple rigidity is closed as
a shortcut.

Three major barrier families are benign for this particular term.  Dense
one-dimensional Golomb rulers through `k=14`, the explicit lifted residue
parabolas through prime `43`, and the genuine `k=48`, codegree-`49`
rank-flat certificate all have `C_center=0` (some can have cross-cell load
one, but never load three).  Thus the four-line high-wedge gate is not
merely a restatement of the collinear-core, modular-parabola, or collective
high-codegree obstruction.  This is finite evidence, not an asymptotic
theorem, but it is an important kill-search result for choosing the next
lemma.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_physical_wedge_dyadic_carleson.py
```

The verifier exhausts the oriented-wedge counts, checks the lossless mass
partition and (3.3)--(3.4) on random cell systems, checks the stored Costas
stress and triple-owner rows, and reruns small genuine Golomb and
lifted-parabola controls.
It also reruns the rank-flat `k=48` certificate.  The main analyzer
independently asserts physical-wedge mass conservation whenever actual
endpoints are available.
