# Bregman Problem 2, Part II attempt 2 — part2b (gpt-5.6-sol, effort=max, 2026-08-13 00:39)

> SINGLE-MODEL, UNREFEREED. Attacks the ghost-face obstruction isolated by
> attempt 1's Lemma SOL.6. part2a tries to CONSTRUCT it, part2b to EXCLUDE it.

# Status

**Alternative (B) is true.** Under \(\operatorname{dom}f=X\), hypothesis (b) is removable:

\[
\boxed{
C\text{ closed, nonempty, and right }D_f\text{-Chebyshev}
\quad\Longrightarrow\quad
C^*=\nabla f(C)\text{ is convex}.
}
\]

The missing perturbation direction is not \(q-p_x\). It is an **outward supporting normal to \(\overline{U^*}\) at the ghost \(q\)**. In that direction, every point of \(S=C^*\subset U^*\) is strictly behind \(q\). Consequently, after perturbation the ghost value is the exact infimum over \(S\), but no point of \(S\) can attain it. This contradicts (c).

I find no error in the attached lemmas used below. I include the convexification step independently so that the conclusion does not rely on the compressed proof of attached SOL.6(3).

---

## Lemma SOL.1 — Dual formulation and relative closedness

**Hypotheses.** Let \(f:X\to]-\infty,+\infty]\) be Legendre with
\[
\operatorname{dom}f=X=\mathbb R^n.
\]
Let
\[
g:=f^*,\qquad \Omega:=U^*=\operatorname{int}\operatorname{dom}g,
\]
and let \(C\subset X\) be closed and nonempty. Put
\[
S:=C^*=\nabla f(C).
\]

**Conclusions.**

1. \(\nabla f:X\to\Omega\) and \(\nabla g:\Omega\to X\) are mutually inverse homeomorphisms.
2. \(S\) is closed relative to \(\Omega\).
3. If \(p=\nabla f(y)\), then
   \[
   D_f(x,y)=f(x)+g(p)-\langle x,p\rangle.
   \tag{SOL.1.1}
   \]
4. Hence right \(D_f\)-Chebyshevness is equivalent to the existence, for every \(x\in X\), of a unique
   \[
   p_x\in\operatorname*{argmin}_{p\in S}
   \big(g(p)-\langle x,p\rangle\big).
   \tag{SOL.1.2}
   \]

**Proof.**

The gradient homeomorphism statement is standard Legendre duality.

If \(p_j\in S\) and \(p_j\to p\in\Omega\), then
\[
\nabla g(p_j)\in C,\qquad
\nabla g(p_j)\to\nabla g(p).
\]
Closedness of \(C\) gives \(\nabla g(p)\in C\), hence \(p\in S\).

Finally, Fenchel equality gives
\[
g(p)=\langle p,y\rangle-f(y)
\]
when \(p=\nabla f(y)\). Substitution into the definition of \(D_f\) yields (SOL.1.1), and the gradient bijection gives (SOL.1.2). ∎

---

## Lemma SOL.2 — Explicit uniform coercivity of all bounded tilts

**Hypotheses.** Let \(f\) be proper, lower semicontinuous and convex with \(\operatorname{dom}f=X\), and put \(g=f^*\).

**Conclusion.** For \(R\ge0\), define
\[
A_R:=\max_{\|z\|=R+1}f(z)<+\infty.
\]
Then for every \(\|x\|\le R\) and every \(p\in X\),
\[
g(p)-\langle x,p\rangle\ge \|p\|-A_R.
\tag{SOL.2.1}
\]
Consequently,
\[
g(p)-\langle x,p\rangle\le M
\quad\Longrightarrow\quad
\|p\|\le M+A_R.
\tag{SOL.2.2}
\]

**Proof.**

For \(p\neq0\), choose
\[
z=(R+1)\frac{p}{\|p\|}.
\]
Then
\[
g(p)\ge \langle z,p\rangle-f(z)
\ge (R+1)\|p\|-A_R.
\]
Since \(\langle x,p\rangle\le R\|p\|\), (SOL.2.1) follows. The case \(p=0\) follows from \(g(0)\ge-A_R\). ∎

