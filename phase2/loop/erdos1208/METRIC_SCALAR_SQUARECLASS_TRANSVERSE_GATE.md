# Metric scalar charge: squareclass resonance versus transverse collisions

## 1. Outcome

Let `A subset Z^2` be distance-Sidon, `|A|=k`, with both coordinate
widths at most `m`.  Put

\[
 \Sigma=A\mathbin\oplus A,\quad N=|\Sigma|=\binom{k}{2},
 \quad h=|H_q|,
\]

and consider the surviving metric scalar charge

\[
 \Phi_q(s,t)=\delta(s)+18\delta(t),
 \qquad(s,t)\in H_q\times\Sigma.                \tag{1.1}
\]

This note proves that all collisions staying in one source squared-distance
squareclass and one target squareclass have energy

\[
 \boxed{\mathcal M_q^{\rm res}\le m^{o(1)}hN.}              \tag{1.2}
\]

In particular this includes every collision in which the two source edges
are parallel and the two target edges are parallel.  After the known
repeated-edge cleanup, any polynomial failure of the scalar gate must
therefore occur among four-distinct-edge collisions which change
squareclass, and hence are directionally transverse, on at least one side.
This is a quantitative branch, not the full scalar estimate.

## 2. Exact endpoint equations in the four-edge core

Take distinct colliding records `(s,t)` and `(s',t')`.  Canonically order
the endpoints and retain the clean target decorations:

\[
\begin{aligned}
 s&=c+d,&s+q&=e+f,&t&=x+y,\\
 s'&=c'+d',&s'+q&=e'+f',&t'&=x'+y'.
\end{aligned}                                                \tag{2.1}
\]

In the four-distinct-edge core the four unordered edges
`{c,d},{c',d'},{x,y},{x',y'}` are different, although their endpoints may
overlap.  Put

\[
\begin{gathered}
 u=c-d,\quad u'=c'-d',\quad v=x-y,\quad v'=x'-y',\\
 \alpha=c-c',\quad\beta=d-d',\quad
 \eta=e-e',\quad\theta=f-f',\quad
 \gamma=x-x',\quad\zeta=y-y'.
\end{gathered}                                                \tag{2.2}
\]

The six cross vectors in the second line lie in the complete difference set
`A-A` and retain their endpoint realizations.  Subtracting the clean
equations and factoring the difference of squared norms gives exactly

