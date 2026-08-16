# Exact hull-root envelope and the chart-reset gate

**Date:** 2026-08-15. All logarithms are base two.

## Verdict

Let \(V(P)\) be the number of nonempty subsets of a generic planar point set
\(P\) in convex position, and let

\[
 f(n)=\min_{|P|=n}V(P).
\]

For a generic directional chart \(\theta\) of an \(n\)-point realization
\(Q\), let \(C_\theta(Q)\) be its nonempty cap count. Then the hull-root
envelope is an **exact recurrence**:

\[
 \boxed{
 f(n+1)=1+\min_{|Q|=n,\,\theta}
              \{V(Q)+C_\theta(Q)\}.}
 \tag{1}
\]

Here realizations of every order type are included in the minimum. Equivalently,
one may let \(\theta\) range over root-admissible projective charts: charts
obtained by sending a supporting line through a deleted hull vertex to the line
at infinity. Thus (1) does not assert that one fixed realization of \(Q\)
supports every chart.

Define the literal one-seam cost

\[
 K_{n,1}:=\min_{|Q|=n,\,\theta}
 \{V(Q)-f(n)+C_\theta(Q)\}.                               \tag{1a}
\]

Then (1) is exactly

\[
 \boxed{f(n+1)=f(n)+1+K_{n,1},}
 \qquad
 \boxed{f(n)=f(n-1)+1+K_{n-1,1}\quad(n\ge2).}           \tag{1b}
\]

Iterating (1) does not, by itself, turn the hinged prefix-free Kraft theorem
into half growth. Along an extreme flag the exact dynamic is

\[
 \boxed{V(P_n)=n+\sum_{k=1}^{n-1}C_{\theta_k}(P_k),}
 \qquad |P_k|=k,                                      \tag{2}
\]

but the state at time \(k\) is the full order type of \(P_k\) together with
its newly available root charts. The selected evolution is a path, not an
exponentially branching finite grammar.

In one chart, the Kraft theorem does give the strongest clean multiplicative
inequality

\[
 \boxed{C_\theta(Q)U_\theta(Q)\kappa_\theta(Q)\ge n^3,}
 \qquad
 \kappa_\theta(Q)=\sum_i2^{-\alpha_i-\beta_i}\le1,    \tag{3}
\]

where \(U_\theta(Q)\) is the cup count and \(\alpha_i,\beta_i\) are the
hinged endpoint ranks. Nevertheless, (2)--(3) yield only polynomial growth.
A scalar model satisfying the exact recurrence, the endpoint banks, and the
Kraft inequality for every \(n\ge20\) has

\[
 C_n=U_n=\binom{n+1}{2},\qquad
 V_n=n+\binom{n+1}{3}=\Theta(n^3).                       \tag{4}
\]

Therefore any half-growth proof through successive hull-root charts needs a
new **chart-coherence or shelling-multiplicity theorem**. It must either keep
hinged responsibilities aligned through recharting, or turn many alternative
hull-root flags into disjoint ordinary faces. Chartwise Kraft plus the exact
one-root recurrence is insufficient.

Exact verifier:

```text
python3 phase2/loop/erdos838/agent_hull_root_envelope_dynamic/verify_hull_root_envelope.py
```

It directly enumerates all ordinary faces and root charts used below. Its
certificate is `hull_root_envelope_certificate.json` in the same directory.

## 1. Proof of the exact envelope

Take an \((n+1)\)-point minimizer \(P\) and a hull vertex \(z\). Put
\(Q=P\setminus\{z\}\). Choose a supporting line through \(z\), with every
point of \(Q\) strictly on the same side, and send that line to infinity by a
projective transformation. The image of \(z\) supplies a direction
\(\theta_z\), while \(Q\) remains in one affine patch. The transformation is
convexity-preserving on \(Q\).

Every ordinary face of \(P\) either avoids \(z\), contributing a face of
\(Q\), or contains \(z\). Apart from the singleton \(\{z\}\), the latter
faces are in bijection with the nonempty caps of \(Q\) in the chart
\(\theta_z\). Hence

\[
 V(P)=V(Q)+1+C_{\theta_z}(Q).                             \tag{5}
\]

This proves the lower bound in (1). Conversely, affinely make any chosen
generic direction of \(Q\) horizontal and write its points in increasing
\(x\)-order. A point \(z=(X,-M)\), with \(X\) to the right of every point and
\(M\) sufficiently large, satisfies

\[
 \operatorname{orient}(q_i,q_j,z)<0\qquad(i<j).           \tag{6}
\]

