# High-rank fixed-edge rectangles: deletion or a disjoint-circuit matching

**Date:** 2026-08-15. All logarithms are base two. The empty face may be
included throughout. This continues
`INDUCED_SUBSET_HIGH_RANK_POCKET_LIFT_GATE.md`.

## Verdict

There is an exact circuit-deletion theorem for the dense fixed-exposed-edge
source by pocket-face rectangle. It needs neither singleton compatibility nor
a product/container model.

Let \(Y,X\) be disjoint physical grounds, let \(\mathcal A\) be ordinary
rank-\(r\) faces in \(Y\), and let \(\mathcal H\) be ordinary faces in
\(X\). For a pair \((A,F)\), form the hypergraph of the \(Y\)-traces of all
nonordinary four-subsets of \(A\cup F\). Its edges have rank at most three.
Deleting \(G\subseteq A\) releases the **whole literal pocket face** \(F\)
if and only if \(G\) hits this trace hypergraph. Consequently, with

\[
                         S_d(n)=\sum_{i=0}^d{n\choose i},        \tag{1}
\]

the number of pairs with a source transversal of size at most \(d\) is at
most

\[
                         \boxed{S_d(n)V(P).}                    \tag{2}
\]

The output is \((A-G)\cup F\); it retains \(F\), and guessing the at most
\(d\) actually deleted source labels recovers \(A\). This is the exact
decoder load, not a description count.

If the source transversal has size greater than \(d\), a maximal matching
contains more than \(d/3\) pairwise source-disjoint circuit traces. If all
sources share one literal exposed edge \(uv\), all but at most two matching
traces avoid \(u,v\). Hence every hard pair has a rooted, edge-retaining
Boolean toggle bank of size

\[
                         2^{\lfloor d/3\rfloor-2}.               \tag{3}
\]

There is a symmetric strengthening. If deletion is allowed on both sides,
the low-deletion bound is still (2), while the hard pair contains more than
\(d/4\) **fully vertex-disjoint crossing four-circuits**. Thus the exact
survivor has both a source-trace matching and a physical circuit matching.

At the live pocket-lift scale, write

\[
 |\mathcal A||\mathcal H|
      \ge F_C(n)\,2^{\sigma L\Delta},\qquad
 V(P)<F_C(n),\qquad L=\log n,                                  \tag{4}
\]

where \(\sigma>0\) is fixed and \(\Delta=o(L)\). Taking
\(d=\lfloor\sigma\Delta/2\rfloor\), (2) shows that all but a

\[
                    2^{-(\sigma/2-o(1))L\Delta}                 \tag{5}
\]

fraction of the rectangle has both transversal numbers greater than \(d\).
Every surviving pair therefore carries
\(\Omega(\Delta)\) source-disjoint traces, and
\(\Omega(\Delta)\) fully disjoint crossing circuits, while preserving the
common edge in all but two of them. The high-rank pocket lift supplies (4)
with, for example, \(\sigma=1/3\) after its polynomial edge localization.

This is a genuine narrowing, but it does **not** close the fixed gap. When
\(\Delta=\Theta(\log L)\), the toggle bank (3) has only
\(2^{\Theta(\log L)}=L^{\Theta(1)}\) faces. The missing multiplier in (4)
is \(2^{\Theta(L\log L)}=n^{\Theta(\log\log n)}\). A factor \(L\) remains
in the logarithm. Moreover, the exact anti-aligned two-parabola regression
has source transversal number \(r\): every source label is a singleton
trace, so only deleting the entire source releases a rank-at-least-three
pocket face. Its internal Boolean cloud pays enormously, but it proves that
matching plus common edge alone cannot do better.

