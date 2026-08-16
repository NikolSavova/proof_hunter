# Pascal top layers give the live fixed-edge trace rectangle at the half boundary

**Date:** 2026-08-15. All logarithms are base two. This continues
`HIGH_RANK_FIXED_EDGE_CIRCUIT_DELETION_MATCHING_GATE.md`.

## Verdict

The proposed four-local Kruskal--Katona stability input is false at exactly
the coefficient-half boundary, even after retaining all of the following
features simultaneously:

* source rank \(r=(1-o(1))\log N\);
* one literal directed exposed edge \(uv\) in every source;
* a Cartesian source by pocket-face rectangle whose mass exceeds the whole
  parent face count by \(2^{\Theta(L\log L)}\);
* a singleton source trace at every source label; and
* \(\Omega(\log L)\) fully vertex-disjoint physical \(1+3\) circuits in
  every source--pocket pair.

For each fixed depth \(D\), balanced Pascal self-substitution gives a
rational stretchable left child \(Q_{k,D}\), of size \(N\), with

\[
 {\log V(Q_{k,D})\over(\log N)^2}
       ={1\over2}+{\beta-1/2\over D}+o_k(1),
 \qquad \beta=1-{1\over4\ln2}.                                  \tag{1}
\]

Its top face layer is within \(2^{O_D(L\log L)}\) of its whole face bank.
Localizing a common directed edge and projecting that layer down to rank
\(L-A\log L\) still leaves a family \(\mathcal A\) with

\[
             \log|\mathcal A|
                 \ge\log V(Q_{k,D})-K_D L\log L.                \tag{2}
\]

As the right child, take a much smaller central Pascal cell whose top layer
\(\mathcal H\) has

\[
                    \log|\mathcal H|=B L\log L+o(L\log L).      \tag{3}
\]

Choosing \(B>K_D\) gives

\[
 { |\mathcal A||\mathcal H|\over V(P)}
                       \ge2^{(B-K_D-o(1))L\log L},               \tag{4}
\]

where \(P=Q_{k,D}\prec Z\) and
\(\log V(P)=\log V(Q_{k,D})+o(L^2)\). Every top pocket face contains a
cap component of rank \(\Theta(\sqrt{L\log L})\). Its disjoint triples,
paired with distinct source labels, are bad \(1+3\) circuits. Thus (4) is
the literal live crossing-circuit rectangle, not merely an abstract
trace-complex example.

Letting first \(k\to\infty\), then choosing \(D\) large, makes the parent
coefficient in (1) arbitrarily close to \(1/2\) from above. Consequently no
stability theorem using only rank, common edge, four-locality, disjoint
trace/circuit matchings, and the \(2^{\Theta(L\log L)}\) rectangle surplus
can produce a uniform super-half gain or a multiplicative source-support
shield.

The scope qualification is essential: (1) is still **above** one half.
This does not construct a least fixed-gap counterexample and does not defeat
a theorem that genuinely uses the strict parent upper bound. It proves that
this minimizer upper bound (or an equivalent endpoint/profile mutation) is
the next indispensable input.

## 1. The fixed-depth Pascal coefficient

Put

\[
 S_k=T(2k-4,k-2),\qquad R_k={2k-4\choose k-2},                  \tag{5}
\]

and let \(Q_{k,D}\) be the \(D\)-fold sufficiently vertical rational
self-substitution of \(S_k\). Write \(\ell=\log R_k\). The maximum cap
and cup ranks of \(S_k\) are \(k-1\), and its maximum ordinary rank is
\(h_k=2k-4\). The central Pascal asymptotics and their graded versions are

\[
 \begin{aligned}
  \log V(S_k)&=\beta\ell^2+O(k\log k),\\
  \log C(S_k)=\log U(S_k)&={\beta\over2}\ell^2+O(k\log k),\\
  h_k/\ell&=1+O(\log k/k),\qquad
  (k-2)/\ell={1\over2}+O(\log k/k).                             \tag{6}
 \end{aligned}
\]

