# High-order deletion on long runs: exact identities, erasure conservation, and the rooted-reset barrier

**Date:** 2026-08-15. All logarithms are base two. This continues
`WEIGHTED_SIDE_DELETION_PROFILE_DESCENT_BARRIER.md` and uses the literal
mask/run split of
`../agent_shield_circuit_cover/RECOVERABLE_CARRIER_COARSENING_MASK_RUN_GATE.md`.

## Verdict

Least-counterexample deletion minimality does have an exact identity at
**every order**, including a cyclic-interval identity for long empty runs.
It does not supply the missing multiplier.

Let physical roles `X_1,...,X_q` partition `P`, and let `E(F)` be the set of
roles missed by an ordinary face `F`. For every family `A` of role masks,

\[
 \boxed{\quad
 \sum_{S\in A}V\!\left(P\setminus\bigcup_{i\in S}X_i\right)
   =\sum_{F\in\mathcal F(P)}|\{S\in A:S\subseteq E(F)\}|.
 \quad}                                                        \tag{1}
\]

Taking `A` to be the `q` cyclic intervals of length `k` gives the literal
long-run moment. At the live scale

\[
 q=\Theta(L),\qquad D=\Theta(n/L),\qquad
 k=\Theta(L/\log L),\qquad kD=\Theta(n/\log L),                \tag{2}
\]

induction on the complement of one run is still
$2^{\Theta(L/\log L)}$ below the parent target, while there are only `q`
interval placements and one face can be counted by all `q`. More
importantly, the induced run child is short of the parent by

\[
             2^{(1-o(1))L\log\log L}
                =n^{(1-o(1))\log\log L}.                       \tag{3}
\]

Equation (1) counts the **global unweighted face law**. The live role
forest carries a selected weighted incidence law, and no established
inequality compares its density inside the deletion children to the global
law. This is the first exact gap.

There is a second, sharper gap. Expanding a low-`Q_eff` forest path through
the actual labels erased on a run turns its virtual branching factor into
the same factor in physical output load. For a length-`k` run of `D`-label
roles, any output which does not encode the erased word has load `D^k`.
Thus

```text
virtual forest factor D^k / physical history load D^k = 1.
```

This conservation law is attained by an exact planar singleton-transversal
system with atom weight `1/n`, a recoverable interval tag, one deletion run,
and uniform actual-label branching. It survives arbitrary subdivision into
dyadic history weights. Consequently high-order deletion moments do not
turn the forest compensation into ordinary faces.

Finally, planarity alone does not force a nonresetting rooted endpoint
potential. The universal `1+3` cage prevents the erased word and a rich
root trace from coexisting, while the rational parabola child has
`V(Q)=2^m` but only `O(m^2)` profiles in each of two directions when the
physical root is retained. Projective substitution places any finite
sequence of these strict cages in distinct physical pockets. Their
potentials live on different `(B,z)` states, so there is no directed cycle
to telescope.

This is a sharp interface barrier, not a sub-half construction. Its
selected trace system is planar and its loads are exact, but additional
ambient multi-label faces may pay in a genuine minimizer. The remaining
positive input must be one of:

1. a branch-to-global density comparison inside deletion children;
2. an output encoding $n^{\Theta(\log\log\log n)}$ erased-word classes;
3. a rooted-export theorem on a positive minimizer slice; or
4. an actual same-configuration profile return/cycle.

## 1. The complete role-deletion transform

For $F\in\mathcal F(P)$, put

\[
 E(F)=\{i:F\cap X_i=\varnothing\},\qquad
 o(F)=q-|E(F)|.                                                \tag{4}
\]

Here `o(F)` is the number of occupied roles, not the rank of `F`. Fix any
mask $S\subseteq[q]$. The face `F` occurs in
$P\setminus\bigcup_{i\in S}X_i$ exactly when $S\subseteq E(F)$. Summing this
indicator over `S in A` proves (1).

For all masks of size `t`, (1) becomes the factorial-moment identity

\[
 \sum_{|S|=t}V\!\left(P\setminus\bigcup_{i\in S}X_i\right)
       =\sum_F\binom{|E(F)|}{t}.                                 \tag{5}
\]

For cyclic intervals

\[
 I_a=\{a,a+1,\ldots,a+k-1\}\pmod q,
\]

write `r_k(E)` for the number of `I_a` contained in `E`. Then

\[
 \boxed{\quad
       \sum_{a=0}^{q-1}V\!\left(P\setminus
                         \bigcup_{i\in I_a}X_i\right)
          =\sum_F r_k(E(F)).
 \quad}                                                        \tag{6}
\]

The first-order minimizer identity is just (5) with `t=1`. Thus passing to
higher deletion order is algebraically free; the issue is quantitative and
measure-theoretic, not the absence of an identity.

### Least-counterexample consequence

Assume `|X_i|=D`, put $L=\log n$, and let

\[
                   \Phi_C(L)={L^2\over2}-CL\log L.              \tag{7}
\]

