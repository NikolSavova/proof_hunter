# Root-chart Kraft and the exact shelling-collision barrier

**Date:** 2026-08-15. All logarithms are base two.

## Verdict

There is a universal projectively natural root code. Let \(P\) have \(m\ge4\)
points, let \(H(P)\) be its hull vertices, and let \(\theta_z\) be the radial
chart of \(Q_z=P\setminus\{z\}\). If

\[
 h_z:=\max_{i\in Q_z}\{\alpha_z(i)+\beta_z(i)\},          \tag{1}
\]

then

\[
 \boxed{\sum_{z\in H(P)}2^{-h_z}\le1.}                   \tag{2}
\]

Adding one bit when \(m=2,3\) makes (2) valid at every nontrivial state.
Consequently, these root codes concatenate down the entire extreme-shelling
tree.

This positive result does **not** close the cross-chart gate. There are two
exact obstructions.

First, the full hinged codebooks in different radial charts cannot be placed
in one row without a chart prefix. If

\[
 \kappa_z:=\sum_{i\in Q_z}2^{-\alpha_z(i)-\beta_z(i)},    \tag{3}
\]

then the desired inequality

\[
 \sum_{z\in H(P)}\kappa_z\le1                            \tag{4}
\]

is false. At the top of the true nine-point minimizer, the left side is
\(33/16\). It exceeds one at every one of its 159 reachable nonsingleton
states. For an \(m\)-point convex polygon, every \(\kappa_z=1\), so the left
side of (4) is \(m\). This is an unbounded stretchable counterexample.

Second, the natural shelling-to-face decoder has **exactly maximal
multiplicity**. If \(\mathcal S(P)\) is the set of labelled extreme shellings,
then every non-singleton ordinary face is represented once in every shelling.
Hence its fibre has size exactly \(|\mathcal S(P)|\), not a smaller overlap
that could preserve shelling entropy. This remains true for arbitrary
nonnegative shelling weights.

The strongest direct consequence for the literal seam cost is only

\[
 \boxed{
 \sum_{z\in H(P)}
 \frac{1}{C_z\bigl(f(n)+K_{n,1}-C_z\bigr)}\le1,}
 \qquad |P|=n+1,                                        \tag{5}
\]

for an \((n+1)\)-point minimizer. In particular,

\[
 K_{n,1}\bigl(f(n)+K_{n,1}\bigr)\ge |H(P)|.             \tag{6}
\]

This is an exact \(f(n)\)-dependent inequality, but it is far weaker than the
already universal polynomial floor
\(K_{n,1}\ge\binom{n+1}{2}\). Thus root-chart Kraft and weighted shelling
multiplicity alone do not imply
\(K_{n,1}\gtrsim f(n)(\log n)/n\).

Exact verifier:

```text
python3 phase2/loop/erdos838/agent_shelling_multiplicity_decoder/verify_root_chart_shelling_collision.py
```

It checks every reachable root chart and every face fibre for the true
nine-point minimizer, the Pascal cell \(T_{4,2}\), and a nine-point homogeneous
vertical Pascal tower. It also audits the top radial charts of the canonical
36-point tower \(T_{4,2}[T_{4,2}]\) and convex polygons through \(m=12\).

## 1. A universal row Kraft inequality for hull roots

Put \(r=|H(P)|\). Fix \(z\in H(P)\). All other hull vertices form an ordinary
face together with \(z\). Under the root-cap bijection, the \(r-1\) vertices
of \(H(P)\setminus\{z\}\) therefore form a cap in the chart \(\theta_z\).
Its edge length is \(r-2\), so

\[
 h_z\ge r-2.                                             \tag{7}
\]

If \(r\ge4\), then

\[
 \sum_{z\in H(P)}2^{-h_z}
 \le r2^{-(r-2)}\le1.                                   \tag{8}
\]

If \(r=3\), the child \(Q_z\) has at least three points. The hinged Kraft
theorem inside \(\theta_z\) gives

\[
 h_z\ge\lceil\log(m-1)\rceil\ge2,                        \tag{9}
\]

and the row sum is at most \(3/4\). This proves (2).

For uniform treatment of the bottom states, define

\[
 \lambda(P,z)=h_z+\mathbf 1_{\{m\le3\}}.                 \tag{10}
\]

At \(m=3\), the corrected row mass is \(3/4\); at \(m=2\), it is one.
Therefore

\[
 \sum_{z\in H(P)}2^{-\lambda(P,z)}\le1                  \tag{11}
\]

for every \(m\ge2\).

Kraft's theorem now assigns a prefix code to the available root choices at
every state. Concatenating those local codewords gives every full shelling
\(\sigma\) a code of length

