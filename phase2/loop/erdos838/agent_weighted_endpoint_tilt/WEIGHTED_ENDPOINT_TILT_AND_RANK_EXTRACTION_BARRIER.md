# A weighted endpoint floor, and why it does not localize rank

**Date:** 2026-08-17. All logarithms are base two.

## Plain-language verdict

There is a clean weighted extension of the strong-tree endpoint theorem.
At every activity $0<t\leq1$, the best rooted cap and cup path polynomials
have product at least

\[
  2^{\frac12\ell(\ell-1)},\qquad
  \ell=\log(1+nt).
\]

At the fixed-rank scale $n=4^k,t=2^{-k}$, this is exactly the quadratic
partition-function scale one would hope to Legendre-transform into the
missing $3k^2/2$ coefficient.  The transform is not justified: the whole
weighted mass can be carried by only about $k/2$ selectable sibling roles,
so the corresponding endpoint bank has degree below $k$ and its rank-$k$
coefficient is zero.  Internal faces of the large sibling blocks may still
pay, but that requires a new recursive rank-allocation theorem.  Thus the
weighted endpoint floor is a genuine theorem and a useful state variable,
but it does not by itself improve Erdős 838.

## 1. Rooted endpoint polynomials

Let $T$ be an ordered full binary strong-decomposition tree with $n$ leaves.
For a leaf $x$, let

\[
 X_x(t)=\sum_{A}t^{|A|-1},
\]

where the sum is over caps whose leftmost leaf is $x$.  Define $Y_y(t)$
dually using cups with rightmost leaf $y$, and put

\[
 X_T(t)=\max_xX_x(t),\qquad Y_T(t)=\max_yY_y(t).       \tag{1}
\]

The endpoint label has been divided out, so a singleton leaf has
$X=Y=1$.  If $T=A\prec B$, with $a=|A|$ and $b=|B|$, the exact recurrences
are

\[
\begin{aligned}
 X_T(t)&=\max\{(1+bt)X_A(t),X_B(t)\},\\
 Y_T(t)&=\max\{Y_A(t),(1+at)Y_B(t)\}.                 \tag{2}
\end{aligned}
\]

Indeed, a cap rooted in $A$ may use zero or one arbitrary leaf of $B$;
all other rooted caps lie wholly in $B$.  The cup statement is reflected.

## 2. The scalar drop lemma

Put

\[
             \phi(u)={u(u-1)\over2}.                  \tag{3}
\]

> **Lemma.** If $a\geq b\geq1$ and $0<t\leq1$, then
> \[
> \log(1+bt)\geq
> \phi(\log(1+(a+b)t))-\phi(\log(1+at)).              \tag{4}
> \]

**Proof.** Set $x=1+at$ and $y=bt$.  Then $0\leq y\leq x-1$.  First,

\[
 \log(1+y)\geq \log x\,\log(1+y/x).                  \tag{5}
\]

To see this without approximation, use natural logarithms and define

\[
 h(y)=(\ln2)\ln(1+y)-(\ln x)\ln(1+y/x).
\]

The numerator of $h'(y)$ after multiplication by the positive factor
$(1+y)(x+y)$ is affine in $y$.  Hence $h$ first increases and then
decreases, or is monotone.  Its minimum on $[0,x-1]$ is therefore at an
endpoint.  But

\[
 h(0)=0,
 \qquad
 h(x-1)=\ln x\{\ln2-\ln(2-1/x)\}\geq0,
\]

which proves (5).  Now write

\[
 A=\log x,qquad B=\log(x+y).
\]

Since $y\leq x$, one has $B\leq A+1$.  Thus (5) gives

\[
 \log(1+y)\geq A(B-A)
 \geq {B-A\over2}(A+B-1)=\phi(B)-\phi(A),
\]

which is (4). $\square$

## 3. Weighted endpoint theorem

> **Theorem.** For every ordered full binary strong tree $T$ on $n$ leaves
> and every $0<t\leq1$,
> \[
> \boxed{
> \log\{X_T(t)Y_T(t)\}
> \geq \phi(\log(1+nt)).}                              \tag{6}
> \]

**Proof.** Follow a larger child at the root.  If it is $A$, then $a\geq b$
and (2) gives

\[
 \log(X_TY_T)\geq\log(X_AY_A)+\log(1+bt).             \tag{7}
\]

Apply induction to $A$ and Lemma (4).  The case in which $B$ is larger is
the reflected argument.  At a leaf, $X=Y=1$, while
$0\leq\log(1+t)\leq1$ and hence $\phi(\log(1+t))\leq0$.
This proves the base case and the theorem. $\square$

For $n=4^k$ and $t=2^{-k}$, one has

\[
 \ell=\log(1+2^k)=k+o(1),
 \qquad
 \log(X_TY_T)\geq {k^2-k\over2}-o(1).                \tag{8}
\]

This is the correct quadratic scale for a tilted endpoint reservoir.

## 4. Exact degree obstruction

An endpoint bank has the form

\[
                  P(z)=\prod_{i=1}^d(1+s_i z),         \tag{9}
\]

where the $s_i$ are sizes of disjoint discarded sibling subtrees.  At the
same canonical activity, take

\[
 n=4^k,qquad t=2^{-k},qquad
 d=\left\lfloor{k-1\over2}\right\rfloor,qquad
 q=\left\lfloor{n-1\over d}\right\rfloor.             \tag{10}
\]

A literal root-to-leaf spine with $d$ right sibling blocks of size $q$
contains the cap bank

\[
                         P(z)=(1+qz)^d.                 \tag{11}
\]

It uses at most $n$ leaves.  Its weighted logarithm satisfies

\[
 \log P(2^{-k})
 =d\log(1+q2^{-k})
 ={k^2\over2}-O(k\log k).                              \tag{12}
\]

Nevertheless $\deg P=d<k$, so

\[
                         [z^k]P(z)=0.                   \tag{13}
\]

Thus even the full quadratic weighted endpoint scale does not force the
target rank in one rooted bank.  This is not a low-face construction: the
$q$-leaf sibling blocks have their own internal faces, and a successful
proof may charge those recursively.  It is an exact barrier to the simpler
inference

\[
 \text{large endpoint partition function}
 \quad\Longrightarrow\quad
 \text{large rank-$k$ endpoint coefficient}.           \tag{14}
\]

## 5. Consequence for the proof strategy

Theorem (6) completes the local part of ledger item P1g.  The attempted
graded propagation fails its mandatory viability test because of
(10)--(13).  P1g should therefore be banked as a construction-side theorem,
not promoted as a coefficient-bearing route.

The remaining strict statement is a **recursive rank-allocation theorem**:
when a tilted endpoint bank has fewer than $k$ roles, its few large sibling
blocks must contribute internal faces in a way that survives the outer
orientation and lands in a positive interval of total rank.  That is the
same near-full-seam lower-tail problem already recorded as P1b/P1d, not a
new reformulation of it.

## 6. Verification

Run

~~~text
python3 phase2/loop/erdos838/agent_weighted_endpoint_tilt/verify_weighted_endpoint_tilt.py
~~~

The verifier checks the scalar lemma at high precision on a broad rational
grid; exhausts every ordered binary tree through ten leaves and several
rational activities, recomputing (2) exactly; and checks the spine
construction and the asymptotic ledger in (10)--(13) through $k=128$.

