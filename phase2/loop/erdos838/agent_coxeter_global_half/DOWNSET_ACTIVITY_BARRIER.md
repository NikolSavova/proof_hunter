# Coxeter path states: the Ferrers-injection ceiling

**Date:** 2026-08-15
**Verdict:** there is a sharp cross-activity inequality for every genuine
reflection-order endpoint cell.  With

\[
 \alpha=\log_2(3/2),
\]

the activity-one rectangle area \(X_{uv}\) and the half-weight endpoint mass
\(G_{uv}(1/2)\) satisfy

\[
 \boxed{G_{uv}(1/2)\ge\frac14X_{uv}^{\alpha}.}
\]

Consequently a vertex Ferrers state \(D_v\) satisfies

\[
 \boxed{\sum_{u<v}G_{uv}(1/2)\ge\frac14|D_v|^{\alpha}.}
\]

This is optimal cellwise, even for stretchable all-cup orders.  It also
shows decisively why a vertex injection into endpoint-path downsets cannot
by itself control the half-weight ratio.  Distinct Ferrers downsets force
only

\[
   \Theta\!\bigl(n(\log n)^2\bigr)
\]

total activity-one area, and the sharp cross-activity theorem converts this
to only \(n(\log n)^{2\alpha}\) half mass.  Both bounds are weaker than the
universal contribution of all triples.  At activity one-half, distinctness
of the dyadic states by itself has no superlinear area consequence at all.
A useful downset route therefore needs a new quantitative separation or
multiplicity statement; the Baek--Balko-style injection alone cannot supply
the missing factor \(n^{1-o(1)}\).

This note does not claim a counterexample to

\[
 H(R)=\frac{nF_R(1/2)}{F_R(1)}=n^{o(1)}.
\]

It is a scope-safe obstruction to one proposed proof interface.

## 1. The abstract Ferrers problem

A finite downset of \(\mathbb N^2\) is a Ferrers diagram.  Let

\[
  A_N=\min\left\{\sum_{j=1}^N |D_j|:
       D_1,\ldots,D_N\subset\mathbb N^2
       \text{ are pairwise distinct finite downsets}\right\}.
\]

> **Theorem 1 (sharp distinct-downset scale).**
> \[
>   \boxed{A_N=\Theta\!\bigl(N(\log N)^2\bigr).}
> \]

**Proof.**  Downsets of area \(m\) are in bijection with integer partitions
of \(m\); write their number as \(p(m)\).  The partition generating function
and the elementary exponential bound give, for every \(x>0\),

\[
\begin{aligned}
 p(m)e^{-xm}
 &\le \prod_{k\ge1}(1-e^{-xk})^{-1},\\
 \log\prod_{k\ge1}(1-e^{-xk})^{-1}
 &=\sum_{r,k\ge1}\frac{e^{-xkr}}r
 \le \frac1x\sum_{r\ge1}\frac1{r^2}
 =\frac{\pi^2}{6x}.
\end{aligned}
\]

Taking \(x=\pi/\sqrt{6m}\) yields

\[
 p(m)\le \exp\!\left(\pi\sqrt{\frac{2m}{3}}\right).       \tag{1}
\]

Hence the number of downsets of area at most \(M\) is at most

\[
 (M+1)\exp\!\left(\pi\sqrt{\frac{2M}{3}}\right).          \tag{2}
\]

Choose \(M=c(\log N)^2\) with a sufficiently small absolute \(c>0\).
For all large \(N\), (2) is at most \(N/2\).  At least \(N/2\) of the
selected diagrams then have area greater than \(M\), proving
\(A_N=\Omega(N(\log N)^2)\).

For the reverse bound, put \(r=\lceil\log_2N\rceil\).  Every subset of
\(\{1,\ldots,r\}\) is a partition into distinct parts, and all these
partitions have size at most \(r(r+1)/2\).  They give at least \(N\)
distinct Ferrers diagrams, each of area \(O((\log N)^2)\).  Thus
\(A_N=O(N(\log N)^2)\).  \(\square\)

## 2. A sharp cross-activity theorem for temporal paths

Fix a type-A reflection order and endpoints \(u<v\).  A temporal path from
\(u\) to \(v\) is encoded by its set of internal vertices.  These supports
form a downset.  Indeed, if consecutive path edges are \((a,b),(b,c)\), the
reflection-order packet axiom places \((a,c)\) strictly between them.  Thus
shortcutting \(b\) preserves the temporal direction, and repeated shortcuts
delete an arbitrary subset of internal vertices.

