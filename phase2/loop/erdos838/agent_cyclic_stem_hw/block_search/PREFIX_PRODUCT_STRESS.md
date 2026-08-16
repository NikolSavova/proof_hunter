# Prefix-product stress test: no scalable obstruction in the standard hard families

**Date:** 2026-08-14  
**Status:** exact verifier passes; no scalable kill found.

Write

\[
 F_k=\sum_{j\le k}v_j,\qquad \ell=\lceil\log_2 n\rceil.
\]

For a block length `b`, the prefix-product condition with slack `s` is

\[
 (PT)_{b,s}:\qquad
 \frac{F_{\ell-b}}{F_{\ell-(q+1)b}}\ge 2^{q-s}
 \quad(q\ge0),                                      \tag{1}
\]

whenever the denominator rank is nonnegative.  Its smallest integral slack
was computed by integer comparisons only; logarithms are used only to report
the finer real slack

\[
 s_{\mathbb R}=\max_q\left(
 q-\log_2\frac{F_{\ell-b}}{F_{\ell-(q+1)b}}
 \right)_+ .                                        \tag{2}
\]

The significance is that `(PT)_(b,s)` implies the mean-rank lower bound
`mu >= ell-(s+3)b`.  Thus the relevant cost is `(s+3)b`.

## Headline result

Every tested scalable nested-prefix and product-grid family satisfies the
strongest possible statement `(PT)_(b,0)` for **every** block `b`.  The three
previous dyadic-boundary counterexamples to adjacent cumulative doubling have
integral slack exactly one at `b=1` and slack zero for all larger blocks.  That
one-unit defect disappears after one homogeneous pair blow-up, and likewise
after one nontrivial vertical iteration of the 17-point template.

| family | exact cases | largest case | maximum integral slack | best `(s+3)b` |
|---|---:|---:|---:|---:|
| parabolic nested prefixes | 9 | `n=260`, `ell=9` | 0 | 3 |
| independently realized product grids | 21 | `r=64, M=2` | 0 | 3 |
| symbolic scalable product grids, `M=2^r` | 7 | `r=64`, `n=1162144876643701751810`, `ell=70` | 0 | 3 |
| dyadic examples plus pair tower | 10 | `n=8256`, `ell=14` | 1, only at base cases | at most 4 |
| vertical powers of the 17-point example | 12 | `n=17^12`, `ell=50` | 1, only at depth 1 | at most 4 |

In particular, this search found no family with `s` growing at all, much less
`s >> log ell`.

## 1. The only positive-slack witnesses are finite one-step cliffs

The exact `b=1` failures are

\[
\begin{array}{c|c|c|c}
n&\ell&F_{\ell-1}/F_{\ell-2}&s_{\mathbb R}\\ \hline
17&5&1658/834&0.0086752819\ldots\\
65&7&2051195/1262797&0.3001580880\ldots\\
129&8&174925706/102065884&0.2227584048\ldots
\end{array}                                          \tag{3}
\]

Each ratio is below two, so the least integral slack is one.  In all three
cases the worst test is `q=1`; there is no accumulated deficit farther down
the prefix chain.  Every `b>=2` has slack zero.

For the exact homogeneous pair tower over the 129-point example, depth zero
has slack one and depths one through six have slack zero.  For homogeneous
vertical powers of the 17-point example, depth one has slack one and depths
two through twelve have slack zero.  Repeating a bounded bad macro therefore
does not repeat its prefix-product debt: convolution supplies enough lower-rank
mass for the anchored numerator to amortize the original cliff.

## 2. Long nested-prefix pockets are harmless for `(PT)`

The tested integral family has depth `d` and `n=d+4`:

\[
 u=(0,0),\quad c=(2d+4,0),\quad
 p_j=(j,j(j-2d-4))\ (1\le j\le d),                  \tag{4}
\]

together with the points `(d+2,1)` and `(d+2,(2d+4)^2)`.  Exact profiles were
computed for

\[
 d=1,2,4,8,16,32,64,128,256.                       \tag{5}
\]

