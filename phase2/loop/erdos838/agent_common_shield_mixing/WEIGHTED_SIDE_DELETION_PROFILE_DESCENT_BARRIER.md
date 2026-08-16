# Weighted side-deletion descent: the exact square-root bank and its 3/8 barrier

**Date:** 2026-08-15. All logarithms are base two. This continues
`THREE_ROOT_RECHART_SYNCHRONIZATION_BARRIER.md`.

## Verdict

The tempting one-role release

\[
                  {H\over D}\max\{C(Q),U(Q)\}                   \tag{1}
\]

is false in the universal dominance cage. Deleting the immediate left
neighbour still leaves a farther left carrier label and a right carrier
label. Those two labels continue to cage every root pair. Repeated
neighbour deletion stops only when **one entire carrier side is empty**.

Let `R_L,R_R` be the complete one-sided word reservoirs, so that
`R_L R_R=H` in the complete product. The actual released banks are

\[
                       U(Q)R_L,\qquad C(Q)R_R.                   \tag{2}
\]

Since `C(Q)U(Q)>=V(Q)`, the unconditional payment is exactly

\[
 \boxed{\qquad
       \max\{U(Q)R_L,C(Q)R_R\}
          \ge\sqrt{V(Q)R_LR_R}
          =\sqrt{V(Q)H}.
 \qquad}                                                       \tag{3}
\]

At the proposed live inputs

\[
             \log H=(1/4+o(1))L^2,\qquad
             \log V(Q)=(1/2-o(1))L^2,                           \tag{4}
\]

(3) has coefficient only `3/8`, not `1/2`. Balanced carrier sides and a
balanced root endpoint profile attain this scalar value. Thus the new
cap--cup injection does not by itself close the fixed gap.

The minimizer deletion identity is also insufficient at this point. It
controls the expected number of empty roles of a random ordinary face,
whereas (2) needs the high-order event that every role on one macroscopic
side is empty. A central-layer mask model has half the roles empty in
expectation but gives a prescribed empty half-side probability only
$1/\binom q{q/2}=2^{-q+O(\log q)}$. At $q=\Theta(\log n)$ this recovers
only a polynomial factor, not the missing $n^{\Theta(\log\log n)}$
multiplier.

The stretchable dominance regression realizes the geometric part exactly,
and an exact nonstretchable central-mask model shows why the first-moment
deletion identity cannot finish it. The remaining positive input must be
a high-order/run deletion estimate, a repeated endpoint-potential reset,
or a profile-change bank across successive physical root configurations.

## 1. Full-side deletion is necessary

Let `Q` be affinely squeezed into a universal dominance cage at a missing
macro role. Split the remaining cyclic carrier roles into the two arcs
$\mathcal L,\mathcal R$ incident with that role. The squeeze may be chosen
uniformly so that for every distinct `x,x' in Q`, every selected
$y\in\mathcal L$, and every selected $w\in\mathcal R$,

