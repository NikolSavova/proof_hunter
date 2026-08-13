# Erdős 838 lower-bound campaign — verify51 (gpt-5.6-sol, effort=max, 2026-08-13 14:21)

> Target: log C + log U >= (1/2 - o(1))(log N)^2 for ARBITRARY point sets.
> With Theorem 1.1 already proved, this resolves Erdős 838 outright.

## Verdict

**The multiscale proof of Theorem 5.1 survives the audit.** Conditional on Lemma 5.2 and the stated endpoint recurrences, I find no reversed inequality, invalid max-to-sum step, or missing case. Two steps—the nonlarge-level independence and the “forward product” endgame—are compressed, but both are correct.

There is, however, a **separate major problem with the campaign premise**: the stated universal cap–cup product lemma would **not by itself finish Erdős 838** using the displayed Section 5 inequalities. It yields only coefficient \(1/4\) for \(W\), not \(1/2\). The decomposable multiscale reset supplies an additional endpoint-alignment phenomenon that is absent for arbitrary order types.

---

## 1. Case split and constants

Let
\[
d_i=\log n_i-\log n_{i+1}
   =-\log\left(1-\frac{s_i}{n_i}\right).
\]
Because the followed child is at least half the current node,
\[
0<d_i\le 1.
\]
At a nonlarge level, \(s_i/n_i<1/L^2\), and for sufficiently large \(L\),
\[
d_i\le 2\frac{s_i}{n_i}<\frac{2}{L^2}.
\]

If \(k<R\) levels are large and \(m\) are nonlarge, stopping gives
\[
4R<\log\frac{N}{n_{\rm stop}}
    =\sum_i d_i
    \le k+\frac{2m}{L^2}
    <R+\frac{2m}{L^2}.
\]
Hence
\[
m>\frac32RL^2.
\]
So the first branch’s constant is correct.

In the second branch, at every selected large node,
\[
|H|\ge \frac{n_i}{2}\ge 2^{L-4R-1},
\qquad
|Q|=s_i\ge\frac{n_i}{L^2}\ge2^{L-4R-2\lambda}.
\]
Thus both children have at least
\[
2^{L-\Delta},\qquad \Delta=4R+2\lambda+1.
\]
The extra \(+1\) is sufficient for both estimates.

If \(u=\log |S|\ge L-\Delta>3\), then
\[
\frac12u^2-3u
\ge \frac12(L-\Delta)^2-3(L-\Delta)
\ge F,
\]
where
\[
F=\frac12(L-\Delta)^2-3L.
\]
Thus the radial estimate is applied in the correct direction.

The cases are exhaustive:

1. fewer than \(R\) large levels;
2. at least \(R\) large levels and \(\mu\ge F-L\);
3. at least \(R\) large levels and \(\mu<F-L\).

---

## 2. Nonlarge-level independence is correct

Suppose \(k\) selected discarded siblings lie on the right of the heavy path. Starting with the terminal leaf, move upward.

- At an unselected level, the current selected set remains entirely inside the path child, so being a cap is preserved.
- At a selected level, the path child is \(A\) and the fixed sibling leaf lies in \(B\). By the strong-glue classification, a cap in \(A\), together with either zero or one prescribed point of \(B\), is again a cap.

Thus every one of the \(2^k\) choices is a cap. The chosen sibling subtrees are disjoint, and the terminal leaf is always included, so the resulting sets are distinct.

The left-sibling/cup case is the reflected argument.

An even shorter rigorous verification comes directly from the recurrences. At every right-sibling level,
\[
X(A\prec B)\ge (b+1)X(A)\ge2X(A),
\]
while intervening levels do not decrease \(X\). Thus \(k\) such levels imply
\[
X(P)\ge2^k.
\]
For left siblings,
\[
Y(A\prec B)\ge(a+1)Y(B)\ge2Y(B).
\]
Since at least half of the \(m>\frac32RL^2\) nonlarge levels have one direction,
\[
\log W(P)\ge \max\{\log X(P),\log Y(P)\}
   >\frac34RL^2.
\]
So the independence claim is valid; it is not merely heuristic “mixed-sign” reasoning.

---

## 3. Monotonicity, including the max structure

For \(T=A\prec B\),
\[
X(T)=\max\{(b+1)X(A),X(B)\}.
\]
Therefore
\[
X(T)\ge X(A),\qquad X(T)\ge X(B).
\]
Similarly,
\[
Y(T)=\max\{Y(A),(a+1)Y(B)\}
\]
gives
\[
Y(T)\ge Y(A),\qquad Y(T)\ge Y(B).
\]
Finally,
\[
M(T)=\max\{M(A),M(B),X(A)Y(B)\}
\]
gives monotonicity of \(M\) from either child.

Consequently, for every subtree \(S\),
\[
M(S)\le M(P),
\]
and the ceiling
\[
X(S),Y(S)\le |S|M(S)\le NM(P)
\]
indeed gives, in logarithms,
\[
x(S),y(S)\le\mu+L.
\]

No maximum is being treated as a sum. Every use simply selects one legitimate term of a maximum as a lower bound.

---

## 4. Deepest reset, attachment gains, and endgame

Assume \(\mu<F-L\), and define
\[
D=F-\mu>L,\qquad \ell=D-L>0.
\]
For every child \(S\) at a selected node,
\[
x(S)+y(S)\ge F,
\qquad
x(S),y(S)\le\mu+L.
\]
Hence each individual coordinate satisfies
\[
x(S),y(S)\ge F-(\mu+L)=\ell.
\]

