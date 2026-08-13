# A candidate upper-bound improvement for Erdős problem 838

> Status, 2026-08-12: complete candidate proof, independently audited
> algebraically and geometrically, but not yet a public novelty claim. A
> broader literature sweep and an expert referee are still required.

All logarithms below are base \(2\), except \(\ln\), which is natural.

## Theorem

Let \(f(N)\) be the largest integer such that every \(N\)-point set in general
position in the plane determines at least \(f(N)\) subsets in convex
position. Then

\[
\boxed{\quad
\limsup_{N\to\infty}
\frac{\log_2 f(N)}{(\log_2N)^2}
\leq 1-\frac{1}{4\ln2}
=0.639326239777\ldots .
\quad}                                             \tag{T}
\]

The public April 2026 discussion of problem 838 records the weaker upper
constant \(1\), so (T) would narrow the base-\(2\) window from

\[
\frac14\leq\liminf\leq\limsup\leq1
\]

to

\[
\frac14\leq\liminf\leq\limsup
\leq1-\frac1{4\ln2}.
\]

## 1. The Pascal cells

We use the classical Erdős--Szekeres Pascal construction. For
\(0\leq i\leq m\), let \(T_{m,i}\) be its cell of

\[
n_{m,i}={m\choose i}
\]

points. The boundary cells are singletons. An interior cell is the strong
separated union

\[
T_{m,i}=A\prec B,\qquad
A=T_{m-1,i-1},\quad B=T_{m-1,i}.
\]

Here \(A\) lies to the left of \(B\), and the copies are placed so that a cap
meeting both children consists of a cap in \(A\) and at most one point of
\(B\). Reflecting the statement exchanges caps and cups. This is the
separated-union construction in the proof of Morris--Soltan Theorem 2.5.
The accompanying geometry audit gives an explicit exact-rational
realization.

Let \(C_{m,i}\) be the number of nonempty cap subsets of \(T_{m,i}\), counting
sets of one or two points as caps. Strong separation gives the exact
recurrence

\[
C_{m,i}=C_{m-1,i}
+\left(1+{m-1\choose i}\right)C_{m-1,i-1},        \tag{1}
\]

with \(C_{m,0}=C_{m,m}=1\). Indeed, a cap either lies in \(B\), or consists
of a cap in \(A\) together with zero or one of the
\({m-1\choose i}\) points of \(B\). If \(U_{m,i}\) counts nonempty cups,
reflection gives

\[
U_{m,i}=C_{m,m-i}.                                 \tag{2}
\]

## 2. Asymptotics of the cap recurrence

Expanding (1) gives a sum over lattice paths from \((0,0)\) to \((m,i)\).
A horizontal step has weight \(1\). The \(j\)-th diagonal step, if made at
time \(r\), has weight

\[
q_{r,j}=1+{r-1\choose j}.
\]

For fixed \(j\), this is nondecreasing in \(r\). Since the \(j\)-th diagonal
step must occur no later than \(r=m-i+j\), the largest path weight is

\[
M_{m,i}=\prod_{j=1}^i
\left(1+{m-i+j-1\choose j}\right).
\]

This latest-diagonal path is itself a summand, and there are at most \(2^m\)
paths. Hence

\[
M_{m,i}\leq C_{m,i}\leq2^mM_{m,i}.                \tag{3}
\]

Write

\[
H(x)=-x\log_2x-(1-x)\log_2(1-x).
\]

The standard entropy estimate for binomial coefficients, summed in (3), and
a uniform Riemann-sum estimate give, when \(i/m\to x\),

\[
\log_2C_{m,i}=m^2A(x)+O(m\log m),                 \tag{4}
\]

where

\[
A(x)=\int_0^x(1-x+s)
H\!\left(\frac{s}{1-x+s}\right)\,ds.              \tag{5}
\]

Only the upper half of (4) is needed for (T).

## 3. Use one central cell, not the full row

