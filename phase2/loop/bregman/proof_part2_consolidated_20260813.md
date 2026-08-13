# Part II consolidated — hypothesis (b) is removable (gpt-5.6-sol, effort=max, 2026-08-13 02:16)

> Merges the two independent wave-2 proofs with the four referee repairs applied.
> Self-contained by construction. Still requires its own referee lane.

# Removal of the dual-closure hypothesis for right Bregman–Chebyshev sets

## 1. Setting and statement

Let \(X=\mathbb R^n\), \(n\ge 1\), with its Euclidean inner product and norm. Let  
\[
f:X\to(-\infty,+\infty]
\]
be Legendre, meaning proper, lower semicontinuous, convex, essentially smooth, and essentially strictly convex. Put
\[
U:=\operatorname{int}\operatorname{dom}f,
\qquad
g:=f^*,
\qquad
\Omega:=U^*:=\operatorname{int}\operatorname{dom}g.
\]

For \(x,y\in U\), define
\[
D_f(x,y):=f(x)-f(y)-\langle\nabla f(y),x-y\rangle.
\]
For \(C\subset U\), the right Bregman projection is
\[
P_C^\to(x):=
\operatorname*{argmin}_{y\in C}D_f(x,y),
\]
where the second argument varies. “\(C\) is right \(D_f\)-Chebyshev” means that \(P_C^\to(x)\) is a nonempty singleton for every \(x\in U\).

For a set \(C\), write
\[
C^*:=\nabla f(C).
\]

---

## Main theorem

### Theorem 1 — Hypothesis (b) in Fact 3.2 is entirely redundant under full domain

Let \(f\) be Legendre on \(X=\mathbb R^n\) and suppose
\[
\operatorname{dom}f=X.
\]
Let \(C\subset X\) be arbitrary. Assume that, for every \(x\in X\),
\[
P_C^\to(x)
=
\operatorname*{argmin}_{y\in C}D_f(x,y)
\]
is a singleton.

Then:

1. \(C\) is automatically nonempty and closed;
2. \(C^*=\nabla f(C)\) is convex.

In particular,
\[
\boxed{
\operatorname{dom}f=X
\quad\text{and}\quad
C\text{ right }D_f\text{-Chebyshev}
\ \Longrightarrow\
\nabla f(C)\text{ is convex}.
}
\]

No assumption of the form
\[
\overline{\nabla f(C)}\subset U^*
\]
is needed.

The proof follows after the preliminary lemmas.

---

# 2. Finite-dimensional convex-analysis preliminaries

For a proper function \(\phi\), its subdifferential is
\[
\partial\phi(x)
:=
\bigl\{p:\phi(z)\ge \phi(x)+\langle p,z-x\rangle
\ \text{for every }z\bigr\}.
\]

### Lemma 2 — Basic convex facts used below

Let \(\phi\) be proper, lower semicontinuous, and convex.

1. **Fenchel equality and subgradient inversion.**
   \[
   \phi(x)+\phi^*(p)\ge \langle x,p\rangle,
   \]
   with equality exactly when
   \[
   p\in\partial\phi(x)
   \quad\Longleftrightarrow\quad
   x\in\partial\phi^*(p).
   \]

2. **Relative-interior subgradients.**
   \[
   \operatorname{ri}(\operatorname{dom}\phi)
   \subset \operatorname{dom}\partial\phi.
   \]

3. A finite convex function is continuous on the interior of its domain. If it is differentiable there, its gradient is continuous.

4. If \(\phi\) is differentiable and strictly convex on an open convex set, then for \(x\ne y\),
   \[
   \phi(x)>
   \phi(y)+\langle\nabla\phi(y),x-y\rangle.
   \]

#### Proof

Fenchel’s inequality follows directly from
\[
\phi^*(p)=\sup_z\bigl(\langle p,z\rangle-\phi(z)\bigr).
\]
Equality at \(x\) means
\[
\langle p,z\rangle-\phi(z)
\le \langle p,x\rangle-\phi(x)
\]
for every \(z\), which is exactly \(p\in\partial\phi(x)\). Applying the same argument to \(\phi^*\), together with the finite-dimensional Fenchel–Moreau identity \(\phi^{**}=\phi\), gives the inversion equivalence.

For the relative-interior assertion, fix
\[
a\in\operatorname{ri}(\operatorname{dom}\phi)
\]
and put
\[
V:=\operatorname{span}(\operatorname{dom}\phi-a).
\]
The restriction of \(\phi\) to \(a+V\) is finite on a relative neighborhood of \(a\). Its directional derivative
\[
d(v):=\lim_{t\downarrow0}
\frac{\phi(a+tv)-\phi(a)}{t},
\qquad v\in V,
\]
is therefore finite and sublinear. The finite-dimensional dominated-extension theorem supplies a linear functional \(\ell\) on \(V\) such that
\[
\ell(v)\le d(v)\qquad(v\in V).
\]
For \(a+v\in\operatorname{dom}\phi\), monotonicity of one-dimensional secant slopes gives
\[
d(v)\le \phi(a+v)-\phi(a).
\]
Representing \(\ell(v)=\langle p,v\rangle\), and extending \(p\) from \(V\) to \(X\), gives
\[
\phi(z)\ge\phi(a)+\langle p,z-a\rangle
\]
for every \(z\). Thus \(p\in\partial\phi(a)\).

