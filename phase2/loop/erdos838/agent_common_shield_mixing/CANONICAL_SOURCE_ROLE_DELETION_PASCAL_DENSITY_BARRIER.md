# Canonical marked-source density versus all-order deletion: a full Pascal barrier

**Date:** 2026-08-15. All logarithms are base two. This continues
`HIGH_ORDER_DELETION_RUN_ROOTED_RESET_BARRIER.md` and sharpens
`LIVE_PASCAL_COMMON_GUARD_MULTIPLICATION_BARRIER.md`.

## Verdict

A branch-to-global density comparison is not the missing theorem. In the
central Pascal cell, the comparison holds at **polynomial density** for the
actual canonical marked-source weights, survives unordered injective role
colouring, and is compatible with the complete all-order role-deletion
transform. Nevertheless the source--release rectangle remains identically
bad and the terminal output load cancels the source factor exactly.

Let

\[
             P=T(2h,h)=Y\prec Z,\qquad N=|P|={2h\choose h},      \tag{1}
\]

where `Y=T(2h-1,h-1)` and `Z=T(2h-1,h)` are the two equal children. There
are a canonical triple $T\subset Y$, a rank $r=O(\log N)$, and a family
$\mathcal D$ of noncap ordinary faces of `Y` such that:

1. the minimizer marking weight from
   `../agent_outer_internal_product/MINIMIZER_WEIGHTED_LOOP_COVER_GATE.md`
   satisfies
   \[
                         \omega(D,T)\ge {1\over2}                 \tag{2}
   \]
   for every $D\in\mathcal D$;
2. after unordered injective colouring of the nonroot labels, one retained
   family `E` has
   \[
                \sum_{D\in\mathcal E}\omega(D,T)
                      \ge {V(P)\over4N^{14}};                    \tag{3}
   \]
3. the noncup released family
   $\mathcal H=\mathcal F(Z)\setminus\mathcal U(Z)$ and the full
   deletion-complement bank satisfy
   \[
                 |\mathcal H|,\ V(Z)\ge {V(P)\over2N^7};        \tag{4}
   \]
4. every role-deletion child retains all of `Z`, so every order of the
   global deletion transform has at least `V(Z)` ordinary faces; and
5. for every $D\in\mathcal E$ and $U\in\mathcal H$, the unique guard is all
   of `D`:
   \[
       (D\setminus G)\cup U\in\mathcal F(P)
                    \quad\Longleftrightarrow\quad G=D.           \tag{5}
   \]

Thus every source role is empty in the terminal output. The empty mask is
the whole cyclic role system, hence one maximal run in every role order.
Pocket replication keeps each raw record weight `omega(D,T)`; it does not
divide by `|H|`. For a fixed `U`, the terminal output load is exactly

\[
                       \Lambda(U)=\sum_{D\in\mathcal E}\omega(D,T),
                                                                    \tag{6}
\]

so the weighted rectangle divided by its actual load yields exactly
`|H|`, not `|E||H|`.

This is a full stretchable planar configuration, not a selected trace
complex. Its entire face count is the exact strong-glue recurrence

\[
                  V(P)=V(Y)+V(Z)+C(Y)U(Z),                       \tag{7}
\]

up to the harmless common empty-face convention. It also survives every
independent reflection or swap of the two top children: the displayed
orientation uses the smallest of the four endpoint products.

The scope is sharp. The Pascal cell is not a counterexample to the desired
half bound; its coefficient is

\[
                  \beta=1-{1\over4\ln2}>\frac12.                 \tag{8}
\]

Consequently it satisfies all **role-deletion lower bounds** that a
half-target least counterexample would inherit, but it violates the parent
upper bound $V(P)<2^{\Phi_{1/2}(\log N)}$. Therefore:

> canonical source density, atom floors, unordered colouring, planarity,
> all-order/cyclic deletion identities, and induction lower bounds on every
> relevant deletion child do not force the missing multiplier. A positive
> result must use the parent fixed-gap upper bound jointly with a genuinely
> global mutation/profile inequality.

No such minimizer inequality is proved here. Conversely, this report does
not claim a sub-half construction.

## 1. The canonical marking is literal in the strong-glue cell

Write `F(X),C(X),U(X)` for the nonempty ordinary, cap, and cup families.
Set

