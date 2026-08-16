# Projected-source storage is an exact cap-load versus opposite-profile gate

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

There is an exact cross-branch storage theorem at one node of the
high-transversal prefix descent.  It gives the desired bounded-load branch
when projected source tags are diffuse, and identifies the precise
concentrated residue when they are not.

Let \(\mathcal D\) be ordinary source faces in the left child of a strong
seam \(Y\prec Z\).  Let \(\mathcal H_K\) be the released faces below one
fixed deleted-prefix tag \(K\), partitioned by their next physical label
\(z\):

\[
                    \mathcal H_K=\bigsqcup_{z\in S}\mathcal H_{K,z}.
                                                               \tag{1}
\]

For each \(D\), write its canonical monotone-hull decomposition as

\[
                         D=A(D)\cup B(D),               \tag{2}
\]

where \(A(D)\) is a cap and \(B(D)\) is a cup.  The ordinary third face

\[
                         W(D,z)=A(D)\cup\{z\}            \tag{3}
\]

retains the branch label \(z\).  If

\[
 \lambda_A=|\{D:A(D)=A\}|,\qquad m_z=|\mathcal H_{K,z}|,
                                                               \tag{4}
\]

then the load of \(W=A\cup\{z\}\) among the Cartesian records
\(\mathcal D\times\mathcal H_K\) is exactly

\[
                              \lambda_A m_z.             \tag{5}
\]

Consequently, with \(a=|\{A(D)\}|\), \(q=|S|\), \(M=|\mathcal D|\), and
\(m=|\mathcal H_K|\),

\[
\boxed{
 |\mathcal W|=aq,\qquad
 |\mathcal W|\,\max_{A,z}(\lambda_A m_z)\ge Mm.
}                                                       \tag{6}
\]

Thus either the third-face load is at most \(\Lambda\), producing at least
\(Mm/\Lambda\) distinct tag faces, or one actual pair \((A,z)\) localizes a
continuing rectangle of mass \(\lambda_A m_z\).

The concentrated branch has exact geometry rather than unspecified
metadata.  When \(A\) is fixed, the cup traces \(B(D)\) are distinct and
recover \(D\) together with \(A\).  Hence it supplies an opposite-facing
cup family of size \(\lambda_A\), while \(\mathcal H_{K,z}\) is the next
prefix family of size \(m_z\).  This is the one-chamber recursive state
suggested by the endpoint potential.

The theorem does **not** force a cycle.  In the live Pascal prefix
regression all full tags \(D\cup\{z\}\) are bad, but their canonical
circuits are the rooted star

\[
                              T(D)\cup\{z\}.             \tag{7}
\]

Every projected tag (3) uses the same forward top-seam direction.  Across
all prefix siblings and all chronology levels, the complete tag bank is
contained in

\[
               \mathcal C(Y)\times Z,
\qquad |\mathcal W_{\rm all}|\le C(Y)|Z|.               \tag{8}
\]

For the central Pascal cell this has only half the parent's quadratic
coefficient.  The heavy fibres in (6) are the opposite cup profiles, also
at half coefficient.  Their product recovers the live source mass, but
they are not one face bank and the cup profile points in the wrong
direction for the actual seam.  Reflection would expose it only in another
configuration and is not an internal payment.

This gives a scalable live-normalized barrier to the proposed
“all bad tags generate a cycle” alternative.  The sharp positive
replacement is:

> diffuse boundary-chain directions must create actual same-configuration
> profile edges and a cycle, while concentration in one chamber must be
> charged recursively through the opposite-profile fibre in (6).

The present report proves the exact one-chamber reduction and shows it is
coefficient-sharp.  It does not prove the missing diffuse-direction
promotion.

## 1. Exact projected-tag theorem

Fix a generic horizontal direction.  For every ordinary face \(D\), its
upper and lower hull chains are respectively a cap and a cup, with a fixed
endpoint convention.  Their ordered pair recovers \(D\).  This is the
standard injection

\[
             \mathcal F(Y)\hookrightarrow
             \mathcal C(Y)\times\mathcal U(Y).          \tag{9}
\]

Use the cap chain as \(A(D)\) and the cup chain as \(B(D)\).  Since
\(\{z\}\) is a cup in the right child, the strong-glue identity makes
\(A(D)\cup\{z\}\) an ordinary face.  Its left and right role traces recover
\((A(D),z)\).  Therefore distinct pairs \((A,z)\) give distinct faces and
\(|\mathcal W|=aq\).

For a fixed output \(A\cup\{z\}\), a record mapping to it consists of an
arbitrary source in the \(A\)-fibre and an arbitrary continuation in the
\(z\)-class.  Its load is exactly \(\lambda_A m_z\), proving (5).  Since

\[
       \sum_A\lambda_A=M,\qquad \sum_zm_z=m,
\]

the average load over the \(aq\) outputs is \(Mm/(aq)\), which proves (6).

When \(A\) is fixed, the map \(D\mapsto B(D)\) is injective: equation (2)
recovers \(D\).  Thus a heavy \(\lambda_A\) is an actual family of distinct
cup faces, not duplicate source histories.  Likewise
\(\mathcal H_{K,z}\) consists of distinct ordinary released faces.  The
high-load alternative is therefore a literal opposite-profile times
continuation rectangle.

