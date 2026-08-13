# Erdős 838 lower-bound campaign — attack_direct (gpt-5.6-sol, effort=max, 2026-08-13 14:55)

> Target: log C + log U >= (1/2 - o(1))(log N)^2 for ARBITRARY point sets.
> With Theorem 1.1 already proved, this resolves Erdős 838 outright.

I do not obtain a universal constant \(>1/4\). What follows are: (i) a sharp consequence of all asymmetric cup–cap double counts, (ii) a proof that this entire black-box route cannot pass \(1/4\), and (iii) an exact algebraic reformulation exposing the additional structure a proof would have to use.

## 1. What all asymmetric cup–cap double counts imply

Write
\[
C_a(P)=\#\{\text{\(a\)-caps in \(P\)}\},\qquad
U_b(P)=\#\{\text{\(b\)-cups in \(P\)}\}.
\]

Let \(2\le a,b\le t\le N\) and suppose
\[
\binom{a+b-4}{a-2}<t.
\]
Then every \(t\)-subset contains an \(a\)-cap or a \(b\)-cup. Double-counting incidences gives
\[
\binom Nt
 \le C_a(P)\binom{N-a}{t-a}
   +U_b(P)\binom{N-b}{t-b},
\]
hence
\[
1\le
 C_a(P)\frac{\binom ta}{\binom Na}
 +U_b(P)\frac{\binom tb}{\binom Nb}.
\tag{1}
\]
Consequently at least one of
\[
C(P)\ge \frac12\frac{\binom Na}{\binom ta},
\qquad
U(P)\ge \frac12\frac{\binom Nb}{\binom tb}
\tag{2}
\]
holds.

Define the homogeneous binary entropy
\[
\mathcal E(x,y)
  =x\log\frac{x+y}{x}+y\log\frac{x+y}{y}
  =(x+y)H\!\left(\frac{x}{x+y}\right),
\]
where \(H(p)=-p\log p-(1-p)\log(1-p)\).

Let \(L=\log N\), take
\[
a=AL+o(L),\qquad b=BL+o(L),\qquad t=N^{\alpha+o(1)}.
\]
Stirling gives
\[
\log\binom{a+b-4}{a-2}
 =\mathcal E(A,B)L+o(L).
\]
Thus, whenever \(\mathcal E(A,B)<\alpha<1\), (2) gives
\[
\frac{\log C(P)}{L^2}\ge A(1-\alpha)-o(1)
\quad\text{or}\quad
\frac{\log U(P)}{L^2}\ge B(1-\alpha)-o(1).
\tag{3}
\]

### Entropy tradeoff

Suppose along a sequence of point sets
\[
\frac{\log C(P)}{L^2}\to c,\qquad
\frac{\log U(P)}{L^2}\to u,
\]
with \(c,u<\infty\). Then
\[
\boxed{\mathcal E(c,u)\ge\frac14.}
\tag{4}
\]

#### Proof

Assume first \(c,u>0\), and put \(e=\mathcal E(c,u)\). Suppose \(e<1/4\). Set
\[
\lambda=\frac1{2e}.
\]
By homogeneity,
\[
\mathcal E(\lambda c,\lambda u)=\lambda e=\frac12.
\]
Choose
\[
\frac12<\alpha<1-2e.
\]
Applying (3) with \(A=\lambda c\), \(B=\lambda u\) gives
\[
c\ge\lambda c(1-\alpha)
\quad\text{or}\quad
u\ge\lambda u(1-\alpha).
\]
But
\[
\lambda(1-\alpha)>\lambda(2e)=1,
\]
so both alternatives are impossible. The cases \(c=0\) or \(u=0\) follow by replacing \((c,u)\) with \((c+\varepsilon,u+\varepsilon)\) and passing to the limit. ∎

Since \(\mathcal E(c,u)\le c+u\), this recovers
\[
c+u\ge\frac14.
\tag{5}
\]
More precisely, if
\[
p=\lim\frac{\log C(P)}{\log C(P)+\log U(P)}
\]
exists, then
\[
\liminf\frac{\log C(P)+\log U(P)}{L^2}
 \ge \frac1{4H(p)}.
\tag{6}
\]
Thus the bound is strictly larger than \(1/4\) whenever the two logarithmic counts are asymptotically imbalanced. In particular, the desired \(1/2\) follows for sequences with \(H(p)\le1/2\). The unresolved case is the balanced regime \(p\to1/2\), exactly where the upper construction lies.

---

## 2. Sharp obstruction to the cup–cap-theorem-only route

The preceding use of all asymmetric parameters is sharp as a black-box argument.

Consider the formal size profile
\[
\phi(x)=x(1-2x),\qquad 0\le x\le\frac12.
\tag{7}
\]
Interpret formally
\[
\log C_{xL}\sim \phi(x)L^2,\qquad
\log U_{xL}\sim \phi(x)L^2.
\]
Its maximum is
\[
\max_{0\le x\le1/2}\phi(x)=\frac18,
\]
at \(x=1/4\). Thus it has
\[
\log C\sim\frac18L^2,\qquad
\log U\sim\frac18L^2,
\tag{8}
\]
and product coefficient \(1/4\).