All blocks have slack zero in every case.  Structurally this is unsurprising:
deleting either one of the two final guard points leaves a convex set.  More
generally, if an `n`-point set contains a convex `(n-1)`-subset and
`A_t=\sum_{j\le t}\binom{n-1}{j}`, then

\[
 F_t\le A_t+A_{t-1},\qquad F_{t+1}\ge A_{t+1}.       \tag{6}
\]

Thus the elementary binomial inequality

\[
 \binom{n-1}{t+1}\ge A_t+2A_{t-1}                  \tag{7}
\]

already implies adjacent cumulative doubling at rank `t`.  The nested-prefix
construction is therefore a poor candidate for a scalable prefix-product
obstruction: its long geometric pocket is accompanied by an almost-convex
reservoir of faces.

## 3. Exact product-grid recurrence

The product family uses a macro configuration with `r+1` blocks: one cloud
apex, two singleton endpoints, and `r-2` internal cells.  Let block `i` have
population `m_i`.  For a sufficiently thin vertical composition, let
`W_i(z)` count its nonempty convex subsets and let `C_i(z),U_i(z)` count its
cap and cup endpoint chains.  Then the convex-subset enumerator is exactly

\[
 W(z)=1+\sum_i W_i(z)+
 \sum_{\substack{S\text{ convex macro support}\\|S|\ge2}}
 C_{\min S}(z)U_{\max S}(z)
 \prod_{h\in S\setminus\{\min S,\max S\}}m_hz.       \tag{8}
\]

For an upward-parabolic cell of population `m`,

\[
 W_i(z)=U_i(z)=(1+z)^m-1,qquad
 C_i(z)=mz+\binom m2z^2.                             \tag{9}
\]

The verifier evaluates (8) without enumerating supports.  It uses the exact
slope-root order of the macro configuration and weighted cap/cup path
matrices; traversing an internal block `j` multiplies a path by `m_j z`.
For every pair of endpoint blocks, the two path polynomials are multiplied by
the endpoint cap/cup polynomials.  This is an exact polynomial recurrence,
truncated only above rank `ell`, which `(PT)` never reads.

Two checks were kept separate:

1. Twenty-one modest cases were realized with explicit rational coordinates,
   cleared to integers, and their profiles were recomputed from exact
   orientation/slope orders.  They agree coefficient-by-coefficient with
   (8), and all have slack zero for every block.
2. The recurrence was then evaluated in the scalable regime `M=2^r` for
   `r=8,12,16,24,32,48,64`.  All blocks again have slack zero.  Every finite
   symbolic instance is realizable by choosing the two rational perturbation
   scales sufficiently small; the coordinate comparison guards the chamber
   convention used by the recurrence.

The largest exact symbolic computation reaches `ell=70`, vastly beyond the
small resonant examples, with no sign of growing slack.

## 4. What an actual counterfamily would have to do

The experiments sharply distinguish local coefficient failure from a failure
of `(PT)`.  A single terminal cliff can cost one doubling, but it does not
accumulate under the standard homogeneous products.  Long guarded pockets are
neutralized by their almost-convex background, while stationary product grids
obey `(PT)_(b,0)` even at enormous scale.

A scalable kill must therefore create **many separated prefix plateaus** in
one rank profile, with the anchored quantity `F_(ell-b)` failing to repay a
new deficit across many successive `b`-windows.  Repeating one fixed macro by
a stationary blow-up is not enough in the examples tested.  The remaining
adversarial direction is a deliberately nonstationary tower whose macro and
cell sizes change by level, with fresh rank depressions aligned at several
distinct distances below `ell`.  No such stretchable construction is known.

## Verification

Run

```bash
python3 phase2/loop/erdos838/agent_cyclic_stem_hw/block_search/verify_prefix_product_stress.py
```

from the repository root.  It prints `prefix-product stress: PASS` and writes
`prefix_product_stress_certificate.json`.  On the 2026-08-14 run it completed
in 15.98 seconds of wall time.  The script also passes `python3 -m py_compile`.
All profile coefficients, symbolic recurrences, coordinate comparisons, and
integral-slack tests are exact integers; only the displayed decimal values of
`s_R` use floating-point logarithms.