\[
                    \{x,x',y,w\}\text{ is nonordinary}.          \tag{5}
\]

> **Lemma 1 (side-erasure dichotomy).** If an ordinary face `F` has
> $|F\cap Q|\ge2$, then
> \[
>        F\cap\bigcup\mathcal L=\varnothing
>        \quad\hbox{or}\quad
>        F\cap\bigcup\mathcal R=\varnothing.                    \tag{6}
> \]

**Proof.** Otherwise select `x,x'` from the root trace and one carrier
label from each occupied side. Their four-set is bad by (5), contradicting
heredity. QED.

This is the iterated form of the earlier two-neighbour shield cover. After
deleting the immediate neighbour on one side, (5) simply uses the nearest
remaining role on that side. Hence no bounded number of local deletions
releases a non-singleton root trace unless it exhausts a full side.

### Exact kill of the one-role splice

In the rational 14-point regression, delete the immediate role `Y` but
retain the farther left endpoint `l` and a label of the right role `W`.
Exhaustive computation gives

\[
 \{S\subseteq Q:(\{l,w,r,t\}\cup S)\text{ ordinary for all }w,t\}
       =\binom Q1.                                               \tag{7}
\]

The reflected statement holds after deleting `W`. Thus neither rank-two
root profiles nor the rank-three root face enters the alleged bank (1).

There is a useful projective explanation. If
`x in int triangle(y,w,x')`, then the line `xx'` separates `y` and `w`.
Indeed, writing

\[
                        x=\alpha y+\beta w+\gamma x',
       \qquad \alpha,\beta,\gamma>0,                            \tag{8}
\]

shows that `orient(x,x',y)` and `orient(x,x',w)` have opposite signs.
Therefore even two roots cannot be sent simultaneously to infinity in an
affine chart containing both carrier sides: their only candidate infinity
line cuts the carrier. This is the exact two-root obstruction requested
after the three-root audit.

## 2. One-sided profile product

Write $\mathcal C(Q),\mathcal U(Q)$ for the two directional root-profile
families in the frozen macro chart and put

\[
                  C=|\mathcal C(Q)|,\quad U=|\mathcal U(Q)|,
                  \quad V_Q=V(Q).                              \tag{9}
\]

The upper/lower boundary decomposition injects ordinary root faces into
compatible endpoint pairs, so

\[
                              CU\ge V_Q.                         \tag{10}
\]

Let `R_L` be the number of decoded carrier words wholly on the left side,
and define `R_R` symmetrically. In the lexicographic macro construction,
every left word glues to the appropriate `U` profile and every right word
to the appropriate `C` profile. Physical role traces recover both factors,
so the union maps have load one. Therefore

\[
                   V(P)\ge\max\{UR_L,CR_R\}.                    \tag{11}
\]

Multiplying the two terms in (11) and applying (10) proves (3). More
generally, with output decoder loads $\Lambda_L,\Lambda_R$,

\[
 V(P)\ge
   \sqrt{{V_QR_LR_R\over\Lambda_L\Lambda_R}}.                  \tag{12}
\]

For complete role alphabets of sizes $d_i$,

\[
 R_L=\prod_{i\in\mathcal L}d_i,qquad
 R_R=\prod_{i\in\mathcal R}d_i,\qquad H=R_LR_R.                \tag{13}
\]

Allowing a role to be empty replaces `d_i` by `d_i+1`; at
`d_i=n^{1-o(1)}` and `q=O(log n)` this changes logarithms by `o(1)`, not a
quadratic coefficient.

### Actual `(B,z)` history load

The load-one statement in (11) concerns the constructed tuple
`(root profile,retained side word)`. If it is used to route a full carrier
record `(B,z)`, the omitted side is genuine lost physical data. A right
output which is already known to retain its marked `z` has at most

\[
                  \Lambda_R^{\rm history}
                     \le R_L\,r_Q\,\lambda_{B,z},                \tag{14}
\]

preimages, where `r_Q` is the root-profile rank bound and
$\lambda_{B,z}$ is the maximum residual history weight over one physical
`(B,z)` incidence. Symmetrically,

\[
                  \Lambda_L^{\rm history}
                     \le R_R\,r_Q\,\lambda_{B,z}.                \tag{15}
\]

The factor `r_Q` is the number of possible retained root marks in the
profile; it disappears if a canonical physical mark is fixed in advance.
The factors `R_L,R_R` do not disappear: they are exactly the erased carrier
completions. Hence profile counting gives the absolute bank (11), but it
does not route arbitrary weighted full-word mass at subpower load.

There is a prior obstruction even before (14). Define rooted profile
counts

\[
 C_z=|\{S\in\mathcal C(Q):z\in S\}|,
 \qquad U_z=|\{S\in\mathcal U(Q):z\in S\}|.                     \tag{15a}
\]

The unrooted inequality `CU>=V_Q` gives no lower bound of the form
`C_zU_z>=V_Q`. The scalable rational parabola regression in
`../agent_outer_internal_product/OPPOSITE_SINGLETON_RETURN_AND_ROOTED_PROFILE_ANTI_ALIGNMENT_GATE.md`
has `V_Q=2^m-1` but `C_z,U_z=O(m^2)` for the retained root. Therefore
(3) is an **absolute ordinary-face bank**. To use it as a weighted
`(B,z)` continuation one needs an additional rooted-export hypothesis or
must release the mark. Equations (14)--(15) state the load only after that
eligibility issue is resolved; the factor `r_Q` cannot repair a missing
rooted profile.

The singleton faces $B\cup\{z\}$ remain different: they retain all of
`B,z` and have physical load one. They supply only the already audited
factor `|Q|=n^{1-o(1)}`.

## 3. Exact coefficient bookkeeping

Let the large child/root scale be `D=n/q`, put $\ell=\log D$, and assume

\[
 \begin{aligned}
  \log H&\ge {1\over4}\ell^2-A\ell\log\ell,\\
  \log V_Q&\ge {1\over2}\ell^2-B\ell\log\ell.                  \tag{16}
 \end{aligned}
\]

Then (3) gives only

\[
 \log V(P)
   \ge {3\over8}\ell^2-{A+B\over2}\ell\log\ell.               \tag{17}
\]

Converting $\ell=L-\log q$ does not change the leading `3/8`. In contrast,
the false bank (1) would have given

\[
 \log(H/D)+\log\max(C,U)
       \ge {1\over2}\ell^2-O(\ell\log\ell),                    \tag{18}
\]

which explains why the one-role release looked sufficient. Equation (7)
is the exact geometric reason (18) is unavailable.

For arbitrary profile exponents `c=log C`, `u=log U`, and side entropies
`r_L=log R_L,r_R=log R_R`, the paid exponent is

\[
                       \max\{u+r_L,c+r_R\}.                     \tag{19}

\]

Subject only to `c+u>=log V_Q` and `r_L+r_R=log H`, its minimum is
`(log V_Q+log H)/2`, attained by exact anti-alignment. This is the scalar
coherent-ramp equality case. Repeated descent needs a physical rule
preventing that anti-alignment from resetting at successive roots.

## 4. What the minimizer deletion identity does and does not give

Partition a configuration into physical roles `X_1,...,X_q`. For an
ordinary face `F`, let `k(F)` be the number of occupied roles. Double
counting gives the exact identity

\[
 \boxed{\qquad
  \sum_{i=1}^q V(P\setminus X_i)
      =\sum_{F\in\mathcal F(P)}(q-k(F))
      =V(P)\bigl(q-E k(F)\bigr).
 \qquad}                                                       \tag{20}
\]

Least-counterexample induction lower-bounds every term on the left. Thus
it can force many empty roles on average. But a full-side deletion is the
high-order event

\[
                 F\cap\bigcup_{i\in\mathcal L}X_i=\varnothing. \tag{21}
\]

which is not controlled by (20).

An exact set-system barrier is the uniform central layer on `q` roles.
Every mask occupies `q/2` roles, so every role is empty with probability
one half and (20) has its largest balanced first moment. For a prescribed
half $\mathcal L$, however,

\[
  \Pr(F\cap\mathcal L=\varnothing)
       ={1\over\binom q{q/2}}
       =2^{-q+O(\log q)}.                                      \tag{22}

\]

At $q=\Theta(\log n)$, (22) is only $n^{-\Theta(1)}$. It cannot supply an
$n^{\Theta(\log\log n)}$ scale-recovery multiplier. This mask model is not
claimed planar; the stretchable universal cage verifies the geometric
side-erasure rule, while (22) isolates the additional correlation theorem
a minimizer proof would need.

Induction on the two half-side deletions gives at most the ordinary banks
$V(P\setminus\bigcup\mathcal L)$ and
$V(P\setminus\bigcup\mathcal R)$. When the
halves have linear size, each is polynomially below the parent fixed-gap
target. Repeating this successfully requires a nested sequence of physical
roots with a nonresetting endpoint potential—the same missing history
coordinate identified by the coherent-ramp audit.

## 5. Verification

Run

```text
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_weighted_side_deletion_profile_descent_barrier.py
```

The exact checker reuses the rational 14-point dominance cage. It verifies
that deleting only `Y` or only `W` releases no root pair, classifies every
root-pair carrier role mask as lying wholly on one of the two sides, checks
that each root-pair line separates every `Y,W` choice, exhausts the
weighted load inequalities, and verifies (3), (17), (20), and the exact
central-layer probability (22) for all even `q<=20`.
