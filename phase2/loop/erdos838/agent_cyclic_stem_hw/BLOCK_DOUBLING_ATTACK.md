# Block doubling: a finite kill and the surviving prefix-product gate

**Date:** 2026-08-14  
**Verdict:** the coefficientwise block-doubling statement is false with
`b=1`, and even its strictly weaker cumulative version is false with `b=1`.
There are exact integral counterexamples at `n=17,65,129`; the latter two
show that the defect recurs at dyadic boundaries and is not merely a tiny
order-type anomaly.  This does **not** disprove the asymptotic assertion that
some `b=O(log log n)` works: every counterexample found has minimal block
two, and no scalable family with unbounded minimal block was found.  On the
positive side, cumulative doubling is now proved unconditionally through
`k+b<=(1-o(1))sqrt(b log n)`, and the planar ear encoding has been sharpened
from an `O(k)` inverse loss to an absolute factor two.

The clean replacement is a cumulative rank-window inequality.  If

\[
 F_k:=\sum_{j\le k}v_j,
 \qquad F_{k+b}\ge2F_k\quad(0\le k\le\ell-2b),       \tag{CW}_b
\]

where `ell=ceil(log_2 n)`, then the uniform mean rank satisfies

\[
 \mu\ge\ell-3b.                                      \tag{1}
\]

Equivalently, `(CW)_b` asks only that the **whole next rank window** contain
at least as much mass as every preceding rank:

\[
 \sum_{j=k+1}^{k+b}v_j\ge\sum_{j=0}^kv_j.            \tag{2}
\]

It is strictly weaker than `v_(k+b)>=2v_k`, tolerates coefficient cliffs,
and has the right form for a bounded-window repair map.  A still weaker
prefix-product condition, allowing a bounded total number of missing
doublings, is sufficient for Erdős 838 and is isolated in Section 4.

All logarithms are base two and the empty face is included.

## 1. Exact 17-point counterexample

Let `P={(i,y_i):0<=i<=16}`, with

```text
(y_0,...,y_16) =
(-610766, -553100, -480898, -445553, -319263, -72366,
  270063, 589685, 996351, -299655, 2060498, -384200,
  4986319, -526183, -679887, -723778, -808443).
```

Every orientation determinant is nonzero.  Exact enumeration gives

\[
 (v_0,\ldots,v_{17})
 =(1,17,136,680,824,645,349,142,33,3,0,\ldots,0).    \tag{3}
\]

Here `ell=5`.  The original coefficientwise statement with `b=1` fails at
the last required rank `k=3`:

\[
 v_4=824<1360=2v_3.                                 \tag{4}
\]

More significantly, cumulative doubling also fails, albeit narrowly:

\[
 F_3=1+17+136+680=834,
 \qquad F_4=1658<1668=2F_3.                         \tag{5}
\]

The configuration is integral and stretchable.  The verifier recomputes
(3) both by direct hull enumeration and by upward-closing every nonconvex
four-circuit; the two exact profiles agree.

Both coefficientwise and cumulative minimal blocks are two.  For `b=2`
the tested range is only `k<=1`, so (3) is a finite obstruction to a
constant-one formulation, not evidence against the proposed asymptotic
`O(log log n)` window.

### Dyadic-boundary resonance at 65 and 129 points

An independent exact cluster search found two further integral
configurations.  Only the ranks needed by the block tests are displayed:

\[
\begin{array}{c|c|c}
n&\ell&(v_0,v_1,\ldots)\\ \hline
65&7&(1,65,2080,43680,353852,863119,788398)\\
129&8&(1,129,8256,349504,5832916,30290697,65584381,72859822).
\end{array}                                                   \tag{6}
\]

At the terminal required `b=1` rank they satisfy

\[
\begin{array}{c|c|c}
n&\text{coefficient failure}&\text{cumulative failure}\\ \hline
65&788398<2(863119)&2051195<2(1262797)\\
129&72859822<2(65584381)&174925706<2(102065884).
\end{array}                                                   \tag{7}
\]

Both coefficient and cumulative tests pass with `b=2`.  The 65-point set is
a deep cluster modification of the saved 58-point onion record; the
129-point set is a heterogeneous two/three-point blow-up of the same record.
The separate `block_search/verify_block_resonance.py` checker reconstructs
their truncated profiles by exact slope-order cap/cup matrices and audits
all collinearity and block comparisons.  These two cases show a repeatable
finite mechanism, but only at the last adjacent step excluded by `b=2`.
No infinite construction preserving a failure for growing `b` is claimed.
Indeed, exact homogeneous pair iteration of the 129-point example has
minimal-block sequence

