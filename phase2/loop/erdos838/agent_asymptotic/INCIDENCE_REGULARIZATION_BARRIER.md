# Incidence barriers for regularization approaches to Erdős 838

All logarithms are base two.  Let \(V(P)\) denote the number of nonempty
subsets of a planar point set \(P\) that are in convex position.  This note
asks whether one can beat the square loss of a single structured extraction
by applying the extractor in *every* intermediate-size subset and aggregating
all resulting witnesses.

The answer is negative for the two standard pipelines.  There is an exact
finite incidence inequality behind this: moving a local convex witness from a
\(t\)-set into an \(n\)-set pays precisely for the logarithmic size of that
witness, and no extra gain comes merely from running over all \(t\)-sets.

## 1. The finite incidence lift

> **Lemma 1 (incidence lift).**  Let \(P\) have \(n\) points and let
> \(1\le h\le t\le n\).  Suppose every \(t\)-point subset \(T\subseteq P\)
> contains at least \(A\) convex subsets of cardinality at least \(h\).  Then
> \[
>  V(P)\ge
>  A\,{\binom nt\over\binom{n-h}{t-h}}
>  =A\,{\binom nh\over\binom th}
>  \ge A\left({n\over t}\right)^h.                 \tag{1}
> \]

### Proof

Count incidences \((T,K)\), where \(|T|=t\), \(K\subseteq T\), \(K\) is
convex, and \(|K|\ge h\).  The hypothesis supplies at least
\(A\binom nt\) incidences.  A fixed convex \(k\)-set occurs in exactly
\(\binom{n-k}{t-k}\) choices of \(T\).  This quantity is nonincreasing in
\(k\), so every eligible \(K\) occurs at most
\(\binom{n-h}{t-h}\) times.  This proves the first inequality.  The identity
is the standard two-way count of a pair consisting of an \(h\)-set inside a
\(t\)-set.  Finally,
\[
 {\binom nh\over\binom th}
 =\prod_{i=0}^{h-1}{n-i\over t-i}\ge(n/t)^h.
 \]
\(\square\)

The lemma counts all local witnesses, not one arbitrarily selected witness.
It therefore already captures the most obvious proposed repair to the
single-extraction square law.

## 2. Applying every structured extraction still squares its exponent

Let \(\mathcal D\) be a hereditary class of point sets and suppose that

1. every \(t\)-point set contains a member of \(\mathcal D\) of size
   \(q=t^{\alpha-o(1)}\); and
2. every \(q\)-point member \(Q\in\mathcal D\) satisfies
   \[
     \log V(Q)\ge(c-o(1))(\log q)^2.              \tag{2}
   \]

The class of (mirror-)decomposable sets is hereditary, and the theorem in
the present Erdős 838 draft has \(c=1/2\) for that class.

Because \(\mathcal D\) is hereditary, a lower bound on the extracted size can
be replaced by any prescribed smaller size.  Thus, uniformly over all
\(t\)-sets, we may take the same integer
\(q=\lfloor t^{\alpha-o(1)}\rfloor\); this removes any issue of different
ambient \(t\)-sets producing differently sized witnesses.

The total mass in (2) cannot all lie on very small subsets.  For fixed
\(\varepsilon>0\), the number of subsets of \(Q\) of size less than
\[
 h=(c-\varepsilon)\log q
\]
is at most
\[
 \sum_{j<h}\binom qj
 \le q^{h+1}
 =2^{(c-\varepsilon+o(1))(\log q)^2}.
\]
Consequently, after slightly decreasing \(\varepsilon\), every such \(Q\)
has
\[
 A=2^{(c-o(1))(\log q)^2}                         \tag{3}
\]
convex subsets of size at least \((c-o(1))\log q\).

