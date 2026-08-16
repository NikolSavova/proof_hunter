# Complete guard layers force a convex union carrier

**Date:** 2026-08-14.  All logarithms are base two and the empty convex
subset is counted.

## Verdict

Planar four-circuit locality breaks the apparent zero-surplus obstruction for
complete guard layers, and for a precise near-complete range.  It is enough
that the guards cover every four-label trace of their `s`-label core.  Then
the carrier together with the **entire** core is convex, so the ordinary-face
bank is the full `2^s` cube, not the truncated Kruskal--Katona shadow
`sum_(i<g)binom(s,i)`.  In particular this holds for every complete layer and,
for core rank `r=g-1`, whenever

\[
 |\mathcal F|>{s\choose r}-{s-4\choose r-4}.                \tag{0}
\]

These full cubes admit a global recoverable-cell telescope.  Let `b` bound
carrier rank, let `q` bound the rank of a union-bank output, and define

\[
 L_U=3{q\choose3}\sum_{i=0}^{b-2}{q-3\choose i},qquad
 L_C=n{b+1\choose2}.                                       \tag{1}
\]

For four-trace-covering cells `c`, with core size `s_c`, guard rank
`g_c=r_c+1`, source multiplicity

\[
 k_c=|\mathcal F_c|;\qquad
 k_c={s_c\choose r_c}\quad\hbox{in the complete case},      \tag{2}
\]

and singleton alphabet size `m_c`, one has

\[
 \boxed{
  \sum_ck_c
  \le
  \sqrt{L_UL_C\,
    \max_c{k_c^2\over m_c2^{s_c}}}\;V(P).}                 \tag{3}
\]

No copy of `V` is spent per core or per root.

On the live slice `b=O(log n)`, `r=Theta(log n)`, and
`m>=n/polylog(n)`, equation (3) gives a fixed-power gain whenever

\[
 s-2r\log(es/r)
   -O\!\left(b\log{e(s+b)\over b}\right)
       \ge\eta\log n.                                      \tag{4}
\]

In particular, every complete core with `s/log n -> infinity` satisfies
(4).  Thus the hard complete or sufficiently near-complete bin is forced
down to `s=O(log n)`, where each fibre has only `n^O(1)` occurrences.

What remains is a prevalence/stability problem: a high but incomplete guard
layer need not contain a large complete sublayer, and quadratically many
`O(log n)` cores may still carry the global mass.  No rank-`O(log n)`,
`Theta(V)` planar regression realizing that final arrangement is constructed
here.  The theorem closes the complete and four-trace-covering obstruction,
not EIC'.

## 1. Rooted guard cells and four-trace coverage

A rooted cell is specified by

* a marked root `T`, deleted label `z in T`, and retained edge
  `e=T setminus {z}`;
* a carrier `B` of size at most `b`, containing `e`, excluding `z`, and
  disjoint from the actual role-pocket `X_T`;
* a core `U`, disjoint from `B union {z}`, of size `s`;
* an integer `r>=4`;
* a uniform family `mathcal F subseteq {U choose r}` and every source

\[
                         A_R=B\cup\{z\}\cup R,qquad
                         R\in\mathcal F,                    \tag{5}
\]

  is a convex marked source with canonical root `T`;
* a canonical alphabet `X subseteq X_T`, `|X|=m`, for which

\[
                              B\cup\{x\}                     \tag{6}
\]

  is convex for every `x in X`.

The cell is determined by `(T,z,B)`; its `U,r,mathcal F,X` are canonical
data.  Its weighted occurrence count is `k=|mathcal F|`.  Call it
**four-trace-covering** if every `E in {U choose 4}` is contained in some
`R in mathcal F`.  A complete layer `mathcal F={U choose r}` is
four-trace-covering.

## 2. Planar union lift

> **Lemma 1 (four-trace cover implies convex union).**  Under (5) with
> `r>=4`, if `mathcal F` is four-trace-covering, then
>
> \[
>                              Q=B\cup\{z\}\cup U            \tag{7}
> \]
>
> is convex.

**Proof.**  If `Q` were nonconvex, planar Caratheodory would give a bad
four-subset `W subseteq Q`.  Extend its trace `W cap U` to a four-subset
`E subseteq U` (when necessary), and choose `R in mathcal F` containing
`E`.  Then

\[
                              W\subseteq A_R,                 \tag{8}
\]

contradicting convexity of the source in (5).  QED.

This is the geometric information absent from a bare set-system shadow.  It
uses the fact that every failure of convex position has a four-label witness.
For abstract closure systems of unbounded circuit rank, the statement is
false.

> **Corollary 1a (explicit high-density threshold).**  The conclusion of
> Lemma 1 holds whenever (0) holds.

**Proof.**  If a fixed four-set `E` is uncovered, every member of
`mathcal F` belongs to `{R in {U choose r}:E not subseteq R}`, a family of
size exactly

\[
                    {s\choose r}-{s-4\choose r-4}.          \tag{9a}
\]

Thus (0) forces every four-set to be covered.  QED.

The threshold is deliberately strict and is the exact elementary density
threshold: a layer consisting of all `r`-sets avoiding one fixed four-set
has equality in (9a).  Geometry may still make its union convex, but layer
density alone cannot prove this.  In normalized form the sufficient density
is

\[
 { |\mathcal F|\over {s\choose r}}
   >1-{(r)_4\over(s)_4};                                  \tag{9b}
\]

for `r/s -> rho` this is `1-rho^4+o(1)`.

Consequently every

\[
                         B\cup\{z\}\cup D,qquad D\subseteq U
                                                               \tag{9}
\]

