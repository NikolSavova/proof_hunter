# Erdős 838: coefficient-scale repair-`C_4` audit

**Verdict.**  The coefficient-scale analytic gate is closed, provided
`C_4` means an ordered graph homomorphism (the two vertices on either side
are allowed to coincide).  No typical-set or degree-regularization lemma is
needed.  If `G` is the repair support, `m=|E(G)|`, and `I(T;I)` is the mutual
information under the uniform-edge law, then

\[
 \boxed{\operatorname{hom}(C_4,G)\ge m^2 2^{-2I(T;I)}.}       \tag{1}
\]

Consequently ACP Theorem 23, which gives
`I(T;I)<=epsilon(r+1)`, implies

\[
 \boxed{\operatorname{hom}(C_4,G)
        \ge m^2 2^{-2\epsilon(r+1)}.}                         \tag{2}
\]

This is stronger than the requested
`m^2/2^{o(r^2)}` whenever `epsilon=o(r)`, and in particular under the
`epsilon=o(1)` near-product regime of ACP.  Combining (2) with the
cross-source decoder gives the exact coefficient-scale estimate

\[
 m\le n,2^r,2^{\epsilon(r+1)}V(P).                          \tag{3}
\]

When `r=Theta(log n)` and `epsilon=o(r)`, the multiplier in (3) is
`2^{o(r^2)}`.

There is one terminology warning.  If `K_{2,2}` is required to be
injective on both sides, the conclusion is false: a star has weighted
rectangle probability one and no injective `K_{2,2}`.  The coefficient
decoder does not require injectivity, however.  It works unchanged when
`T_1=T_2` or `I_1=I_2`; hence ordered homomorphic rectangles are exactly
the right objects here.

## 1. The two rectangle measures must not be confused

Let `G subseteq L times R` be a finite simple bipartite graph.  Write

\[
 m=|E(G)|,\qquad d_x=|N(x)|,\quad e_y=|N(y)|.
\]

Under the uniform law on edges its marginals are

\[
 \mu(x)=d_x/m,\qquad \nu(y)=e_y/m.                            \tag{4}
\]

ACP Theorem 23 first proves that the product-marginal edge density is

\[
 q=\sum_{xy\in E(G)}\mu(x)\nu(y)
   ={1\over m^2}\sum_{xy\in E(G)}d_xe_y,                    \tag{5}
\]

and then that the **weighted** homomorphic rectangle probability is at
least `q^4`.  Explicitly that probability is

\[
 {1\over m^4}
 \sum_{x_1,x_2,y_1,y_2}
 \prod_{a,b}1_G(x_a,y_b)
 d_{x_1}d_{x_2}e_{y_1}e_{y_2}.                              \tag{6}
\]

Equation (6) is not the unweighted rectangle count divided by any fixed
ambient cardinality.  Thus multiplying the probability in ACP (131) by a
putative number of equally likely tuples is not valid.  The missing step
is nevertheless supplied exactly by mutual information, as follows.

## 2. An entropy--spectral `C_4` lemma

> **Theorem 1 (uniform-edge entropy forces counted rectangles).**
> Let `(X,Y)` be a uniformly random edge of a nonempty finite simple
> bipartite graph `G`, and put `I=I(X;Y)` in bits.  Then
> \[
>        \operatorname{hom}(C_4,G)\ge |E(G)|^2 2^{-2I}.       \tag{7}
> \]
> Here homomorphisms are ordered and may identify the two vertices in the
> same part.

**Proof.**  From (4), using base-two logarithms,

\[
\begin{aligned}
 H(X)&=\log_2m-{1\over m}\sum_{xy\in E(G)}\log_2d_x,\\
 H(Y)&=\log_2m-{1\over m}\sum_{xy\in E(G)}\log_2e_y.
\end{aligned}                                                \tag{8}
\]

Since `H(X,Y)=log_2 m`,

\[
 I=\log_2m-{1\over m}\sum_{xy\in E(G)}
                   \log_2(d_xe_y).                           \tag{9}
\]

Thus the geometric mean of `d_xe_y` over the edges is

\[
 D:=\left(\prod_{xy\in E(G)}d_xe_y\right)^{1/m}=m2^{-I}.     \tag{10}
\]

Let `A` be the biadjacency matrix and let `sigma_1` be its largest
singular value.  The adjacency matrix of the underlying bipartite graph is

\[
 B=\begin{pmatrix}0&A\\A^{\mathsf T}&0\end{pmatrix},
\]

whose spectral radius is `sigma_1`.  The vector

\[
 z_v=\sqrt{\deg(v)/(2m)}
\]

has Euclidean norm one.  Its Rayleigh quotient, followed by AM--GM, gives

\[
 \sigma_1\ge z^{\mathsf T}Bz
 ={1\over m}\sum_{xy\in E(G)}\sqrt{d_xe_y}
 \ge \left(\prod_{xy\in E(G)}\sqrt{d_xe_y}\right)^{1/m}
 =\sqrt D.                                                    \tag{11}
\]

Finally,

\[
 \operatorname{hom}(C_4,G)
 =\operatorname{tr}\{(AA^{\mathsf T})^2\}
 =\sum_j\sigma_j^4
 \ge\sigma_1^4
 \ge D^2=m^2 2^{-2I}.                                       \tag{12}
\]

This proves (7).  `square`

The bound is exact on every complete bipartite graph, including a star.
It is also exponent-sharp on pseudorandom biregular graphs: if both sides
have size `N` and degree `d`, then `I=log_2(N/d)`, and the leading
nondegenerate `C_4` count is of scale `d^4=m^2 2^{-2I}`.

