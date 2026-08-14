# Second-wave mean-size / closure-lattice attack

**Date:** 2026-08-13
**Claim boundary:** one candidate inequality is disproved rigorously; the
mean-size criterion itself remains a conjecture.  All logarithms are base two.

For a planar point set `P`, this note includes the empty set and writes

\[
 V(P)=\#\{A\subseteq P:A\text{ is in convex position}\},\qquad
 \mu(P)=\frac1{V(P)}\sum_A|A|.
\]

Under `cl(A)=P\cap conv(A)`, the sets `A` above are the **independent sets**
`ext(K)` of the affine convex geometry, in bijection with its closed sets
`K`.  They are not the objects called *free convex sets* in the convex-
geometry literature.  Thus `mu` is the uniform average number of extreme
points of a closed set, equivalently the average down-degree of the closure
lattice.

## 1. Theorem: the quadratic mean-size inequality is false

The proposed intrinsic inequality

\[
 \log V(P)\le \left(\frac12+o(1)\right)\mu(P)^2 \tag{QMS}
\]

fails even for rationally realizable mirror-decomposable point sets.

### Counterfamily

Let `m` be even and let

\[
 Q_m=T_{m,m/2}
\]

be the balanced cell in the standard strong-glue Pascal construction.  It
has `n_m=binom(m,m/2)` points.  The exact cap/cup/convex recurrences are

\[
\begin{aligned}
 C(A\prec B)&=C(B)+(|B|+1)C(A),\\
 U(A\prec B)&=U(A)+(|A|+1)U(B),\\
 W(A\prec B)&=W(A)+W(B)+C(A)U(B),
\end{aligned} \tag{1}
\]

and differentiating their graded versions gives the exact first-moment
recurrences implemented in `mean_lattice_attack.py`.

The already-audited Pascal-cell asymptotic, which also follows from the
latest-diagonal lattice-path squeeze for `C`, is

\[
 \log V(Q_m)=
 \left(1-\frac1{4\ln2}\right)m^2+O(m\log m).       \tag{2}
\]

For completeness, the lower bound in (2) is not a cap/cup overcount: at the
top strong split,

\[
 C_{m-1,m/2-1}^2\le W(Q_m)\le C_{m,m/2}^2,
\]

and both ends have the coefficient in (2).

Every cap in `T_(m,i)` has size at most `i+1`, and every cup has size at most
`m-i+1`.  The upper and lower hull chains of a nonsingleton convex subset
share their two endpoints.  Therefore every convex subset of `Q_m` has at
most

\[
 (m/2+1)+(m/2+1)-2=m
\]

points.  In particular `mu(Q_m)<=m`.  Combining this with (2) gives

\[
 \liminf_{m\to\infty}
 \frac{\log V(Q_m)}{\mu(Q_m)^2/2}
 \ge 2-\frac1{2\ln2}
 =1.278652479555\ldots>1.                         \tag{3}
\]

This disproves (QMS), including any uniform interpretation restricted to
the regime `mu->infinity`.  It also locates the failure geometrically: a
single macroscopic Pascal cell has substantially more closed sets per unit
of squared average down-degree than an iterated balanced template.

The exact finite values move toward (3):

| `m` | `log n_m` | `mu-log n_m` | `log V/(mu^2/2)` |
|---:|---:|---:|---:|
| 32 | 29.162983 | +2.471097 | 1.099358869 |
| 64 | 60.668617 | +3.131716 | 1.164508359 |
| 128 | 124.171434 | +3.720874 | 1.210563063 |
| 192 | 187.879892 | +4.045645 | 1.229247127 |
| 256 | 251.672843 | +4.270040 | 1.239541146 |

These rows are exact integer evaluations; only the displayed divisions and
logarithms are floating point.

## 2. Theorem: a weaker minimizer dichotomy would still give `1/2`

Although universal QMS is false, the following strictly weaker target is
sufficient and is compatible with the counterfamily.

> **Low-mean minimizer dichotomy.**  For every configuration `P_n` attaining
> `f(n)`, either
> \[
> \mu(P_n)\ge(1-o(1))\log n,                       \tag{A}
> \]
> or
> \[
> \log V(P_n)\le(1/2+o(1))\mu(P_n)^2.             \tag{B}
> \]

Here the error need only be uniform along minimizers.  Equivalently, it is
enough to prove (B) only in the low-mean branch where (A) fails.

### Proof of sufficiency

Put `F_n=log f(n)` and `L=log n`.  The proved construction upper bound gives
`F_n<=(1/2+o(1))L^2`.  Hence either (A) or (B) implies

\[
 \mu(P_n)\ge(1-o(1))\sqrt{2F_n}.                  \tag{4}
\]

The exact deletion identity and averaging give

\[
 F_n-F_{n-1}
 \ge-\log\left(1-\frac{\mu(P_n)}n\right)
 \ge\frac{\mu(P_n)}{n\ln2}.                      \tag{5}
\]

Writing `G_n=sqrt(2F_n)` and using `G_n>=G_(n-1)`, equations (4)--(5) yield

