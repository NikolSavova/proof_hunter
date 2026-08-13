# Part I referee — maths lane (gpt-5.6-sol, effort=max, 2026-08-12 23:53)

> Adversarial, default-to-refutation. Numeric claims made HERE are derived,
> not executed — script them before trusting.

## Mathematical audit

### 1. Lemma SOL.2

The derivative is correct:
\[
\frac{d}{dt}\bigl((4t^2-2)e^{-t^2}\bigr)
=8te^{-t^2}-2t(4t^2-2)e^{-t^2}
=4t(3-2t^2)e^{-t^2}.
\]
Hence
\[
q'(t)=e^t+4t(3-2t^2)e^{-t^2}.
\]

The three interval argument is valid.

- On \([1,\sqrt{3/2}]\), \(3-2t^2\ge0\), so \(q'(t)>0\).
- On \([\sqrt{3/2},3/2]\), with \(p(t)=8t^3-12t\),
  \[
  p'(t)=24t^2-12>0,\qquad p(3/2)=9.
  \]
  The exact Taylor certificate is
  \[
  e^{3/2}>1+\frac32+\frac{9}{8}+\frac{9}{16}
  =\frac{67}{16}>4,
  \]
  so \(e^{-3/2}<1/4\). Also \(e>5/2\). Thus
  \[
  q'(t)=e^t-p(t)e^{-t^2}>\frac52-\frac94=\frac14.
  \]
- On \([3/2,2]\), \(p(2)=40\), and
  \[
  q'(t)\ge e^{3/2}-40e^{-9/4}
  =e^{-9/4}(e^{15/4}-40).
  \]
  The tight exponential step is genuinely certified:
  \[
  \sum_{k=0}^{8}\frac{3^k}{k!}
  =\frac{806769}{40320}
  =20+\frac{369}{40320}>20,
  \]
  and
  \[
  1+\frac34+\frac{(3/4)^2}{2}
  =\frac{65}{32}>2.
  \]
  Positive omitted terms give \(e^3>20\) and \(e^{3/4}>2\), hence
  \[
  e^{15/4}=e^3e^{3/4}>40.
  \]

All listed constants check:
\[
p(3/2)=9,\quad p(2)=40,\quad
\frac{41}{12}-\frac{17}{5}=\frac1{60}.
\]
Finally,
\[
q(1)=e+\frac2e.
\]
Since \(e>8/3\) and \(s+2/s\) is strictly increasing for \(s\ge8/3\),
\[
e+\frac2e>\frac83+\frac34=\frac{41}{12}>\frac{17}{5}.
\]
There is no gap in the analytic curvature proof.

### 2. Exact divergence reduction

For \(x,y\in U\),
\[
D_f(x,y)=\sum_{j=1}^2\left[x_j\ln x_j-x_j\ln y_j-x_j+y_j\right].
\]
With \(y=c(t)=(e^t,e^{-t^2})\),
\[
-x_1\ln y_1=-x_1t,\qquad
-x_2\ln y_2=+x_2t^2.
\]
Therefore
\[
D_f(x,c(t))
=f(x)+e^t+e^{-t^2}-x_1t+x_2t^2.
\]
Thus \(K(x)=f(x)\) is exactly independent of \(t\). No term has been lost.

### 3. Global uniqueness and endpoints

The second derivative is
\[
h_x''(t)=q(t)+2x_2>\frac{17}{5}.
\]
The \(x_1\)-dependence is purely linear, while \(x_2>0\) only increases curvature. Hence the argument is valid uniformly for arbitrarily small or large positive coordinates.

Continuity on the compact interval gives existence. Strict convexity gives at most one minimizer, including endpoints. The endpoint trichotomy is exhaustive because \(h_x'\) is strictly increasing:

- \(h_x'(1)\ge0\): unique minimum at \(1\);
- \(h_x'(2)\le0\): unique minimum at \(2\);
- otherwise \(h_x'(1)<0<h_x'(2)\): one interior zero and one interior minimum.

As \(x\) approaches \(\partial U\), the curvature remains bounded below by \(17/5\). As either coordinate tends to infinity, compactness prevents parameter escape and the same endpoint/interior argument remains valid. The proof covers every finite \(x\in U\), not merely sampled points.

### 4. Legendre and hypothesis audit

The entropy extension is proper, lower semicontinuous and convex, with
\[
\dom f=\mathbb R_+^2,\qquad U=\mathbb R_{++}^2.
\]
On \(U\),
\[
\nabla f(x)=(\ln x_1,\ln x_2).
\]
Its norm diverges at every finite boundary point of \(\dom f\), establishing essential smoothness. The boundary-subgradient contradiction is valid, so
\[
\dom\partial f=U.
\]
Strict convexity on \(U=\dom\partial f\) establishes essential strict convexity. Thus \(f\) is Legendre.

The conjugate computation is exact:
\[
g^*(u)=e^u,\qquad f^*(u)=e^{u_1}+e^{u_2},
\]
so
\[
\dom f^*=U^*=\mathbb R^2,
\qquad
\nabla f:U\to U^*
\]
is the coordinatewise logarithm bijection.

The compact set \(C\) lies strictly inside \(U\), and
\[
C^*=\{(t,-t^2):1\le t\le2\}
\]
is compact. Therefore
\[
\overline{C^*}=C^*\subset U^*.
\]
Thus hypothesis (b) is genuinely retained, while only \(\dom f=X\) fails. The optional supercoercivity argument is also correct.

There is no contradiction with the supplied Luo–Meng–Wen–Yao theorem: its condition \(U=X\) fails here.

### 5. Nonconvexity

For \(C^*\), the endpoint midpoint is
\[
\frac{(1,-1)+(2,-4)}2=\left(\frac32,-\frac52\right),
\]
whereas the unique arc point with first coordinate \(3/2\) is
\[
\left(\frac32,-\frac94\right).
\]
Thus \(C^*\) is nonconvex.

For \(C\), writing it as the graph
\[
\psi(r)=e^{-(\ln r)^2},
\]
the stated derivative is correct:
\[
\psi''(r)=\frac{e^{-(\ln r)^2}}{r^2}
\left(4(\ln r)^2+2\ln r-2\right)>0
\]
for \(r\in[e,e^2]\). Hence the graph does not contain the midpoint of its endpoint points, so \(C\) is also nonconvex.

### 6. Scope of Theorem SOL.8

The six theorem items establish exactly that deleting hypothesis (a) invalidates Fact 3.2 even while hypothesis (b) and global right-Chebyshevness are retained. The manuscript correctly avoids claiming that every individual convexity conclusion requires full domain, or that this is the first nonconvex entropy example. No novelty overreach appears.

The central analytic proof therefore survives. The only defects are in the ancillary numerical documentation.

VERDICT: MINOR_REPAIRS

1. **Location:** `PROBLEM.md`, candidate curvature bullet; `verify.py` Block C; `out_verify.txt` Block C.  
   **Claim:** \(h_x''\ge 3.454041\) uniformly, and the interval run certifies \(h_x''\ge3.454\).  
   **Why wrong:** 
   \[
   \inf_{t\in[1,2]}q(t)=e+\frac2e
   \approx3.454040710802.
   \]
   Thus, for example, at \(t=1\) and \(x_2=10^{-8}\),
   \[
   h_x''(1)\approx3.454040730802<3.454041.
   \]
   Moreover, the archived interval lower bound is only \(3.453673\), and the code actually tests `> 3.45`, not `>= 3.454`; it therefore does not certify the threshold printed in the log.  
   **Suggested fix:** Replace the rounded-up claim by the exact statement
   \[
   h_x''(t)>e+\frac2e>\frac{17}{5},
   \]
   or simply by \(h_x''>3.45\). Relabel `3.453673` as a certified enclosure lower bound rather than the value of the infimum, and make the logged threshold match the tested threshold.

2. **Location:** `verify.py` header and Block D comments.  
   **Claim:** The finite grid scan is “exhaustive” and confirms the uniqueness property actually claimed.  
   **Why wrong:** It samples only 27 choices of \(x\) and finitely many \(t\)-values, so it cannot certify the quantifier “for every \(x\in U\)” or uniqueness in the continuum. It also counts only strict interior grid minima, so an endpoint minimizer produces zero such minima.  
   **Suggested fix:** Describe Block D only as a finite numerical sanity check. Cite Lemma SOL.5—not the grid scan—as the proof of the universal singleton assertion.