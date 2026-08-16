# Common-guard replication reduces to the heterogeneous cap--cup ramp

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The parabola blocker can be replicated with arbitrary projective child
order types behind one fixed guard edge.  This gives an exact planar wrapper
in which

1. every guard-retaining singleton transversal is ordinary;
2. every guard-retaining trace using two labels from one child is
   nonconvex; and
3. after deleting the guards, the entire face count is the standard
   heterogeneous first-cap/last-cup recurrence.

The recurrence does **not** force coefficient one half from scalar child
data.  There is an exact cap/cup ramp for which its normalized max-plus
value stays at `max(alpha,c)`.  At the live formal values
`alpha=c=1/4`, it stays at `1/4`, not `1/2`.

This is an applicability barrier, not a new planar upper construction.
Realizing the ramp requires a sequence of `D`-point children whose full
face counts are already below coefficient one half and whose cap/cup mass
is graded across `Theta(log D)` distinct slopes.  The known stationary,
periodic, finite-menu, and small-step projective children have coefficient
at least one half before entering the wrapper.  Thus a genuine sub-half
realization would already solve the open heterogeneous Baek--Balko
cap/cup-alignment problem.  The guard construction does not create that
missing child.

This also gives the precise aggregate-circuit interpretation.  The two
guard endpoints are a common size-two hitting set for all same-child bad
circuits.  Deleting them releases the linear cap/cup composition.  A large
matching of external traces is exactly a forward term `C_iU_j`; the ramp
shows that same-block products `C_iU_i` do not force those forward terms to
gain a quadratic coefficient.

## 1. Exact planar common-guard wrapper

Let `u,v,z_1,...,z_q` be the vertices, in this order, of a strictly convex
polygonal chain closed by the chord `uv`.  At macro vertex `z_i`, place an
arbitrary finite planar order type `Q_i` in a sufficiently small
neighbourhood.  Use the projective nesting map from
`DETACHED_RADIAL_LEXICOGRAPHIC_PROFILE.md`, Theorem 1, with the **common**
edge `uv`.  It makes the image `X_i` totally ordered by

\[
 x\prec_i y\quad\Longrightarrow\quad
 x\in\operatorname{int}\operatorname{conv}\{u,v,y\}.    \tag{1}
\]

The image may be arbitrarily small and preserves the labelled order type
of `Q_i`.  Choose the neighbourhoods small enough that all triples meeting
distinct blocks have the fixed macro strong-glue signs.  These are finitely
many strict inequalities, so the construction has a rational realization.

For an explicit compatibility normalization, send `u,v` to `(-1,0)` and
`(1,0)` and use the positive pocket coordinates `(L,R)` from that nesting
theorem.  Choose the macro `z_i` on a generic rational strictly convex
antichain, with `L(z_i)` increasing and `R(z_i)` decreasing.  Inside block
`i` use

\[
 L=L(z_i)+\varepsilon f+\varepsilon^2g,\qquad
 R=R(z_i)+\varepsilon f-\varepsilon^2g,                 \tag{1a}
\]

where `(f,g)` is an affine chart of `Q_i`.  The common first-order `f`
increment gives total guard nesting; the transverse second-order `g` term
preserves the child order type.  The antichain order gives the standard
left/right mixed signs.  This simultaneously proves nesting and vertical
strong glue, rather than assuming two unrelated small-perturbation limits.

> **Theorem 1 (common-guard projective wrapper).**  The wrapper can be
> chosen so that:
>
> * every set `\{u,v,x_1,...,x_q\}`, `x_i in X_i`, is ordinary;
> * an ordinary set containing both `u,v` meets every `X_i` in at most one
>   point; and
> * writing `n_i=|X_i|`, and `C_i,U_i,W_i` for the nonempty cap, cup, and
>   ordinary-face counts in the actual rooted chart, the total nonempty
>   face count is exactly
>
> \[
> \boxed{
> W(P)=\sum_{i=0}^{q+1}W_i+
>   \sum_{0\le i<j\le q+1}C_iU_j
>       \prod_{i<k<j}(1+n_k),}                           \tag{2}
> \]
>
> where the endpoint guard blocks have
> `n_0=n_(q+1)=C_0=U_0=W_0=C_(q+1)=U_(q+1)=W_(q+1)=1`.

