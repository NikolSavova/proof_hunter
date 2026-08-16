# Circuit-transversal cubes and the central-layer barrier

**Date:** 2026-08-15.  All logarithms are base two and the empty convex
subset is counted.

## Verdict

There is an exact stability/container theorem beyond the complete-layer
union lift.  For a carrier cell, project every bad planar four-circuit of the
full carrier/core union onto the core.  Convex union outputs are **exactly**
the independent sets of this rank-at-most-four trace hypergraph.  If its
minimum transversal has size `tau`, deleting a canonical minimum transversal
releases a full cube of size `2^(s-tau)`.  These cubes have the same global
root/carrier decoder as the complete-layer bank, so

\[
 \boxed{
 \sum_c k_c\le
 \sqrt{L_JL_C\max_c{k_c^2\over m_c2^{s_c-\tau_c}}}\;V(P).}
                                                               \tag{1}
\]

Moreover, either `tau` is small and (1) pays, or the trace hypergraph has a
matching of at least `tau/4` disjoint bad-circuit traces.  This is the
strongest unconditional circuit-container dichotomy obtained here.

It does **not** close the central logarithmic bin.  There are two exact
obstructions.

1. An uncovered combinatorial four-trace need not be a bad circuit: delete
   guards from the complete layer of a convex oval and arbitrary four-traces
   become uncovered while the projected circuit hypergraph remains empty.
2. There is a scalable planar complete-middle-layer construction with
   `s=2r=Theta(log n)` in which the full `2^s` carrier cube is already
   available, but every nonempty core choice is incompatible with every
   retained internal completion.  Thus no larger carrier-local
   core-times-completion bank exists.  At the exact `(3k)` decoder scale its
   square factor is at least

   \[
                    {\binom{2r}{r}\over2^r}
                    =2^{r-o(r)},                            \tag{2}
   \]

   so it fails by a fixed power in the wrong direction.

The construction has only polynomial marked mass and is not a global
`Theta(V)` counterexample.  Consequently this report rules out a purely
local stability/uncovered-trace closure; it does not rule out a cross-fibre
prevalence theorem and does not prove EIC'.

## 1. Canonical carrier cells

Fix a cell determined by `(T,z,B)` as in
`COMPLETE_GUARD_LAYER_UNION_LIFT.md`:

* `T` is a marked root, `z in T`, and `e=T setminus {z}`;
* `B` has size at most `b`, contains `e`, excludes `z`, and is disjoint from
  the actual role-pocket `X_T`;
* `U` is a canonical core of size `s`, disjoint from `B union {z}`;
* `mathcal F subseteq {U choose r}` is a nonempty family of size `k`, and

  \[
                       A_R=B\cup\{z\}\cup R                \tag{3}
  \]

  is a convex marked source for every `R in mathcal F`;
* `X subseteq X_T`, `|X|=m`, is canonical and `B union {x}` is convex for
  every `x in X`.

Put

\[
                         Q=B\cup\{z\}\cup U.                \tag{4}
\]

For every bad four-subset `W subseteq Q`, record its nonempty core trace

\[
                         E(W)=W\cap U.                      \tag{5}
\]

Let `mathcal H` be the resulting trace hypergraph after duplicate traces are
removed.  It has edge rank at most four.  Its edges need not be four-sets:
the fixed carrier labels may occupy part of `W`.

## 2. Exact projected-circuit complex

> **Lemma 1 (projection identity).**  For every `D subseteq U`,
>
> \[
> B\cup\{z\}\cup D\text{ is convex}
> \quad\Longleftrightarrow\quad
> D\text{ contains no edge of }\mathcal H.                 \tag{6}
> \]

**Proof.**  If the left side is nonconvex, planar Caratheodory supplies a bad
four-subset `W` inside it.  Then `E(W) subseteq D`.  Conversely, if
`E(W) subseteq D`, all labels of `W setminus E(W)` already lie in
`B union {z}`, so `W` is a bad subset of the proposed output.  QED.