Continuity of a finite convex function on an open set follows from the usual local-cube argument: convexity bounds the function above by its values at finitely many surrounding vertices, reflection gives a local lower bound, and the secant inequalities then give local Lipschitz continuity.

If \(\phi\) is differentiable, local boundedness of subgradients and closedness of the subgradient graph imply continuity of the gradient. Indeed, if \(x_j\to x\), every cluster point of \(\nabla\phi(x_j)\) belongs to
\[
\partial\phi(x)=\{\nabla\phi(x)\}.
\]

Finally, for \(x\ne y\), strict convexity gives, for \(0<t<1\),
\[
\phi(y+t(x-y))
<
(1-t)\phi(y)+t\phi(x).
\]
After subtracting \(\phi(y)\), dividing by \(t\), and letting \(t\downarrow0\), one obtains the strict first-order inequality. ∎

---

### Lemma 3 — Full-domain Legendre duality

Assume \(f\) is Legendre and
\[
\operatorname{dom}f=X.
\]
Then:

1. \(f\) is finite, continuously differentiable, and strictly convex on \(X\);
2. \(\Omega=\operatorname{int}\operatorname{dom}f^*\) is nonempty, open, and convex;
3. \(\nabla f:X\to\Omega\) is a homeomorphism;
4. its inverse is \(\nabla g\), where \(g=f^*\):
   \[
   (\nabla f)^{-1}=\nabla g.
   \]

#### Proof

Because \(f\) is essentially smooth and \(\operatorname{dom}f=X\), it is differentiable throughout \(X\). Since it is essentially strictly convex and
\[
\operatorname{dom}\partial f=X,
\]
it is strictly convex on \(X\). Lemma 2 gives continuity of \(f\) and \(\nabla f\).

The gradient is injective: if
\[
\nabla f(x)=\nabla f(y)
\]
with \(x\ne y\), applying the strict first-order inequality in both directions gives a contradiction.

We next show that the range of \(\nabla f\) is open. Fix \(x\in X\), put
\[
p:=\nabla f(x),
\]
and choose \(r>0\). On the sphere \(\|z-x\|=r\), the continuous function
\[
z\mapsto f(z)-f(x)-\langle p,z-x\rangle
\]
is strictly positive. Hence its minimum is some \(\delta>0\).

If
\[
\|v\|<\frac{\delta}{2r},
\]
then on that sphere,
\[
f(z)-\langle p+v,z\rangle
>
f(x)-\langle p+v,x\rangle.
\]
Thus \(f-\langle p+v,\cdot\rangle\) attains its minimum over the closed ball \(B(x,r)\) at an interior point \(y\). First-order optimality gives
\[
\nabla f(y)=p+v.
\]
Therefore the range of \(\nabla f\) is open.

Fenchel equality shows that every point of this range belongs to \(\operatorname{dom}g\), so
\[
\nabla f(X)\subset\Omega.
\]

Conversely, take \(p\in\Omega\). By Lemma 2, \(\partial g(p)\ne\varnothing\). If
\[
x\in\partial g(p),
\]
Fenchel inversion gives
\[
p\in\partial f(x)=\{\nabla f(x)\}.
\]
Thus \(p=\nabla f(x)\), proving
\[
\nabla f(X)=\Omega.
\]

Moreover,
\[
\partial g(p)
=
\{x:p=\nabla f(x)\}.
\]
Injectivity of \(\nabla f\) makes this a singleton. Hence \(g\) is differentiable on \(\Omega\), with
\[
\nabla g=(\nabla f)^{-1}.
\]
Both gradients are continuous by Lemma 2, so they are mutually inverse homeomorphisms. ∎

---

# 3. Attainment already forces \(C\) to be nonempty and closed

This is the repair needed to make the phrase “under (a) and (c) alone” literally correct.

### Lemma 4 — Right-projection attainment forces nonemptiness and closedness

Assume \(f\) is Legendre with \(\operatorname{dom}f=X\). Let \(C\subset X\) and suppose
\[
\operatorname*{argmin}_{y\in C}D_f(x,y)
\]
is nonempty for every \(x\in X\). Then \(C\) is nonempty and closed.

#### Proof

Nonemptiness follows immediately from existence of any one projection.

Let \(z\in\overline C\). Choose \(y_j\in C\) with
\[
y_j\to z.
\]
Continuity of \(f\) and \(\nabla f\) gives
\[
D_f(z,y_j)
=
f(z)-f(y_j)-\langle\nabla f(y_j),z-y_j\rangle
\longrightarrow0.
\]
Since Bregman distances are nonnegative,
\[
\inf_{y\in C}D_f(z,y)=0.
\]
By attainment, some \(\bar y\in C\) satisfies
\[
D_f(z,\bar y)=0.
\]
Strict convexity and Lemma 2 give
\[
D_f(z,\bar y)=0\quad\Longleftrightarrow\quad z=\bar y.
\]
Thus \(z\in C\). Therefore \(C\) is closed. ∎