These are the latest-step path-product estimates for the central Pascal
cell. They hold coefficientwise for the maximum-rank terms: replacing each
total in (6) by its top coefficient changes its logarithm by
\(O(k\log k)\).

For fixed \(D\), retain only leading \(\ell^2\)-coefficients. If \(c_d\)
and \(w_d\) denote \(\log C(Q_{k,d})/\ell^2\) and
\(\log V(Q_{k,d})/\ell^2\), the graded strong-substitution recurrence gives

\[
       c_d={d\beta\over2}+{d(d-1)\over4},\qquad
       w_d=d\beta+{d(d-1)\over2}.                               \tag{7}
\]

Indeed the cap recurrence adds the top seed cap and
\((k-2)(d-1)\ell\); the face recurrence joins the two preceding endpoint
profiles to a top seed face. Since \(\log|Q_{k,D}|=D\ell\), (7) gives
exactly (1). The error accumulated in any fixed number of substitutions is
\(O_D(k\log k)=O_D(L\log L)\).

## 2. The top layer and the common edge

The maximum ordinary rank in \(Q_{k,D}\) is

\[
                         q=D(2k-4).                              \tag{8}
\]

Let \(T_{k,D}\) be the number of rank-\(q\) faces. The coefficientwise
version of (6), followed through the fixed number \(D\) of positive graded
recurrences, gives

\[
                  T_{k,D}\ge V(Q_{k,D}),2^{-O_D(k\log k)}.     \tag{9}
\]

Every rank-\(q\) face has \(q\) directed boundary edges, oriented with its
interior on the left. There are fewer than \(N^2\) physical directed edges,
so one \(uv\) belongs to a family \(\mathcal T_{uv}\) with

\[
                         |\mathcal T_{uv}|
                              \ge {qT_{k,D}\over N(N-1)}.        \tag{10}
\]

Put \(\Delta=A\log L\) and \(r=\lfloor L-\Delta\rfloor\). Take all
rank-\(r\) downfaces containing \(u,v\) from the faces in
\(\mathcal T_{uv}\), and call the distinct resulting family
\(\mathcal A\). Every member remains ordinary and retains the same literal
directed exposed edge. A fixed rank-\(r\) set lies in at most
\({N-r\choose q-r}\) rank-\(q\) sets. Hence

\[
 |\mathcal A|
   \ge {qT_{k,D}\over N(N-1)}
             {{q-2\choose r-2}\over {N-r\choose q-r}}.          \tag{11}
\]

Now

\[
       q-L=D(2k-4-\log R_k)=O_D(\log L),                         \tag{12}
\]

so \(q-r=O_D(\log L)\). Bounding the denominator in (11) by
\(N^{q-r}\) and using (9) proves (2). Notice that this is the actual
global overlap loss; no top face is treated as a private carrier.

## 3. A small low-face pocket supplies the live slack

Choose \(j=j(k)=o(k)\) so that, for a prescribed constant \(B>K_D\),

\[
             \log v_{2j-4}(S_j)=B L\log L+o(L\log L).            \tag{13}
\]

This is possible with \(j=\Theta(\sqrt{L\log L})\), by (6). Put
\(Z=S_j\), and let \(\mathcal H\) be its top ordinary layer. Its physical
size satisfies

\[
                 \log|Z|=\Theta(\sqrt{L\log L})=o(L),           \tag{14}
\]

so \(n=|Q_{k,D}|+|Z|=N(1+o(1))\).

Use the standard strong-glue chart

\[
                              P=Q_{k,D}\prec Z.                  \tag{15}
\]

In this chart a spanning face is a left cap joined to a right cup, and

\[
             V(P)=V(Q_{k,D})+V(Z)+C(Q_{k,D})U(Z).                \tag{16}
\]

Equations (6)--(7), (13), and \(j=o(k)\) imply

