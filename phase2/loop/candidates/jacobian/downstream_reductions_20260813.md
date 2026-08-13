# Jacobian aftermath — reductions (gpt-5.6-sol, effort=max, 2026-08-13 09:16)

> The counterexample is three weeks old. This sweep is about finding what is
> ALREADY TAKEN, not about admiring the result.

# Bottom line

There is **no canonical dimension** attached to either the BCW or Drużkowski reduction: both proofs contain choices of factorization, sharing, polarization, and padding. Thus “the exact \(N\)” only makes sense after fixing an implementation.

For two natural, fully specified implementations, I get:

| Construction | Dimension | Form | Three-point witness? |
|---|---:|---|---|
| Textbook, unshared BCW schedule | **79** | \(Z+\mathcal H(Z)\), \(\mathcal H\) cubic homogeneous | **Yes, explicitly** |
| Carrier-shared BCW implementation already posted | **39** | same form | **Yes, explicitly** |
| Drużkowski applied to the 79-variable map, using the fixed polarization below | **575** | \(U+(AU)^{*3}\), \(A\in M_{575}(\mathbf Q)\), \(\operatorname{rank}A=79\) | **Yes, explicitly** |
| Compressed Drużkowski route from the 39-variable map | **327** | \(U+(AU)^{*3}\), \(A\in M_{327}(\mathbf Q)\), \(\operatorname{rank}A=39\) | **Yes, explicitly** |
| Weyl-algebra consequence | \(A_3\), not \(A_2\) | explicit endomorphism \(x_i\mapsto F_i,\ \partial_i\mapsto D_i\) | Explicitly non-surjective |