## 3. Application to ACP Theorem 23

ACP uses

\[
 R_0=r+1,\qquad \rho={\log_2m\over R_0},\qquad
 \tau+\kappa=R_0                                             \tag{13}
\]

and assumes

\[
 H(T)\le(\rho+\epsilon)\tau,\qquad
 H(I)\le(\rho+\epsilon)\kappa.                              \tag{14}
\]

Adding (14) and subtracting `H(T,I)=log_2m=rho R_0` gives

\[
 I(T;I)\le\epsilon R_0.                                     \tag{15}
\]

Substitution in Theorem 1 proves (2).  Notice that this argument uses the
stronger first conclusion of ACP Theorem 23, not its later weighted-`C_4`
probability.  ACP Theorem 25 is not needed in this stable branch.  Its
fixed-component/fan dichotomy remains useful for organizing the
component-surplus branch, but it should not be cited as an unweighted
`C_4` regularization theorem: it is not one.

## 4. The cross-source decoder accepts homomorphic rectangles

For a repair edge write `T_j=(R_j,p_j)`.  Let

\[
 (T_1,T_2,I_1,I_2)                                           \tag{16}
\]

be any ordered homomorphic `C_4`, meaning that all four `(T_a,I_b)` are
repair records; equality `T_1=T_2` or `I_1=I_2` is allowed.  The two cross
sources

\[
 A_{12}=R_1\mathbin\cup I_2,\qquad
 A_{21}=R_2\mathbin\cup I_1                                 \tag{17}
\]

are ordinary convex faces.  The decoder of the all-interval report works
without a distinctness assumption.  Given `(A_12,A_21)`, guess `p_1,p_2`
in at most `n^2` ways and the two set partitions in at most `2^{2r}` ways.
This recovers the four entries of (16), after which invalid guesses are
discarded.  Therefore

\[
 \operatorname{hom}(C_4,G)\le n^2 2^{2r}V(P)^2.              \tag{18}
\]

Combining (2) and (18), and taking square roots, proves (3).

This also resolves the diagonal issue.  For the star `K_{1,M}` the entire
count `M^2` uses a repeated left vertex, but (17) simply outputs the two
source faces corresponding to the two right vertices.  The same fibre
bound applies.  Deleting such tuples in order to insist on an injective
`K_{2,2}` would throw away valid coefficient-scale credit.

## 5. Adversarial checks and sharp warnings

### Star

For `K_{1,M}`,

\[
 I=0,\quad q=1,\quad W=1,\quad
 \operatorname{hom}(C_4)=M^2,
 \quad \operatorname{inj}(C_4)=0.                            \tag{19}
\]

So Theorem 1 and the homomorphic decoder are exact, while any claim about
injective rectangles is false.

### Harmonic Ferrers cells

Let both parts be `[N]` and put an edge between `i,j` iff `ij<=N`.  Then
`d_i=floor(N/i)` and

\[
\begin{aligned}
 m_N&=N\log N+O(N),\\
 \sum_{ij\in E}d_i d_j&={1\over2}N^2(\log N)^2+O(N^2\log N),\\
 \operatorname{hom}(C_4)&=2N^2\log N+O(N^2).
\end{aligned}                                                \tag{20}
\]

Hence the product-marginal edge density tends to `1/2`, whereas

\[
 {\operatorname{hom}(C_4)\over m_N^2}
 ={2+o(1)\over\log N}.                                      \tag{21}
\]

Thus weighted probability cannot be converted to counted density with a
universal constant loss.  This is precisely why the mutual-information
factor in (1) is the correct invariant.  The exact verifier evaluates the
finite Ferrers formulas rather than relying on (20).

### Hub-core/wing family

Take `h` left hubs and `h` right hubs, join the two hub sets completely,
and attach `w` private leaves to every hub on the opposite side.  For
`w>>h`, put `M=hw`.  Then the graph has about `2M` edges, its
product-marginal edge density is bounded away from zero, while

\[
 {\operatorname{hom}(C_4)\over m^2}\asymp {1\over h}.        \tag{22}
\]

At the same time `I(T;I)=Theta(log h)`, so (1) predicts exactly the
possible exponent loss.  Choosing `h=M^a` produces a loss `M^{-a}` but
also mutual information `Theta(a log M)`.  It therefore does not defeat
the entropy-stable branch; it explains why a bare lower bound on `q` would
have been insufficient.

## 6. Exact conclusion for the full proof

The analytic statement needed after the coefficient-scale cross-source
decoder is now a theorem:

\[
 \boxed{
 I(T;I)=o(r^2)
 \quad\Longrightarrow\quad
 \#\{\hbox{ordered repair }C_4\hbox{ homomorphisms}\}
 \ge {m^2\over2^{o(r^2)}}.}                                 \tag{23}
\]

In ACP's notation it is enough that `epsilon=o(r)`.  There is no
weighted-to-unweighted regularization residual at coefficient scale.  Any
remaining gap in the full Erdős 838 argument lies before this point
(obtaining the repair support with the stated entropy alternative, and
closing every component-surplus recursion), not in rectangle extraction
or global cross-source reuse.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_cyclic_stem_hw/verify_repair_c4_coefficient.py
```

The verifier uses exact integer arithmetic for all graph counts, checks the
equivalent product form of Theorem 1 on every nonempty labelled bipartite
graph through `4 x 4`, verifies the star identities, and evaluates the
harmonic Ferrers and hub-core/wing stress families.  Decimal arithmetic is
used only to print human-readable ratios.