\[
 L(\sigma)=\sum_{(A,z)\in\sigma}\lambda(A,z),            \tag{12}
\]

and the shelling tree obeys

\[
 \sum_{\sigma\in\mathcal S(P)}2^{-L(\sigma)}\le1.        \tag{13}
\]

Thus the failure below is not the absence of a root-level Kraft code.

## 2. The raw radial codebooks do not share a namespace

For each fixed root \(z\), the hinged theorem gives
\(\kappa_z\le1\). To concatenate the inner point codes after first selecting
a root, however, one would need root-prefix lengths \(d_z\) satisfying

\[
 \sum_{z\in H(P)}2^{-d_z}\kappa_z\le1.                  \tag{14}
\]

With no chart prefix, \(d_z=0\), this is precisely the false inequality (4).
If every chart receives the same prefix length, the minimum real-valued
overhead is

\[
 d=\log R(P),\qquad R(P):=\sum_{z\in H(P)}\kappa_z.       \tag{15}
\]

This is the exact chart-namespace tax.

For the true nine-point minimizer, its three top root charts each have

\[
 \kappa_z=\frac{11}{16},\qquad h_z=4.                    \tag{16}
\]

Thus

\[
 R(P)=\frac{33}{16}>1,
 \qquad
 \sum_z2^{-h_z}=\frac3{16}.                              \tag{17}
\]

The full chart codebooks already overlap by a factor \(33/16\), whereas the
maximum-length root code leaves substantial slack.

The obstruction is scalable. Put \(m\) points on a parabola. They form a
convex polygon. In every root chart the hinged length multiset is

\[
 \{1,2,\ldots,m-3,m-2,m-2\}.                            \tag{18}
\]

Hence

\[
 \kappa_z=1,\qquad h_z=m-2,\qquad
 R(P)=m,qquad
 \sum_z2^{-h_z}=\frac{m}{2^{m-2}}.                       \tag{19}
\]

The namespace cost \(\log m\) exactly matches the entropy of choosing one of
the \(m\) symmetric roots. Raw inner-chart prefix words cannot supply that
root label for free.

## 3. Exact weighted shelling-collision theorem

Write a shelling in deletion order. At a transition
\(A\to A\setminus\{z\}\), the point \(z\) is extreme in \(A\), and its
radial chart has a cap bank of size \(C(A,z)\).

Fix a non-singleton ordinary face \(F\) of \(P\) and a shelling \(\sigma\).
There is a unique first point of \(F\) deleted by \(\sigma\); call it
\(z_\sigma(F)\). Immediately before that deletion, all of \(F\) is still
present. The root-cap bijection says that

\[
 F\setminus\{z_\sigma(F)\}
\]

is a cap symbol in that transition. Conversely, every cap symbol \(S\) at
\((A,z)\) decodes to the ordinary face \(S\cup\{z\}\). Therefore, for every
fixed shelling,

\[
 \{\text{non-singleton faces of }P\}
 \longleftrightarrow
 \bigsqcup_{(A,z)\in\sigma}
 \{\text{nonempty caps in the }z\text{-chart of }A-z\}  \tag{20}
\]

is a bijection.

Now assign arbitrary weights \(w_\sigma\ge0\), and put
\(W=\sum_\sigma w_\sigma\). Let

\[
 \mu(A,z)=\sum_{\sigma\ni(A,z)}w_\sigma                 \tag{21}
\]

be the transition flow. The preceding bijection gives the two exact
identities

\[
 \boxed{
 \sum_{(A,z):\,F\subseteq A,\ z\in F}\mu(A,z)=W
 \quad\text{for every non-singleton face }F,}            \tag{22}
\]

and

\[
 \boxed{
 \sum_{(A,z)}\mu(A,z)C(A,z)=W\bigl(V(P)-|P|\bigr).}      \tag{23}
\]

Thus every decoded face has exactly the total shelling weight as its fibre.
No choice of global shelling weights reduces that multiplicity.

For uniform weights, if \(a(A)\) is the number of deletion prefixes reaching
\(A\) and \(b(A-z)\) is the number of suffix shellings below \(A-z\), then

\[
 \mu(A,z)=a(A)b(A-z),                                    \tag{24}
\]

and \(W=|\mathcal S(P)|\). Formula (22) says that the apparent branching
entropy is lost completely when the shelling tag is forgotten.

This loss is exponentially scalable. Every generic point set with \(m\ge2\)
has at least

\[
 |\mathcal S(P)|\ge2\cdot3^{m-2},                        \tag{25}
\]

because there are two choices at size two and at least three hull choices at
every larger state. A convex polygon has \(m!\) shellings. Yet every face
fibre in (22) has that same exponential or factorial size.

