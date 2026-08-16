# Two synchronized reset chains: full-ACP history barrier and the exact actual-incidence residue

## Verdict

Two fixed-root reset chains can be synchronized projectively while retaining
the complete ACP repair tuple and a common terminal blocker alphabet.  Every
monotone subsequence is then a genuine exterior-repair history, and two
chains carry quadratic logarithmic **history** entropy.  Nevertheless the
whole construction has, up to the fixed outer base, exactly the face complex
of an arbitrary prescribed planar order type.  On the coefficient-half
upper construction, any two-face decoder for pairs of histories has fibre

\[
                         2^{(1-o(1))(\log n)^2}.          \tag{1}
\]

This is a sharp counterexample to a history-counted two-chain telescope.
It is not an EIC counterexample: histories repeatedly traverse the same
actual incidences.  If the chains have $N_1,N_2$ states and common
alphabet $Y$, then their selected terminal incidence support has exactly

\[
                         |Y|(N_1+N_2)                    \tag{2}
\]

records.  Even after every later tip of its **own** chain is also admitted
as a blocker, the support is at most

\[
 {N_1\choose2}+{N_2\choose2}+|Y|(N_1+N_2),              \tag{3}
\]

and for fixed outer cores it injects into ordinary rank-two faces by

\[
            (R\cup\{x\},p)\longmapsto\{x,p\}.           \tag{4}
\]

Thus first divergence and chronology create no additional selected mass.
If every later tip in the combined chronology is admitted, replace the
first two terms by ${N_1+N_2\choose2}$; the conclusion is unchanged.

Allowing the retained outer core $R$ to vary does not by itself create a
residue.  Precisely, if at most $\Lambda$ distinct cores support the same
ordered ear--blocker pair $(x,p)$, then (4) has load at most $\Lambda$, and

\[
                         |E|\leq\Lambda V(P).             \tag{5}
\]

But high $\Lambda$ is harmless once either mark is retained.  For all
singleton-ear records sharing one ear label $x$, mapping to the repaired
target has load at most its rank: given $T$ and a choice $p\in T$, the core
$R=T-\{p\}$ and source $R\cup\{x\}$ are forced.  Dually, for records sharing
one blocker $p$, mapping to the source has load at most its rank.  If all
sources and targets have rank at most $r+1$, then

\[
             |E_x|\leq(r+1)V(P),\qquad
             |E^p|\leq(r+1)V(P).                        \tag{5a}
\]

For a literally fixed pair $(x,p)$ both maps are injective, regardless of
how incompatible the cores are.  Thus the first noncircular residue must
vary **both** marks through large alphabets, or have hidden ears of rank
greater than one whose full set identity also varies.  It is not a fixed-
pair crossing-core problem.

There is a complementary exact same-target theorem.  If two singleton-ear
fibres share the marked repaired target $(T,p)$, their Cartesian product
maps to the two ordinary faces

\[
                         \left(T,\{x_1,x_2\}\right)       \tag{6}
\]

with global load at most $|T|$.  Hence

\[
 \sum_{(T,p)}|X_1(T,p)|\,|X_2(T,p)|
                         \leq (r+1)V(P)^2                \tag{7}
\]

when repaired targets have rank at most $r+1$.  The only two-chain pairs
not covered by (7) have different marked terminal targets, hence different
retained outer states.  Equations (5), (5a), and (7) isolate the same
residue from the one-record and two-record sides: simultaneous ear/blocker
variation together with different retained outer states.

Exact verifier:

    python3 phase2/loop/erdos838/agent_one_sided_reflection/verify_two_chain_synchronized_acp.py

## 1. A projectively synchronized full-ACP construction

Let $Q=(q_0,\ldots,q_{m-1})$ be any rational general-position point set,
indexed by increasing first coordinate, $q_i=(a_i,b_i)$.  Choose a
rational $M$ such that

\[
                         b_i+Ma_i
\]

is strictly increasing.  Choose $C$ sufficiently large and put

