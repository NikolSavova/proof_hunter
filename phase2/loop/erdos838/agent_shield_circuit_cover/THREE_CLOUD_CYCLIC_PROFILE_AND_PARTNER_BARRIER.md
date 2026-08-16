# Three nested vertex clouds: cyclic profile gate and partner anti-alignment

**Date:** 2026-08-15. This continues
`NESTED_TRIANGLE_VERTEX_CLOUD_FIXED_GAP_GATE.md`. It distinguishes a valid
conditional cyclic profile product from the false arbitrary-child cyclic
splice.

## Verdict

Three macroscopic clouds do not automatically recover the remaining
\(n^{\log_2 3+o(1)}\) fixed-gap factor.

Under an explicit **rectangular seam hypothesis**, there is an exact
load-one cyclic bank. If cloud \(i\) has face count \(H_i\), two directional
profile counts \(A_i,R_i\), and surplus

\[
                         \sigma_i={A_iR_i\over H_i},        \tag{1}
\]

then the best of the three one-gap banks satisfies

\[
       \max_i B_i\ge
       (H_1H_2H_3)^{1/3}(\sigma_1\sigma_2\sigma_3)^{1/3}. \tag{2}
\]

This is sharp at the scalar level. The cap--cup encoding supplies only
\(\sigma_i\ge1\), so for comparable clouds (2) returns one cloud-sized bank,
not the additional polynomial. To close the fixed gap through this route
one needs

\[
                  (\sigma_1\sigma_2\sigma_3)^{1/3}
                         \ge n^{\log_2 3+o(1)}.             \tag{3}
\]

More importantly, strict triangle nesting does not imply the rectangular
seam hypothesis. An exact rational nested-shell family has every
cross-cloud \(2+2\) edge pair convex, yet a positive-density family of
cyclic \(1+3\) circuits is perfectly anti-aligned:

* for a three-label face in one cloud and a same-layer choice from either
  of the other two clouds, exactly one choice is convex;
* the bad choice always hides the middle-layer label of the triple; and
* deleting that hidden label and inserting the unused same-layer third
  vertex is still nonconvex.

The finite configuration admits a rational lexicographic blow-up to
arbitrarily many nested layers while preserving a positive density of these
records. Thus neither pairwise edge compatibility nor the actual third
triangle vertex forces a cyclic repair.

This is not a sub-half construction. The good half of the rank-four records
is an ordinary polynomial bank, and other multi-label profiles may pay.
What is ruled out is an unconditional one-face theorem based only on three
clouds, triangle nesting, and the same-layer partner operation.

## 1. The valid conditional cyclic inequality

Let \(X_1,X_2,X_3\) be disjoint physical clouds. For each \(i\), let
\(\mathcal A_i,\mathcal R_i\subseteq\mathcal F(X_i)\) be two recoverable
directional profile families, with sizes \(A_i,R_i\). Assume:

1. the usual boundary-pair map injects \(\mathcal F(X_i)\) into
   \(\mathcal A_i\times\mathcal R_i\), so \(A_iR_i\ge H_i\); and
2. for every \(i\) modulo three, every union
   \[
                    R\cup A,qquad
                    R\in\mathcal R_{i-1},\quad
                    A\in\mathcal A_{i+1},                 \tag{4}
   \]
   is an ordinary face.

The second assumption is the rectangular seam hypothesis. It holds in an
actual infinitesimal radial/lexicographic three-cluster product. It is not a
consequence of nesting, same-type singleton transversals, or strong
separation alone.

> **Theorem 1 (conditional three-cycle bank).** Under assumptions 1--2,
> the gap-\(i\) bank has
> \[
>                         B_i=R_{i-1}A_{i+1},              \tag{5}
> \]
> with decoder load one, and (2) holds.

**Proof.** Since the clouds are disjoint, intersecting the union (4) with
the two physical clouds recovers both traces. Hence the map is injective
and proves (5). Cyclic multiplication gives

\[
       B_1B_2B_3=(A_1R_1)(A_2R_2)(A_3R_3)
                 =(H_1H_2H_3)(\sigma_1\sigma_2\sigma_3).  \tag{6}
\]

Taking a geometric mean proves (2). \(\square\)

There is no hidden polynomial in this identity. Abstractly, taking
\(A_i=R_i=q\) and \(H_i=q^2\) gives equality \(B_i=H_i\) for all three
gaps. This scalar equality is not claimed as a realized order type; it
shows exactly which additional geometric statement is needed: a lower
bound on endpoint surplus, not another application of cyclic averaging.

At the vertex-cloud scale, strong induction gives

\[
                         H_i\ge2^{\Phi_C(L-\log_2 3+o(1))}.
                                                                  \tag{7}
\]

Equations (2) and (7) reach the ambient target precisely when (3) holds.
Thus the cyclic route converts the remaining problem into a quantitative
three-direction surplus theorem.

