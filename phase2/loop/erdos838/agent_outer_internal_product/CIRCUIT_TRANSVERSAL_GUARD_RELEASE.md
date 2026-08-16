# Erdős 838: circuit transversals give an exact guard-release branch

**Date:** 2026-08-14.  All logarithms are base two.

## Verdict

After one-pocket localization there is an exact cover-or-toggle theorem for
the outer traces of the planar four-circuits.

* If a set `G` of outer guards meets every bad outer trace, then deleting
  `G` makes the carrier compatible with the **entire** internal face
  reservoir.  No further geometric hypothesis is needed.
* If the trace clutter has a matching of `k` disjoint traces, then the
  source extensions have a Boolean toggle bank of exactly `D 2^k`
  ordinary faces.
* Since every trace has size one or two, a maximum matching supplies both
  alternatives at once: the union of its traces is a transversal of size
  at most `2k`.

This gives a fixed-power EIC' corollary.  If `tau_c<=t`, where `tau_c` is
the minimum trace-transversal size, release a minimum transversal.  The
output recovers the internal face and the released carrier; guessing the
at-most-`t` deleted labels gives overlap at most
`S_t(n)=sum_(i<=t)binom(n,i)`.  Using the carrier itself as the other bank
gives the sharp entropy-powered estimate

\[
       |E_{\tau\le t}|\le
       D^2\sqrt{{S_t(n)\over H}}\,V(P).                     \tag{S1}
\]

Here `H` is the common internal face reservoir.  The factor `D^4/H` in the
cell square inequality is allowed to be smaller than one; retaining it is
what makes (S1) much stronger than the earlier `D^3/2` threshold.

If `tau_c>t`, the rank-two matching-cover relation forces a matching of
`k_0=floor(t/2)+1` disjoint traces.  If the resulting toggle banks have
overlap `L_T`, the two branches combine to

\[
 |E|\le\left(
 D^2\sqrt{{S_t(n)\over H}}+L_TD2^{-k_0}\right)V(P).         \tag{S2}
\]

When `D>=n^delta`, `H>=2^{c(log D)^2}`, and
`t=floor(c delta log D/2)`, the first term is eventually smaller than one,
while the second has a fixed power gain whenever `L_T=n^o(1)`.  Any
exponent `epsilon<c delta/4` is available before the harmless `n^o(1)`
loss.

The toggle conclusion is conditional only in the **global overlap** `L_T`,
not in its geometry.  A common global guard alphabet `W` also gives the
alternative exact released-carrier bound

\[
                   L_R\le\sum_{j=0}^{2k_0}{|W|\choose j}.    \tag{S3}
\]

The sparse common-guard example from the companion report does not satisfy
the hypotheses cheaply.  Although every nested pair has the canonical
`2+2` witness on the tangent edge `uv`, the complete split-circuit clutter
also contains a singleton `1+3` trace at **every** outer vertex.  Its
minimum transversal is the whole carrier.  Releasing it erases the context,
while the toggle face `{x}` belongs to every contextual toggle bank.  Thus
the example precisely defeats both overlap parameters; its unrestricted
convex outer shield remains the paying bank.

This is a genuine fixed-power branch, but not a complete proof: the missing
statement is that every remaining quadratic-entropy family either has the
overlaps in (S2), or its concentrated toggle banks expand to an unrestricted
outer shield complex.

## 1. Split-circuit traces

Let `P=O disjoint_union X` be a labelled planar general-position set.  Fix
an ordinary outer carrier `R subseteq O` and an internal reservoir
`H subseteq F(P)` whose members are subsets of `X`.  Assume one-point
compatibility:

\[
              R\cup\{x\}\in F(P)
              \quad\text{for every }x\in\bigcup H.          \tag{3}
\]

Define the **outer trace clutter** `T(R,H)` on vertex set `R` as follows.
A nonempty set `T subseteq R` is a trace when `|T|` is one or two and there
are `F in H` and `S subseteq F` such that