In particular, \(g\) is supercoercive.

---

## Lemma SOL.3 — LSC hull and localization of every extra minimizer

**Hypotheses.** Assume those of SOL.1, and suppose \(C\) is right \(D_f\)-Chebyshev. Define
\[
h:=g+\iota_S.
\]
Let its lower-semicontinuous hull be
\[
\bar h(q):=
\lim_{\rho\downarrow0}\;
\inf_{\|z-q\|<\rho}h(z).
\tag{SOL.3.1}
\]

For \(x\in X\), let \(p_x\in S\) be the unique minimizer of
\[
h_x(p):=h(p)-\langle x,p\rangle,
\]
and set
\[
m_x:=h(p_x)-\langle x,p_x\rangle.
\]

**Conclusions.**

1. One has
   \[
   g\le \bar h\le h,
   \qquad
   \bar h(p)=h(p)=g(p)\quad(p\in S).
   \tag{SOL.3.2}
   \]
2. \(\bar h\) is proper, lower semicontinuous and supercoercive.
3. \(p_x\) minimizes \(\bar h-\langle x,\cdot\rangle\), with minimum \(m_x\).
4. Every additional minimizer lies in
   \[
   \overline S\setminus\Omega\subset\operatorname{bd}\Omega.
   \tag{SOL.3.3}
   \]
5. If \(q\) is such an additional minimizer, there is a recovery sequence \(s_j\in S\) satisfying
   \[
   s_j\to q,
   \qquad
   h(s_j)\to\bar h(q),
   \qquad
   h(s_j)-\langle x,s_j\rangle\to m_x.
   \tag{SOL.3.4}
   \]

**Proof.**

Because \(h\ge g\) and \(g\) is lower semicontinuous,
\[
g\le\bar h.
\]
The constant sequence at a point gives \(\bar h\le h\). Thus equality holds on \(S\), proving (SOL.3.2). Supercoercivity follows from \(\bar h\ge g\) and SOL.2.

Since \(h_x\ge m_x\), taking lower limits gives
\[
\bar h(p)-\langle x,p\rangle\ge m_x
\]
for every \(p\). Equality holds at \(p_x\).

Suppose \(q\in\Omega\) is another minimizer. Since \(\bar h(q)<+\infty\), the definition of the lsc hull supplies \(s_j\in S\) with \(s_j\to q\) and \(h(s_j)\to\bar h(q)\). Relative closedness of \(S\) in \(\Omega\) gives \(q\in S\). Hence
\[
h(q)-\langle x,q\rangle=m_x,
\]
contradicting uniqueness over \(S\), unless \(q=p_x\). Thus every additional minimizer is outside \(\Omega\). The recovery sequence also proves \(q\in\overline S\), hence \(q\in\operatorname{bd}\Omega\). ∎

---

## Lemma SOL.4 — A boundary point has a strict outward supporting normal

**Hypotheses.** Let \(\Omega\subset X\) be nonempty, open and convex, and let
\[
q\in\operatorname{bd}\Omega.
\]

**Conclusion.** There exists a unit vector \(\nu\in X\) such that
\[
\langle \nu,z-q\rangle\le0
\qquad(z\in\overline\Omega),
\tag{SOL.4.1}
\]
and, more strongly,
\[
\delta_q(z):=\langle\nu,q-z\rangle>0
\qquad(z\in\Omega).
\tag{SOL.4.2}
\]

**Proof.**

The supporting-hyperplane theorem applied to the closed convex set \(\overline\Omega\) at \(q\) gives a nonzero \(\nu\) satisfying (SOL.4.1). Normalize it so that \(\|\nu\|=1\).

