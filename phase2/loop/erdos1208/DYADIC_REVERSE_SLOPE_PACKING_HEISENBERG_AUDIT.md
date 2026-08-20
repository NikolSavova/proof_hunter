# Dyadic reverse multiplicity: slope packing and Heisenberg-energy audit

## 1. Outcome

Fix a dyadic family \(\mathcal L_L\) of nonhorizontal derivative lines with

\[
 L\le |S_\ell|<2L.
\]

Let a child record retain its shift, slope, intercept, and tail triple:

\[
 \chi=(h,\mu,\beta,V).
\]

Write \(\rho_L(\chi)\) for the number of parent-line pairs from
\(\mathcal L_L\) which produce \(\chi\) under the exact child quotient, and
put \(\rho_L=\max_\chi\rho_L(\chi)\).  Combining the arithmetic slope count
with full-family same-slope packing gives

\[
 \boxed{
 \rho_L\le
 \min\left\{
 k,\
 {8(m-1)^2k(k-1)\over L(L-1)^3}
 \right\}.}                                           \tag{1.1}
\]

Thus the former crude reverse multiplicity \(k\) is genuinely improved
once

\[
 L^4\gg m^2k.                                         \tag{1.2}
\]

For an excess dominated by this band, (1.1) closes the desired
\(k^{3+o(1)}\) scale when

\[
 L\ge (mk)^{1/2}m^{-o(1)}.                            \tag{1.3}
\]

Together with the direct slope-count estimate

\[
 T_L\ll {m^2k^2\over L},
\]

the \(k^3\)-dominated residual is reduced from
\(\sqrt{k}<L\lesssim m^2/k\) to

\[
 \boxed{
 \sqrt{k}<L<
 \min\{m^2/k,\sqrt{mk}\}\,m^{o(1)}.}                  \tag{1.4}
\]

This does not finish the \(m^2\)-dominated range.

The patch group is exactly the three-dimensional Heisenberg group.  A
primary-source audit of Murphy--Wheeler, Theorem 5, gives a
characteristic-zero energy bound for the unweighted patch parameters.
However, the theorem alone does not close (1.4): the proof needs the
endpoint-weighted correlation

\[
 \sum_g r_{\Gamma\Gamma^{-1}}(g){K_g\choose3},         \tag{1.5}
\]

where \(K_g\) is the actual child-line occupancy.  Ordinary Heisenberg
energy controls only \(\sum_g r(g)^2\), and Cauchy--Schwarz loses too much
when parent intersections can be only three points.  The exact missing
input is therefore a support-sensitive Heisenberg incidence theorem, not
another unweighted group-energy estimate.

Finally, a genuine 219-point integral distance-Sidon certificate has
\(L=20>\sqrt{219}\) and one child record with three reverse preimages, all
on isolated two-vertex parameter paths and with no common core between
different preimages.  This is a finite barrier to any claim that reverse
multiplicity greater than one automatically creates a long quadratic
parameter path.

## 2. Proof of the reverse-multiplicity bound

For a line parameter \(g=(c,\lambda,\alpha)\), use the affine shear

\[
 G_g(r,y)=(r+c,\ y+\alpha+\lambda r).
\]

If \(g_+\) and \(g_-\) are a parent pair producing \(\chi\), their shifts
are \(d+h\) and \(d\), where \(d\) is determined by the reverse preimage.
Once \(d\) is fixed, each parent line is uniquely determined by its three
derivative points on \(V-d\).  Hence reverse preimages inject into the
lower-shift parent lines.

Let \(J_L\) be the number of possible reduced slopes of \(L\)-rich lines.
The arithmetic audit gives

\[
 J_L\le {8(m-1)^2\over(L-1)^2}.                       \tag{2.1}
\]

For any fixed slope \(\lambda\), distinct lines of that slope have tail
sets meeting in at most one point.  Consequently every unordered tail
pair belongs to at most one such line, and

\[
 N_\lambda{L\choose2}\le{k\choose2},\qquad
 N_\lambda\le {k(k-1)\over L(L-1)}.                   \tag{2.2}
\]

Summing (2.2) over (2.1) bounds the total number of possible lower parent
lines and proves the second term in (1.1).  The first term is the earlier
endpoint bound: for a fixed child tail \(v\in V\), every reverse shift has
\(v-d\in R\), giving at most \(k\) choices of \(d\).

## 3. Exact global energy consequence

Let

\[
 T_L=\sum_{\ell\in\mathcal L_L}{|S_\ell|\choose3},
 \qquad
 d_L(U)=|\{\ell\in\mathcal L_L:U\subset S_\ell\}|.
\]

The parent overlap mass

\[
 P_L=\sum_U{d_L(U)\choose2}
\]

satisfies

\[
 P_L\ge {1\over2}
 \left({T_L^2\over{k\choose3}}-T_L\right).            \tag{3.1}
\]

Every term of \(P_L\) maps to a child record from the full rich-line
family.  If \(T\) denotes the total number of such records, (1.1) gives

