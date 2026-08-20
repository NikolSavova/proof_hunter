# Global directional compensation: an unavoidable subpolynomial loss

## Status

Let \(A\subset[0,m]^2\cap\mathbb Z^2\) be distance-Sidon.  For every
active primitive unoriented direction \(w\), put

\[
 e_w=|\{g>0:gw\in(A-A)\setminus\{0\}\}|,
 \qquad
 M_w={m\over\|w\|_\infty},                            \tag{0.1}
\]

and let \(H_w\) be the clean closed-record load from
DIRECTIONAL_MIDPOINT_POINTWISE_NO_GO_GLOBAL_GATE.md.  Recall the exact
identity

\[
 \sum_wH_w=3|\mathcal H_A|.                            \tag{0.2}
\]

The proposed global constant inequality

\[
 \sum_wH_w\stackrel?\ll
 k\sum_we_w+\sum_wM_w^2                               \tag{0.3}
\]

is false.  There is an infinite family of genuine integer Euclidean
distance-Sidon sets for which

\[
 \boxed{
 {\sum_wH_w\over k\sum_we_w+\sum_wM_w^2}
 =\Omega(k).}                                         \tag{0.4}
\]

On the same family, every individual active direction satisfies

\[
 ke_w+M_w^2=O(k^2),                                   \tag{0.5}
\]

while \(|\mathcal H_A|=\Omega(k^4)\).  Thus high centroid mass does
**not** force an active short primitive direction whose local
\(ke_w+M_w^2\) budget pays for it.  The literal short-direction inverse
theorem is false both pointwise and after summation.

The construction uses a balanced, nearly isotropic integer transform of
the modular parabola.  Unlike a determinant-one shear, it has no forced
short image direction.  A CRT choice makes every active transformed
direction primitive, while a separate polynomial-avoidance step makes
all Euclidean distances distinct.

There is an important qualification.  The CRT construction has

\[
 m\le\exp(O(k^2)),                                     \tag{0.6}
\]

so the loss in (0.4) is at least \(\Omega(\sqrt{\log m})\), but is still
\(m^{o(1)}\).  Therefore this is a decisive no-go for an absolute-constant
global charge, not a counterexample to the ambient theorem.  Any viable
directional theorem must explicitly allow an unbounded divisor/sieve
loss, at least polylogarithmic on this family.

## 1. The balanced transform

For an integer parameter \(t\), define

\[
 L_t=
 \begin{pmatrix}
  t&-1\\
  1&t+1
 \end{pmatrix},
 \qquad
 \det L_t=t^2+t+1.                                    \tag{1.1}
\]

This is asymptotically a scalar matrix, rather than a shear.  For a
vector \(q=(x,y)\),

\[
 L_tq=(tx-y,\;x+(t+1)y),                               \tag{1.2}
\]

and its squared norm is

\[
 |L_tq|^2
 =t^2(x^2+y^2)+2ty^2+(x^2+2xy+2y^2).                 \tag{1.3}
\]

