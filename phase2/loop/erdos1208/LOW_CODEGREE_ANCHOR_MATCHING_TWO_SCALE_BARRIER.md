# Low source codegree: exact two-scale reduction and a matching-anchor barrier

## 1. Outcome

Fix a dyadic clean-fibre group and write

\[
 c(p)=\#\{q:s,s'\in H_q\},\qquad p=(s,s'),\ s\ne s'.       \tag{1.1}
\]

The part with `c(p)<k` has a sharp pointwise reduction to the raw
opposite-scale distance-gap multiplicity.  If

\[
 C_{<k}(r)=
 \sum_{\substack{p=(s,s'):\
        \delta(s)-\delta(s')=-18r\\c(p)<k}}c(p),          \tag{1.2}
\]

then

\[
 \boxed{C_{<k}(r)\le (k-1)R_D(-18r).}                    \tag{1.3}
\]

Consequently the exact remaining bridge for this band is the genuinely
two-scale estimate

\[
 \boxed{
 \sum_{r:U_L(r)\ge T}R_D(-18r)
 \ \ll\ {N(H_*+k^3)\over kT}.}                           \tag{1.4}
\]

Indeed, (1.3) and (1.4) give the required reciprocal tail
`N(H_*+k^3)/T`.  Formula (1.4) keeps the determinant-qualified target gap
`r` and the raw source gap `-18r`; neither marginal theorem proved so far
contains this alignment.

There is no pointwise power saving in (1.3), even for literal matching
anchor graphs.  For arbitrarily large `k` there are polynomial-height
integral distance-Sidon sets, a nonzero `r`, and an ordered source pair
`p` such that

\[
 \begin{gathered}
 R_D(-18r)=1,\qquad c(p)=\Theta(k)<k,\qquad
 C_{<k}(r)=c(p)=\Theta(k),                                \tag{1.5}\\
 U_N(r)=\Theta(k),\qquad W_{r,N}=\Theta(k^2),             \tag{1.6}
 \end{gathered}
\]

and the entire anchor graph representing `Q_p` is a matching.  The two
target edges belonging to `s` and `s'` are disjoint for every record.  Thus
even exact matching anchors and determinant-rich target endpoints do not
save `k^epsilon` at one gap.  Any proof of (1.4) must aggregate over many
`r`, or exploit a global resource which the one-gap planting consumes.

This construction is a barrier, not a counterexample to (1.4): at
`T=Theta(k)` the right side of (1.4) is much larger than its one planted
source-gap representation.

## 2. The exact low-band reduction

Let `Sigma` be the unordered pair-sum set and let `D=delta(Sigma)`.  Since
`A` is distance-Sidon, `delta:Sigma->D` is injective.  Therefore

