# Global Ferrers rectangle--shield telescope and the exact overlap residue

**Date:** 2026-08-15.  All logarithms are base two and the empty convex
subset is counted.

## Verdict

The diagonal, quadratic-source-entropy branch does not collapse from local
Ferrers structure alone.  There is, however, an exact global one-face
telescope.  Its load is the minimal missing invariant.

Give a canonical rectangle cell `c` selected demand `m_c` and a nonempty
ordinary-face target bank `B_c`.  Define its uniform normalized shield load

\[
 \Lambda_{\rm unif}=
   \max_F\sum_{c:F\in\mathcal B_c}{m_c\over|\mathcal B_c|}.          \tag{1}
\]

Then

\[
                       \boxed{\sum_cm_c\le
                              \Lambda_{\rm unif}V(P).}      \tag{2}
\]

More sharply, allow every cell to split its demand arbitrarily among all of
its available blocker, outer-shield, Ferrers, forward, and one-gap targets.
The least possible maximum face load is

\[
 \lambda_*=min_{a_{cF}\ge0}
       \max_F\sum_ca_{cF},
 \qquad
 \sum_{F\in\mathcal B_c}a_{cF}=m_c.                       \tag{3}
\]

It has the exact dual formula

\[
 \boxed{\displaystyle
 \lambda_*=max_{\substack{\mu_F\ge0\\\sum_F\mu_F=1}}
       \sum_cm_c\min_{F\in\mathcal B_c}\mu_F.}            \tag{4}
\]

Equivalently, fractional Hall gives the purely combinatorial formula

\[
 \boxed{\displaystyle
 \lambda_*=\max_{\varnothing\ne\mathcal A\subseteq\mathcal C}
 {\sum_{c\in\mathcal A}m_c\over
  |\bigcup_{c\in\mathcal A}\mathcal B_c|}.}               \tag{4a}
\]

Thus `lambda_*<=D^(1-epsilon)` is precisely the desired global
rectangle-or-shield charge.  Failure produces an actual subfamily whose
total available face union is too small for its demand; dually, it produces
a single global face-price measure under which **every** available target
in the energetic cells is expensive.  Maximum raw overlap, pair decoder
load, and local bank size are all weaker than (3)--(4a).

This invariant passes both mandatory regressions.

* One three-arc carrier--root rectangle has only `2^O(r)` rank-`r` sources.
  At a fixed-power cap `D=n^(delta+o(1))`, the actual blocker alphabet has
  `2^{Omega((log D)^2)}` detached faces and makes `lambda_*` fixed-power
  small.  Therefore a hard family needs
  `2^{Omega((log D)^2)}` genuinely different rectangle contexts.
* The complete-core `MARK_C4` tensor is also automatically discharged.  If
  its upper core has subpower label size, its source support is
  subquadratic and the blocker shield pays.  If the core has fixed-power
  label size, the hypothesis that all uniform core choices are faces forces
  the whole core to be convex by planar four-locality; its Boolean shield
  then overwhelms the selected tensor.  Hence it cannot be a
  `Theta(V)`-mass fixed-power regression.

The coefficient-scale composition theorem does not remove the remaining
overlap.  At its outermost decomposition, an arbitrary-cluster three-arc
realization has only three macro positions, so its scale split has
`alpha=0`, `beta=1` in upper-jump equation (32a) and gives no strict
coefficient rise.  Oppositely oriented child clusters can attain the
known cap/cup anti-alignment at one cut.  A recoverable cycle of
`Theta(log n)` containers is paid instead by the cyclic one-gap/profile
identity; without that recoverable containerization, the hypotheses of the
composition theorem are absent.

No planar `Theta(V)`-mass regression for (3) was found.  Such a regression
must have quadratic many rectangle-context bits, high fractional reuse of
*all* blocker/outer/Ferrers/one-gap banks, no recoverable cyclic container,
and no macroscopic comparable-regeneration core.  This is strictly sharper
than “high diagonal energy.”

## 1. Exact fractional Carleson telescope

Let `mathcal V` be the ordinary convex-face family, `|mathcal V|=V`.  A
cell `c` has nonnegative demand `m_c` and an admissible target set
`emptyset != mathcal B_c subseteq mathcal V`.  The targets may be the union
of several geometric banks.  A **fractional routing** is a family
`a_(c,F)>=0`, supported on `F in mathcal B_c`, with