Nevertheless it satisfies every asymptotic constraint (3). Indeed, suppose \(A\le B\). Concavity of binary entropy on \([0,1/2]\) gives
\[
H(p)\ge2p,
\]
and therefore
\[
\mathcal E(A,B)\ge2A.
\tag{9}
\]
If \(\alpha\ge\mathcal E(A,B)\), then
\[
A(1-\alpha)
 \le A(1-\mathcal E(A,B))
 \le A(1-2A)
 =\phi(A).
\tag{10}
\]
Thus the cap side alone can satisfy (3); if \(B<A\), the cup side does.

This is not asserted to be a realizable geometric profile. It is a feasible solution of the complete system of inequalities supplied by:

* every asymmetric cup–cap threshold;
* every sample size \(t=N^\alpha\);
* double-counting each cap/cup size;
* then summing over all \(O(L)\) relevant sizes.

Therefore:

> Repeated use of the cup–cap theorem through inequalities of the form (1), even retaining all sizes and all asymmetries, cannot force a coefficient above \(1/4\).

A deletion argument can escape this obstruction only if it uses extension/overlap information between chains in different residual sets. Merely finding a chain, deleting it, and reapplying the same theorem does not retain that information.

---

## 3. Exact matrix reformulation of the target

Let
\[
m_{ij}=\frac{y_j-y_i}{x_j-x_i},\qquad i<j.
\]
For \(i<j<k\),
\[
\chi(i,j,k)=+
\quad\Longleftrightarrow\quad
m_{ij}<m_{jk}.
\tag{11}
\]

For a selected sequence \(i_1<\cdots<i_s\), it is a cup exactly when
\[
m_{i_1i_2}<m_{i_2i_3}<\cdots<m_{i_{s-1}i_s},
\tag{12}
\]
and a cap exactly when these inequalities are reversed. The converse follows because every chord slope is a positive weighted average of the consecutive slopes it spans.

Order all pairs \(e_r=(i_r,j_r)\), \(i_r<j_r\), by increasing slope. Ties between disjoint pairs may be ordered arbitrarily. Define
\[
T_{ij}=I+E_{ji},
\]
where \(E_{ji}\) has its only nonzero entry in position \((j,i)\).

Starting with the all-ones column vector, processing an edge \(ij\) by
\[
z_j\leftarrow z_j+z_i
\]
counts all increasing-slope paths ending at \(j\). Hence the exact identities are
\[
\boxed{
U(P)=\mathbf1^{\!T}T_{e_M}\cdots T_{e_1}\mathbf1,
\qquad
C(P)=\mathbf1^{\!T}T_{e_1}\cdots T_{e_M}\mathbf1,
}
\tag{13}
\]
where \(M=\binom N2\).

Moreover,
\[
m_{ik}
 =\frac{(x_j-x_i)m_{ij}+(x_k-x_j)m_{jk}}{x_k-x_i},
\tag{14}
\]
so \(m_{ik}\) lies strictly between \(m_{ij}\) and \(m_{jk}\). Thus the slope order is a stretchable reflection order on the positive roots of type \(A_{N-1}\).

Consequently the target is exactly the following reverse-product inequality:

\[
\log\!\left(\mathbf1^{\!T}T_{e_M}\cdots T_{e_1}\mathbf1\right)
+
\log\!\left(\mathbf1^{\!T}T_{e_1}\cdots T_{e_M}\mathbf1\right)
\ge\left(\frac12-o(1)\right)(\log N)^2
\tag{15}
\]
for every stretchable reflection order.

A proof for all reflection orders would be stronger than the geometric statement.

---

## 4. Triangle-flip compression is not monotone

For \(i<j<k\), put
\[
A=T_{ij},\qquad B=T_{ik},\qquad D=T_{jk}.
\]
A direct multiplication gives
\[
DBA-ABD=E_{ki}.
\tag{16}
\]