The remaining theorem is now precise: a least-counterexample/internal-bank
argument must turn the \(\Omega(\Delta)\) physical matching into a bank with
\(2^{\Omega(L\Delta)}\) **cross-context** mass, or prove that concentrating
the matchings forces a large ordinary support shield. Detached toggle faces
provide only \(2^{O(\Delta)}\). Fixing a matching of an uncontrolled constant
multiple of \(\Delta\) literal circuits can consume the available slack, but
a sufficiently small constant multiple can in fact be fixed while retaining
\(2^{\Omega(L\Delta)}\) mass; Section 4 records that useful sharpening. The
remaining failure is therefore not literal localization itself, but converting
the resulting common-circuit rectangle into an ordinary mixed bank.

## 1. Four-local deletion is exactly a transversal problem

Let \(P\) be a planar general-position configuration with a fixed physical
partition \(P=Y\sqcup X\). Let \(A\subseteq Y\) and \(F\subseteq X\) be
ordinary. Define the **source-trace clutter**

\[
 \mathcal T_Y(A,F)=
 \{C\cap A:C\in {A\cup F\choose4},\ C\text{ nonordinary}\}.    \tag{6}
\]

Every member is nonempty and has rank one, two, or three, since \(A\) and
\(F\) are individually ordinary. Put

\[
 \tau_Y(A,F)=\min\{|G|:G\subseteq A,\ G\cap T\ne\varnothing
                         \text{ for every }T\in\mathcal T_Y(A,F)\}. \tag{7}
\]

The empty clutter has transversal number zero.

> **Theorem 1 (source-retaining circuit deletion).** For every
> \(G\subseteq A\),
> \[
>       (A\setminus G)\cup F\text{ is ordinary}
>       \quad\Longleftrightarrow\quad
>       G\text{ hits every member of }\mathcal T_Y(A,F).         \tag{8}
> \]

**Proof.** If \(G\) misses a trace \(C\cap A\), the associated bad
four-set \(C\) survives in \((A\setminus G)\cup F\), so the union is not
ordinary. Conversely, if the union is not ordinary, planar four-locality
supplies a nonordinary four-subset \(C\) of it. This \(C\) meets both
grounds and belongs to (6), while \(C\cap A\) misses \(G\), a
contradiction. \(\square\)

This statement includes all \(3+1,2+2,1+3\) signed types. The rank-two
guard-release theorem is recovered when every pocket singleton is already
compatible with \(A\), which excludes the \(3+1\) type. No such
compatibility is assumed here.

Let \(\nu_Y(A,F)\) be the maximum number of pairwise disjoint members of
\(\mathcal T_Y(A,F)\).

> **Lemma 2 (rank-three matching cover).**
> \[
>                       \tau_Y(A,F)\le3\nu_Y(A,F).               \tag{9}
> \]

**Proof.** The union of the edges of a maximum matching is a transversal:
otherwise a disjoint edge could be added. Every matching edge has rank at
most three. \(\square\)

The use of a *maximum* matching is unnecessary for construction: any
maximal matching has the same cover property and proves (9) with its own
size.

## 2. Exact load of the bounded-deletion branch

Let \(\mathcal R\subseteq\mathcal A\times\mathcal H\) be any simple
record family. For every record with \(\tau_Y(A,F)\le d\), choose the first
minimum transversal \(G(A,F)\) in a fixed physical order and output

\[
                       W(A,F)=(A-G(A,F))\cup F.                  \tag{10}
\]

Theorem 1 says that this is an ordinary face. The physical partition gives

\[
                  W\cap X=F,\qquad W\cap Y=A-G.                 \tag{11}
\]

After \(W\) is fixed, guessing \(G\subseteq Y\setminus W\),
\(|G|\le d\), recovers \(A=(W\cap Y)\cup G\). Thus an output has at most
\(S_d(|Y|)\le S_d(n)\) preimages.

> **Theorem 3 (bounded source-deletion bank).**
> \[
>   |\{(A,F)\in\mathcal R:\tau_Y(A,F)\le d\}|
>                             \le S_d(n)V(P).                    \tag{12}
> \]

There is a useful least-counterexample sharpening. Include the empty face
in all three face counts and put

\[
 V_{\rm mix}(P;Y,X)=V(P)-V(P[Y])-V(P[X])+1.                    \tag{12a}
\]

