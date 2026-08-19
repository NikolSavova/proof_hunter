# A fractional-basis bound for four-literal endpoint collisions

## 1. Status and outcome

Retain the four-literal load

\[
 \tau(x,y,d,f)
 =\#\{(p,q):\Lambda(p,q)=(x,y,d,f)\}
\]

from `FOUR_LITERAL_ENDPOINT_COMPLETION_GATE.md`.  This note gives an exact
pointwise majorant for the off-diagonal part of its second moment.  A
collision of two preimages forces four overlaps of the adaptive popular set
and eight overlaps of the complete difference set.  Six of the resulting
forms have six vector degrees of freedom.  The full-rank pair graph is
exactly `K_(3,5)`, with determinant a Gaussian unit on every edge.

One of the five right-hand forms duplicates a displacement already on the
left.  Removing that form and averaging the twelve bases of the remaining
`K_(3,4)` gives the minimax fractional exponents `1/3` on three overlap
counts and `1/4` on four more.  This yields a rigorous seven-overlap
analytic gate retaining all four popularity memberships.

The aggregate sum of the majorant is not yet controlled at the required
scale.  The result is therefore a new exact reduction, not a resolution of
Erdős 1208.

## 2. Collision normal form

Write `J` for counterclockwise rotation through `pi/2` and `L=I+J`.  For a
fixed literal key `(x,y,d,f)`, one preimage is parametrized by `(p,q)`, with

\[
 C=d+f-x-y,
 \qquad p'=p+J(C-q),
 \qquad q'=p'+x+q-f.                            \tag{2.1}
\]

The two records have roles

\[
 (x,x+q,x+p,d+p-q,d,d+p-Lq,d-Jp)               \tag{2.2}
\]

and

\[
 (f-p',x+q,f,y,x+y+q-f,y-Jq',d-Jp).            \tag{2.3}
\]

Compare this preimage with `(p+r,q+s)`.  Then

\[
 p'\mapsto p'+r-Js,
 \qquad q'\mapsto q'+r+(I-J)s.                 \tag{2.4}
\]

Let `P` be the adaptive popular-shift set and put

\[
 R_P(t)=|P\cap(P-t)|,
 \qquad R_D(t)=|D\cap(D-t)|.                   \tag{2.5}
\]

The four popular forms

\[
 P=p,\quad Q=q,\quad P'=p',\quad Q'=q'         \tag{2.6}
\]

lie in overlap sets with displacements

\[
 r,\quad s,\quad r-Js,\quad r+(I-J)s.          \tag{2.7}
\]

Across all literal keys, use the six Gaussian-vector variables
`(x,y,d,f,p,q)`.  The eight variable `D`-forms and their displacements are

\[
\begin{array}{c|l|l}
 &\text{form}&\text{displacement}\\ \hline
 V_0&x+q&s\\
 V_1&x+p&r\\
 V_2&d+p-q&r-s\\
 V_3&d+p-Lq&r-Ls\\
 V_4&d-Jp&-Jr\\
 V_5&f-p'&Js-r\\
 V_6&x+y+q-f&s\\
 V_7&y-Jq'&-Jr-Ls.
\end{array}                                                        \tag{2.8}
\]

Thus `V_0` and `V_6` impose different literal incidences but have the same
overlap size `R_D(s)`.

## 3. Exact rank graph

Identify the plane with the Gaussian numbers.  In variable order
`(x,y,d,f,p,q)`, the twelve forms have coefficient rows

\[
\begin{array}{c|rrrrrr}
P&0&0&0&0&1&0\\
Q&0&0&0&0&0&1\\
P'&-i&-i&i&i&1&-i\\
Q'&1-i&-i&i&i-1&1&1-i\\ \hline
V_0&1&0&0&0&0&1\\
V_1&1&0&0&0&1&0\\
V_2&0&0&1&0&1&-1\\
V_3&0&0&1&0&1&-(1+i)\\
V_4&0&0&1&0&-i&0\\
V_5&i&i&-i&1-i&-1&i\\
V_6&1&1&0&-1&0&1\\
V_7&-(1+i)&0&1&1+i&-i&-(1+i).
\end{array}                                                        \tag{3.1}
\]

### Proposition 3.1

