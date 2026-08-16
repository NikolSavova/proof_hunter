# Pointwise deletion paths and normalized rank extension

**Date:** 2026-08-14  
**Verdict:** the pointwise asymptotic deletion-path statement survives every
planar test in this lane, including the balanced Pascal cells on which the
one-state activity gap tends to zero.  It is not proved.  The work does,
however, isolate a cleaner full-strength target,

\[
 p_r(P):={ (r+1)v_{r+1}(P)\over(n-r)v_r(P)}
 \geq 2^{-r-o(r)}\qquad(r\leq(1-o(1))\log_2n),       \tag{RE}
\]

and proves a sharp abstract barrier: the planar first-repair bound, the
complete 3-skeleton, and an Erdős--Szekeres-sized face in **every** member of
a deletion chain do not imply either the pointwise path bound or (RE).  A
genuine planar circuit-elimination/common-endpoint supersaturation theorem is
still necessary.

All logarithms in the deletion-path sections are natural.  The empty face is
included.

## 1. Exact pointwise target and the failed local shortcut

For a point set `S`, write

\[
 Z_S(t)=\sum_A t^{|A|},\qquad
 \mu_t(S)=tZ'_S(t)/Z_S(t),
\]

and, for `m=|S|`,

\[
 r(S)=\log{m-\mu_{1/2}(S)\over m-\mu_1(S)}.
\]

Along an arbitrary fixed deletion order
`S_n superset S_(n-1) superset ... superset S_1`, put

\[
 X(\pi)=\sum_{m=1}^n r(S_m).                       \tag{1}
\]

The asymptotic pointwise statement

\[
 X(\pi)\geq\log n-O(\log\log n)                    \tag{2}
\]

would close the half-weight attack.  The exact constant version with
`log(n/2)` is false on saved 24- and 30-point planar records, but only by
`0.0112` and `0.0933`, respectively.

Since

\[
 r(S)=\int_{1/2}^1 {\operatorname {Var}_t K\over m-\mu_t}\,d\log t,
\]

one always has

\[
 r(S)\geq {\mu_1(S)-\mu_{1/2}(S)\over m}.          \tag{3}
\]

This suggests the local endpoint-gap lemma
`mu_1-mu_(1/2)>=1-o(1)`.  It is false very strongly, even on one of the
central planar construction families.

### Exact central-Pascal obstruction

For the balanced Pascal cell `T_(m,m/2)`, the graded strong-glue recurrence
was evaluated at both activities, including derivatives.  The exact values
(rounded only for display) are

| `m` | number of points | `mu_1-mu_(1/2)` |
|---:|---:|---:|
| 20 | 184,756 | 0.395073 |
| 32 | 601,080,390 | 0.280059 |
| 64 | 1,832,624,140,942,590,534 | 0.168427 |
| 128 | `binom(128,64)` | 0.097518 |
| 256 | `binom(256,128)` | 0.054072 |

Thus the gap tends toward zero, not one.  Nevertheless explicit deletion
paths in the same family have `X=log n-O(1)` in the finite range.  Low-gap
balanced states are compensated by the unbalanced states forced after their
leaves are deleted.  Any successful proof of (2) must be genuinely
multiscale; a pointwise lower bound on (3) cannot work.

## 2. Planar path tests

`path_asymptotic_probe.py` evaluates `Z(t)` and its logarithmic derivative
from the exact slope reflection order.  It is polynomial in the number of
points and was checked against the independent exact subset replay of the
saved 24-point counterpath.

No tested realizable family has an asymptotically growing deficit
`log n-X`.  Representative worst paths are:

| family/path | `n` | `X/log n` | `X-log n` |
|---|---:|---:|---:|
| saved 24-point bad path | 24 | 0.7784 | -0.7044 |
| greedy saved 30-point record | 30 | 0.7746 | -0.7668 |
| greedy `T_(8,4)` | 70 | 0.8773 | -0.5212 |
| left-to-right `T_(10,3)` | 120 | 0.9316 | -0.3277 |
| greedy `T_(4,2)[T_(4,2)]`-type 8-by-8 cell | 64 | 0.8310 | -0.7028 |
| 30-point record blown up fourfold | 120 | 0.8522 | -0.7076 |

