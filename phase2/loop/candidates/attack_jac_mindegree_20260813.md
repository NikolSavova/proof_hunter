# jac_mindegree (gpt-5.6-sol, effort=max, 2026-08-13 09:59)

## Verdict

I cannot honestly supply either **(A)** a checked total-degree \(4,5,\) or \(6\) counterexample, or **(B)** a proof excluding one of those degrees.

As of **August 13, 2026**, I found no accepted result improving the global bound
\[
4\le d_{\min}(3)\le 7.
\]
The existing exact audit explicitly leaves ordinary degrees \(4,5,6\) open, and the graded classification leaves relevant mixed-sign cases unresolved. ([github.com](https://github.com/shadybrook/jacobian-counterexample-research/blob/main/paper/main.md))

What can be proved structurally is sharper than “the search failed”:

1. **A genuinely \(2\)-to-\(1\) Keller mechanism is impossible in any degree.**
2. **The cubic marked-factor/tangent-sweep mechanism has minimum total degree exactly \(7\).** The degree-\(7\) term is essential, not removable slack within that construction.
3. Therefore, any degree-\(\le6\) example must use a genuinely different, non-Galois, generically at least \(3\)-sheeted affine modification.

The recent three-dimensional “degree four” construction in Gao’s paper is degree four in the **geometric-degree** sense, not ordinary polynomial degree. In the same weighted-lift family its ordinary component degrees are \((12,11,4)\), so it does not improve the bound here. ([arxiv.org](https://arxiv.org/html/2608.00222))

---

## 1. Why the quadratic \(2\)-to-\(1\) factorization cannot work

Let
\[
\mu:\operatorname{Sym}^r(\mathbb C^2)\times\operatorname{Sym}^s(\mathbb C^2)
\longrightarrow \operatorname{Sym}^{r+s}(\mathbb C^2),
\qquad (L,Q)\longmapsto LQ.
\]

There is a reciprocal scaling
\[
(L,Q)\longmapsto (\lambda L,\lambda^{-1}Q)
\]
that preserves \(LQ\). The resultant transforms as
\[
\operatorname{Res}(\lambda L,\lambda^{-1}Q)
=\lambda^{s-r}\operatorname{Res}(L,Q),
\]
because the resultant is homogeneous of degrees \(s\) and \(r\) in the two sets of coefficients.

For the successful \(1+2\) factorization,
\[
s-r=1.
\]
Thus \(\operatorname{Res}(L,Q)=1\) kills the scaling orbit transversely. A squarefree cubic then has
\[
\binom31=3
\]
possible marked linear factors. This is exactly the Alpöge mechanism described by Tao. ([terrytao.wordpress.com](https://terrytao.wordpress.com/?blogsub=confirming))

For a quadratic split \(1+1\), however,
\[
s-r=0.
\]
Hence the resultant is **invariant** under reciprocal scaling. Imposing
\[
\operatorname{Res}(L,M)=1
\]
does not kill the scaling direction. Indeed, the tangent vector
\[
(L,-M)
\]
is tangent to the resultant-one locus and is annihilated by \(D\mu\), since
\[
D\mu(L,-M)=LM-LM=0.
\]
So the multiplication map still has a one-dimensional differential kernel and cannot be Keller.

If one instead quotients by the scaling first, the induced map to binary quadratics is generically \(2\)-to-\(1\). But this is also impossible for a Keller counterexample for a global reason:

> A function-field extension of degree \(2\) in characteristic zero is Galois, while a Keller map whose function-field extension is Galois is an automorphism.

This is the classical Campbell–Razar–Wright Galois-case theorem. ([mathoverflow.net](https://mathoverflow.net/questions/513387/galois-structure-of-the-new-counterexample-to-the-jacobian-conjecture-an-explic))

Thus:

\[
\boxed{\text{No generically \(2\)-to-\(1\) Keller counterexample exists, in any dimension or total degree.}}
\]

More generally, a collapse arising as a quotient by an actual finite symmetry group is Galois and is therefore also excluded. The successful cubic map instead has a nonnormal degree-\(3\) extension with \(S_3\) Galois closure and no nontrivial deck transformation. ([mathoverflow.net](https://mathoverflow.net/questions/513387/galois-structure-of-the-new-counterexample-to-the-jacobian-conjecture-an-explic))

---

## 2. Degree \(7\) is forced in the one-variable weighted lift

Write
\[
u=1+xy,\qquad
\gamma=\gamma_0+\alpha xy+\beta x^2z,\qquad \beta\ne0,
\qquad w=u\gamma .
\]

For a tangent-sweep seed \(p(w)\) of degree \(d\ge2\), the twisted map has the structural form
\[
C=x\gamma,
\qquad
B=\frac{p(w)+2\gamma}{x\gamma},
\qquad
A=\frac{q(w)+\gamma w}{(x\gamma)^2},
\]
where the tangent normalization forces \(\deg q=d+1\).

After the divisibilities are imposed, the leading contributions are
\[
A_{\rm top}\sim \frac{u^{d+1}\gamma^{d-1}}{x^2},
\qquad
B_{\rm top}\sim \frac{u^d\gamma^{d-1}}x,
\qquad
C_{\rm top}\sim x\gamma .
\]

Using
\[
u_{\rm top}=xy,\qquad \gamma_{\rm top}=\beta x^2z,
\]
their leading monomials have exponent vectors
\[
(3d-3,d+1,d-1),\qquad
(3d-3,d,d-1),\qquad
(3,0,1),
\]
and therefore total degrees
\[
\boxed{5d-3,\quad 5d-4,\quad 4.}
\]

Lower powers of \(w\) have strictly smaller ordinary degree, so they cannot cancel these terms. This reproduces the exact degree-growth formula recorded in the structural audit. ([github.com](https://github.com/shadybrook/jacobian-counterexample-research/blob/main/paper/main.md))

The smallest admissible seed is \(d=2\), because \(d=1\) would produce the forbidden generic degree-\(2\) case. Therefore
\[
(5d-3,5d-4,4)=(7,6,4).
\]

For \(d=2\), the unavoidable top terms are proportional to
\[
x^3y^3z,\qquad x^3y^2z,\qquad x^3z.
\]

Hence
\[
\boxed{\text{Total degree \(7\) is minimal in the entire one-variable tangent-sweep/weighted-lift family.}}
\]

---

## 3. The master equation shows exactly where the cubic power enters

Use invariant coordinates
\[
U=xy,\qquad V=x^2z,
\]
whose ordinary source degrees are
\[
\deg U=2,\qquad \deg V=3.
\]

A map with the Alpöge weights can be written
\[
C=x\Lambda(U,V),\qquad
B=\frac{P(U,V)}x,\qquad
A=\frac{Q(U,V)}{x^2},
\]
where polynomiality is equivalent to
\[
P\in(U,V),\qquad Q\in(U^2,V).
\]

The target invariants are
\[
\beta=BC=\Lambda P,\qquad
\alpha=AC^2=\Lambda^2Q.
\]

Writing
\[
\{f,g\}=f_Ug_V-f_Vg_U,
\]
one obtains directly
\[
\{\alpha,\beta\}
=\Lambda^2\left(
2Q\{\Lambda,P\}
-P\{\Lambda,Q\}
+\Lambda\{Q,P\}
\right).
\]

Thus the Keller condition reduces to the single equation
\[
\boxed{
2Q\{\Lambda,P\}
-P\{\Lambda,Q\}
+\Lambda\{Q,P\}
=\kappa\ne0.
}
\]

For the minimal transverse one-variable ansatz, choose \(e\) with
\[
\{\Lambda,e\}\in\mathbb C^\times
\]
and write
\[
P=p(e)+\Lambda R(e),\qquad
Q=q(e)+\Lambda S(e).
\]

The coefficient of \(\Lambda^2\) in the master equation is
\[
3S R'-2R S'=0.
\]
On the nondegenerate branch \(RS\ne0\), this gives
\[
\left(\frac{R^3}{S^2}\right)'=0,
\]
hence, in the UFD \(\mathbb C[e]\),
\[
R=a\,h^2,\qquad S=b\,h^3
\]
for a polynomial \(h\).

This \(2\!:\!3\) cusp relation is the source of the cubic power. In the Alpöge normalization,
\[
e=1+U,\qquad \Lambda=2-3U-V,
\]
and
\[
P=4e+2-3\Lambda e^2,\qquad
Q=e+e^2-\Lambda e^3.
\]

The term
\[
-\Lambda e^3
\]
contains
\[
V U^3,
\]
of invariant ordinary degree
\[
3+3\cdot2=9.
\]
Dividing by \(x^2\) produces
\[
\frac{VU^3}{x^2}=x^3y^3z,
\]
of total degree \(7\).

This is not caused by the numerical choices \(2,3,4\). Those constants are normalization data. The essential ingredients are:

- the powers \(\Lambda,\Lambda^2\) required by the monomial twist;
- the forced relation \(R^3/S^2=\text{constant}\);
- a nonconstant transverse \(h\);
- the independent invariant degrees \(2\) and \(3\).

Consequently, changing the linear normalization of the cubic, the determinant, or the collision cannot remove the degree-\(7\) term. One must leave this ansatz.

Tao’s hyperplane analysis points to the same conclusion from the factorization side: among the three dual-root types, the source becomes \(\mathbb A^3\) precisely in the double-root-plus-simple-root case used here. ([terrytao.wordpress.com](https://terrytao.wordpress.com/?blogsub=confirming))

---

## 4. What a lower-degree example would have to do

A total-degree-\(\le6\) example cannot be:

- a generic double cover;
- a finite-group quotient;
- a degree-\(1\) tangent seed;
- another member of the \(1+2\) one-variable weighted lift;
- a mere linear or \(SL_2\) renormalization of the marked-cubic construction.

It would need a **nonnormal generic cover of degree at least \(3\)** together with a different polynomial compactification that clears the boundary with smaller ordinary-degree cost.

The most natural unresolved graded target is the symmetric weight pattern
\[
(1,-1,-1),
\]
rather than Alpöge’s
\[
(1,-1,-2).
\]
Its invariant generators both have ordinary degree \(2\), potentially avoiding the \(2+3\) degree penalty above. But the graded classification explicitly leaves the first cases for \((1,-1,-1)\) open; there is presently no corresponding construction. ([arxiv.org](https://arxiv.org/html/2607.20210))

So the real structural frontier is:

\[
\boxed{\text{Construct a non-Galois \(3\)-sheeted affine modification with pole-clearing orders smaller than \(1,2\).}}
\]

---

## 5. Degree \(3\) in dimension \(3\): citation caution

Three different low-degree statements should not be conflated:

1. **Wang:** total degree at most \(2\), in every dimension.
2. **Wright:** cubic-homogeneous Keller maps in dimension \(3\) are linearly triangularizable. ([tandfonline.com](https://www.tandfonline.com/doi/abs/10.1080/03081089308818214))
3. **Moh–Sathaye:** Moh’s own account states that the full three-variable case with all three components of degree at most \(3\) was checked affirmatively by computer, producing roughly a hundred-page printout. ([math.purdue.edu](https://www.math.purdue.edu/~ttm/jacobian.html))

Thus the reported lower bound \(d_{\min}(3)\ge4\) is not a consequence of Wang alone, nor should it be cited merely to the cubic-homogeneous theorem. For a publication, I would want the precise Moh–Sathaye manuscript or a subsequent published theorem/certificate before treating the bibliographic point as closed.

---

## Bottom line

I have **not** lowered the global upper bound or raised the global lower bound. The honest status remains
\[
4\le d_{\min}(3)\le7
\]
subject to the degree-\(3\) citation issue just noted.

But the structural obstruction is sharp:

\[
\boxed{
\begin{array}{l}
\text{A \(2\)-sheeted collapse is impossible globally;}\\[2mm]
\text{the first viable factorization is \(1+2\), hence \(3\)-sheeted;}\\[2mm]
\text{its resultant gauge and affine filling force the cubic cusp power;}\\[2mm]
\text{that power forces the monomial }x^3y^3z\text{ and total degree }7.
\end{array}}
\]

Therefore degree \(7\) is not slack in the known mechanism. Any degree \(4,5,\) or \(6\) counterexample must introduce genuinely new geometry.