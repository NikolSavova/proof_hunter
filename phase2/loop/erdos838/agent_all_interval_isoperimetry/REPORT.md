# All-interval recovery: a sharp atomic counterexample

**Date:** 2026-08-14

**Verdict.**  The proposed all-interval word inequality is false in the
atomic tangent-word model, even at the capped demand scale relevant to the
rankwise proof.  The counterexample is a full Cartesian product, so it is
not caused by a sparse or non-injective word encoding.  It also counts
*every* two-point/two-ended interval target, without imposing a forward
orientation.  Consequently neither summing all active intervals nor a
better decoder can repair the statement at this level of abstraction.

The missing capacity is identifiable: a genuine planar block with a huge
alphabet has many non-atomic cap/cup faces inside the block.  Any viable
replacement for KIC has to retain these endpoint face complexes (or an
equivalent internal-pocket term).  Source subfaces plus two-point endpoints
are insufficient.

All logarithms below are base two.

## 1. The maximal atomic reservoir

Let `Q_1,...,Q_b` be disjoint alphabets of sizes `m_i`, and take the full
word family

\[
                  \mathcal W=\prod_{i=1}^b Q_i,
       \qquad M=|\mathcal W|=\prod_i m_i.          \tag{1}
\]

Every source word is regarded as a `b`-set, one letter from every alphabet.
Its ordinary source-face reservoir is the union of all its subsets.  For a
full product this union is exactly

\[
                  D=\prod_{i=1}^b(m_i+1),          \tag{2}
\]

because a partial word independently chooses either no letter or one letter
from each coordinate.

Give the all-interval attack the largest possible atomic two-ended pool.
For every `i<j`, allow an unordered two-letter choice in each endpoint
alphabet and, independently in every intervening alphabet, either no letter
or an arbitrary singleton, with no orientation restriction.  Its size is

\[
 T_{ij}=\binom{m_i}{2}\binom{m_j}{2}
                    \prod_{i<q<j}(m_q+1),
 \qquad T=\sum_{i<j}T_{ij}.                        \tag{3}
\]

This is at least as generous as the forward-target model: every target
made from a cap-before-cup word pair belongs to (3), while (3) also counts
the pairs with the wrong tangent orientation.  Different interval tags may
be counted separately, which only makes `T` larger than the actual union.

The hoped-for KIC-type estimate would imply, up to a subexponential loss,

\[
                       D+T\ \gtrsim\ M^{1+1/b}.    \tag{4}
\]

The next theorem disproves much more: `D+T` can be only polynomially larger
than `M`, while both `M^(1/b)` and the capped demand are exponential in `b`.

There is a useful general identity behind the construction.  Write

\[
 a_i=\log m_i,\quad A_{i-1}=\sum_{q<i}a_q,\quad
 C_{j+1}=\sum_{q>j}a_q,
\]

and define the left and right endpoint surpluses

\[
                 \lambda_i=a_i-A_{i-1},\qquad
                 \rho_j=a_j-C_{j+1}.              \tag{4a}
\]

Then, with `R=D/M`, equations (1)--(3) give

\[
 \boxed{
 {D+T\over M}
 \le R\left(1+{1\over4}\sum_{i<j}2^{\lambda_i+\rho_j}\right).} \tag{4b}
\]

Indeed, after dividing `T_ij` by `M`, the optional intermediate
coordinates contribute
`prod_(i<q<j)(1+1/m_q)<=R`; the two endpoints and the omitted outside
coordinates contribute `2^(lambda_i+rho_j)/4`.  Thus the full all-interval
Kraft sum is controlled by two one-sided prefix/suffix potentials.  A
symmetric ramp makes both potentials bounded at every location.

## 2. A symmetric ramp--plateau--ramp product

> **Theorem 1 (atomic all-interval counterexample).**  Let `h>=6`, put
> `L=2^h` and `k=L/2`, and form the exponent word
> \[
> (a_1,\ldots,a_b)=
> (1,2,4,\ldots,L/2,
>       \underbrace{L,\ldots,L}_{k\text{ copies}},
>       L/2,\ldots,4,2,1),                         \tag{5}
> \]
> so `b=k+2h`.  Set `m_i=2^{a_i}` and use the full product (1).  Then
> \[
> \boxed{
> {D+T\over M}<21\left(1+\binom b2\right),\qquad
> M^{1/b}\ge 2^{2L/3}.}                            \tag{6}
> \]
> If `n_0=sum_i m_i`, `ell=ceil(log n_0)`, and
> `d=2^(ell-b)`, then
> \[
>                  d\ge {2^{L/2}\over2L}.          \tag{7}
> \]
> In particular, for all sufficiently large `h`,
> \[
>                         D+T<dM.                  \tag{8}
> \]

**Proof.**  First divide (2) by (1).  Since `1+x<=e^x`,

\[
 {D\over M}=\prod_i(1+2^{-a_i})
 \le \exp\left(\sum_i2^{-a_i}\right)<e^3<21.      \tag{9}
\]

Indeed each geometric ramp contributes
`sum_(q=0)^(h-1) 2^(-2^q)<1`, and the plateau contributes
`k2^(-L)<1`.

For the interval term put

\[
 A_{i-1}=\sum_{q<i}a_q,\qquad C_{j+1}=\sum_{q>j}a_q.
\]