\[
 \boxed{
 {1\over2}\left({T_L^2\over{k\choose3}}-T_L\right)
 \le P_L\le\rho_LT.}                                  \tag{3.2}
\]

There are \(D=O(\log k)\) dyadic richness bands.  Suppose the high-richness
excess dominates the already-paid low contribution, and choose a band
with \(T_L\) at least \(1/D\) of that excess.  Then \(T\le2DT_L\), and
(3.2) yields

\[
 T\ll D^2(1+\rho_L)k^3.                               \tag{3.3}
\]

Substitution of (1.1) proves (1.3).  Independently,
same-slope triple packing and (2.1) give

\[
 T_L
 <{16(m-1)^2L\over3(L-1)^2}{k\choose2}
 \ll {m^2k^2\over L},                                 \tag{3.4}
\]

which gives the other upper cutoff in (1.4).

## 4. An exact isolated-preimage distance-Sidon stress

The verifier constructs an explicit integral graph with \(k=219\).  Its
child record is

\[
 (h,\mu,\beta,V)
 =
 \left(
 7,\ 7919,\ 10^{15}+3,\
 \{10^6,10^6+1,10^6+3\}
 \right).                                             \tag{4.1}
\]

It has three reverse denominators

\[
 d\in\{10^4,2\cdot10^4,3\cdot10^4\}.                  \tag{4.2}
\]

For each \(d\), there are two parent lines of richness \(20\), with
parameters

\[
 g_d=(d,\lambda_d,\alpha_d),\qquad
 g_{d+7}
 =(d+7,\lambda_d+7919,\alpha_d+7919d+10^{15}+3),
                                                               \tag{4.3}
\]

and

\[
 g_{d+7}g_d^{-1}=(7,7919,10^{15}+3).                  \tag{4.4}
\]

The two supports in each pair meet in exactly \(V-d\); supports belonging
to different denominators are disjoint.  The child line (4.1) has exactly
the three tails in \(V\).  The six parameter vertices form three isolated
edges: no two denominators differ by \(h\).  All
\({219\choose2}=23871\) squared distances are distinct.

This stress is well below the critical aggregate, but it is a genuine
barrier to a purely local path extraction.  A proof must use the number of
such isolated preimages, their endpoint cost, or their global parameter
energy.

## 5. Exact Heisenberg identification

Represent a patch by

\[
 g=(q,\lambda,\alpha).
\]

Composition of its affine shears is

