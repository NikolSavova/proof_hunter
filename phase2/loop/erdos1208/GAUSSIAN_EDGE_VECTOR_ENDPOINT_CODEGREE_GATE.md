# Gaussian edge-vector charge: the endpoint-codegree gate

## 1. Outcome

This note keeps the complete endpoint data in the Gaussian charge from
`GAUSSIAN_EDGE_VECTOR_CHARGE.md`.  It proves three structural facts:

1. every fixed Gaussian key is a matching between clean-start edges and
   arbitrary edges;
2. the four endpoint roles decorating a clean start form a pair-linear
   system;
3. after stratifying a collision by its full twelve-role equality pattern,
   the desired energy estimate follows from one explicit two-endpoint
   codegree bound.

It also disposes of the branch in which both source edges and both arbitrary
edges share a same-position endpoint.  However, the resonant construction in
`GAUSSIAN_EDGE_VECTOR_TWO_ARM_BARRIER.md` proves that the Gaussian energy
bound, and therefore the remaining codegree estimate, is false in general.
The value of this reduction is diagnostic: it localizes the exact endpoint
codegree in which that counterexample must concentrate and identifies a
branch that cannot be responsible for the loss.

Throughout, `A subset Z^2` is distance-Sidon, `|A|=k`,

\[
 \Sigma=A\mathbin\oplus A,\qquad N=|\Sigma|=\binom{k}{2},
\]

and `H_q subset Sigma` is the clean-start fibre for a fixed realized directed
difference `q`.  Write `h=|H_q|`.  If `s in H_q`, canonically order the
endpoints of `s` and `s+q` and write

\[
 s=c+d,\qquad s+q=e+f,\qquad c<d,\quad e<f.                 \tag{1.1}
\]

Cleanliness says that `c,d,e,f` and the two distinguished endpoints defining
`q` are all distinct.  For any `t in Sigma`, write

\[
 t=x+y,\qquad x<y.                                         \tag{1.2}
\]

Thus `u(s)=c-d` and `u(t)=x-y`.  Put

\[
 \lambda=3(I+J),\qquad \Gamma_q(s,t)=u(s)+\lambda u(t).     \tag{1.3}
\]

## 2. Fixed keys are matchings

**Lemma 2.1 (fixed-key matching).**  For a fixed vector `z`, the records

\[
 \{(s,t)\in H_q\times\Sigma:\Gamma_q(s,t)=z\}              \tag{2.1}
\]

have pairwise distinct first coordinates and pairwise distinct second
coordinates.

**Proof.**  The canonical edge-vector map `u:Sigma -> Z^2` is injective:
equal vectors have equal squared lengths, so distance-Sidonicity identifies
the unordered edge, and the canonical orientation then identifies the
vector.  If `s` and `z` are fixed, (1.3) determines `u(t)` and hence `t`.
Likewise, `t` and `z` determine `s`.  Therefore no two records in one load
can repeat either coordinate.  In particular, a load of size `r` contributes
exactly `r(r-1)` ordered off-diagonal collisions.  \(\square\)

## 3. The clean-start decoration is pair-linear

**Lemma 3.1 (pair-linearity).**  Among clean starts decorated as in (1.1),
any prescribed labels in any two of the four roles `c,d,e,f` occur in at most
one clean start.

**Proof.**  The pairs `(c,d)` and `(e,f)` determine `s` directly from (1.1).
Suppose instead that two distinct clean starts

\[
 (c,d;e,f),\qquad (c',d';e',f')                            \tag{3.1}
\]

share labels in two cross roles.  Subtracting

\[
 c+d+q=e+f,qquad c'+d'+q=e'+f'                            \tag{3.2}
\]

gives, in the four cases,

\[
\begin{array}{c|c|c}
\text{shared roles}&\text{directed-vector equality}&
 \text{forbidden identification}\\ \hline
c=c',\ e=e'&d-d'=f-f'&d=f,\\
c=c',\ f=f'&d-d'=e-e'&d=e,\\
d=d',\ e=e'&c-c'=f-f'&c=f,\\
d=d',\ f=f'&c-c'=e-e'&c=e.
\end{array}                                                \tag{3.3}
\]