\[
             |T|+|S|=4,\qquad T\cup S\text{ is nonconvex}.  \tag{4}
\]

Thus the traces are exactly the outer parts of the bad `1+3` and `2+2`
split circuits which occur inside the reservoir.  A set `G subseteq R` is
a circuit transversal if it meets every member of `T(R,H)`.

> **Theorem 1 (guard-release lemma).**  If `G` is a circuit transversal,
> then
> \[
>                 (R-G)\cup F\in F(P)\qquad(F\in H).        \tag{5}
> \]

**Proof.**  Suppose `(R-G) union F` is nonconvex.  Planar Caratheodory
gives a nonconvex four-subset `Q`.  It cannot lie entirely in `R-G` or in
`F`, because both are ordinary faces.  It cannot contain three outer
points and one internal point `x`, because it is then a subset of the
ordinary face `R union {x}` from (3).  Therefore `Q=T union S` has split
`1+3` or `2+2`.  Its outer trace `T` belongs to `T(R,H)` but is contained
in `R-G`, contradicting that `G` is a transversal.  QED.

It is essential here to hit **every** split-circuit trace, not merely the
canonical tangent-edge witness for every nested internal pair.  Deleting
one tangent guard can expose a new `1+3` circuit in which a different outer
vertex is hidden by three internal points.

## 2. A maximum matching is both a cover and a Boolean bank

Let `nu(R,H)` be the maximum number of pairwise disjoint members of the
trace clutter.  Since every trace has size at most two, this parameter has
two simultaneous interpretations.

> **Theorem 2 (cover-or-toggle lemma).**  Let
> `P_1,...,P_k` be a maximum trace matching, where `k=nu(R,H)`, and put
> \[
>                         G=P_1\cup\cdots\cup P_k.           \tag{6}
> \]
> Then:
>
> 1. `G` is a circuit transversal and `|G|<=2k`, so (5) holds;
> 2. suppose `Y subseteq X` has size `D` and
>    `R union {y}` is an ordinary face for every `y in Y`.  Then
>    \[
>      B(R,P,Y)=\left\{
>       \left(R-\bigcup_{i\in I}P_i\right)\cup\{y\}:
>                  I\subseteq[k],\ y\in Y\right\}           \tag{7}
>    \]
>    is an ordinary-face bank of exact size
>    \[
>                             |B(R,P,Y)|=D2^k.               \tag{8}
>    \]

**Proof.**  A maximum matching is maximal.  If a trace were disjoint from
`G`, it could be added to the matching, a contradiction.  Hence `G` is a
transversal and its size is at most `2k`.

Every face in (7) is a subset of the ordinary face `R union {y}`, so it is
ordinary.  The matching traces are nonempty and pairwise disjoint; hence
different subsets `I` delete different outer label sets.  The partition
`O disjoint_union X` recovers `y`.  Thus all `D2^k` faces are distinct.
QED.

For trace clutters of rank two this is the cleanest possible elementary
matching-cover relation.  If all singleton traces are first selected, the
remaining traces form an ordinary graph; endpoints of a maximal matching
cover that graph.  Equivalently, if `s` outer vertices occur as singleton
traces and the residual graph has matching number `nu_2`, then

\[
       s+\nu_2\le\tau(T(R,H))\le s+2\nu_2,\qquad
       k=s+\nu_2,                                           \tag{9}
\]

where `tau` is minimum transversal size.

## 3. Entropy-powered small-transversal release

Consider a contextual family indexed by `c`.  Assume:

* the outer carriers `R_c subseteq O` are pairwise distinct ordinary faces;
* every record cell has `|E_c|=D^2`;
* `H subseteq F(X)` is one common internal reservoir of size `H`;
* every cell satisfies the singleton compatibility (3); and
* the trace clutter of every cell in the present subfamily has a
  transversal `G_c` of size at most `t`.

