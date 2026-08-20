# Global directional pair energy: the projective-dilation barrier

## 1. Verdict

Let \(A\subset[0,m]^2\cap\mathbb Z^2\) be distance-Sidon, put

\[
 \mathscr D=(A-A)\setminus\{0\},\qquad N=k(k-1),
\]

and let \(\mathcal W(A)\) be the primitive unoriented directions of its
endpoint edges.  For \(w\in\mathcal W(A)\), define

\[
 B_w(r)=|\{q\in\mathscr D:\det(w,q)=r\}|,
 \qquad
 P_w=\sum_{r\ne0}\binom{B_w(r)}2,                   \tag{1.1}
\]

and \(\mathcal P(A)=\sum_wP_w\).

The proposed global packing estimate

\[
 \boxed{\mathcal P(A)
 \le m^{o(1)}(k^3+m^2)}                             \tag{1.2}
\]

survives all genuine distance-Sidon stresses in the repository.  It is
not proved.  The audit gives an exact description of what remains and
rules out the main easier substitutes.

1. \(\mathcal P\) is exactly a **projective difference-closure count**:

   \[
    \boxed{
    \mathcal P(A)=
    \#\{\{q,q'\}\subset\mathscr D:
      \operatorname{prim}(q-q')\in\mathcal W(A),
      \det(q-q',q)\ne0\}.}                          \tag{1.3}
   \]

   Thus it counts pairs of endpoint differences whose connecting vector
   is a rational dilation of some endpoint edge.  It does not retain the
   content of that edge.

2. The sharp universal estimate is only

   \[
    \mathcal P(A)\le\binom N2.                       \tag{1.4}
   \]

   Hence (1.2) is proved in the high-height range \(m\ge N\asymp k^2\),
   but (1.4) loses a full power at critical height \(m\asymp k^{3/2}\).

3. Endpoint realization and vector-Sidonicity cannot prove (1.2).  The
   layered \(\mathbb F_{p^2}\)-parabola construction from
   `CLOSED_FIBRE_Q_HEIGHT_LAYERED_BARRIER.md` has

   \[
    k=p^2,\quad m=O(p^3)=O(k^{3/2}),\quad
    P_{(1,0)}={1\over3}p^7-{1\over2}p^6+O(p^5)
             =\Omega(k^{7/2}).                      \tag{1.5}
   \]

   It is an actual common-endpoint integer vector-Sidon set, but it is
   not Euclidean distance-Sidon.  The explicit transform which repairs
   its radial collisions preserves (1.5) while raising the height to
   \(O(k^2)\), where \(m^2\) pays.

4. Even for genuine distance-Sidon sets, \(P_w\) can exceed the selected
   closed-fibre quantity in one direction by a factor \(\Theta(k)\).
   There are polynomial-height examples with

   \[
    P_{(1,0)}=2\binom k3=\Theta(k^3),qquad
    Q_{(1,0)}=k(k-1)-4=\Theta(k^2).                 \tag{1.6}
   \]

Consequently (1.2) is a genuine strengthening, not a harmless rewrite of
the closed-fibre \(Q\) gate.  Its exact missing input is a global theorem
saying that Euclidean radial uniqueness prevents many projective
dilations from coexisting at critical height.  If that theorem is false,
one must return to the content-aware closed functional rather than use
flat pair energy.

## 2. Exact projective identity

For distinct \(q,q'\in\mathscr D\), there is exactly one primitive
unoriented direction

\[
 w=\operatorname{prim}(q-q').                       \tag{2.1}
\]

The pair lies in one common nonzero determinant fibre for \(w\) if and
only if

\[
 \det(w,q)=\det(w,q')\ne0.                          \tag{2.2}
\]

The equality is automatic from (2.1); nonzero simply removes pairs on
the radial line \(\mathbb Zw\).  Summing unordered pairs inside every
fibre proves (1.3).  Since every pair has only one direction, (1.4)
follows immediately.

In endpoint coordinates, write

\[
 q=b-a,qquad q'=d-c.
\]

Then

\[
 q-q'=b+c-a-d=h w                                  \tag{2.3}
\]

for some nonzero integer \(h\).  Activity of \(w\) supplies an endpoint
edge \(f-e=gw\) for some positive integer \(g\), so every record obeys

\[
 g(b+c-a-d)=h(f-e).                                 \tag{2.4}
\]

The exact closed case is \(|h|=g\), using the appropriate orientation of
the endpoint edge.  Flat \(\mathcal P\) admits every rational dilation
\(h/g\).  Equation (2.4), rather than an ordinary
Schur or centroid relation, is the algebraic survivor.

## 3. The summed directional energy identity

Let

\[
 n_{w,t}=|\{a\in A:\det(w,a)=t\}|.
\]

Then

\[
 B_w(r)=\sum_t n_{w,t}n_{w,t+r}.                    \tag{3.1}
\]

Thus \(2P_w\) is the nonzero autocorrelation energy

\[
 H_w:=\sum_{r\ne0}\bigl(B_w(r)^2-B_w(r)\bigr),
 \qquad \sum_wH_w=2\mathcal P(A).                  \tag{3.2}
\]

This is the stronger summed directional gate requested in the audit.  It
has no hidden endpoint multiplicity: distance-Sidonicity makes every
directed difference recover its ordered endpoints.

If

\[
 e_w=\sum_t\binom{n_{w,t}}2
\]

is the number of endpoint edges parallel to \(w\), Young's convolution
inequality gives the rigorous pointwise estimate

\[
 \sum_rB_w(r)^2
 \le \left(\sum_tn_{w,t}\right)^2
      \left(\sum_tn_{w,t}^2\right)
 =k^2(k+2e_w).                                      \tag{3.3}
\]

This cannot be summed at the target scale.  The \(k^3\) term can recur
over many active directions, while the layered construction makes the
\(k^2e_w\) term sharp to order.  The identities

\[
 \sum_we_w={N\over2},\qquad |\mathcal W(A)|\le {N\over2} \tag{3.4}
\]

therefore do not close (1.2).  Pointwise projection energy is not the
missing global argument.

## 4. Critical common-endpoint obstruction

For completeness, take a nonsquare \(d\pmod p\), write
\(t=a+b\omega\in\mathbb F_{p^2}\), and encode

\[
 (t,t^2)=(a+b\omega,c+e\omega)
 \longmapsto (a+2pc+4p^2e,b).                       \tag{4.1}
\]

The radix \(2p\) separates all three signed digit differences, and the
field parabola is vector-Sidon, so (4.1) is a common-endpoint integer
vector-Sidon set.  It has \(p\) horizontal layers of \(p\) points.  For
\(w=(1,0)\),

\[
 B_w(r)=(p-|r|)p^2\qquad(0<|r|<p).                 \tag{4.2}
\]

Consequently

\[
\begin{aligned}
 P_w
 &=2\sum_{h=1}^{p-1}\binom{hp^2}{2}\\
 &={1\over3}p^7-{1\over2}p^6+O(p^5),               \tag{4.3}
\end{aligned}
\]

proving (1.5).  The reflected vectors \((u,1)\) and \((u,-1)\) occur as
different endpoint edges, so Euclidean radial uniqueness fails.

The dominance transform

\[
 (x,y)\mapsto(3px+y,y)                              \tag{4.4}
\]

makes the set genuinely distance-Sidon.  Horizontal projection
multiplicities, hence (4.2)--(4.3), are unchanged.  Its height is
\(O(p^4)=O(k^2)\), and so it does not refute (1.2).  This is the exact
height/radial boundary: a critical-height Euclidean realization of this
layer pattern would be a genuine counterexample by \(k^{1/2}\).

## 5. A genuine one-direction loss

The gap between flat pair energy and the content-aware functional already
occurs in genuine distance-Sidon sets.  Prescribe the projection
multiset

\[
 y(A)=\{0,0,1,2,\ldots,k-2\}.                       \tag{5.1}
\]

Choose the \(x\)-coordinates greedily and keep them distinct.  When
adding the \(j\)-th point, there are only \(O(j^3)\) forbidden integer
values:

* equality of one new distance with one of the \(O(j^2)\) old distances
  gives at most two roots for each old endpoint;
* equality of two new distances gives one root because the old
  \(x\)-coordinates are distinct; and
* the \(j\) used coordinates are forbidden.

Therefore a choice exists with all coordinates in an \(O(k^3)\) box.
The resulting set is genuinely distance-Sidon and has exactly one
horizontal endpoint edge, so \(e_{(1,0)}=1\).  From (5.1),

\[
 B_{(1,0)}(r)=k-|r|\qquad(0<|r|\le k-2).            \tag{5.2}
\]

Equations (1.6) follow:

\[
 P_{(1,0)}=2\sum_{s=2}^{k-1}\binom s2=2\binom k3,
\]

while the unique selected positive gap gives

\[
 Q_{(1,0)}=2\left(1+\sum_{s=3}^{k-1}s\right)
             =k(k-1)-4.                             \tag{5.3}
\]

Hence replacing selected contents by the pair cap can lose a full factor
of \(k\) even after all endpoint and Euclidean requirements are imposed.
The large ambient height pays for this example globally, but no local
comparison \(P_w\le m^{o(1)}Q_w\) is possible.

## 6. Genuine summed stresses

The following exact profiles use the full sum over active directions:

\[
\begin{array}{c|r|r|r|r|c}
\text{family}&k&m&\mathcal P&\sum_D\mathcal Q_D&
 \mathcal P/(k^3+m^2)\\ \hline
\text{prescribed-20}&20&115&26748&29002&1.260\\
\text{prescribed-40}&40&362&345908&401212&1.773\\
\text{prescribed-60}&60&711&1576232&1824114&2.185\\
\text{stored closure-60}&60&447&787498&896292&1.894\\
\text{finite-field lift }p=43&43&1790&847864&988328&0.258
\end{array}                                          \tag{6.1}
\]

The first three rows are the greedy prescribed-projection family of
Section 5; the fourth is the independent critical closure witness.  The
ratios grow slowly and are compatible with logarithmic loss, not a fixed
power.  The finite-field lift again lives at the \(m^2\) scale.  No
genuine polynomial-height counterexample to (1.2) was found.

## 7. Exact remaining gate

The proof problem can now be stated without fibre notation:

> Let \(D=A-A\) for a Euclidean distance-Sidon set in the \(m\)-box.
> Bound the number of unordered pairs \(q,q'\in D\) for which the slope
> of \(q-q'\) is also a radial slope occupied by \(D\), excluding the
> common radial line, by \(m^{o(1)}(k^3+m^2)\).

The obstruction (4.1) satisfies every part except Euclidean radial
uniqueness and exceeds the target by \(k^{1/2}\) at critical height.
Thus a proof must use radial norm labels **globally across directions**;
projection moments, endpoint cocycles, vector Sidonicity, and pointwise
height caps have all been exhausted.

If this global radial packing statement fails, (2.4) shows why the flat
gate was too strong: it counts arbitrary rational dilation ratios
\(h/g\).  The correct fallback is the original content-aware closed
functional, which retains the actual selected contents \(g\).

## 8. Verification

Run

```text
python3 phase2/loop/erdos1208/verify_global_directional_pair_energy_projective_dilation.py
```

The verifier checks the exact projective identity, the summed directional
energy, Young's pointwise bound, the layered \(\mathbb F_{p^2}\)
obstruction and its Euclidean repair, the greedy finite-avoidance family,
the exact factor-\(k\) one-direction loss, and all finite rows in (6.1).