\[
 \mathcal S_Y=\mathcal F(Y)\setminus\mathcal C(Y),
 \qquad
 \mathcal H_Z=\mathcal F(Z)\setminus\mathcal U(Z).              \tag{9}
\]

Fix `D in S_Y`. Its canonical tangent-triple family is

\[
 \mathcal T(D)=
 \{\{v_i,v_{i+1},v_j\}:j\notin\{i,i+1\}\},                    \tag{10}
\]

where the `v_i` are the boundary vertices of `D` in cyclic order. For
every `z in Z`, strong glue gives

\[
       Q\cup\{z\}\text{ is ordinary}
             \quad\Longleftrightarrow\quad Q\text{ is a cap}    \tag{11}
\]

for every nonempty `Q subseteq D`. The tangent cover contains a noncap
triple because it must witness the non-addability of `z`. More importantly,
the predicate in (11) is independent of `z`. Hence the first member of
`T(D)` witnessing `z` is one fixed triple `T(D)` for **every** `z in Z`.

Its bad-circuit degree obeys

\[
                         d(T(D))\ge |Z|=N/2.                       \tag{12}
\]

The heavy threshold in the canonical marking is `D_0/2`, where

\[
 D_0={N-2\mu\over(R-2)\mu}.                                    \tag{13}
\]

For the Pascal cells, $R=O(\log N)$ and $\mu=\Omega(\log N)$. To see the
second assertion directly, the number of faces of rank at most
$\alpha\log N$ is at most $N^{\alpha\log N+1}$; choosing
$\alpha<\beta$ and comparing with (8) shows that a positive fraction of
the face law has rank $\Omega(\log N)$. Hence $D_0\le N$ for all
sufficiently large `h`; the exact `T(6,3)` verifier checks this directly.
Thus every `z in Z` is a heavy record assigned to the same
`T(D)`, and the literal definition of the marked weight gives

\[
 \omega(D,T(D))
   ={1\over N}|\{p:T_D(p)=T(D)\text{ and }p\text{ is heavy}\}|
   \ge {|Z|\over N}={1\over2}.                                 \tag{14}
\]

This is stronger than the `1/N` atom floor. It is not an artificial
row-normalization.

Partition `S_Y` by `(T(D),|D|)`. There are at most
`binom(|Y|,3)(2h+1)<=N^4` cells, so one fibre `D` has

\[
                         |\mathcal D|\ge {|\mathcal S_Y|\over N^4}.
                                                                    \tag{15}
\]

All faces in a Pascal cell have rank at most `2h=O(log N)`, so this fibre
is rank-safe without a further cutoff.

Colour the nonroot physical labels of `Y` independently by the
`s=r-3` nonroot roles. Unordered injective colouring retains weight at
least `(s!/s^s)` of (15). Since `s<=2h`,

\[
             {s!\over s^s}\ge e^{-s}\ge3^{-2h}\ge N^{-3}        \tag{16}
\]

for `h>=3`. Combining (14)--(16) with the polynomial parent/child estimate
proved next gives (3).

## 2. A polynomial, not quasipolynomial, parent/child ratio

The previous Pascal barrier used the sufficient but loose estimate
`V(P)/V(Y)<=2^{O(h log h)}`. The exact cap recurrence improves this to

\[
                         \boxed{V(P)/V(Y)\le N^7.}                \tag{17}
\]

For completeness, put `m=2h-2`, `i=m/2`, and

\[
 a=C_{m,i-1},\qquad b=C_{m,i},\qquad B={m\choose i},
 \qquad c=C_{2h-1,h-1}.                                       \tag{18}
\]

The exact recurrence and the child mixed bank give

\[
                    c=b+(1+B)a,\qquad V(Y)\ge ab.                \tag{19}
\]

Let `M_(m,j)` be the latest-step path product in the cap recurrence. Its
standard bounds are

\[
                 M_{m,j}\le C_{m,j}\le {m\choose j}M_{m,j}.     \tag{20}
\]

For adjacent central indices, cancellation of the path products gives

\[
             {M_{m,i}\over M_{m,i-1}}\le2^m,
 \qquad
             {M_{m,i-1}\over M_{m,i}}\le2^m.                    \tag{21}
\]

Indeed, in the first ratio every common numerator factor is no larger than
its denominator and the last factor is at most `2^m`. In the reverse ratio,
each common factor grows by at most