Using `binom(m,2)<=m^2/2` in (3), and bounding the optional
intermediate-letter multiplier by the full down-face ratio (9), gives

\[
 {T_{ij}\over M}
 < {21\over4}
       2^{a_i-A_{i-1}}2^{a_j-C_{j+1}}.             \tag{10}
\]

Every left-ramp entry satisfies `A_(i-1)=a_i-1`; the first plateau
entry has the same identity because the left ramp sums to `L-1`.
Thereafter the prefix only grows.  Hence

\[
                       a_i-A_{i-1}\le1             \tag{11}
\]

for every `i`.  By symmetry,

\[
                       a_j-C_{j+1}\le1             \tag{12}
\]

for every `j`.  Equations (10)--(12) give `T_ij<21M`, and summing over
the fewer than `binom(b,2)` intervals proves the first part of (6).

The exponent of `M` is

\[
 S:=\log M=kL+2(L-1)\ge L^2/2.                    \tag{13}
\]

For `h>=6`, `b=L/2+2h<=3L/4`, so `S/b>=2L/3`, proving the second
part of (6).

Finally `n_0>=k2^L`, whence

\[
 \ell-b\ge L+\log k-(k+2h)
          =L/2-h-1.                                \tag{14}
\]

This is (7).  Its right side eventually exceeds
`21(1+binom(b,2))`, so (8) follows from (6).  QED.

The counterexample remains valid if the atomic reservoir is enlarged to
include **every** face using at most two letters in each endpoint block,
including the one-ended pair--singleton and singleton--pair families omitted
from (3).  Put

\[
 B_i=m_i+\binom{m_i}{2}le m_i^2
\]

and grant the full atomic vertical-composition count

\[
 \mathcal A=1+\sum_iB_i+
   \sum_{i<j}B_iB_j\prod_{i<q<j}(m_q+1).          \tag{14a}
\]

In the constructed instance `B_i<=m_i^2<=M`.  The proof of (10), now
without the factor `1/4`, shows that every interval summand in (14a) is
less than `84M`.  Therefore

\[
 \boxed{\mathcal A/M<1+b+84\binom b2<d}           \tag{14b}
\]

for all sufficiently large `h`.  Thus the failure is not an artefact of
forgetting mixed one-ended atomic targets.

## 3. Why this hits all three regression tests

1. **Full product grid.**  The sources are not a subset of a product: they
   are the entire product.  Thus the failure cannot be blamed on copies
   receiving the same short word.
2. **Long nested prefix.**  The two exponential ramps are precisely a
   scalable forgotten-prefix/suffix construction.  Their defining identity
   `a_i-(a_1+...+a_(i-1))=1` says that moving an endpoint inward gains only
   the entropy just discarded.  Every single interval, including a plateau-
   spanning interval, consequently has only constant excess over `M`.
3. **All-cup to all-cap.**  Formula (3) ignores cap/cup orientation and
   awards every unordered endpoint pair.  An adversarial orientation or an
   all-cup--all-cap threshold can only remove targets, so it cannot restore
   (4).

The example also respects the rank window in which capped demand is
nontrivial.  Here

\[
 b=L/2+O(\log L),\qquad \log n_0=L+O(\log L),      \tag{15}
\]

so `b=(1/2+o(1))log n_0`, and the cap `d=2^(ell-b)` is exponential
in `b`.  Nevertheless the maximal atomic all-interval reservoir has only
polynomial excess.

## 4. Geometric meaning and the corrected target

The counterexample does **not** disprove the planar capped-Hall statement.
It disproves the abstraction which treats a large tangent alphabet as an
atomic list of endpoint letters.

A vertical composition with block sizes `m_i` realizes all the source words
in (1) and all the rank-two endpoint targets in (3).  But an actual
`m_i`-point block also contains higher cap/cup faces.  If `C(Q_i)` and
`U(Q_i)` denote its nonempty cap and cup counts, the genuine interval term is

\[
 C(Q_i)U(Q_j)\prod_{i<q<j}m_q,                    \tag{16}
\]

not merely the rank-two lower bound in (3).  On the long `m_i=2^L`
plateau, the internal cup--cap theorem forces large non-atomic endpoint
reservoirs.  Those are exactly the terms erased by the atomic word model.

Thus a valid replacement for KIC must be an **enriched all-interval
inequality** with one of the following equivalent inputs:

* the full endpoint polynomials `C(Q_i),U(Q_i)`;
* the ordinary convex-face mass inside every tangent alphabet/pocket; or
* a recursive term which descends into a high-entropy alphabet before
  treating it as one coordinate.

The ramp identity (11) shows why a Kraft inequality on forgotten word
coordinates alone cannot work: it is exactly saturated at every depth.
The next attack should therefore recurse on **entropy mass**, not on the
number of exposed coordinates, and stop at a block only after charging its
internal cap/cup complex.

## 5. The exact enriched Bellman recurrence

Retaining the full endpoint complexes gives a clean corrected quantity, but
not yet a universal lower bound.  Let `C_i,U_i,V_i` be the nonempty cap,
cup, and convex-face counts inside block `Q_i`.  For a convex macro chain,
the enriched reservoir is exactly