If equality held in (SOL.4.1) at some \(z\in\Omega\), choose \(\rho>0\) such that
\[
B(z,\rho)\subset\Omega.
\]
Then
\[
z+\frac{\rho}{2}\nu\in\Omega
\]
but
\[
\left\langle\nu,z+\frac{\rho}{2}\nu-q\right\rangle
=\frac{\rho}{2}>0,
\]
contradicting (SOL.4.1). Therefore the inequality is strict throughout \(\Omega\). ∎

---

## Lemma SOL.5 — Ghost-face exclusion by an outward-normal perturbation

**Hypotheses.** Assume (a) and (c). Use the notation of SOL.3. Suppose, for contradiction, that for some \(x\in X\) there exists
\[
q\in\operatorname{bd}\Omega
\]
such that
\[
q\in\operatorname*{argmin}
\big(\bar h-\langle x,\cdot\rangle\big).
\]

**Conclusion.** For every \(\varepsilon>0\),
\[
\operatorname*{argmin}_{p\in S}
\big(g(p)-\langle x+\varepsilon\nu,p\rangle\big)
=\varnothing,
\]
where \(\nu\) is the supporting normal from SOL.4. This contradicts (c). Hence no ghost minimizer exists.

**Proof.**

Write
\[
m:=m_x
=\bar h(q)-\langle x,q\rangle.
\]
By SOL.3, choose \(s_j\in S\) such that
\[
s_j\to q,
\qquad
h(s_j)-\langle x,s_j\rangle\to m.
\tag{SOL.5.1}
\]

Let \(\nu\) be the unit supporting normal from SOL.4, and fix any \(\varepsilon>0\). For every \(s\in S\subset\Omega\), define
\[
A_x(s):=h(s)-\langle x,s\rangle-m\ge0
\]
and
\[
\delta_q(s):=\langle\nu,q-s\rangle>0.
\]
Then the exact perturbation identity is
\[
\begin{aligned}
&h(s)-\langle x+\varepsilon\nu,s\rangle
-\big(m-\varepsilon\langle\nu,q\rangle\big)
\\
&\qquad=
A_x(s)+\varepsilon\delta_q(s)
>0.
\end{aligned}
\tag{SOL.5.2}
\]

Thus every \(s\in S\) satisfies
\[
h(s)-\langle x+\varepsilon\nu,s\rangle
>
m-\varepsilon\langle\nu,q\rangle.
\tag{SOL.5.3}
\]

On the other hand, the recovery sequence satisfies
\[
A_x(s_j)\to0,
\qquad
\delta_q(s_j)\to0.
\]
Therefore, by (SOL.5.2),
\[
h(s_j)-\langle x+\varepsilon\nu,s_j\rangle
\longrightarrow
m-\varepsilon\langle\nu,q\rangle.
\tag{SOL.5.4}
\]

Combining (SOL.5.3) and (SOL.5.4) gives
\[
\inf_{s\in S}
\big(h(s)-\langle x+\varepsilon\nu,s\rangle\big)
=
m-\varepsilon\langle\nu,q\rangle,
\]
but no \(s\in S\) attains that value.

Because \(\operatorname{dom}f=X\), the perturbed parameter
\[
x+\varepsilon\nu
\]
belongs to \(U=X\). Right \(D_f\)-Chebyshevness therefore requires the corresponding minimizer over \(S\) to exist. This contradiction excludes \(q\). ∎

### Key point

The direction \(q-p_x\) need not work because points of \(\Omega\) can lie farther than \(q\) in that direction. The supporting normal \(\nu\) satisfies the decisive global inequality
\[
\langle\nu,s\rangle<\langle\nu,q\rangle
\qquad(s\in S).
\]
Hence no jumping minimizer can beat the ghost value: the perturbed infimum is forced to be the unattained boundary limit.

---

## Lemma SOL.6 — Convexification once ghosts are excluded

**Hypotheses.** Let \(f\) be Legendre with \(\operatorname{dom}f=X\), put \(g=f^*\) and \(\Omega=\operatorname{int}\operatorname{dom}g\). Let \(S\subset\Omega\) be nonempty and relatively closed.

Let \(k:X\to]-\infty,+\infty]\) be proper and lower semicontinuous, and suppose