---

# 4. Exact dual formulation

### Lemma 5 — Right projection is exactly a dual tilt minimization

Assume the hypotheses of Lemma 3 and let \(C\subset X\) be closed and nonempty. Put
\[
S:=\nabla f(C)\subset\Omega.
\]
Then:

1. \(S\) is closed relative to \(\Omega\);
2. for \(y\in C\) and \(p=\nabla f(y)\),
   \[
   D_f(x,y)
   =
   f(x)+g(p)-\langle x,p\rangle;
   \]
3. for every \(x\in X\),
   \[
   \nabla f\!\left(
     \operatorname*{argmin}_{y\in C}D_f(x,y)
   \right)
   =
   \operatorname*{argmin}_{p\in S}
   \bigl(g(p)-\langle x,p\rangle\bigr).
   \tag{4.1}
   \]

Thus the two argmin sets have exactly the same cardinality; in particular, emptiness, existence, uniqueness, and multiplicity are all preserved.

#### Proof

If
\[
p_j\in S,\qquad p_j\to p\in\Omega,
\]
then
\[
\nabla g(p_j)\in C
\]
and, by continuity of \(\nabla g\),
\[
\nabla g(p_j)\to\nabla g(p).
\]
Closedness of \(C\) gives \(\nabla g(p)\in C\), hence \(p\in S\). Thus \(S\) is relatively closed in \(\Omega\).

For \(p=\nabla f(y)\), Fenchel equality gives
\[
g(p)=\langle p,y\rangle-f(y).
\]
Therefore
\[
\begin{aligned}
D_f(x,y)
&=f(x)-f(y)-\langle p,x-y\rangle\\
&=f(x)+g(p)-\langle x,p\rangle.
\end{aligned}
\]
The additive term \(f(x)\) is independent of \(y\), and
\[
\nabla f:C\to S
\]
is a bijection. Hence (4.1) follows as an equality of argmin sets. ∎

---

# 5. The corrected arbitrary-slope bound

The unit-slope estimate proves coercivity. Supercoercivity requires the following arbitrary-slope form.

### Lemma 6 — Uniform arbitrary-slope coercivity

Let \(f\) be proper, lower semicontinuous, convex, and finite on \(X\), and put \(g=f^*\). For \(R\ge0\) and \(L>0\), define
\[
A_{R,L}
:=
\max_{\|z\|=R+L}f(z)<+\infty.
\]
Then, for every \(\|x\|\le R\) and every \(p\in X\),
\[
g(p)-\langle x,p\rangle
\ge
L\|p\|-A_{R,L}.
\tag{5.1}
\]

Consequently \(g\) is supercoercive:
\[
\frac{g(p)}{\|p\|}\longrightarrow+\infty
\qquad(\|p\|\to\infty).
\]

#### Proof

For \(p\ne0\), choose
\[
z=(R+L)\frac p{\|p\|}.
\]
By the definition of \(g\),
\[
g(p)\ge \langle z,p\rangle-f(z)
\ge (R+L)\|p\|-A_{R,L}.
\]
Since
\[
\langle x,p\rangle\le R\|p\|,
\]
we obtain (5.1).

For \(p=0\), choose any \(z\) on the sphere of radius \(R+L\). Then
\[
g(0)\ge -f(z)\ge-A_{R,L}.
\]

Because \(L>0\) is arbitrary, taking \(R=0\) proves supercoercivity. ∎

---

# 6. The lower-semicontinuous hull and boundary ghosts

Assume from now on that every dual tilt over \(S\) has a unique attained minimizer. Define
\[
h:=g+\iota_S,
\]
where \(\iota_S=0\) on \(S\) and \(+\infty\) off \(S\).

Its lower-semicontinuous hull is
\[
k(q)
:=
\operatorname{cl}_{\mathrm{lsc}}h(q)
:=
\lim_{\rho\downarrow0}
\inf_{\|z-q\|<\rho}h(z).
\tag{6.1}
\]

This is only an lsc hull, not yet a convex hull.

For each \(x\in X\), let \(p_x\in S\) be the unique minimizer of
\[
h(p)-\langle x,p\rangle,
\]
and set
\[
m_x:=g(p_x)-\langle x,p_x\rangle.
\]

### Lemma 7 — Hull minimizers and their localization

Under the preceding hypotheses:

1. 
   \[
   g\le k\le h,
   \qquad
   k=g\quad\text{on }S.
   \tag{6.2}
   \]
2. \(k\) is proper, lower semicontinuous, and supercoercive.
3. \(p_x\) minimizes
   \[
   k(p)-\langle x,p\rangle
   \]
   with the same minimum \(m_x\).
4. If \(q\ne p_x\) is another minimizer, then
   \[
   q\in\overline S\setminus\Omega
   \subset\operatorname{bd}\Omega.
   \tag{6.3}
   \]
5. Whenever \(k(q)<+\infty\), there is a recovery sequence
   \[
   s_j\in S,\qquad
   s_j\to q,\qquad
   g(s_j)\to k(q).
   \tag{6.4}
   \]

#### Proof