## 4. Consequence for the literal seam cost

Let \(P\) be an \((n+1)\)-point minimizer. For each hull root \(z\), put

\[
 Q_z=P\setminus\{z\},\qquad
 D_z=V(Q_z)-f(n),\qquad C_z=C_{\theta_z}(Q_z).            \tag{26}
\]

The exact hull-root recurrence gives

\[
 D_z+C_z=K_{n,1}                                         \tag{27}
\]

for every \(z\in H(P)\). Choose a child point attaining \(h_z\). The cap and
cup subsets of its two longest hinged paths give

\[
 2^{h_z}\le C_zU_z.                                      \tag{28}
\]

Every cup is an ordinary face of \(Q_z\), so

\[
 U_z\le V(Q_z)=f(n)+D_z=f(n)+K_{n,1}-C_z.                \tag{29}
\]

Combining (2), (28), and (29) proves (5). Since
\(0<C_z\le K_{n,1}\), every denominator in (5) is at most
\(K_{n,1}(f(n)+K_{n,1})\), proving (6).

At \(n=8\), the true nine-point minimizer has

\[
 f(8)=113,\qquad K_{8,1}=54,\qquad
 (D_z,C_z,U_z,h_z)=(1,53,93,4)                           \tag{30}
\]

for each of its three hull roots. The strongest displayed minimizer sum is

\[
 \sum_z\frac1{C_z(f(8)+K_{8,1}-C_z)}
 =\frac1{2014}.                                          \tag{31}
\]

Thus (5) is extremely slack even in the first nonordinary weighted optimizer.
The loss occurs in (28): \(2^{h_z}=16\), while \(C_zU_z=4929\).

## 5. Exact finite calibration

### True nine-point minimizer

The reachable deletion DAG has 168 states, 483 root transitions, and 6,984
full shellings. There are 159 non-singleton faces. Hence the tagged local-cap
ledger contains

\[
 6984\cdot159=1{,}110{,}456                              \tag{32}
\]

entries, and every one of the 159 face fibres has size 6,984. The raw radial
mass exceeds one at all 159 nonsingleton states; its maximum is five. The
minimum-hinged-length candidate fails at 139 states. The corrected
maximum-length row (11) fails at none.

### Six-point Pascal cell

For \(T_{4,2}\), direct determinants give

\[
 (V,|\mathcal S|)=(50,336).                              \tag{33}
\]

Its top raw radial mass is \(15/4\), while its maximum-length root mass is
\(1/2\). All 44 nonsingleton reachable states violate raw union Kraft. The
tagged ledger has \(336(50-6)=14{,}784\) entries, with fibre size 336 over
each of the 44 non-singleton faces.

### Homogeneous vertical Pascal towers

The exact square \(T_{3,1}[T_{3,1}]\) has

\[
 (|P|,V,|\mathcal S|)=(9,273,64{,}560).                  \tag{34}
\]

Its top raw radial mass is \(313/64\), versus maximum-length mass \(15/64\).
All 264 nonsingleton states violate raw union Kraft, and every face fibre has
size 64,560.

For the canonical 36-point square \(T_{4,2}[T_{4,2}]\), the independent
reverse-product calculation gives

\[
 (C,U,V)=(14{,}136,14{,}136,441{,}399).                  \tag{35}
\]

It has eight hull roots. Exact radial dynamic programming gives

\[
 \sum_z\kappa_z=\frac{1419}{256}>1,
 \qquad
 \sum_z2^{-\min_i(\alpha_z(i)+\beta_z(i))}=\frac{11}{8}>1,
 \qquad
 \sum_z2^{-h_z}=\frac9{256}<1.                           \tag{36}
\]

Thus both the full-codebook union and the tempting shortest-diagonal root
length fail on a standard vertical tower. Only the provable maximum-diagonal
root length survives.

## 6. The remaining cross-chart gate

The exact target remains

\[
 K_{n,1}\ge(1-o(1))\frac{\log n}{n}f(n)                 \tag{37}
\]

on full logarithmic density, or its cumulative equivalent from the hull-root
envelope report. The present theorem shows that root choices do possess a
valid prefix code, so the missing ingredient is now precise: a successful
argument must retain a nonnegligible fraction of root-code entropy **after**
mapping local cap symbols to ordinary faces.

The canonical decoder (20) retains none; every face has full shelling
multiplicity. Any viable replacement must either construct genuinely new
cross-chart face labels, or prove a bounded-multiplicity remapping whose fibre
is \(o(|\mathcal S(P)|)\) by the amount required in (37). A decoder that only
records the ordinary face \(S\cup\{z\}\) cannot succeed.