The three coefficients in (1.3) determine \(q\) up to sign.  Indeed,
equality for \(q=(x,y)\) and \(q'=(x',y')\) first gives

\[
 x^2+y^2=x'^2+y'^2,
 \qquad y^2=y'^2,                                     \tag{1.4}
\]

and then the constant coefficient gives \(xy=x'y'\).  Hence
\(q'=\pm q\).

Consequently, for any finite integer vector-Sidon set, equality of the
post-transform squared lengths of two distinct unordered edges is a
nonzero polynomial of degree at most two in \(t\).  Any arithmetic
progression of candidate parameters contains only finitely many bad
values.

## 2. Simultaneous primitivity by CRT

Let \(P_p\) be the least-residue modular parabola and let
\(\mathcal W_p\) be its active primitive directions.  Write
\(w=(a,b)\in\mathcal W_p\), so \(|a|,|b|\le p\), and define

\[
 Q(w)=a^2+ab+b^2.                                     \tag{2.1}
\]

If a prime \(\ell\) divides both coordinates of \(L_tw\), then two
independent facts hold.

First, \(w\not\equiv0\pmod\ell\), since it is primitive, so \(L_t\) has
a nontrivial kernel modulo \(\ell\).  Therefore

\[
 \ell\mid t^2+t+1.                                    \tag{2.2}
\]

Second, if \(L_tw=(X,Y)\), then

\[
 aY-bX=a^2+ab+b^2=Q(w),                               \tag{2.3}
\]

so

\[
 \ell\mid Q(w).                                       \tag{2.4}
\]

Let \(\mathscr P_p\) be the finite set of primes dividing at least one
\(Q(w)\), \(w\in\mathcal W_p\).  For each
\(\ell\in\mathscr P_p\), choose a residue \(t_\ell\pmod\ell\) for which

\[
 t_\ell^2+t_\ell+1\not\equiv0\pmod\ell.               \tag{2.5}
\]

Such a residue exists because the quadratic has at most two roots; for
\(\ell=2\) it has none.  Put

\[
 R_p=\prod_{\ell\in\mathscr P_p}\ell.
\]

The Chinese remainder theorem supplies \(t_0\pmod{R_p}\) satisfying all
conditions (2.5).  For every

\[
 t=t_0+nR_p,                                          \tag{2.6}
\]

equations (2.2)--(2.5) show that

\[
 \boxed{\gcd((L_tw)_1,(L_tw)_2)=1
        \quad\text{for every }w\in\mathcal W_p.}      \tag{2.7}
\]

There are \(O(p^4)\) unordered pairs of endpoint edges.  By (1.3), each
forbids at most two values of \(n\) in (2.6).  Choose a nonnegative
\(n=O(p^4)\) outside all forbidden values and large enough that \(t\ge2\).
Then

\[
 A_p=L_tP_p                                             \tag{2.8}
\]

is genuinely Euclidean distance-Sidon, every transformed active direction
is primitive, and all exact centroid records are preserved.

Every prime in \(\mathscr P_p\) is at most \(3p^2\).  The elementary
Chebyshev bound for the primorial gives

\[
 R_p\le\prod_{\ell\le3p^2}\ell=\exp(O(p^2)).          \tag{2.9}
\]

Equations (2.6), (2.8), and the coordinate range of \(P_p\) give

\[
 m\le\exp(O(p^2)),                                     \tag{2.10}
\]

proving (0.6).

## 3. The complete directional budget is only cubic

Put \(s=\|w\|_\infty\).  From (1.2), if \(|a|=s\), then

\[
 |ta-b|\ge(t-1)s,

\]

while if \(|b|=s\), then

\[
 |a+(t+1)b|\ge ts.
\]

Together with the primitivity in (2.7) and the bound \(m\le(t+2)p\),
this gives

\[
 M_{L_tw}\le{4p\over s}.                              \tag{3.1}
\]

There are at most \(4s\) primitive unoriented directions of sup-norm
\(s\).  Hence

\[
\begin{aligned}
 \sum_{u\in\mathcal W(A_p)}M_u^2
 &\le16p^2\sum_{s=1}^p{4s\over s^2}\\
 &\le64p^2H_p
 =O(p^2\log p).                                       \tag{3.2}
\end{aligned}
\]

The invertible linear map preserves direction occupancies, and

\[
 \sum_ue_u=\binom p2.
\]

Therefore

\[
 p\sum_ue_u+\sum_uM_u^2=O(p^3).                       \tag{3.3}
\]

Also \(e_u\le p\) and (3.1) gives \(M_u\le4p\), proving the individual
bound (0.5).

On the other hand, the exact integer triple sums of \(P_p\) occupy fewer
than \(9p^2\) cells, so

\[
 |\mathcal H_{P_p}|=\Omega(p^4).                       \tag{3.4}
\]

The invertible transform preserves this hypergraph.  Combining (0.2),
(3.3), and (3.4) proves (0.4).

Finally (2.10) gives

\[
 p=\Omega(\sqrt{\log m})                               \tag{3.5}
\]

up to absolute constants, so even an \(o(\sqrt{\log m})\) loss cannot
repair (0.3) on this construction.  An \(m^{o(1)}\) loss still can.

## 4. Explicit genuine certificates

The CRT is used only for the asymptotic existence proof.  Small balanced
parameters already exhibit the global failure.  The following sets are
all genuine Euclidean distance-Sidon sets, and every transformed active
direction is primitive.

\[
\begin{array}{c|r|r|r|r}
p&t&m&|\mathcal H_A|&
 \displaystyle{\sum_wH_w\over
 p\sum_we_w+\sum_wM_w^2}\\ \hline
23&20&439&8652&2.832829\\
43&69&2897&126852&7.045972\\
59&99&5741&496968&11.241572
\end{array}                                           \tag{4.1}
\]

For \(p=43,t=69\), the exact directional mass is

\[
 \sum_wH_w=380556,
\]

more than seven times the proposed complete global budget.  In contrast,
the determinant-one shear \(t=28\) had a short fixed horizontal direction
which made the same ratio \(0.106997\ldots\).  The balanced transform
shows that this short compensator was a feature of the chosen
Euclideanization, not a consequence of high centroid energy.

## 5. Exact remaining scope

The following statements are now false:

* one active direction has \(ke_w+M_w^2\) comparable to the centroid
  hypergraph mass;
* the sum of all active-direction budgets controls the mass with an
  absolute constant;
* the global estimate can be proved by a constant-loss midpoint or
  constituent-direction charge.

The ambient target still permits

\[
 \sum_wH_w\le m^{o(1)}
 \left(k\sum_we_w+\sum_wM_w^2\right).                 \tag{5.1}
\]

The construction proves that the \(m^{o(1)}\) factor in such a statement
is essential and must absorb simultaneous-primitivity sieve losses.
Whether (5.1), with an adequate divisor-type loss, holds remains open.

## 6. Verification

Run

    python3 phase2/loop/erdos1208/verify_global_directional_short_compensator_no_go.py

The verifier checks the symbolic distance-separation coefficients in
(1.3), genuine Euclidean distance-Sidonicity, the determinant and
Eisenstein-norm divisibility in (2.2)--(2.4), simultaneous primitivity of
all transformed active directions, exact centroid hyperedge mass, and all
three ratios in (4.1).