\[
 \mathcal E_b=
 \sum_iV_i+
 \sum_{i<j}C_iU_j\prod_{i<q<j}(m_q+1).             \tag{17}
\]

The interval families are disjoint after tagging their first and last
multiply occupied blocks.  Formula (17) has the following two-state Bellman
recurrence:

\[
 \begin{array}{lll}
 P_1=C_1,&&F_1=V_1,\\
 P_j=C_j+(m_j+1)P_{j-1},&&
 F_j=F_{j-1}+V_j+P_{j-1}U_j.                     \tag{18}
 \end{array}
\]

Here `P_j` is unspent left-cap credit transported through optional singleton
blocks, and `F_j=mathcal E_j` is spent convex credit.  If
`M_j=prod_(q<=j)m_q`, the normalized recurrence is

\[
 \begin{split}
 p_j&=(1+1/m_j)p_{j-1}+C_j/M_j,\\
 f_j&=f_{j-1}/m_j+V_j/M_j+p_{j-1}(U_j/m_j),       \tag{19}
 \end{split}
\]

where `p_j=P_j/M_j` and `f_j=F_j/M_j`.  The factor `1/m_j` in the first
term of `f_j` is the exact forgotten-suffix loss.  Unlike a decoder bound,
there is no hidden fibre in (18)--(19).

For a genuine rooted-pocket proof, (18) must become a vector recurrence:
`P_j` is distributed over the two endpoint tangent ranks, and the spend
`P_(j-1)U_j` is replaced by the southeast-dominance convolution from the
two-root tangent criterion.  Summing the vector to a scalar before the spend
permits all-cup--all-cap anti-alignment and is invalid.

The exact scalar statement which would discharge a product pocket of source
rank `b` is

\[
 \boxed{
 F_b\ge 2^{\lceil\log(\sum_i m_i)\rceil-b-o(b)}
                 \prod_i m_i.}                    \tag{EKIC}
\]

For arbitrary planar blocks this is not currently proved.  Its two-block
core already asks cap mass on the left to meet cup mass on the right; this
is the unrestricted endpoint-alignment problem in another notation.

## 6. Full internal marginals still do not give a scalar theorem

The ramp example is automatically paid if its plateau blocks have suitably
aligned endpoint complexes.  It is **not** automatically paid by a large
product `C_iU_i` in every block.  The following numerical profile is an
exact obstruction to any proof using only the scalar constraints
`C_i,U_i<=V_i` and a same-block cap--cup product bound.

On plateau position `p=1,...,k`, put

\[
 \begin{split}
 C_p&=2^{(p+1)L},&
 U_p&=2^{(k-p+2)L},&
 V_p&=C_p+U_p.                                    \tag{20}
 \end{split}
\]

On a ramp block use only the unavoidable one- and two-point endpoint
families.  The normalized plateau endpoint logs are

\[
 x_p=\log(C_p/m)=pL,qquad
 y_p=\log(U_p/m)=(k-p+1)L.                        \tag{21}
\]

Consequently every plateau block has the very strong same-block product

\[
             \log(C_pU_p)=(k+3)L={L^2\over2}+3L, \tag{22}
\]

and `V_p` contains both marginals.  Nevertheless, after including the left
and right ramps,

\[
 x_p-\sum_{q<p}a_q=1,qquad
 y_p-\sum_{q>p}a_q=1.                             \tag{23}
\]

The same upper bounds hold on the ramps.  Thus every forward product in
(17), even with all optional intermediate singletons, is at most `21M`.
Also

\[
 \max_p\log V_p\le(k+1)L+1={L^2\over2}+L+1,
 \qquad
 \log M={L^2\over2}+2L-2.                        \tag{24}
\]

It follows that

\[
                  \mathcal E_b/M=b^{O(1)},        \tag{25}
\]

whereas the capped demand is at least `2^(L/2)/(2L)`.  So `(EKIC)` fails
for these scalar data despite the positive linear surplus in (22).

This is a **numerical profile obstruction**, not a claimed planar order
type.  Its role is precise: no collection of inequalities involving only
the numbers `(m_i,C_i,U_i,V_i)` separately at each block can prove EKIC
unless it also rules out the directional gradient (21).  The needed extra
input is a recursive compatibility law tying where cap mass and cup mass
sit in the endpoint/tangent array.  In a mirror-decomposition tree this is
exactly what the endpoint-reset theorem supplies.  For an arbitrary pocket,
it is the missing geometry.

There is a sharp max-plus form of the obstruction.  For equal plateau sizes
write `x_i=log(C_i/m)` and `y_i=log(U_i/m)`.  A cross term from `i<j`,
normalized by the full source product, has logarithm

\[
 x_i+y_j-L(i-1+k-j)-2(L-1)+O(1).                 \tag{26}
\]

The gradient `x_i=iL`, `y_i=(k-i+1)L` makes (26) constant for **every**
pair.  Therefore the sharp recursive target cannot merely assert
`x_i+y_i` is large.  It must force a reset of this slope, pay `V_i`, or
retain the two-dimensional tangent type until a later compatible spend.

The exact scalar threshold can be stated as follows.