The required weighted fact is true for every Boolean downset.

> **Theorem 2 (downset activity interpolation).**  Let \(\mathcal L\) be a
> finite downset of subsets and let \(0<h\le1\).  Put
> \(\alpha_h=\log_2(1+h)\).  Then
> \[
>  \boxed{\sum_{S\in\mathcal L}h^{|S|}
>         \ge |\mathcal L|^{\alpha_h}.}                  \tag{3}
> \]

**Proof.**  Induct on the ground-set size.  Split on one label.  The
zero-section and stripped one-section are downsets \(\mathcal L_0\) and
\(\mathcal L_1\), with \(\mathcal L_1\subseteq\mathcal L_0\).  Write
\(a=|\mathcal L_0|\), \(b=|\mathcal L_1|\), so \(0\le b\le a\).  Induction
gives

\[
 Z_{\mathcal L}(h)
 \ge a^{\alpha_h}+h b^{\alpha_h}.                    \tag{4}
\]

For \(x=b/a\), it remains to prove
\(1+hx^{\alpha_h}\ge(1+x)^{\alpha_h}\).  After division by
\(x^{\alpha_h}\), this is

\[
 (1+x^{-1})^{\alpha_h}-(x^{-1})^{\alpha_h}\le h.     \tag{5}
\]

The left side is the unit increment of the concave function
\(y\mapsto y^{\alpha_h}\), evaluated at \(y=x^{-1}\ge1\).  It is at most
its value at \(y=1\), namely \(2^{\alpha_h}-1=h\).  This proves (3).
\(\square\)

Write a temporal path polynomial as

\[
 P_{uv}(t)=t\sum_{S\in\mathcal L_{uv}}t^{|S|}.          \tag{6}
\]

At \(h=1/2\), Theorem 2 gives the exact reflection-order inequality

\[
 \boxed{P_{uv}(1/2)\ge\frac12P_{uv}(1)^\alpha,
        \qquad \alpha=\log_2(3/2).}                    \tag{7}
\]

Apply (7) to the forward and reverse temporal path families.  If

\[
 X_{uv}=R_{uv}(1)B_{uv}(1),\qquad
 G_{uv}(t)=R_{uv}(t)B_{uv}(t),
\]

then

\[
 \boxed{G_{uv}(1/2)\ge\frac14X_{uv}^{\alpha}.}         \tag{8}
\]

This exponent is optimal in genuine stretchable orders.  For points on a
strict cup, one endpoint direction is direct and the other admits every
subset of the internal vertices.  With \(m\) internal vertices,

\[
 X_{uv}=2^m,\qquad G_{uv}(1/2)=\frac14(3/2)^m
 =\frac14X_{uv}^{\alpha}.                              \tag{9}
\]

Now let \(D_v\) be the union of the integer rectangles of areas \(X_{uv}\).
Since \(0<\alpha<1\),

\[
\begin{aligned}
 \sum_{u<v}G_{uv}(1/2)
 &\ge\frac14\sum_{u<v}X_{uv}^{\alpha}\\
 &\ge\frac14\left(\sum_{u<v}X_{uv}\right)^\alpha
 \ge\boxed{\frac14|D_v|^\alpha}.                    \tag{10}
\end{aligned}
\]

Equation (10) is the strongest direct conversion obtained here from the
integer Ferrers state to the weighted endpoint polynomials.  The Boolean
cup example prevents any larger universal exponent in (8), so an
improvement must couple different cells or different vertices.

## 3. Consequence for endpoint path-state injections

For an increasing endpoint pair \(u<v\), let \(R_{uv}(1)\) and
\(B_{uv}(1)\) be the two integer monotone-path counts.  A common split-state
construction assigns to each right endpoint \(v\) a downset generated by
the rectangles

\[
 [R_{uv}(1)]\times[B_{uv}(1)],\qquad u<v.             \tag{11}
\]

Suppose one proves that the \(n\) endpoint downsets are distinct.  Even
granting that assertion, union area gives only

\[
 |D_v|\le \sum_{u<v}R_{uv}(1)B_{uv}(1).              \tag{12}
\]

Theorem 1 therefore yields at most the state-counting conclusion