Thus replacing the consecutive slope packet
\[
(ij),(ik),(jk)
\]
by
\[
(jk),(ik),(ij)
\]
strictly decreases the cup count and strictly increases the cap count. With arbitrary prefix and suffix contexts,
\[
U(\sigma)-U(\sigma')=\alpha>0,\qquad
C(\sigma')-C(\sigma)=\beta>0,
\tag{17}
\]
where, for suitable nonnegative context products \(L,R,\widehat L,\widehat R\),
\[
\alpha=\mathbf1^{\!T}R E_{ki}L\mathbf1,\qquad
\beta=\mathbf1^{\!T}\widehat L E_{ki}\widehat R\mathbf1.
\tag{18}
\]
Hence
\[
C(\sigma')U(\sigma')-C(\sigma)U(\sigma)
 =\beta U(\sigma)-\alpha C(\sigma)-\alpha\beta,
\tag{19}
\]
whose sign is context-dependent.

This already occurs on four rational points. Let the first three points be
\[
(0,0),(1,1),(2,4),
\]
and take the fourth respectively as
\[
(3,8),\qquad (3,13/2),\qquad (3,21/4).
\]
Their triple-sign patterns and counts are:

\[
\begin{array}{c|c|c|c}
y_4&\#(-)\text{ triples}&(C,U)&CU\\ \hline
8&0&(10,15)&150\\
13/2&1&(11,13)&143\\
21/4&2&(12,12)&144.
\end{array}
\]

Moving from the first to the second configuration flips only \(234\) from \(+\) to \(-\), and decreases \(CU\). Moving from the second to the third flips only \(134\) from \(+\) to \(-\), and increases \(CU\).

Therefore no orientation-independent rule of “flip every mutable triangle toward a canonical/decomposable order” can be monotone for \(CU\). Any successful compression would have to track the global context weights \(\alpha,\beta,C,U\).

---

## 5. A precise weighted lemma that would suffice

For \(p\in P\), let \(C_p\) and \(U_p\) be the numbers of caps and cups containing \(p\). Define the mean sizes of uniformly chosen caps and cups by
\[
\mu_C(P)=\frac{\sum_{K\in\mathcal C(P)}|K|}{C(P)},\qquad
\mu_U(P)=\frac{\sum_{K\in\mathcal U(P)}|K|}{U(P)}.
\]
Then
\[
\sum_{p\in P}\frac{C_p}{C(P)}=\mu_C(P),\qquad
\sum_{p\in P}\frac{U_p}{U(P)}=\mu_U(P).
\]
Hence some \(p\) satisfies
\[
\frac{C_p}{C(P)}+\frac{U_p}{U(P)}
 \ge\frac{\mu_C(P)+\mu_U(P)}N.
\tag{20}
\]
Since
\[
C(P-p)=C(P)-C_p,\qquad U(P-p)=U(P)-U_p,
\]
we obtain
\[
\begin{aligned}
&\log C(P)+\log U(P)
 -\log C(P-p)-\log U(P-p)\\
&\qquad\ge
\frac1{\ln2}
\left(\frac{C_p}{C(P)}+\frac{U_p}{U(P)}\right).
\end{aligned}
\tag{21}
\]

It follows rigorously that the weighted assertion
\[
\boxed{
\mu_C(P)+\mu_U(P)
 \ge (1-o(1))\log |P|
}
\tag{22}
\]
for every \(P\) would prove the target. Indeed, repeatedly deleting a point supplied by (20) gives
\[
\log C(P)+\log U(P)
 \ge \frac1{\ln2}\sum_{m=2}^N
       \frac{(1-o(1))\log m}{m}
 =\left(\frac12-o(1)\right)(\log N)^2.
\tag{23}
\]

Thus (22) is a clean weighted form of the missing engine. The formal profile (7) has typical cap and cup sizes about \(L/4\), so the cup–cap-theorem-only information is consistent with only
\[
\mu_C+\mu_U\sim\frac12L,
\]
again exposing the factor of two.

---

## 6. Why the decomposable singleton recurrence cannot hold generally

Let \(R(P)=\sqrt{C(P)U(P)}\). Take one of the exact rational iterated constructions from the paper, with \(N\) points and
\[
\log R(P)=O((\log N)^2).
\]
List it in \(x\)-order as \(p_1,\dots,p_N\), and put
\[
P_n=\{p_1,\dots,p_n\}.
\]
Then
\[
\prod_{n=2}^N\frac{R(P_n)}{R(P_{n-1})}=R(P_N),
\]
so for some \(n\),
\[
\frac{R(P_n)}{R(P_{n-1})}
 \le 2^{O((\log N)^2/N)}
 =1+o(1).
\tag{24}
\]
In particular, even for a consecutive split
\[
P_n=P_{n-1}<\{p_n\},
\]
there is no universal recurrence
\[
R(P_n)\ge\sqrt2\,R(P_{n-1}),
\]
let alone the full decomposable recurrence with its additional positive term. Hence an arbitrary \(x\)-split cannot simply inherit the Lemma 5.2 factor. A useful lossy recurrence would have to give only an incremental factor of order
\[
1+\Theta\!\left(\frac{\log n}{n}\right),
\]
whose accumulated logarithm is quadratic.

For the endpoint route, the identity
\[
W(P)=N+\sum_{p<q}c(p,q)u(p,q)
\]
and the known coefficient-\(1/4\) bound imply only
\[
\max_{p<q}c(p,q)u(p,q)
 \ge 2^{(1/4-o(1))(\log N)^2}.
\]
Reaching coefficient \(1/2\) at one endpoint pair requires genuinely new concentration information; averaging cannot supply it.

**VERDICT: PARTIAL — the target lemma and any universal constant \(>1/4\) remain unproved. The cleanest established statement is that every finite normalized limit point**
\[
c=\lim\frac{\log C(P)}{(\log N)^2},\qquad
u=\lim\frac{\log U(P)}{(\log N)^2}
\]
**satisfies**
\[
\boxed{
(c+u)\,
H\!\left(\frac{c}{c+u}\right)\ge\frac14.
}
\]
**This is sharp for all arguments using only asymmetric cup–cap thresholds and size-by-size double counting; escaping \(1/4\) requires extension/overlap information not contained in those inequalities.**