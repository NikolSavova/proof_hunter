# Coupled Pareto and two-anchor mutations on the nonstrong frontier

**Date:** 2026-08-15.  Face and endpoint counts are nonempty.

## Verdict

There is an exact strongest two-child mutation inequality, but its finite
geometry is a barrier rather than a curvature gain.  For exact endpoint
deficit

\[
 \psi_a(c)=\min_{Q,\theta:C_\theta(Q)=c}\{V(Q)-f(a)\},
 \qquad
 \Phi_a(c)=\min_{d\le c}\psi_a(d),                         \tag{1}
\]

put

\[
 K_{a,b}=\min_{c,u}\{\Phi_a(c)+\Phi_b(u)+cu\}.             \tag{2}
\]

Then the minimum face count among all physical literal strong glues with
child sizes $a,b$ is exactly

\[
 \boxed{S_{a,b}=f(a)+f(b)+K_{a,b}.}                         \tag{3}
\]

Consequently

\[
 \boxed{K_{a,b}\ge f(a+b)-f(a)-f(b),}                       \tag{4}
\]

with equality precisely when some global $(a+b)$-point minimizer occurs in
that literal-seam class.  If a global minimizer $A\prec B$ has exact profile
$(c,u)$, it satisfies the full rectangle of two-child replacements

\[
 \boxed{
 \psi_a(c)+\psi_b(u)+cu
 \le \psi_a(c')+\psi_b(u')+c'u'
 \quad\text{for every attainable }(c',u').
 }                                                           \tag{5}
\]

This is necessary and sufficient for stationarity under arbitrary
two-child replacement.  It is stronger than separate weighted-child
minimality whenever one endpoint moves left and the other right.  It is also
the end of the purely two-child algebra: every right side of (5) is an
actual planar replacement.

The exact $B(8,2)$ scan gives the sharp singleton-anchor calibration

\[
 K_{8,1}=54,
 \qquad
 \min_c\{\Phi_8(c)+c\}\text{ is attained at }(V,C)=(114,53).
                                                               \tag{6}
\]

Thus

\[
 S_{8,1}=113+1+54=168=f(9).                                \tag{7}
\]

The ordinary eight-point profile $(113,55)$ gives $169$ instead.  The true
nine-point minimum is obtained by selecting the **nonstrong flat**
eight-point child, not the ordinary minimizer.  Every hull-vertex deletion
of the stored nine-point minimizer has the exact root profile $(114,53)$.
This is planar equality in (3)--(5), not a scalar fake.

At two eight-point children the same exhaustive scan goes much farther left:

\[
 K_{8,8}=1580,
 \qquad
 S_{8,8}=1806,
 \qquad
 (V,C)=(V,U)=(255,36)                                    \tag{8}
\]

at the unique optimizing profile pair.  In comparison, the ordinary pair
has value $3251$ and the flat pair has value $3037$.  Coupling therefore
does not restore the large product $p(8)^2=3025$; it selects the all-chain
end of the frontier.

There is also an explicit nonstrong nine-point killer with

\[
                         (V,C)=(172,71).                    \tag{9}
\]

For the displayed stored minimizer profile $(168,82)$ and flat profile
$(169,76)$, at every integer sibling endpoint $t\ge1$ it gives

\[
\begin{aligned}
 (172+71t)-(168+82t)&=4-11t<0,\\
 (172+71t)-(169+76t)&=3-5t<0.                              \tag{10}
\end{aligned}
\]

Thus neither displayed nine-point profile is a weighted child optimizer
beside any nonempty sibling.  The killer, the flat witnesses, and both true
finite minimizers are all non-strong-decomposable.

No sufficient asymptotic curvature inequality results.  Equation (4) is
the only universal absolute floor furnished by two-child replacement, and
using it to prove a new lower bound for $f(a+b)$ is circular.  The finite
equalities show that a valid proof must establish new one-child planar
curvature for $\Phi$, or use a mutation outside the fixed two-child seam.

## 1. Exact two-child envelope theorem

For fixed endpoint charts, strong gluing gives

\[
 V(Q\prec R)=V(Q)+V(R)+C(Q)U(R).                         \tag{11}
\]

Minimizing the right side first over configurations with exact endpoints
$c,u$ gives

\[
 S_{a,b}=f(a)+f(b)+
 \min_{c,u}\{\psi_a(c)+\psi_b(u)+cu\}.                   \tag{12}
\]

The minimum in (12) is unchanged if $\psi$ is replaced by $\Phi$.  Indeed,
if $\Phi_a(c)$ is attained at an endpoint $d\le c$, replacing $c$ by $d$
does not increase either the deficit or the positive product.  The same
argument applies to $u$.  This proves (3).