is an ordinary face.  These `2^s` outputs form the **union bank**.  The
completion bank consists of the `m` faces (6).

## 3. Exact global decoders

Let `q` bound the rank of outputs in (9); one may take
`q<=b+1+max s_c`, or the smaller actual rank bound.

> **Lemma 2 (union-bank decoder).**  A face lies in at most `L_U` union
> banks.

**Proof.**  An output in (9) contains the full root.  Guess `T` inside it and
`z in T`, costing `3 binom(q,3)`.  The carrier contains the retained edge.
Guess the remaining at most `b-2` carrier labels from outside `T`, then put

\[
                         B=e\cup B',qquad
                         D=C\setminus(B\cup\{z\}).           \tag{10}
\]

The tuple `(T,z,B)` determines the cell and hence `U`; validity requires
`D subseteq U`.  This proves (1).  QED.

> **Lemma 3 (completion decoder).**  A face lies in at most `L_C` completion
> banks.

**Proof.**  Guess the retained edge inside a rank-`b+1` completion output and
the missing root label among all `n` labels.  This determines `T`.  Since
`B cap X_T=emptyset`, a valid guess has

\[
                    \{x\}=C\cap X_T,qquad B=C\setminus\{x\}.
                                                               \tag{11}
\]

The cell is forced.  QED.

The decoders charge every root and every carrier.  The number of complete
cores does not appear separately.

## 4. Global Cauchy telescope

> **Theorem 4 (four-trace union telescope).**  Equation (3) holds.

**Proof.**  The two bank sizes in a cell are exactly

\[
                         |\mathcal U_c|=2^{s_c},qquad
                         |\mathcal C_c|=m_c.                 \tag{12}
\]

Put

\[
                         K=\max_c{k_c^2\over m_c2^{s_c}}.    \tag{13}
\]

Then `k_c^2<=K|mathcal U_c||mathcal C_c|`.  Sum square roots,
apply Cauchy, and use Lemmas 2--3:

\[
\begin{aligned}
 \sum_ck_c
 &\le\sqrt K\sum_c\sqrt{|\mathcal U_c||\mathcal C_c|}\\
 &\le\sqrt{K
       \left(\sum_c|\mathcal U_c|\right)
       \left(\sum_c|\mathcal C_c|\right)}\\
 &\le\sqrt{K L_UL_C}\,V(P).
\end{aligned}                                               \tag{14}
\]

This proves (3).  QED.

## 5. Exponent audit

Put `L=log n`, let `b=C_bL+O(1)`, `r=gamma L+O(1)`, and
`m>=n/L^a`.  Since a union output has rank at most `q=s+b+1`,

\[
 \log L_U
 \le O(\log q)+b\log{e(s+b)\over b},
 \qquad
 \log L_C=L+O(\log L).                                     \tag{15}
\]

Also

\[
                         \log k\le r\log(es/r).             \tag{16}
\]

The `log m=L-O(log L)` term cancels the missing-root term in `L_C`.
Substitution into (3) gives (4).

If `s/L -> infinity`, the positive term `s` dominates both
`L log(s/L)` losses, proving a super-fixed-power gain.  Hence any complete
cell surviving the telescope has `s=O(L)`.  This is substantially stronger
than the set-system KK gate, which has essentially zero surplus when
`r<s/2`.

### Comparison with the `(3k)`--`(3m)` gate

For a complete layer, the old shadow denominator is

\[
             \Phi_r(k)=\sum_{i=0}^r{s\choose i},
             \qquad k={s\choose r}.                        \tag{17}
\]

The squared factor multiplying `V` in `(3l)` is changed by the exact ratio

\[
 {L_U\over L_S}\,
 {\sum_{i=0}^r{s\choose i}\over2^s}.                       \tag{18}
\]

Thus the planar lift really does replace the zero-KK denominator by the full
cube, while paying the explicit union-output decoder `L_U` in place of
`L_S`; no fibre count is hidden.  It closes all superlogarithmic complete
cores by (4), but it does **not** close every logarithmic complete core.  For
example, at `r=s/2=Theta(L)`,
`k^2/2^s=2^{s-o(s)}`, so the local square demand itself can consume the full
cube before decoder loss.  This central logarithmic bin remains part of the
prevalence problem.

## 6. Exact sharpness at linear cores

The oval construction from `HEAVY_PROFILE_FIRST_DIVERGENCE.md` is the sharp
linear-core model.  Put `s` guard labels on one outer arc, take every
`r`-subset as a guard, and put the common pocket behind the deleted root.
Then (7) is visibly a convex outer face, the union bank has exact size `2^s`,
and all `binom(s,r)m` completion records still collapse to the same `m`
completion faces.

For `s,r=Theta(L)`, every source and every union output has rank `O(L)` and
the local square constant in (13) can be order one or larger, depending on
the entropy constants.  Repeating polynomially many such cells is compatible
with the theorem.  Making them carry `Theta(V)=2^Theta(L^2)` mass while
respecting the global decoders is the unresolved final prevalence problem.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_complete_guard_union_lift.py
```

The exact rational checker constructs two recoverable complete cells with
`s=6`, `r=4`, `m=4`.  It verifies all fifteen marked sources in each cell,
the four-circuit union lift, all sixty-four union faces, the collapsed
completion bank, and both global decoders.  The local square constant is
`225/256`, and both the local comparison and global Cauchy step are
equalities.  It separately deletes one member of the complete fifth layer,
checks that the remaining five guards still cover every four-trace, and
audits the strict density threshold.