It is an extreme point, and precisely the cap subsets extend through \(z\).
Thus equality (5) holds for this constructed extension, proving the upper
bound and (1).

If

\[
 \Phi_n(c)=\min\{V(Q)-f(n):C_\theta(Q)=c\},               \tag{7}
\]

then the same statement is the exact weighted Pareto formula

\[
 K_{n,1}=f(n+1)-f(n)-1=\min_c\{\Phi_n(c)+c\}.            \tag{8}
\]

In particular, the recurrence optimizes \(V+C\), not \(V\) and then \(C\).

## 2. The projective flag dynamic

Repeatedly delete a hull vertex. For every extreme shelling flag

\[
 P_1\subset P_2\subset\cdots\subset P_n=P,
\]

let \(\theta_k\) be the radial chart in which
\(P_{k+1}=P_k\prec\{z_{k+1}\}\). Applying (5) at each step gives (2).
Consequently,

\[
 f(n)=n+\min_{\text{realizable extreme flags}}
              \sum_{k=1}^{n-1}C_{\theta_k}(P_k).          \tag{9}
\]

This is a weighted, growing-state projective dynamic. The transition data at
level \(k\) are

\[
 (\text{order type of }P_k,\ \text{chosen root chart }\theta_k,
   \ C_{\theta_k}(P_k)).                                  \tag{10}
\]

There is no fixed finite chart alphabet in (9), and no reason for the next
chart to preserve the cap/cup roles of the current one.

The available exact values give the following one-step envelope costs. Here
\(p(k)\) is the least cap count among ordinary \(V\)-minimizers, whereas
\(K_{k,1}=f(k+1)-f(k)-1\) is the weighted cost selected by (8).

| \(k\) | \(f(k)\) | \(p(k)\) | \(K_{k,1}\) |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 |
| 2 | 3 | 3 | 3 |
| 3 | 7 | 6 | 6 |
| 4 | 14 | 11 | 11 |
| 5 | 26 | 17 | 17 |
| 6 | 44 | 28 | 27 |
| 7 | 72 | 40 | 40 |
| 8 | 113 | 55 | 54 |

The first strict weighted departures occur at \(k=6\) and \(k=8\). At
\(k=8\), the ordinary minimizer has \((V,C)=(113,55)\), while the exact
root-envelope child has \((V,C)=(114,53)\). Thus

\[
 168=1+114+53<1+113+55=169.                               \tag{11}
\]

Under definition (1a), the separate singleton is not part of the seam cost:

\[
 K_{8,1}=(114-113)+53=54,
 \qquad f(9)=f(8)+1+K_{8,1}=113+1+54=168.                \tag{11a}
\]

This is the literal one-step reason the true nine-point minimizer sits over a
nonminimal eight-point child.

## 3. What hinged Kraft gives in one root chart

For each point \(i\) in a chart, choose a longest cap starting at \(i\), of
edge length \(\alpha_i\). Every subset of its noninitial vertices, together
with \(i\), is again a cap with left endpoint \(i\). Different initial
points give disjoint families. Therefore

\[
 C_\theta(Q)\ge A_\theta:=\sum_i2^{\alpha_i}.             \tag{12}
\]

The dual argument gives

\[
 U_\theta(Q)\ge B_\theta:=\sum_i2^{\beta_i}.              \tag{13}
\]

The hinged theorem supplies a prefix-free code of length
\(\alpha_i+\beta_i\), so

\[
 \kappa_\theta:=\sum_i2^{-\alpha_i-\beta_i}\le1.         \tag{14}
\]

Apply Hölder's inequality to
\(x_i=2^{\alpha_i}\), \(y_i=2^{\beta_i}\), and
\(z_i=2^{-\alpha_i-\beta_i}\). Since \(x_iy_iz_i=1\),

\[
 n^3
 \le \left(\sum_i x_i\right)
       \left(\sum_i y_i\right)
       \left(\sum_i z_i\right)
 =A_\theta B_\theta\kappa_\theta
 \le C_\theta U_\theta\kappa_\theta.                    \tag{15}
\]

This proves (3), including the potentially useful factor
\(\kappa_\theta^{-1}\).
It is sharp at the profile level: the stretchable eight-point certificate in
the hinged report has all eight code lengths equal to three and
\(\kappa_\theta=1\).

Since every cup is an ordinary face, \(U_\theta(P_k)\le V(P_k)\). Hence (2)
and (3) imply

\[
 V(P_{k+1})\ge V(P_k)+1+\frac{k^3}{V(P_k)},               \tag{16}
\]

and therefore