No trace is empty: otherwise the same `W` would lie in every nonempty source
(3).  Also every `R in mathcal F` is independent in `mathcal H`, by (3) and
(6).

Let `tau=\tau(mathcal H)` and choose the lexicographically first minimum
transversal `J` as canonical cell data.  Then `U setminus J` is independent,
so Lemma 1 gives the full **transversal cube**

\[
 \mathcal J_c=
 \{B\cup\{z\}\cup D:D\subseteq U\setminus J\},qquad
 |\mathcal J_c|=2^{s-\tau}.                                \tag{7}
\]

Since the complement of every source guard `R` is a transversal,

\[
                         \tau\le s-r.                       \tag{8}
\]

Equivalently, `s-tau` is the maximum size of a convex core extension of the
fixed carrier.  Thus (7) is the largest full subcube certified merely by
deleting core coordinates.

## 3. Exact global telescope

Let `q` bound the rank of outputs in (7); one may take
`q<=b+1+max_c(s_c-tau_c)`.  Define

\[
 L_J=3{q\choose3}\sum_{i=0}^{b-2}{q-3\choose i},
 \qquad L_C=n{b+1\choose2}.                                \tag{9}
\]

> **Theorem 2 (global circuit-transversal telescope).**  Equation (1)
> holds over any family of canonical cells.

**Proof.**  A transversal-cube output contains the full root.  Guess `T`
inside it, guess `z in T`, and guess the at most `b-2` carrier labels outside
`T`.  This recovers `(T,z,B)`, hence the cell, `mathcal H`, and its canonical
`J`.  This is exactly the decoder (9), with no guess for the transversal.

A completion output is decoded by guessing its retained root edge and the
missing root label; disjointness from the actual role-pocket then recovers
`x` and `B`.  Its overlap is at most `L_C`, as before.  Hence

\[
 \sum_c|\mathcal J_c|\le L_JV(P),\qquad
 \sum_c|\mathcal C_c|\le L_CV(P),                          \tag{10}
\]

where `|mathcal C_c|=m_c`.  Apply Cauchy to
`k_c^2<=K|mathcal J_c||mathcal C_c|`, with
`K=max_c k_c^2/(m_c2^{s_c-tau_c})`.  QED.

On `b=O(L)`, `r=Theta(L)`, `m>=n/polylog(n)`, a sufficient fixed-power
condition is

\[
 s-\tau-2r\log(es/r)
 -O\!\left(b\log{e(s-\tau+b)\over b}\right)
 \ge\eta L.                                                \tag{11}
\]

This retains the explicit `(3k)` root/carrier loss.  It never spends one copy
of `V` per transversal, core, carrier, or root.

## 4. Small transversal or disjoint bad traces

> **Lemma 3 (rank-four matching alternative).**  If `nu` is the maximum
> matching size of `mathcal H`, then
>
> \[
>                              \tau\le4\nu.                 \tag{12}
> \]

**Proof.**  Take a maximal matching.  The union of its edges has at most
`4nu` vertices and meets every edge of `mathcal H`, since an edge disjoint
from that union would enlarge the matching.  QED.

Thus failure of the transversal-cube branch with `tau=Omega(L)` supplies
`Omega(L)` pairwise disjoint **geometric** bad-circuit traces.  This is
strictly stronger than disjoint uncovered members of `{U choose 4}`.
However, the corresponding four-circuits may share all their fixed carrier
labels and may be joined by further cross-circuits.  Equation (12) alone does
not make them private or recoverably toggleable; the common-cage regression
from `PREVALENCE_COMMON_CAGE_REGRESSION.md` remains applicable.  A second
bank needs additional separability beyond matching.

## 5. Why uncovered four-traces are insufficient

Suppose `Q` itself is convex.  Then `mathcal H` is empty and every one of the
`2^s` carrier/core subsets is a face, regardless of which source guards were
retained in `mathcal F`.  Starting with the complete `r`-layer and deleting
all guards containing a fixed four-set `E` makes `E` uncovered and leaves

