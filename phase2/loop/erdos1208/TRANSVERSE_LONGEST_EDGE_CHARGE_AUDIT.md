# Longest-edge charging: exact reduction and diameter obstruction

## Summary

Every transverse relation

\[
 d=f+Je,\qquad d,e,f\in D=A-A,
\]

has a unique longest member among the three underlying unoriented edges of
the distance-Sidon set `A`.  Charging the relation to this edge gives an
attractive route to the cubic target: a bound of `k^(1+o(1))` charges per edge
would imply at once that the total number of transverse relations is
`k^(3+o(1))`.

This pointwise route is now unsafe.  A deterministic closure construction
keeps one edge as the **strict global diameter** while its fixed-row relation
count follows a stable `Theta(k^(3/2))` finite profile through `k=90`.  The
same certificate also gives a concrete failure of the proposed two-graphic-
forest proof.  The global cubic total remains healthy, so the surviving
formulation is again a moment or rich-tail estimate over all charged edges.

Everything numerical below is checked in exact integer arithmetic by
`verify_transverse_longest_charge.py`.  The apparent square-root power law is
finite evidence, not an asymptotic counterexample family.

## 1. The unique longest edge

Suppose two members of `(d,e,f)` have the same length.  Distance-Sidonicity
then says that they are the same underlying edge, so their oriented vectors
are equal up to sign.  Inserting any such equality in

\[
 d=f+Je
\]

shows that the remaining nonzero vector has length `sqrt(2)` or `2` times the
common length.  Thus a tie cannot occur at the maximum: every transverse
relation has a unique longest underlying edge.

Let `c(g)` be the number of oriented transverse relations charged to an
unoriented edge `g`.  Since `A` has `binom(k,2)` edges,

\[
 \max_g c(g)\le k^{1+o(1)}
 \quad\Longrightarrow\quad
 \sum_g c(g)\le k^{3+o(1)}.                       \tag{1.1}
\]

The right side is precisely the transverse cubic estimate needed by the
rotated-support route.

There are two fixed-edge geometries.  If `d` is longest, rotate coordinates
so that `d=(R,0)` and write

\[
 e=(x,-a),\qquad f=(R-a,-x).
\]

The strict inequalities `|e|,|f|<R` imply

\[
 0<a<R.
\]

Thus every row relation pairs a downward edge of `A` with a rightward edge,
whose positive coordinate drops add to `R`.  Relations with `f` longest are
in bijection with these under

\[
 (d,e,f)\longmapsto(f,-e,d).
\]

If `e` is longest, then `d-f=Je`; this is the formally dual fixed-column
family and has to be controlled separately.

## 2. The failed two-forest theorem

For a fixed longest row `d`, represent a relation by its endpoint edge in the
`e` projection and its endpoint edge in the `f` projection.  It was tempting
to conjecture that every relation can be assigned to one of the two
projections so that both assigned graphs are forests.  Edmonds' matroid-union
criterion would then give at most `2k-2` relations.

The conjecture survives all `14,266` longest-row families in the older
120-point heavy-row witness.  It nevertheless fails for the purpose-built
diameter family.  At `k=45`, the fixed diameter row has `90` relations but
rank only `83` in the union of its two projected graphic matroids.  At `k=90`
the figures are

\[
 266\quad\hbox{relations},\qquad 173\quad\hbox{union rank}. \tag{2.1}
\]

The fixed-column version already fails in four oriented families of the
120-point witness: two have `(size,rank)=(104,100)` and two have
`(60,58)`.  Hence neither role can be handled by two projected forests.

The verifier computes the union rank by reducing matroid union to
intersection between the direct sum of two graphic matroids and the partition
matroid allowing one copy of each relation.  It then runs the standard exact
augmenting-path algorithm.

## 3. A strict global-diameter adversary

Fix

\[
 d=(10000,0)
\]