Apply this inside every \(t\)-subset of an \(n\)-point set and use Lemma 1.
Write
\[
 L=\log n,\qquad \log t=(\beta+o(1))L,
 \qquad \log q=(\alpha\beta+o(1))L.
\]
Equations (1)--(3) give
\[
 \log V(P)\ge
 \left(c\alpha^2\beta^2+c\alpha\beta(1-\beta)-o(1)\right)L^2. \tag{4}
\]
Optimizing over \(0<\beta\le1\), the coefficient supplied by this
all-subsets incidence lift is
\[
 \boxed{
 \begin{cases}
 c\alpha^2,&\alpha\ge1/2,\\[2mm]
 \displaystyle {c\alpha\over4(1-\alpha)},&0<\alpha<1/2.
 \end{cases}}                                                   \tag{5}
\]
Indeed, the quadratic in (4) is
\(c\alpha\bigl(\beta-(1-\alpha)\beta^2\bigr)\); its stationary point is
\(1/(2(1-\alpha))\).

The relevant case is \(\alpha\ge1/2\).  There, (5) is exactly the
coefficient obtained by applying the structured theorem once to a largest
available extraction.  Running the extractor in every polynomial-scale
subconfiguration and retaining *all* its internal convex-subset mass gives
no improvement.

For the sharp decomposable theorem \(c=1/2\), a hypothetical
\(t^{1/2-o(1)}\)-point decomposable extraction would still transfer only
coefficient \(1/8\).  More generally, even this incidence-amplified route
beats \(1/4\) only when
\[
 \alpha>1/\sqrt2,
\]
and reaches \(1/2\) only for \(\alpha=1-o(1)\).  Thus the near-spanning
target from `FULL_REGULARIZATION_TRANSFER.md` is unchanged after the most
natural nonlocal aggregation over all ambient \(t\)-sets.

The known mutually-avoiding-pair theorem does not actually produce a
decomposable union of size \(t^{1/2-o(1)}\).  The preceding \(1/8\) statement
is deliberately more optimistic: even granting that stronger conclusion
would not suffice.

## 3. Same-type transversals have an invariant ceiling

There is an even cleaner calculation for same-type regularization.

> **Lemma 2 (transversal incidence lift).**  Suppose every \(t\)-point
> subset of \(P\) contains disjoint blocks \(B_1,\ldots,B_k\), each of size
> \(s\), such that every transversal choosing one point from each \(B_i\)
> is in convex position.  Then
> \[
>  v_k(P)\ge s^k{\binom nt\over\binom{n-k}{t-k}}
>            =s^k{\binom nk\over\binom tk}
>            \ge s^k(n/t)^k.                     \tag{6}
> \]

### Proof

Each \(t\)-set supplies \(s^k\) convex \(k\)-sets.  Count the pairs
\((T,K)\), and observe that each convex \(k\)-set is contained in exactly
\(\binom{n-k}{t-k}\) of the \(t\)-sets.  The last inequality is the one in
Lemma 1. \(\square\)

Suppose the regularization guarantee has the asymptotic form
\[
 s\ge t\,2^{-\gamma k-o(\log n)}.                 \tag{7}
\]
Here one factor \(2^{-k+o(k)}\) is the initial partition into
\(ES(k)=2^{k+o(k)}\) blocks; if the same-type theorem retains a fraction
\(m^{-d+o(1)}\), then \(\gamma=d+1\).

Combining (6) and (7) cancels the intermediate scale \(t\):
\[
 \log v_k(P)\ge k(\log n-\gamma k)-o((\log n)^2). \tag{8}
\]
If \(k=(x+o(1))\log n\), the coefficient is
\[
 x-\gamma x^2\le {1\over4\gamma}.                \tag{9}
\]

Thus applying the same-type lemma in every \(t\)-point subconfiguration,
counting all of its transversals, and lifting them by incidence gives
exactly the same ceiling as the one-shot pipeline:

* even a perfect same-type step has \(\gamma=1\), hence ceiling \(1/4\);
* the Bukh--Vasileuski retention exponent \(d=4\) has \(\gamma=5\), hence
  ceiling \(1/20\).

This calculation is independent of the chosen intermediate scale and hence
also blocks choosing many different scales and taking the best resulting
bound.  Summing the lower bounds over all \(n\) possible integer scales can
add at most \(\log n=o((\log n)^2)\) to their logarithm, so it cannot improve
the leading coefficient either.  It does not block a proof that combines
compatible choices from several blocks with multiple occupancy; such a proof
would no longer be a transversal-only argument.

## 4. Endpoint marginals do not force forward alignment