\[
 A_i={C\over2}-a_i,\qquad
 B_i=b_i+Ma_i-{C\over2}.                                \tag{8}
\]

We may require $A_i>0>B_i$.  Thus $A_i$ strictly decreases, $B_i$
strictly increases, and $A_i-B_i>0$.  Normalize the fixed roots as

\[
                         u=(0,0),\qquad v=(1,0)
\]

and set

\[
 z_i=\left({A_i\over A_i-B_i},-{1\over A_i-B_i}\right). \tag{9}
\]

The map from $q_i$ to $(A_i,B_i)$ is affine and invertible, and (9) is
one projective collineation whose homogeneous denominators are positive.
It preserves the complete oriented matroid, up to one global sign.  In
particular

\[
                         V(\{z_i\})=V(Q).                 \tag{10}
\]

The dominance/containment identity is

\[
 z_i\in\operatorname{int}\operatorname{conv}\{u,v,z_j\}
 \quad\Longleftrightarrow\quad A_i>A_j, B_i<B_j.        \tag{11}
\]

Therefore every earlier tip lies strictly inside the rooted triangle of
every later tip.

Partition the first $2N$ labels into two ordered subsequences $X^1,X^2$
of size $N$, and let the final $D=m-2N$ labels be $Y$.  Let $R$ be
any fixed rational convex polygon above $uv$, with $uv$ as an edge and
with all $z_i$ in its outward edge cone.  The choice $A_i>0>B_i$ puts
every $z_i$ below $uv$ with first coordinate in $(0,1)$, so such an
$R$ exists.  Define, for $z^c_t\in X^c$,

\[
 \mathcal A^c_t=R\cup\{z^c_t\}.                         \tag{12}
\]

For every later tip $p$, in particular every $p\in Y$,

\[
 \begin{aligned}
 \mathcal A^c_t&\text{ is an ordinary convex source},\\
 p&\text{ is exterior/outward for }\mathcal A^c_t,\\
 T^c_{t,p}:=\operatorname{ext}(\mathcal A^c_t\cup\{p\})
     &=R\cup\{p\},\\
 I^c_t:=\mathcal A^c_t-T^c_{t,p}&=\{z^c_t\}.
 \end{aligned}                                         \tag{13}
\]

Indeed $z^c_t$ is strictly inside the triangle $uvp$, whereas
$R\cup\{p\}$ is convex.  Thus (13) is the full ACP tuple, not a syntactic
tree edge.  The same $Y$ blocks every selected state in both chains, and
every reset retains its entire earlier prefix in the full hidden triangle
pocket.

The synchronization is maximally hostile to guarded multiplication.  For
any two distinct cloud labels $z_i,z_j$, the earlier lies inside the
rooted triangle of the later, so

\[
                         R\cup\{z_i,z_j\}
\]

is nonconvex.  A convex face retaining the outer base contains at most one
chain or blocker label.  Cross-chain first divergence cannot be encoded by
a guarded mixed face.

Finally put $P=R\cup\{z_0,\ldots,z_{m-1}\}$.  Intersecting an ordinary
face of $P$ with the tip cloud gives an ordinary face of the tip cloud.
Consequently

\[
                         V(P)\leq2^{|R|}V(Q).             \tag{14}
\]

The repair geometry has added only the fixed-base factor; it has not
created a hidden mixed bank.

## 2. Why the history theorem is false

Fix $h\leq N$.  Every increasing $h$-subset

\[
                         i_1<\cdots<i_h
\]

of one chain and every $y\in Y$ give the genuine history

\[
 \mathcal A_{i_1}\xrightarrow{z_{i_2}}\mathcal A_{i_2}
 \xrightarrow{z_{i_3}}\cdots
 \xrightarrow{z_{i_h}}\mathcal A_{i_h}
 \xrightarrow{y}R\cup\{y\}.                            \tag{15}
\]

Every arrow in (15) is an actual exterior repair of the form (13).  Hence
one chain has

\[
                         D{N\choose h}                   \tag{16}
\]