The first claim is stability of the convex macro chain.  The nesting map is
chosen anisotropically: its first-order displacement is the common nesting
functional and its transverse displacement is second order.  Hence every
mixed triple with two labels in one block has the usual vertical
strong-glue sign, while triples in three blocks have the macro sign.  The
second claim follows from (1): among two selected points in one child, the
inner lies in the triangle formed by the outer point and the guards.  For (2), classify a
multi-block face by its first and last occupied blocks.  Its first trace is
a cap, its last trace is a cup, and every intermediate occupied block is a
singleton.  Conversely the strong-glue orientation rules make every such
choice ordinary.  The block traces recover the choice, so (2) is an
equality.

Thus the common-base source layer has size

\[
                         M=\prod_{i=1}^qn_i,             \tag{3}
\]

but the fixed guard destroys every attempt to multiply `M` by a
multi-point local face.  Deleting the guard edge loses no hidden history;
it exposes exactly (2).

## 2. Exact max-plus optimization

Take equal child sizes `n_i=D`, put `L=log D`, and let

\[
                         q=(\alpha+o(1))L.               \tag{4}
\]

Suppose at quadratic scale a child has

\[
 {\log C_i\over L^2}=x_i+o(1),\qquad
 {\log U_i\over L^2}=c-x_i+o(1),\qquad 0\le x_i\le c.   \tag{5}
\]

Write `t_i=i/L` and `y_i=x_i-t_i`.  The terms in (2) have normalized
exponents

\[
\begin{array}{c|c}
\text{term}&L^{-2}\log(\text{term})\\ \hline
X_i\text{ to }X_j, i<j&c+y_i-y_j+o(1),\\
u\text{ to }X_j&c-y_j+o(1),\\
X_i\text{ to }v&\alpha+y_i+o(1),\\
u\text{ to }v&\alpha+o(1).
\end{array}                                             \tag{6}
\]

If `c>=alpha`, choose

\[
                 x_i=t_i+{c-\alpha\over2}.               \tag{7}
\]

Then every `y_i` is the same, (5) remains feasible, all cross-child terms
have exponent `c`, and the two guard terms have exponent
`(c+alpha)/2`.  Including the unavoidable local and source banks gives

\[
 \boxed{
 \inf_{(x_i)}\max\{\text{scalar exponents visible in (2)}\}
       =\max\{c,\alpha\}\quad(c\ge\alpha).}              \tag{8}
\]

The lower bound is immediate from the local child bank and the guard-to-
guard source product.  Equation (7) proves the matching upper value for
the scalar recurrence.  In particular `c=alpha=1/4` has `x_i=t_i` and
value exactly `1/4`.

## 3. Finite integral ramp

The asymptotic obstruction has an exact integer form which respects the
unavoidable singleton/pair baseline.  Let `D=2^L`, `q=floor(L/4)`, index
the children by `i=0,...,q-1`, and prescribe

\[
        C_i=D^{i+2},\qquad U_i=D^{q+1-i},\qquad
        W_i=C_i+U_i.                                    \tag{9}
\]

Then

\[
                   C_iU_i=D^{q+3}                       \tag{10}
\]

in every child, while every forward term in (2) satisfies

\[
 C_iU_j(1+D)^{j-i-1}le2D^{q+2}qquad(i<j),              \tag{11}
\]

for `q<=D/2`.  Each one-guard term is at most `2D^{q+1}`, and the pure source
term is `(1+D)^q<=2D^q`.  Therefore the scalar recurrence obeys

\[
       D^q\le W(P)\le 4(q+2)^2D^{q+3},                  \tag{12}
\]

so

\[
             {\log W(P)\over L^2}={q\over L}+o(1)
                       ={1\over4}+o(1).                  \tag{13}
\]

This is the same directional ramp as the scalar obstruction in
`agent_all_interval_isoperimetry/REPORT.md`, now placed exactly inside the
common-guard root-bad wrapper.