\[
 2,2,1,1,1,1,1
\]

at `n=129,258,516,...,8256`.  The dyadic resonance must be recreated by a
fresh nonstationary macro; repeating the same macro self-heals.

## 2. Why cumulative windows suffice

> **Theorem 1 (cumulative block doubling).**  If `(CW)_b` holds, then
> `mu>=ell-3b`.

**Proof.**  Extend the definition by `F_j=0` for `j<0`.  Repeating
`(CW)_b` downward from `ell-b` gives, for every `q>=1`,

\[
 F_{\ell-(q+1)b}\le2^{-q}F_{\ell-b}\le2^{-q}V.       \tag{8}
\]

For the uniform random face rank `K`, the positive deficit identity is

\[
 \mathbb E(\ell-K)_+
 =\sum_{t=1}^{\ell}\Pr(K\le\ell-t)
 =\frac1V\sum_{t=1}^{\ell}F_{\ell-t}.               \tag{9}
\]

The first `b` summands cost at most `bV`.  Group the rest into blocks of
length `b`; (8), including the trivial first block, bounds them by

\[
 bV\sum_{q\ge0}2^{-q}=2bV.                          \tag{10}
\]

Thus `E(ell-K)_+<=3b`.  Since ranks above `ell` only increase the mean,
`mu>=ell-3b`.  QED.

Consequently `(CW)_b` with `b=O(log ell)=O(log log n)` proves

\[
 \mu\ge\log n-O(\log\log n),                       \tag{11}
\]

which is more than enough for the coefficient-one-half lower bound in
Erdős 838.

This universal window statement would also be a major Erdős--Szekeres
advance: (1) forces a convex face of rank at least `ell-3b`, so
`b=O(log ell)` would imply

\[
 ES(t)\le2^{t+O(\log t)}.
\]

That is close to the conjectural `2^(t-2)+1` scale and explains why a
routine local ear proof should not be expected.

The combinatorial target (2) is useful: it would follow from a single
injective routing of every face of rank at most `k` into the faces in ranks
`k+1,...,k+b`.  Unlike coefficientwise doubling, it does not demand that
every source land at one prescribed rank or that local rank ratios behave
monotonically.

### An unconditional initial range

There is a rigorous region in which `(CW)_b` follows from ordinary
Erdős--Szekeres supersaturation.  Put `t=k+b` and `m=ES(t)`.  If

\[
 n\ge m,
 k\le(n-1)/3,
 \qquad
 \binom{n-k}{b}\ge2\binom tb\binom mt,              \tag{12}
\]

then `F_t>=2F_k`.  Indeed, double-counting `m`-sets and one convex
`t`-witness gives

\[
 v_t\ge{\binom nt\over\binom mt},                  \tag{13}
\]

while `k<=(n-1)/3` gives
`F_k<=2 binom(n,k)`.  Finally

\[
 {\binom nt\over\binom nk}
 ={\binom{n-k}{b}\over\binom tb},                  \tag{14}
\]

so (12) implies `v_t>=F_k`.

With the current bound

\[
 \log ES(t)\le t+O(\sqrt{t\log t}),                \tag{15}
\]

condition (12) holds uniformly for

\[
 k+b\le(1-o(1))\sqrt{b\log n}.                     \tag{16}
\]

For `b=Theta(log log n)` this reaches
`Theta(sqrt(log n log log n))`.  The entire remaining difficulty is the
middle-to-near-logarithmic rank range.

## 3. The exact rank-extension product and what it would take

Let `p_r` be the mean fraction of the `n-r` missing points which extend a
uniform convex rank-`r` face.  Cover double counting gives

\[
 p_r={ (r+1)v_{r+1}\over(n-r)v_r}.                  \tag{17}
\]

Therefore the coefficient block ratio is exactly

\[
 {v_{k+b}\over v_k}
 ={(n-k)(n-k-1)\cdots(n-k-b+1)
   \over(k+1)(k+2)\cdots(k+b)}
   \prod_{j=0}^{b-1}p_{k+j}.                        \tag{18}
\]

This makes the quantitative requirement transparent.  A polynomial-loss
rank-extension theorem

\[
 p_r\ge {2^{-r}\over r^C}                           \tag{19}
\]

would prove coefficient block doubling for
`b=(C+O(1))log ell`.  More generally a bound
`p_r>=2^{-r-o(r)}` gives a block `b=o(ell)`, enough for
`mu>=ell-o(ell)` but not automatically the sharper `O(log ell)` loss.

Conversely, if coefficient block doubling fails, (18) forces at least one
rank in the block to have