histories and an ordered pair, one from each chain, has

\[
                         D^2{N\choose h}^2.              \tag{17}
\]

If such pairs are sent to two ordinary faces, pigeonhole and (14) force
maximum fibre at least

\[
 {D^2{N\choose h}^2\over 2^{2|R|}V(Q)^2}.               \tag{18}
\]

Take the established coefficient-half upper construction for $Q$, split
its ordered labels into three linear-sized parts, take
$h=\lfloor\log_2m\rfloor$, and let $|R|=O(\log m)$.  Then

\[
 \log_2{N\choose h}=(1-o(1))(\log_2m)^2,\qquad
 \log_2V(Q)\leq(1/2+o(1))(\log_2m)^2.
\]

Substitution in (18) gives (1).  A first-divergence descriptor contains
only a position and two labels, hence $O(\log m)$ bits; even giving this
descriptor to the decoder for free does not change (1).

The chronology collision is equally explicit.  If chain indices begin at
zero, a fixed terminal record $(\mathcal A_t,y)$ is reached by

\[
                         {t\choose h-1}                  \tag{19}
\]

different length-$h$ histories.  At the last state this already has
quadratic logarithmic size.  These histories are not new selected repair
records, and (19) must not be charged as EIC demand.

## 3. Actual support collapses to rank two

Consider first a fixed retained core $R$.  A singleton-chain record is

\[
 e=(R\cup\{x\},p),\qquad
 \operatorname{ext}(R\cup\{x,p\})=R\cup\{p\}.           \tag{20}
\]

The chronology makes $x$ the earlier label and $p$ the later label.
Thus

\[
                         e\mapsto\{x,p\}                 \tag{21}
\]

is injective, and its output is always an ordinary rank-two face.  This
proves (2)--(4), including all internal transitions if they are selected.
For a pair of actual records, one from each chain, applying (21) in each
coordinate gives an injective two-face code.

There is also a direct terminal code.  For
$(\mathcal A^1_i,y_a),(\mathcal A^2_j,y_b)$, output

\[
             \bigl(\{z^1_i,z^2_j\},\{y_a,y_b\}\bigr).    \tag{22}
\]

The first face recovers the two states from their chain colours.  The
second recovers the ordered blockers up to swapping, so (22) has load at
most two, and load one when the two records use the same blocker.  This is
the exact one-step positive boundary: stacking histories, not terminal
repair geometry, caused (18).

Now allow the retained core to vary and write records canonically as

\[
                         e=(R,x,p).                       \tag{23}
\]

Let

\[
 \lambda(x,p)=|\{R:(R,x,p)\in E\}|,\qquad
 \Lambda=\max_{x,p}\lambda(x,p).                        \tag{24}
\]

Here the fixed chain chronology determines which member of the unordered
pair is the ear and which is the blocker; equivalently, $\lambda$ is the
fibre of (21) itself.  The same map (21) therefore has fibre exactly
$\lambda(x,p)$.  Since every pair of
labels is an ordinary face,

\[
 |E|=\sum_{\{x,p\}}\lambda(x,p)
       \leq\Lambda {n\choose2}\leq\Lambda V(P),          \tag{25}
\]

which proves (5).  Notice that the pair of ordinary faces

\[
                         (R\cup\{x\},R\cup\{p\})         \tag{26}
\]

recovers the complete record injectively.  Thus a high value of
$\Lambda$ is not an information ambiguity, and in the fixed-mark slices it
is not a one-face obstruction either.

> **Theorem 3 (fixed-mark core compression).** Suppose every source and
> repaired target in a singleton-ear record family has rank at most $r+1$.
> For a fixed ear label $x$, the target map has load at most $r+1$:
> 
> \[
>                        (R,x,p)\longmapsto T=R\cup\{p\}. \tag{26a}
> \]
> 
> For a fixed blocker label $p$, the source map has load at most $r+1$:
> 
> \[
>                        (R,x,p)\longmapsto A=R\cup\{x\}. \tag{26b}
> \]
> 
> If both $x,p$ are fixed, either map is injective.

