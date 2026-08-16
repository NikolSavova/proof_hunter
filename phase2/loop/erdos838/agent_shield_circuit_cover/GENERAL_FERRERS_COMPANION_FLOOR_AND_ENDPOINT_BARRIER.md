# General Ferrers companion floors and the endpoint-module barrier

**Date:** 2026-08-15. All logarithms are base two. This abstracts the
two-rectangle synchronization in
`PASCAL_FERRERS_MINIMAX_ZIPPER_GATE.md` and audits the physical
endpoint modules extracted in
`COHERENT_RAMP_ENDPOINT_MODULE_LOCALIZATION.md`. It uses no cyclic
omitted-gap factorization.

## Verdict

There is an exact robust companion-floor theorem. Its minimal datum is
the **lower convex envelope of the endpoint tail in the physical wall
order**; log-convexity of the endpoint atoms is neither needed nor
sufficient.

For a normalized endpoint distribution \(w\) on \(r\) ordered rows, put

\[
 W(q)=\sum_{i\ge q}w_i\quad(0\le q\le r),
 \qquad \underline W=\text{the greatest convex minorant of }W,       \tag{1}
\]

where \(W(r)=0\). For a rectangle with \(m\) columns define

\[
\begin{aligned}
 f_{m,w}(x)&=(1+x)(1+m\underline W(x)),\\
 F_m(w)&=\min_{0\le x\le r} f_{m,w}(x),\\
 G_m(w)&=\max_{0\le a\le mr} f_{m,w}(a/m).
                                                                    \tag{2}
\end{aligned}
\]

The first quantity is a direction-uniform companion floor. The second
is a peak that every complete Young-lattice sweep must encounter.

Suppose two incomparable physical inversion rectangles \(X,Y\) occur in
one endpoint transform and every chamber \(Q\) satisfies

\[
 \frac{C(Q)U(Q)}{H}\ge
       \Delta\,\mathcal I_X(Q)\mathcal I_Y(Q),                     \tag{3}
\]

where each \(\mathcal I\) is the uniform-row times weighted-column
Ferrers factor defined below. If the sweep is complete on \(Y\), then

\[
 \boxed{\displaystyle
 \max_Q\frac{C(Q)U(Q)}H\ge
       \Delta F_{m_X}(w_X)G_{m_Y}(w_Y).}                           \tag{4}
\]

In particular, the following two elementary hypotheses suffice:

\[
 W_X(q)\ge
 \left(\frac1{L(1+q)}-\frac1{m_X}\right)_+
 \quad(0\le q\le r_X),                                           \tag{5}
\]

and, for some integer \(q_0\ge2\),

\[
                         W_Y(q_0)\ge\eta.                         \tag{6}
\]

They give the completely explicit bound

\[
 \boxed{\displaystyle
 \max_Q\frac{C(Q)U(Q)}H\ge
       \frac{\Delta\,m_Xm_Yq_0\eta}{8L}.}                         \tag{7}
\]

Thus (7) exceeds \(N^{\log_2 3+\varepsilon}\) whenever

\[
 \log_N\frac{\Delta m_Xm_Yq_0\eta}{L}
       \ge\log_2 3+\varepsilon+o(1).                              \tag{8}
\]

This exactly contains the Pascal proof: one middle rectangle supplies
the harmonic companion floor \(m_X2^{-o(t)}\), while the other supplies
the Pascal convex-tail peak.

However, the endpoint localization currently available for the
coherent ramp does **not** imply (5). It selects one fixed physical pair
\(e=(a,b)\). All records in that rooted module therefore have the same
extreme row in an external inversion rectangle. Its endpoint
distribution can be a delta atom, for which

\[
 \underline W(x)=(1-x)_+,
 \qquad F_m(w)=2.                                                  \tag{9}
\]

So the whole factor \(m\) can disappear. Even imposing exact
log-convexity does not repair this: the geometric distribution
\(w_i\propto2^{-i}\), realized by an explicit rational cap chain, has

\[
 F_m(w)=O(\log m)                                                  \tag{10}
\]

when \(r=m\). Therefore the localized physical endpoint modules do not
yet meet the robust theorem's hypotheses. A genuine next lemma must
prove a harmonic lower tail in the **actual cross-wall order**, or
charge its failure to an ambient shield/face bank.

## 1. Exact Ferrers inequality

Let a Ferrers state have column heights
\(h_1,\ldots,h_m\in\{0,\ldots,r\}\). No monotonicity convention is
needed in the calculation. Write

\[
 \bar h=\frac1m\sum_{j=1}^m h_j,
 \qquad
 \overline W=\frac1m\sum_{j=1}^m W(h_j),                          \tag{11}
\]

and define its inversion factor by

\[
                   \mathcal I_{m,w}(h)
                  =(1+\bar h)(1+m\overline W).                    \tag{12}
\]

Because \(\underline W\le W\) and \(\underline W\) is convex, Jensen's
inequality gives