with endpoints `(10000,0)` and `(0,0)`.  Every other stored point lies
strictly inside the circle with centre `(5000,0)` and radius `4990`.
Consequently every other pairwise distance is strictly less than `10000`, so
`d` is the unique global diameter.

Starting from the certified 35-point seed, repeatedly adjoin the valid
integer point which creates the most new relations

\[
 u-v+J(x-y)=d
\]

while preserving all squared-distance inequalities and the strict circle
condition.  The exact checkpoints are

| `k` | fixed diameter row | row / `k^(3/2)` | two-forest rank | relation-hypergraph degeneracy |
|---:|---:|---:|---:|---:|
| 35 | 61 | 0.294597 | 61 | 3 |
| 45 | 90 | 0.298142 | 83 | 3 |
| 70 | 180 | 0.307344 | 133 | 4 |
| 90 | 266 | 0.311543 | 173 | 5 |

The stable `0.30 k^(3/2)` normalization is strong evidence against using a
near-linear maximum charge as the main proof target.  It is especially
relevant that the charged edge is not merely longest within each relation:
it is the strict global diameter of the whole point set.

At `k=90`, the complete transverse profile is

\[
 T=336428=0.46149\ldots k^3.                       \tag{3.1}
\]

The unique-longest role counts are

\[
 (T_d,T_e,T_f)=(114876,106676,114876),             \tag{3.2}
\]

and there are no maximum ties.  After grouping both orientations and all
three longest roles, the diameter edge receives

\[
 c(d)=1124=1.31644\ldots k^{3/2}.                  \tag{3.3}
\]

Thus the pointwise charge itself, not only one oriented row, exhibits the
square-root-heavy scale.  In contrast, the total (3.1) remains well below a
constant times `k^3`.

## 4. What remains viable

The exact longest-charge second moment is

\[
 M_{\rm long}=\sum_g c(g)^2.
\]

For the main stored witnesses its normalization is

| witness | `k` | `T/k^3` | `max c(g)` | `M_long/k^4` |
|---|---:|---:|---:|---:|
| heavy closure | 30 | 0.97881 | 164 | 2.53979 |
| heavy closure | 60 | 1.20146 | 344 | 3.64364 |
| heavy closure | 120 | 1.61944 | 896 | 6.52076 |
| diameter closure | 90 | 0.46149 | 1124 | 0.76391 |

Therefore the moment estimate

\[
 \boxed{\sum_g c(g)^2\le k^{4+o(1)}}               \tag{4.1}
\]

survives.  Since there are fewer than `k^2` edges, Cauchy--Schwarz makes
(4.1) imply

\[
 \sum_g c(g)\le k^{3+o(1)}.
\]

Equivalently, it is enough to prove the rich-tail estimate

\[
 \#\{g:c(g)\ge t\}\le k^{4+o(1)}t^{-2}.           \tag{4.2}
\]

This is not yet a simplification of the previously isolated fourth-moment
gate; it is a more geometrically organized version of it.  Its value is
negative and diagnostic: the unique-longest orientation does not make the
problem pointwise.  Any successful charging proof must control the
**distribution** of heavy longest edges, not forbid a square-root-heavy edge.

## 5. Exact artifacts and conclusion

`analyze_transverse_longest_charge.py` contains the 90-point certificate,
enumerates the row and column families, and implements the matroid algorithm.
`verify_transverse_longest_charge.py` checks:

* all pairwise distances in the certificate are distinct;
* the fixed edge is the strict global diameter;
* the four checkpoint row counts and matroid ranks;
* the complete role decomposition, global cubic count, maximum charge, and
  charge second moment at `k=90`.

The conclusion is sharp: longest-edge charging remains a useful
disintegration of the global energy, but its hoped-for `L^infinity` theorem
has the same square-root-heavy obstruction as the original row formulation.
The live theorem is an `L^2`/tail statement such as (4.1) or the equivalent
decorated-parallelogram and row--source `C_4` gates.
