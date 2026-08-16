# Pairwise-convex triple circuits: guard release, shield matching, and the same-edge barrier

**Date:** 2026-08-15.  This attacks the dense four-target Hall residue after
the ordinary targets

\[
 A=B\cup G,\quad C=B\cup F,\quad
 W=F\cup\{v\},\quad Q=B\cup\{v\}                       \tag{1}
\]

have been retained.  All point sets are in planar general position.

## Verdict

There is an exact local circuit classification.  If the three pairwise
unions `B union F`, `B union {v}`, and `F union {v}` are convex but
`B union F union {v}` is not, every minimal obstruction is a four-circuit
which contains `v` and meets both `B` and `F`.  Its role split is necessarily

\[
                 (2B,1F,1v)\quad\hbox{or}\quad(1B,2F,1v). \tag{2}
\]

Moreover, deleting `Z subseteq B union F` releases the full union exactly
when `Z` hits every such circuit trace.  If `tau` is the minimum hitting-set
size, a maximum disjoint trace matching has size at least `tau/3`.
This yields an exact rooted-release versus detached-shield bank: at total
rank `r=|B|+|F|`, one cell supplies either `2^{r-tau}` ordinary rooted
downfaces containing `v`, or a canonical detached Boolean shield of at
least `2^tau` faces.  Thus the larger local reservoir is always
`2^{r/2-O(1)}`.  The global statement uses the actual one-face output load;
there is no hidden context copy.

Two tempting strengthenings are false.

1. The bad circuit need not meet either tangent neighbor of `v` in
   `B union {v}`.  A seven-point integer example below has a circuit
   `v+B+2F` disjoint from both tangent neighbors.
2. A small guard release need not cross-complete with the old source
   completion.  There is a scalable `m by m` rational rectangle with one
   unique one-label release in every column, but every released face is
   incompatible with every source-row ear.  All bad circuits have one
   common base root and are independent of the source row.

The scalable regression is not a global low-face counterexample: its rows
and columns have singleton marks, so the two-point faces `{g_i,x_j}` form
an injective `m^2` bank.  It is a sharp kill of any theorem based only on
the four Hall targets, one canonical circuit, or the naive released union.
The genuine residual must have quadratic entropy inside the row/column
faces while simultaneously making every small mark projection highly
reused--precisely the high-support-redundancy/common-edge child left by the
current synthesis.

## 1. Triple-partite four-circuit normal form

Let `B,F` be disjoint label sets and `v` a further label.  Assume

\[
 B\cup F,\qquad B\cup\{v\},\qquad F\cup\{v\}
                       \in\mathcal F(P),                 \tag{3}
\]

but put `U=B union F union {v}` and assume `U notin mathcal F(P)`.
Let `mathcal K(B,F;v)` be all nonconvex four-subsets of `U`.

> **Theorem 1 (triple-partite circuit cover).**  The family `mathcal K` is
> nonempty.  Every `K in mathcal K` contains `v`, meets both `B` and `F`,
> and has one of the two splits (2).  In particular
> 
> \[
>  |\mathcal K|\le { |B|\choose2}|F|+|B|{|F|\choose2}. \tag{4}
> \]

**Proof.**  A nonconvex finite planar set has one point in the convex hull
of the others.  Caratheodory supplies three containing points, hence a
nonconvex four-subset.  A bad four-set avoiding `v` would be contained in
the first face in (3); one avoiding `F` or `B` would be contained in the
second or third.  It must therefore contain `v` and at least one label of
each other role.  The remaining fourth label gives exactly (2), and (4)
counts the possibilities.  QED.

Each `K` has exactly one hidden label.  At the role level there are only
six signed types: the two splits in (2), and in each split the hidden role
is `v`, `B`, or `F`.  Thus a disjoint circuit matching has a one-sixth
submatching of one common signed role type.  The actual witness labels can
be chosen canonically from `(B,F,v)`, so this normalization costs no
ambient `n^3` factor when those sets are retained by the context.

## 2. Exact guard-transversal release

