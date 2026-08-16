# Weighted normalized Kraft is false on a stretchable five-point chart

**Date:** 2026-08-16. All logarithms are base two.

## Verdict

The most natural attempt to remove the harmonic loss from
`HETEROGENEOUS_THRESHOLD_SQUARE_MESH_GATE_20260816.md` is false, even for
a generic integral planar chart.

Give macro position $i$ child size $n_i>1$, and put

\[
 \ell_i=\log n_i,
\]

and let $R_i=A_i+B_i$ be its exact weighted cap-plus-cup endpoint reward,
where a path using sibling $j$ earns \(\log(1+n_j)\). The proposed
weighted Kraft inequality was

\[
                 \sum_i 2^{-R_i/\ell_i}\le 1.              \tag{1}
\]

It agrees with the proved hinged Kraft theorem when all child sizes are
equal, and it survived broad random testing. Nevertheless (1) is false.
For the five points

~~~text
(0,  0), (1, 10), (2, 15), (3, 21), (4, 50)
~~~

the increasing slope order is

~~~text
12 13 23 03 02 01 04 14 24 34.
~~~

This is a reduced reflection order. With child sizes

\[
                         (256,16,16,16,256),             \tag{2}
\]

put $c=\log257$ and $d=\log17$. Exact tropical execution gives

\[
 (R_0,R_1,R_2,R_3,R_4)=(2d,2c,2c,c+2d,3d).             \tag{3}
\]

Consequently the left side of (1) is

\[
 17^{-1/4}+2\,257^{-1/2}+74273^{-1/4}+17^{-3/8}
 >1.0232.                                                \tag{4}
\]

The strict lower bound in (4) is certified using only integer powers; no
floating-point comparison is needed.

This kills only the normalized Kraft shortcut. The exact square-mesh
conjecture

\[
 \max_i\left\{{\ell_i^2\over2}+R_i\right\}
 \ge {1\over2}\left(\log\sum_i n_i\right)^2
       -{1\over2}(\log5)^2                              \tag{5}
\]

has margin greater than five bits on the same example. The proved harmonic
version also remains valid. Thus (1) is strictly stronger than the local
Bellman statement actually wanted.

## 1. Exact geometry

The ten slopes are

\[
 5,{11\over2},6,7,{15\over2},10,{25\over2},{40\over3},
 {35\over2},29,
\]

in the displayed root order. Processing those crossings from the initial
permutation (01234) swaps adjacent entries at positions

\[
                         1,2,1,0,1,2,3,2,1,0,            \tag{6}
\]

and ends at (43210). Hence the example is not merely an arbitrary edge
ordering: it is stretchable and belongs to the geometric scope of the
heterogeneous recursion.

All triple determinants are nonzero. The verifier checks the root order,
the adjacent-swap word, the final reversal, and the determinant margin
directly from the integer coordinates.

## 2. Symbolic weighted recurrence

Represent a reward by a pair $(a,b)$, meaning $ac+bd$. Since

\[
                         17^2=289>257,                  \tag{7}
\]

we have (2d>c>d); this resolves every nontrivial maximum in the
recurrence exactly. Starting all cap and cup rewards at zero and applying

\[
 A_i\leftarrow\max(A_i,A_j+w_j),\qquad
 B_j\leftarrow\max(B_j,B_i+w_i)                         \tag{8}
\]

at the ten roots gives (3).

For completeness, the four terms in (4) have the exact rational lower
bounds

\[
 17^{-1/4}>{4924\over10000},\quad
 {2\over\sqrt{257}}>{1247\over10000},\quad
 74273^{-1/4}>{605\over10000},\quad
 17^{-3/8}>{3456\over10000}.                            \tag{9}
\]

Their sum is (10232/10000). Each inequality in (9) is checked after
raising to the fourth, second, fourth, or eighth power respectively.

There is also a scalable explanation. Replacing (2) by

\[
                         (2^{2t},2^t,2^t,2^t,2^{2t})
\]

makes the normalized rewards tend to

\[
                         (1,4,4,4,3/2).
\]

The Kraft sum therefore tends to

\[
 {1\over2}+{3\over16}+2^{-3/2}
 = {11\over16}+{1\over2\sqrt2}>1.                     \tag{10}
\]

The failure is structural rather than a small-size logarithmic artefact.

## 3. Consequence for the proof campaign

The thresholded hinged proof remains the safe local theorem. Any removal
of its harmonic factor must use more than a code length obtained by
dividing the endpoint reward by the anchor scale. In particular, the
following tempting chain is invalid:

1. prove (1) by a continuous or unequal-letter Kraft code;
2. optimize the resulting code lengths by convexity; and
3. infer the zero-harmonic square mesh.

The counterexample stops that route at step 1. It does not affect the
fixed-size supersaturation program or the selected-family
circuit/profile route, which remain the substantive global bottlenecks.

## 4. Verification

Run

~~~text
python3 phase2/loop/erdos838/verify_weighted_normalized_kraft_barrier.py
~~~

The verifier checks the integer order type, exact slope order, reduced
word, symbolic endpoint recurrence, the four integer-power certificates
in (9), the strict violation (4), and a rigorous rational-log lower bound
of five bits for the square-mesh margin.