## 2. Exact nested cyclic anti-alignment

Use the deterministic rational/integer nested triangles from
`verify_first_incoherent_sibling_nested_triangle_barrier.py`, with ten
layers

\[
                         T_t=\{x_{t,0},x_{t,1},x_{t,2}\},
                         \qquad 0\le t<10,                 \tag{8}
\]

and cloud \(X_a=\{x_{t,a}:0\le t<10\}\). All thirty shell labels, together
with the five-point central child, are in general position, and the
triangles are strictly nested.

### Proposition 2 (edge-good, triple-bad cycle)

The following statements hold exactly.

1. For every two colors \(a\ne b\), every two-label trace in \(X_a\) and
   every two-label trace in \(X_b\) have convex union. There are \(6075\)
   such cross-cloud edge pairs.
2. Fix a color \(a\), layers \(i<j<k\), and a layer \(t\). Let \(b,c\) be
   the other two colors. Exactly one of
   \[
    \{x_{i,a},x_{j,a},x_{k,a},x_{t,b}\},\qquad
    \{x_{i,a},x_{j,a},x_{k,a},x_{t,c}\}                  \tag{9}
   \]
   is convex.
3. In the bad set in (9), the unique hidden point is \(x_{j,a}\).
4. The natural third-partner release
   \[
                         \{x_{i,a},x_{k,a},x_{t,b},x_{t,c}\} \tag{10}
   \]
   is nonconvex.

The verifier checks all

\[
                         3\binom{10}{3}10=3600            \tag{11}
\]

records. Thus every record has one load-one rank-four face in (9), one
strict \(1+3\) circuit, and zero successful outputs of form (10).

This is genuine three-cloud anti-alignment. Pairwise edge modules are
perfectly compatible, so a theorem restricted to \(2+2\) cross circuits
sees no obstruction. The failure begins at a local rank-three profile and
persists after using the actual third vertex from its triangle layer.

## 3. Scalable rational blow-up

The finite obstruction scales while preserving a positive density of
records.

> **Proposition 3 (positive-density blow-up).** For every \(q\ge1\), there
> is a rational general-position family of \(10q\) strictly nested rainbow
> triangles in which at least \(3600q^4\) macro-distinct records satisfy
> items 2--4 of Proposition 2. All cross-cloud edge pairs whose four labels
> lie in four distinct base cells retain item 1.

**Construction.** The base configuration has finitely many strict
orientation, containment, hidden-point, and release-failure inequalities.
Choose one rational point \(o\) in the innermost triangle. Around every base
triangle \(T_t\), take \(q\) sufficiently close rational homothetic copies
about \(o\), strictly ordered by scale. Make their scale interval much
smaller than the containment margin to the adjacent base triangles. The
resulting \(10q\) triangles are totally nested.

Each of the thirty base vertices has now become a small cell of \(q\)
physical labels. Choose the cells so small that every representative choice
preserves all strict base signs. A final generic rational perturbation,
smaller than all margins, gives general position and preserves nesting.

For each base color, base triple \(i<j<k\), base partner layer \(t\), three
independent micro choices in the triple cells, and one synchronized micro
choice in the partner triangle, Proposition 2 survives. This gives exactly
\(3600q^4\) certified anti-aligned records. \(\square\)

The blow-up is a scalable obstruction to the local repair operation, not an
upper bound for the full ambient face complex. In particular, the good
choice in (9) itself gives \(\Theta(q^4)\) distinct rank-four faces, and
arbitrary internal cell profiles remain uncounted.

## 4. Consequence for the fixed-gap proof

There are now two honest branches.

### Seam-separated branch

If the actual nested clouds admit recoverable profile families satisfying
the full rectangular hypothesis (4), Theorem 1 applies. Closure still
requires the endpoint-surplus bound (3). The cyclic identity alone only
returns the geometric mean cloud bank.

### Incoherent branch

If (4) fails, a bad union contains a cross-cloud four-circuit. Proposition
2 shows that even the favorable situation “all edge pairs good” does not
force a third-cloud repair: concentrated \(1+3\) circuits can cycle and the
same-layer partner can remain bad. A positive theorem must retain more than
the layer and colors—at least the hidden middle label and its two tangent
neighbors—or globally charge the polynomial rank-four release bank with
the rich cloud face history.

This avoids the false arbitrary-child cyclic splice. No product of local
profiles is asserted until its complete Cartesian seam compatibility has
been proved.

## 5. Verification

Run

~~~text
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_three_cloud_cyclic_profile_and_partner_barrier.py
~~~

The verifier checks 729 exact scalar cyclic identities, all 6075
cross-cloud edge pairs, all 3600 cyclic triple records, their hidden labels,
and the failure of every same-layer third-partner release.