The decoder is exact at the level stated.  The third face \(W\) reveals
\((A,z)\); paired with the original source endpoint \(D\), it recovers the
immediate branch choice and the discarded cap projection.  Together with a
reduced released endpoint and the globally fixed prefix \(K\), it recovers
the original record.  What (3) does not recover by itself is the source
inside one \(A\)-fibre; that loss is exactly \(\lambda_A\).

## 2. Weighted formulation

The same statement holds for nonnegative record weights of product form
\(\alpha_D\gamma_U\).  Put

\[
 \lambda_A=\sum_{D:A(D)=A}\alpha_D,\qquad
 m_z=\sum_{U\in\mathcal H_{K,z}}\gamma_U.               \tag{10}
\]

Then (5) is the exact weighted load, the total mass is
\((\sum_A\lambda_A)(\sum_zm_z)\), and (6) is unchanged with weighted
\(M,m\).  In particular it applies to the unit release-bank normalization
and to row-normalized source weights.

For arbitrary nonproduct record weights, define

\[
                       L_{A,z}
 =\sum_{\substack{D:A(D)=A\\U\in\mathcal H_{K,z}}}
                 w_{D,U}.                              \tag{11}
\]

There are still exactly \(aq\) possible tag faces and

\[
                  |\mathcal W|\max_{A,z}L_{A,z}
                         \ge\sum_{D,U}w_{D,U}.           \tag{12}
\]

The high-load cell remains a literal fixed-\((A,z)\) localization, although
without product weights its mass need not factor into two marginal sizes.

## 3. Pascal realizes the concentrated branch sharply

Return to the central Pascal split

\[
 P_n=T(n,n/2)=Y\prec Z.
\]

Use the fixed-rank/fixed-root source family and fixed-rank pocket layer from
HIGH_TRANSVERSAL_PASCAL_PREFIX_DAG_BARRIER.  They have sizes

\[
 |\mathcal D|,|\mathcal H|
       \ge V(P_n)2^{-O(L\log L)},\qquad L=\log|P_n|.    \tag{13}
\]

At any prefix node, every next label \(z\) lies in the same physical right
child.  Hence all projected tag faces use the same top-seam cap-to-singleton
direction.  Summing over every node cannot create more than the ambient
bank in (8); repeated appearances of the same \((A,z)\) are genuine
cross-level collisions.

For every full source \(D\) and every \(z\in Z\), choose the canonical
noncap triple \(T(D)\subset D\).  The set \(T(D)\cup\{z\}\) is nonconvex,
so

\[
                         D\cup\{z\}\notin\mathcal F(P_n). \tag{14}
\]

All bad full tags therefore point from the source root toward the right
child.  They form a star/DAG, not a directed profile cycle.

Let

\[
 C_Y=C(Y),\qquad U_Y=U(Y).
\]

The universal hull injection gives

\[
                          V(Y)\le C_YU_Y.               \tag{15}
\]

Uniform Pascal asymptotics give

\[
\begin{aligned}
 \log C_Y&=\left({\beta\over2}+o(1)\right)L^2,\\
 \log U_Y&=\left({\beta\over2}+o(1)\right)L^2,\\
 \log V(P_n)&=(\beta+o(1))L^2.                         \tag{16}
\end{aligned}
\]

Since \(\log|Z|=O(L)\), the full cross-level tag bank \(C_Y|Z|\) has
coefficient \(\beta/2\).  A largest cap fibre can simultaneously carry
\(\beta/2\) coefficient worth of distinct cup traces.  Equation (15) shows
that these two square-root banks reconstruct the source scale exactly.
No fixed-power gain is hidden in (6).

This is the same endpoint-potential obstruction in a decoder-faithful
form: the large \(U_Y\) family is an actual same-configuration bank, but it
is the unused, backward-facing profile.  It can pay only after a genuine
reset/cycle supplies an edge which uses it.

## 4. Consequence for cross-branch routing

At a high-transversal prefix node there are now two rigorous branches.

1. **Diffuse projected tags.**  If every tag face has load at most
   \(\Lambda\), (12) gives at least total-mass/\(\Lambda\) distinct ordinary
   third faces, with the branch label physically retained.
2. **Concentrated projected tags.**  A fixed cap \(A\) and next label \(z\)
   carry high mass.  Under product weights, this localizes a large family of
   opposite cups \(B(D)\) and a large continuation family
   \(\mathcal H_{K,z}\).  The next operation must either recurse on this
   one-chamber state or create an actual edge using the cup profile.

What cannot be inferred is that the bad full tags in the second branch
already create a cycle.  Pascal shows they may all share one forward
direction and one rooted-star sign.  The endpoint potential may telescope
only after an actual same-configuration return edge has been constructed.

This isolates the next missing geometric statement:

> assign each sibling label its actual completion-side boundary-chain
> chamber.  Either the chamber distribution is diffuse enough to create a
> decoded cycle of realized profile edges, or one chamber captures enough
> weight that the cap-fibre/cup-profile localization above can be iterated
> without coefficient loss.

The second alternative is exact here.  The first remains open.

## 5. Verification

**verify_projected_source_cross_branch_storage.py** checks:

* all cap/cup hull decompositions in the rational
  \(T(6,3)=T(5,2)\prec T(5,3)\) split;
* every bad full tag, every good projected tag, the exact output loads at
  every prefix sibling node, and the heavy-fibre cup decoder;
* the complete cross-level containment in
  \(\mathcal C(Y)\times Z\);
* the cap--cup endpoint inequality and square-root Pascal calibration
  through \(n=96\); and
* the weighted load identity on exhaustive small integer fibre tables.