Put

\[
Q_m=T_{m,\lfloor m/2\rfloor}.
\]

Every convex-position subset \(S\) of an \(x\)-generic point set is uniquely
determined by the ordered pair consisting of its upper hull chain and lower
hull chain. The first is a cap and the second a cup. Therefore, with
\(i=\lfloor m/2\rfloor\),

\[
V(Q_m)\leq1+C_{m,i}U_{m,i}
=1+C_{m,i}C_{m,m-i},                              \tag{6}
\]

where \(V(Q_m)\) denotes the number of its convex-position subsets and the
initial \(1\) counts the empty set.

Since \(i/m\to1/2\), (4)--(6) imply

\[
\log_2V(Q_m)\leq2A(1/2)m^2+O(m\log m).            \tag{7}
\]

The remaining integral is elementary. From (5),

\[
\begin{aligned}
A(1/2)
&=\int_0^{1/2}\left[
(s+\tfrac12)\log_2(s+\tfrac12)-s\log_2s+\tfrac12
\right]\,ds\\
&=\frac12-\frac1{8\ln2}.
\end{aligned}                                     \tag{8}
\]

Consequently,

\[
\log_2V(Q_m)\leq
\left(1-\frac1{4\ln2}\right)m^2+O(m\log m).       \tag{9}
\]

On the other hand, Stirling's formula gives

\[
|Q_m|={m\choose\lfloor m/2\rfloor}
=2^{m-O(\log m)}.                                 \tag{10}
\]

For arbitrary \(N\), choose the least \(m\) for which \(|Q_m|\geq N\), then
retain any \(N\) points of \(Q_m\). Deleting points cannot create new
subsets of the remaining point set, and (10) gives

\[
m=\log_2N+O(\log\log N).
\]

Substitution in (9) proves (T).

## 4. Why the central cell is the best single Pascal cell

This is not needed for (T), but it checks that the choice \(i\sim m/2\) is
optimal within this family. Direct integration gives

\[
A(x)+A(1-x)=H(x)-\frac{x(1-x)}{\ln2}.             \tag{11}
\]

Since \(\log_2|T_{m,xm}|=mH(x)+o(m)\), the normalized coefficient supplied
by a cell at density \(x\) is

\[
K(x)=\frac{H(x)-x(1-x)/\ln2}{H(x)^2}.             \tag{12}
\]

It is symmetric about \(1/2\) and strictly decreases on \((0,1/2)\). For a
short verification, put

\[
h=-x\ln x-(1-x)\ln(1-x),\qquad q=x(1-x).
\]

Then \(K=\ln2\,(h-q)/h^2\), and

\[
K'=\frac{\ln2}{h^3}\bigl(h'(2q-h)-hq'\bigr)<0
\quad(0<x<1/2),
\]

because \(h',q'>0\) and \(h\geq2q\). Thus (12) is minimized at \(x=1/2\),
where it equals the constant in (T).

## 5. Verification status

The proof has four independently checkable parts.

1. **Exact geometry.** The agent_geometry/audit_geometry.py script constructs
   rational coordinates and checks every orientation. It exhaustively
   verifies (1), the hull-chain injection, and the classical row
   decomposition through \(m=5\).
2. **Exact integer recurrence.** The agent_asymptotic/dp_audit.py script
   evaluates cap, convex-cell, and row recurrences with arbitrary-precision
   integers through any requested \(m\).
3. **Asymptotics.** The agent_asymptotic/DERIVATION.md note independently
   derives (3)--(12), including log-base conversion and finite-\(m\) tables.
4. **Prior art.** The original 1978 paper, the 2000 Morris--Soltan survey,
   the current Erdős Problems page and its April 2026 comments, and direct
   searches for the constants contain no matching bound found so far.
   This is encouraging, not a completed MathSciNet-level novelty clearance.

The main remaining obligation is therefore literature/expert verification,
not a known gap in the displayed proof.