**Proof.** Given $T$ and the globally fixed $x$, choose the marked
blocker $p\in T$.  There are at most $|T|\leq r+1$ choices, after which
$R=T-\{p\}$ and $A=R\cup\{x\}$ are forced.  The source argument is
dual: given $A$ and fixed $p$, choose $x\in A$, then
$R=A-\{x\}$ and $T=R\cup\{p\}$ are forced.  With both marks fixed no
choice remains.  Notice that convexity, core compatibility, and the hiding
circuit are not used beyond certifying that $A,T$ are ordinary faces.
QED.

More generally, if $X,Y$ are the ear and blocker alphabets of $E$,
Theorem 3, (25), and the raw source-degree bound give the exact menu

\[
 |E|\leq
 \min\bigl\{(r+1)|X|,(r+1)|Y|,\Lambda,D\bigr\}V(P).     \tag{26c}
\]

Therefore failure of a $D^{1-\epsilon}$ charge requires simultaneously

\[
 |X|,|Y|>{D^{1-\epsilon}\over r+1},\qquad
 \Lambda>D^{1-\epsilon}.                               \tag{26d}
\]

A fixed pair with arbitrarily many mutually incompatible cores is already
paid by its pairwise distinct repaired targets.  Circuit localization can
only become relevant after both marks vary.

## 4. Same marked targets have an exact two-chain code

For a repaired target $T$ and its marked blocker $p\in T$, put

\[
 R=T-\{p\},\qquad
 X_c(T,p)=\{x:R\cup\{x\}\text{ is a selected chain-}c
          \text{ source repaired by }p\text{ to }T\}.    \tag{27}
\]

For every $x_1\in X_1(T,p)$, $x_2\in X_2(T,p)$, output (6).  Both
coordinates are ordinary faces.  Given the output, there are at most
$|T|$ possible marks $p$, and then $R,x_1,x_2$ and both records are
determined; the two disjoint chain alphabets determine the assignment of
$x_1,x_2$.  Summing over all outputs proves (7).  Without recoverable chain
colours the same proof has the harmless factor two.

Equivalently, if

\[
 E_c=\sum_{(T,p)}|X_c(T,p)|,\qquad
 \theta={\sum_{(T,p)}|X_1(T,p)||X_2(T,p)|\over E_1E_2}, \tag{28}
\]

then

\[
                         \theta E_1E_2\leq(r+1)V(P)^2.   \tag{29}
\]

Large common-target overlap is therefore already paid.  If `theta` is
small, almost every cross-chain pair has different marked targets and hence
different retained outer states.  Together, (26c) and (29) isolate the only
remaining two-chain problem: off-diagonal interaction in which the ear and
blocker marks both vary through large alphabets (or the hidden ear has rank
greater than one and varies as a set).  Projective universality of the reset tips alone says
nothing about that interaction.

## 5. What this removes from the proof search

The following proposed mechanisms are now ruled out or closed exactly.

* Counting monotone histories, even when every arrow is a genuine ACP
  repair and both chains share all terminal blockers, overcounts selected
  incidence demand by a quadratic logarithmic factor.
* First-divergence and reset-depth tags do not fix that overcount: they
  distinguish traversals of the same incidence support.
* Fixed-core singleton chains require no higher mixed-face theorem; their
  complete actual support is already a rank-two face bank.
* Fixed-ear families map to repaired targets with rank load, and fixed-
  blocker families map to sources with rank load.  In particular a fixed
  ear--blocker pair remains harmless even across maximally incompatible
  outer cores.
* Same marked terminal targets across two chains have the two-face decoder
  (6), with only the target-rank loss.

The surviving statement must have simultaneous large variation of both
marks together with different outer cores/marked targets, or non-singleton
hidden ears varying as sets.  This is the genuine quadratic crossing-core atom already
visible in the ACP split; it cannot be reduced to one fixed pair or another
theorem about unlabelled reset chains.