\[
 {v_{r+1}\over v_r}<2^{1/b},
 \qquad \mathbb E u(A)=(r+1){v_{r+1}\over v_r}
 <2^{1/b}(r+1).                                     \tag{20}
\]

For `b=Theta(log ell)`, this is an almost-minimal-up-degree slice, much
sharper than the current `u(A)<=4(r+1)` hard-family threshold.  Thus the
coefficient conjecture is essentially a polynomial-loss strengthening of
the existing rank-extension gate rather than a free consequence of the
cyclic classification.

## 4. The weaker prefix-product condition

Local doubling in every window is not necessary.  The proof of Theorem 1
uses only the accumulated growth of the prefixes.

For integers `b>=1` and `s>=0`, consider

\[
 \boxed{
 {F_{\ell-b}\over F_{\ell-(q+1)b}}\ge2^{q-s}
 \quad\text{for every }q\ge0,}                     \tag{PT}_{b,s}
\]

with zero denominators interpreted as automatic.  In logarithmic form this
is

\[
 \sum_{j=1}^q
 \log {F_{\ell-jb}\over F_{\ell-(j+1)b}}
 \ge q-s.                                          \tag{21}
\]

So prefix growth must average one bit per block, but it may lose `s` bits
in arbitrary local cliffs.

> **Theorem 2 (prefix-product tail bound).**  If `(PT)_(b,s)` holds, then
> \[
>  \boxed{\mu\ge\ell-(s+3)b.}                      \tag{22}
> \]

**Proof.**  The hypothesis gives

\[
 F_{\ell-(q+1)b}
 \le\min(1,2^{s-q})V.                              \tag{23}
\]

Use (9), retain the first `b` terms trivially, and group the rest into
`b`-blocks.  Since

\[
 \sum_{q\ge0}\min(1,2^{s-q})=(s+1)+1=s+2,          \tag{24}
\]

the positive deficit is at most `(s+3)b`.  QED.

This is the weakest clean block-product target produced by this attack.
It proves the desired mean estimate whenever

\[
 (s+3)b=O(\log\ell).                                \tag{25}

\]

For comparison, the logically exact mean condition is

\[
 \sum_{r<\ell}(\ell-r)v_r-
 \sum_{r>\ell}(r-\ell)v_r
 \le O(\log\ell)V.                                 \tag{26}
\]

No local ratio condition is necessary for (26).  The prefix-product form is
a scale-local, one-sided certificate for it which still exposes a plausible
geometric routing problem.

## 5. The constant-two ear map and the exact remaining gate

For a convex rank-`r` face `A` and an exterior point `p` blocked for `A`,
the exact planar repair is

\[
 I=A\setminus\operatorname{ext}(A+p),
 \qquad B=\operatorname{ext}(A+p)=(A-I)+p,           \tag{27}
\]

where `I` is a cyclic interval of `A` and `|I|+|B|=r+1`.  Fix the hidden
rank `i=|I|`, and let `E_(r,i)` count these incidences.

> **Theorem 3 (constant-two ear encoding).**  For every `r>=4` and
> `1<=i<=r-2`,
> \[
>  \boxed{E_{r,i}\le2v_i v_{r-i+1}.}               \tag{28}
> \]

**Proof.**  Map `(A,p)` to `(I,B)`.  The pair determines the nonconvex set
`S=I dotcup B=A+p`; possible roots `p` are hull vertices of `S` whose
deletion is convex.  A planar nonconvex set has at most two such hull
repairs.  The only delicate case is a triangular hull with at least two
hidden points.  For two hidden points with barycentric coordinates `x_j`
and `y_j`, general position makes the three ratios `x_j/y_j` distinct; a
triangle-vertex deletion can be convex only for the unique middle ratio.
Thus a pair `(I,B)` has at most two preimages, proving (28).  QED.

Summing gives the improved convolution

\[
 E_r\le2\sum_{i=1}^{r-2}v_i v_{r-i+1}.              \tag{29}
\]

This removes the previous factor `r-i+1` completely.  It still lands in a
**pair** of compatible convex faces, not one face; bounding (29) by `V^2`
loses a fatal factor `V`.

There is an exact positive completion inside each fixed frame.  Fix the
root `p`, tangent endpoints `x,y`, source rank `r`, and hidden size `i`.
Let `X_f` be all hidden intervals in the frame and `Y_f` all retained faces
`R=B-p`.  Every cross-union

\[
 I\cup R\quad(I\in X_f,\ R\in Y_f)                 \tag{30}
\]

is a distinct convex rank-`r` face: `I+{x,y}` and `R` are convex polygons
on opposite sides of their common edge `xy`.  Hence