Put

\[
 A_c=\{R_c\},\qquad
 B_c=\{(R_c-G_c)\cup F:F\in H\},\qquad
 S_t(n)=\sum_{i=0}^t{n\choose i}.                           \tag{9a}
\]

Theorem 1 says every member of `B_c` is ordinary.  The partition
`O disjoint_union X` makes `F` recoverable from the output, so
`|B_c|=H`.

> **Theorem 3 (small-transversal reservoir multiplication).**  Under the
> preceding assumptions,
> \[
>       \boxed{\sum_c|E_c|\le
>                   D^2\sqrt{{S_t(n)\over H}}\,V(P).}       \tag{9b}
> \]
> More generally, replace `S_t(n)` by the actual maximum multiplicity of a
> released carrier if that is smaller.

**Proof.**  The banks `A_c` have overlap one because the carriers are
distinct.  A face `U in B_c` recovers

\[
                  F=U\cap X,\qquad R_c-G_c=U\cap O.         \tag{9c}
\]

Guessing `G_c`, of size at most `t`, then recovers `R_c`; there are at most
`S_t(n)` guesses.  Hence the `B_c`-overlap is at most `S_t(n)`.

For each cell use the real-valued local constant

\[
                         K={D^4\over H}.                     \tag{9d}
\]

It may be smaller than one.  The cell square inequality is the equality

\[
             |E_c|^2=D^4=K|A_c||B_c|.                      \tag{9e}
\]

The recoverable-cell Cauchy telescope with overlaps one and `S_t(n)` gives
(9b).  QED.

The exact criterion for a fixed power `epsilon>0` is

\[
                         {H\over S_t(n)}
                              \ge D^{2+2\epsilon}.           \tag{9f}
\]

Indeed (9f) makes the multiplier in (9b) at most `D^(1-epsilon)`.
The reservoir entropy makes (15) automatic for a logarithmic-size
transversal with a sufficiently small constant.

> **Corollary 4 (explicit logarithmic cover).**  Fix `c,delta>0`.  Suppose
> \[
>        D\ge n^\delta,\qquad H\ge2^{c(\log D)^2},\qquad
>        t\le {c\delta\over2}\log D.                        \tag{9g}
> \]
> Then the multiplier in (9b) tends to zero superpolynomially in `D`.
> In particular it is at most `D^(1-epsilon)` for every fixed `epsilon`
> and all sufficiently large `D`.

**Proof.**  Put `d=log D` and `L=log n`; then `L<=d/delta`.  The standard
binomial estimate gives

\[
 \log S_t(n)\le t\log(en/t)
       \le {c\delta d\over2}(L+O(1))
       \le {c\over2}d^2+O(d).                              \tag{9h}
\]

Thus

\[
 \log\left(D^2\sqrt{S_t(n)/H}\right)
                   \le2d-{c\over4}d^2+O(d),                \tag{9i}
\]

which proves the assertion.  QED.

In the one-pocket application `H=F(X)` and the internal alphabet has at
least `D` labels.  Hence the universal planar convex-subset lower bound
supplies the middle hypothesis of (9g) for every fixed `c<1/4` and all
sufficiently large `D`.

The contrapositive is the useful structural output.  After removing the
subfamily paid by Corollary 4, every surviving context has

\[
            \tau(T(R_c,H))>{c\delta\over2}\log D.           \tag{9j}
\]

By Theorem 2, `tau<=2nu`; hence every such context contains a matching of
more than `(c delta/4)log D` pairwise disjoint split-circuit traces.

## 4. Global low-matching guard release

Return to `C` contextual cells.  In cell `c` let `R_c` be its outer
carrier, `H` the common internal reservoir, and `T_c=T(R_c,H)`.  Assume
the hypotheses of the outer--internal mixed-bank theorem:

* `|G_c|=D^2`;
* the first ordinary-face bank `A_c` has `|A_c|>=2D` and overlap at most
  `Lambda`;