\[
 |\mathcal F|={s\choose r}-{s-4\choose r-4},                \tag{13}
\]

yet produces no bad circuit at all.  Therefore the density threshold in the
complete-layer report is a sufficient route to convexity, not a converse or
a stability description of geometric circuits.

The verifier gives the sharp finite version: on an eight-label convex core
at rank four, delete just the guard `E` itself.  The layer has 69 of its 70
members, `E` is uncovered, and the entire carrier/core union remains convex.

## 6. Scalable central-layer separation regression

The following construction shows that even the maximum possible core cube
need not mix with the internal completion alphabet.

Let

\[
 p(t)=(t,1-t^2),\quad a=p(-1),\quad b=p(1),\quad z=p(0),    \tag{14}
\]

and choose `s` distinct rational parameters
`t_i in [-1/2,1/2] setminus {0}`.  Put

\[
 B=\{a,b\},\quad T=\{a,b,z\},\quad
 U=\{p(t_1),\ldots,p(t_s)\}.                               \tag{15}
\]

All labels in `B union {z} union U` are in convex position on the strictly
concave parabola, and `ab` is an edge.  Hence for every
`R in {U choose r}`, the source `T union R` is convex and `T` is canonical.

For `u=(t,1-t^2)` with `|t|<=1/2`, the horizontal section of triangle
`abu` at height `y` is

\[
 \left[-1+{(t+1)y\over1-t^2},
        1+{(t-1)y\over1-t^2}\right].                       \tag{16}
\]

It contains the fixed open rectangle

\[
                    \Omega=(-1/2,1/2)\times(0,1/8).        \tag{17}
\]

The same holds for triangle `abz`.  Choose any general-position rational
point set `X subset Omega`.  Then every `x in X` is interior to every
triangle `abz` and `abu`.  Consequently

* `T union {x}` is nonconvex, so `x` is an actual root-pocket label;
* `B union {x}` is a convex completion face;
* for every nonempty `D subseteq U` and every nonempty completion face
  `F` retaining `B` and meeting `X`, the set `B union D union F` contains a
  bad four-subset `{a,b,u,x}` and is nonconvex.

Thus the core bank and internal bank are completely separated once the
actual carrier is retained.  This remains true if `X` is a shrunk copy of a
low-convex-rank order type, so the whole configuration may have maximum face
rank `O(log n)` when `s=O(log n)`.

Take `s=2r`.  The complete layer has

\[
              k={2r\choose r},\qquad |\mathcal J|=2^{2r},  \tag{18}
\]

and no carrier-local union bank can exceed `2^(2r)`.  At the global decoder
scale (9), `L_C/m>=1` and `L_J>=1`, so the factor in (1) is at least (2).
For `r=gamma L+O(1)`, Stirling gives `2^{r-o(r)}=n^{gamma-o(1)}`.  The full
cube therefore fails to meet the square demand, and the geometric separation
forbids repairing it by multiplying with a retained pocket face.

This is a scalable **local** planar regression.  Its marked source mass is
only `binom(2r,r)=n^{O(1)}`; it does not realize the `Theta(V)` weighted mass
required for a global counterexample.  A proof can still succeed by showing
that quadratically many such carrier cells cannot coexist without a new
cross-fibre face bank.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_circuit_transversal_central_barrier.py
```

The exact rational verifier has two parts.  First it constructs an actual
marked cell with a nonempty projected circuit hypergraph and checks (6) on
all 64 core subsets, obtaining 43 convex outputs, `tau=2`, maximum matching
two, and maximum independent rank four.  Second it checks the parabola
regression at `s=8`, `r=4`, `m=5`: 70 complete-middle-layer sources, all 256
core-cube faces, no mixed carrier/core/completion face, and a 69-member
non-four-covering sublayer whose geometric circuit hypergraph is empty.

