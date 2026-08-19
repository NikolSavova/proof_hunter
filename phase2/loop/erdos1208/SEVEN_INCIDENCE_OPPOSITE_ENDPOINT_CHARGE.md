# The opposite-endpoint charge for the adaptive seven-incidence count

## 1. Status

Let `A` be distance-Sidon, put

\[
 D=A-A,\qquad N=|D|,\qquad S=|D+D|,
\]

and retain the adaptive popular set `P=mathcal P_K` and rich fibres
`Q_K(u,s)` from `SUPPORT_ADAPTIVE_RICH_FIBRE_GATE.md`.  This note gives a
new exact reorganization of the off-diagonal count

\[
 \mathcal O_K:=\sum_{r\ne0}Z_K(r)
 =\sum_{u,s}g_K(u,s)(g_K(u,s)-1).                 \tag{1.1}
\]

Every ordered pair inside one rich fibre is charged to an element of the
correct-size universe `D x (D+D)`.  Unlike the earlier endpoint-midpoint
charge, the new charge is **exactly injective inside each individual
fibre**.  Consequently all residual multiplicity is cross-fibre
multiplicity.  The quadratic switching gadget and the dense Sidon-ruler
family that destroyed the midpoint charge do not destroy this one.

This is a sharper sufficient gate, not a proof of its remaining
cross-fibre multiplicity estimate.  Abstract radial transversals still have
polynomial charge load, so the gate continues to detect the load-bearing
complete-difference hypothesis.

## 2. Symmetric form of the seven incidences

Write

\[
 L=I+J.
\]

Fix `(u,s)` and put `w=s-u`.  For `q in Q_K(u,s)`, define

\[
 x_q=u+q,\qquad y_q=w-q,\qquad v_q=w-Lq.          \tag{2.1}
\]

The definition of the rich fibre is exactly

\[
 u,x_q,y_q,v_q\in D,\qquad q\in P.               \tag{2.2}
\]

For an ordered pair `q,q'` in the same fibre, put `r=q'-q`.  Then