\[
 \begin{aligned}
  \log V(Z)&=O(L\log L),\\
  \log(C(Q_{k,D})U(Z))
        &={1\over2}\log V(Q_{k,D})+O(L\log L).
 \end{aligned}                                                   \tag{17}
\]

Thus \(V(P)=V(Q_{k,D})(1+o(1))\), logarithmically, and (2)--(3)
give (4).

This pocket is itself a low-face Pascal child, not a hidden Boolean cloud.
Its internal bank is exactly the source of the required quasipolynomial
factor, but that bank is reused against essentially all left sources. It
therefore cannot be counted once per source.

## 4. Every pair has the required physical circuit matching

The top-rank recurrence for

\[
       S_j=T(2j-4,j-2)=T(2j-5,j-3)\prec T(2j-5,j-2)             \tag{18}
\]

shows that every \(F\in\mathcal H\) is the union of a maximum cap in the
left child and a maximum cup in the right child. The cap component has
rank \(j-2\). In particular, \(F\) is not a cup, and its cap component can
be partitioned into

\[
                         s=\left\lfloor{j-2\over3}\right\rfloor \tag{19}
\]

pairwise disjoint non-cup triples \(J_1,\ldots,J_s\).

For any \(A\in\mathcal A\) and any distinct
\(y_1,\ldots,y_s\in A\), the four-sets

\[
                              \{y_i\}\cup J_i                  \tag{20}
\]

are nonordinary by the strong-glue classification: the left singleton is
a cap, while \(J_i\) is not a right cup. They are fully vertex-disjoint.
Moreover, for every \(y\in A\), using any one \(J_i\) shows that
\(\{y\}\) is a source trace. Therefore

\[
                    \tau_Y(A,F)=\nu_Y(A,F)=r,
 \qquad
                    \nu_\times(A,F)\ge\min\{r,s\}.              \tag{21}
\]

Since \(j=\Theta(\sqrt{L\log L})\), (21) supplies far more than the
\(\Theta(\log L)\) physical matching required by the live deletion gate.
The common edge \(uv\) is disjoint from all but at most two of the selected
source labels, exactly as in the fixed-edge matching theorem.

## 5. What this kills, and what it leaves

The source support contains no ordinary set larger than the maximum face
rank \(q=O(L)\). Hence it cannot contain a single convex Boolean shield of
rank \(\Omega(L\log L)\). Its many rank-\(r\) faces and their proper
downshadows are instead stored coherently in the Pascal hierarchy. The
smaller pocket does have \(2^{\Theta(L\log L)}\) top-face mass, but (16)
shows the exact reuse: it is one global child bank, not a multiplier of the
left source mass.

Thus the following implication is false without a minimizer hypothesis:

> high rank + common exposed edge + live rectangle surplus + many disjoint
> crossing circuits \(\Longrightarrow\) a multiplicative support shield or
> a uniform coefficient improvement above one half.

The construction is compatible with every local deletion, matching,
four-cover, and source-shadow identity currently banked. It is not
compatible with the strict fixed-gap parent upper. The surviving operation
must compare (16) to that upper bound, or derive a profile/mutation surplus
that is absent at equality. This is a substantially narrower target than a
four-local KK stability theorem.

## 6. Verification

Run

```text
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_pascal_top_layer_live_fixed_edge_stability_barrier.py
```

The verifier uses exact integer graded Pascal recurrences and exact rational
determinants. It checks (7) as a formal affine expression in \(\beta\),
audits top-layer concentration for central cells and fixed-depth iterates,
verifies the exact common-edge/downshadow incidence bound, and gives a
finite live ledger with \((k,D,j)=(12,3,24)\) in which
\(|\mathcal A||\mathcal H|/V(P)>2^{\lfloor L\rfloor\lceil\log L\rceil}\).
It also constructs the rational 26-point splice
\(T(4,2)\prec T(6,3)\), enumerates all 2,116 top pocket faces, and verifies
the common-edge source rectangle, singleton source traces, non-cup triple
witnesses, and the exact strong-glue face recurrence.