\[
                         \sum_{F\in\mathcal B_c}a_(c,F)=m_c.           \tag{5}
\]

> **Theorem 1 (global fractional rectangle--shield telescope).**
> Equations (2)--(4a) hold.  In particular,
> 
> \[
>                         \sum_cm_c\le\lambda_*V(P).       \tag{6}
> \]

**Proof.**  Uniform routing
`a_(c,F)=m_c/|mathcal B_c|` gives (1)--(2).  For an arbitrary routing,

\[
 \sum_cm_c=\sum_F\sum_ca_(c,F)
       \le V\max_F\sum_ca_(c,F),                           \tag{7}
\]

which proves (6) after minimizing.

For completeness, dualize (3).  Give the face-load inequalities
nonnegative multipliers `mu_F` and normalize `sum_Fmu_F=1` using the
coefficient of the objective.  The multiplier of `a_(c,F)` is nonnegative
exactly when the cell dual variable is at most `mu_F` for every
`F in mathcal B_c`.  Its largest allowed value is therefore
`min_(F in mathcal B_c)mu_F`.  Finite-dimensional linear-programming
duality gives (4).

There is also a useful integral-looking form of the same LP.  Fix a proposed
load `lambda` and make a flow network: the source sends `m_c` to every cell,
every cell is joined with infinite capacity to each face in its bank, and
each face sends capacity `lambda` to the sink.  Max-flow/min-cut says that
all demand can be routed exactly when

\[
       \sum_{c\in\mathcal A}m_c
       \le\lambda\left|\bigcup_{c\in\mathcal A}\mathcal B_c\right|
       \quad\hbox{for every }\mathcal A\subseteq\mathcal C.          \tag{7a}
\]

Minimizing `lambda` proves (4a).  QED.

Consequently the missing planar statement
can be phrased without a routing: **every** subfamily of live rectangles
must expand into enough distinct faces across the union of all its banks.

For a full selected cap, take `m_c=Dw_c`, where `w_c` is the number of
underlying source records canonically assigned to the cell.  If sources may
carry at most `A=O(r)` canonical root marks, proving (6) for marked demand
loses only the harmless factor `A=n^o(1)`.  Therefore the live target is

\[
                         \lambda_*\le n^{o(1)}D^{1-\epsilon}.          \tag{8}
\]

The dual is a useful exact high-overlap localization.  If (8) fails, there
is a probability distribution `mu` on actual ordinary faces such that the
weighted sum of the cheapest target price in every live bank exceeds the
right side.  Hence failure cannot be blamed on choosing the wrong one of
the blocker, outer, Ferrers, or one-gap banks: they are simultaneously
expensive under the same `mu`.

This weighted bank expansion is the minimal one-face invariant.  The pair statement

\[
 \sum_c|\mathcal S_c||\mathcal B_c|\le L V(P)^2           \tag{9}
\]

for a source bank `mathcal S_c`, even with `L=1`, does not bound
`lambda_*`.  Perpendicular reuse can make the source coordinate identify
the carrier and the shield coordinate identify the root while every
ordered pair remains injective.  The four-local carrier--root rectangle and
the actual three-arc realization both exhibit this pattern.

## 2. What planar Ferrers structure contributes

For fixed blocker/root data `(x,z)`, let carrier edge `uv` be admissible
when

\[
                         x\in\operatorname{int}\triangle(u,v,z).     \tag{10}
\]

After the affine normalization `x=(0,0)`, `z=(0,1)`, write
`u=(-a,b)`, `v=(c,d)`, `a,c>0`.  The exact test is

\[
                         {b\over a}+{d\over c}<0.           \tag{11}
\]

Thus admissible carriers form a bipartite Ferrers graph.  If it has `m`
edges and the smaller side has size `s`, sorting its row degrees
`d_1>=...>=d_s` gives a complete rectangle of area

\[
             \max_i i d_i\ge {m\over H_s},
             \qquad H_s=\sum_{i=1}^s{1\over i}.            \tag{12}
\]

This loses only `O(log n)` and therefore preserves both fixed-power and
coefficient-scale mass.  It rules out the nonbipartite all-pairs carrier
axis of the formal four-local model.