1. \(g\le k\);
2. \(k=g\) on \(S\);
3. for every \(x\in X\), the function
   \[
   k(p)-\langle x,p\rangle
   \]
   has a unique minimizer \(p_x\in S\).

**Conclusion.** \(S\) is convex.

**Proof.**

### Step 1: Local boundedness and continuity of \(x\mapsto p_x\)

Fix \(x_0\in X\), choose
\[
R:=\|x_0\|+1,
\]
and fix \(s_0\in S\). For \(\|x\|\le R\), minimality gives
\[
\begin{aligned}
g(p_x)-\langle x,p_x\rangle
&\le k(p_x)-\langle x,p_x\rangle\\
&\le k(s_0)-\langle x,s_0\rangle\\
&\le g(s_0)+R\|s_0\|=:M_R.
\end{aligned}
\]
By SOL.2,
\[
\|p_x\|\le M_R+A_R
\qquad(\|x\|\le R).
\tag{SOL.6.1}
\]

Now let \(x_j\to x_0\), and write \(p_j=p_{x_j}\), \(p_0=p_{x_0}\). The bound (SOL.6.1) makes \((p_j)\) bounded. If \(p_{j_\ell}\to\bar p\), then minimality yields
\[
\begin{aligned}
k(p_{j_\ell})-\langle x_0,p_{j_\ell}\rangle
&\le
k(p_0)-\langle x_0,p_0\rangle\\
&\quad+
\langle x_{j_\ell}-x_0,p_{j_\ell}-p_0\rangle.
\end{aligned}
\tag{SOL.6.2}
\]
Taking lower and upper limits and using lower semicontinuity gives
\[
k(\bar p)-\langle x_0,\bar p\rangle
\le
k(p_0)-\langle x_0,p_0\rangle.
\]
Uniqueness at \(x_0\) implies \(\bar p=p_0\). Thus
\[
x_j\to x_0\quad\Longrightarrow\quad p_{x_j}\to p_{x_0}.
\tag{SOL.6.3}
\]

### Step 2: Differentiability of the conjugate

Let
\[
F:=k^*.
\]
Supercoercivity of \(k\), inherited from \(k\ge g\), implies that \(F\) is finite everywhere. Moreover,
\[
F(x)=\langle x,p_x\rangle-k(p_x).
\]

For \(v\in X\), the two optimality inequalities give
\[
\langle v,p_x\rangle
\le F(x+v)-F(x)
\le\langle v,p_{x+v}\rangle.
\]
Consequently,
\[
0\le
F(x+v)-F(x)-\langle p_x,v\rangle
\le
\|v\|\,\|p_{x+v}-p_x\|.
\tag{SOL.6.4}
\]
By (SOL.6.3), the right-hand side is \(o(\|v\|)\). Hence
\[
F\in C^1(X),
\qquad
\nabla F(x)=p_x.
\tag{SOL.6.5}
\]

### Step 3: The range of \(\nabla F\) is exactly \(S\)

The inclusion
\[
\nabla F(X)\subset S
\]
is part of the hypotheses.

Conversely, take \(p\in S\) and put
\[
y:=\nabla g(p).
\]
Legendre duality gives
\[
\operatorname*{argmin}_{z\in X}
\big(g(z)-\langle y,z\rangle\big)
=
\partial f(y)
=
\{p\}.
\tag{SOL.6.6}
\]
Since \(k\ge g\) and \(k(p)=g(p)\), the same \(p\) is the unique minimizer of
\[
k(z)-\langle y,z\rangle.
\]
Thus \(p_y=p\), proving
\[
\nabla F(X)=S.
\tag{SOL.6.7}
\]

### Step 4: Identification with a subdifferential domain

Put
\[
H:=F^*=k^{**}.
\]
Fenchel subgradient inversion and (SOL.6.5) give
\[
p\in\partial F(x)
\quad\Longleftrightarrow\quad
x\in\partial H(p).
\]
Therefore
\[
\operatorname{dom}\partial H
=
\nabla F(X)
=
S.
\tag{SOL.6.8}
\]