> **Lemma 2 (sharp plateau reset inequality).**  Consider `k` equal blocks
> of logarithmic size `L`, with a left and right outside tail of total
> logarithmic size `R` each.  Put
> `x_i=log(C_i/m)` and `y_i=log(U_i/m)`.  Suppose, for every `i`,
> \[
> x_i+y_i\ge K,\qquad a\le x_i,\qquad x_i\le W.    \tag{27}
> \]
> Then some adjacent forward interval satisfies
> \[
> \boxed{
> \log{C_iU_{i+1}\over M}
> \ge K-L(k-1)-2R-
>       {W-a-L(k-1)\over k-1}.}                   \tag{28}
> \]
> Here `M` is the product of all plateau and tail alphabet sizes.  Optional
> intermediate singleton choices only improve the bound.

**Proof.**  Set `z_i=x_i-L(i-1)`.  From (27),

\[
 \begin{split}
 x_i+y_{i+1}-L(i-1+k-i-1)-2R
 &\ge K-L(k-1)-2R-(z_{i+1}-z_i).                 \tag{29}
 \end{split}
\]

At least one adjacent increment is no larger than
`(z_k-z_1)/(k-1)`.  The other two bounds in (27) give

\[
 z_k-z_1\le W-a-L(k-1).                           \tag{30}
\]

Substitution proves (28).  QED.

The gradient (21) attains equality in (28): take
`K=(k+1)L`, `a=L`, `W=kL`, and `R=L-1`; both sides equal `2`.
Thus even the linear term is sharp.  To pay capped demand `d`, a scalar
same-block product theorem would need the right side of (28) to be at least
`log d-o(b)`.  The usual leading-coefficient statement
`K=(1/2+o(1))L^2` does not decide this; the ramp turns its unresolved linear
error into the whole capped deficit.

## 7. The corrected tangent-vector recurrence

The scalar bank in (18) forgets exactly the datum which decides whether a
left cap and a right cup glue.  For a fixed directed root chord, let
`Theta` be the finite set of two-root tangent cells.  Write a cell as
`theta=(lambda,rho)`, in the two angular rank orders.  The tangent criterion
says that an upper cell `theta` and a lower cell `phi` are compatible when

\[
                  D(\theta,\phi)=1
  \quad\Longleftrightarrow\quad
  \lambda_\theta>\lambda_\phi,
  \quad \rho_\theta<\rho_\phi.                   \tag{31}
\]

Let `c_j,u_j` be the cap and cup count vectors of block `j`.  Transporting
an unspent rooted cap through block `j` can change its endpoint neighbours,
so in general it is described by a nonnegative integer kernel `K_j` on
`Theta`, rather than multiplication by a scalar.  The exact vector Bellman
recurrence is

\[
 \boxed{
 \begin{split}
 p_1&=c_1, & f_1&=V_1,\\
 p_j&=c_j+K_jp_{j-1}, &
 f_j&=f_{j-1}+V_j+p_{j-1}^{\mathsf T}D u_j.
 \end{split}}                                     \tag{32}
\]

If the type space is collapsed to one cell and every pair is declared
compatible, `K_j` has the single entry `m_j+1`, and (32) reduces to (18).
For a fixed common root/signature, every compatible product in the last
term is a convex two-ended target.  The ordered-array recovery theorem gives
at most two source matchings for fixed state, and the global description
bound is at most `2r^6`.  Thus, after summing states, the geometrically usable
credit is

\[
              {1\over2r^6}
              \sum_{\text{states},j}p_{j-1}^{\mathsf T}Du_j, \tag{33}
\]

up to the already explicit subexponential number of prefix states.  Formula
(33) is the exact fibre loss; there is no `n^(Theta(r))` decoder.

There is a rigorous one-step reset theorem for (31).

> **Lemma 3 (weighted tangent spend/reset partition).**  Let `alpha,beta`
> be nonnegative weights on two finite tangent-cell families, of total mass
> `A,B`.  Put
> \[
> G=\sum_{\theta,\phi}\alpha_\theta\beta_\phi
>                              D(\theta,\phi).
> \]
> Assign an incompatible pair first to `L` if
> `lambda_theta<=lambda_phi`, and otherwise to `R` (where necessarily
> `rho_theta>=rho_phi`).  If their weights are `G_L,G_R`, then
> \[
>                  \boxed{AB=G+G_L+G_R.}           \tag{34}
> \]
> Consequently one term is at least `AB/3`.  In either failure term, after
> removing equal-rank cells, the strict rank relation is a disjoint union of
> dyadic separated rectangles on at most `ceil(log n)` levels.  Hence either
> the union of diagonal equality cells carries at least a
> `1/(1+ceil(log n))` fraction of the failure, or one dyadic level does.

**Proof.**  The tangent criterion partitions every pair into the compatible
case, failure of the first strict inequality, or success of the first and
failure of the second.  This is (34).  For one strict failed rank relation,
pad the rank order to a power of two and assign a pair to the lowest dyadic
interval containing both ranks.  Its two child intervals form a separated
rectangle; lowest ancestors are unique, rectangles at one depth have
disjoint rank supports, and there are at most `ceil(log n)` depths.  Together
with the one diagonal class this is a partition into at most
`1+ceil(log n)` batches.  QED.