\[
 (q,\lambda,\alpha)(q',\lambda',\alpha')
 =
 (q+q',\lambda+\lambda',
  \alpha+\alpha'+\lambda q').                         \tag{5.1}
\]

This is the standard three-dimensional Heisenberg law with coordinates

\[
 (g_1,g_2,g_3)=(\lambda,q,\alpha).
\]

The inverse and right quotient are

\[
 (q,\lambda,\alpha)^{-1}
 =(-q,-\lambda,-\alpha+\lambda q),                    \tag{5.2}
\]

\[
 (c,\lambda_c,\alpha_c)(d,\lambda_d,\alpha_d)^{-1}
 =
 \left(
 c-d,\lambda_c-\lambda_d,
 \alpha_c-\alpha_d-(\lambda_c-\lambda_d)d
 \right).                                             \tag{5.3}
\]

Thus (5.3) is exactly the derivative child shift, slope, and intercept.

Murphy and Wheeler, *Growth in Some Finite Three-Dimensional Matrix
Groups*, [arXiv:2005.05077, Theorem 5](https://arxiv.org/abs/2005.05077),
prove the following.  For \(\Gamma\subset H(\mathbb F_q)\), let

- \(z\) be the maximum load in a coset of the center \(Z\);
- \(M_{\rm ab}\) be the maximum load in a coset of a two-dimensional
  abelian subgroup \(LZ\).

If the field has characteristic \(p\),

\[
 |\Gamma|z\le p^2,\qquad z\le\sqrt{|\Gamma|},
\]

then

\[
 E_H(\Gamma)
 \ll|\Gamma|^{5/2}z+|\Gamma|^2M_{\rm ab}.              \tag{5.4}
\]

The square-root condition is \(z\le\sqrt{|\Gamma|}\), not merely
\(z\le|\Gamma|\).

For a fixed finite \(\Gamma\subset H(\mathbb Q)\), choose a sufficiently
large prime avoiding all denominators and all nonzero rational expressions
which encode quotient equalities, center coincidences, and projected
three-point determinants.  Reduction modulo that prime preserves the
energy and both coset maxima, while making
\(|\Gamma|z\le p^2\).  Therefore (5.4) has the following
characteristic-zero corollary:

\[
 \boxed{
 E_H(\Gamma)
 \ll|\Gamma|^{5/2}z+|\Gamma|^2M_{\rm ab}
 \quad(z\le\sqrt{|\Gamma|}).}                         \tag{5.5}
\]

This reduction is lossless for a fixed finite parameter set.

## 6. The two Heisenberg coset loads in endpoint language

Let \(\Gamma_L\) be the parameters of all lines in \(\mathcal L_L\), and
put \(N_L=|\Gamma_L|\).  A center coset fixes \((q,\lambda)\) and varies
\(\alpha\).  These are parallel lines in one derivative cell.  Their
supports are disjoint, so

\[
 z_L\le{k\over L}.                                    \tag{6.1}
\]

An \(LZ\)-coset projects to an affine line in the
\((q,\lambda)\)-plane.  For a nonhorizontal or vertical projected line,
there are at most \(J_L\) projection points, each with center load at most
\(k/L\).  A horizontal projected line fixes \(\lambda\), and is controlled
directly by same-slope packing.  Hence

\[
 M_{{\rm ab},L}
 \le
 \max\left\{
 {J_Lk\over L},\
 {k(k-1)\over L(L-1)}
 \right\}
 \ll {m^2k\over L^3}+{k^2\over L^2}.                 \tag{6.2}
\]

Similarly,

\[
 N_L
 \le J_L{k(k-1)\over L(L-1)}
 \ll {m^2k^2\over L^4}.                               \tag{6.3}
\]

When \(z_L\le\sqrt{N_L}\), (5.5)--(6.3) give the completely explicit
unweighted estimate

\[
 E_H(\Gamma_L)
 \ll
 {m^5k^6\over L^{11}}
 +{m^4k^6\over L^{10}}
 +{m^6k^5\over L^{11}}.                               \tag{6.4}
\]

When the square-root hypothesis fails, the trivial
\(E_H(\Gamma_L)\le N_L^3\) remains available.

## 7. Why unweighted Heisenberg energy does not close the scalar gate

For an oriented parent pair with quotient \(g\), translate its common tail
set by the second shift.  It lies on the child line with parameter \(g\).
If \(K_g\) is that child's full occupancy, then the exact endpoint-weighted
bound is

\[
 P_L
 \le
 W_L:=
 \sum_g r^+_{\Gamma_L\Gamma_L^{-1}}(g){K_g\choose3},  \tag{7.1}
\]

where one orientation is retained for every unordered parent pair.  Its
representation energy is at most \(E_H(\Gamma_L)\).

There is a global square-weight bound for child lines.  Dyadic slope
counting and same-slope packing give

\[
 \sum_{\text{all child lines }\ell}
 {K_\ell\choose3}^2
 \ll m^2k^4.                                         \tag{7.2}
\]

Indeed a dyadic \(K\)-band has
\(O(m^2k^2/K^4)\) lines and contributes
\(O(m^2k^2K^2)\); summing geometrically up to \(K=k\) proves (7.2).
Consequently

\[
 W_L\ll m k^2 E_H(\Gamma_L)^{1/2}.                    \tag{7.3}
\]

If \(T_L\gg k^3\), (3.1) and (7.3) yield only

\[
 T_L\ll m^{1/2}k^{5/2}E_H(\Gamma_L)^{1/4}.            \tag{7.4}
\]

Even using \(T_L\asymp N_LL^3\) self-consistently, the two terms in (5.5)
give, at best,

\[
 T_L
 \ll
 {m^{4/3}k^{22/3}\over L^{17/3}}
 +{m k^5M_{{\rm ab},L}^{1/2}\over L^3}.               \tag{7.5}
\]

Substitution of (6.2) does not reach
\(m^{o(1)}(k^3+m^2)\) throughout (1.4).  The loss is structural:
Heisenberg energy can be small while a few quotients carry child lines
with very large endpoint occupancy, or energy can be large through
parameter coincidences whose parent supports meet in only three points.

Therefore Murphy--Wheeler is a valid and exact input, but not by itself a
finish.  A usable next theorem must correlate \(r(g)\) with \(K_g\), or
show that the large terms in (7.1) force a common core, a long quotient
path, or ambient height.

## 8. Exact remaining target

After (1.1)--(1.4), a counterexample to the derivative route must
simultaneously have:

1. a dominant dyadic band in (1.4);
2. fixed-child reverse multiplicity near the slope-packing ceiling;
3. most reverse preimages distributed among many same-slope packing
   blocks, rather than a common tail core;
4. quotient paths broken into short components, as in Section 4;
5. a large positive correlation between Heisenberg quotient multiplicity
   and child-line occupancy, exceeding what (7.2)--(7.3) see.

This is strictly smaller than the previous “distributed overlap” residual.
The next plausible attack is a support-weighted point--plane incidence
estimate for (7.1), with the complete endpoint translations retained.

## 9. Verification

Run

    python phase2/loop/erdos1208/verify_dyadic_reverse_slope_packing_heisenberg_audit.py

The verifier checks the Heisenberg product, inverse, associativity, and
right quotient; the exact algebra in (1.1); center and abelian-coset loads;
the weighted endpoint inequality (7.1); and the full 219-point isolated
reverse certificate, including all 23871 squared distances.