It does **not** rule out the square obstruction.  Three small circular arcs
around a triangle realize the complete bipartite case in (12): every
left--right carrier and every upper root contains the common blocker in its
root triangle.  Completion faces vary with the carrier, while marked
halfplane faces vary with the root.  The ordered pair decoder has only the
root-mark load, but all rectangles may reuse the same untagged shields.
Accordingly, Ferrers extraction supplies an available bank to (3); it gives
no universal upper bound on its global load.

## 3. Exact test on the three-arc rectangle

Use carrier pools of sizes `l,r`, `g` root blocks of size `p=2h+1`, and a
common selected alphabet of size `D`.  The number of distinct underlying
middle-layer sources is

\[
                         s_0=lr g{p\choose h+1}.            \tag{13}
\]

Every source has the full selected degree `D`.  The natural realization has
two detached banks:

\[
 H_X=V(P|X)\ge f(D),qquad
 H_O=2^{l+r+gp},                                          \tag{14}
\]

where `H_O` is the Boolean complex of the three outer arcs.  For one
rectangle context, fractional routing over their union gives

\[
 \lambda_*\le {Ds_0\over H_X+H_O-1}.                     \tag{15}
\]

More generally, the uniform choices separately give
`Ds_0/H_X` and `Ds_0/H_O`.

On the live rank cutoff, `h<=r_source=O(log n)` and `l,r,gp<=n`.  Hence

\[
                         \log s_0=O(\log n).               \tag{16}
\]

If `D=n^(delta+o(1))`, the established reservoir bound gives

\[
                         \log H_X=Omega((\log n)^2).        \tag{17}
\]

Equations (15)--(17) discharge one three-arc rectangle with much more than
a fixed power.  In particular, the arbitrary order type inserted in the
small blocker disk is harmless; its universal induced face complex is the
bank `H_X`.

Suppose instead a hard selected family is covered by `C` such contexts.
Since every context supplies only `2^O(log n)` sources, quadratic source
entropy forces

\[
                         \log C=Omega((\log D)^2).          \tag{18}
\]

The same `H_X` and the same outer shield may be reused in all `C` contexts,
so applying (15) context by context would spend `V` `C` times.  The global
quantity (4a), not the local counts (14), measures whether every subfamily
of contexts has enough distinct outer/Ferrers/one-gap targets.  This is the
precise overlap gap.

## 4. The complete-core MARK_C4 tensor cannot be hard

Consider the full tensor from `MARK_C4_ROOT_CIRCUIT.md`.  Let `K` be its
`k`-label upper core, use every `t`-subset as a retained core, let `a` be
the hidden singleton alphabet, and let the selected repair alphabet have
size `D`.  The source support and selected demand are

\[
                         s=a{k\choose t},qquad M=Ds.       \tag{19}
\]

The construction takes `K` in convex position.  This Boolean shield is in
fact forced if all `t`-subsets are source faces and `t>=4`: every four-set
of `K` extends to a used `t`-set and is convex, so planar four-locality makes
`K` itself convex.  Therefore

\[
             V(P)\ge\max\left\{s,2^k,f(D)\right\}.         \tag{20}
\]

> **Proposition 2 (full MARK tensor discharge).**  Suppose source rank
> `t+O(1)=O(log n)` and `D=n^(delta+o(1))` for fixed `delta>0`.  For every
> sufficiently small fixed `epsilon>0`, (19) satisfies
> 
> \[
>                         M\le D^{1-\epsilon}V(P).          \tag{21}
> \]

**Proof.**  Put `L=log n`.  Fix a small constant `eta>0`.  If
`log k<=eta L`, then

\[
 \log s\le L+O(L)\log(ek/t)
          \le(O(eta)+o(1))L^2.                            \tag{22}
\]

Choose `eta` and then `epsilon` so that (22) is below
`log f(D)-epsilon log D`; the source--alphabet discharge proves (21).

If `log k>eta L`, then `k>n^eta`.  On the other hand

\[
                         \log M=O(L^2),                    \tag{23}
\]

because `a,D,k<=n` and `t=O(L)`.  The Boolean bank `2^k` is
`2^{n^eta}`, which dominates `M D^epsilon`.  Equation (20) again proves
(21).  QED.

Thus every parameter scaling of the literal full tensor takes one of the
two already-paid branches.  Restricting the upper cores to a sparse
quadratic-entropy subfamily avoids the forced Boolean shield, but then it is
no longer the full `MARK_C4` tensor; it is precisely the global varying-core
problem measured by (3).