This proves a compatible spend or a canonical one-marginal child at every
mixed state.  It does **not** prove capped Hall by iteration: paying a
`log n` loss at linearly many rank drops costs `2^(Theta(r log r))`, and a
large equality cell may retain all quadratic core entropy.  The recurrence
must enter that cell and expose its next tangent coordinate.

## 8. A realizable fixed-cell obstruction

The equality-cell issue is real geometry, not only an array pathology.
Take the root chord

\[
                         u=(0,0),\qquad v=(1,0).
\]

Above it fix endpoint neighbours

\[
 a_u=(1/4,3/16),\qquad a_v=(3/4,3/16),             \tag{35}
\]

and put arbitrarily many optional points on the strictly concave arc
`y=x(1-x)` between them.  Every choice of a fixed number of optional points,
together with `u,v,a_u,a_v`, is a rooted convex chain with the same tangent
type

\[
                         (L_A,R_A)=(4/3,-4/3).     \tag{36}
\]

Below the chord fix

\[
 b_u=(-3,-1),\qquad b_v=(4,-1),                   \tag{37}
\]

and use optional points on
`y=(x-1/2)^2-53/4` between them.  These give rooted convex chains of fixed
type

\[
                         (L_B,R_B)=(3,-3).         \tag{38}
\]

Both inequalities in (31) fail, so **no** upper chain glues convexly to any
lower chain.  With `q` optional points on each side and `s=floor(q/2)`, each
cell contains

\[
                              M_q=\binom qs        \tag{39}
\]

distinct equal-rank rooted chains, but the compatible product is zero.  By
contrast, reflecting the upper arc to `y=-x(1-x)` gives lower type
`(-4/3,4/3)`, and every one of the `M_q^2` cross pairs is convex.

Thus a fixed tangent cell can carry arbitrarily large internal entropy.  The
complete ordinary subchain reservoirs on the two sides have only
`2^(q+O(1))=M_q q^(O(1))` faces each, additively, rather than the
`M_q^2=2^(2q-O(log q))` compatible product.  Full two-dimensional tangent
distributions correctly report zero spend; they do not themselves force a
reset or internal product.

This is a stretchable rational local gadget.  It is not a counterexample to
Erdos 838 or to the full repair-record theorem: an ACP record also knows that
`A=(T-p) union I` is a convex source and that `p` is an outward successor.
The gadget proves that these correlations are indispensable additional
axioms.  Entropy and tangent distributions alone are insufficient.

## 9. Interface with the outward-successor split

The outward-successor theorem produces an injective repair record

\[
                         g\longmapsto(T_g,I_g),
 \qquad |T_g|+|I_g|=r+1,                          \tag{40}
\]

with

\[
 H(T)+H(I\mid T)=\log|\mathcal G|.                \tag{41}
\]

It also canonically retains the common prefix and blocker in `T`.  Therefore
the vector state in (32) can be indexed without an ambient-label decoder:
only the two tangent ranks and the recursive hidden suffix remain.

Lemma 3 now gives the exact mixed-state trichotomy:

1. compatible tangent mass spends through (33);
2. a left-failure rectangle fixes a left marginal and recurses into the
   corresponding hidden suffix; or
3. a right-failure rectangle does the reflected recursion.

Equations (40)--(41) ensure that entering a child does not lower entropy per
expected rank.  The rational gadget in Section 8 shows why internal-face
mass does not automatically force case 1: both entropy terms may be large
inside one incompatible cell while their separate ordinary reservoirs are
only additive.

The corrected remaining theorem is consequently a **hierarchical tangent
reset**, not a one-level dominance inequality:

\[
 \boxed{
 \begin{minipage}{0.86\linewidth}
 Along the prefix-correlated outward-successor recursion, a fixed tangent
 failure cell must either spend through a compatible descendant rectangle,
 release its internal convex-face complex, or pass to children whose total
 doubled capped load is at least the parent load, with only `2^{o(r)}`
 global reuse.
 \end{minipage}}                                   \tag{HTR}
\]

`(HTR)` would combine the exact entry factor `S^(1/r)` from the
outward-successor theorem, the polynomial recovery loss (33), and
entropy-density conservation (41), and would close the capped Hall gate.
The scalar gradient of Section 6 and the fixed-cell gadget are its two sharp
tests.  No proof of `(HTR)` is supplied here; nor is there a realizable
repair-record counterexample.  The advance is that a vector-valued
one-level version is now rigorously killed, and the exact missing recursive
axiom and fibre budget are explicit.

## 10. What the ACP correlation adds

For an outward-successor record put

\[
 R_g=T_g-\{p_g\},\qquad I_g=A_g-T_g.
\]

The correlation absent from Section 8 has the exact normal form

\[
 \boxed{
 A_g=R_g\cup I_g\text{ convex},\qquad
 T_g=R_g\cup\{p_g\}\text{ convex},}               \tag{42}
\]

where `I_g` is one consecutive source interval, `p_g` is an outward
successor of a witness source with the canonical prefix, and
`g mapsto(R_g,I_g,p_g)` is injective.  The last assertion follows from the
canonical recovery of `p_g` from `T_g` and the identity in (42).

Thus the incompatible upper/lower Cartesian product in Section 8 cannot be
inserted unchanged: every occurring pair `(R,I)` must already have the
convex union `R union I`.  To reproduce zero completed compatibility one
needs a genuine **toggle**: replacing `I` by the outward label `p` moves the
rooted tangent type across the compatibility boundary.

