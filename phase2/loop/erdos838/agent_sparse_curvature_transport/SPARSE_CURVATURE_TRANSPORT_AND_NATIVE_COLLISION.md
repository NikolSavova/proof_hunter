# Sparse curvature transport and the native-cap collision gate

**Date:** 2026-08-15. All logarithms are base two.

## Verdict

There is an exact sparse concentration mechanism, but by itself it does not
survive decoding to ordinary faces.

Put

\[
 K_{m-1,1}=f(m)-f(m-1)-1
\]

and define the excess potential of an $m$-point state $A$ by

\[
 E(A)=V(A)-f(m).
\]

For every extreme deletion $A\to B=A\setminus\{z\}$, with root-cap cost
$C(A,z)$, there is an exact conservation law

\[
 \boxed{E(B)+C(A,z)=K_{m-1,1}+E(A).}                    \tag{1}
\]

Consequently, along every extreme shelling, the cap-symbol ledger admits a
causal bottom-up partition into curvature layers of sizes

\[
 K_{1,1},K_{2,1},\ldots,K_{N-1,1}
\]

and a final residual of size $E(P)$ for the initial $N$-point set $P$.
For an $N$-point minimizer the residual vanishes, and the top layer has
exactly $K_{N-1,1}$ tags among the $f(N)-N$ tags in each shelling. Its exact
density is therefore

\[
 \boxed{p_N=\frac{K_{N-1,1}}{f(N)-N}.}                  \tag{2}
\]

Thus the desired gate $K_{N-1,1}\asymp f(N)(\log N)/N$ would indeed produce
an $o(1)$-mass layer. This is the strongest exact positive concentration
statement available from the hull-root recurrence.

The obstruction is native-cap rigidity. At the top of a minimizer, if the
first root is $z$ and

\[
 C_z=C(P,z),\qquad D_z=V(P-z)-f(N-1),
\]

then $C_z+D_z=K_{N-1,1}$. The top curvature layer must consume all $C_z$
current root-cap tags and all $D_z$ excess tags exported by the child. In
particular, the ordinary hull face $H(P)$ is selected once in every shelling.
Under the canonical face decoder it has fibre exactly the total shelling
weight $W$, not $o(W)$.

There is also a quantitative approximate gate. Give the shellings arbitrary
weights, let $W_z$ be the weight beginning with root $z$, and suppose a causal
top-layer selection retains at least $(1-\eta)WK_{N-1,1}$ unit curvature while
every canonical ordinary-face output has load at most $\varepsilon W$. Then

\[
 \boxed{
 \sum_z\frac{W_z}{W}\frac{C_z}{K_{N-1,1}}
 \le \eta+\varepsilon\frac{\sum_z C_z}{K_{N-1,1}}
 \le \eta+\varepsilon |H(P)|.}                         \tag{3}
\]

Therefore, whenever $\eta=o(1)$ and
$\varepsilon |H(P)|=o(1)$, almost all seam curvature must be child excess:

\[
 \sum_z\frac{W_z}{W}\frac{D_z}{K_{N-1,1}}=1-o(1).      \tag{4}
\]

This is the precise surviving gate. A near-capacity sparse decoder with
$\varepsilon=O(K_{N-1,1}/f(N))$ cannot use a nonnegligible native cap portion
when

\[
 |H(P)|K_{N-1,1}/f(N)=o(1).
\]

It must instead prove curvature almost entirely from the nonminimality of the
children, or use a genuinely noncanonical geometric output theorem.

There is a complementary direct high-wall inequality. If $r=|H(P)|$, the
other $r-1$ hull vertices form a cap in every root chart, and all their
nonempty subsets are caps. Hence

\[
 \boxed{K_{N-1,1}\ge C_z\ge 2^{r-1}-1.}                 \tag{5}
\]

Thus large hulls are already controlled directly; the sparse route is needed
only below this exponential hull wall.

Exact verifier:

```text
python3 phase2/loop/erdos838/agent_sparse_curvature_transport/verify_sparse_curvature_transport.py
```

It checks (1) on every subset and every extreme-root transition of the exact
nine-point minimizer, $T_{4,2}$, a convex octagon, and
$T_{3,1}[T_{3,1}]$. It computes shelling weights by exact dynamic programming
and solves the forced-native congestion problem by integral max-flow.