If a displayed vector is zero, both source endpoints agree and the starts
are equal.  Otherwise vector-Sidonicity identifies the ordered endpoint
pairs and gives the forbidden within-start equality in the last column.
Each contradicts cleanliness.  \(\square\)

This is useful structure absent from an abstract radially unique vector set:
`H_q` is a four-partite linear hypergraph on copies of `A`.

## 4. Exact algebra of a pairwise collision

Take two distinct colliding records.  Decorate them by

\[
 (c,d;e,f;x,y),\qquad(c',d';e',f';x',y').                  \tag{4.1}
\]

Define the six complete-difference vectors

\[
 \alpha=c-c',\quad \beta=d-d',\quad
 \eta=e-e',\quad \theta=f-f',\quad
 \gamma=x-x',\quad \delta=y-y'.                           \tag{4.2}
\]

Every one lies in the complete directed difference set `A-A`, including
zero; whenever nonzero it retains its ordered endpoint realization.  The
two clean equations and the charge collision give exactly

\[
 \boxed{\alpha+\beta=\eta+\theta,\qquad
        \alpha-\beta=-\lambda(\gamma-\delta).}             \tag{4.3}
\]

Thus any inverse argument should be applied to six *realized* complete
differences with the endpoint decorations in (4.1), not merely to four
abstract vectors.

## 5. A harmless simultaneous-overlap branch

Call a source overlap same-position if `c=c'` or `d=d'`, and an arbitrary
edge overlap same-position if `x=x'` or `y=y'`.

**Proposition 5.1.**  The number of ordered off-diagonal Gaussian collisions
having both kinds of same-position overlap is at most

\[
 4k(k-2)h=O(Nh).                                           \tag{5.1}
\]

**Proof.**  Fix one source role, say `c`.  If `D_c(a)` is the number of clean
starts with `c=a`, then `D_c(a)<=k-1` and

\[
 \sum_aD_c(a)(D_c(a)-1)\le(k-2)h.                          \tag{5.2}
\]

This counts ordered distinct source pairs sharing that role.  The same
bound holds for role `d`.

Fix such a source pair.  Its nonzero vector difference `u(s)-u(s')` is now
fixed.  The collision equation determines

\[
 u(t)-u(t')=-\lambda^{-1}(u(s)-u(s')).                     \tag{5.3}
\]

If `x=x'`, then `u(t)-u(t')=y'-y`.  Vector-Sidonicity gives at most one
ordered pair `(y',y)`, after which there are at most `k` choices for the
common endpoint `x`.  The case `y=y'` is identical.  Multiplying the two
source-role choices by the two arbitrary-edge-role choices proves (5.1).
Overlaps between the four cases only lower the union size.  \(\square\)

Consequently a bad energy cannot be explained by this most obvious endpoint
concentration.  At least one side of almost every excessive collision must
avoid a same-position endpoint overlap.

## 6. The full endpoint-codegree reduction

Use the ordered twelve-role list

\[
 \mathcal R=(c,d,e,f,c',d',e',f',x,y,x',y').                \tag{6.1}
\]

A collision satisfies the Gaussian endpoint equation

\[
 c-d-c'+d'+\lambda x-\lambda y-\lambda x'+\lambda y'=0.   \tag{6.2}
\]

Its **full equality pattern** records which of all twelve roles in (6.1)
carry the same point of `A`.  This deliberately includes the zero-coefficient
clean target roles `e,f,e',f'`; discarding them would lose the `H_q`
decoration.

Fix an equality pattern `P`.  Merge equal roles in (6.2), add their Gaussian
integer coefficients, and discard blocks whose total coefficient is zero.
Call the remaining blocks the **active blocks** of `P`.  For two active
blocks `i!=j` and two distinct points `a,b in A`, let

\[
 d_{P,i,j}(a,b)                                             \tag{6.3}
\]

be the number of ordered off-diagonal collision rows of pattern `P` having
labels `a,b` in blocks `i,j`.  Define

\[
 T_q=\max_{P,i\ne j,a\ne b}d_{P,i,j}(a,b).                 \tag{6.4}
\]

This is a completely endpoint-realized codegree: every row counted in it
still obeys both clean equations, both canonical orientations, all twelve
role equalities and inequalities, and the complete-difference relations
(4.3).