This is exactly the number of ordinary faces meeting both physical
grounds. If every record has (F\ne\varnothing) and (d<r), then (10)
meets both grounds. Therefore

\[
 |\{(A,F)\in\mathcal R:\tau_Y(A,F)\le d\}|
                         \le S_d(n)V_{\rm mix}(P;Y,X).           \tag{12b}
\]

If (P) is a least counterexample to (F_C), (p=|X|), and
(N=|Y|<n), induction and the parent upper give

\[
 V_{\rm mix}(P;Y,X)
       <F_C(n)-F_C(N)-F_C(p)+1.                                \tag{12c}
\]

This is an actual use of both internal banks, not a detached Cauchy
estimate. Its quantitative strength is limited. For (p=n/s=o(n)), put
(eta=-\log_2(1-1/s)). The mean value theorem gives

\[
 {F_C(n)-F_C(n-p)\over F_C(n)}
   \le(\ln2)\{\Phi_C(L)-\Phi_C(L-\eta)\}
   =O_C\!\left({L\over s}\right)                               \tag{12d}
\]

whenever (L/s=o(1)), where
(Phi_C(z)=z^2/2-Cz\log z). Thus (s=L^A), (A>1), saves only
((A-1)\log L+O(1)) bits. This is negligible beside the
(Theta(L\log L)) live slack. The mixed-capacity refinement is exact but
does not close the high-matching branch.

For weighted histories, let

\[
 \kappa=\max_{A,F}\sum_{\omega:\pi(\omega)=(A,F)}w_\omega.    \tag{13}
\]

Applying the same decoder after projection gives the scope-honest form

\[
 \sum_{\omega:\tau_Y(\pi(\omega))\le d}w_\omega
                             \le\kappa S_d(n)V(P).               \tag{14}
\]

Thus duplicate chronology is an explicit factor \(\kappa\); it is not
silently treated as geometry. In the literal Cartesian source by pocket
rectangle, \(\kappa=1\).

### Two-sided deletion

Let \(\mathcal C(A,F)\) be the hypergraph on \(A\cup F\) whose edges are
all bad crossing four-sets, and let \(\tau_\times(A,F)\) and
\(\nu_\times(A,F)\) be its transversal and matching numbers. Then

\[
                         \tau_\times\le4\nu_\times.             \tag{15}
\]

If \(G\subseteq A\cup F\) hits every edge, then
\(((A\cup F)\setminus G)\) is ordinary. Given this output and \(G\), the
partition recovers both original faces. Therefore

\[
 |\{(A,F)\in\mathcal R:\tau_\times(A,F)\le d\}|
                             \le S_d(n)V(P).                    \tag{16}
\]

If \(\tau_\times>d\), (15) gives more than \(d/4\) fully
vertex-disjoint physical crossing circuits. This is stronger than merely
having disjoint source traces.

## 3. What the common edge really contributes

Assume every \(A\in\mathcal A\) contains the same physical exposed edge
\(uv\), with the same interior side. If \(\tau_Y(A,F)>d\), Lemma 2 gives
a source-trace matching of size

\[
                            s> d/3.                              \tag{17}
\]