\[
 \overline W\ge\frac1m\sum_j\underline W(h_j)
             \ge\underline W(\bar h).
\]

Consequently

\[
                 \boxed{\mathcal I_{m,w}(h)\ge f_{m,w}(\bar h)
                    \ge F_m(w).}                                 \tag{13}
\]

During a complete Young-lattice sweep one cell is crossed at each step,
so the total area takes every value \(a=0,1,\ldots,mr\). At area \(a\),
\(\bar h=a/m\). Equation (13) therefore also proves

\[
                     \max_{h\text{ on the sweep}}
                     \mathcal I_{m,w}(h)\ge G_m(w).               \tag{14}
\]

Multiplying the all-chamber floor (13) for \(X\) by the forced peak
(14) for \(Y\) proves (4). Notice that arbitrary leakage/interleaving in
the \(X\)-rectangle is harmless: its state may change adversarially at
the chamber where \(Y\) peaks, but it cannot fall below \(F_{m_X}(w_X)\).

This is the exact content needed from “two incomparable rectangles.” A
claim that only bounds the two rectangles in different chambers is not
enough; the pointwise factorization (3) is essential.

## 2. Two checkable sufficient conditions

For (5), set

\[
 \phi(x)=\left(\frac1{L(1+x)}-\frac1{m_X}\right)_+.               \tag{15}
\]

The function \(\phi\) is convex. If (5) holds at every integer, then
\(\phi\) is a convex minorant of the endpoint-tail data, so
\(\underline W_X\ge\phi\). When \(\phi(x)>0\),

\[
 (1+x)(1+m_X\phi(x))=m_X/L;
\]

when \(\phi(x)=0\), one has \(1+x\ge m_X/L\). Hence

\[
                         F_{m_X}(w_X)\ge m_X/L.                   \tag{16}
\]

For (6), monotonicity of the tail implies that

\[
 \psi(x)=\eta(1-x/q_0)_+
\]

is a convex minorant of \(W_Y\). At the integer
\(x=\lfloor q_0/2\rfloor\),

\[
 x\psi(x)\ge q_0\eta/8.
\]

The sweep contains a state of mean height exactly this integer, and so

\[
                         G_{m_Y}(w_Y)\ge m_Yq_0\eta/8.            \tag{17}
\]

Equations (16)--(17) prove (7). The constants are deliberately uniform;
using the continuous maximum improves \(1/8\) to \(1/4\).

Neither ordinary log-convexity nor log-concavity of the atoms implies
(5). Condition (5) is an anti-concentration statement tied to the
physical wall order, not merely to the multiset of endpoint degrees.

## 3. Audit of the coherent-ramp endpoint module

The exact identity in `COHERENT_RAMP_ENDPOINT_MODULE_LOCALIZATION.md` is

\[
                         \bar H=\sum_e C_eU_e.                    \tag{18}
\]

Low endpoint surplus localizes a polynomial fraction of both directional
families to one actual pair \(e=(a,b)\). This is a genuine internal
cap-by-cup rectangle, but it has **zero endpoint spread**: every selected
cap and every selected cup has the same left and right physical endpoint.
If a neighboring block crosses the relevant endpoint first, the induced
row distribution is

\[
                         w=(1,0,\ldots,0).                        \tag{19}
\]

Its tail is \(W(0)=1\), \(W(q)=0\) for \(q\ge1\). The lower convex
envelope is the wedge in (9), and

\[
 \min_x(1+x)(1+m(1-x)_+)=2.                                     \tag{20}
\]

Thus (18) and the \(D^{-O(\log q)}\) localization fractions do not imply
even \(m^\varepsilon\) companion growth. Having
\(\Theta(\log N)\) such roles does not help: the obstruction occurs
inside each physical endpoint alphabet, while role count is only
polylogarithmic.

The Pascal module is different in exactly the required way. Its dominant
cap family has a common root but a **variable opposite endpoint**. The
hereditary Pascal recursion supplies the harmonic convex-tail minorant
that is absent from (18).

## 4. Exact stretchable barriers

### 4.1 A dense fixed-pair module with polynomial surplus

Let

\[
 P(t)=\left(\frac{1-t^2}{1+t^2},\frac{2t}{1+t^2}\right),
 \qquad u=(-1,0),\quad v=(1,0).                                  \tag{21}
\]

Choose \(m\) positive rational parameters and \(m\) negative rational
parameters with distinct absolute values. The resulting \(2m+2\) points
lie on the unit circle, are in general position, and every subset is an
ordinary convex face.

The upper family

\[
 \{\{u,v\}\cup S:S\subseteq\{P(t):t>0\}\}
\]

consists of \(2^m\) caps with exact endpoints \(e=(u,v)\). The analogous
lower family consists of \(2^m\) cups with the same exact endpoints, and
all \(4^m\) cap-cup unions are distinct ordinary faces. Hence this one
fixed pair carries more than one quarter of all ordinary faces.