\[
 V(P_{k+1})^2-V(P_k)^2\ge2k^3.                            \tag{17}
\]

Summation yields only \(V(P_n)\ge(1+2\sum_{k<n}k^3)^{1/2}\), of order
\(n^2\). The universal endpoint floor

\[
 C_\theta(P_k)\ge k+\binom{k}{2}=\binom{k+1}{2}           \tag{18}
\]

is stronger here. Inserted into (2), it gives

\[
 V(P_n)\ge n+\sum_{k<n}\binom{k+1}{2}
          =n+\binom{n+1}{3}=\Theta(n^3).                  \tag{19}
\]

Neither estimate approaches
\(2^{(1/2-o(1))(\log n)^2}\).

## 4. Why the finite-grammar half theorem does not iterate here

The finite-grammar argument assigns a prefix code to every outgoing child
position of a fixed state. Its entropy is \(\log\rho(M)\), where \(M\) is the
transition-count matrix; this is also the exponential size-growth rate. None
of those ingredients survives unchanged in a hull shelling:

1. Equation (9) selects one predecessor at every level. As a transition
   system for the selected flag it is unary, so its effective spectral radius
   is one and \(\log\rho(M)=0\).
2. Different hull roots are alternatives under a minimum, not disjoint child
   positions whose sizes add. Treating them as grammar branches counts
   shellings, not ordinary faces.
3. The state and its chart menu grow with \(k\). There is no fixed finite
   transition matrix to which a stationary entropy law applies.
4. A root extension pays only the cap bank. The cup bank used in (15) is
   already contained in \(V(P_k)\); the recurrence does not multiply the two
   banks.
5. A later root gives a fresh edge-slope chronology. Prefix words constructed
   in different charts have no canonical concatenation.

Thus the finite-grammar theorem remains correct, but its branching hypothesis
is absent from the exact hull-root dynamic.

## 5. Exact nine-point chart-reset certificate

For the stored true minimizer

\[
\begin{split}
 &(62614,7322),(2922,4014),(10209,14386),\\
 &(20660,24299),(33336,29017),(30137,33324),\\
 &(15334,45211),(14934,55621),(10934,61521),
\end{split}
\]

direct enumeration gives \(V=168\). Its hull vertices are labels \(1,0,8\).
Deleting any of the three produces an eight-point child with

\[
 (V,C,U)=(114,53,93),\qquad
 (\alpha_i+\beta_i)_{i=1}^8=(3,3,3,4,4,4,4,4),           \tag{20}
\]

up to reordering, and \(\kappa=11/16\). In each top chart,

\[
 A=33,\qquad B=43,\qquad
 AB\kappa=\frac{15609}{16}>8^3.                           \tag{21}
\]

The three exact radial orders are

| deleted root | radial child order |
|---:|:---|
| 1 | \((8,7,6,2,3,5,4,0)\) |
| 0 | \((1,2,3,4,5,6,7,8)\) |
| 8 | \((0,4,5,7,6,3,2,1)\) |

Physical label \(2\) has

\[
 (\alpha_2,\beta_2)=(3,1)\quad\text{in the root-1 chart},
 \qquad
 (\alpha_2,\beta_2)=(1,3)\quad\text{in the root-8 chart}. \tag{22}
\]

Thus an equally cheap hull-root choice can reverse the hinged responsibility
of the same point. This is a literal finite obstruction to carrying a cap
charge forward without a chart-coherence lemma.

The verifier exhausts every extreme shelling of this order type:

- 168 reachable nonempty deletion states;
- 483 exact hull-root transitions;
- 6,984 labelled extreme shellings;
- 23 distinct root-cost sequences, all summing to \(168-9=159\).

The attainable root costs, indexed by child size, are

| child size | attainable \(C\) |
|---:|:---|
| 1 | \(1\) |
| 2 | \(3\) |
| 3 | \(6,7\) |
| 4 | \(10,11,12,13,15\) |
| 5 | \(16,18,19,21,22,24\) |
| 6 | \(25,26,28,31\) |
| 7 | \(36,39\) |
| 8 | \(53\) |

Every one of the 483 charts satisfies (12)--(15) by direct subset
enumeration.

## 6. A scalable scalar barrier

For each \(n\), put \(r=\lceil\log n\rceil\) and take the first \(n\)
binary words of length \(r\). Define

\[
 \alpha_i=\operatorname{wt}(i),\qquad
 \beta_i=r-\operatorname{wt}(i),\qquad 0\le i<n.          \tag{23}
\]

These words are prefix-free and

\[
 \kappa_n=\frac{n}{2^r}\le1.                             \tag{24}
\]