At most two pairwise disjoint traces meet \(\{u,v\}\). Delete those and
write the remaining traces as \(T_1,\ldots,T_{s'}\), where

\[
                            s'\ge s-2.                           \tag{18}
\]

For every \(I\subseteq[s']\),

\[
                  A_I=A\setminus\bigcup_{i\in I}T_i             \tag{19}
\]

is an ordinary downface of \(A\), contains \(u,v\), and still has \(uv\)
as an exposed edge on the same side. Pairwise disjoint nonempty traces make
all \(A_I\) distinct. This proves (3).

The same statement holds for a full circuit matching after discarding the
at most two circuits which meet \(u\) or \(v\). The edge therefore retains
one common projective chart for every toggle output. What it does **not**
do is make any partial toggle (19) compatible with \(F\). Only a complete
transversal has that implication.

Across varying sources, the exact decoder for (19) is obtained by guessing
the deleted union, of rank at most \(3s'\). If \(K_*\) distinct sources
each choose one canonical hard partner, then

\[
       V(P)\ge {K_*2^{s'}\over S_{3s'}(n)}.                      \tag{20}
\]

Equation (20) is honest but useless at the live scale:
\(\log S_{3s'}(n)=\Theta(L\Delta)\), whereas \(s'=\Theta(\Delta)\).
A source code of deletion distance \(3s'\) removes the denominator, but
extracting it costs the same Hamming-ball factor. This is the exact global
overlap obstruction to promoting the local toggle bank.

## 4. Fixed-gap audit

Suppose (4) holds and put \(d=\lfloor\sigma\Delta/2\rfloor\). Since
\(d=o(n)\),

\[
 \log S_d(n)
    \le d\log(en/d)
    \le(\sigma/2+o(1))L\Delta.                                 \tag{21}
\]

Apply (12) and (16). The union of the two low-transversal branches has at
most

\[
          2S_d(n)V(P)
             \le F_C(n)2^{(\sigma/2+o(1))L\Delta}               \tag{22}
\]

records. Dividing by (4) proves (5). Every remaining record simultaneously
satisfies

\[
 \nu_Y>{d\over3}={\sigma\over6}\Delta-O(1),\qquad
 \nu_\times>{d\over4}={\sigma\over8}\Delta-O(1).               \tag{23}
\]

After removing the exposed-edge collisions, the right sides lose at most
two.

For the pocket lift in the preceding report, its equations (29) and (31)
give

\[
          |\mathcal A||\mathcal H|
               \ge F_C(n)2^{(1-o(1))L\Delta}.                   \tag{24}
\]

The edge-and-side localization costs only \(2^{O(L)}\), and its choice of
\(\Delta\) has \(L=o(L\Delta)\). Hence (4) holds with any fixed
\(\sigma<1\), in particular with the conservative \(\sigma=1/3\).

At the minimally advertised quasipolynomial scale
\(\Delta=\Theta(\log L)\), (23) gives only
\(\Theta(\log L)\) disjoint circuits. Even the full local Boolean toggle
has logarithm \(O(\log L)\), while (24) needs a cross-context bank of
logarithm \(\Theta(L\log L)\). This is not a constant bookkeeping loss.

Literal localization of \(s\) full circuits has at most \(n^{4s}\)
possible ordered descriptions. For an uncontrolled
\(s=\Theta(\Delta)\), its logarithm is \(4sL=\Theta(L\Delta)\), so it may
consume the complete slack in (24). The constants nevertheless leave a
rigorous common-circuit subrectangle. Put

\[
        s=\left\lfloor{\sigma\Delta\over32}\right\rfloor,
        \qquad d=8s.                                           \tag{24a}
\]

The low two-sided-deletion branch has at most
\(V(P)2^{(\sigma/4+o(1))L\Delta}\) records. Every other record has a
matching of more than \(2s\) fully disjoint crossing circuits. Choose its
first \(s\) circuits in the physical order. Pigeonholing their ordered
four-label description costs at most

\[
                n^{4s}\le2^{(\sigma/8+o(1))L\Delta}.           \tag{24b}
\]

Consequently one fixed literal \(s\)-circuit matching is shared by at least

\[
                V(P)2^{(5\sigma/8-o(1))L\Delta}                \tag{24c}
\]

surviving records. Because these circuits are physical, every one remains
bad for every cross-combination of the row and column projections of this
fibre. Thus a small linear matching *can* be localized with substantial
slack. What is still missing is a square-preserving operation on that
common-circuit rectangle: deleting/toggling its detached traces pays only
\(2^{O(s)}\), and retaining either endpoint family has unrestricted
cross-context overlap.

## 5. Exact all-delete calibration

Use the two opposite parabolic clouds from
`INDUCED_SUBSET_HIGH_RANK_POCKET_LIFT_GATE.md`. Their lexicographic
orientation has the following exact property: a subset meeting both clouds
is ordinary if and only if each cloud trace has rank at most two.

Take a source face \(A\) of rank \(r\ge3\), containing a fixed adjacent
edge \(uv\), and a pocket face \(F\) of rank \(q\ge3\). For every
\(a\in A\) and every triple \(J\in{F\choose3}\),

\[
                              \{a\}\cup J                         \tag{25}
\]

is a nonordinary crossing four-set. Hence every singleton \(\{a\}\) is a
source trace and

\[
                            \tau_Y(A,F)=r.                        \tag{26}
\]

Only deletion of the whole source releases \(F\). The source-trace
matching has size exactly \(r\), and after preserving \(uv\), (19) is the
full Boolean interval on \(A\setminus\{u,v\}\).

For completeness, the full crossing circuit hypergraph consists of all
\(3+1\) and \(1+3\) choices. Its transversal number is

\[
                \tau_\times(A,F)=r+q-\max\{r,q,4\}.              \tag{27}
\]

Indeed a surviving set contains no crossing bad circuit exactly when one
side is empty or both nonempty sides have rank at most two. Formula (27)
follows by maximizing the number of surviving labels.

This is a scalable rational and stretchable obstruction to improving
Theorems 1--3 by local planarity, high source rank, or the common edge. It
is not a least-counterexample construction: each parabolic cloud is itself
convex and has a Boolean face bank. The calibration says exactly where a
positive theorem must enter: it must charge that internal bank, or obtain a
cross-context shield from the concentration of the circuit matchings.

### Audit against rooted semialgebraic extraction

There is no conflict with
`../agent_outer_internal_product/ROOT_AWARE_FIXED_EDGE_SEMIALGEBRAIC_EXTRACTION_GATE.md`.
That theorem starts with one fixed literal carrier (F), (k) disjoint
ear-role **clouds** of size nearly (n), and inverse-polylogarithmic density
of already ordinary rooted full transversals. It then extracts a complete
rooted box. Here a hard pair supplies only (O(\Delta)) disjoint traces
inside one rank-(r=O(L)) source. It supplies neither large role alphabets
nor a positive density of rooted ordinary tuples. Promoting the physical
traces to such clouds is exactly the missing cross-context operation.

The homogeneous nested-ear example in that report is consistent with the
present gate: every rooted pair is bad, the rooted-good density is zero, and
the absolute external support is Boolean. Both results isolate the same
alternative—positive rooted density pays at the required
(2^{\Theta(L\Delta)}) scale, while homogeneous badness must be charged to
an internal shield. Neither result derives that charge from the parent
fixed-gap upper bound.

The rank-only source downshadow does not supply that charge. If
\(|\mathcal A|={x\choose r}\), Kruskal--Katona gives only

\[
       |\partial_{r-j}\mathcal A|\ge{x\choose r-j},\qquad
       {{x\choose r-j}\over{x\choose r}}
          =\prod_{h=0}^{j-1}{r-h\over x-r+h+1}.                  \tag{28}
\]

For the pocket-lift density \(x/r\asymp2^\Delta\), the ratio in (28) is
\(2^{-j\Delta+O(j)}\): the proper shadow can shrink rather than expand.
If the family is literally a complete layer, planar four-locality upgrades
its support to a convex Boolean shield; proving a stability version of this
upgrade for the far-from-complete residue is precisely the missing
internal-bank theorem.

## 6. Verification

Run

```text
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_high_rank_fixed_edge_circuit_deletion_matching_gate.py
```

The verifier uses exact rational determinants. It exhausts every deletion
of several anti-aligned source--pocket pairs, checks (8) and its two-sided
analogue, computes exact transversal and matching numbers, verifies (26)
and (27), checks that all common-edge toggle faces are distinct and retain
the edge, exhausts small decoder fibres against (1), checks the exact mixed
face decomposition (12a), audits (28) exactly, and verifies the live
fixed-gap and mixed-capacity inequalities at five large scales.