Every strong glue in (11) is an actual $(a+b)$-point configuration, so its
face count is at least $f(a+b)$.  Taking the minimum proves (4).  Conversely,
if a global minimizer has a literal $a+b$ seam, it attains this minimum and
forces equality.  Replacing both children simultaneously by any exact
profiles proves (5).

This identifies the strongest possible statement from arbitrary two-child
mutation: a stronger numerical inequality would reject a physical profile
which realizes the right side of (12).

### Exact mixed curvature

Let

\[
 H(c,u)=\Phi_a(c)+\Phi_b(u)+cu.                            \tag{13}
\]

For any four endpoint values one has the identity

\[
\begin{aligned}
 &H(c_0,u_0)+H(c_1,u_1)-H(c_0,u_1)-H(c_1,u_0)\\
 &\hspace{35mm}=(c_0-c_1)(u_0-u_1).                       \tag{14}
\end{aligned}
\]

All unknown planar terms cancel.  Thus the only mixed curvature in the
literal-seam functional is the known bilinear product.  Any additional
lower curvature must be a theorem about at least one of the one-dimensional
frontiers $\Phi_a,\Phi_b$; it cannot be generated by rearranging the seam
identity.

## 2. Complete eight-point coupled audit

The packet-state scanner exhausts all $1{,}232{,}944$ commutation classes of
$B(8,2)$.  Because every coefficient of $V+c t$ and
$V+W+cu$ is positive, retaining the least endpoint count at each ordinary
count loses no weighted or coupled minimizer.

At integer penalty one,

\[
 \min_Q\{V(Q)+C(Q)\}=167,\qquad (V,C)=(114,53),            \tag{15}
\]

and this is the only optimizing profile.  At penalty two the minimum has
already moved to

\[
 \min_Q\{V(Q)+2C(Q)\}=218,
 \qquad (V,C)=(120,49).                                   \tag{16}
\]

Therefore the flat witness is selected exactly by the smallest possible
nonempty sibling penalty; it is not selected by any integer penalty at
least two.  The ordinary profile is beaten at every $t\ge1$ because

\[
                  (114+53t)-(113+55t)=1-2t<0.             \tag{17}
\]

For two eight-point children, direct evaluation of all ordered pairs of the
84 retained profile rows gives

\[
\begin{array}{c|c|c}
\text{left and right profiles}&K\text{-term}&S_{8,8}\\ \hline
(113,55),(113,55)&3025&3251\\
(114,53),(114,53)&2811&3037\\
(255,36),(255,36)&1580&1806.
\end{array}                                               \tag{18}
\]

The last row is the exact global minimum within the $8+8$ literal-seam
class.  The drop from the ordinary endpoint product is $1445$ faces.

## 3. The true nine-point minimizer is the singleton saturation

For a hull vertex $z$ of a point set $P$, the other labels admit an angular
order in which every triple with $z$ has the same root sign.  Writing
$Q=P-z$, the singleton-root identity is

\[
 V(P)=V(Q)+1+C_z(Q),                                      \tag{19}
\]

up to exchanging cap and cup.  This is the $b=1$ case of (11).

The stored true nine-point minimizer has three hull vertices.  Exact subset
and root-sign enumeration gives, for each of them,

\[
                   (V(Q),C_z(Q))=(114,53).                \tag{20}
\]

Hence every hull root realizes

\[
 V(P)=114+1+53=168,
 \qquad
 \{V(Q)-f(8)\}+C_z(Q)=1+53=K_{8,1}.                      \tag{21}
\]

The eight-point child in (20) is nonstrong.  The nine-point parent is also
nonstrong recursively, since no compatible full binary strong tree exists,
but it has the literal singleton root needed for (19).  This distinction is
why the coupled calculation remains valid without assuming strong
decomposability.

The flat nine-point witness has three singleton-root profiles

\[
                         (113,55),\quad(114,54),\quad(117,51). \tag{22}
\]

Each has

\[
                    \{V(Q)-113\}+C_z(Q)=55,              \tag{23}
\]

one above $K_{8,1}=54$.  Replacing its eight-point child by the physical
$(114,53)$ optimizer decreases the parent from $169$ to $168$.  Thus the
full two-child inequality rejects the flat nine-point configuration by the
sharp integer margin one.

## 4. A deeper nonstrong nine-point killer

The following Aichholzer--Aurenhammer--Krasser database record is retained
as an independent integer witness:

\[
\begin{array}{c|rrrrrrrrr}
i&0&1&2&3&4&5&6&7&8\\ \hline
x_i&65050&8768&17668&44168&50758&29668&42718&38358&39458\\
y_i&18218&288&8028&13808&15298&17348&29148&46818&65248
\end{array}                                               \tag{24}
\]