The published/posting status as of August 13, 2026 is: the 79-variable bound has appeared in an arXiv preprint; a full degree-\(3\), 19-variable map has been posted with verification; and an explicit \(A_3\) Dixmier counterexample has also been posted. I did not locate an Alpöge-specific printed Drużkowski matrix; the dimensions \(575\) and \(327\) and the block matrices below are my calculations. ([arxiv.org](https://arxiv.org/pdf/2607.18186))

---

## 1. Bass–Connell–Wright reduction

### 1.1 Precise statement

Over a characteristic-zero field, after translating so that \(F(0)=0\) and linearly normalizing \(DF(0)=I\), the BCW construction replaces a Keller map by a higher-dimensional map

\[
\Phi(Z)=Z+\mathcal H(Z),
\]

where:

- \(\mathcal H\) is homogeneous of degree \(3\);
- \(J\mathcal H\) is nilpotent;
- polynomial invertibility of \(F\) is equivalent to polynomial invertibility of \(\Phi\).

The proof proceeds through stabilization and elementary polynomial automorphisms, followed by a unipotent reduction and homogenization. The optional multilinearization step is not needed here. ([researchgate.net](https://www.researchgate.net/publication/38390367_The_Jacobian_conjecture_Reduction_of_degree_and_formal_expansion_of_the_inverse))

### 1.2 Normalize Alpöge’s map

Compose on the target with

\[
(a,b,c)\longmapsto \left(\frac c2,b,a\right).
\]

This changes determinant \(-2\) to \(1\) and gives \(F_0=I+\) higher terms:

\[
\begin{aligned}
f_1&=x-\frac32x^2y-\frac12x^3z,\\
f_2&=y+3xz+12xy^2+6x^2yz+9x^2y^3+3x^3y^2z,\\
f_3&=z+4y^2+3xyz+7xy^3+3x^2y^2z+3x^2y^4+x^3y^3z.
\end{aligned}
\]

Its terms of degree at least \(4\) number

\[
\begin{array}{c|cccc}
d&4&5&6&7\\ \hline
\#\text{ terms}&3&2&2&1.
\end{array}
\]

### 1.3 The elementary degree-lowering gadget

Suppose a term \(\lambda M=PQ\) of degree \(d>3\) occurs in component \(i\). Introduce two variables \(u,v\) and use

\[
S(X,u,v)=(X,u+P(X),v+Q(X)),
\]

followed on the target by

\[
T(Y,U,V)=(Y-UVe_i,U,V).
\]

Then

\[
\widetilde F=T\circ(F\times I_2)\circ S
\]

has \(i\)-th component

\[
F_i-(u+P)(v+Q)
  =(F_i-PQ)-uQ-Pv-uv,
\]

and two new components \(u+P\), \(v+Q\). Thus the original degree-\(d\) term disappears and is replaced by terms of degrees

\[
p+1,\quad q+1,\quad 2,\quad p,\quad q,
\]

where \(p=\deg P,\ q=\deg Q,\ p+q=d\). This is exactly the BCW Section II.3 gadget. ([researchgate.net](https://www.researchgate.net/publication/38390367_The_Jacobian_conjecture_Reduction_of_degree_and_formal_expansion_of_the_inverse))

Fix balanced choices

\[
4=2+2,\quad 5=2+3,\quad 6=3+3,\quad 7=3+4.
\]

If \(c(d)\) denotes the number of gadgets needed to eliminate one degree-\(d\) term, then

\[
c(d)=1+c(p+1)+c(q+1)+c(p)+c(q),
\qquad c(d)=0\quad(d\leq3),
\]

giving

\[
c(4)=1,\qquad c(5)=2,\qquad c(6)=3,\qquad c(7)=5.
\]

Therefore Alpöge’s eight high-degree terms require

\[
3c(4)+2c(5)+2c(6)+c(7)
=3+4+6+5=18
\]

gadgets. Since each adds two variables,

\[
s=3+2\cdot18=\boxed{39}.
\]

This is the support-tracked count independently recorded by Long. ([arxiv.org](https://arxiv.org/pdf/2607.18186))

The auxiliary variables at this stage are

\[
u_1,v_1,\ldots,u_{18},v_{18}.
\]

With a fixed lexicographic factorization rule for each monomial, this gives an exact implementable map

\[
K(X)=X+K_2(X)+K_3(X),\qquad X\in\mathbf C^{39},
\]

where \(K_j\) is homogeneous of degree \(j\).

Under the syntactic, non-sharing schedule, the original 13 nonlinear terms become

\[
13+4\cdot18=85
\]

quadratic/cubic term occurrences: every gadget replaces one term by five, a net increase of four.

### 1.4 Unipotent reduction and homogenization

Introduce a second block \(Y\in\mathbf C^{39}\) and define

\[
U(X,Y)=
\left(
X+K_2(X)+Y,\;
Y-K_3(X)
\right).
\]

Its fibers are explicitly those of \(K\): solving \(U(X,Y)=(A,B)\) gives

\[
Y=B+K_3(X),\qquad K(X)=A-B.
\]

Finally introduce \(T\) and homogenize:

\[
\boxed{
\Phi_{79}(X,Y,T)=
\left(
X+T K_2(X)+T^2Y,\;
Y-K_3(X),\;
T
\right).
}
\]

Thus

\[
\Phi_{79}=I_{79}+\mathcal H_{79},
\qquad
\mathcal H_{79}
=
\left(
T K_2(X)+T^2Y,\;
-K_3(X),\;
0
\right),
\]

and every component of \(\mathcal H_{79}\) is cubic homogeneous. The dimension is

\[
\boxed{N_{\mathrm{BCW}}=2\cdot39+1=79}.
\]

The cubic part has exactly

\[
85+39=\boxed{124}
\]

term occurrences: 85 from \(K_2,K_3\), plus the 39 terms \(Y_iT^2\).

So the standard sparse implementation is **not enormous**: 79 variables and 124 cubic terms.

### 1.5 Smaller carrier-shared implementation

A posted mechanical BCW implementation shares intermediate “carrier” variables and produces a degree-\(3\) map in only 19 variables, with 16 carriers and an explicit three-point collision. ([rhicksrad.github.io](https://rhicksrad.github.io/jacobian-degree3/))

Let that map be \(G=(G_1,\ldots,G_{19})\), and normalize its linear part by

\[
K=\left(\frac{G_3}{2},G_2,G_1,G_4,\ldots,G_{19}\right).
\]

Then

\[
K=I_{19}+K_2+K_3,
\]

with exactly

\[
31\text{ quadratic terms}+31\text{ cubic terms}.
\]

Applying the same doubling and homogenization gives

\[
\boxed{
\Phi_{39}(X,Y,T)=
\left(
X+TK_2(X)+T^2Y,\;
Y-K_3(X),\;
T
\right)
}
\]

in

\[
\boxed{2\cdot19+1=39}
\]

variables, with \(39+31+31=81\) cubic terms.

Thus:

- **79** is the transparent unshared textbook output;
- **39** is an explicit carrier-shared BCW output;
- neither is an invariant of the original map.

---

## 2. Drużkowski form

### 2.1 The classical construction

For a cubic-homogeneous map \(f(z)=z+\mathcal H(z)\), write the vector cubic as

\[
\mathcal H(z)=B_0(D_0z)^{*3}
\]

for rectangular matrices \(D_0,B_0\). After padding so that \(B\) is surjective and \(D\) is injective, put

\[
A=DB.
\]

Then the higher-dimensional map

\[
\mathscr D(U)=U+(AU)^{*3}
\]

is paired with \(f\). The pairing preserves constant Jacobian, injectivity, surjectivity, and polynomial invertibility. A clean constructive version, including explicit formulas for \(A,B,C,D\), is given by Gorni–Zampieri. ([arxiv.org](https://arxiv.org/pdf/1204.4026))

It is therefore applied **after** the cubic-homogeneous BCW reduction, not directly to the original degree-\(7\) map.

### 2.2 An exact \(575\times575\) matrix from the 79-variable output

Write the 124 cubic terms of \(\mathcal H_{79}\) as

\[
\mathcal H_{79}(Z)
=
\sum_{\nu=1}^{124}
\lambda_\nu e_{i_\nu}
\,r_\nu s_\nu t_\nu,
\]

where repetitions among \(r_\nu,s_\nu,t_\nu\) are allowed.

Use the universal polarization identity

\[
rst=
\frac{
(r+s+t)^3+(r-s-t)^3
-(r+s-t)^3-(r-s+t)^3
}{24}.
\]

For each of the 124 monomial occurrences, introduce four rows of \(D_0\):

\[
\begin{aligned}
\ell_{\nu,1}&=r_\nu+s_\nu+t_\nu,\\
\ell_{\nu,2}&=r_\nu-s_\nu-t_\nu,\\
\ell_{\nu,3}&=r_\nu+s_\nu-t_\nu,\\
\ell_{\nu,4}&=r_\nu-s_\nu+t_\nu,
\end{aligned}
\]

and four corresponding columns of \(B_0\):

\[
\frac{\lambda_\nu}{24}e_{i_\nu},\quad
\frac{\lambda_\nu}{24}e_{i_\nu},\quad
-\frac{\lambda_\nu}{24}e_{i_\nu},\quad
-\frac{\lambda_\nu}{24}e_{i_\nu}.
\]

Hence

\[
q=4\cdot124=\boxed{496},
\]

with

\[
D_0\in M_{496\times79}(\mathbf Q),
\qquad
B_0\in M_{79\times496}(\mathbf Q),
\]

and

\[
\mathcal H_{79}(Z)=B_0(D_0Z)^{*3}.
\]

The rows of \(D_0\) span all 79 coordinates:

- \(Y_iT^2\) spans every \(Y_i\) and \(T\);
- every BCW carrier occurs at least in the permanent quadratic term \(u_jv_j\);
- \(x,y,z\) occur in the original terms.

Therefore \(D_0\) has column rank 79. It remains only to make \(B\) surjective. Set

\[
B=\begin{pmatrix}B_0&I_{79}\end{pmatrix},
\qquad
D=
\begin{pmatrix}
D_0\\
0_{79\times79}
\end{pmatrix}.
\]

Then

\[
B\in M_{79\times575}(\mathbf Q),\qquad
D\in M_{575\times79}(\mathbf Q),
\]

and the required matrix is exactly

\[
\boxed{
A=DB=
\begin{pmatrix}
D_0B_0&D_0\\
0&0
\end{pmatrix}
\in M_{575}(\mathbf Q).
}
\]

Thus the fixed construction gives

\[
\boxed{N_{\mathrm{Drużkowski}}=496+79=575}.
\]

Moreover,

\[
\operatorname{rank}A=79,\qquad
\ker A=\ker B.
\]

This block formula is an exact specification of every entry of \(A\); printing 330,625 entries would be much less useful than supplying \(B_0,D_0\) and the polarization rule.

### 2.3 Smaller \(327\)-variable version

For the 39-variable carrier-shared homogeneous map, the 81 cubic terms split as follows:

\[
\begin{array}{c|cc}
\text{source}&\text{three distinct variables}&\text{type }ab^2\\ \hline
Y_iT^2&0&19\\
TK_2&27&4\\
-K_3&18&13\\ \hline
\text{total}&45&36.
\end{array}
\]

Use four cubes for the 45 squarefree terms, and

\[
ab^2=\frac{(a+b)^3+(a-b)^3-2a^3}{6}
\]

for the 36 repeated-variable terms. Then

\[
q=4\cdot45+3\cdot36=288.
\]

Adding the \(39\)-column identity block to \(B_0\) gives

\[
\boxed{N=288+39=327},
\]

with

\[
\boxed{
A=
\begin{pmatrix}
D_0B_0&D_0\\
0&0
\end{pmatrix}
\in M_{327}(\mathbf Q),\qquad \operatorname{rank}A=39.
}
\]

This \(327\) count is my calculation, not something I found already published.

---

## 3. Does the non-injectivity witness transfer?

**Yes. Constructively, at every step.** More strongly, the generic degree \(3\) transfers.

### 3.1 One BCW degree-lowering step

For

\[
\widetilde F=T\circ(F\times I_2)\circ S,
\]

if \(F(p_1)=F(p_2)=F(p_3)\), define

\[
\widetilde p_j=S^{-1}(p_j,0,0)
=
\left(p_j,-P(p_j),-Q(p_j)\right).
\]

Then

\[
\widetilde F(\widetilde p_j)
=
T(F(p_j),0,0),
\]

which is independent of \(j\). Thus the collision is transported by explicit polynomial formulas.

Because stabilization and pre/post composition by automorphisms give bijections on fibers, they preserve every fiber cardinality and the function-field degree, not just noninvertibility.

### 3.2 Doubling and homogenization

Let \(p_j^{(s)}\) be the three lifted points of the final degree-\(3\) map \(K\). Then

\[
q_j=
\left(
p_j^{(s)},\;
K_3(p_j^{(s)}),\;
1
\right)
\]

satisfies

\[
\Phi(q_j)=
\left(
K(p_j^{(s)}),0,1
\right).
\]

So the three points remain explicit and rational.

The generic degree is also preserved. For a target \((A,B,t)\) with \(t\neq0\),

\[
\Phi(X,Y,t)=(A,B,t)
\]

is equivalent to

\[
Y=B+K_3(X)
\]

and

\[
K(tX)=tA-t^3B.
\]

Consequently, for every \(t\neq0\), the fiber is naturally bijective to a fiber of \(K\). Hence the cubic-homogeneous map remains generically \(3\)-to-\(1\).

### 3.3 Drużkowski pairing

Let

\[
C=
\begin{pmatrix}
0_{q\times r}\\
I_r
\end{pmatrix},
\qquad BC=I_r,
\]

where \(r=79\) or \(39\). Then

\[
f(z)=B\mathscr D(Cz).
\]

Suppose \(f(z_1)=f(z_2)=f(z_3)\). Fix \(z_1\), and define

\[
\delta_j=\mathscr D(Cz_1)-\mathscr D(Cz_j).
\]

Since \(B\delta_j=0\),

\[
\delta_j\in\ker B=\ker A.
\]

Set

\[
U_j=Cz_j+\delta_j.
\]

For \(\delta\in\ker A\),

\[
\mathscr D(U+\delta)=\mathscr D(U)+\delta.
\]

Therefore

\[
\mathscr D(U_j)
=
\mathscr D(Cz_j)+\delta_j
=
\mathscr D(Cz_1).
\]

The points remain distinct because

\[
BU_j=z_j.
\]

This also gives a fiber bijection. For an arbitrary target \(V\),

\[
z\longmapsto
Cz+V-\mathscr D(Cz)
\]

is a bijection

\[
f^{-1}(BV)\;\longrightarrow\;\mathscr D^{-1}(V).
\]

So the Drużkowski map is also generically \(3\)-to-\(1\). This is not merely a contrapositive existence argument.

---

## 4. The Dixmier direction

### 4.1 The logical direction matters

Tsuchimoto and Belov–Kanel–Kontsevich prove

\[
\boxed{\mathrm{JC}_{2n}\Longrightarrow \mathrm{DC}_n}.
\]

Their arguments pass through reduction to positive characteristic; the BKK paper explicitly identifies finite-characteristic reduction as its main tool. ([arxiv.org](https://arxiv.org/abs/math/0512171))

The contrapositive is

\[
\neg\mathrm{DC}_n\Longrightarrow\neg\mathrm{JC}_{2n},
\]

**not**

\[
\neg\mathrm{JC}_{2n}\Longrightarrow\neg\mathrm{DC}_n.
\]

Therefore appending a fourth coordinate to Alpöge’s map gives a counterexample to \(\mathrm{JC}_4\), but it does **not** produce an endomorphism of \(A_2\). There is no \(A_2\) endomorphism “corresponding” to that map under this implication—constructively or nonconstructively.

The BKK/Tsuchimoto route is indeed unsuitable as a coefficient-by-coefficient transformation from a Jacobian counterexample to a Weyl endomorphism, but the deeper obstruction here is simply that the arrow points the wrong way.

### 4.2 The correct explicit consequence is in \(A_3\)

The classical same-dimensional implication is

\[
\mathrm{DC}_n\Longrightarrow\mathrm{JC}_n.
\]

Its contrapositive gives

\[
\neg\mathrm{JC}_3\Longrightarrow\neg\mathrm{DC}_3,
\]

and this direction is completely explicit.

Let

\[
J=DF.
\]

Because \(\det J=-2\),

\[
J^{-1}=-\frac12\operatorname{adj}(J)
\]

has polynomial entries. Define polynomial derivations

\[
D_i=\sum_{k=1}^3 (J^{-1})_{ki}\,\partial_{x_k}.
\]

Then

\[
D_i(F_j)=\delta_{ij},
\qquad
[D_i,D_j]=0.
\]

Hence

\[
\boxed{
\Psi(x_i)=F_i,\qquad
\Psi(\partial_i)=D_i
}
\]

defines an endomorphism of

\[
A_3(\mathbf C)
=
\mathbf C\langle x_i,\partial_i\rangle/
([\partial_i,x_j]-\delta_{ij}).
\]

It is injective because the Weyl algebra is simple. It is not surjective: the order-zero part of its image is \(\mathbf C[F_1,F_2,F_3]\), but \(x\notin\mathbf C[F]\), since \(x\) takes the three values \(0,1,-1\) on the displayed colliding points while every polynomial in \(F\) has the same value there.

This exact \(A_3\) construction has already been written down and machine-audited; the posted audit reports about two minutes for all exact checks. ([github.com](https://github.com/wmayner/dixmier-counterexample))

Appending \(w\) to \(F\) gives only the equally explicit \(A_4\) endomorphism

\[
\Psi\otimes\operatorname{id}_{A_1},
\]

with \(w\mapsto w\), \(\partial_w\mapsto\partial_w\). It still does not descend to \(A_2\).

---

## 5. Feasibility

| Object | Variables | Degree / size | Laptop verdict |
|---|---:|---|---|
| Original map | 3 | degrees \(7,6,4\); 16 expanded terms | Trivial |
| Unshared degree-\(3\) BCW map \(K\) | 39 | 85 nonlinear term occurrences | Easy |
| Homogeneous BCW map | 79 | 124 cubic terms, 79 linear terms | Easy to construct/evaluate; naive \(79\times79\) determinant expansion unnecessary |
| Carrier-shared homogeneous map | 39 | 81 cubic terms, 39 linear terms | Very easy |
| Drużkowski matrix from 79-map | 575 | \(575^2=330{,}625\) rational entries; rank 79 | Matrix and collision easy in sparse/factored form |
| Drużkowski matrix from 39-map | 327 | rank 39; 288 nonzero cube components | Easy in sparse/factored form |
| Explicit Weyl endomorphism | \(A_3\) | 3 polynomial images plus 3 first-order operators | Easy |

For the \(575\)-variable Drużkowski construction:

- \(B_0\) has only 496 nonzero entries;
- \(D_0\) has at most \(3\cdot496=1488\) nonzero entries;
- the factored representation \(A=DB\) is small;
- evaluating \(U+(AU)^{*3}\) is straightforward.

What is potentially hopeless is **fully expanding** every cube. A row of \(A\) can, in a crude worst case, involve up to 499 variables, whose cube contains at most

\[
\binom{501}{3}=20{,}833{,}250
\]

ordinary cubic monomials. Across 496 nonzero cubic components, the deliberately loose worst-case bound exceeds \(10^{10}\) monomial occurrences. One should therefore retain the form

\[
U+(AU)^{*3}
\]

rather than expand it.

For the Weyl endomorphism, the coefficients of the \(D_i\) are \(2\times2\) cofactors of \(DF\), divided by \(-2\). Their degrees are at most

\[
(7-1)+(6-1)=11,
\]

so this is a genuinely small explicit object.

---

## Cited versus computed here

**Cited:**

- BCW’s constructive degree and homogeneous reductions;
- the tracked 79-variable bound;
- the posted 19-variable cubic map;
- Gorni–Zampieri’s constructive pairing and preservation of injectivity;
- \(JC_{2n}\Rightarrow DC_n\);
- the already-posted explicit \(A_3\) Weyl endomorphism.

**Computed here:**

- the exact 124-term count for the fixed 79-variable schedule;
- the \(575\times575\) block matrix \(A=DB\);
- the compressed \(327\times327\) alternative;
- the explicit collision-lifting formulas through homogenization and Drużkowski pairing;
- the feasibility and expansion-size estimates.