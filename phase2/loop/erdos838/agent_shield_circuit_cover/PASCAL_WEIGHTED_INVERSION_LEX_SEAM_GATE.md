# A lexicographic seam breaks the Pascal weighted anti-alignment

**Date:** 2026-08-15. All logarithms are base two. This continues
`PASCAL_STRONG_GLUE_PROJECTION_SPECTRUM_GATE.md`.

## Verdict

The diffuse weighted-inversion residue is not intrinsic to the abstract
opposite-density Pascal strong glue. There is an explicit rational
realization of the same binary strong-glue construction with a diagonal
projection satisfying

\[
 \boxed{
 \sup_\theta {C_\theta(P_t)U_\theta(P_t)\over V(P_t)}
 \ge N_t^{1.6689662610\ldots-o(1)}.
 }                                                       \tag{1}
\]

In particular, this realization exceeds $N^{\log_2 3+\varepsilon}$ for
some fixed $\varepsilon>0$. The proof uses ordinary one-face cap and cup
banks, not the retracted arbitrary-child cyclic profile splice.

The result is deliberately gauge-specific. It does **not** prove that every
realization of the same strong-glue order type has the lexicographic seam
chamber. Disjoint cross-wall events can be commuted as the realization
changes. Therefore (1) closes the Pascal regression whenever the outer
pockets may be horizontally thinned before gluing, but it does not yet
close the fixed-gauge weighted synchronization theorem. A scalable
anti-aligned counterexample must now use that cross-wall gauge freedom; the
Pascal cap recurrence itself does not provide the obstruction.

## 1. The rational lex-seam realization

Let $t$ be a multiple of $80$, and put

\[
 x={1\over4},\qquad \eta={11\over20},\qquad
 s=\eta t,\qquad i={3s\over4},\qquad j={t\over4}.       \tag{2}
\]

Take rational realizations

\[
                   A=T(s,i),\qquad B=T(t,j)             \tag{3}
\]

normalized vertically into $[0,1]$. Their recursive strong-glue words are
binary: prefix $1$ is the earlier/lower child and prefix $0$ the
later/upper child. Horizontally compress both configurations by a rational
$\delta_t>0$, and set

\[
 A' =\{(\delta_t x,y):(x,y)\in A\},\qquad
 B' =\{(1+\delta_t x,2+y):(x,y)\in B\}.                \tag{4}
\]

For sufficiently small positive $\delta_t$, (4) is a genuine strong glue:
within-block slopes are arbitrarily large, while every cross slope stays
between fixed positive constants. Thus

\[
                              P_t=A'\prec B'.           \tag{5}
\]

In the construction chart, (5) has exactly the face and endpoint
recurrences used in `RANK_SAFE_ENDPOINT_SURPLUS_GATE.md`.

Now project by

\[
                              f(x,y)=x-y/2.             \tag{6}
\]

The two macro constants cancel. After choosing $\delta_t$ below the least
relevant vertical prefix gap, the order in each child is reversed and the
cross comparisons used below agree with reverse binary lexicographic order
$0<1$. An arbitrarily small rational perturbation makes the whole
projection generic without changing any of the strict prefix comparisons.

This is an explicit finite construction for every $t$; no limiting or
nonstretchable order type is used.

## 2. Two ordinary directional banks

Write $z=s-i=11t/80$ for the number of zeroes in an $A$-word.

First define

\[
 G_A=\{a\in A:a\text{ begins with }1^{j+1}\}.          \tag{7}
\]

Every $B$-word has only $j$ ones. Hence every member of $G_A$ follows every
$B$-label in the reverse lexicographic chamber. A natural cup of $B$
becomes a cap when the child order is reversed, and adding one label of
$G_A$ outside its endpoint interval preserves the cap sign. Therefore

\[
                 C_\theta(P_t)\ge |G_A|\,U(B),
 \qquad
 |G_A|={s-j-1\choose i-j-1}.                           \tag{8}
\]

For the opposite bank, let $A_0$ be the prefix-$0$ child of $A$:

\[
                              A_0=T(s-1,i).             \tag{9}
\]

Define two $B$-guard pools

\[
 \begin{aligned}
 G_B^-&=\{b\in B:b\text{ begins with }0^{z+1}\},\\
 G_B^+&=\{b\in B:b\text{ begins with }1\}.
 \end{aligned}                                         \tag{10}
\]

No $A$-word has more than $z$ zeroes, so every $G_B^-$ label precedes every
$A$-label. Every $A_0$ word begins with $0$, so every $G_B^+$ label follows
every $A_0$ label. A natural cap of $A_0$ becomes a cup under reversal, and
one guard from each side preserves every cup triple. Hence

\[
 U_\theta(P_t)\ge |G_B^-|\,|G_B^+|\,C(s-1,i),          \tag{11}
\]

where

\[
 |G_B^-|={t-z-1\choose j},\qquad
 |G_B^+|={t-1\choose j-1}.                             \tag{12}
\]

Equations (8) and (11) are injective ordinary chain banks. Their sign check
is also the special case of Theorem 1 in the preceding report: the cap uses
one $A$ label outside a $B$ interval, and the cup uses a $B$ pair
straddling the entire $A_0$ trace.

## 3. A sharp-enough first-order cap ratio