\[
 R_D(z)=\#\{(s,s')\in\Sigma^2:
                   \delta(s)-\delta(s')=z\}.             \tag{2.1}
\]

There are exactly `R_D(-18r)` ordered source pairs in (1.2).  Each has
integer codegree at most `k-1`, proving (1.3) term by term.  Summing over

\[
 S_T=\{r:U_L(r)\ge T\}                                   \tag{2.2}
\]

gives the identity-preserving reduction

\[
 \sum_{r\in S_T}C_{<k}(r)
 \le (k-1)\sum_{r\in S_T}R_D(-18r).                      \tag{2.3}
\]

The target endpoint-wedge theorem controls the first marginal through
`|S_T|`, and the source moment controls sums over all source gaps.  Neither
controls the restricted sum on the right of (2.3).  This is exactly the
target/source anti-correlation still missing in the low band.

## 3. Exact endpoint structure of anchor stars

The matching obstruction below is preceded by two useful exact lemmas.
Fix `p=(s,s')` and orient the unique anchor of `q in Q_p` as

\[
 q=a_q-b_q.                                               \tag{3.1}
\]

For either role `z in {s,s'}`, write `E(z+q)` for its clean target edge.

### 3.1 A fixed second anchor

Suppose `q_i=a_i-b` have a common second anchor.  Then, for fixed `z`, the
target edges `E(z+q_i)` are pairwise vertex-disjoint.

Indeed, if two target edges were `{x,u_i}` and `{x,u_j}`, subtraction of
their pair-sum equations would give

\[
 u_i-u_j=a_i-a_j.                                        \tag{3.2}
\]

Uniqueness of directed point differences gives `u_i=a_i,u_j=a_j`, which
violates the six-distinct condition of both clean rows.

### 3.2 A fixed first anchor

Suppose instead `q_i=a-b_i`.  For fixed `z`, put

\[
 T_i(z)=\{b_i\}\cup E(z+q_i).                            \tag{3.3}
\]

Every triple has point sum `a+z`.  Two such triples which meet are equal:
cancel a common point and use uniqueness of unordered pair sums.  Distinct
triples are consequently disjoint.  An equal triple has at most three
preimages, because its distinguished point `b_i` has only three choices.

It follows that the records in a fixed-first-anchor star can be 3-coloured
so that the triples (3.3) in one role are pairwise disjoint in every colour.
Colouring independently in the `s` and `s'` roles gives nine classes which
are simultaneously disjoint in both roles.

### 3.3 A matching anchor graph has no target replacement

If the full anchor graph of `Q_p` is a matching, then

\[
 E(s+q)\cap E(s'+q)=\varnothing\qquad(q\in Q_p).          \tag{3.4}
\]

To see this, take `q=a-b` and suppose the two target edges are `{x,u}` and
`{x,v}`.  The clean equations imply

\[
 s+(a-x)=b+u,\qquad s'+(a-x)=b+v.                        \tag{3.5}
\]

The same six points show that these two rotated rows are clean.  Hence
`a-x in Q_p`, represented by anchor `(a,x)`.  This anchor shares `a` with
`(a,b)`, contradicting matching.  Thus a literal matching lies entirely
in the nonreplacement branch.  The construction below respects (3.4).

## 4. A literal matching construction

Choose one source edge pair `{C,D}`, `{E,F}` and write

\[
 s_0=C+D,\qquad s_1=E+F.                                 \tag{4.1}
\]

For `1<=j<=Q`, choose independent points `A_j,B_j,X_j,Y_j`, put

\[
 q_j=A_j-B_j,                                             \tag{4.2}
\]

and define two further points

\[
 U_j=s_0+q_j-X_j,\qquad V_j=s_1+q_j-Y_j.                 \tag{4.3}
\]

Then

\[
 s_0+q_j=X_j+U_j,\qquad s_1+q_j=Y_j+V_j.                \tag{4.4}
\]

After generic specialization both rows are clean.  All `2Q` anchor
endpoints are different, so the prescribed anchors `{A_j,B_j}` form a
matching.  More is true: one can specialize so that

\[
 Q_{(s_0,s_1)}=\{q_1,\ldots,q_Q\}.                       \tag{4.5}
\]

There is no hidden formal common translation.  Treating the coordinates
of `C,E,A_j,B_j,X_j,Y_j` as independent and writing
`D=C+v_0,F=E+v_1`, coefficient comparison in the two equations

\[
 s_0+(P-P')=R+R',\qquad
 s_1+(P-P')=S+S'                                         \tag{4.6}
\]

shows that their only simultaneous identities are

\[
 (P,P';R,R';S,S')=(A_j,B_j;X_j,U_j;Y_j,V_j).            \tag{4.7}
\]

Every other candidate (4.6) is a nonzero linear polynomial condition and
is excluded in the finite-avoidance specialization.  Thus the *entire*
anchor graph is the prescribed matching, not merely a selected subgraph.

## 5. Aligning the two scalar scales

Fix `C_0>0`, put

\[
 r=-4(C_0+1),\qquad K=36(C_0+1),                          \tag{5.1}
\]

and choose

\[
 v_0=(K-t,t+1),\qquad v_1=(K-t-1,t).                    \tag{5.2}
\]

Then

\[
 |v_0|^2-|v_1|^2=2K=-18r.                               \tag{5.3}
\]

Independently plant `T` target records.  From a common point `Z`, take
first-edge vectors

\[
 a_l=(C_0,T_l),                                          \tag{5.4}
\]

and at independent centres take partner-edge vectors

\[
 b_l=(C_0+2,T_l).                                        \tag{5.5}
\]

They satisfy

\[
 |a_l|^2-|b_l|^2=r,qquad
 |2\det(a_l,b_l)|=4|T_l|.                                \tag{5.6}
\]

Choose distinct polynomial-size `T_l>N/4`, with their fixed edge norms all
different.  Then all `T` records are counted by `U_N(r)`, and their first
edges form a star, so

\[
 U_N(r)\ge T,\qquad W_{r,N}\ge {T\choose2}.              \tag{5.7}
\]

Exclude every unintended equation

\[
 \delta(e)-\delta(e')=-18r.                              \tag{5.8}
\]

The prescribed source pair is the only formal identity of this type, so
the specialization can have

\[
 R_D(-18r)=1.                                             \tag{5.9}
\]

Take `Q,T` proportional to `M`.  The point count is

\[
 k=4+6Q+(1+3T)=6Q+3T+5=\Theta(M).                       \tag{5.10}
\]

Equations (4.5), (5.3), and (5.9) now give

\[
 C_{<k}(r)=Q=\Theta(k)R_D(-18r),                         \tag{5.11}
\]

while (5.7) supplies determinant-qualified target richness of order `k`.
This proves the sharpness assertions (1.5)--(1.6).

## 6. Polynomial-height specialization

All points in Sections 4--5 are affine forms in `O(k)` free integer point
variables.  The prescribed identities (4.4), (5.3), and (5.6) hold
formally.  The bad events are:

* a repeated point or a failure of six-distinctness;
* an unintended equal squared distance;
* an unintended equal disjoint triple sum, including an extra common
  translation in (4.5); and
* an unintended occurrence of the fixed gap (5.8).

After the coefficient checks above, every bad event is the zero set of a
nonzero polynomial of degree at most two.  There are at most `O(k^6)` of
them.  Their product is a nonzero polynomial of degree `O(k^6)`.  The grid
nonvanishing lemma therefore supplies an integral specialization from a
grid of polynomial side length.  The fixed vectors (5.2), (5.4), and
(5.5) also have polynomial coordinates.  Hence the final set has
polynomial height and is genuinely integral distance-Sidon.

This argument may also exclude all unintended equal triple sums.  The
total clean mass of the construction is then `Theta(Q)=Theta(k)`; the
unavoidable rotations of each prescribed triple equality contribute only
a constant number of rows.

## 7. Exact finite certificate

The verifier performs two independent audits.

First, on the 22-point transverse-closure witness it exhaustively checks
the fixed-first- and fixed-second-anchor lemmas.  Its profile is

\[
 (\#p,\#\text{incoming stars},\#\text{outgoing stars},
   \max d^-,\max d^+,\max\text{ triple load})
 =(2276,8,388,2,3,3).                                    \tag{7.1}
\]

Second, it constructs a 62-point specialization and enumerates every
clean fibre.  It finds exactly six common translations for the planted
source pair, verifies that their twelve anchor endpoints are distinct,
and checks

\[
 (c(p),R_D(-18r),U_N(r),W_{r,N},r)=(6,1,7,21,-4004).    \tag{7.2}
\]

All 1,891 unordered squared distances and pair sums are distinct.

Run

```text
PYTHONPATH=phase2/loop/erdos1208 \
python3 phase2/loop/erdos1208/verify_low_codegree_anchor_matching_barrier.py
```

## 8. Remaining gate

The low-codegree band has therefore reached a clean stopping point:

\[
 \sum_{r:U_L(r)\ge T}C_{<k}(r)
 \le k\sum_{r:U_L(r)\ge T}R_D(-18r).                    \tag{8.1}
\]

The coefficient `k` cannot be reduced by any pointwise theorem using
matching anchors, disjoint role targets, determinant qualification, or
target endpoint wedges.  What remains is precisely a many-gap theorem:
large determinant-qualified target richness at `r` must be negatively
correlated, in aggregate, with raw distance-gap population at the dilated
opposite gap `-18r`.  The existing marginal tails do not imply this, and
the one-gap construction shows why a local inverse statement cannot.