Because \(g\) is lower semicontinuous and \(g\le h\), maximality of the lsc minorant gives
\[
g\le k.
\]
The constant sequence at a point gives \(k\le h\). Thus \(k=g\) on \(S\).

Since \(S\ne\varnothing\), \(k\) is finite somewhere. Also
\[
k\ge g,
\]
so Lemma 6 makes \(k\) supercoercive.

For all \(p\),
\[
h(p)-\langle x,p\rangle\ge m_x.
\]
Passing to lower limits yields
\[
k(p)-\langle x,p\rangle\ge m_x.
\]
At \(p_x\in S\),
\[
k(p_x)=g(p_x),
\]
so equality holds.

Suppose \(q\) is an additional minimizer. Then \(k(q)<+\infty\). From (6.1), choose \(s_j\) with
\[
\|s_j-q\|<\frac1j,
\qquad
h(s_j)\le
\inf_{\|z-q\|<1/j}h(z)+\frac1j.
\]
These points belong to \(S\), and
\[
h(s_j)=g(s_j)\to k(q).
\]
This proves the recovery statement and \(q\in\overline S\).

If \(q\in\Omega\), relative closedness of \(S\) gives \(q\in S\). Then
\[
g(q)-\langle x,q\rangle=m_x,
\]
contradicting uniqueness over \(S\), unless \(q=p_x\). Therefore every additional minimizer is outside \(\Omega\). Since it lies in \(\overline S\subset\overline\Omega\), it belongs to \(\operatorname{bd}\Omega\). ∎

A point \(q\) as in Lemma 7 is called a **boundary ghost**.

Crucially, its tie is
\[
\boxed{
k(q)-\langle x,q\rangle=m_x,
}
\tag{6.5}
\]
not necessarily
\[
g(q)-\langle x,q\rangle=m_x.
\]

---

# 7. No ghosts implies convexity

### Lemma 8 — Convexification after all ghosts are excluded

Retain the notation above. Suppose that, for every \(x\in X\),
\[
\operatorname*{argmin}_{p\in X}
\bigl(k(p)-\langle x,p\rangle\bigr)
=
\{p_x\},
\qquad p_x\in S.
\tag{7.1}
\]
Then \(S\) is convex.

#### Proof

Define
\[
F:=k^*.
\]
Because \(k\) is supercoercive, \(F\) is finite on all of \(X\), and
\[
F(x)=\langle x,p_x\rangle-k(p_x).
\]

### Step 1: local boundedness of \(p_x\)

Fix \(R>0\) and \(s_0\in S\). If \(\|x\|\le R\), minimality gives
\[
\begin{aligned}
g(p_x)-\langle x,p_x\rangle
&=k(p_x)-\langle x,p_x\rangle\\
&\le k(s_0)-\langle x,s_0\rangle\\
&=g(s_0)-\langle x,s_0\rangle\\
&\le g(s_0)+R\|s_0\|.
\end{aligned}
\]
Using Lemma 6 with \(L=1\),
\[
g(p_x)-\langle x,p_x\rangle
\ge \|p_x\|-A_{R,1}.
\]
Thus \(p_x\) is bounded uniformly for \(\|x\|\le R\).

### Step 2: continuity of \(x\mapsto p_x\)

Let \(x_j\to x\), and write \(p_j=p_{x_j}\), \(p=p_x\). The local bound makes \((p_j)\) bounded. If a subsequence converges to \(\bar p\), minimality gives
\[
k(p_j)-\langle x,p_j\rangle
\le
k(p)-\langle x,p\rangle
+
\langle x_j-x,p_j-p\rangle.
\]
Lower semicontinuity of \(k\) therefore yields
\[
k(\bar p)-\langle x,\bar p\rangle
\le
k(p)-\langle x,p\rangle.
\]
Uniqueness in (7.1) gives \(\bar p=p\). Hence
\[
x_j\to x\quad\Longrightarrow\quad p_{x_j}\to p_x.
\tag{7.2}
\]

### Step 3: differentiability of \(F\)

Optimality at \(x\) and \(x+v\) gives
\[
\langle v,p_x\rangle
\le F(x+v)-F(x)
\le \langle v,p_{x+v}\rangle.
\]
Therefore
\[
0
\le
F(x+v)-F(x)-\langle p_x,v\rangle
\le
\|v\|\,\|p_{x+v}-p_x\|.
\]
By (7.2), the right-hand side is \(o(\|v\|)\). Thus
\[
F\in C^1(X),
\qquad
\nabla F(x)=p_x.
\tag{7.3}
\]

### Step 4: the gradient range is exactly \(S\)

Equation (7.3) gives
\[
\nabla F(X)\subset S.
\]

Conversely, let \(p\in S\) and put
\[
x:=\nabla g(p).
\]
By Lemma 3,
\[
p=\nabla f(x).
\]
Fenchel’s inequality gives, for every \(z\),
\[
g(z)-\langle x,z\rangle\ge -f(x),
\]
with equality exactly when
\[
z\in\partial f(x)=\{p\}.
\]
Since \(k\ge g\) and \(k(p)=g(p)\), \(p\) is also the unique minimizer of
\[
k(z)-\langle x,z\rangle.
\]
Hence \(p=p_x=\nabla F(x)\). Therefore
\[
\nabla F(X)=S.
\tag{7.4}
\]