\[
 G_n-G_{n-1}
 =\frac{2(F_n-F_{n-1})}{G_n+G_{n-1}}
 \ge\frac{F_n-F_{n-1}}{G_n}
 \ge\frac{1-o(1)}{n\ln2}.
\]

Summation gives `G_n>=(1-o(1))log n`, and therefore

\[
 \log f(n)\ge(1/2-o(1))(\log n)^2.
\]

The Pascal counterfamily lies safely in branch (A): the exact data above
have positive and growing `mu-log n`.  The useful replacement for QMS is
therefore not a larger universal constant; it is a theorem saying that any
low-mean *minimizer* must obey the sharp quadratic inequality.

## 3. Exact evidence on the surviving mean criterion

No tested family falsifies

\[
 \mu(P)\ge\log n-O(1).                             \tag{MS}
\]

This is evidence, not a theorem.

### Exhaustive strong-glue trees

Every distinct seven-coordinate state
`(n,C,U,W,C',U',W')` was enumerated through 13 leaves.  There are 207,986
states at `n=13`.  With the empty set included, the minimum observed deficits
are:

| `n` | 6 | 8 | 10 | 11 | 12 | 13 |
|---:|---:|---:|---:|---:|---:|---:|
| `min(mu-log n)` | -0.150180 | -0.148760 | -0.211634 | -0.236355 | -0.277412 | -0.286555 |

The deficit becomes more negative over part of this small range, so a proof
cannot use the zero-error inequality.  No unbounded trend is established.

### Reduced words and realizable rooted circuits

The exact Gate-A enumeration of all reflection-order commutation classes
through `n=7` is stronger than enumeration of realizable order types.  Its
mean minimizer has empty-inclusive deficit `-0.204615`.  The saved `n=7,8,9`
records replay exactly and have rational fixed-`x` realizations; their
deficits are respectively

```text
-0.204615, -0.219298, -0.143329.
```

The saved exact-integer heuristic certificates at `n=10,12,16,20` give

```text
-0.069469, +0.102705, +0.635987, +0.935383.
```

Only the replayed values are certified; optimality beyond the exhaustive
range is not claimed.

### Nested cages, Horton sets, and balanced cells

Eight exact rational nested-triangle samples were tested at each listed
depth.  The most negative deficits found were

| `n` | 6 | 9 | 12 | 18 | 24 | 30 | 36 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| deficit | -0.184963 | -0.122805 | -0.140907 | -0.025862 | +0.225082 | +0.570105 | +0.640116 |

The `n=6` row is the exact two-nested-triangle configuration with 44
nonempty convex subsets (45 closed sets).  Dyadic Horton sets move in the
opposite direction: the deficit rises from `+0.382857` at `n=8` to
`+5.824432` at `n=256`.  Balanced Pascal cells also have positive growing
deficit, as shown in Section 1.  Thus the standard strong blow-ups, Horton
recursion, and tested nested cages all survive (MS).

## 4. Closure-lattice identity and the remaining obstruction

For a closed set `K`, put

\[
 h(K)=|ext(K)|,\qquad i(K)=|K|-h(K).
\]

The Boolean intervals `[ext(K),K]` partition `2^P`, giving the exact identity

\[
 (1+t)^n=\sum_{K\text{ closed}}t^{h(K)}(1+t)^{i(K)}. \tag{6}
\]

At `t=1`, differentiation says that under the **interior-weighted** measure
`Pr(K) proportional to 2^{i(K)}`,

\[
 \mathbb E\,[h(K)+i(K)/2]=n/2.                    \tag{7}
\]

But (MS) concerns the uniform measure on closed sets.  Moving from (7) to
the uniform measure is the exact change-of-measure obstruction.  The Pascal
counterfamily shows that a sharp universal relation involving only
`log V` and the uniform first moment cannot have coefficient `1/2`.
Additional control of the interior statistic, or a minimizer-specific
negative correlation between `h` and `i`, is required.

## 5. Conjecture and recommended next target

**Conjecture (still live).**  Every realizable rank-three affine convex
geometry on `n` points has uniform average down-degree at least
`log n-O(1)`.  The weaker minimizer-only version is enough for Erdős 838.

The most targeted next statement is the low-mean dichotomy of Section 2,
expressed using (6): prove that a minimizer with unusually small uniform
`E[h]` cannot simultaneously have the interior-weight distribution needed
to violate sharp QMS.  This avoids the now-refuted universal QMS while using
exactly the extra lattice statistic that QMS discarded.

## 6. Reproduction

From the repository root:

```bash
python3 -m py_compile phase2/loop/erdos838/agent_mean_lattice/mean_lattice_attack.py
python3 phase2/loop/erdos838/agent_mean_lattice/mean_lattice_attack.py
```

The run takes about 13 seconds on the current machine and writes
`agent_mean_lattice/certificate.json`.  That certificate contains every
exact integer state for the displayed Pascal rows, all exhaustive minima,
the rational-family results, and each replayed reduced word.  It is about
176 KB; large integers are stored in full decimal form.
