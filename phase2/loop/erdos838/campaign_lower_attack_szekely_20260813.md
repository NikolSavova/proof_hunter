# Erdős 838 lower-bound campaign — attack_szekely (gpt-5.6-sol, effort=max, 2026-08-13 14:15)

> Target: log C + log U >= (1/2 - o(1))(log N)^2 for ARBITRARY point sets.
> With Theorem 1.1 already proved, this resolves Erdős 838 outright.

# The Székely lane is blocked at Step 1

The premise that Székely proved the normalized lower constant \(1/2\) is incorrect. The publisher’s abstract states verbatim:

> “Our main result is \(\exp(0.7214\log^2 n)\ge G(n)\ge \exp(0.2275\log^2 n)\).”

It also identifies a Ramsey–Turán-type theorem as the main tool. ([link.springer.com](https://link.springer.com/article/10.1007/BF02579149))

Here Székely’s logarithm is natural. Converting to the normalization in the question gives

\[
0.2275\ln 2=0.15769\ldots,\qquad
0.7214\ln 2=0.50004\ldots .
\]

Thus Székely’s 1984 result is, up to the rounding in the abstract,

\[
0.1577\lesssim
\frac{\log_2 G(n)}{(\log_2 n)^2}
\lesssim \frac12.
\]

The coefficient \(1/2\) is his **upper bound**, not an arbitrary-graph lower bound. Consequently there is no neighboring proof at coefficient \(1/2\) waiting to be transferred.

The sentence in the paper should therefore be replaced by something like:

> Székely studied the graph analogue and obtained a lower normalized coefficient about \(0.1577\), together with the random-graph upper coefficient \(1/2\).

## 1. What the graph argument actually counts

Let

\[
h_t(G)=k_t(G)+k_t(\overline G)
\]

be the number of homogeneous \(t\)-sets. The upper bound follows immediately from \(G(n,1/2)\):

\[
\mathbb E h_t(G)=2\binom nt2^{-\binom t2}.
\]

Writing \(L=\log_2 n\) and \(t=xL\),

\[
\log_2 \mathbb E h_t(G)
=
\left(x-\frac{x^2}{2}\right)L^2-o(L^2),
\]

whose maximum is \(L^2/2\), at \(x=1\). Summing over \(t\) does not change the leading exponent.

The lower argument is a fixed-size Ramsey-multiplicity argument followed by optimization over \(t\). Its graph-theoretic engine is the neighborhood recursion

\[
k_a(G)
 =\frac1a\sum_{v\in V(G)}
 k_{a-1}\bigl(G[N_G(v)]\bigr),
\]

\[
k_b(\overline G)
 =\frac1b\sum_{v\in V(G)}
 k_{b-1}\bigl(\overline{G[\overline N_G(v)]}\bigr).
\]

The crucial facts are:

1. \(N_G(v)\) and \(\overline N_G(v)\) partition \(V(G)\setminus\{v\}\);
2. a clique containing \(v\) is exactly \(v\) plus a clique in \(G[N_G(v)]\);
3. an independent set containing \(v\) is exactly \(v\) plus an independent set in \(G[\overline N_G(v)]\).

A density or threshold decision can therefore be followed by induction on an ordinary induced graph whose only relevant parameter is its number of vertices. Modern Ramsey-multiplicity accounts package this as a threshold-set/lattice-path induction and explicitly describe it as the multiplicity analogue of the Erdős–Szekeres Ramsey argument. ([its.caltech.edu](https://www.its.caltech.edu/~dconlon/Multiplicity.pdf))

The quadratic multiplicity loss responsible for Székely’s rounded lower coefficient is on the scale

\[
h_t(G)\gtrsim \binom nt\,3^{-(1+o(1))t^2}.
\]

Indeed, this gives

\[
\log_2 h_t(G)
\ge tL-(\log_2 3)t^2-o(L^2),
\]

and optimizing at

\[
t=\frac{L}{2\log_2 3}
\]

gives

\[
\frac{1}{4\log_2 3}L^2
=0.15773\ldots\,L^2.
\]

So even the graph argument’s quantitative output is nowhere near \(1/2\).

## 2. The precise dictionary

| Graph setting | Point-set setting | Status |
|---|---|---|
| Red/blue color on pairs | Sign \(\pm\) on increasing triples | Analogy only; arity changes |
| Red clique / blue clique | Cap / cup | Exact as “homogeneous subset” |
| \(R(a,b)\le\binom{a+b-2}{a-1}\) | Cup–cap theorem with the same binomial form | Exact numerical analogue |
| Graph complement | Vertical reflection, swapping caps and cups | Exact global symmetry |
| Vertex neighborhood \(N_\pm(v)\) | Link graph of a point, or continuation sets of a pair | Not an induced one-parameter problem |
| Homogeneous-subgraph total \(K+I\) | Convex count \(W\sim C\,U\) in the construction | Sum versus product |

There cannot be a same-ground-set graph reduction. If caps were cliques and cups independent sets in a graph on \(P\), then every graph triangle would have to be monochromatic, because every three-point set is either a cap or a cup. But a two-coloring of the edges of \(K_N\), \(N\ge4\), in which every triangle is monochromatic is constant: once one edge is red, every triangle containing it is red, and this forces every edge red. Thus only the all-cap or all-cup order types could be represented.

A useful exact formulation uses the link graph at a leftmost point \(p\). Color the pair \(qr\) by \(\chi(p,q,r)\). Then

\[
\{p\}\cup S\text{ is a cap}
\iff
S\text{ is a cap and }S\text{ is a \((-)\)-clique in the link of }p.
\]

The graph recursion leaves one hereditary condition; the geometric recursion leaves an **intersection of two conditions**.

This is also why the abstract ordered \(3\)-uniform setting mentioned by Baek–Balko is too broad. The cup–cap theorem uses realizability and slope transitivity, not merely a two-coloring of triples.

## 3. What transfers using only the cup–cap theorem

There is nevertheless a clean transfer of the Ramsey-subset double count.

Let \(c_r(P)\) and \(u_s(P)\) be the numbers of \(r\)-caps and \(s\)-cups, and put

\[
m=m(r,s)=\binom{r+s-4}{r-2}+1.
\]

Every \(m\)-subset contains an \(r\)-cap or an \(s\)-cup. Double-counting the containing \(m\)-sets gives

\[
c_r(P)\binom{N-r}{m-r}
+
u_s(P)\binom{N-s}{m-s}
\ge \binom Nm.
\]

Equivalently,

\[
\frac{c_r(P)}{\binom Nr}\binom mr
+
\frac{u_s(P)}{\binom Ns}\binom ms
\ge1. \tag{1}
\]

Since \(c_r(P)\le C(P)\) and \(u_s(P)\le U(P)\), (1) yields a genuine product lower bound.

### Proposition

For every \(N\)-point set \(P\),

\[
\log_2 C(P)+\log_2 U(P)
\ge
\left(\frac14-o(1)\right)(\log_2 N)^2.
\tag{2}
\]

### Proof

Put \(L=\log_2 N\) and, along a subsequence if necessary,

\[
A=\frac{\log_2 C(P)}{L^2},\qquad
B=\frac{\log_2 U(P)}{L^2}.
\]

Take \(r=xL+o(L)\), \(s=yL+o(L)\), and set

\[
q=\frac{x}{x+y},\qquad
\alpha=(x+y)H(q),
\]

where \(H\) is binary entropy. Stirling’s formula gives

\[
\log_2 m=\alpha L+o(L).
\]

Consequently,

\[
\log_2\frac{\binom Nr}{\binom mr}
=
x(1-\alpha)L^2+o(L^2),
\]

and similarly with \(y\). Therefore (1) forces

\[
A\ge x(1-\alpha)-o(1)
\quad\text{or}\quad
B\ge y(1-\alpha)-o(1). \tag{3}
\]

Suppose \(S=A+B<1/4-\varepsilon\). Choose, up to a harmless perturbation at the endpoints,

\[
q=\frac{A}{A+B},\qquad
x=\frac{q}{2H(q)},\qquad
y=\frac{1-q}{2H(q)}.
\]

Then \(\alpha=1/2\), while

\[
x(1-\alpha)=\frac{q}{4H(q)},\qquad
y(1-\alpha)=\frac{1-q}{4H(q)}.
\]

But \(H(q)\le1\), so

\[
S<\frac14\le\frac1{4H(q)}.
\]

Hence both

\[
A=qS<\frac{q}{4H(q)},\qquad
B=(1-q)S<\frac{1-q}{4H(q)},
\]

contradicting (3). This proves (2). \(\square\)

### Sharp barrier for this entire double-counting scheme

The coefficient \(1/4\) cannot be improved using only the family of inequalities (1).

Indeed, the hypothetical values

\[
A=B=\frac18
\]

satisfy every asymptotic constraint (3). To see this, put \(z=\min(x,y)\). Since

\[
H(q)\ge2\min(q,1-q),
\]

we have \(\alpha\ge2z\), and hence

\[
\min\{x(1-\alpha),y(1-\alpha)\}
\le z(1-2z)\le\frac18.
\]

Thus at least one alternative in (3) always holds for \(A=B=1/8\). Therefore the complete collection of cup–cap-theorem subset counts, even with all asymmetric choices of \(r,s\), has sharp product coefficient \(1/4\), not \(1/2\).

This is the exact quantitative limit of the part of Székely’s framework that depends only on a Ramsey threshold.

## 4. Where the graph recursion itself dies

For an ordered pair \(p<q\), define the two continuation sets

\[
N_\pm(p,q)=\{r>q:\chi(p,q,r)=\pm\}.
\]

They partition the points to the right of \(q\), so this initially resembles the graph neighborhood split. But the graph closure identity fails: a cap in \(N_-(p,q)\) need not become a cap after adjoining \(p,q\).

Here is an exact rational witness:

\[
p=(0,0),\quad q=(1,3),\quad r=(2,0),\quad s=(3,1).
\]

The four orientation determinants are

\[
[p,q,r]=-6,\qquad [p,q,s]=-8,
\]

\[
[p,r,s]=2,\qquad [q,r,s]=4.
\]

Thus the set is in general position, and both \(r,s\in N_-(p,q)\). The pair \(\{r,s\}\) is vacuously a cap, but

\[
\{p,q,r,s\}
\]

is not a cap because \([q,r,s]>0\).

What does survive is an ordered-pair-state recurrence. If \(F_-(p,q)\) denotes the number of cap continuations beginning with \(p,q\), then

\[
F_-(p,q)
=
1+\sum_{\substack{r>q\\\chi(p,q,r)=-}}F_-(q,r),
\tag{4}
\]

and analogously for cups. But (4) is a weighted path recursion on ordered pairs, not an induction on an ordinary induced point set whose extremal behavior depends only on its cardinality.

This is the exact missing graph structure:

- in a graph, fixing one vertex lowers the relation from binary to unary membership in a neighborhood;
- for orientations, fixing one point leaves a binary link relation;
- fixing two points produces unary continuation sets, but the state then moves from \((p,q)\) to \((q,r)\).

A transferred Ramsey–Turán argument would therefore need a new anti-correlation theorem controlling

\[
\sum_{\chi(p,q,r)=-}F_-(q,r)
\quad\text{and}\quad
\sum_{\chi(p,q,r)=+}F_+(q,r)
\]

simultaneously over many pair states. The cup–cap theorem supplies no such weighted statement. Proving one with the required accumulated coefficient would be new geometric content of essentially the same strength as the target lemma; it would no longer be a transfer of Székely.

## 5. Why the two \(1/2\)'s appeared

The agreement is only at the level of upper exponents, and the underlying statistics differ.

- **Graphs:** in \(G(N,1/2)\), a \(k\)-set pays \(\binom{k}{2}\) independent one-bit constraints. The saddle point

  \[
  \max_k\left(k\log_2N-\frac{k^2}{2}\right)
  \]

  is \(\frac12(\log_2N)^2\). Each of the clique and independent-set families separately already has exponent \(1/2\); their sum still has exponent \(1/2\).

- **Point-set construction:** the cap and cup families each have exponent \(1/4\), and the convex-set count comes from their endpoint-compatible product, producing \(1/2\).

So there is a shared entropy-versus-quadratic-cost shape, but not a shared combinatorial recursion. In particular, the graph statistic is a **sum**, whereas the proposed geometric route needs a **product**.

**VERDICT: OBSTRUCTED.** Székely’s theorem does not contain the claimed coefficient-\(1/2\) lower bound; its normalized lower coefficient is only about \(0.1577\). Moreover, the graph multiplicity step uses induced-neighborhood closure, while cap/cup continuation is an ordered-pair-state weighted recursion.

**Established statement.** For every \(N\)-point planar set in general position,

\[
\boxed{\;
\log_2 C(P)+\log_2 U(P)
\ge
\left(\frac14-o(1)\right)(\log_2N)^2
\;}
\]

and \(1/4\) is the sharp consequence of the complete family of subset double-counting inequalities obtained solely from the Erdős–Szekeres cup–cap theorem.