The only nontrivial loss in (11) is $C(s-1,i)/C(s,i)$. The usual
$O(d\log d)$ Pascal asymptotic is too coarse for this polynomial question,
so we need the following first-order lemma.

Let

\[
 D(d,k)=\prod_{h=0}^{k-1}
        \left(1+{d-1-h\choose k-h}\right).             \tag{13}
\]

This is the contribution obtained by always taking the weighted left term
in

\[
 C(d,k)=C(d-1,k)+\left(1+{d-1\choose k}\right)C(d-1,k-1).
                                                               \tag{14}
\]

> **Lemma 1 (dominant Pascal path).** For every fixed
> $y\in(0,1)$ and $k=yd+O(1)$,
> 
> \[
>             \log C(d,k)=\log D(d,k)+o(d),            \tag{15}
> \]
> 
> and consequently
> 
> \[
> \log {C(d-1,k)\over C(d,k)}
>   =-K(y)d+o(d),\qquad
> K(y)={-\ln(1-y)-y\over\ln2}.                         \tag{16}
> \]

**Proof.** Expand (14) over lattice paths. Index the weighted left steps by
the number $r_h$ of unweighted right delays preceding them. The sequence
$(r_h)$ is a partition inside a $k\times(d-k)$ rectangle. The all-left path
has $r_h=0$ and weight (13). Binomial comparison gives, while at least $m$
left steps remain,

\[
 {1+{n-r-1\choose q}\over1+{n-1\choose q}}
 \le \exp\left(-c_y{rq\over d}\right)                 \tag{17}
\]

for an absolute $c_y>0$ depending only on a compact neighborhood of $y$.
Take $m=\lceil\sqrt d\rceil$. Summing (17) over delay partitions uses the
elementary Euler bound

\[
 \sum_\lambda e^{-c_y m|\lambda|/d}
   =\prod_{q\ge1}(1-e^{-c_y mq/d})^{-1}
   =\exp(O(\sqrt d)).                                  \tag{18}
\]

The final $m$ weighted steps and all possible terminal delays contribute at
most $(d+1)^{O(m)}=2^{O(\sqrt d\log d)}$. Thus

\[
       D(d,k)\le C(d,k)
       \le D(d,k)2^{O(\sqrt d\log d)},                 \tag{19}
\]

which proves (15). For $z=d-k$, cancellation in (13) gives

\[
 \log {D(d-1,k)\over D(d,k)}
  =\sum_{q=1}^k\log {z-1\over z+q-1}+o(d).
                                                               \tag{20}
\]

The Riemann sum in (20) is

\[
 d\int_0^y\log_2{1-y\over1-y+u}\,du
 =-K(y)d,
\]

and (16) follows from (15). $\square$

The estimate is intentionally only $o(d)$; that is exactly the precision
needed for a fixed power of $N$.

## 4. Exponent calculation

The strong-glue cross term dominates the two child complexes quadratically:

\[
                         V(P_t)=(1+o(1))C(A)U(B).       \tag{21}
\]

Indeed its quadratic coefficient is $0.5457170\ldots$, while that of
$V(B)$ is $0.5407728\ldots$ and that of $V(A)$ is smaller still.

Combining (8), (11), and (21),

\[
 \log {C_\theta(P_t)U_\theta(P_t)\over V(P_t)}
 \ge \log|G_A|+\log|G_B^-|+\log|G_B^+|
      +\log{C(s-1,i)\over C(s,i)}-o(t).                \tag{22}
\]

Put $H=H_2(1/4)=0.8112781244\ldots$. Stirling and Lemma 1 give the
coefficient of $t$ in (22) as

\[
 \begin{aligned}
 \Phi={}&(\eta-x)
 H_2\left({\eta(1-x)-x\over\eta-x}\right)\\
 &+(1-\eta x)H_2\left({x\over1-\eta x}\right)
 +H_2(x)-\eta K(1-x)\\
 ={}&1.3539958178\ldots .                              \tag{23}
 \end{aligned}
\]

Since $log N_t=Ht+o(t)$,

\[
 {\Phi\over H}=1.6689662610\ldots
               >\log_2 3=1.5849625007\ldots,          \tag{24}
\]

which proves (1).

The exact integer bank already crosses the target at $t=240$; its
normalized exponents for $t=80,160,240,320$ are respectively

\[
 1.48942856\ldots,quad1.57750216\ldots,quad
 1.60693627\ldots,quad1.62178362\ldots .              \tag{25}
\]

## 5. What remains

The theorem proves that the Pascal cap/cup endpoint skew is not itself a
projection-uniform barrier. The only surviving counter-regression must
prevent the three prefix rectangles in (7) and (10) from coexisting in one
actual chamber. In the cross-wall language, it must commute disjoint swap
events so that the $A$-after bank and the two-sided $B$ guards are
systematically anti-aligned.

The first-jump theorem from the preceding report pays a concentrated
failure by a common physical edge. What remains is therefore a genuinely
diffuse cross-wall scheduling problem. The lex gauge is a realizable
positive endpoint, not a proof for every schedule.

## 6. Verification

Run

```text
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_pascal_weighted_inversion_lex_seam_gate.py
```

The script evaluates the exact Pascal recurrences through $t=320$, checks
the prefix-bank lower bound, checks the dominant-path lower term, and
verifies (23)--(25). Expected output begins

```text
PASS: lex-seam weighted inversion bank; limit exponent=1.668966261001
```
