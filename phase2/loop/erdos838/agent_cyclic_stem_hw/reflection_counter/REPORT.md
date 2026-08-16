# Unit reflection orders: repeatable-gadget countersearch

**Date:** 2026-08-14  
**Verdict:** no repeatable counterfamily to the asymptotic half-weight target

\[
H(R)=\frac{nF_R(1/2)}{F_R(1)}=n^{o(1)}
\]

was found.  The search did improve the finite unit-reflection-order record to
`H=2.002978494...`, so the already-false constant-two strengthening remains
false even after imposing complete, unit, once-per-root factorization.  This
is **not** a counterexample to `H=n^{o(1)}`.  Every stationary block gadget
tested self-heals, and the most adversarial repeatable doubling found has the
exact asymptotic law `H=Theta(1/n)`.

## 1. Exact model and verification boundary

A state is a reduced word for the longest permutation `w0 in S_n`.  Its root
sequence contains every positive root `(i,j)`, `i<j`, exactly once.  Every
root carries the unit factor

\[
T_{ij}(z)=I+zE_{j,i}.
\]

With forward and reverse row-update products `B_R(z),A_R(z)`, the
empty-inclusive path-pair polynomial is

\[
F_R(z)=1+nz+\langle A_R(z),B_R(z)\rangle_F-n.       \tag{1}
\]

The verifier reconstructs the sorting network, rejects any backward crossing,
checks the complete root set, and evaluates (1) at `1` and `1/2` with integers
and a common power-of-two denominator.  For the main 58-wire record it also
recomputes the entire graded polynomial independently.

Thus none of the weighted, incomplete-support, or bare inverse-pair
counterexamples from `agent_inverse_pair_hw` enter this report.

## 2. Finite record: above two, but only finitely

Braid annealing from the known 58-point planar record produced a reflection
order with exact profile

```text
(1,58,1653,30856,220920,428423,284024,76618,14864,2059,192).
```

It has

\[
F(1)=1059668,\qquad F(1/2)=\frac{18736483}{512},
\]

and hence

\[
\boxed{H=\frac{543358007}{271275008}
      =2.002978494060168\ldots}.                         \tag{2}
\]

The saved reduced word has length `binom(58,2)=1653`; exact replay confirms
all 1653 distinct positive roots and unit weights.  This slightly improves
the planar constant-two counterexample `2.000767...`.  Stretchability was not
preserved by the braid search, so (2) is claimed only for the full reflection-
order/pseudoline class.  Most importantly, (2) says nothing adverse about an
`n^{o(1)}` envelope.

## 3. Fixed block cablings all self-heal

The constructor inflates each macro wire by a copy of an inner sorting
network.  It tests:

* internal crossings before or after the macro crossings;
* row and column linear extensions of every rectangular cross-block grid;
* periodic schedules `0,1,01,001,011`;
* macro record words of sizes `2,...,7`;
* independent `id/reverse/mirror/reverse-mirror` states in the inner blocks.

The basic periodic catalog has `6*5*5=150` exact families, through at most 128
wires.  Every family has `H<1` at its terminal tested depth.  Homogeneous
representatives are:

| macro size | sizes tested | `H` at depth one | terminal `H` |
|---:|---:|---:|---:|
| 2 | `2,4,8,16,32,64` | `1.125000` | `0.313251` |
| 3 | `3,9,27,81` | `1.265625` | `0.300093` |
| 4 | `4,16,64` | `1.333333` | `0.572928` |
| 5 | `5,25,125` | `1.354167` | `0.299434` |
| 6 | `6,36` | `1.391667` | `0.948779` |
| 7 | `7,49` | `1.408390` | `0.904322` |

An exhaustive depth-two internal-symmetry scan for macro sizes 3, 4, 5
evaluated `256+1024+4096=5376` further cabled words.  Symmetry heterogeneity
does create larger finite bumps, but repeating each winner again kills them:

```text
r=3: 1.265625, 1.150359, 0.920911, 0.711815
r=4: 1.333333, 1.174267, 0.765744
r=5: 1.354167, 1.091915, 0.505709
```

These experiments are not a theorem for arbitrary nonstationary Coxeter
substitution.  They do rule out the simplest stationary row/column gadgets,
including short periodic changes of phase and orientation.

## 4. The strongest repeatable seed has exact `Theta(1/n)` decay

The least destructive repeatable operation was **strand doubling**: replace
every old wire by two adjacent wires, cross the internal pair first, and
replace each old crossing by the row sweep of its `2 by 2` crossing grid.
Apply it to the record (2).

For any seed with empty-inclusive profile

\[
Z(t)=\sum_kv_kt^k,\qquad |R|=n,
\]

the doubled word is again a unit complete reflection order and its profile is
given exactly by