### Step 5: Relative closedness forces convexity

Let
\[
p_0,p_1\in S,\qquad 0<t<1,
\qquad r=(1-t)p_0+tp_1.
\]
Since \(p_0,p_1\in\operatorname{dom}H\) and \(\operatorname{dom}H\) is convex,
\[
r\in\operatorname{dom}H.
\]
Also \(r\in\Omega\), because \(\Omega\) is convex.

Choose
\[
a\in\operatorname{ri}(\operatorname{dom}H).
\]
In finite dimensions,
\[
\operatorname{ri}(\operatorname{dom}H)
\subset\operatorname{dom}\partial H=S.
\tag{SOL.6.9}
\]
For \(0<\eta<1\), set
\[
r_\eta=(1-\eta)r+\eta a.
\]
If
\[
B_{\operatorname{aff}(\operatorname{dom}H)}(a,\rho)
\subset\operatorname{dom}H,
\]
then convexity gives the explicit inclusion
\[
B_{\operatorname{aff}(\operatorname{dom}H)}
(r_\eta,\eta\rho)
\subset\operatorname{dom}H.
\]
Thus
\[
r_\eta\in\operatorname{ri}(\operatorname{dom}H)
\subset S.
\]
Since \(r_\eta\to r\), \(r\in\Omega\), and \(S\) is relatively closed in \(\Omega\), it follows that \(r\in S\). Therefore \(S\) is convex. ∎

---

## Theorem SOL.7 — Hypothesis (b) is removable

**Hypotheses.** Let \(f\) be Legendre on \(X=\mathbb R^n\) with
\[
\operatorname{dom}f=X.
\]
Let \(C\subset X\) be closed and nonempty, and suppose \(C\) is right \(D_f\)-Chebyshev.

**Conclusion.**
\[
C^*=\nabla f(C)
\]
is convex. No assumption on \(\overline{C^*}\) is required.

**Proof.**

Let \(S=C^*\), \(h=g+\iota_S\), and \(k=\bar h\).

By SOL.3, the unique minimizer \(p_x\in S\) of every tilt of \(h\) is also a minimizer of the corresponding tilt of \(k\), and every possible additional minimizer is a boundary ghost.

SOL.5 excludes every such ghost: its existence would make the perturbed tilt at \(x+\varepsilon\nu\) have an unattained infimum, contradicting right \(D_f\)-Chebyshevness.

Thus every tilt of \(k\) has the unique minimizer \(p_x\in S\). Moreover,
\[
g\le k,\qquad k=g\text{ on }S,
\]
and \(S\) is relatively closed in \(\Omega\). Lemma SOL.6 therefore gives that \(S=C^*\) is convex. ∎

---

# GHOST-FACE EXCLUSION PRINCIPLE

The requested principle holds in the following stronger form:

\[
\boxed{
\text{Under (a) and tilt attainment for every }x,
\text{ no boundary point can minimize any lsc-hull tilt.}
}
\]

Indeed, if \(q\in\operatorname{bd}U^*\) were such a minimizer, choose an outward unit normal
\[
\nu\in N_{\overline{U^*}}(q).
\]
Then, for every \(s\in C^*\),
\[
\langle\nu,s\rangle<\langle\nu,q\rangle.
\]
The perturbed ghost value at \(x+\varepsilon\nu\) is approached by the recovery sequence, while every actual point has the strictly positive excess
\[
\underbrace{
h(s)-\langle x,s\rangle-m_x
}_{\ge0}
+
\varepsilon
\underbrace{
\langle\nu,q-s\rangle
}_{>0}.
\]
Hence the infimum is not attained.

The finite-height boundary accumulation itself may still exist—for example for the square-root kernel—but it can never be a minimizing ghost.

---

# VERIFICATION RECIPE

## 1. Exact algebraic check of the decisive perturbation identity