If `P` is a least counterexample to $V(P)\ge2^{\Phi_C(\log |P|)}$,
then every term on the left of (6) is at least
$2^{\Phi_C(\log(n-kD))}$. Since $V(P)<2^{\Phi_C(L)}$, the uniform global face
law satisfies

\[
 \mathbb E_F r_k(E(F))
   >q\,2^{-\Delta_{\rm del}},\qquad
 \Delta_{\rm del}=\Phi_C(L)-\Phi_C(\log(n-kD)).                \tag{8}
\]

For the extremal mask/run scale `kD=n/log L`,

\[
 \Delta_{\rm del}
      =\left({1\over\ln2}+o(1)\right){L\over\log L}.           \tag{9}
\]

Because $r_k(E)\le q$, (8) guarantees only the lower bound
$\Pr(r_k(E)>0)>2^{-\Delta_{\rm del}}$ for the fraction of globally counted faces
carrying such a run. This is exponentially small on the `L/log L` scale.
The `q` placements cancel against the possible `q`-fold reuse of one face,
so the identity does not give a multiplier.

The run itself has `m=kD=n/log L` points and
`log m=L-log log L`. Induction inside it loses

\[
 \begin{aligned}
 \Delta_{\rm child}
   &=\Phi_C(L)-\Phi_C(L-\log\log L)\\
   &=(1-o(1))L\log\log L,                                     \tag{10}
 \end{aligned}
\]

which is (3). Equations (9) and (10) are different deficits: deleting the
run leaves an almost-full complement, while using the run as the rich
induced child needs the three-logarithm multiplier.

Nothing in (1), including all choices of `A`, lower-bounds the selected
history mass inside these global faces. The live weights came from
source/mark and forest localization. A transfer would require an explicit
density parameter such as

\[
 \eta=\inf_{S}\frac{\text{selected mass supported in }
             \mathcal F(P\setminus X_S)}
            {V(P\setminus X_S)},                               \tag{11}
\]

and no positive lower bound for $\eta$ is currently banked. The common-cage
regressions have a rich detached deletion bank while their selected mixed
incidence graph is empty, so `eta=0` is possible at the interface level.

## 2. Expansion-load conservation

The following elementary statement is the exact weighted-history ledger
needed after the effective role forest.

> **Theorem 2 (erased-alphabet conservation).** Fix a terminal physical
> state `c`, an erased-word alphabet `A_c`, and an ordinary child bank
> `J_c`. Give every record `(a,G) in A_c times J_c` weight `w_a>=0`.
> Suppose the proposed ordinary output reveals `G` and a code
> `pi(a)` taking at most `K_c` values, but no other information about `a`.
> Then the number of physical outputs is at most `K_c|J_c|`, and some code
> fibre has weighted load at least
> 
> \[
>             {\sum_{a\in A_c}w_a\over K_c}.                    \tag{12}
> \]
> 
> Consequently weighted demand divided by worst load yields at most
> `K_c|J_c|`. If `pi` is constant, expanding the erased alphabet gives
> exactly no gain over `|J_c|`.

**Proof.** There are at most `K_c` outputs for each `G`. Their loads sum to
`sum_a w_a`, so one is at least the average (12). Summing over `G` proves
the output bound. Equality holds when the code fibres have equal weight.
QED.

For a `k`-role run with alphabets of size `D`, `|A_c|=D^k`. In the
near-uniform low-`Q_eff` branch, expanding the selected largest-label path
back through all physical label classes is precisely this alphabet.
The forest factor `C_eff` is `D^{k-o(k)}`. If the mixed output forgets the
run word, (12) returns the same factor as history load. The genuine
`(B,z)` multiplicity in
`WEIGHTED_SIDE_DELETION_PROFILE_DESCENT_BARRIER.md`, equations (14)--(15),
is this conservation law with one side as `A_c`.

### Exact planar equality case with an atom floor

Take `q+1` disjoint rational point clouds on a parabola, one tag cloud and
`q` word roles, each word role having `D` labels. Every choice of one point
per used cloud is an ordinary same-order-type transversal. For every tag
`s in Z/qZ` and every full word `a in [D]^q`, delete the cyclic interval
`I_s` of length `k` and output

\[
                (s,a|_{[q]\setminus I_s}).                       \tag{13}
\]

The tag is a retained physical point. The mask has exactly one run, so it
is already in the few-run branch of the mask/run theorem. There are

\[
 qD^q\ \text{records},\qquad qD^{q-k}\ \text{outputs},
 \qquad \text{load }D^k.                                      \tag{14}
\]

Giving every record weight `1/n` makes the exact load `D^k/n`; hence the
initial polynomial atom floor does not help. Conditional on a tag and a
role, all `D` actual labels have equal mass. Thus the example also has the
strongest possible mass-uniform branching. It is stretchable, rational,
and its interval tag has load one; the only collision is the genuinely
erased physical word.