Further probes covered random permutation plots through `n=64`, random and
rotating nested triangles through `n=96`, and central Pascal cells through
`n=120`.  Several small examples violate `X>=log(n/2)`, but the observed
deficits remain constant-sized.  These are tests, not a proof of (2).

## 3. A cleaner full-strength coefficient target

Let

\[
 s_r={v_r\over\binom nr}
\]

be the probability that a uniform `r`-set is in convex position.  Then

\[
 p_r={s_{r+1}\over s_r}
 ={(r+1)v_{r+1}\over(n-r)v_r}                     \tag{4}
\]

is the mean fraction of points which extend a uniform convex `r`-face.
If (RE) holds uniformly through `k=(1-o(1))log_2 n`, then

\[
 s_k=\prod_{r<k}p_r\geq2^{-k^2/2-o(k^2)}.
\]

Consequently

\[
 \log_2v_k
 \geq k\log_2n-{k^2\over2}-o(k^2)
 =\left({1\over2}-o(1)\right)(\log_2n)^2,          \tag{5}
\]

which proves the missing lower coefficient directly.

In boundary notation

\[
 B_r=(n-r)v_r-(r+1)v_{r+1},
\]

(RE) is exactly

\[
 B_r\leq\bigl(2^{r+o(r)}-1\bigr)(r+1)v_{r+1}.     \tag{6}
\]

This is a particularly natural interface for the first-failure switch.  The
proved switch

\[
 (r-1)B_{r+1}\leq\sum_{|A|=r}b(A)u(A)
 \leq(r+1)B_{r+1}                                  \tag{7}
\]

is nearly regular whenever `u(A)>0`.  The only missing part of (6) is a
rank-preserving reset for the maximal faces `u(A)=0`.

### Exact construction-side evidence

Every saved planar profile satisfies (RE) with substantial slack.  More
significantly, the known sharp balanced constructions approach it from the
correct side.  The worst exponent

\[
 \max_{r\leq .95\log_2n}{-\log_2p_r\over r}
\]

in the exact scans is

| family | `log_2 n` | worst tested exponent |
|---|---:|---:|
| central Pascal `m=16` | 13.65 | 0.4920 |
| central Pascal `m=32` | 29.16 | 0.6314 |
| central Pascal `m=64` | 60.67 | 0.7347 |
| balanced vertical iterate `h=8,d=6` | 59.11 | 0.7203 |
| balanced vertical iterate `h=10,d=6` | 81.91 | 0.7696 |

For `m=64`, the worst row is `r=57` and already has
`log_2 p_r+r=15.12`.  The exponent moving upward toward one near the top
rank is consistent with sharpness of the final coefficient `1/2`; it never
crosses one in the exact range.

## 4. Abstract multiscale barrier

The following construction shows precisely what (7), a 4-flag rule, and a
rank threshold fail to capture.

Let `n=2^D`, order the ground set as `[n]`, and for every `4<=j<=D` choose a
`j`-set

\[
 H_j\subset(2^{j-2},2^{j-1}]
\]

near the right endpoint.  These blocks are pairwise disjoint.  Define a
simplicial complex `F_D` by

\[
 A\in F_D
 \quad\Longleftrightarrow\quad
 |A|\leq3\ \hbox{ or }\ A\subseteq H_j\text{ for some }j.       \tag{8}
\]

It has all of the following properties.

1. **4-flag:** every nonface contains a nonface of size four.
2. **Sharp repair bound:** if a nonface `S` has size at least five, at most
   one deletion `S-x` is a face.  Indeed, two repaired deletions would have a
   common set of at least three points lying in two disjoint blocks; if both
   lay in one block, `S` itself would be a face.