\[
 \boxed{
 \alpha+\beta=\eta+\theta,\qquad
 (\alpha-\beta)\mathbin\cdot(u+u')
 +18(\gamma-\zeta)\mathbin\cdot(v+v')=0.}                  \tag{2.3}
\]

The second equation is equivalent to

\[
 |u|^2+18|v|^2=|u'|^2+18|v'|^2.                            \tag{2.4}
\]

Thus a scalar collision is an equal-radius pair after the integral lift
`(u,v)->(u,3v,3v) in Z^6`.  Equation (2.3), rather than the radius equality
alone, is the endpoint-rich inverse datum: it keeps both clean translates
and all complete-difference realizations.

## 3. Uniform binary representation bound

For a positive integer `r`, let `sf(r)` be its squarefree kernel, so
`r=sf(r) ell(r)^2` with `ell(r)` positive integral.

**Lemma 3.1.**  Uniformly for positive integers `a,b,n`,

\[
 \#\{(X,Y)\in\mathbb Z^2:aX^2+bY^2=n\}
 \le6\tau(an).                                               \tag{3.1}
\]

**Proof.**  Multiply the equation by `a` and map a solution to

\[
 z=aX+Y\sqrt{-ab}\in K=\mathbb Q(\sqrt{-ab}).               \tag{3.2}
\]

This is an algebraic integer of norm `an`; hence `(z)` is an integral
principal ideal of norm `an`.  A quadratic field has at most `tau(an)`
integral ideals of that norm: a split prime of exponent `j` gives `j+1`
local choices, while an inert or ramified prime gives at most one.  Two
generators of one principal ideal differ by a unit, and an imaginary
quadratic field has at most six units.  The map `(X,Y)->z` is injective.
This also covers nonsquarefree `ab`, since `sqrt(-ab)` remains an algebraic
integer in the same field.  \(\square\)

Here `n<=38m^2` and `a<=2m^2`, so `an<=76m^4`.  The divisor bound makes
(3.1) `m^{o(1)}` uniformly in both squareclasses.

## 4. Resonant energy theorem

For squarefree `a,b`, let

\[
 \mathcal C_{a,b}=\{(s,t)\in H_q\times\Sigma:
 \operatorname{sf}(\delta(s))=a,
 \operatorname{sf}(\delta(t))=b\},                          \tag{4.1}
\]

and let `r_(a,b)(n)` count records in this cell with charge `n`.  Define

\[
 \mathcal M_q^{\rm res}=\sum_{a,b,n}r_{a,b}(n)^2.           \tag{4.2}
\]

It counts ordered colliding record pairs whose two source labels have the
same squarefree kernel and whose two target labels have the same squarefree
kernel; diagonals are included.

**Theorem 4.1.**  One has (1.2).

**Proof.**  Inside a cell write `delta(s)=aX^2` and
`delta(t)=bY^2`.  Distance-Sidonicity supplies at most one edge for each
distance label, so `r_(a,b)(n)` is at most the number of positive solutions
of

\[
 aX^2+18bY^2=n.                                              \tag{4.3}
\]

Lemma 3.1 makes its maximum `m^{o(1)}`.  Therefore

\[
 \sum_n r_{a,b}(n)^2
 \le m^{o(1)}\sum_n r_{a,b}(n)
 =m^{o(1)}|\mathcal C_{a,b}|.                               \tag{4.4}
\]

Sum over the disjoint cells, whose total size is `hN`.  \(\square\)

Parallel integral displacements are multiples of one primitive vector, so
their squared norms have the same squarefree kernel.  Hence every collision
with parallel source edges and parallel target edges lies in (4.2).  This
explains rigorously why the resonant two-arm subsystem that destroys the
Gaussian vector charge is harmless here.

## 5. Transverse reduction and low-diversity branch

Let `T_q^(4)` count ordered four-distinct-edge collisions for which

\[
 \operatorname{sf}(\delta(s))\ne\operatorname{sf}(\delta(s'))
 \quad\hbox{or}\quad
 \operatorname{sf}(\delta(t))\ne\operatorname{sf}(\delta(t')). \tag{5.1}
\]

Call these squareclass-transverse.  Proposition 2.1 of
`METRIC_SCALAR_PAIR_SUM_CHARGE.md` bounds all off-diagonal three-edge
collisions by `4h^2`.  Theorem 4.1 gives

\[
 \boxed{\mathcal M_{q,18}
 \le m^{o(1)}hN+4h^2+T_q^{(4)}.}                            \tag{5.2}
\]

Thus the precise remaining local target is

\[
 T_q^{(4)}\le m^{o(1)}N(h+k).                               \tag{5.3}
\]

Every row counted by `T_q^(4)` obeys the full endpoint system (2.3), has
four distinct edge labels, and has a nonparallel source pair or a
nonparallel target pair.  The converse can fail because nonparallel vectors
may still belong to one norm squareclass.

There is also a complete low-diversity branch.  Put

\[
 K_q=|\operatorname{sf}(\delta(H_q))|,
 \qquad K=|\operatorname{sf}(\delta(\Sigma))|.              \tag{5.4}
\]

Cauchy--Schwarz across the at most `K_qK` cells at each charge value and
Theorem 4.1 yield

\[
 \boxed{\mathcal M_{q,18}\le K_qK\,m^{o(1)}hN.}             \tag{5.5}
\]

Hence the full scalar estimate holds whenever `K_qK=m^{o(1)}`.  This
contains the fixed pair-of-directions and collinear branches.

There is an important range barrier to using (5.5) globally.  A squareclass
`a` contains at most `floor(sqrt(2)m/sqrt(a))` possible labels below
`2m^2`.  If the `K` occupied squarefree kernels are listed increasingly,
the `j`-th is at least `j`, and hence

\[
 N\le\sqrt2m\sum_{j=1}^Kj^{-1/2}
 \le2\sqrt2m\sqrt K,
 \qquad
 \boxed{K\ge {N^2\over8m^2}.}                              \tag{5.6}
\]

At the cube-root scale `k=m^(2/3+o(1))`, this already forces
`K>=m^(2/3-o(1))`.  Thus (5.5) is a real low-diversity theorem but cannot,
by itself, handle the critical global distance set.  The unconditional
resonant deletion (4.3), which loses no factor `K`, is the useful part for
the main problem.

## 6. Exact profiles and restart point

The verifier reports `(mass, total energy, resonant energy, transverse
energy, resonant four-edge, transverse four-edge, maximum cell load)`:

\[
\begin{array}{c|r|r|r|r|r|r|r}
\text{family}&hN&\mathcal M&\mathcal M^{\rm res}&
 \mathcal M-\mathcal M^{\rm res}&T_{\rm res}^{(4)}&T_q^{(4)}&
 \max r_{a,b}\\ \hline
\text{closure }30&6090&6342&6090&252&0&252&1\\
\text{closure }40&17940&20592&17940&2652&0&2648&1\\
\text{closure }80&199080&221584&199080&22504&0&22474&1\\
\text{closure }120&906780&1023788&906780&117008&0&116938&1\\
\text{Costas }22&7854&8382&7854&528&0&514&1\\
\text{parabola image }43&154413&157133&154421&2712&4&2704&2
\end{array}                                                 \tag{6.1}
\]

The closure resonant energy is exactly diagonal: every off-diagonal closure
collision changes squareclass on at least one side.  The theorem removes
the old one-dimensional resonance but not the dominant finite core.

On the `s=50` two-arm construction, restrict to its certified internal-`Y`
clean subfibre and internal-`X` target edges.  All source labels have
squareclass `2`, all target labels squareclass `1`, and

\[
 (h_Y,N_X,h_YN_X,|\operatorname{im}\Phi|,
 \mathcal M^{\rm restricted},\max\Phi^{-1})
 =(114,1225,139650,139345,140262,3).                         \tag{6.2}
\]

The same subsystem has Gaussian vector energy `869608`; the positive binary
quadratic form reduces it to almost diagonal scale.  The live restart target
is (5.3): turn many transverse equal radii in the six-dimensional lift into
two equal two-dimensional endpoint norms, contradicting distance-Sidonicity.