\[
\boxed{
Z^+(t)=1+n(2t+t^2)
 +(1+t+t^2/4)\bigl(Z(2t)-1-2nt\bigr).}              \tag{3}
\]

Equivalently, each old rank-`j` term with `j>=2` contributes

\[
v_j\left(2^jt^j+2^jt^{j+1}+2^{j-2}t^{j+2}\right),  \tag{4}
\]

and `n` within-pair edges contribute `nt^2`.  The verifier checks (3)
coefficient by coefficient against a literal 116-wire transvection product.

The first values are

| depth | `N` | exact/decimal `H` | `2^r p_r`, `r=floor(log2 N)` |
|---:|---:|---:|---:|
| 0 | 58 | `2.0029784941` | `2.40164` |
| 1 | 116 | `1.6890349506` | `3.90387` |
| 2 | 232 | `0.9889666094` | `6.68730` |
| 3 | 464 | `0.3799088640` | `11.6396` |
| 5 | 1856 | `0.0514208752` | `36.2614` |
| 10 | 59392 | `0.0013866111` | `444.437` |

So the normalized graded-extension inequality also gains, rather than loses,
slack under this repeatable gadget.

There is an exact asymptotic evaluation.  Put

\[
R_d(t)=Z_d(t)-1-N_dt,quad N_d=n_0 2^d,quad
a(t)=(1+t/2)^2.
\]

Equation (3) gives

\[
R_{d+1}(t)=N_dt^2+a(t)R_d(2t).                     \tag{5}
\]

If `h=deg Z_0`, iteration of (5) shows, for fixed `t>0`,

\[
R_d(t)\sim v_h P_d(t)(2^dt)^h,qquad
P_d(t)=\prod_{j=0}^{d-1}a(2^jt).                    \tag{6}
\]

The positive within-pair sum in the iterated recurrence is lower order than
the descendants of the seed's top-rank term.  Moreover the product ratio
telescopes:

\[
\frac{P_d(1/2)}{P_d(1)}
=\left(\frac{5/4}{1+2^{d-2}}\right)^2
\sim25\,2^{-2d}.                                    \tag{7}
\]

Combining (6)--(7) yields the general law

\[
H(R_d)\sim \frac{25n_0^2}{2^h}\frac1{N_d}.          \tag{8}
\]

For (2), `n_0=58` and `h=10`, so

\[
\boxed{N_dH(R_d)\longrightarrow
       \frac{25\cdot58^2}{2^{10}}=\frac{21025}{256}.} \tag{9}
\]

This is stronger than merely failing to amplify: the finite `H>2` seed
becomes polynomially harmless at the exact rate `1/N`.

## 5. Nested one-wire lifts: a finite upward plateau, not a gadget theorem

As a different scalability test, a new largest wire was inserted while
preserving the old root order exactly.  All legal interleavings were scored.
Starting from the exact 8-wire minimum:

| `n` | legal lifts scored | exact best `H` |
|---:|---:|---:|
| 8 | seed | `325/228 = 1.425439...` |
| 9 | `1,108,776` | `3951/2720 = 1.452574...` |
| 10 | `51,336,671` | `5875/4032 = 1.457093...` |

The `n=9` value is still below the unrelated planar record `7875/5408`, and
the exponent `log_n H` falls from about `0.170` at `n=9` to `0.163` at
`n=10`.  These nested lifts show that monotone finite growth is possible, but
they do not expose a repeatable schedule or evidence for `H>=n^epsilon`.

## 6. Bottom line

* The finite bound `H<=2` is false in the exact unit reflection-order class;
  (2) is a slightly stronger finite record.
* No counterexample to the asymptotic target `H=n^{o(1)}` was found.
* All `150+5376` stationary/short-period block gadgets tested self-heal.
* The strongest repeatable doubling has the proved exact scaling
  `H~(21025/256)/N`, and its relevant normalized graded ratios acquire rapidly
  increasing slack.
* A genuine counterfamily must therefore use growing or nonstationary state,
  not a fixed row/column cable, a fixed orientation cycle, or repetition of
  the present finite `H>2` core.

## 7. Reproduction

From the repository root:

```bash
python3 phase2/loop/erdos838/agent_cyclic_stem_hw/reflection_counter/verify_reflection_counter.py

# Slow optional replay of all 150 periodic cabled families:
python3 phase2/loop/erdos838/agent_cyclic_stem_hw/reflection_counter/verify_reflection_counter.py \
  --full-catalog

c++ -O3 -std=c++17 \
  phase2/loop/erdos838/agent_cyclic_stem_hw/reflection_counter/reflection_insertion_search.cpp \
  -o /tmp/reflection_insertion_search
```

The default verifier takes about six seconds on the development machine.  It
uses no floating-point assertion.