### Deepest selected node

At \(A\prec B\), the crossing term gives
\[
x_A+y_B\le\mu.
\]
Then
\[
y_A\ge F-x_A
    \ge F-\mu+y_B
    \ge D+\ell
    =2D-L,
\]
and similarly
\[
x_B\ge F-y_B
    \ge F-\mu+x_A
    \ge2D-L.
\]
Therefore the parent has both coordinates at least
\[
h_0=2D-L,
\]
because \(X\) preserves \(X(B)\) and \(Y\) preserves \(Y(A)\).

### Later attachments

If the path child \(H\) is left and \(Q\) is right, then
\[
x_H+y_Q\le\mu,
\qquad
x_Q+y_Q\ge F.
\]
Subtracting gives
\[
x_Q\ge x_H+F-\mu=x_H+D.
\]
The parent preserves \(y_H\) and has \(x\)-coordinate at least \(x_Q\), so \(x\) gains \(D\).

If \(H\) is right, the reflected calculation gives
\[
y_Q\ge y_H+D,
\]
while \(x\) is preserved. Intermediate nodes preserve both coordinates by monotonicity.

### Final crossing

Among the \(R-1\) attachments, one direction occurs
\[
q_*\ge\left\lceil\frac{R-1}{2}\right\rceil
\]
times. Immediately before its final occurrence, the relevant path coordinate is at least
\[
h_0+(q_*-1)D.
\]
The crossing-compatible coordinate in the opposite child is at least \(\ell\). Hence the crossing term gives
\[
\mu\ge h_0+(q_*-1)D+\ell
     =(q_*+2)D-2L.
\]
Substituting \(D=F-\mu\),
\[
\mu\ge(q_*+2)(F-\mu)-2L,
\]
so
\[
(q_*+3)\mu\ge(q_*+2)F-2L,
\]
and therefore
\[
\mu\ge
\frac{q_*+2}{q_*+3}F-\frac{2L}{q_*+3}
=F-\frac{F+2L}{q_*+3}.
\]

Now
\[
\Delta=O(\sqrt L),\qquad
F=\frac12L^2-O(L^{3/2}),\qquad
q_*=\Omega(\sqrt L).
\]
Since \(F=O(L^2)\),
\[
\frac{F+2L}{q_*+3}=O(L^{3/2}).
\]
Thus
\[
\mu\ge\frac12L^2-O(L^{3/2}).
\]
The alternative \(\mu\ge F-L\) gives the same conclusion directly. Since \(W(P)\ge M(P)\), the theorem follows.

The algebra and all inequality directions are correct.

---

## 5. Where the proof really uses decomposability

The large-level argument is essentially an abstract max-plus reset lemma. Once the following are available, its algebra no longer uses geometry:

1. a local radial bound \(x(S)+y(S)\ge F\);
2. global ceilings \(x(S),y(S)\le\mu+L\);
3. monotonicity of \(X,Y,M\);
4. a crossing inequality
   \[
   \mu\ge x(A)+y(B);
   \]
5. a nested sequence of sufficiently large bipartitions.

The decisive reset mechanism is:

> If global \(M\) is deficient by \(D=F-\mu\), then the crossing constraint forces the opposite coordinate in the sibling to exceed the path coordinate by \(D\). Repeated attachments of the same direction accumulate this deficit until a later crossing product forces \(\mu\) back up to nearly \(F\).

The specifically tree/decomposable ingredients are:

- the heavy-path hierarchy and left/right sibling labels;
- the exact crossing term \(M(A\prec B)\ge X(A)Y(B)\);
- the directional preservation encoded by the cap/cup recurrences;
- the independent optional-leaf construction in the nonlarge branch;
- currently, the local radial bound itself, since Lemma 5.2 was proved from the decomposition tree.

The factors \(a+1,b+1\) are needed in the nonlarge branch and in Lemma 5.2, but the large-level reset uses only monotonicity and the exact crossing term.

---

## Separate decisive issue: the proposed target lemma does not yet finish the problem

Let
\[
c=\log C,\quad u=\log U,\quad x=\log X,\quad y=\log Y,\quad \mu=\log M.
\]
The displayed universal inequalities give
\[
c\le L+x,\qquad u\le L+y,
\]
and
\[
x\le L+\mu,\qquad y\le L+\mu.
\]
Therefore
\[
c+u\le 4L+2\mu,
\]
so
\[
\mu\ge\frac{c+u-4L}{2}.
\]
Since \(W\ge M\), the proposed target
\[
c+u\ge\left(\frac12-o(1)\right)L^2
\]
only implies
\[
\log W\ge\left(\frac14-o(1)\right)L^2,
\]
not coefficient \(1/2\).

The exact identity
\[
W=N+\sum_{p<q}c(p,q)u(p,q)
\]
does not repair this by itself: a dot product need not be comparable to the product of the two sums when the endpoint distributions are anticorrelated.

Thus the campaign still needs a **universal endpoint-alignment/reset lemma**, for example something on the scale
\[
\log W\ge \log C+\log U-o(L^2),
\]
or a multiscale cut inequality replacing
\[
M(A\prec B)\ge X(A)Y(B)
\]
up to subquadratic logarithmic loss.

This is precisely the part of Theorem 5.1 that remains genuinely decomposability-dependent. A universal cap–cup product bound would provide the local radial mass, but not the crossing compatibility needed to convert that mass into \(W\) with no factor-of-two loss.