This example also has low endpoint surplus. Put

\[
                         R_m=1+m+\binom m2.
\]

Any cap contains at most two lower-arc internal points, since every
lower-arc triple is a cup. Therefore

\[
 C\le 2^{m+2}R_m,\qquad U\le2^{m+2}R_m,\qquad
 H=2^{2m+2}-1,
\]

and consequently

\[
                         \frac{CU}{H}\le8R_m^2=O(m^4).           \tag{22}
\]

So a polynomial-surplus child may genuinely devote a constant fraction
of all its faces to a single fixed endpoint pair. This is a sharp
stretchable obstruction to deriving (5) from the current localization.
The ambient Boolean face complex pays enormously; the construction is
not claimed to be a global low-\(V\) counterexample.

### 4.2 Log-convex endpoint weights still have a logarithmic floor

There is also an exact one-ended obstruction with nonzero endpoint
spread. Put

\[
                         A_i=(i,-i^2),\qquad0\le i\le n.          \tag{23}
\]

Fix the right root \(A_n\), and take the caps
\(\{A_n\}\cup S\) for nonempty
\(S\subseteq\{A_0,\ldots,A_{n-1}\}\). The number whose left endpoint is
\(A_i\) is

\[
                         d_i=2^{n-1-i}.                           \tag{24}
\]

Thus \(d_i^2=d_{i-1}d_{i+1}\): the endpoint atoms are exactly geometric,
and hence log-convex with equality. After normalization their tails are

\[
                         W(q)=\frac{2^{n-q}-1}{2^n-1}.            \tag{25}
\]

This tail is already convex. With \(m=n\) and
\(q=\lceil\log n\rceil\),

\[
 F_n(w)\le(1+q)(1+nW(q))
        \le\frac73(1+\lceil\log n\rceil)                         \tag{26}
\]

for \(n\ge2\). Hence a perfectly log-convex physical endpoint sequence
can lose \(n/\operatorname{polylog}n\) of the desired companion factor.

This bad order is stretchable, not just an abstract weighting. The
cross walls of the fixed root \(A_n\) occur after the \(n\) selected
endpoint rows and may be left untouched. For a
large rational \(X\) and sufficiently small positive rational
\(\epsilon\), take a second cloud

\[
 B_j=(X+\epsilon j,\ X^2+\epsilon^2j^2),\qquad0\le j<m.          \tag{27}
\]

Under the projection \(x+sy\), the \(A_iB_j\) equality wall is

\[
 s_{ij}=\frac{i-X-\epsilon j}{i^2+X^2+\epsilon^2j^2}.            \tag{28}
\]

For \(X\gg n+m\) and then \(\epsilon>0\) sufficiently small, all walls
in row \(i\) precede all walls in row \(i+1\). The \(A\)-internal walls
are positive, whereas the \(B\)-internal walls equal
\(-1/(\epsilon(j+k))\) and lie far to the left. Thus the whole bad
geometric endpoint order is traversed while both internal orders remain
fixed. All inequalities are strict and open. Avoiding the finitely many
mixed collinearities by an arbitrarily smaller rational perturbation
gives rational general-position realizations for every \(n,m\).

This construction rules out replacing (5) by “Ferrers + log-convex
endpoint degrees.” Again, its large ambient cap/face complex is an
available shield payment; what it kills is the proposed local implication.

## 5. Exact residual

The robust synchronization mechanism is now reduced to one precise
geometric question:

> In a live induction-minimal coherent-ramp child, can the endpoint
> weights of the physical rooted module be ordered by the actual
> neighboring cross walls so that the harmonic minorant (5) fails by
> \(N^{\Omega(1)}\), without the concentrated prefixes themselves
> yielding a decodable cap/face or circuit-shield bank?

The current endpoint-pair localization does not answer this question.
The circle and parabola constructions show that neither low surplus,
one dense endpoint pair, nor log-convex endpoint degrees can answer it
alone. What remains must use minimizer/global-load information or a
new shield charge for concentrated physical prefixes.

## 6. Verification

Run

    python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_general_ferrers_companion_floor_and_endpoint_barrier.py

The verifier uses exact rational arithmetic. It:

1. exhausts small Ferrers states and checks Jensen's inequality, the
   all-state floor, and the complete-sweep peak;
2. checks the harmonic-minorant implication (16), including exact
   convex-envelope evaluation;
3. verifies the delta floor \(F_m=2\) and the logarithmic geometric
   floor;
4. verifies the rational circle fixed-pair module, all its product
   unions, and the polynomial-surplus bound; and
5. verifies a rational instance of the row-major cross-wall realization
   (23)--(28), including general position and separation from all internal
   walls.

Expected output:

    PASS: Ferrers floor/peak theorem and endpoint barriers; states=90, delta_floor=2, geometric_floor=7.317647058824, circle=(10, 201, 201, 1023, 256), row_major=(8, 8, 64)
