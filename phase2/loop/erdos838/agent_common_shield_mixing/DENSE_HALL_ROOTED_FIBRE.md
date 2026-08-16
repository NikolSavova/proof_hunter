# Dense Hall obstruction: rooted-fibre localization and the incidence-only barrier

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

A genuinely dense Hall obstruction cannot keep the marked blocker shield
diffuse.  There is an exact localization theorem.  Let `A` be a family of
`C` canonical contexts of common demand `m`, let

\[
                 \mathcal U=\bigcup_{c\in\mathcal A}\mathcal B_c,
                 \qquad \rho={Cm\over|\mathcal U|},                 \tag{1}
\]

and suppose every context supplies at least `K` marked shield occurrences
`(p,F)`, where `F in mathcal U`, `p in F`, and `|F|<=h`.  Then some actual
marked face is shared by at least

\[
                    \boxed{\ {K\rho\over hm}\ }                    \tag{2}
\]

contexts.  If each occurrence also has one of at most `T` tangent/history
states, one complete `(p,F,tau)` state is shared by at least

\[
                    \boxed{\ {K\rho\over hmT}\ }.                  \tag{3}
\]

Consequently, if

\[
 K=2^{(a-o(1))(\log D)^2},\quad \rho>D^{1-\epsilon},
 \quad h,m,T=D^{O(1)},                                    \tag{4}
\]

the common rooted-tangent fibre still has
`2^{(a-o(1))(log D)^2}` histories.  Thus Hall failure rigorously descends
to the already isolated common marked-shield, fixed-tangent, omitted-petal
atom.  The quadratic entropy cannot be lost among marks, faces, carrier
edges, or tangent cells.

There is a second sharp consequence if `A` is an inclusion-minimal
maximizer of (1).  A context of demand `m_c` has fewer than

\[
                         {m_c\over\rho}                            \tag{5}
\]

private target faces.  In particular, at density
`rho>D^(1-epsilon)`, an atomic demand-`D` context has fewer than
`D^epsilon` context-decodable outputs.  Hence every fixed-power forward or
mixed bank has already exited before the common rooted fibre; the strict
Hall residue is necessarily collision-dominated in every such bank.

This is as far as extremal minimality and bank incidence alone can go.  A
scalable tensor of finite-projective-plane incidence graphs has all the
following properties simultaneously:

* its full context family is the unique inclusion-minimal Hall maximizer;
* its Hall density is exactly the common context demand `D`;
* every context has a bank of size
  `K=2^{Theta((log D)^2)}`;
* every target has degree exactly `K`, so there are no private or low-degree
  faces; and
* distinct contexts have distinct banks, with intersections governed by
  Hamming distance rather than a common-bank tensor.

The incidence graph contains induced `2K2`s and is not Ferrers.  It is an
exact **abstract kill** of the proposed inference “minimal dense Hall plus
high degrees forces a common tensor.”  It is not a planar EIC' regression:
actual rooted carrier incidence is Ferrers, and the listed geometric banks
have additional circuit/profile relations absent from the design.  No
scalable planar `Theta(V)`-mass Hall regression was found.  The next theorem
must therefore use those planar relations *inside* the fixed
`(p,F,tau)` omitted-petal fibre; another pruning of the Hall incidence graph
cannot suffice.

## 1. Private-target pruning at a Hall maximizer

Let contexts have arbitrary positive demands `m_c`.  For a nonempty family
`A`, write

\[
 M(A)=\sum_{c\in A}m_c,\qquad
 U(A)=\left|\bigcup_{c\in A}\mathcal B_c\right|,
 \qquad \rho(A)={M(A)\over U(A)}.                         \tag{6}
\]

Choose `A` to maximize `rho(A)`, and subject to that choose it
inclusion-minimal.  For `c in A`, let

\[
 E_c=\mathcal B_c\setminus
       \bigcup_{d\in A\setminus\{c\}}\mathcal B_d                 \tag{7}
\]

be its private targets.

> **Theorem 1 (strict private-target bound).**  If `|A|>1`, then
> 
> \[
>                         |E_c|<{m_c\over\rho(A)}          \tag{8}
> \]
> 
> for every `c in A`.

**Proof.**  Put `M=M(A)`, `U=U(A)`, `e=|E_c|`, and `m=m_c`.
Inclusion-minimality says

\[
                         {M-m\over U-e}<{M\over U};        \tag{9}
\]

the denominator is nonzero because at least one other nonempty bank
remains.  Cross multiplication gives `U m>M e`, which is (8).  QED.

If a local target bank is context-decodable, its targets occur in no other
context and hence lie in `E_c`.  This proves (5).  Notice that (8) is much
stronger than an average-degree statement for any bank whose local size is
superpolynomial in `D`.

## 2. A quadratic shield forces a common marked rooted fibre

A marked shield occurrence is a triple `(c,p,F)` with

\[
                    F\in\mathcal B_c,\qquad p\in F,
                    \qquad |F|\le h.                     \tag{10}
\]

Let `K_c` be the number of distinct marked pairs `(p,F)` supplied by
context `c` and suppose `K_c>=K`.

> **Theorem 2 (dense-Hall marked localization).**  Equations (2)--(3)
> hold.  More generally, for nonuniform demands and marked incidence count
> `K_c`, some marked face has occurrence degree at least
> 
> \[
>              {\sum_{c\in A}K_c\over h|\mathcal U|}.     \tag{11}
> \]