### Step 5: identification with a subdifferential domain

Let
\[
H:=F^*=k^{**}.
\]
Fenchel subgradient inversion and differentiability of \(F\) give
\[
x\in\partial H(p)
\quad\Longleftrightarrow\quad
p\in\partial F(x)
\quad\Longleftrightarrow\quad
p=\nabla F(x).
\]
Using (7.4),
\[
\operatorname{dom}\partial H=S.
\tag{7.5}
\]

### Step 6: relative closedness fills every chord

Let
\[
D:=\operatorname{dom}H.
\]
Take \(p_0,p_1\in S\) and \(0<t<1\), and put
\[
r=(1-t)p_0+tp_1.
\]
Since \(D\) and \(\Omega\) are convex,
\[
r\in D\cap\Omega.
\]

Choose
\[
a\in\operatorname{ri}D.
\]
By Lemma 2 and (7.5),
\[
a\in\operatorname{dom}\partial H=S.
\]
For \(0<\eta<1\), define
\[
r_\eta=(1-\eta)r+\eta a.
\]
If \(A=\operatorname{aff}D\) and
\[
B_A(a,\rho)\subset D,
\]
then
\[
B_A(r_\eta,\eta\rho)\subset D,
\]
because
\[
r_\eta+u
=
(1-\eta)r+\eta\left(a+\frac u\eta\right).
\]
Thus
\[
r_\eta\in\operatorname{ri}D\subset S.
\]
Now
\[
r_\eta\to r,
\qquad r\in\Omega.
\]
Since \(S\) is closed relative to \(\Omega\), \(r\in S\). Hence \(S\) is convex. ∎

---

## Lemma 9 — The ghost reduction

If \(S\) is nonconvex, then there exist
\[
x_0\in X,\qquad
p_0=p_{x_0}\in S,\qquad
q\in\operatorname{bd}\Omega
\]
such that \(q\ne p_0\) and
\[
k(q)-\langle x_0,q\rangle
=
g(p_0)-\langle x_0,p_0\rangle
=:m_0.
\tag{8.1}
\]
Moreover, there is a recovery sequence
\[
s_j\in S,\qquad
s_j\to q,\qquad
g(s_j)\to k(q).
\tag{8.2}
\]

#### Proof

If no such additional hull minimizer existed, Lemma 7 would imply that every tilt of \(k\) had the unique minimizer \(p_x\in S\). Lemma 8 would then make \(S\) convex. The contrapositive gives the ghost \(q\), and Lemma 7 gives its location, tie, and recovery sequence. ∎

This is the precise ghost statement: the tied height is \(k(q)\), which can strictly exceed \(g(q)\).

---

# 8. Supporting normals and ghost exclusion

### Lemma 10 — Every boundary point has a normal strict on the interior

Let \(\Omega\subset X\) be nonempty, open, and convex, and let
\[
q\in\operatorname{bd}\Omega.
\]
Then there exists a unit vector \(n\) such that
\[
\langle n,z-q\rangle\le0
\qquad(z\in\overline\Omega),
\tag{9.1}
\]
and
\[
\langle n,s-q\rangle<0
\qquad(s\in\Omega).
\tag{9.2}
\]

#### Proof

Put \(K=\overline\Omega\). For a nonempty open convex set,
\[
\Omega=\operatorname{int}K.
\]
Indeed, if \(a\in\Omega\), \(b\in K\), and \(0\le t<1\), then
\[
(1-t)a+tb\in\Omega;
\]
this follows by approximating \(b\) from \(\Omega\) and transporting a ball around \(a\) by convex combinations. Consequently a point interior to \(K\) must belong to \(\Omega\). Thus \(q\in\operatorname{bd}K\).

Choose \(a_j\notin K\) with \(a_j\to q\), and let \(z_j\) be the Euclidean projection of \(a_j\) onto the closed convex set \(K\). Define
\[
n_j:=\frac{a_j-z_j}{\|a_j-z_j\|}.
\]
Projection optimality gives
\[
\langle n_j,z-z_j\rangle\le0
\qquad(z\in K).
\]
Also
\[
\|a_j-z_j\|\le\|a_j-q\|\to0,
\]
so \(z_j\to q\). Passing to a convergent subsequence of the unit vectors \(n_j\) gives a unit vector \(n\) satisfying (9.1).

If equality held in (9.1) at some \(s\in\Omega\), choose \(r>0\) with
\[
B(s,r)\subset\Omega.
\]
Then \(s+\frac r2n\in\Omega\), but
\[
\left\langle n,s+\frac r2n-q\right\rangle
=\frac r2>0,
\]
contradicting (9.1). Hence strictness holds throughout \(\Omega\).

Equivalently, for every \(s\in\Omega\),
\[
\langle n,q-s\rangle>0.
\tag{9.3}
\]
Unboundedness and flat boundary faces do not affect this pointwise strictness. ∎

---

### Lemma 11 — Outward perturbation excludes every finite-height ghost