Direct hull enumeration gives face profile

\[
                         (9,36,84,42,1),                  \tag{25}
\]

so $V=172$.  Exhausting all generic projection chambers of the displayed
realization gives minimum cap profile

\[
                         (9,36,24,2),                     \tag{26}
\]

so $C=71$.  Equations (10) follow immediately.  In particular the finite
$9+9$ values for the displayed profiles are

\[
\begin{array}{c|c}
\text{profile used on both sides}&V(Q)+V(R)+C(Q)U(R)\\ \hline
(168,82)&7060\\
(169,76)&6114\\
(172,71)&5385.
\end{array}                                               \tag{27}
\]

The last line is only an upper bound on the full $9+9$ seam minimum because
$B(9,2)$ has not been exhausted.  It is sufficient to prove that coupling
does not rescue either displayed endpoint profile.

There is a realization-scope caveat for the ordinary minimizer.  The value
$82$ is the minimum over the 72 affine projection chambers of the stored
rational realization, whereas the realization-independent audit presently
only proves $p(9)\ge72$.  Thus the first inequality in (10) is asserted for
the displayed profile.  Uniformly over every realization, the same killer
beats an ordinary minimizer whenever $t\ge5$.

## 5. Induced two-anchor/bipartition barrier

There is a more restrictive physical mutation which uses only the two
induced children already present in a configuration $P$.  For an ordered
bipartition $P=R\sqcup S$, independently rechart the displayed rational
realizations of $P[R]$ and $P[S]$ and strongly glue them.  If

\[
 \pi(T)=\min_\theta C_\theta(P[T]),                       \tag{28}
\]

reflection gives the same minimum for cups, and the best such mutation has

\[
 M_P(R,S)=V(P[R])+V(P[S])+\pi(R)\pi(S).                  \tag{29}
\]

Every global minimizer must satisfy $V(P)\le M_P(R,S)$ for every ordered
bipartition.  Exhausting all $2^n-2$ bipartitions gives

\[
\begin{array}{c|c|c|c}
P&V(P)&\min M_P&\#\text{ ordered minimizers}\\ \hline
\text{ordinary }8&113&113&16\\
\text{flat }8&114&113&12\\
\text{ordinary }9&168&168&6\\
\text{flat }9&169&169&10.
\end{array}                                               \tag{30}
\]

Thus the induced mutation detects the ordinary nonminimality of the flat
eight-point witness, but it does **not** detect the flat nine-point witness:
that configuration is stationary under every one of these induced
two-child mutations.  The successful margin-one move in (23) must import a
different eight-point order type.

The scan in (30) ranges over every projection direction of each displayed
induced realization.  It does not claim to exhaust all realization-space
components of every induced order type.  This limitation only weakens the
barrier; the unrestricted exact inequality is already (5), which does find
the external replacement.

## 6. Nonstrong audit and consequence

For each of the ordinary and flat eight-point configurations, and for the
ordinary, flat, and killer nine-point configurations, the verifier exhausts
every leaf permutation, every recursive cut, and both mirror signs.  No
strong decomposition exists.  After a failed search the caches contain all
ordered nonempty subsets:

\[
                   109{,}600\quad(n=8),
 \qquad            986{,}409\quad(n=9).                  \tag{31}
\]

The finite conclusion is sharp:

1. an ordinary minimizer need not minimize the weighted child functional;
2. the weighted optimizer can be a genuinely nonstrong flat point;
3. that flat point can saturate the exact global recurrence one size later;
4. another nonstrong point can then move the envelope farther left; and
5. the bilinear seam supplies exactly (14), with no hidden planar curvature.

Therefore a half-coefficient closure cannot follow from two-child
stationarity alone.  It needs a new quantitative lower theorem for the
one-child deficits $\Phi_a$, or a physical mutation which changes the seam
and is not represented by (11).

## 7. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_coupled_pareto_two_anchor/verify_coupled_pareto_two_anchor.py
```

The checker uses exact integer and rational arithmetic.  It:

1. recompiles the independent packet-state scanner and exhausts all
   $1{,}232{,}944$ classes of $B(8,2)$;
2. verifies (6)--(8), (14)--(18), and the unique optimizing profiles;
3. directly enumerates every face and projection chamber of all five
   rational configurations;
4. verifies every hull-root sign and the singleton profiles (20)--(23);
5. exhausts every stored-realization induced bipartition in (30); and
6. exhausts all ordered recursive strong-tree states for all five
   configurations.

The machine-readable coordinates and expected values are in
`coupled_pareto_certificate.json`.  The verifier prints PASS.