## 5. Coefficient-scale composition audit

The fixed-point inequality (32a) from `agent_upper_jump/REPORT.md` is

\[
 c_{out}\ge c+(1-2c)\alpha\beta.                          \tag{24}
\]

It needs a scale-covering induced macro core with
`log|I|=(alpha+o(1))L`, comparable child log-size
`(beta+o(1))L`, and the required count/mean or common-skew profile.

At the outermost decomposition, an arbitrary-cluster three-arc embedding
has only three macro positions.
Hence `log|I|=O(1)=o(L)`, so `alpha=0`, `beta=1`, and (24) gives only
`c_out>=c`.  It does not supply a strict rise.  If one of the arcs itself
admits a scale-covering family of comparable subclusters, the theorem can
instead be applied recursively there; the three-arc incidence conditions
alone do not force such a family.  This is not a technical
loss: orient one child all-cup and the next all-cap.  At that cut the
spanning endpoint product is the polynomial `D(m)^2` from the exact
anti-aligned example in Section 8.1 of the upper-jump report, even though
both child face counts are exponential.  An arbitrary projective-universal
cluster can carry the same one-cut imbalance.

Around a **recoverable cycle**, anti-alignment cannot occur at every gap.
The exact identity

\[
 \prod_i{B_i\over P_0}
       =\prod_i{A_iR_i\over L_i^3}
       \ge\prod_i{V(X_i)\over L_i^3}                      \tag{25}
\]

from the radial one-gap theorem forces one large cyclic shield bank.  For
quadratic source entropy and `q=O(log D)`, its gain is superpolynomial in
`D`.  This pays both the three-arc generalization and the radial
`MARK_C4`/repair-star regressions whenever their cyclic container list is
recoverable.

Consequently the composition audit gives a clean split, not a closure:

* macroscopic comparable regeneration rises by (24);
* recoverable many-container radial regeneration pays by (25);
* a constant-macro arbitrary-cluster embedding can remain anti-aligned and
  is coefficient-equivalent to its child.

The last case cannot carry the hard quadratic source entropy without
quadratically many globally varying contexts.  Controlling the common
targets of those contexts is exactly (3)--(4a).

## 6. Exact remaining overlap invariant

For the live family, give every canonical context all presently proved
target banks:

1. faces of its actual selected blocker alphabet;
2. its Ferrers biclique completions and forward two-ended outputs;
3. its root-marked halfplane bank;
4. its unrestricted outer shield;
5. any recoverable cyclic one-gap/profile bank; and
6. its source/top anchor faces.

Let `mathcal B_c` be their union and calculate `lambda_*` from (3), or
equivalently test the weighted expansion ratios in (4a).  The remaining
theorem is exactly

\[
                         \lambda_*\le n^{o(1)}D^{1-\epsilon}.          \tag{26}
\]

All known planar regressions satisfy (26): the three-arc and complete
`MARK_C4` tensors by Sections 3--4, and the radial product by (25).  The
formal four-local carrier--root rectangle can violate it only because it
suppresses the planar shield/profile banks by declaration.

If (26) is false in a planar system, (4a) supplies a concrete subfamily
whose entire target union is too small, while duality (4) supplies a common
price measure witnessing simultaneous high reuse of every listed bank.
This is the minimal exact obstruction.  A maximum pointwise overlap is not enough:
different banks can have their maxima on disjoint subfamilies, whereas one
dual measure certifies their joint failure without an unjustified common
pigeonhole.

No scalable planar family with selected mass
`M>D^(1-epsilon)V(P)` and bounded source rank was found.  Constructing one
would require a quadratic-entropy sparse core family whose varying contexts
erase every cyclic/container address while their blocker, outer, forward,
and one-gap target unions all remain small under the same dual measure.
This is a sharper target than another local rectangle or circuit theorem.

## 7. Verification artifact

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_global_ferrers_shield_telescope.py
```

The exact checker verifies the uniform telescope, the weighted Hall formula,
and matching primal/dual certificates for overlapping banks, the Ferrers threshold and harmonic
biclique estimate on rational carrier data, the finite three-arc normalized
loads, the root-mark multiplicity, and the complete-core/Boolean-shield
alternatives on a range of exact parameters.  The rational-coordinate
realization of the three-arc rectangle itself is independently checked by
`verify_external_alphabet_energy_trichotomy.py` in the same directory.