Suppose the ghost data of Lemma 9 exist. Let \(n\) be the outward supporting normal from Lemma 10. Then, for every \(t>0\), the tilt
\[
x_t:=x_0+tn
\]
has no minimizer over \(S\):
\[
\operatorname*{argmin}_{s\in S}
\bigl(g(s)-\langle x_t,s\rangle\bigr)
=\varnothing.
\tag{9.4}
\]

#### Proof

Define the perturbed ghost level
\[
L_t
:=
k(q)-\langle x_t,q\rangle
=
m_0-t\langle n,q\rangle.
\tag{9.5}
\]

For every \(s\in S\), the exact difference from \(L_t\) is
\[
\begin{aligned}
g(s)-\langle x_t,s\rangle-L_t
&=
\bigl(g(s)-\langle x_0,s\rangle-m_0\bigr)
+t\langle n,q-s\rangle.
\end{aligned}
\tag{9.6}
\]
The first term is nonnegative because \(p_0\) minimizes the original tilt over \(S\). The second is strictly positive because
\[
S\subset\Omega
\quad\text{and}\quad
\langle n,q-s\rangle>0.
\]
Therefore
\[
g(s)-\langle x_t,s\rangle>L_t
\qquad(s\in S).
\tag{9.7}
\]

On the other hand, the recovery sequence from Lemma 9 satisfies
\[
s_j\to q,
\qquad
g(s_j)\to k(q).
\]
Hence
\[
g(s_j)-\langle x_t,s_j\rangle
\longrightarrow
k(q)-\langle x_t,q\rangle
=L_t.
\tag{9.8}
\]
Thus
\[
\inf_{s\in S}
\bigl(g(s)-\langle x_t,s\rangle\bigr)=L_t,
\]
but (9.7) shows that no point of \(S\) attains this value.

No continuity of \(g\) at \(q\) was used. The argument uses only the hull height \(k(q)\) and a recovery sequence.

Every \(t>0\) is admissible because
\[
x_t\in X=\operatorname{dom}f=U.
\]
There is no small-\(t\) restriction. ∎

---

# 9. Proof of the main theorem

By Lemma 4, the assumed projection attainment makes \(C\) nonempty and closed.

Set
\[
S:=\nabla f(C).
\]
Lemma 5 shows that \(S\) is relatively closed in \(\Omega\), and that right \(D_f\)-Chebyshevness is equivalent to every dual tilt
\[
g(p)-\langle x,p\rangle,\qquad p\in S,
\]
having a unique attained minimizer.

Suppose, for contradiction, that \(S\) is nonconvex. Lemma 9 then produces a boundary ghost
\[
q\in\operatorname{bd}\Omega
\]
at the hull height
\[
k(q)-\langle x_0,q\rangle=m_0,
\]
together with a recovery sequence.

Lemma 11 shows that, for every \(t>0\), the perturbed dual tilt at
\[
x_t=x_0+tn
\]
has an unattained infimum over \(S\). By the exact argmin correspondence in Lemma 5, the right Bregman projection \(P_C^\to(x_t)\) is empty. This contradicts right \(D_f\)-Chebyshevness.

Therefore \(S=\nabla f(C)\) is convex. ∎

---

# 10. Why the hull height is indispensable

Finite boundary values of \(f^*\) do not imply boundary continuity.

Consider
\[
g(u,v)=
\begin{cases}
u^2-\sqrt u+\dfrac{v^2}{u},&u>0,\\[1ex]
0,&(u,v)=(0,0),\\
+\infty,&\text{otherwise}.
\end{cases}
\tag{10.1}
\]
Its interior domain is
\[
\Omega=(0,\infty)\times\mathbb R.
\]

On \(\Omega\),
\[
\nabla^2g(u,v)=
\begin{pmatrix}
2+\dfrac1{4u^{3/2}}+\dfrac{2v^2}{u^3}
&
-\dfrac{2v}{u^2}
\\[1.2ex]
-\dfrac{2v}{u^2}
&
\dfrac2u
\end{pmatrix},
\]
with
\[
\det\nabla^2g(u,v)
=
\frac4u+\frac1{2u^{5/2}}>0.
\]
Thus \(g\) is strictly convex on \(\Omega\).

Its extension at the origin is convex because, for \(0<t<1\),
\[
g(tu,tv)-t g(u,v)
=
(t^2-t)u^2+(t-\sqrt t)\sqrt u<0.
\]
It is lower semicontinuous at the origin since
\[
g(u,v)\ge-\sqrt u.
\]
Also,
\[
\frac{\partial g}{\partial u}
=
2u-\frac1{2\sqrt u}-\frac{v^2}{u^2}
\longrightarrow-\infty
\qquad(u\downarrow0),
\]
so \(g\) is essentially smooth. It is supercoercive, and consequently \(f:=g^*\) is finite on \(\mathbb R^2\). Strict convexity and supercoercivity give a unique dual maximizer for every tilt, making \(f\) differentiable; subgradient inversion gives injectivity of \(\nabla f\), hence strict convexity. Thus \(f\) is a full-domain Legendre function and \(f^*=g\).

At
\[
q=(0,0),
\qquad g(q)=0,
\]
but along
\[
p_u=(u,\sqrt u),
\]
one has
\[
g(p_u)=u^2-\sqrt u+1\longrightarrow1.
\]
Hence \(g\) is not continuous at \(q\).