There is also a concrete obstruction to replacing compatibility by separate
lower bounds on total cap and cup mass.  In an ordered heterogeneous strong
composition with clusters \(Q_1,\ldots,Q_r\), the unavoidable two-cluster
term is
\[
 F=\sum_{i<j} C(Q_i)U(Q_j).                       \tag{10}
\]
The order in (10) is essential.

> **Lemma 3 (endpoint anti-alignment).**  For arbitrarily large \(m,r\)
> there are valid clusters, all of size \(m\), for which
> \[
>  \sum_i C(Q_i),\ \sum_i U(Q_i)=\Theta(r2^m),
> \]
> but, in the displayed order,
> \[
>  F=O(r^2m^2 2^m+r^2m^4).
> \]
> Hence \(F/((\sum C)(\sum U))=2^{-m+O(\log m)}\), even though both
> endpoint marginals are exponentially large.

### Proof

Take the first \(\lfloor r/2\rfloor\) clusters to be \(m\)-point cups and
the remaining clusters to be \(m\)-point caps.  In general position, an
all-cup cluster has
\[
 (C,U)=\left(m+\binom m2,,2^m-1\right),
\]
because only its one- and two-point subsets are caps; an all-cap cluster has
the two coordinates reversed.  Thus both marginal sums are
\(\Theta(r2^m)\).  A pair of cup clusters or a pair of cap clusters
contributes \(O(m^2 2^m)\) to (10), while a cup cluster followed by a cap
cluster contributes only \(O(m^4)\).  There are fewer than \(r^2\) pairs,
which proves the asserted bound.  These are genuine geometric clusters:
insert sufficiently small affine copies at the points of any vertical
composition template.  \(\square\)

Reversing the two groups changes the cross-group contribution from
\(O(r^2m^4)\) to \(\Theta(r^2 4^m)\).  Thus even cluster sizes and the two
endpoint marginals together miss an exponentially consequential ordering
variable.  A useful many-piece theorem must control a forward-aligned
quantity such as (10) itself (or a higher-occupancy analogue), not merely
show that many caps and many cups exist somewhere.

## 5. What multiplicity would actually have to supply

Polynomially many disjoint structured pieces do not change any quadratic
coefficient: summing their internal convex counts adds only \(O(\log n)\)
to the logarithm.  To exploit \(t^{1/2}\)-scale decomposable pieces one
therefore needs cross-piece convex subsets, not merely many copies of the
one-piece theorem.

At the full scale, one \(n^{1/2}\)-point decomposable piece supplies only
\[
 2^{(1/8-o(1))(\log n)^2}
\]
convex subsets.  Effective aggregation would need the following additional
numbers of *distinct* compatible witnesses:

* \(2^{(1/8-o(1))(\log n)^2}\) beyond the one-piece mass merely to reach
  the known universal coefficient \(1/4\);
* \(2^{(3/8-o(1))(\log n)^2}\) beyond it to reach coefficient \(1/2\).

Equivalently, the missing statement must create products across many
pieces, as the strong-tree recurrence does.  Standard mutually avoiding
extraction gives one pair, and standard same-type regularization gives
single-occupancy transversals.  Neither supplies this multiplicative
compatibility.

## 6. Consequence for the structural lane

The following avenues are now rigorously separated.

1. **One structured subset:** needs size \(n^{1-o(1)}\) to preserve the
   coefficient \(1/2\).
2. **The extractor in every \(t\)-subset:** Lemma 1 and (5) show that this
   does not relax the near-spanning requirement when the extraction exponent
   is at least \(1/2\).
3. **Same-type transversals at every scale:** Lemma 2 shows that the initial
   partition entropy remains and enforces the coefficient \(1/(4\gamma)\).
4. **Polynomially many structured pieces:** summing their internal counts
   is negligible on the quadratic logarithmic scale.

Any successful regularization proof must therefore establish at least one
of the following genuinely stronger facts:

* a near-spanning decomposable extraction;
* multiple-occupancy compatibility across many regularized blocks;
* or an approximate decomposition in which every defect is charged to a
  new family of convex subsets.

The second option should be formulated directly in endpoint language: one
needs many products of cap mass from an earlier piece with cup mass from a
later piece.  Existence of many pieces without such forward endpoint
alignment cannot affect the leading coefficient.