* `|H|>=D^3/2`.

Fix an integer `k_0>=1` and consider the low-matching cells

\[
                         C_- =\{c:\nu(T_c)<k_0\}.            \tag{10}
\]

Choose a maximum matching and its guard union `G_c` as in Theorem 2.  Then
`|G_c|<2k_0`, and Theorem 1 makes

\[
 M_c=\{(R_c-G_c)\cup F:F\in H\}                             \tag{11}
\]

an ordinary-face bank of size `|H|`.

> **Corollary 5 (released low-matching cells).**  If a fixed ordinary face
> belongs to at most `L_R` of the banks (11), then
> \[
>                         \sum_{c\in C_-}|G_c|
>                    \le\sqrt{\Lambda L_R}\,V(P).           \tag{12}
> \]

**Proof.**  In every cell,
`D^4<=|A_c||M_c|` by `|A_c|>=2D` and `|M_c|>=D^3/2`.
Apply the recoverable-cell Cauchy telescope with overlaps `Lambda,L_R`.
QED.

There is a useful direct decoder for `L_R`.  Suppose the original carriers
`R_c` are distinct and all selected guard unions lie in one global set
`W subseteq O` of size `t`.  A released carrier `U=R_c-G_c` has at most

\[
                         S_g(t)=\sum_{j=0}^g{t\choose j}     \tag{13}
\]

preimages with `|G_c|<=g`, because one guesses `G_c subseteq W` and then
`R_c=U union G_c`.  Intersecting a mixed face in (11) with `O` recovers
`U`.  Therefore

\[
                         L_R\le S_{2k_0-1}(t).               \tag{14}
\]

The same statement allows multiplicity `M` of the original carriers by
multiplying the right side by `M`.

## 5. Global high-matching toggle gain

For `c` with `nu(T_c)>=k_0`, retain any `k_0` matching traces and let
`B_c` be the toggle bank (7), using the `D` source-atom labels in the cell.
It has size `D2^k_0`.  Let `L_T` be the maximum number of these contextual
toggle banks containing one ordinary face.

> **Corollary 6 (toggle gain).**  The high-matching record mass satisfies
> \[
>                 \sum_{c:\nu(T_c)\ge k_0}|G_c|
>                         \le L_TD2^{-k_0}V(P).              \tag{15}
> \]

**Proof.**  Summing the toggle banks with overlap `L_T` gives

\[
       |C_+|D2^{k_0}=\sum_{c\in C_+}|B_c|\le L_TV(P).       \tag{16}
\]

Multiply by `D/2^k_0`, since the record mass is `|C_+|D^2`.
QED.

Combining the two branches proves the advertised theorem.

> **Theorem 7 (global circuit-transversal split).**
> \[
> \boxed{
> |E|\le\left(
>    \sqrt{\Lambda L_R}+L_TD2^{-k_0}\right)V(P).}           \tag{17}
> \]
> If `k_0>=epsilon log D`, `L_T=n^o(1)`, and
> \[
>                         \Lambda L_R
>                    \le n^{o(1)}D^{2-2\epsilon},           \tag{18}
> \]
> then `|E|<=n^o(1)D^(1-epsilon)V(P)`.  Via (14), a sufficient
> guard-alphabet condition is
> \[
>       \Lambda\sum_{j<2k_0}{t\choose j}
>                    \le n^{o(1)}D^{2-2\epsilon}.           \tag{19}
> \]

This is the requested fixed-power guard-release corollary.  It does not
assume that base-retaining mixed faces exist; all circuit guards are deleted
before the internal reservoir is attached.

The entropy-powered version removes the auxiliary first bank and global
guard alphabet altogether.