There is a rigorous base case where the internal complex always pays.

> **Theorem 5 (fixed-core short-ear discharge).**  Fix a retained convex
> core `R`, and let `mathcal G_R` be ACP records satisfying (42), all with
> `|I_g|<=s`.  If `m` is the number of ambient labels which occur in an ear
> or as a blocker, then
> \[
> \boxed{
> |\mathcal G_R|
> \le m\sum_{j=0}^s\binom mj
> \le (s+1)m^{s+1}.}                              \tag{43}
> \]
> Consequently, if `s=o(log m)`, the ordinary convex-face complex on those
> `m` labels satisfies
> \[
>                       |\mathcal G_R|\le V(P)     \tag{44}
> \]
> for all sufficiently large `m`.

**Proof.**  With `R` fixed, a record is determined by its blocker label and
its hidden label set, proving (43).  The explicit Erdős--Szekeres
double-count bound gives, for `L_m=floor(log m)>=64`,

\[
                     V(P)\ge2^{L_m^2/10}.          \tag{45}
\]

The logarithm of the right side of (43) is at most
`(s+1)log m+O(log(s+1))=o((log m)^2)`, proving (44).  QED.

In particular, a complete fixed-core rank-one successor cell has at most
`m^2` records and is swallowed by its ambient label cloud.  The hard ACP
branch must have ears of linear logarithmic rank, or quadratic entropy over
many retained cores.  This recovers, directly from the ACP correlation, the
same stopping scale as the terminal-child theorem.

More generally, if the record family is covered by `K` retained cores, (43)
gives

\[
                 |\mathcal G|\le K(s+1)n^{s+1}.    \tag{45a}
\]

When `r=Theta(log n)`, `s=o(r)`, and `log K=o(r^2)`, the right side has
`o(r^2)` logarithmic bits and is again absorbed by (45).  Thus the two
conditions in the preceding paragraph are simultaneous and quantitative:
a hard short-ear family cannot hide behind subquadratically many cores.

## 11. The zero-compatible cell does embed, but its short-ear complex pays

A blanket non-embedding lemma is false.  Here is an exact rational ACP
gadget.  Let `R` be a convex upper rooted chain containing
`u=(0,0),v=(1,0)`.  For `j=0,...,q-1`, put

\[
 z_j=\left({1\over2}+{j^2\over100q^2},-2^{j+1}\right).        \tag{46}
\]

For every `i<j`, the horizontal cross-section of the triangle
`conv{u,v,z_j}` at the height of `z_i` contains `[13/50,3/4]`, while the
first coordinate of `z_i` lies strictly between `1/2` and `51/100`.
Thus `z_i` lies strictly inside `conv(R union {z_j})`.  Define

\[
 A_i=R\cup\{z_i\},\qquad p=z_j,qquad
 T_{ij}=R\cup\{z_j\},\qquad I_{ij}=\{z_i\}.       \tag{47}
\]

Every set `A_i` and `T_ij` is convex, while `A_i union {z_j}` is nonconvex
and repairs exactly by deleting `z_i`.  The witness source is `A_j`; choose
the canonical boundary orientation so all sources share the upper boundary
prefix through `u`, and `z_j` is its
outward successor.  Relative to the configuration `R union {z_0,...,z_(q-1)}`,
no other `z` is addable to `A_i`: a deeper point hides `z_i`, and a shallower
point is interior to the hull already containing `z_i`.  Thus the sources
even have addable degree zero.

There are `binom(q,2)` repair records but only `q` source faces and `q`
repaired targets.  Hence ACP correlation alone does **not** turn records
injectively into either component.  Nevertheless Theorem 5 applies with
`s=1`; more concretely the label cloud itself has far more than `q^2`
ordinary convex faces asymptotically by (45).  The embedded fixed-cell
obstruction is therefore harmless for exactly the required internal-complex
reason.

Choosing `|R|=ceil(log q)-1` puts the source rank at
`(1+o(1))log|P|`, so this is a scalable regression at the correct rank
window, not merely a fixed-rank picture.  What it does not realize is the
hard case `|I|=Theta(r)` with quadratic retained-core entropy.

Combining (42)--(45), any counterexample to `(HTR)` must simultaneously
have

* hidden intervals of `Theta(r)` rank;
* `2^{Omega(r^2)}` entropy across retained cores or hidden families; and
* outward blocker reuse across those cores, since fixed-core short ears are
  already paid by their label complex.

This is precisely the product-grid scale.  No realizable family is known
which keeps the toggle (42), defeats all descendant tangent rectangles, and
also keeps its internal face complex below capped demand.

## 12. Quadratic hidden entropy does not by itself create blocker surplus

Conditioning on `(R,p)` and applying an unrestricted lower bound to the
hidden-ear label union is insufficient, even if
`H(I|R,p)=Theta(r^2)`.  The exact obstruction is the long-ear version of
the common-apex product repair cell.

Take `b=floor(alpha r)` ordered internal microblocks, each of size
`M=2^(floor(beta r))`, and let the hidden ear choose one point in every
block.  Thus

\[
 |\mathcal I|=M^b,qquad
 H_2(I\mid R,p)=b\log M
             =(\alpha\beta+o(1))r^2.              \tag{48}
\]