The distinction between \(g(q)\) and a ghost height can be made exact. Let
\[
p_0=(1,1)
\]
and
\[
S
=
\{p_0\}
\cup
\left\{
\left(u,\sqrt{u(1+\sqrt u)}\right):u>0
\right\}.
\]
Along the curve,
\[
g\left(u,\sqrt{u(1+\sqrt u)}\right)
=1+u^2.
\]
Also
\[
g(p_0)=1.
\]
Thus at \(x_0=0\), \(p_0\) is the unique actual minimizer over \(S\), with value \(1\), while for
\[
h=g+\iota_S,\qquad k=\operatorname{cl}_{\mathrm{lsc}}h,
\]
the origin is a ghost satisfying
\[
k(q)=1>g(q)=0.
\]

The outward normal to \(\Omega\) at \(q\) is
\[
n=(-1,0).
\]
For \(x_t=tn=(-t,0)\),
\[
g\left(u,\sqrt{u(1+\sqrt u)}\right)
-\left\langle x_t,
\left(u,\sqrt{u(1+\sqrt u)}\right)\right\rangle
=
1+u^2+tu>1,
\]
with limit \(1\) as \(u\downarrow0\), while the value at \(p_0\) is \(1+t\). Hence the perturbed infimum is \(1\) and is not attained.

This example is not a counterexample to Theorem 1; it demonstrates exactly why right-projection attainment fails and why the proof must use \(k(q)\), not \(g(q)\).

---

# 11. Reconciliation of the two wave-2 proofs

The two wave-2 approaches do not substantively disagree.

1. **Common core.** Both:
   - pass exactly from right Bregman projection to dual tilt minimization;
   - form \(h=g+\iota_S\) and its lsc hull \(k\);
   - localize extra hull minimizers to \(\operatorname{bd}U^*\);
   - perturb in an outward supporting-normal direction;
   - use a recovery sequence to prove nonattainment.

2. **Different convexification routes.**
   - The part2a route uses quantitative separation of the unique zero and the epigraph identity for \(k^{**}\).
   - The part2b route proves \(k^*\in C^1\), identifies
     \[
     \nabla k^*(X)=S=\operatorname{dom}\partial k^{**},
     \]
     and then uses relative closedness.
   
   Both routes are valid after ghosts are excluded. This document uses the second route.

3. **The supercoercivity wording.** The unit-slope estimate in part2b proves coercivity, not supercoercivity. Lemma 6 supplies the correct arbitrary-slope estimate. The arbitrary-slope statement is the right one.

4. **The ghost height.** Any formulation using
   \[
   g(q)-\langle x_0,q\rangle=m_0
   \]
   is wrong in general. The correct relation is
   \[
   k(q)-\langle x_0,q\rangle=m_0.
   \]
   The discontinuity example above shows that \(k(q)>g(q)\) can occur.

5. **Closedness and nonemptiness.** A theorem that retained these as assumptions would remove only the dual-closure part of hypothesis (b). Lemma 4 repairs this: full-domain projection attainment itself forces both properties.

6. **Flat faces.** A flat face may contain several boundary points with equality in the supporting inequality, but every interior point satisfies strict inequality. No tangential affinity of \(g\) is needed.

---

# 12. Exact verification recipe

The following checks use exact symbolic arithmetic only.

## 12.1 Arbitrary-slope arithmetic

```python
import sympy as sp

R, L, rho = sp.symbols("R L rho", positive=True)

gain = (R + L)*rho - R*rho
assert sp.simplify(gain - L*rho) == 0
```

This is the coefficient behind
\[
g(p)-\langle x,p\rangle
\ge L\|p\|-A_{R,L}.
\]

---

## 12.2 Discontinuous boundary example

```python
u = sp.symbols("u", positive=True)
v = sp.symbols("v", real=True)

G = u**2 - sp.sqrt(u) + v**2/u

H = sp.hessian(G, (u, v))
expected_det = 4/u + 1/(2*u**sp.Rational(5, 2))

assert sp.simplify(H.det() - expected_det) == 0

# Path (u, sqrt(u)): boundary limit is 1, while g(0,0)=0.
disc_path = sp.simplify(G.subs(v, sp.sqrt(u)))
assert sp.limit(disc_path, u, 0, dir="+") == 1

# Ghost-recovery curve.
ghost_v = sp.sqrt(u*(1 + sp.sqrt(u)))
ghost_height = sp.simplify(G.subs(v, ghost_v))

assert sp.simplify(ghost_height - (1 + u**2)) == 0

# Actual point p0=(1,1).
assert sp.simplify(G.subs({u: 1, v: 1}) - 1) == 0
```

These checks certify
\[
g(q)=0,\qquad k(q)=1
\]
for the displayed set \(S\).

---

## 12.3 Supporting-normal strictness

For
\[
\Omega=\{(u,v):u>0\},\quad q=(0,0),\quad n=(-1,0),
\]
the strict interior gap is exactly \(u\).

