# Candidate spherical transfer and higher-dimensional logarithmic improvement

## Statement

Let \(s_2(t)\) be the least \(N\) such that every \(N\)-point subset of the
unit sphere \(S^2\) contains \(t\) points with all pairwise spherical (or chordal)
distances distinct.  The 2026 planar proof of Clemen--Führer--Roche-Newton
transfers, after the spherical incidence substitutions recorded below, to
give the candidate theorem

\[
  s_2(t)=O(t^3).                                      \tag{1}
\]

Combining (1) with the Conlon--Fox--Gasarch--Harris--Ulrich--Zbarsky recurrence

\[
 s_j(t)=O\bigl(s_{j-1}(t)t^3/\log t\bigr)
\]

would give

\[
 s_j(t)=O_j\bigl(t^{3j-3}(\log t)^{2-j}\bigr)
\]

and hence, for every fixed \(d\ge3\),

\[
 \boxed{
 F_d(n)\gg_d n^{1/(3d-3)}
             (\log n)^{(d-2)/(3d-3)}.}               \tag{2}
\]

This improves the published logarithmic exponent
\((d-3)/(3d-3)\) by \(1/(3d-3)\), without changing the power of \(n\).

## Why the planar proof should transfer

The Clemen--Führer--Roche-Newton proof encodes repeated distances by a rank-4
conflict hypergraph.  It preprocesses a linear-size subset so that per-vertex
isosceles counts, rich bisectors, rich distances, and centred-circle
multiplicities are controlled.  It then applies the Li--Postle sparse
hypergraph coloring theorem.

On \(S^2\):

1. Rudnev--Selig's spherical Guth--Katz argument gives spherical distance
   energy \(O(N^3\log N)\), the input for the average 4-degree.
2. Equidistance loci and fixed-centre fixed-distance loci are spherical
   circles.  Choose a stereographic pole off the finitely many relevant
   circles.  Stereographic projection turns them into Euclidean circles or
   lines while preserving incidences.
3. Marcus--Tardos point--circle incidence estimates therefore give the same
   rich-circle and isosceles estimates used in the planar proof.  The standard
   spherical fixed-distance bound is uniformly \(O(N^{4/3})\); in the
   orthogonal-distance case one first quotients the harmless antipodal
   duplication.

At the planar heavy-distance threshold \(N^{4/3-1/99}\), the rich-distance
lemma gives \(O(N^{2/9}\log N)\) heavy distances.  The uniform
\(O(N^{4/3})\) fixed-distance bound gives \(O(N^{14/9}\log N)\) total heavy
pairs and, after median pruning, maximum heavy-distance 2-degree
\(O(N^{5/9}\log N)\).  All average degrees and codegrees are therefore
unchanged from the planar proof:

\[
 \bar\Delta_4\ll N^2\log N,
 \quad \bar\Delta_3\ll N^{11/9}\log^{2/9}N,
 \quad \bar M\asymp N^{2/3}\log^{1/3}N.
\]

Taking \(f=N^{1/100}\), Li--Postle then gives an independent set of size
\(\Omega(N^{1/3})\), which is (1).

## Honest gap ledger

This file records a promising, independently audited candidate corollary, not
a submission-ready proof.

- The transfer needs a self-contained rewrite of every preprocessing and
  codegree lemma from arXiv:2606.05841 in spherical language.
- One must state carefully whether chordal or geodesic distance is used.  On a
  unit sphere they are strictly monotone functions of one another, so equality
  patterns agree.
- The fixed-distance/pseudocircle estimate and logarithmic exponents survived
  an independent audit, but should be written out fully for submission.
- A targeted public search did not find (1) or (2), but novelty needs an expert
  check.  CFGHUZ explicitly used the older spherical base
  \(s_2(t)=O(t^3\log t)\); the new planar preprint does not state the spherical
  consequence.

The prime-power upper theorem in `proof_prime_power.md` is currently the more
complete result of this attack.