The ambient parabola is deliberately face-rich. Equation (14) is not a
low-face construction; it proves that no decoder argument can treat the
forest compensation as a new face alphabet. To gain from the run one must
make the output record at least
$K_c=n^{\Theta(\log\log\log n)}$ distinguishable erased-word classes.

At (2),

\[
             \log D^k=(\Theta(1)+o(1)){L^2\over\log L}
                  \gg L\log\log L.                              \tag{15}
\]

Thus the physical erasure capacity is more than large enough to absorb the
entire desired multiplier (3).

## 3. Planar cage and rooted-potential reset

The erasure ledger would be harmless if rich run-child faces could be
attached to enough erased-word classes. The exact planar obstruction is
the universal dominance cage already verified in
`WEIGHTED_SIDE_DELETION_PROFILE_DESCENT_BARRIER.md`: a face with at least
two root labels must erase an entire carrier side. The long-run version in
`LONG_RUN_PAIR_STAR_INCIDENCE_BARRIER.md` has a fixed physical pair
$o,p$ and

\[
             p\in\operatorname{int}\triangle(o,a,b)             \tag{16}
\]

for every left label `a` and right label `b`. Hence the compatible
run-child-face by retained-context incidence graph can be empty. Its
triangle tag remembers only two of the $\Theta(L)$ word coordinates and has
the exact complementary load.

Could repeated side deletion nevertheless force a rooted endpoint
potential to telescope? Not from the present state. The rational parabola
child of
`../agent_outer_internal_product/OPPOSITE_SINGLETON_RETURN_AND_ROOTED_PROFILE_ANTI_ALIGNMENT_GATE.md`
has

\[
                V(Q)=2^m,\qquad C_z,U_z=O(m^2),                  \tag{17}
\]

for one retained physical root `z`; at `m=14` the exact counts are
`C_z=86`, `U_z=106`, and `C_zU_z=9116<2^14`. Thus even the absolute
endpoint product need not survive the mark required by the history
decoder.

> **Lemma 3 (finite rooted-reset composition).** Suppose each member of a
> finite list is a rational cage interface whose arbitrary-child pocket has
> already been put in the local universal-dominance chart. The interfaces
> can be nested in successively smaller pockets so that every prescribed
> earlier cage circuit is preserved, every intrinsic child order type is
> preserved, and the retained roots at different levels are distinct
> physical labels.

**Proof.** At one substitution step place an affine copy of the next local
interface in the designated dominance pocket and scale it by a positive
parameter `epsilon`. The required intrinsic determinants are positive
powers of `epsilon` times their original nonzero values. Every prescribed
macro and cage inequality is strict at the chosen local model and remains
strict for all sufficiently small `epsilon`. There are only finitely many
conditions, so a positive rational `epsilon` works simultaneously. Iterate.
QED.

At level `j` the state is `(B_j,z_j)` with a new physical root. The
directed endpoint potential at level `j+1` is not the endpoint of the state
at level `j`; it is a fresh chart variable. Hence the exact cycle telescope
from `MINIMIZER_ALL_LOOP_ENDPOINT_POTENTIAL_GATE.md` does not apply.

This substitution statement controls the nested interface, not the total
ambient face count. A genuine least-counterexample proof may still exclude
the tower by finding an ambient profile surplus or a `V`-decreasing
mutation. What deletion minimality alone cannot do is identify the
different rooted states or turn their virtual forest factors into faces.

## 4. Exact remaining positive statement

Let a weighted terminal family have states `c`, masses `mu_c`, effective
forest factors `C_c`, long-run child banks `J_c`, and actual ordinary union
decoder load `Lambda`. If a construction realizes `C_c` distinguishable
physical choices for every state, the literal sufficient inequality is

\[
              V(P)\ge {1\over\Lambda}
                    \sum_c\mu_c C_c|J_c|.                        \tag{18}
\]

Equation (18) is useful only when `C_c` is represented by actual
distinguishable outputs. Theorem 2 shows that if the output retains only
`K_c` erased-word classes, then its contribution is at most
`K_c|J_c|`; writing `C_c` in the numerator and again in `Lambda` is a
cancellation, not a bank.

Therefore the precise next theorem must show, on positive live mass,

\[
 K_c\ge n^{\sigma\log\log\log n}                                \tag{19}
\]

for a fixed `sigma>0`, or else force an actual directed return to the same
rooted profile state. A run occurrence, all-order deletion identities,
near-uniform actual-label branching, and the `1/n` atom floor do not imply
(19).

## 5. Verification

Run

```text
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_high_order_deletion_run_rooted_reset_barrier.py
```

The checker verifies (1), (5), and (6) on the complete rational 14-point
cage face complex for every role mask; exhausts the planar run-erasure
encoder for small `q,D,k`, including the exact `1/n` loads and one-run
masks; checks the two fixed-gap deficits and erasure exponent numerically;
and rechecks the exact rooted profile obstruction `(86,106)`.