Delete the common root `v` from every circuit and form the three-uniform
trace hypergraph

\[
       \mathcal H(B,F;v)=\{K-\{v\}:K\in\mathcal K(B,F;v)\}. \tag{5}
\]

Let `tau` be its transversal number and `nu` its matching number.

> **Theorem 2 (release equals circuit cover).**  For every
> `Z subseteq B union F`,
> 
> \[
>    U-Z\in\mathcal F(P)
>       \quad\Longleftrightarrow\quad
>    Z\cap H\ne\varnothing\quad\hbox{for every }H\in\mathcal H. \tag{6}
> \]
> 
> Moreover
> 
> \[
>                              \nu\le\tau\le3\nu.        \tag{7}
> \]

**Proof.**  If a trace `H` survives, its bad four-set `H union {v}`
survives, so `U-Z` is nonconvex.  Conversely, if `U-Z` is nonconvex,
Caratheodory supplies a bad four-subset of it; Theorem 1 puts its trace in
`mathcal H`, disjoint from `Z`.  This proves (6).

Every transversal meets every matching edge, so `nu<=tau`.  The union of
the edges in any maximal matching is a transversal: otherwise a disjoint
edge could be added.  A maximum matching therefore gives a transversal of
size `3nu`, proving the other inequality.  QED.

Choose canonically a minimum transversal `Z` and a maximum matching
`H_1,...,H_nu`.  Put

\[
 R=U-Z,\qquad S=H_1\mathbin{\dot\cup}\cdots
                    \mathbin{\dot\cup}H_\nu\subseteq B\cup F. \tag{8}
\]

The set `R` is an ordinary face containing `v`, and `S` is a subset of the
ordinary face `C=B union F`.  Consequently there are exactly

\[
        2^{|R|-1}=2^{r-\tau}\quad\hbox{ordinary subsets of `R` containing `v`,}
                                                               \tag{9}
\]

and `2^{3nu}` ordinary subsets of `S`.  By (7), `3nu>=tau`.

For a weighted cell family `Omega`, define `Lambda_root` as the maximum
total generating weight of one output in the first reservoir in (9), and
`Lambda_sh` analogously for one **nonempty** subset of `S`.  Exact incidence
counting gives

\[
 \sum_\omega w_\omega2^{r_\omega-\tau_\omega}
       \le\Lambda_{\rm root}V(P),                       \tag{10}
\]

on any selected root branch, and

\[
 \sum_\omega w_\omega(2^{3\nu_\omega}-1)
       \le\Lambda_{\rm sh}V(P)                          \tag{11}
\]

on any selected shield branch.  There is no decoder assertion hidden in
(10)--(11): all cross-context reuse is precisely in the displayed loads.

Splitting cells according to `tau<=r/2` gives the local dichotomy

\[
 \boxed{\text{rooted release of size at least }2^{r/2}
   \quad\hbox{or}\quad
   \text{detached shield of size at least }2^{r/2}-1.}   \tag{12}
\]

This can give a fixed-power multiplier when its actual global load is
subpower.  It does not by itself multiply a dense source row alphabet:
all records in one `(B,F,v)` column use the same two reservoirs.

## 3. Tangent-neighbor localization is false

Take

\[
\begin{aligned}
B&=\{(-5,1),(-1,11),(2,9),(11,1)\},\\
F&=\{x=(2,-10),z=(9,-4)\},\qquad v=(5,-6).             \tag{13}
\end{aligned}
\]

All three sets in (3) are strictly convex, while `U` is nonconvex.  In
`Q=B union {v}`, the tangent neighbors of `v` are

\[
                         (-5,1),\qquad(11,1).            \tag{14}
\]

Nevertheless

\[
                    \{(-1,11),x,z,v\}                   \tag{15}
\]

is a bad circuit: `v` lies strictly inside the triangle formed by the
other three labels.  It contains neither point in (14).  Thus even the
all-pairwise-convex hypothesis does not make the old insertion edge a
circuit guard.  Any tangent localization must use the **released** hull or
an additional canonical pocket condition.

