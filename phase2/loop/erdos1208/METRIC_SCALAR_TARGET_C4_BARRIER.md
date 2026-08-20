# Metric scalar excess: exact target-`C_4` split and a genuine barrier

## 1. Verdict

Target wedges and their induced eight-endpoint parallelograms control only
one exact part of scalar excess.  The complementary **bi-matching excess**
can contain large-area, squareclass-transverse collisions even when both the
source graph and its clean translated image have no wedges or four-cycles.

This is not merely an abstract graph obstruction.  The companion verifier
certifies a 74-point integral distance-Sidon set, one clean fibre of size 12,
and one scalar-charge bucket of load 12 such that all 132 ordered
off-diagonal collisions in the bucket are

* four-distinct-edge;
* squareclass-transverse;
* above the adaptive target-determinant cutoff; and
* source-and-clean-target bi-matching.

Both wedge counts, both `C_4` counts, and the number of nontrivial
parallelograms among its twelve source pair sums are zero.  Consequently no
collisionwise charge of the surviving scalar core to target `C_4`'s or to
the parallelograms induced by those `C_4`'s can be valid.

The construction does **not** violate the proposed aggregate scalar bound:
its excess is tiny compared with `Nk^3`.  It is a sharp barrier to the
proposed proof mechanism and identifies the exact new term that must be
bounded.

## 2. Exact bucket decomposition

Fix `q`, and for a scalar key `lambda` put

\[
 B_{q,\lambda}
 =\{(s,t)\in H_q\times\Sigma:
        \delta(s)+18\delta(t)=\lambda\},
 \qquad L_{q,\lambda}=|B_{q,\lambda}|.                    \tag{2.1}
\]

Distance-Sidonicity makes `delta` injective.  Hence both coordinate
projections of one bucket are injective: a source `s` determines `t`, and a
target `t` determines `s`.  Let `F` be the graph of source endpoint edges in
the bucket and let `T=tau_q(F)` be its clean translated image.

Write

\[
 W_S=\sum_x{d_F(x)\choose2},\qquad
 W_T=\sum_x{d_T(x)\choose2}.                              \tag{2.2}
\]

Two different source edges cannot share both endpoints, and the
star-to-matching theorem says that a source-overlap pair cannot also be a
target-overlap pair.  Therefore the ordered off-diagonal pairs in the
bucket split exactly as

\[
 \boxed{
 L(L-1)=2W_S+2W_T+B^{\rm bi}_{q,\lambda},}                \tag{2.3}
\]

where `B^bi` counts ordered pairs whose source edges are disjoint and whose
clean target edges are also disjoint.

Summing buckets gives the exact scalar-excess identity

\[
 \boxed{
 \mathcal M_{q,18}-Nh_q
 =2\sum_\lambda(W_S+W_T)
  +\sum_\lambda B^{\rm bi}_{q,\lambda}.}                 \tag{2.4}
\]

The wedge/`C_4` mechanism from
`MATCHING_BLOCK_TRANSLATION_LEVERAGE.md` applies to the first sum.  In
particular, target wedges expose realized outer differences, with exact
second moment `2W_T+8C_4(T)`, and every target four-cycle induces an
eight-distinct-source-endpoint relation

\[
 s_{xy}+s_{x'z}=s_{xz}+s_{x'y}.                            \tag{2.5}
\]

Equation (2.4) shows precisely why this cannot be the whole proof: it says
nothing about the bi-matching term.

## 3. A genuine large-area transverse bi-matching channel

The certificate starts from the following twelve representations of one
quadratic-form value:

\[
 |u_i|^2+18|v_i|^2=23716.                                 \tag{3.1}
\]