\[
 \sum_{u<v}R_{uv}(1)B_{uv}(1)
 \ge \Omega\!\bigl(n(\log n)^2\bigr).                \tag{13}
\]

But the face polynomial already contains every triple, so

\[
 F_R(1)\ge1+n+\binom n2+\binom n3=\Theta(n^3).        \tag{14}
\]

Thus (13) is not merely short of the quasipolynomial target: it is weaker
than a rank-three fact which costs no downset machinery.  Iterating ordinary
hereditary lifting does not repair this deficit, by the exact
hereditary-multiplicity barrier already banked elsewhere in the campaign.

The weighted conversion (10) does not change the verdict.  The proof of
Theorem 1 shows that, among \(n\) distinct integer downsets, the minimum of
\(\sum_v|D_v|^\alpha\) is

\[
 \Theta\!\left(n(\log n)^{2\alpha}\right).             \tag{15}
\]

Consequently (10) guarantees only that order of half-weight endpoint mass.
But every triple is convex and has weight \(1/8\), so already

\[
 F_R(1/2)\ge\frac18\binom n3=\Theta(n^3).              \tag{16}
\]

Thus even the sharp cross-activity theorem is quantitatively dominated by
the complete three-skeleton.

The conclusion is deliberately limited.  A downset theorem could still be
useful if it controlled more than distinctness, for example:

* exponential separation between successive boundary profiles;
* a weighted area dilation from activity \(1/2\) to activity \(1\);
* many independently decodable downsets per endpoint; or
* compatibility across nested endpoints with subquadratic history fibres.

None of these follows from the injective state label itself.

## 4. Why distinctness at activity one-half destroys the integer gain

At activity \(h=1/2\), the path values \(R_{uv}(h),B_{uv}(h)\) are positive
dyadic rationals.  Pairwise distinct real Ferrers regions can be arbitrarily
close.  Explicitly, for \(1\le j\le N\) and \(\delta=2^{-N}\), take

\[
 D_j=[0,h+j\delta]\times[0,h].                       \tag{17}
\]

These are \(N\) distinct dyadic downsets, but

\[
 \sum_{j=1}^N\operatorname{area}(D_j)
 =Nh^2+\frac{h\delta N(N+1)}2
 =\frac N4+o(1).                                      \tag{18}
\]

The collapse persists even if the coordinates are evaluations of
nonnegative integer path-shaped polynomials.  Put

\[
 P_j(t)=t+jt^N,\qquad Q_j(t)=t.                       \tag{19}
\]

At \(t=1\), the rectangles have distinct integral widths \(j+1\).  At
\(t=1/2\), their total area is

\[
 \sum_{j=1}^N P_j(1/2)Q_j(1/2)
 =\frac N4+\frac{N(N+1)}{2^{N+2}}.                    \tag{20}
\]

Equation (19) is an abstract polynomial obstruction, not a claim that this
particular list is realized simultaneously by one reduced word.  Its role
is logical: positivity, integrality of coefficients, a direct-root term,
and distinct activity-one states still do not imply quantitative separation
at activity one-half.  A Coxeter proof must use packet geometry or a global
activity coupling beyond those data.

## 5. Surviving Coxeter target

The exact finite inequality \(F_R(1)\ge(n/2)F_R(1/2)\) is already false for
a certified 58-wire reduced word.  The live statement is only

\[
 \log\frac{F_R(1)}{F_R(1/2)}\ge(1-o(1))\log n.          \tag{21}
\]

Theorems 1--2 and (15)--(20) show that the split-state injection cannot
establish (21) even after using the optimal cellwise activity interpolation.
It must be augmented by a theorem coupling different cells or vertices: for
example, bounded multiscale capture loss in the cell Bellman inequality, or
a global tangent-pocket/link inequality.  Merely proving that all vertex
downsets differ should no longer be treated as a candidate closing lemma.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_coxeter_global_half/verify_downset_activity_barrier.py
```

The checker computes partition numbers exactly, reconstructs the true
minimum total area of \(N\) distinct integer Ferrers diagrams for a finite
range, exhausts all Boolean downsets on four labels against Theorem 2, checks
the distinct-part upper construction and the sharp Boolean equality, verifies
the dyadic collapse with `Fraction` arithmetic, and replays (7)--(10) on the
certified 58-wire reduced word.
