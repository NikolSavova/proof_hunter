# Omitted petals: central-shadow descent, relative circuit factoring, and the alphabet barrier

**Date:** 2026-08-14.  All logarithms are base two.

## Verdict

The final tangent-marked fibre admits an exact rank-halving descent, and
bad-circuit component factoring remains exact after the common prefix is
fixed.  Neither statement, however, preserves the collision square in the
large-alphabet regime.  A scalable radial family retaining the full tangent
cell, actual repair mark, actual shield face, and common prefix realizes the
loss sharply while its residual relative circuit graph is connected.

Let `B` be the fixed tangent-guarded prefix and let `mathcal D` be `M`
distinct uniform `t`-petals such that

\[
                         B\cup D\in\mathcal F(P)            \tag{1}
\]

for every `D`.  For `0<=k<=t`, put

\[
 d(I)=|\{D\in\mathcal D:I\subseteq D\}|,
                         \qquad |I|=k.                     \tag{2}

The exact first and second moments are

\[
 \sum_Id(I)=M\binom tk,
 \qquad
 \sum_Id(I)^2=
       \sum_{D,D'}\binom{|D\cap D'|}{k}.                  \tag{3}

Every `B union I` is an ordinary face.  Thus, with weights and maximum
shadow codegree `Lambda_k`,

\[
 \boxed{W\binom tk\le\Lambda_kV(P).}                       \tag{4}
\]

Low codegree pays.  A high-codegree output fixes `I`, replaces the base by
`B'=B union I`, and leaves distinct residual petals `E=D-I` of rank
`t-k`.  At `k=floor(t/2)` this is an exact rank halving.  Pairwise detached
incompatibility persists, and its first bad circuit crosses both residual
petal differences.

For a fixed base `B'`, define the relative link

\[
 \mathcal L_(B')(Z)=\{E\subseteq Z:B'\cup E\in\mathcal F(P)\}. \tag{5}

Partition `Z` into containers and join two containers when a bad four-
circuit in `B' union Z` has variable points in both.  If `Z_1,...,Z_s` are
the component unions, then

\[
 \boxed{\mathcal L_(B')(Z)=
          \mathop{*}_{a=1}^s\mathcal L_(B')(Z_a),
        \qquad V_(B')(Z)=\prod_aV_(B')(Z_a).}              \tag{6}

This is the base-relative version of the detached component identity.  It
gives the same exact entropy/Kraft localization: independent residual
components pay their full link shields, and failure descends to one
relative-circuit-connected child of rank at most `ceil(t/2)`.

The proposed **square-preserving** telescope is nevertheless false.  In a
complete `L`-ary transversal family on `t` variable radial blocks,

\[
 M=L^t,qquad
 \#\{I:d(I)>0\}=\binom tkL^k,qquad
 d(I)=L^{t-k}.                                             \tag{7}

Consequently

\[
 \boxed{\sum_Id(I)^2=M^2{\binom tk\over L^k}.}             \tag{8}

At `k=t/2`, `L=D^delta`, `t=kappa log D`, the factor in (8) loses
`Theta((log D)^2)` bits.  A heavy prefix fixing any chosen `k` block values
leaves the complete product on the other `t-k` blocks.  Choosing the
unfixed blocks as one cyclic interval makes their relative bad-circuit
graph connected, so (6) gives no independent-component product at that
node.

This family still exits through the radial one-gap/container shields and
therefore is not an EIC' counterexample.  It proves that central shadows
plus **undirected** circuit-component factoring cannot close the final
atom.  The next load-bearing history coordinate is the value/profile in
each omitted alphabet block, together with a canonical first-divergence
container.  Merely knowing that some base-assisted circuit joins two blocks
overconnects the radial example and discards precisely the local shield
which pays it.

## 1. Weighted central-shadow identities

Let the petals carry weights `w_D>=0`, and put `W=sum_Dw_D`.  Define

\[
 s(I)=\sum_{D\supseteq I}w_D,
             \qquad \mathcal I_k=\{I:|I|=k,\ I\subseteq D
                                      \text{ for some }D\}. \tag{9}

> **Theorem 1 (central-shadow Carleson and energy).**
> \[
> \sum_{I\in\mathcal I_k}s(I)=\binom tkW,                 \tag{10}
> \]
> \[
> \sum_{I\in\mathcal I_k}s(I)^2
>   =\sum_{D,D'}w_Dw_(D')\binom{|D\cap D'|}{k},           \tag{11}
> \]
> and if `Lambda_k=max_Is(I)`, then (4) holds with `W` in
> place of `M`.

**Proof.**  A petal has exactly `binom(t,k)` `k`-subsets, which proves
(10).  Expanding the square and then counting the common `k`-subsets of
`D,D'` proves (11).  Finally, every output `B union I` is ordinary by
deletion from (1), and `B` is fixed, so distinct `I` give distinct ordinary
faces.  Hence

\[
 \binom tkW=\sum_Is(I)\le\Lambda_k|\mathcal I_k|
                              \le\Lambda_kV(P).             \tag{12}
\]

QED.

There is a size-biased rank-halving formulation.  Choose `I` with
probability proportional to `s(I)`.  Then

\[
 \mathbb E_*s(I)={\sum_Is(I)^2\over\binom tkW}.             \tag{13}

Cauchy and `|mathcal I_k|<=V(P)` imply

\[
 \mathbb E_*s(I)\ge {\binom tkW\over V(P)}.                \tag{14}

Thus either (12) already pays, or a size-biased child retains large mass
while its variable rank falls from `t` to `t-k`.  Equation (11), not just
(14), is the correct square ledger.

For an unweighted family, same-shadow collisions have energy

\[
 \mathcal C_k={1\over2}
       \left(\sum_Id(I)^2-M\binom tk\right).               \tag{15}

If a `theta` share of this energy maps to ordinary splice faces with load
`L`, the previous one-face collision quadratic applies to the incidence
mass `N=M binom(t,k)`.  The strict detached residue has no such splice, so
the high-shadow child below is unavoidable.

## 2. Exact rank-halving child

Fix `I` and restrict to

\[
                 \mathcal D_I=\{D\in\mathcal D:I\subseteq D\}. \tag{16}

Put `B'=B union I` and `E_D=D-I`.  Then

\[
                         B'\cup E_D=B\cup D                \tag{17}

is ordinary, and all residual petals have rank `t-k`.  Distinct `D` give
distinct `E_D`.

> **Lemma 2 (detached incompatibility survives).**  If the original
> completions `B union D` are pairwise detached-incompatible, then so are
> the carriers `B' union E_D`.  Moreover, a bad four-circuit in the union
> of two carriers meets both `E_D-E_(D')` and `E_(D')-E_D`.

**Proof.**  The carriers are literally the original completions by (17).
A bad circuit exists.  It cannot lie in either individual ordinary
carrier, so it contains a point exclusive to each one.  Since `B'` is
common, those points lie in the two residual differences.  QED.

At central `k`, the rank is at most `ceil(t/2)`.  No tangent state is lost:
`B'` still contains the five tangent guards, while the previously fixed
repair mark `p` and shield face `F` remain external named data of the cell.

## 3. Relative circuit-component factoring

Let `B'` be any ordinary face, disjoint from a variable support
`Z=X_1 dotcup ... dotcup X_m`.  Define a graph on the container labels by
joining `i,j` if some bad four-set

\[
                         C\subseteq B'\cup Z               \tag{18}

has nonempty intersection with both `X_i` and `X_j`.  Let the connected
component unions be `Z_1,...,Z_s`.

> **Theorem 3 (relative circuit join).**  Equation (6) holds.

**Proof.**  Restriction gives one inclusion.  Conversely, suppose
`E cap Z_a` belongs to `mathcal L_(B')(Z_a)` for every `a`, but
`B' union E` is nonconvex.  Choose a bad four-circuit `C` in it.  Since
`B'` is ordinary, `C` has a variable point.  If all variable points of `C`
lie in one `Z_a`, then

\[
                  C\subseteq B'\cup(E\cap Z_a),            \tag{19}

contradicting the local link condition.  Otherwise `C` meets containers in
two different components, but (18) makes those containers adjacent, also a
contradiction.  Hence the link is the simplicial join, and its choices are
uniquely recovered componentwise, proving the product count.  QED.

For a uniform residual family of size `M_I`, let `E_a=E cap Z_a`,
`h_a=H(E_a)`, and `V_a=|mathcal L_(B')(Z_a)|`.  Exactly as in the detached
identity,

\[
 \log{V_(B')(Z)\over M_I}
 =\left(\sum_ah_a-\log M_I\right)
     +\sum_a(\log V_a-h_a).                               \tag{20}

Thus a failure of fixed-power link surplus forces small total correlation,
small total local surplus, and an entropy-density localization to one
relative-circuit-connected component.  The component rank is no larger
than the already-halved residual rank.

The adjective **relative** is essential.  Circuits which contain points of
the fixed prefix can join variable containers even when the induced
configuration on `Z` has no such circuit.  The exact verifier audits (6)
over every base face of a nontrivial rational configuration.

## 4. Why the square does not telescope

Take `t` labelled containers `X_1,...,X_t`, each of size `L`, and the
complete transversal family

\[
              \mathcal D=\{\{x_(1,j_1),...,x_(t,j_t)\}:
                                   (j_1,...,j_t)\in[L]^t\}. \tag{21}

A `k`-shadow chooses its `k` occupied container labels and their values.
Therefore there are exactly `binom(t,k)L^k` outputs, all with the same
codegree `L^(t-k)`.  This proves (7).  Squaring the common degree gives

\[
 \sum_Id(I)^2=\binom tkL^kL^{2(t-k)}
       =L^{2t}{\binom tk\over L^k},                        \tag{22}

which is (8).

For `k=t/2`, Stirling gives

\[
 \log {M^2\over\sum_Id(I)^2}
       =k\log L-\log\binom tk
       ={t\over2}\log L-t+O(\log t).                     \tag{23}

On the live scale in the verdict, this is `Theta((log D)^2)`.  Hence an
argument which replaces a parent collision square by the sum of the child
squares loses a leading quadratic coefficient in one step.  No choice of
constant-factor Cauchy bookkeeping repairs (23).

The first moment does not have this defect: (10) is exact.  The obstruction
is specifically the square needed by the collision telescope.  The lost
quantity is the alphabet value in every unretained block.

## 5. Scalable tangent-marked barrier

Use the radial repair-star construction from
`TANGENT_MARKED_SHIELD_DESCENT.md`.  Fix representatives in the four
blocks around the repair insertion,

\[
                         X_(q-1),X_0,X_1,X_2,              \tag{24}

fix an actual repair label `p`, and fix an actual internal shield face
`F` containing `p`.  The remaining

\[
                              t=q-4                        \tag{25}

active blocks, each of size `L`, give precisely (21).  The common prefix
contains the full tangent cell `(a,u,p,v,b)` after adjoining the marked
star, and every nontrivial star--shield union is nonconvex.  Thus the
construction retains every datum required in the question.

Choose `k` variable blocks and fix their representatives.  This is a
literal high-shadow fibre of size `L^(t-k)` with common enlarged prefix.
Choose the unretained blocks to be one cyclic interval.  The standard
radial nesting circuits meet two neighboring variable containers (and may
also use fixed prefix vertices), so the relative circuit graph of the
interval is connected.  Theorem 3 therefore has only one child.

With `q=Theta(log D)` and `L=D^delta`, both the parent and a central child
have quadratic logarithmic entropy.  Equation (23) proves that the
rank-halving square loss is sharp in an actual planar, fixed-tangent,
marked-repair family.

This construction has large local block reservoirs.  The cyclic one-gap
profile theorem multiplies them and pays the EIC target.  The barrier says
that neither the central shadow nor the undirected relative component graph
sees those reservoirs: the former erases block values, while the latter is
made connected by base-assisted `2+1+1` circuits.

## 6. Exact rational audit

The verifier reuses the eight rational two-point radial blocks and the
nonconvex four-point repair shield from the tangent report.  After fixing
the tangent blocks `7,0,1,2`, the four variable blocks `3,4,5,6` give

\[
                              t=4,\quad L=2,\quad M=16.     \tag{26}

For every `k`, exhaustive enumeration verifies

\[
 \begin{array}{c|c|c|c|c}
 k&\#\text{incidences}&\#\text{outputs}&d(I)&\sum_Id(I)^2\\ \hline
 0&16&1&16&256\\
 1&64&8&8&512\\
 2&96&24&4&384\\
 3&64&32&2&128\\
 4&16&16&1&16.
 \end{array}                                               \tag{27}

At the central level, `384=16^2 binom(4,2)/2^2`, exactly (8).  Fixing the
outer representatives in blocks `3,4` leaves a rank-two four-member child
on blocks `5,6`; all four carriers are ordinary and pairwise detached-
incompatible.  Its relative circuit graph is connected.  On the full four
variable blocks the relative graph is in fact complete, witnessed by exact
rational bad four-circuits containing the fixed prefix.

The verifier also exhausts the relative-link identity (6) over every base
face of a five-point nonconvex rational configuration, checks the weighted
identities (10)--(11) on nonuniform set families, and verifies every
displayed count in (27).

## 7. Exact remaining coordinate

After central rank halving and relative component localization, the unpaid
state is:

1. a fixed tangent cell, repair mark, shield face, and convex prefix;
2. one relative-circuit-connected support child;
3. uniform residual petals of rank at most half the parent rank; and
4. a large alphabet of possible values at each residual container/address.

The radial barrier shows that “connected” is too coarse: base-assisted
circuits can connect every pair of containers even though the paying face
capacity is stored inside the individual alphabet blocks and their cyclic
directional profiles.  The next history coordinate must therefore be a
**canonical first-divergence container and its oriented local profile**.
Using all available bad circuits as undirected edges destroys that address.

Equivalently, a successful telescope must charge the factor `L^k` lost in
(8) to ordinary faces of the omitted alphabets before descending.  Without
that charge, square-preserving rank halving is false on the exact planar
family above.