## 1. Proof of the transport identity

Let $A$ have $m$ points and let $B=A\setminus\{z\}$. The hull-root identity is

\[
 V(A)=V(B)+1+C(A,z).                                    \tag{6}
\]

The exact envelope recurrence is

\[
 f(m)=f(m-1)+1+K_{m-1,1}.                               \tag{7}
\]

Subtracting (7) from (6) gives

\[
 V(A)-f(m)=V(B)-f(m-1)+C(A,z)-K_{m-1,1},
\]

which is (1).

Now regard every cap symbol exported at a transition as one unit token. Work
upward from the one-point survivor. Inductively, suppose the child ledger has
already been partitioned into its lower curvature layers and a reservoir of
exactly $E(B)$ unassigned tokens. The current transition introduces
$C(A,z)$ new tokens. Equation (1) says that the combined pool has size

\[
 E(B)+C(A,z)=K_{m-1,1}+E(A).
\]

Assign any $K_{m-1,1}$ tokens to the new curvature layer and export the other
$E(A)$ tokens. This proves the causal partition by induction.

The total curvature core through size $N$ is

\[
 \sum_{m=2}^{N}K_{m-1,1}=f(N)-N,                        \tag{8}
\]

while a shelling of $P$ has $V(P)-N$ cap tokens. Their difference is exactly
$E(P)$. For a minimizer, (8) consumes the whole ledger. Formula (2) follows
by selecting only its top layer.

This construction is a concentration theorem for unit recurrence mass, not
an independent lower bound for $K_{N-1,1}$. It identifies exactly what a
sparse shelling proof would have to decode without losing root entropy.

## 2. Top-layer rigidity

Let $P$ now be a minimizer, so $E(P)=0$. If a shelling starts with $z$, the
child reservoir has size $E(P-z)=D_z$. At the top induction step, (1) becomes

\[
 D_z+C_z=K_{N-1,1}.                                     \tag{9}
\]

There is no outgoing residual. Hence every token in the pool is forced into
the top layer, including every current root-cap tag.

Every nonempty subset of $H(P)\setminus\{z\}$ is a cap in the $z$-chart. In
particular, the cap $H(P)\setminus\{z\}$ decodes to the same ordinary face
$H(P)$ for every first root. Thus exact causal concentration has

\[
 L(H(P))=\sum_z W_z=W.                                  \tag{10}
\]

The top layer may be sparse as a fraction of the full ledger, but its
canonical decoder still has a full-weight collision.

For a nonminimal parent, there is an outgoing residual $E(P)$. The top demand
can use at most $D_z$ child tokens, so it must use at least

\[
 a_z=(K_{N-1,1}-D_z)_+=(C_z-E(P))_+                    \tag{11}
\]

native top-cap tokens in every shelling beginning with $z$. This is the
quantity optimized in the finite max-flow calculations below.

## 3. Proof of the weighted approximate gate

For a minimizer, let $M_z$ be the selected native-cap mass in shellings whose
first root is $z$. There are exactly $C_z$ possible native ordinary faces for
that root. If every face has load at most $\varepsilon W$, then

\[
 M_z\le \varepsilon W C_z.                              \tag{12}
\]

The selected child-excess mass is at most $W_zD_z$. Therefore retention of
$(1-\eta)WK_{N-1,1}$ units implies

\[
 (1-\eta)WK_{N-1,1}
 \le \varepsilon W\sum_z C_z+\sum_zW_zD_z.              \tag{13}
\]

Using $D_z=K_{N-1,1}-C_z$ and $\sum_zW_z=W$, rearrangement gives the first
inequality in (3). Since $C_z\le K_{N-1,1}$, the second follows.

This proof allows the selection to depend on the complete suffix shelling and
to balance native choices globally. Its only structural assumptions are
causal unit-token transport and the canonical ordinary-face output.

## 4. Exact finite calibration

### True nine-point minimizer

Here

\[
 (V,f(9),W,K_{8,1})=(168,168,6984,54).
\]

The full ledger has 159 tags per shelling, so the exact top-layer density is