After adjoining `(P,Q,P',Q')`, the pair `(V_a,V_b)` gives an invertible
map on the six Gaussian variables exactly when

\[
 a\in\{0,1,5\},
 \qquad b\in\{2,3,4,6,7\}.                    \tag{3.2}
\]

Every one of these fifteen Gaussian determinants is a unit; equivalently,
the corresponding real `12 x 12` determinant has absolute value one.  All
other pairs have deficient rank.  Hence the valid pair graph is exactly
`K_(3,5)`.

The verifier expands (3.1) into integer real blocks and checks all 28 pairs
by fraction-free elimination.  There is no numerical rank tolerance.

For each edge `(a,b)` of (3.2), the six output values injectively recover
`(x,y,d,f,p,q)`.  Consequently, if `C(r,s)` counts all ordered pairs of
distinct four-literal preimages with offset `(r,s)`, then

\[
\begin{split}
 C(r,s)\le{}&R_P(r)R_P(s)R_P(r-Js)R_P(r+(I-J)s)\\
 &\mathrel{}\cdot R_D(t_a)R_D(t_b),             \tag{3.3}
\end{split}
\]

where `t_a,t_b` are the displacements from (2.8).

## 4. Optimal minimax fractional basis

Discard `V_6`, whose displacement duplicates that of `V_0`, and average
uniformly over the twelve edges

\[
 \{0,1,5\}\times\{2,3,4,7\}.                  \tag{4.1}
\]

Every left vertex has marginal weight `1/3`; every right vertex has
marginal weight `1/4`; and each popular form occurs in every basis, so it
has weight one.  Taking the geometric mean of (3.3) gives the following
bound.

### Theorem 4.1: seven-overlap majorant

For every `(r,s) != (0,0)`,

\[
\boxed{\begin{aligned}
 C(r,s)\le{}&R_P(r)R_P(s)R_P(r-Js)R_P(r+(I-J)s)\\
 &\cdot [R_D(s)R_D(r)R_D(Js-r)]^{1/3}\\
 &\cdot [R_D(r-s)R_D(r-Ls)R_D(Jr)R_D(Jr+Ls)]^{1/4}.
\end{aligned}}                                                       \tag{4.2}
\]

Signs have been removed using `R_D(-t)=R_D(t)`.  The stronger pointwise
minimum form is

\[
\boxed{\begin{aligned}
 C(r,s)\le{}&R_P(r)R_P(s)R_P(r-Js)R_P(r+(I-J)s)\\
 &\cdot\min_{\substack{a\in\{0,1,5\}\\b\in\{2,3,4,7\}}}
 R_D(t_a)R_D(t_b).
\end{aligned}}                                                       \tag{4.3}
\]

An integer-power certificate for (4.2) is

\[
\boxed{\begin{aligned}
 C(r,s)^{12}\le{}&
 [R_P(r)R_P(s)R_P(r-Js)R_P(r+(I-J)s)]^{12}\\
 &\cdot[R_D(s)R_D(r)R_D(Js-r)]^4\\
 &\cdot[R_D(r-s)R_D(r-Ls)R_D(Jr)R_D(Jr+Ls)]^3.
\end{aligned}}                                                       \tag{4.4}
\]

The largest exponent `1/3` in (4.2) is optimal among fractional
combinations of the `K_(3,5)` bases after equal displacements are merged.
Indeed, if every merged exponent is at most `theta`, the row weights of
`V_1,V_5` are at most `theta`, so the row weight of `V_0` is at least
`1-2theta`.  The merged `s` exponent is at least that row weight, forcing
`1-2theta<=theta`, or `theta>=1/3`.  Construction (4.1) attains equality.

## 5. Exact aggregate gate

Every ordered pair of distinct preimages of one literal key has a unique
nonzero offset.  Therefore

\[
 \sum_{x,y,d,f}\tau(x,y,d,f)^2
 =M_K+\sum_{(r,s)\ne(0,0)}C(r,s).               \tag{5.1}
\]

Combining (5.1) with (4.2) reduces the four-literal completion theorem to