\[
 v_r\ge|X_f||Y_f|.                                  \tag{31}
\]

Sparse incidence inside one frame therefore completes to a larger
rectangle of genuine faces.  The hard case is a nearly complete rectangle
reused across many blockers; controlling that reuse is precisely the
forward two-ended alignment problem.

The cumulative formulation also gives a sharp first-failure reduction.
Suppose `k>=2b` is the first failure of `(CW)_b`.  The two preceding windows
give `F_(k-2b)<=F_k/4`.  Meanwhile cover double counting gives

\[
 \sum_{r=0}^k\sum_{A\in\mathcal F_r}u(A)
 =\sum_{s=1}^{k+1}s v_s
 <2(k+1)F_k.                                        \tag{32}
\]

It follows that at least `F_k/2` faces have rank in `(k-2b,k]` and
`u(A)<=8(k+1)`.  One of those `2b` ranks therefore contains at least

\[
 {F_k\over4b}                                       \tag{33}
\]

low-addable faces.  Optimized hull activity removes the low-exterior-label
part of this slice; every unresolved source has the capped supply of
exterior ears.  Equations (28)--(31) reduce the rest exactly to capped
two-ended Hall.

More seriously, one fixed tangent/interval pocket can contain an arbitrary
smaller planar order type.  Thus no bound on the inverse fibre follows from
the cyclic endpoints alone.  A successful proof of `(PT)_(b,s)` must use a
recursive pocket reset which retains the two tangent endpoints and shows
that at most `s=O(log ell)` doubling bits are lost over the whole recursion.
The current one-root ear map supplies the state, but not that amortized
bound.

## 6. Exact stress tests

The new verifier establishes the following.

1. The 17-point configuration (3) is checked with integral geometry and two
   independent profile algorithms.
2. All 59 previously saved exact profiles have coefficient minimal block at
   most two and cumulative minimal block one.  This includes the hard
   `n=44,58` records and the saved central Pascal profiles.
3. Every one of the 1,222 Pascal cells with row parameter at most 50 has
   both coefficient and cumulative minimal block one.
4. Homogeneous vertical iteration of the 17-point counterexample has
   minimal block two at depth one, but both minimal blocks are one at every
   depth from two through eight (`n=17^8`, `ell=33`).  The finite defect is
   smoothed rather than amplified.
5. The separate dyadic-resonance verifier certifies the `n=65,129` profiles
   and failures in (6)--(7); both configurations still pass every required
   coefficient and cumulative comparison with `b=2`.  Its exact homogeneous
   pair tower repairs the failure after two further levels.
6. The ear-map verifier checks 6,439 exterior incidences, maximum pair fibre
   two, 971 fixed tangent frames and all their rectangle completions, plus
   exact common-ear and common-target obstruction families.

Thus neither the Pascal extremizers nor fixed-template iteration provides a
scalable counterexample.  A genuine obstruction must be nonstationary,
placing a fresh descending profile tail at every new dyadic boundary.  These
finite tests are evidence only; they do not prove `(CW)_b` or `(PT)_(b,s)`.

Run

```bash
python3 phase2/loop/erdos838/agent_cyclic_stem_hw/verify_block_window.py
python3 phase2/loop/erdos838/agent_cyclic_stem_hw/block_search/verify_block_resonance.py
python3 phase2/loop/erdos838/agent_cyclic_stem_hw/ear_map/verify_ear_map.py
```

The scripts write `block_window_certificate.json`,
`block_resonance_certificate.json`, and `ear_map_certificate.json`; every
stored finite comparison is integer or rational.

## 7. Recommended next lemma

The best direct target is now:

> **Cumulative pocket-reset lemma.**  For `b=O(log ell)` and every `q`,
> route `2^(q-O(1))` tokens from each face of rank at most
> `ell-(q+1)b` injectively into the faces of rank at most `ell-b`, or prove
> the resulting cardinality inequality recursively inside a fixed
> two-tangent pocket.

Its counting conclusion is exactly `(PT)_(b,O(1))`; even an
`O(log ell)` total loss with constant `b` suffices.  This formulation is
strictly more tolerant than coefficient block doubling, survives the exact
17-point cliff, and asks the cyclic repair machinery only for amortized
prefix growth rather than a rank-preserving extension at every step.

On the computational side, the first meaningful falsification attempt is a
direct `n=257` or `513` search for a `b=2` failure, seeded by a genuinely new
onion macro.  Further homogeneous blow-ups of the 129-point example test the
wrong regime: their exact recurrence already shows self-healing.