**Proof.**  An ordinary face `F` of rank at most `h` supports at most `h`
contained marks.  Hence the number of marked bins `(p,F)` over
`F in mathcal U` is at most `h|mathcal U|`.  The number of incidences is at
least `CK`; double counting gives a bin of degree at least

\[
 {CK\over h|\mathcal U|}
       ={K\over h}{\rho\over m},                          \tag{12}
\]

which proves (2) and also proves (11).  Pigeonholing the at most `T`
states inside this bin proves (3).  QED.

For the live repair system, `p` is the actual retained repair label and
`F` is an actual ordinary blocker-only shield face.  The tangent state can
be taken to include the insertion edge and its two protected neighboring
vertices.  Even the crude ambient bound `T<=n^4` is only a fixed power of
`D` on a fixed-power cap `D=n^(delta+o(1))`.  Thus (4) proves that a dense
Hall family lands in the precise fixed-mark, fixed-shield, fixed-tangent
fibre of `TANGENT_MARKED_SHIELD_DESCENT.md`, with the full quadratic
history coefficient unchanged.

The theorem also explains why the marked halfplane bank alone was not
enough.  Its local size is only `2^{Theta(q)}=D^{Theta(1)}` for
`q=Theta(log D)`, so (2) gives only a fixed-power fibre.  The input which
preserves quadratic entropy is the full marked blocker reservoir with
`K=2^{Theta((log D)^2)}`.

No uniform mark-degree assumption is hidden here.  If a context has an
ordinary blocker reservoir `mathcal H_c` of `H` nonempty faces of rank at
most `h`, mark every face by all its contained repair labels.  Then

\[
       K_c=\sum_{F\in\mathcal H_c}|F|\ge H.               \tag{12a}
\]

The nonuniform form (11) applies to these actual incidences even if one
repair label belongs to very few shield faces.  Thus a quadratic ordinary
reservoir, aggregated over its genuine contained marks, is already enough
for the localization.

## 3. Exact incidence-only obstruction

Let `r` be a prime power and let `PG(2,r)` be the projective plane.  It has

\[
                         N=r^2+r+1                              \tag{13}
\]

points and the same number of lines; every line has `r+1` points and every
point lies on `r+1` lines.  Take the `t`-fold tensor incidence system:
contexts are line tuples, targets are point tuples, and a context is joined
to a target exactly when incidence holds in every coordinate.  Then

\[
 C=U=N^t,\qquad K=(r+1)^t,                                \tag{14}
\]

and both sides are `K`-regular.

Give every context demand `D`.  Regularity and equality of the two sides
imply Hall expansion: for every context subfamily `A`, edge counting gives

\[
             K|A|\le K|N(A)|,qquad |N(A)|\ge|A|.          \tag{15}
\]

Therefore every Hall density is at most `D`, while the full family has
density exactly `D`.  The tensor incidence graph is connected: any two
line tuples share the coordinatewise tuple of their pairwise intersection
points as a common distance-two neighbor.  Equality in (15) for a proper
nonempty `A` would disconnect `A union N(A)` from the rest.  Hence the full
family is the unique inclusion-minimal maximizer.

Every target has degree `K`.  For two context tuples `ell,ell'` at Hamming
distance `s`, projective-plane uniqueness of line intersections gives

\[
                   |\mathcal B_ell\cap\mathcal B_(ell')|
                    ={K\over(r+1)^s}.                    \tag{16}
\]

Thus all banks are distinct, there are no private targets, and bank
overlap has a genuine product-code geometry rather than one common bank.
The base incidence graph already contains an induced `2K2`: choose two
lines and, on each, a point absent from the other line.  Hence it is not
Ferrers.

Fix `r=2` and choose

\[
              t=\left\lceil {a(\log D)^2\over\log3}\right\rceil.
                                                                    \tag{17}
\]

Then `K=2^{(a+o(1))(log D)^2}` while (14)--(16) and Hall density `D`
remain exact.  This proves the scalable abstract barrier claimed in the
verdict.  It specifically kills an incidence-only continuation of
Theorems 1--2.  A geometric proof may still win because rooted planar
carrier graphs obey the Ferrers threshold and actual bad circuits create
the detached one-gap banks included in `mathcal B_c`.

## 4. Consequence for the Hall attack

The extremal-minimal route has therefore made one rigorous advance and
reached one rigorous wall.

1. A dense Hall obstruction plus the quadratic marked blocker reservoir
   forces a quadratic common `(p,F,tau)` fibre.  There is no remaining
   global mark, shield, edge, or tangent-cell overlap problem.
2. Context-decodable mixed outputs have size below `D^epsilon` in every
   context of the minimal obstruction.
3. High target degrees by themselves cannot align the omitted histories;
   the projective-plane tensor is a sharp scalable countermodel.

Thus the sole surviving statement is geometric: in the common
`(p,F,tau)` fibre, the omitted-petal collision system must either expose a
recoverable first-divergence/container profile whose detached faces are
already added to `mathcal U`, or create a large context-decodable splice
bank, contradicting Theorem 1.  This is exactly the planar ingredient not
present in the abstract tensor.  No proof of that final statement, and no
planar counterexample to it, was found here.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_dense_hall_rooted_fibre.py
```

The exact checker exhausts the private-target inequality over small set
systems, checks the marked localization bound, constructs `PG(2,r)` for
`r=2,3`, verifies degrees, line intersections, an induced `2K2`, and
unique Hall equality in the Fano plane, and audits the tensor formulas and
Hamming intersection law.