\[
 \frac{54}{159}=\frac{18}{53}.
\]

Each of the three roots has

\[
 (W_z,C_z,D_z,a_z)=(2328,53,1,53).
\]

All 53 native cap tags are forced. An exact max-flow that is allowed to choose
and coordinate every forced native output still has optimum maximum load

\[
 \boxed{6984=W.}
\]

The common hull triangle alone certifies equality. Thus the first true
weighted minimizer is already a sharp collision witness for exact sparse
transport.

### Pascal cell

For $T_{4,2}$,

\[
 (V,f(6),E,W,K_{5,1})=(50,44,6,336,17).
\]

Every one of its four roots has

\[
 (W_z,C_z,D_z,a_z)=(84,21,2,15).
\]

Even though the parent may export six residual tokens, at least 15 of the 17
top-curvature tokens must be native. The exact globally balanced native
minimum is

\[
 \boxed{131=\frac{131}{336}W.}
\]

This is substantially stronger than the separate-root averaging lower bound
$5W/28$.

### Vertical Pascal square

For $T_{3,1}[T_{3,1}]$,

\[
 (V,f(9),E,W,K_{8,1})=(273,168,105,64560,54).
\]

The large parent excess allows several roots to use mostly or entirely child
residual. The exact forced-native mass is 523,800 and its globally optimized
maximum load is

\[
 \boxed{2117=\frac{2117}{64560}W.}
\]

This example shows the other side of the gate: far from the minimizing
envelope, excess tokens can bypass most current cap curvature. The transport
identity alone therefore supplies no geometric concentration theorem.

### Convex polygons

Against the global $f$-baseline, the convex octagon has

\[
 (V,E,K_{7,1},C_z,D_z)=(255,142,40,127,55).
\]

Since the parent excess exceeds the entire top demand, (11) forces no native
token at all. This is a sharp warning that the algebraic core can select tags
with no local relation to the current root chart on a highly nonminimal set.

There is also a scalable stretchable collision benchmark internal to the
convex family. For a convex $N$-gon,

\[
 V=2^N-1,\qquad W=N!,\qquad K^{\rm conv}_{N-1}=C_z=2^{N-1}-1.
\]

The top layer has density

\[
 \frac{2^{N-1}-1}{2^N-1-N}\longrightarrow\frac12,
\]

and the full set is a native top-cap face in every shelling, with fibre
exactly $W=N!$. Hence a universal causal-cap decoder cannot obtain entropy
merely by thinning the ledger; its success must use the small global excess
scale specific to true minimizers.

## 5. Exact max-flow model

For each top root $z$, there are $W_z$ suffix shellings and $C_z$ possible
native cap faces. A causal top allocation must select at least $a_z$ distinct
native faces per suffix shelling. Aggregate these selections as integer flows
$x_{z,F}$ satisfying

\[
 \sum_Fx_{z,F}=W_za_z,\qquad 0\le x_{z,F}\le W_z.       \tag{14}
\]

The upper bound encodes that a face occurs only once in one top cap bank. For
a proposed maximum load $M$, impose

\[
 \sum_zx_{z,F}\le M\qquad\text{for every ordinary face }F.             \tag{15}
\]

This is an integral bipartite flow problem. Binary search over $M$ gives the
exact optima quoted above. Any aggregate solution can be decomposed into
$W_z$ rows of $a_z$ distinct faces, so the model is equivalent to allowing
arbitrary suffix-dependent selection, not merely a relaxation.

## 6. Remaining route

The exact transport theorem reduces the surviving hull-root strategy to one
specific alternative:

1. prove that, on minimizing parents, the weighted child excess $D_z$ carries
   $1-o(1)$ of $K_{N-1,1}$ and has a geometrically decodable sparse
   certificate; or
2. replace the canonical face output by a new geometry-respecting remapping
   that separates the forced native cap tags.

Equation (3) shows why a native-cap proof cannot simply be diluted: at the
near-capacity congestion scale its contribution is asymptotically negligible
unless the hull is already in the direct exponential regime (5). The convex
and vertical examples show that excess transport exists algebraically, but
not that it counts new ordinary faces. That excess-to-faces theorem is the
remaining literal-seam gate.