> **Theorem 8 (sharp cover-threshold split).**  Fix an integer `t>=0`, put
> \[
>                         k_0=\lfloor t/2\rfloor+1,          \tag{19a}
> \]
> and split cells according as `tau(T_c)<=t` or `tau(T_c)>t`.  Assume the
> carriers are distinct and let `L_T` be the toggle-bank overlap on the
> second subfamily.  Then
> \[
> \boxed{
> |E|\le\left(
> D^2\sqrt{{S_t(n)\over H}}+L_TD2^{-k_0}\right)V(P).}       \tag{19b}
> \]

**Proof.**  Theorem 3 pays the cells with a transversal of size at most
`t`.  In every remaining cell, `tau>t` and Theorem 2 gives
`tau<=2nu`, hence `nu>=floor(t/2)+1=k_0`.  Corollary 6 pays those cells.
QED.

> **Corollary 9 (explicit fixed power).**  Fix `c,delta>0`, suppose
> `D>=n^delta`, `H>=2^{c(log D)^2}`, and `L_T=n^o(1)`.  Take
> \[
>                         t=\left\lfloor
>                         {c\delta\over2}\log D\right\rfloor. \tag{19c}
> \]
> Then for every fixed
> \[
>                         0<\epsilon<{c\delta\over4},        \tag{19d}
> \]
> and all sufficiently large `n`, (19b) gives
> \[
>                         |E|\le n^{o(1)}D^{1-\epsilon}V(P). \tag{19e}
> \]

**Proof.**  Corollary 4 makes the first multiplier in (19b) eventually
smaller than one.  The choice (19c) gives
`k_0>=(c delta/4)log D-O(1)`.  Therefore the second multiplier is
`n^o(1)D^(1-c delta/4)`, which proves (19e) for every smaller fixed
`epsilon`.  QED.

Without the `L_T` hypothesis, Theorem 3 is still unconditional progress:
all unpaid contexts have `Omega(log D)` pairwise disjoint outer circuit
traces.  The exact remaining global task is to turn high toggle overlap
into the unrestricted shield bank seen in the sparse example.

## 6. Audit against the sparse common-guard family

Take the lower-parabola carriers and projective insertion chain from
`OUTER_INTERNAL_MIXED_BANK.md`.  For every carrier `R`, canonical nesting
gives the tangent-edge circuits

\[
                         \{u,v,x_i,x_j\}.                    \tag{20}
\]

It is tempting to hit (20) by deleting only `u`.  This is invalid because
(20) is not the whole split-circuit clutter.

On the exact 20-point internal record, for every vertex `a in R` there is a
convex internal triple `S_a` such that

\[
                         \{a\}\cup S_a\text{ is nonconvex}. \tag{21}
\]

Thus every singleton `{a}` is a trace.  The trace matching number and
minimum transversal number are both

\[
                         \nu(T(R,H))=\tau(T(R,H))=|R|.       \tag{22}
\]

The release set from Theorem 2 is the whole carrier, so all released
carriers coincide with the empty set and `L_R=C`.  The toggle bank contains
the singleton `{x}` for each source label `x`, and `{x}` belongs to all `C`
contextual toggle banks, so `L_T=C` as well.  Neither side of (17) gives a
power gain.

This is a useful sharpness result.  Canonical tangent-edge witnesses are
enough to certify nonconvexity but not enough to certify convexity after
guard release.  The full `1+3/2+2` trace clutter is load-bearing.  In the
scalable construction the unrestricted outer cloud is convex and supplies
the missing shield; proving an analogous shield alternative for arbitrary
outer families is exactly what remains.

## 7. Exact verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_circuit_transversal_guard_release.py
```

The checker exhausts all rank-two trace clutters through eight vertices,
verifying the matching cover and toggle identities; audits the released
carrier decoder (14); and constructs the exact rational sparse family.  On
all 56 six-vertex outer carriers it finds every singleton trace,
`nu=tau=6`, verifies guard release on every internal face of an eight-point
subrecord, and confirms `L_R=L_T=56`.  It also exhibits explicit failures
after deleting only one or both canonical tangent guards.