For this example, the unique singleton transversal in (6) is `{x}`.
Deleting `x` makes `B union {z,v}` convex; deleting any other single label
does not release the full union.

## 4. A scalable same-edge anti-aligned rectangle

Keep `B,v` from (13).  For any `m`, choose small rational parameters and
points near

\[
             g_0=(0,-12),\qquad x_0=(2,-10),\qquad z_0=(9,-4). \tag{16}
\]

One explicit verifier family uses, for `1<=i,j<=m`,

\[
\begin{aligned}
t_i&={i\over10000m},&
 g_i&=(t_i,-12+3t_i+7t_i^2),\\
s_j&={j\over10000m},&
 x_j&=(2+s_j,-10+2s_j+3s_j^2),\\
&&z_j&=(9-2s_j,-4+s_j+5s_j^2).                         \tag{17}
\end{aligned}
\]

Put

\[
 A_i=B\cup\{g_i\},\quad F_j=\{x_j,z_j\},\quad
 C_j=B\cup F_j,\quad W_j=F_j\cup\{v\},\quad Q=B\cup\{v\}. \tag{18}
\]

For the exact checked family, and for arbitrary `m` after an arbitrarily
small generic rational perturbation within the same open cells:

* `A_i,C_j,W_j,Q` are ordinary faces for every `i,j`;
* `C_j union {v}` is nonconvex, with the fixed-role circuit
  `{(-1,11),x_j,z_j,v}` hiding `v`;
* `{x_j}` is the unique singleton circuit transversal, so
  `R_j=B union {z_j,v}` is the canonical release; but
* every cross union `B union {g_i,z_j,v}` is nonconvex; indeed `v` is
  caged again by the same-edge source ear and released column; and
* even `A_i union C_j` is nonconvex.

Thus the canonical circuit, its one-label guard, its released face, and
all four Hall targets fail to create the naive mixed source--release union.
The circuit is constant across each complete column fibre (as the source
row varies), so its canonical outer-triangle/release load is exactly `m`.

There are `m^2` actual marked records `(A_i,C_j)`.  They have one `Q`, `m`
source targets `A_i`, and `m` each of `C_j,W_j`.  For a subfamily meeting
`a` rows and `c` columns, its size is at most `ac` and its four-target union
has at least `a+2c+1` faces.  The ratio increases in both variables, hence

\[
                         \lambda_4={m^2\over3m+1}.       \tag{19}
\]

The pair `(A_i,C_j)` has load one and retains the actual row and column
marks.  More elementarily, `{g_i,x_j}` is a two-point ordinary face and
these `m^2` faces are distinct.  Therefore this construction is **not** a
counterexample to the desired global theorem.  It proves exactly that a
positive theorem must exploit low-load cross marks or higher child profile
entropy; neither tangent-neighbor localization nor the full released union
can replace that step.

The construction is open and projectively local.  Independent rational
order types can be embedded in sufficiently small neighborhoods of the
three centers in (16), followed by a generic perturbation.  This destroys
any claim that one local cloud must itself be a cap, while preserving all
displayed cell signs.  To become a genuine quadratic-entropy regression,
however, one would have to replace the singleton row/column marks by many
faces with highly reused projections.  That is the surviving
support-redundancy gate, not a consequence of the circuit tensor.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_pairwise_convex_triple_circuit_cover.py
```

Expected output:

```text
PASS: tangent counterexample circuits=6 tau=1 nu=1; rectangle m=7 records=49 hall4=49/22 circuit_load=7 release_load=7 mark_pair_load=1
```

The checker uses exact `Fraction` arithmetic.  It verifies all pairwise
convexity conditions, enumerates every bad four-circuit, checks the
triple-partite role split and the exact transversal/release equivalence,
computes `tau,nu`, confirms the non-tangent witness, and exhausts all 49
cells of the scalable rectangle including the failed mixed release.  It
also enumerates every record subfamily at the row/column-count level to
verify (19) exactly.