\[
 {1+{m-i+j\choose j}\over1+{m-i+j-1\choose j}}
       \le {m-i+j\over m-i}\le2,                               \tag{22}
\]

and there are at most `m` factors. Equations (20)--(22) imply

\[
                          2^{-2m}\le {b\over a}\le2^{2m}.        \tag{23}
\]

Using `B<=2^m`, (19), and `r=b/a`,

\[
 {c^2\over V(Y)}
   \le{(r+1+B)^2\over r}\le2^{4m+4}.                           \tag{24}
\]

The central recurrence is `V(P)=2V(Y)+c^2`, so
`V(P)/V(Y)<=2^{4m+5}`. Finally

\[
                 N={2h\choose h}\ge {2^{2h}\over2h+1}           \tag{25}
\]

implies (17) for `h>=3`.

The known cap asymptotic also gives

\[
       |\mathcal S_Y|\ge V(Y)/2,
       \qquad |\mathcal H_Z|\ge V(Z)/2                         \tag{26}
\]

for all sufficiently large `h` (the exact dynamic program verifies it from
`h=3` onward). Equations (14)--(17) and (26) yield (3)--(4).

## 3. Unordered roles and the complete deletion transform

Fix the maximizing colouring in (16). Use the three labels of `T` as
singleton roles and the colour classes in $Y\setminus T$ as the other roles.
They partition all of `Y`; every retained source occupies exactly one label
in every role.

For any family `A` of role masks, the exact transform from the preceding
report applies:

\[
 \sum_{S\in A}V\!\left(P\setminus\bigcup_{i\in S}X_i\right)
   =\sum_{F\in\mathcal F(P)}|\{S\in A:S\subseteq E(F)\}|.       \tag{27}
\]

This holds at every order and for cyclic intervals in any chosen order of
the unordered colour classes. Every deletion complement on the left still
contains the entire induced child `Z`, and therefore

\[
             V\!\left(P\setminus\bigcup_{i\in S}X_i\right)
                         \ge V(Z)\ge {V(P)\over N^7}.             \tag{28}
\]

Since $\log V(P)=(\beta+o(1))(\log N)^2$ with $\beta>1/2$, the right side of
(28) exceeds

\[
 2^{\frac12(\log N_S)^2-C(\log N_S)\log\log N_S}               \tag{29}
\]

for every relevant remaining size `N_S<=N` and all sufficiently large
`N`. Thus the example satisfies the complete family of role-deletion
**lower bounds** available from fixed-gap least-counterexample induction.

Yet for every `D in E`, `U in H`, and `G subseteq D`, strong glue gives
(5): if $D\setminus G$ is nonempty, its right partner `U` is not a cup, so the
union is nonordinary. Only deleting the entire source releases `U`.
The terminal mask is all roles, hence one full cyclic run. The output
retains no source label, so (6) is its actual physical-history load.

This proves that even a polynomial branch-to-global density comparison and
all higher deletion moments cannot supply the desired
$N^{\Omega(\log\log\log N)}$ factor.

## 4. Exact local mutation audit

Write the endpoint profiles of the two children as

\[
 C(Y)=U(Z)=c,\qquad U(Y)=C(Z)=u.                              \tag{30}
\]

The exact Pascal recurrence has `c<=u`. The displayed top split uses mixed
term `c^2`. Independent reflection of either child and swapping the children
produce precisely

\[
                         c^2,\quad cu,\quad cu,\quad u^2.        \tag{31}
\]

Thus the current orientation is already minimal among all reflection/swap
mutations. This kills the most immediate `V`-decreasing repair of the dense
all-delete branch.

It does not prove global `V`-minimality among all `N`-point order types.
Indeed the coefficient in (8) rules that out relative to the desired half
benchmark. A successful minimizer argument must exploit this global surplus
through a mutation or profile bank not expressible by (27), (28), or the
four endpoint choices (31).

## 5. Verification

Run

```text
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_canonical_source_role_deletion_pascal_density_barrier.py
```

The exact rational `T(6,3)` audit reconstructs every canonical tangent
family, assigns every blocked point to its first witness, computes the heavy
threshold and literal marked weights, performs unordered colouring, checks
all deletion transforms on the complete ambient face complex, and verifies
the terminal loads. The independent integer dynamic program checks
(17)--(26), the polynomial live normalization, and reflection minimality
through `2h=120`.