Put an `M`-point outward blocker cloud in a common apex pocket.  Every
blocker hides the whole internal word; a fixed outer witness tail makes it
the successor of a source with the same prefix.  These are the standard
prefix-correlated common-apex repairs.  The record, source, and repaired-
target counts are

\[
                  |\mathcal G|=M^{b+1},qquad
                  |\mathcal S|=M^b,qquad
                  |\mathcal T|=M.                 \tag{49}
\]

The hidden label union has only

\[
                         m=bM,qquad
                 \log m=(\beta+o(1))r.            \tag{50}
\]

points on the logarithmic scale.  Even the conjectural unrestricted bound
with coefficient `1/2` would give from its size alone only

\[
             \log V(\text{hidden cloud})
             \ge(\beta^2/2-o(1))r^2.              \tag{51}
\]

If `alpha>beta/2`, this is smaller than the entropy in (48), whose source
faces are already known explicitly.  It supplies no reason for the missing
factor `M=2^(beta r+O(1))` in (49).  The proved coefficient `1/4` is still
weaker.  Thus “quadratic conditional entropy + unrestricted lower bound on
the union” cannot prove HTR.

Hidden-ear thinning has the same exact limitation.  The complete down-face
reservoir of the product words is

\[
                         (M+1)^b,qquad
 { (M+1)^b\over M^b}
   =\left(1+{1\over M}\right)^b=1+o(1),           \tag{52}
\]

not a factor `M`.

This is not a counterexample to HTR.  Its internal geometry supplies the
missing multiplication through genuine two-ended faces.  The full-span
rank slice alone has

\[
               \binom M2^2M^{b-2}
               ={(M-1)^2\over4}M^b,              \tag{53}
\]

which is much larger than the `M^(b+1)` record demand.  Equations
(48)--(53) isolate the exact stability statement still needed: high hidden
entropy must be converted to an **oriented two-ended surplus relative to
the already-present source family**, not to an absolute lower bound in
terms of the label-union size.

The common-apex product and the nested rank-one gadget are the two endpoint
regressions.  In the first, thinning and absolute cloud bounds fail but the
two-ended product pays.  In the second, no two-ended product is needed
because the short-ear cloud pays.  A genuine HTR obstruction would have to
interpolate between them while defeating both mechanisms; no such
realizable family is known.

## 13. Independent fixed-gap low-count structural line

The separate artifact `LOW_V_FIXED_GAP.md` audits a route independent of
ACP Hall.  Its exact conclusions are:

* under `log V(P)<=(1/2-delta)(log n)^2`, a mirror-decomposable extraction
  of exponent `alpha>sqrt(1-2delta)` already contradicts the sharp strong
  theorem;
* adding an enclosing generic triangle produces a one-node prime order type
  while multiplying `V` by at most eight and increasing the largest
  decomposable subset by at most three;
* every sub-half homogeneous vertical tower has a macro scale of relative
  logarithmic size at least `(3-sqrt(9-8delta))/2`, so the fixed gap removes
  the guarded/fixed-template obstruction exactly;
* a scalable nongeometric hereditary complex satisfies `CU>=V`, the scalar
  cup--cap constraint, and the strong bound on every declared structured
  piece while keeping all such pieces of size `O(log n)`.  Hence a genuine
  regularization proof must use planar oriented compatibility, not scalar
  entropy and endpoint totals alone.

## 14. Two-record/two-face uncrossing

The separate artifact `TWO_RECORD_UNCROSSING.md` proves the exact square
inequality for a complete linear-ear product cell.  If the two active
endpoint alphabets have sizes `q_1,q_b`, the blocker cloud has size `y`,
and every `<=2` choice in the endpoint alphabets gives the corresponding
two-ended face, then

\[
 |\mathcal G|^2\le
 \left\lceil{q_1 q_b y^2\over
  (1+q_1+\binom{q_1}2)(1+q_b+\binom{q_b}2)}\right\rceil V(P)^2.
\]

For `q_1=q_b=y=M` the fibre is at most four, even with arbitrary variable
retained cores.  One output face stores the first source; the endpoint
`<=2` subsets of the second face code its two endpoint labels and both
blockers.  A dominance/reset corollary says low endpoint alphabets recurse
with increased entropy density, high endpoint/blocker alphabets are
component surpluses, and balanced endpoints spend with `2^o(r)` loss.

The stronger symmetric form modifies one terminal coordinate in each of
the two output sources.  Its identical fibre formula needs only two
separate one-slot face pools; the active tangent cells need not be
nonadjacent and may be the same cell.  This matters because adjacent cell
antichains do not necessarily coexist even after their common guard is
deleted; `TWO_RECORD_UNCROSSING.md` gives an exact eleven-point integer
counterexample.  Hence the symmetric code removes a real, not cosmetic,
geometric obstruction.

The elementary shortcut `I union {p}` is convex is false: the exact rational
configuration `A={(x,x^2):-4<=x<=4}`, `p=(1/10,-3)` hides
`I={(-1,1),(0,0),(1,1)}`, while `(0,0)` is interior to the triangle formed
by `p` and the two ear endpoints.  The remaining gate is to derive the
two-ended endpoint pool from an arbitrary weighted DRC fan; whole-ear fan
completeness alone does not provide that tangent-coordinate factorization.