```python
n = sp.Matrix([-1, 0])
q = sp.Matrix([0, 0])
s = sp.Matrix([u, v])

support_value = sp.simplify(n.dot(s - q))
delta = sp.simplify(n.dot(q - s))

assert support_value == -u
assert delta == u
```

Because \(u>0\),
\[
\langle n,s-q\rangle=-u<0,
\qquad
\langle n,q-s\rangle=u>0.
\]

This directly checks that unboundedness of the halfspace and flatness of its boundary cause no loss of strictness for interior points.

---

## 12.4 Exact recovery-sequence convergence

Take
\[
u_j=\frac1{j^2},
\qquad
v_j=\frac{\sqrt{j+1}}{j^{3/2}}.
\]
Then
\[
v_j^2=u_j(1+\sqrt{u_j}).
\]

```python
j, t = sp.symbols("j t", positive=True)

u_j = 1/j**2
v_j = sp.sqrt(j + 1)/j**sp.Rational(3, 2)

assert sp.simplify(v_j**2/u_j - (1 + 1/j)) == 0

g_j = 1 + 1/j**4
perturbed_j = g_j + t/j**2

assert sp.limit(u_j, j, sp.oo) == 0
assert sp.limit(v_j, j, sp.oo) == 0
assert sp.limit(g_j, j, sp.oo) == 1
assert sp.limit(perturbed_j, j, sp.oo) == 1

gap_j = sp.simplify(perturbed_j - 1)
assert sp.simplify(gap_j - (1/j**4 + t/j**2)) == 0
```

Thus every finite point has strictly positive excess
\[
\frac1{j^4}+\frac{t}{j^2}>0,
\]
while the excess converges exactly to zero. This is “infimum approached but not attained.”

---

## 12.5 Generic perturbation identity

```python
E, delta, t = sp.symbols("E delta t", nonnegative=True)

gap = E + t*delta
assert sp.expand(gap - (E + t*delta)) == 0
```

In the proof,
\[
E=g(s)-\langle x_0,s\rangle-m_0\ge0,
\qquad
\delta=\langle n,q-s\rangle>0,
\qquad
t>0,
\]
so the exact perturbed excess is
\[
E+t\delta>0.
\]

---

# 13. Comparison with Bauschke–Macklem–Wang Fact 3.2

Fact 3.2 assumed:

1. \(\operatorname{dom}f=X\);
2. \(C\subset U\) closed and nonempty, with
   \[
   \overline{\nabla f(C)}\subset U^*;
   \]
3. \(C\) right \(D_f\)-Chebyshev.

Theorem 1 keeps assumptions 1 and 3 and removes assumption 2 entirely:

- \(C\subset U\) is automatic because \(U=X\);
- nonemptiness and closedness follow from projection attainment;
- the condition
  \[
  \overline{\nabla f(C)}\subset U^*
  \]
  is unnecessary.

What is **not** improved:

- full domain \(\operatorname{dom}f=X\) remains essential to this argument;
- right projections must exist and be unique for every \(x\in X\);
- the theorem is finite-dimensional;
- no assertion is made for left Bregman projections;
- the theorem proves convexity of \(\nabla f(C)\), not necessarily convexity of \(C\);
- it does not assert that \(\nabla f(C)\) is closed in \(X\) or that its closure stays inside \(U^*\).

---

# 14. Repair audit

- **R1 — No boundary continuity claim:** satisfied. The perturbation is benchmarked against \(k(q)\), and convergence is supplied by a recovery sequence \(g(s_j)\to k(q)\).
- **R2 — Correct ghost tie:** satisfied:
  \[
  k(q)-\langle x_0,q\rangle=m_0.
  \]
- **R3 — Headline matches theorem:** satisfied by Lemma 4; nonemptiness and closedness are consequences, not retained assumptions.
- **R4 — Arbitrary-slope estimate:** satisfied by Lemma 6. The unit-slope bound is used only for boundedness; arbitrary \(L>0\) proves supercoercivity.

---

# 15. What remains

1. **No residual mathematical gap is identified for the stated finite-dimensional theorem.**

2. The proof uses ordinary foundational results of finite-dimensional convex analysis—Fenchel–Moreau duality, finite-dimensional dominated linear extension, Euclidean compactness, and projection onto a closed convex set. Their exact applications were included above; they were not reconstructed from set-theoretic foundations.

3. The following cases remain outside the theorem:
   - infinite-dimensional spaces;
   - \(\operatorname{dom}f\ne X\);
   - projection existence only on a proper subset of \(U\);
   - left Bregman projections.

4. Full domain is used decisively: the outwardly perturbed query
   \[
   x_0+tn
   \]
   must remain admissible for every \(t>0\). If \(U\ne X\), it may leave \(U\).

5. Boundary discontinuity and finite-height boundary accumulation are not ruled out. What is ruled out is their occurrence as minimizing hull ghosts while all right projections continue to attain their minima.

6. Infinite-height accumulation creates no omitted case: if every sequence \(s_j\in S\) approaching \(q\) has
   \[
   g(s_j)\to+\infty,
   \]
   then \(k(q)=+\infty\), so \(q\) cannot minimize a finite hull tilt.

7. The verification scripts are exact sanity checks, not substitutes for the general proof.