**Theorem 6.1 (endpoint-codegree gate).**  If `C_q` is the set of ordered
off-diagonal Gaussian collisions, then

\[
 \boxed{|C_q|\le B_{12}k^2T_q,\qquad B_{12}=4,213,597.}     \tag{6.5}
\]

In particular, the precise sufficient lemma

\[
 \boxed{T_q\le k^{o(1)}(h+k)}                              \tag{6.6}
\]

implies

\[
 \mathcal G_q=Nh+|C_q|le k^{o(1)}N(h+k),                  \tag{6.7}
\]

which would be the Gaussian charge gate for Erdős problem 1208.  Theorem 6.1
is a valid implication, but the two-arm barrier shows that hypothesis (6.6)
does not hold uniformly.

**Proof.**  The sum of all coefficients in (6.2) is zero.  A nonempty
pattern cannot have fewer than three active blocks.  Indeed one active
block is impossible because its coefficient would also have to sum to
zero.  With two active blocks the coefficients are `zeta,-zeta` for
`zeta!=0`, and (6.2) would identify their two labels, contrary to their
being different equality blocks.

For each fixed `P`, choose any two of its active blocks.  Every collision
row supplies one ordered pair of labels in those blocks.  There are at most
`k^2` such pairs, and each occurs at most `T_q` times.  Hence the number of
rows of pattern `P` is at most `k^2T_q`.  There are at most the Bell number
`B_12` equality patterns, proving (6.5).  Finally `N` is comparable to
`k^2`, so (6.6) and the exact diagonal contribution `Nh` give (6.7).
\(\square\)

Conversely, for any fixed `epsilon>0`, a failure

\[
 |C_q|>k^\epsilon N(h+k)                                   \tag{6.8}
\]

forces one full clean equality pattern and two fixed active endpoint-block
labels to occur together in `gg k^epsilon(h+k)` collisions (with an absolute
loss depending only on twelve roles).  This is the localized inverse target.

## 7. The two-arm no-go in codegree language

The resonant two-arm family has `k=2s`, a clean fibre of size
`h=Omega(s^2)`, and

\[
 |C_q|=\Omega(s^6),\qquad N(h+k)=\Theta(s^4).                \tag{7.1}
\]

Combining this with (6.5) forces

\[
 \boxed{T_q=\Omega(s^4)=\Omega(k^2h)}                       \tag{7.2}
\]

up to the absolute twelve-role-pattern constant.  Thus the desired bound
`T_q<=k^(o(1))(h+k)` fails by a quadratic factor.  Proposition 5.1 shows
that only `O(Nh)=O(s^4)` of these collisions can have same-position
overlaps on both edge pairs.  Hence the counterexample is not an endpoint
star disguised as additive energy: almost all of its excess lives in
patterns with a non-overlap side.

The Gaussian route is therefore closed unless a replacement charge or a
global compensation explicitly pays for the dilation-related parallel-arm
structure.  Trying to prove (6.6), even with the full clean decoration, is
not a viable restart target.

## 8. Exact finite profiles

The companion verifier selects a largest clean fibre in each stored family
and reports

\[
 (k,h,|C_q|,\#\{P\text{ occupied}\},T_q,
   |C_q^{\rm simultaneous\ overlap}|).
\]

\[
\begin{array}{c|r|r|r|r|r|r}
\text{family}&k&h&|C_q|&\#P&T_q&\text{overlap branch}\\ \hline
\text{closure }30&30&14&90&41&11&0\\
\text{closure }40&40&23&936&276&32&0\\
\text{closure }80&80&63&8424&678&116&0\\
\text{closure }120&120&127&45960&995&436&236\\
\text{Costas }22&22&34&0&0&0&0\\
\text{parabola image }43&43&171&4778&800&142&0\\
\text{resonant two-arm }s=50&100&114&769052&470&5778&2042
\end{array}                                                \tag{8.1}
\]

The final row is the important stress: its Gaussian energy is `1,333,352`,
already larger than the raw target `N(h+k)=1,059,300`.  Its codegree is much
larger than `h+k=214`, while only 2,042 of 769,052 off-diagonal collisions
belong to the simultaneous-overlap branch.  These finite values are
consistent with the asymptotic no-go in Section 7.