The full-hierarchy audit separates level depth from reuse.  For a marked
rank-`k` nesting step, the `2^(k-1)` subfaces containing its fresh tip give
an exact Kraft inequality.  At ranks `k>=ceil(log n/2)`, their mass pays the
cap `2^(ceil(log n)-k)`.  Along one monotone chain the marked downclosures
are disjoint, so even `Theta(r)` nesting levels cost only a constant factor
(or `r` when the mark is implicit).  The sole remaining loss is inter-chain
reuse: exponentially many
variable-core histories can merge into the same marked downfaces, and no
current tangent invariant bounds that multiplicity.

The guard-retaining weighted-shadow theorem regularizes that multiplicity:
delete `t` non-guard vertices from a variable base but retain the two
endpoints of the insertion edge.  In the resulting face the inserted mark's
two cyclic neighbours recover the edge.  Duplicated Hall gives exact fibre
`ceil((k-t+1)Lambda/binom(k-2,t))`; a heavy collision therefore fixes the
mark, a common `(k-t)`-prefix, and the same tangent edge.  With
`t=ceil(sqrt(k))` all state tags cost `2^o(r)`.  Light states map directly
to faces and close after applying the symmetric code independently to the
two records.

If a later adjacent-edge rotation erodes the common prefix, the erased
pieces form disjoint prefixes/suffixes of a nested boundary interval.  There
are at most `r` such switches and at most `3^r` complete erosion transcripts;
hull growth prevents cycles.  This is `2^o(r^2)` and closes the transcript
budget for the weaker coefficient target, but not yet global terminal-face
reuse across different outer cores.

At the coefficient scale the latter reuse closes by stopping at the first
heavy shadow and using the two full-rank cross-sources of a repair `C_4`.
If their guarded prefixes omit at most `t=ceil(sqrt(r))` labels, the output
prefix pair has fibre at most `r^O(1)n^(2t+2)`: guess the two residuals and
the two blockers, then recover both diagonal records.  This is
`2^O(r^(3/2))=2^o(r^2)`.  Hence light shadows, heavy shadows, and adjacent
root-walk transcripts all have subquadratic global reuse.  The residual
ACP interface is to expose the guarded shadow on those full-rank cross-
sources, rather than only on one lower-rank component; the argument does
not close the sharper `2^o(r)` capped Hall scale.

There is a still simpler coefficient-scale conclusion.  Any counted repair
`C_4` maps to its two full cross-sources `R_1 union I_2` and
`R_2 union I_1`.  Guessing the two blockers and the two set partitions has
fibre at most `n^2 2^(2r)=2^O(r)`.  Thus global terminal-face-pair reuse
across arbitrary outer cores is completely closed once a rectangle has
been extracted.  The only remaining coefficient-scale issue in this line
is analytic: convert the weighted `C_4` mass from near-product stability,
after component-surplus/degree regularization, into
`|G|^2/2^o(r^2)` counted rectangles.  The capped Hall route still needs the
finer endpoint code because `2^O(r)` is not `2^o(r)`.

## 15. Component-surplus pair recursion obstruction

The separate artifact `COMPONENT_SURPLUS_PAIR.md` gives the exact entropy
deficit of the two direct repair projections.  For a record `(R,I,p)` with
source `A=R union I` and target `T=R union {p}`,

\[
 2H(R,I,p)-H(A)-H(T)
 =H(I,p\mid R)-I(I;p\mid R).
\]

Thus a near-product conditional fibre maximizes rather than removes the
projection loss.  An unequal-alphabet realization of ACP Proposition 26
has rank `L/2+O(1)`, retained-target density surplus tending to `1/2`, and
conditional projection deficit `3L^2/16+L`.  Its one-slot two-record code
also has fibre `2^(L/2+O(1))`.  Hence marginal entropy and rank slicing alone
cannot preserve `|G|^2` in the component-surplus branch.  The missing term
is exactly the internal all-interval/strong-block face capacity; the planar
family is a stress test, not a counterexample to 838.

Two source outputs reduce this particular family's loss to the two blocker
labels, `2L=Theta(r)`, so the obstruction is specifically to the capped
`2^o(r)` decoder (and to the mixed source--target marginal recursion), not
to a coarse `2^o(r^2)` coefficient estimate.

## 16. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_all_interval_isoperimetry/verify_counterexample.py
python3 phase2/loop/erdos838/agent_all_interval_isoperimetry/verify_vector_recurrence.py
python3 phase2/loop/erdos838/agent_all_interval_isoperimetry/verify_low_v_fixed_gap.py
python3 phase2/loop/erdos838/agent_all_interval_isoperimetry/verify_two_record_uncrossing.py
python3 phase2/loop/erdos838/agent_all_interval_isoperimetry/verify_component_surplus_pair.py
```

The audit checks (2)--(14) exactly with Python integers for a range of `h`,
checks every interval potential in (10), verifies that the capped demand
eventually exceeds the entire maximal atomic reservoir, and checks the
enriched scalar profile (20)--(25).
The vector audit checks the exact weighted partition (34) on exhaustive
small integer arrays and verifies the rational compatible/incompatible
fixed-cell gadgets by exact convex-hull arithmetic.