\[
\begin{split}
 \sum_{r,s}{}'&R_P(r)R_P(s)R_P(r-Js)R_P(r+(I-J)s)\\
 &\quad\cdot[R_D(s)R_D(r)R_D(Js-r)]^{1/3}\\
 &\quad\cdot[R_D(r-s)R_D(r-Ls)R_D(Jr)R_D(Jr+Ls)]^{1/4}
 \le N^{o(1)}M_K,                               \tag{5.2}
\end{split}

where the prime omits `(0,0)`.  Bound (5.2) retains all four adaptive
popularities and seven distinct complete-difference overlaps.  It is
strictly more endpoint-sensitive than the earlier two-overlap and
six-overlap relaxations.

What remains is an aggregate support-compensated proof of (5.2), or a
counterexample within genuine complete differences.  Generic radial sets
cannot decide it because they lack the endpoint-positive-definite identity
of `D=A-A`.

The exact verifier gives the following collision profiles
`(M_K, sum tau^2, occupied offsets, maximum C(r,s))`:

\[
\begin{array}{c|r|r|r|r}
\text{family}&M_K&\sum\tau^2&\#(r,s)&\max C(r,s)\\ \hline
\text{closure }40&1{,}139{,}274&1{,}161{,}442&1{,}414&670\\
\text{Costas }17&46{,}212&51{,}896&160&556\\
\text{Costas }23&3{,}020{,}644&4{,}188{,}520&1{,}730&29{,}298.
\end{array}                                                        \tag{5.3}
\]

Every occupied offset satisfies all twelve unit-determinant basis bounds
and the integer twelfth-power certificate (4.4).

## 6. Aggregate summation audit

The fractional basis does not close by a black-box Hölder step.  This can
be quantified before invoking any asymptotics.  Let `B_occ` be the sum of
the stronger minimum-basis right side (4.3), restricted only to offsets
which actually occur.  The verifier gives

\[
\begin{array}{c|r|r|c}
\text{family}&B_{\rm occ}&M_K&B_{\rm occ}/M_K\\ \hline
\text{closure }40&1{,}215{,}966{,}079{,}722&1{,}139{,}274&
 1{,}067{,}316.62\ldots\\
\text{Costas }17&12{,}952{,}750{,}200&46{,}212&280{,}289.75\ldots\\
\text{Costas }23&37{,}450{,}787{,}292{,}824&3{,}020{,}644&
 12{,}398{,}279.07\ldots.
\end{array}                                                        \tag{6.1}
\]

Thus even the occupied-offset minimum is many orders of magnitude larger
than the desired moment.  The usefulness of Theorem 4.1 is inverse: a
large genuine collision count forces seven simultaneous rich overlaps.
Summing those overlap cardinalities independently discards almost all of
the endpoint compatibility.

There is also a clean generic norm bound showing the scale of the loss.
For one basis edge, bound two independent popular-overlap factors in
`ell^1` and the other two in `ell^infty`; bound both `D` factors in
`ell^infty`.  Since

\[
 \|R_P\|_1=|P|^2,
 \quad\|R_P\|_\infty=|P|,
 \quad\|R_D\|_\infty=N,                         \tag{6.2}
\]

the resulting two-variable sum is at most

\[
 |P|^6N^2.                                      \tag{6.3}
\]

The adaptive definition gives only

\[
 |P|\le\min\{S,N^3/S\},                        \tag{6.4}
\]

because `P` lies in the `S`-element difference support and every popular
shift has `R_D(q)>S/N`, while `sum_q R_D(q)=N^2`.  Consequently the raw
norm estimate is

\[
 N^2\min\{S,N^3/S\}^6,                         \tag{6.5}
\]

far above the supercritical scale `M_K>=S^2` throughout the admissible
range `N<=S<=N^2`.

This audit changes the role of (4.2): it is not a standalone summation
lemma.  Any successful use must retain at least one of the following pieces
which (6.1)--(6.5) discard:

1. the canonical endpoint heads of the seven `D` overlaps;
2. the complete-difference Fourier lower bound;
3. the fact that only the supercritical regime `M_K>>S^2` needs closure.

The next viable refinement is therefore a head-decorated fractional-basis
or a supercritical inverse theorem, not further Hölder optimization of
(5.2).

Run `verify_four_literal_fractional_basis_gate.py` for the exact rank graph,
fractional marginals, reconstruction identities, and pointwise inequalities
on the stored genuine stresses.