\[
\begin{array}{c|c|c|c}
i&u_i&v_i&|v_i|^2\\ \hline
1&(96,118)&(4,4)&32\\
2&(100,114)&(2,6)&40\\
3&(105,109)&(3,6)&45\\
4&(96,116)&(3,7)&58\\
5&(91,117)&(4,9)&97\\
6&(99,109)&(7,8)&113\\
7&(89,117)&(6,9)&117\\
8&(98,108)&(6,10)&136\\
9&(99,107)&(4,11)&137\\
10&(82,120)&(0,12)&144\\
11&(91,111)&(2,13)&173\\
12&(84,116)&(3,13)&178
\end{array}                                                \tag{3.2}
\]

The twelve target norms in the last column have distinct squarefree
kernels.  The target vectors are pairwise nonparallel.

Take anchors `b=(0,0)` and

\[
 a=q=(1000003,1000033).                                   \tag{3.3}
\]

For each row choose an integral source base point `c_i`, put
`d_i=c_i+100u_i`, choose an integral clean-target point `e_i`, and set

\[
 f_i=c_i+d_i+q-e_i.                                       \tag{3.4}
\]

Finally choose an integral scalar-target base point `g_i` and put
`h_i=g_i+100v_i`.  The verifier stores explicit choices of the free base
points.  They were selected generically, then every assertion below was
checked exactly; no probabilistic claim remains in the certificate.

Equation (3.4) gives

\[
 e_i+f_i=c_i+d_i+q,                                       \tag{3.5}
\]

so `s_i=c_i+d_i` lies in `H_q` and its clean partner is the edge
`e_if_i`.  All 74 points are distinct and all 2,701 squared distances are
distinct.  The three collections

\[
 \{c_id_i\},\qquad\{e_if_i\},\qquad\{g_ih_i\}            \tag{3.6}
\]

are pairwise endpoint-disjoint matchings.  Moreover the fibre `H_q` consists
of exactly the twelve displayed sources.

After the factor-100 scaling, (3.1) says

\[
 |c_i-d_i|^2+18|g_i-h_i|^2=237160000                     \tag{3.7}
\]

for every `i`.  Thus these twelve records form one complete scalar bucket,
giving `12*11=132` ordered off-diagonal collisions.

The adaptive cutoff is

\[
 \left\lfloor{N\over h_q}\right\rfloor
 =\left\lfloor{2701\over12}\right\rfloor=225.            \tag{3.8}
\]

The minimum target doubled area among the 66 unordered collision pairs is

\[
 \min_{i<j}|2\det(100v_i,100v_j)|=20000>225.               \tag{3.9}
\]

Distinct target squareclasses make every pair squareclass-transverse.  All
four scalar edges in an off-diagonal collision are distinct, indeed their
endpoint roles are disjoint.  Hence the entire bucket lies in the exact
large-area transverse core left by the proved scalar reductions.

On the other hand `F` and `tau_q(F)` are matchings, so

\[
 W_S=W_T=C_4(F)=C_4(T)=0,\qquad
 B^{\rm bi}_{q,237160000}=132.                             \tag{3.10}
\]

The twelve source pair sums also have distinct two-sums, so there is no
nontrivial source parallelogram to receive a fallback charge.

## 4. Consequence for the aggregate theorem

The target-`C_4` route remains useful for the wedge-covered part of (2.4),
but the aggregate scalar conjecture now has a sharper irreducible target:

\[
 \boxed{
 \sum_{q,\lambda}
 B^{\rm bi,large,tr}_{q,\lambda}
 \le m^{o(1)}Nk^3.}                                       \tag{4.1}
\]

Here the superscript restricts to four-edge, squareclass-transverse
collisions with target doubled area greater than `N/h_q`.  The certificate
shows that (4.1) cannot be proved by assigning each collision to a source
or clean-target wedge, an induced target four-cycle, or its source
parallelogram.

What remains available in the example, and therefore in a viable proof, is
the scalar-target pair itself: the 132 collisions expose all cross pairs
among the twelve distinct nonparallel vectors `v_i`.  A successful global
charge must retain those determinant-decorated scalar-target cross pairs,
or exploit endpoint escape across many fibres, rather than passing only
through `tau_q(F)`.

Run `verify_metric_scalar_target_c4_barrier.py` for the exact certificate.