## 4. Why this is not yet a planar sub-half construction

Numbers (9) satisfy the elementary scalar constraints

\[
 C_i,U_i\le W_i,qquad C_iU_i=D^{q+3},                   \tag{14}
\]

but no theorem currently realizes the whole ramp by `D`-point order types
with the asserted `W_i` simultaneously.  This is the load-bearing issue.

For a stationary or small-step lexicographic child, the exact cap/cup
recurrences and the cap--cup theorem give child coefficient at least one
half; see `agent_asymptotic/NEW_HALF_AUDIT.md`.  Such a child makes
`c>=1/2` before wrapping, and (8) is at least `1/2`.  A planar realization
of (9) with `c=1/4` would therefore have to be a rapidly heterogeneous
primitive family outside all currently controlled constructions.  It is
equivalent in difficulty to the known unrestricted forward cap/cup
anti-alignment loophole, not a consequence of projective nesting.

Hence the construction audit is:

* **exact planar:** common guard, arbitrary child order types, source layer,
  circuit suppression, and recurrence (2);
* **exact scalar:** coefficient-`1/4` ramp (9)--(13);
* **not established:** a planar family of children realizing that ramp with
  full face counts below one half.

There is also an unconditional fixed-point barrier which survives arbitrary
nonvertical/projective substitutions.

> **Theorem 2 (ambient-child fixed-point barrier).**  Let a parent `P_N`
> be obtained from `q_N=N^{o(1)}` disjoint nonempty child blocks (and
> `N^{o(1)}` additional anchors) by any planar placement or projective
> substitutions.  Some child `Q_N` has
> `|Q_N|>=(N-N^{o(1)})/q_N`.  If every such macroscopic child available to the
> construction satisfies
> 
> \[
>       \log V(Q_N)\ge(1/2-o(1))(\log|Q_N|)^2,            \tag{15}
> \]
> 
> then
> 
> \[
>       \log V(P_N)\ge(1/2-o(1))(\log N)^2.              \tag{16}
> \]

Indeed every ordinary subset of a child remains an ordinary subset of the
parent, so `V(P_N)>=V(Q_N)`.  Also
`log|Q_N|>=log N-log q_N-o(1)=(1-o(1))log N`.  No seam orientation, blocker, or
projective map can erase this ambient local bank.

Thus the common-guard wrapper cannot recursively turn the known
coefficient-half projective children into a sub-half family.  A sub-half
realization of the ramp must import a macroscopic primitive child which is
already sub-half.  In this exact sense the proposed construction is
circular: it relocates the open upper-construction problem into a child; it
does not solve it.

## 5. Consequence for the aggregate blocker graph

The guard wrapper is the extremal small-transversal branch.  Its canonical
same-child nesting circuits all contain both `u,v`, so their external-role
transversal number is two.  Deleting those guards reduces the problem to
the forward interval terms in (2).

In the complementary large-matching branch, each disjoint external circuit
trace supplies a potential cut/interval.  Formula (6) shows what a valid
weighted theorem must retain: the signed endpoint state `y_i`, not only the
same-block energy `C_iU_i`.  Any matching/container bound which forgets
that state admits the constant-slope ramp (7) and cannot improve the
quarter coefficient.

Thus the precise next positive target is a **planar profile-reset theorem**:
either the circuit matching forces a decrease in the slope `y_i`, creating
a forward term larger than (6), or a child with large `W_i` pays locally.
This is stronger than a role-hitting-set dichotomy and is exactly the
history coordinate absent from the failed strong-separation argument.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_common_guard_profile_ramp.py
```

The verifier first constructs an exact rational three-child, four-label
wrapper from (1a).  It checks all 64 guard-retaining transversals, all 18
same-child nesting pairs, and all `2^14` subsets; the brute face count
`1914` equals (2).  It then checks the finite recurrence and bounds
(9)--(13) with exact integers for `16<=L<=160`, exhaustively audits the
max-plus identity (8) on a discrete grid for small `q`, and checks the
finite ambient-child inequality behind (15)--(16).