\[
 x_{q'}=x_q+r,\qquad y_{q'}=y_q-r,
 \qquad v_{q'}=v_q-Lr.                            \tag{2.3}
\]

Thus (2.2)--(2.3) are precisely the seven `D`-incidences in the definition
of `Z_K(r)`, with both shifts retained in `P`.

## 3. The opposite-endpoint charge

For distinct `q,q'` in `Q_K(u,s)`, set

\[
 \boxed{
 \Xi(u,s,q,q')=(v_q,\ u+x_{q'})
               =(v_q,\ 2u+q').}                 \tag{3.1}
\]

The first coordinate lies in `D`; the second is a sum of the two elements
`u,x_{q'} in D`.  Hence

\[
 \Xi:\Omega_K\longrightarrow D\times(D+D),       \tag{3.2}
\]

where

\[
 \Omega_K=\{(u,s,q,q'):q,q'\in Q_K(u,s),\ q\ne q'\}.
\]

The name ``opposite-endpoint'' refers only to the two opposite pieces of
the switching diagram used in (3.1); it does not invoke the endpoint
decoration of a vector in `A-A`.

### Proposition 3.1: fibrewise injectivity

For fixed `(u,s)`, the restriction of `Xi` to the ordered distinct pairs in
`Q_K(u,s)^2` is injective.

### Proof

The first coordinate is

\[
 v_q=s-u-Lq.
\]

Since `L` is nonsingular, it recovers `q`.  Once `u` is fixed, the second
coordinate `2u+q'` recovers `q'`.  QED.

This removes the precise failure mode of the midpoint charge.  That charge
can identify polynomially many ordered pairs *inside one fibre*.  Under
`Xi`, a collision can occur only between two different fibre labels.

Define the charge load

\[
 \nu(v,t)=|\Xi^{-1}(v,t)|.                        \tag{3.3}
\]

Then

\[
 \boxed{\mathcal O_K=\sum_{v\in D}\sum_{t\in D+D}\nu(v,t).} \tag{3.4}
\]

The sharp missing theorem has either of the following sufficient forms:

\[
 \sum_{v,t}\nu(v,t)\le N^{1+o(1)}S,              \tag{3.5}
\]

or the stronger size-biased average-load estimate

\[
 \boxed{
 \sum_{v,t}\nu(v,t)^2
 \le N^{o(1)}\sum_{v,t}\nu(v,t).}                \tag{3.6}
\]

Indeed Cauchy--Schwarz, (3.2), and (3.6) give

\[
 \mathcal O_K^2
 \le NS\sum_{v,t}\nu(v,t)^2
 \le N^{1+o(1)}S\mathcal O_K,
\]

which is (3.5).  Estimate (3.5) is exactly the off-diagonal theorem needed
in `ADAPTIVE_RICH_FIBRE_STABILITY_LEDGER.md`.  A briefly proposed tensor
counterexample to (3.6) was invalid: Cartesian digit tensors have repeated
nonzero differences whenever one digit difference is zero.  See
`TENSOR_ZERO_DIGIT_OBSTRUCTION.md`.  Thus (3.6) remains open.

There is also an exact set-system form.  For a fibre label
`F=(u,s)`, let

\[
 E_F=\{\Xi(u,s,q,q'):q,q'\in Q_K(u,s),\ q\ne q'\}.
\]

Proposition 3.1 gives

\[
 |E_F|=g_K(u,s)(g_K(u,s)-1),\qquad
 \nu=\sum_F1_{E_F}.                              \tag{3.7}
\]

Consequently

\[
 \boxed{
 \sum_{v,t}\nu(v,t)^2
 =\mathcal O_K+\sum_{F\ne F'}|E_F\cap E_{F'}|.} \tag{3.8}
\]

Thus (3.6) is purely a cross-fibre intersection theorem.  No estimate for
the internal additive energy of an individual rich fibre remains in this
formulation.

The sets in (3.7) are explicit almost-bicliques.  For `F=(u,s)`, put
`w=s-u` and

\[
 V_F=\{w-Lq:q\in Q_K(u,s)\}\subseteq D,
 \qquad
 T_F=\{2u+q:q\in Q_K(u,s)\}\subseteq D+D.        \tag{3.9}
\]

Both displayed parametrizations are injective.  If `q` indexes its two
images by `V_F(q),T_F(q)`, then

\[
 \boxed{
 E_F=(V_F\times T_F)
       \setminus\{(V_F(q),T_F(q)):q\in Q_K(u,s)\}.} \tag{3.10}
\]

Thus one fibre contributes a complete bipartite rectangle with its
canonical perfect matching deleted.

There is also an exact pairwise overlap formula.  Let

\[
 F=(u,s),\quad G=(U,S_0),\quad w=s-u,\quad W=S_0-U.
\]

If `W-w` does not lie in `L Z^2`, then `E_F cap E_G` is empty.  Otherwise
put

\[
 \alpha=L^{-1}(W-w),\qquad \beta=2(u-U),          \tag{3.11}
\]

and define

\[
 A_{FG}=Q_F\cap(Q_G-\alpha),\qquad
 B_{FG}=Q_F\cap(Q_G-\beta).                      \tag{3.12}
\]

Equality of the first coordinates of two charges forces `p=q+alpha`, and
equality of the second coordinates forces `p'=q'+beta`.  Hence

\[
\begin{split}
 |E_F\cap E_G|=|\{(q,q')\in A_{FG}\times B_{FG}:&\ q\ne q',\\
                 &q+\alpha\ne q'+\beta\}|,
                                                               \tag{3.13}\\
 |E_F\cap E_G|\le&\ |A_{FG}|\,|B_{FG}|.          \tag{3.14}
\end{split}
\]

Combining (3.8) and (3.14) gives the concrete sufficient overlap theorem

\[
 \sum_{F\ne G}|A_{FG}|\,|B_{FG}|
 \le N^{o(1)}\mathcal O_K.                       \tag{3.15}
\]

The two translations in (3.11) are not arbitrary: one is forced by the
difference of the `w`-labels and the other by twice the difference of the
`u`-labels.  This coupled two-projection overlap, rather than an individual
fibre bound, is the exact remaining combinatorial object.

## 4. Exact preimage system for one charge key

Fix `(v,t) in D x (D+D)`.  In a preimage of this key write

\[
 a=u,\qquad b=x_q=u+q.                            \tag{4.1}
\]

Since `t=2u+q'`, all remaining parameters are forced by `(a,b)`:

\[
 q=b-a,\qquad q'=t-2a.                            \tag{4.2}
\]

Substitution into (2.1) gives the following exact formula.

### Proposition 4.1

The load `nu(v,t)` equals the number of ordered pairs `(a,b)` satisfying

\[
\begin{gathered}
 q=b-a\in P,\qquad q'=t-2a\in P,\qquad q\ne q',  \tag{4.3}\\
 a,\ b,\ t-a,\ v+J(b-a),                         \tag{4.4}\\
 v+(I-J)a+Lb-t,\qquad v+L(a+b-t)\in D.           \tag{4.5}
\end{gathered}
\]

The fixed first charge coordinate `v` is itself the seventh element of
`D`.

### Proof

Starting from a charged pair, (4.1)--(4.2) are immediate.  The six variable
members of `D` in (4.4)--(4.5) are respectively

\[
 u,\ x_q,\ x_{q'},\ y_q,\ y_{q'},\ v_{q'},
\]

because

\[
\begin{aligned}
 x_{q'}&=a+q'=t-a,\\
 y_q&=v+Jq=v+J(b-a),\\
 y_{q'}&=v+Lq-q'=v+(I-J)a+Lb-t,\\
 v_{q'}&=v+Lq-Lq'=v+L(a+b-t).
\end{aligned}                                    \tag{4.6}
\]

Conversely (4.3)--(4.5), with

\[
 u=a,\quad s=a+v+L(b-a),                         \tag{4.7}
\]

reconstruct all of (2.1)--(2.3), and (3.1) gives `(v,t)`.  QED.

Thus the aggregate problem has been reduced to a support-compensated
six-affine-copy theorem in the two vector variables `(a,b)`.  This is more
specific than a generic Fourier or additive-energy estimate: the two
popular shifts in (4.3), all six variable copies in (4.4)--(4.5), and the
fixed complete difference `v` must remain present.

## 5. Equations forced by a charge collision

Let `(a,b)` and `(a+delta,b+epsilon)` be two distinct preimages of the same
key `(v,t)`.  Taking the difference of the corresponding six entries in
(4.4)--(4.5) gives the exact displacement list

\[
 \boxed{
 \delta,\quad \epsilon,\quad-\delta,\quad
 J(\epsilon-\delta),\quad
 (I-J)\delta+L\epsilon,\quad
 L(\delta+\epsilon).}                            \tag{5.1}
\]

Every vector in (5.1) is therefore realized as the displacement between a
specified pair of elements of `D`.  In addition, the associated popular
shifts change by

\[
 q\mapsto q+(\epsilon-\delta),\qquad
 q'\mapsto q'-2\delta.                            \tag{5.2}
\]

Formula (5.1) is the exact inverse datum behind (3.6).  Deleting any of its
six components returns to unrestricted dilation or radial-transversal
models already known to be too large.  A proof of (3.6) must use the fact
that all six pairs belong to the *same* complete difference set, or show
that a high-multiplicity family of (5.1) creates enough distinct elements
of `D+D`.

There is a weak unconditional calibration.  Since `a,t-a in D`, there are
at most `R_D(t)` choices for `a`; for each `a` there are at most `N` choices
for `b`.  Hence

\[
 \nu(v,t)\le N R_D(t).                            \tag{5.3}
\]

This is far too weak to prove (3.6), but it identifies the only surviving
source of compression: many popular six-copy completions over many
representations of one ordinary sum `t`.

## 6. Exact stress tests and the surviving theorem

`verify_seven_incidence_opposite_endpoint_charge.py` checks the identities,
the fibrewise injection, and the fixed-key reconstruction exactly.

The key complete-difference profiles are:

\[
\begin{array}{c|r|r|r|r}
\text{family}&\mathcal O_K&|\operatorname{supp}\nu|&
 \mathcal O_K/|\operatorname{supp}\nu|&\max\nu\\ \hline
\text{closure }30&1,420&1,420&1&1\\
\text{closure }40&370,516&329,141&1.12571\ldots&9
\end{array}                                      \tag{6.1}
\]

The Costas families have maximum load at most a small constant.  On the
unrestricted 18-point quadratic switching gadget, the corresponding charge
has average load below `1.1` and maximum load two.  More decisively, on the
entire intended `h^2` fibre of the Sidon-ruler midpoint barrier, `Xi` is
exactly injective for every `h`: there

\[
 v_q=c-Lx_q
\]

recovers the first fibre element, while `u+x_{q'}` recovers the second.

By contrast, on the abstract radial transversals of sides 8 and 12, the
average loads are respectively `22.65...` and `77.20...`, with maxima 98
and 391.  Thus (3.6) is not a theorem about radial uniqueness.  Its precise
remaining form is:

> **Cross-fibre opposite-endpoint theorem.**  For `D=A-A` arising from a
> distance-Sidon set and for the support-adaptive popular set `P`, the load
> in (3.3) satisfies (3.6), or at least its first-moment consequence (3.5).

This theorem would finish the adaptive tail and hence the cube-root order in
Erdos problem 1208.  It is again the cleanest direct aggregate gate.  The
next proof should attack the coupled fixed-key affine system
(4.3)--(4.5), not return to the midpoint charge or to the raw majorant
`R_D(r)^2 R_D((I+J)r)`.