3. **Rank threshold in every suffix:** for `S_m=[m]`, choosing
   `j=ceil(log_2m)` leaves a complete `H_j` (or the preceding block at an
   exact dyadic endpoint), so
   
   \[
   \operatorname {rank}(F_D|S_m)\geq\lceil\log_2m\rceil.
   \]
4. **But bounded path activity:** apart from the complete 3-skeleton, the
   partition function contains only the disjoint Boolean corrections
   
   \[
   \sum_j\left((1+t)^{|H_j\cap[m]|}
       -\sum_{k=0}^3\binom{|H_j\cap[m]|}{k}t^k\right)=O(m).
   \]
   The 3-skeleton has partition function `Theta(m^3)`.  Hence
   `mu_1-mu_(1/2)=O(1/m)+O(log m/m^2)` and `r(S_m)=O(1/m^2)`, so
   
   \[
   X(\pi)=O(1).                                    \tag{9}
   \]

The exact finite values already stabilize:

| `n` | `X` | `X/log n` |
|---:|---:|---:|
| 256 | 2.07768 | 0.3747 |
| 1,024 | 2.08676 | 0.3011 |
| 4,096 | 2.08898 | 0.2511 |
| 16,384 | 2.08953 | 0.2153 |

The same example defeats (RE).  At full size and `r=floor(D/2)`, the
hockey-stick identity gives

\[
 v_r=\sum_{j=r}^D\binom jr=\binom{D+1}{r+1},
\]

and therefore

\[
 p_r={D-r\over r+2}{r+1\over n-r}=n^{-1+o(1)},    \tag{10}
\]

whereas `2^{-r}=n^{-1/2+o(1)}`.  Thus (RE) fails exponentially.

This does not refute the planar statement: (8) is not a rank-three planar
oriented-matroid free-set complex.  It proves that the planar input cannot be
compressed to Carathéodory rank, maximum face size, 4-flagness, or the
at-most-three-repairs theorem.

## 5. Best remaining attack

The rank-extension formulation is now the most economical target.  A proof
of the following tagged pocket-reset lemma would establish (6):

> For every boundary incidence `(A,p)` at rank `r`, route it through visible
> hull flips and recursive pockets to a convex `(r+1)`-face `C`, carrying the
> hidden subset of `A` as an `r`-bit tag, such that each tagged target has
> `2^{o(r)}` inverse histories.

There are only `2^r` hidden-subset tags, exactly the allowed loss in (6).
The first-repair theorem supplies only polynomial inverse multiplicity on
nonmaximal steps.  What remains is to show that a maximal-face pocket reset
can retain its tangent identity without acquiring an `n^c` label or being
reused at linearly many onion levels.

Equivalently, one needs a planar common-endpoint supersaturation theorem:
the abstract construction above has isolated Boolean facets, whereas planar
rooted-circuit elimination should force overlapping cap/cup endpoint
families which create the missing `(r+1)`-faces.  No valid telescoping scalar
potential was found.  In particular, the endpoint activity gap is ruled out
by the Pascal table in Section 1, and the hull-partition identity by itself
also holds in abstract convex geometries exhibiting rank-three barriers.

## 6. Verification

From the repository root:

```bash
python3 -m py_compile \
  phase2/loop/erdos838/agent_path_asymptotic/path_asymptotic_probe.py \
  phase2/loop/erdos838/agent_path_asymptotic/rank_extension_probe.py

python3 \
  phase2/loop/erdos838/agent_path_asymptotic/path_asymptotic_probe.py

python3 \
  phase2/loop/erdos838/agent_path_asymptotic/rank_extension_probe.py
```

The saved planar profiles and Pascal/vertical recurrences use exact integer
coefficients.  The reflection-order path evaluator uses exact rational slope
orders and floating arithmetic only for the two scalar matrix products and
displayed logarithms.  The abstract profiles use exact binomial counts.