```python
import sympy as sp

A, eps, delta, m, nq = sp.symbols(
    'A eps delta m nq',
    real=True
)

# A = h_x(s)-m >= 0
# delta = <nu,q-s> > 0
# <nu,s> = <nu,q>-delta
ns = nq - delta
hx = m + A

perturbed_value = hx - eps*ns
ghost_floor = m - eps*nq

gap = sp.expand(perturbed_value - ghost_floor)

assert sp.simplify(gap - (A + eps*delta)) == 0
```

Under
\[
A\ge0,\qquad \varepsilon>0,\qquad\delta>0,
\]
the exact gap is strictly positive.

## 2. Exact recovery-sequence sanity check

The following rational model checks the limiting mechanism without floating-point arithmetic:

```python
j, eps = sp.symbols('j eps', positive=True)
A_j = 1/j**2
delta_j = 1/j

gap_j = A_j + eps*delta_j

assert sp.limit(A_j, j, sp.oo) == 0
assert sp.limit(delta_j, j, sp.oo) == 0
assert sp.limit(gap_j, j, sp.oo) == 0
```

Every finite member has positive gap, while the gaps tend to zero. That is exactly “infimum approached but not attained.”

## 3. Exact checks for any proposed ghost configuration

Given proposed data \(x,q,s_j\):

1. Verify
   \[
   q\in\operatorname{bd}U^*.
   \]
2. Find a supporting normal \(\nu\) satisfying
   \[
   \langle\nu,z-q\rangle\le0
   \quad(z\in\overline{U^*}).
   \]
   For a polyhedral \(U^*\), this is an exact rational LP check.
3. Verify strictness for interior points:
   \[
   \langle\nu,q-s\rangle>0
   \quad(s\in C^*).
   \]
4. Verify the recovery limits
   \[
   s_j\to q,\qquad
   h(s_j)-\langle x,s_j\rangle\to m_x.
   \]
5. Form exactly
   \[
   A_j=
   h(s_j)-\langle x,s_j\rangle-m_x,
   \qquad
   \delta_j=\langle\nu,q-s_j\rangle.
   \]
6. Check
   \[
   A_j\ge0,\quad\delta_j>0,\quad
   A_j\to0,\quad\delta_j\to0.
   \]
7. The perturbed excess is exactly
   \[
   A_j+\varepsilon\delta_j.
   \]
   Therefore every finite point is strictly above the boundary limit, while the sequence approaches it.

## 4. Convexification checks

A referee need only verify the following standard finite-dimensional chain:

\[
\text{unique minimizers of all lsc coercive tilts}
\Longrightarrow
k^*\in C^1,
\]
\[
\nabla k^*(X)=S,
\]
\[
S=\operatorname{dom}\partial k^{**},
\]
and
\[
\operatorname{ri}(\operatorname{dom}k^{**})
\subset \operatorname{dom}\partial k^{**}.
\]

The explicit local bound needed for the first implication is
\[
\|p_x\|
\le
g(s_0)+R\|s_0\|+A_R
\qquad(\|x\|\le R).
\]

---

# WHAT REMAINS

1. **No gap remains for alternative (B) in finite-dimensional \(X\).** Hypothesis (b) is removable under the stated assumptions (a) and (c).

2. The proof uses three standard finite-dimensional convex-analysis facts:
   - Legendre gradient duality;
   - the supporting-hyperplane theorem at every boundary point of an open convex set;
   - \(\operatorname{ri}(\operatorname{dom}H)\subset\operatorname{dom}\partial H\) for proper closed convex \(H\).

3. The crucial use of \(\operatorname{dom}f=X\) is that every outward perturbation
   \[
   x+\varepsilon\nu
   \]
   remains an admissible projection parameter. If \(U\neq X\), that perturbation may leave \(U\); this is exactly why the Part I counterexample is not contradicted.

4. Finite-height accumulation on \(\operatorname{bd}U^*\) is not excluded. What is excluded is its participation as a minimizer of an lsc-hull tilt.

5. Infinite-dimensional variants are not addressed; compactness of bounded minimizing sequences and the relative-interior argument would require separate treatment.