Write \(A_n=\sum_i2^{\alpha_i}\) and
\(B_n=\sum_i2^{\beta_i}\). Exact calculation gives

\[
 A_n,B_n\le\binom{n+1}{2}\qquad(n\ge20);                 \tag{25}
\]

the last failure is \(n=19\), where \(B_{19}=194>190\).
There is also a short all-\(n\) proof. Inside a fixed bit length, the bank
increment from the new word \(m\) is at most \(m+1\), which is the increment
of \(\binom{n+1}{2}\). At the reset
\(n=2^{r-1}+1\), the larger new bank is

\[
 2\cdot3^{r-1}+2^{r-1},                                  \tag{26}
\]

which is at most \(\binom{2^{r-1}+2}{2}\) for \(r\ge6\).
The finite interval \(20\le n\le32\) initializes the induction. From one
reset to the next, the left side of (26) grows by at most a factor of three,
whereas the displayed binomial floor grows by more than a factor of three.

Now set the scalar banks and value as in (4). Equations (24)--(25) ensure
all of (12)--(15), the endpoint floor, and \(C_n,U_n\le V_n\). Moreover,

\[
 V_{n+1}=V_n+1+C_n.                                      \tag{27}
\]

Yet \(\log V_n=O(\log n)\). This scalar sequence is not claimed to be a
planar order type. Its role is exact and limited: no manipulation using only
the hull recurrence, endpoint containment, and hinged Kraft can prove half
growth.

The profile itself is geometrically calibrated at \(n=8\). The stretchable
configuration

\[
 p_i=(i,y_i),\qquad
 (y_0,\ldots,y_7)=(0,-6857,-15714,33429,-39429,9714,857,-6000)
\]

realizes all eight length-three profile words, with

\[
 (V,C,U)=(130,65,65),\qquad \kappa=1.                    \tag{28}
\]

## 7. Scalable stretchable reset freedom

The construction in the converse proof of (1) can be repeated indefinitely.
Given a stretchable \(P_k\) and any generic direction \(d_k\):

1. apply an orientation-preserving rational affine map taking \(d_k\) to the
   horizontal chart;
2. order the images by \(x\);
3. add an integral point \((X,-M)\) satisfying (6).

The old order type is unchanged by the affine map, the new point is extreme,
and the root cost is exactly the freshly selected directional cap count.
At the next stage one may choose a completely different generic direction.
Thus arbitrary finite fresh-chart scripts are stretchably realizable; no
metric or projective compatibility penalty accumulates automatically.

The verifier constructs one exact integral chain through \(n=12\), using
alternating affine slopes \(-1,2,-3,4,\ldots,-11\). It enumerates every face
after each extension and checks (5). This construction is a witness to reset
freedom, not a low-face asymptotic construction.

## 8. Exact missing gate

A successful continuation must add information absent from the scalar model
and violated by the reset examples. Recurrence (1b) gives the exact identity

\[
 \log f(N)=
 \sum_{k=1}^{N-1}
 \log\!\left(1+\frac{1+K_{k,1}}{f(k)}\right).             \tag{29}
\]

Consequently, half growth is **exactly equivalent** to the cumulative gate

\[
 \sum_{k<N}
 \log\!\left(1+\frac{1+K_{k,1}}{f(k)}\right)
 \ge\left(\frac12-o(1)\right)(\log N)^2.                 \tag{30}
\]

This is the sharp statement; no pointwise regularity is being assumed. A
pointwise sharp-scale **sufficient**, but not equivalent, condition is

\[
 \boxed{
 K_{k,1}\ge(1-o(1))\frac{\log k}{k}f(k).}                \tag{31}
\]

It is enough that (31) fail only on a set whose
\(\sum(\log k)/k\)-weight is \(o((\log N)^2)\). The coefficient is exact:
if \(K_{k,1}/f(k)\sim a(\log k)/k\), then (29) gives
\(\log f(N)\sim(a/2)(\log N)^2\).

By (8), condition (31) is precisely the directional Pareto-curvature
inequality

\[
 \Phi_k(c)+c\ge(1-o(1))\frac{\log k}{k}f(k)
 \qquad\text{for every attainable }c.                    \tag{32}
\]

Thus a chart-coherence theorem must transfer enough current hinged mass into
later paid caps to imply (30), or a shelling-multiplicity theorem must show
that sufficiently many alternative roots encode sufficiently disjoint
ordinary faces. Either mechanism would replace the missing finite-grammar
branching entropy.

Without one of these two genuinely cross-chart inputs, (1)--(3) stop at the
polynomial barrier (4).
