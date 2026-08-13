# Erdős #669 prior-art record (2026-08-13)

## Status found

- The [Erdős Problems entry](https://www.erdosproblems.com/669) labels the
  problem open, records the \(k=3\) asymptotic and only the elementary
  pair-counting upper bound for general \(k\). Its warning that database status
  is not a literature guarantee applies here.
- The original source is Erdős, “Some Unsolved Problems,” in
  *Combinatorics, Geometry and Probability* (1997),
  [DOI 10.1017/CBO9780511662034.004](https://doi.org/10.1017/CBO9780511662034.004).
  An earlier formulation is problem 17 in Erdős,
  [“Some of my favourite problems in various branches of
  combinatorics”](https://lematematiche.dmi.unict.it/index.php/lematematiche/article/download/587/555/),
  *Le Matematiche* 47 (1992), around p.238. It explicitly asks to prove
  existence of the normalized at-least-\(k\) limit. Thus the website's
  displayed conclusion should formally use a limsup until existence is proved.
- Green and Tao solved the exact large-\(n\) three-rich-line problem; see
  [On sets defining few ordinary lines](https://arxiv.org/abs/1208.4714).
- Noam Elkies uses exactly the \(t_k,T_k\) notation and surveys generalized
  orchard constructions in
  [On some points-and-lines problems and configurations](https://arxiv.org/abs/math/0612749).
  His focus includes bounded maximum collinearity and recursive lower exponents,
  which are adjacent to but distinct from #669's unrestricted quadratic-density
  constants.
- The directly relevant older construction source is Ilona Palásti,
  [A construction for arrangements of lines with vertices of large
  multiplicity](https://real-j.mtak.hu/5463/1/StudScientMath_21.pdf), Studia
  Sci. Math. Hungar. 21 (1986), 67--78. Section 2 gives the four-direction
  coefficient \(7/200\) for fourfold vertices.
- Pinchasi--Radoičić--Sharir explicitly collect the pair identity and
  Melchior's inequality for \(k\)-lines in
  [On empty convex polygons in a planar point set](https://doi.org/10.1016/j.jcta.2005.03.007),
  JCTA 113 (2006), 385--419. Thus the upper-bound ingredient used here is
  standard prior art.
- For \(k\ge5\), Shnurnikov's published arrangement inequality is stronger
  than Melchior for this purpose; see
  [On the number of regions and multiplicities of vertices in plane
  arrangements](https://arxiv.org/abs/1203.1296), §3, inequality (3).
  Pair counting gives
  \[
  \limsup_{n\to\infty}\frac{F_k(n)}{n^2}
  \le\frac1{k^2+3k-15}\qquad(k\ge5),
  \]
  after separating the exceptional near-pencil cases, which have only
  \(O(1)\) vertices of a fixed multiplicity. Melchior remains stronger at
  \(k=4\).
- R. J. Simpson,
  [“Convex lattice polygons of minimum area”](https://doi.org/10.1017/S0004972700028525),
  *Bull. Austral. Math. Soc.* 42 (1990), 353–367, proves that minimum-area
  convex lattice \(2k\)-gons may be taken parallel-sided and tabulates the
  determinant sums \(7,14,24,40,59,87,121,164\) for \(4\leq k\leq11\).
  Thus the direction-vector optimization used in the zonotope note is
  definitely prior art.
- Bárány and Tokushige,
  [“The minimum area of convex lattice \(n\)-gons”](https://www.renyi.hu/~barany/cikkek/94.pdf),
  *Combinatorica* 24 (2004), 171–185, prove that \(A(n)/n^3\) has a limit.
  Their reduction identifies a centrally symmetric minimizing polygon as a
  zonotope whose area is the sum of pairwise absolute determinants.
- Stanley's lattice-zonotope Ehrhart formula supplies the general polynomial
  behind the exact count; see
  [“A zonotope associated with graphical degree sequences”](https://math.mit.edu/~rstan/pubs/pubfiles/83.pdf),
  DIMACS Series 4 (1991), Theorem 2.2.

## Prior-art kill for \(1/28\)

Queries run included combinations of:

- `Palasti multiplicity 4 arrangement`;
- `1/28 fourfold points line arrangement`;
- `n^2/28 quadruple points lines`;
- `3:3:4:4 line arrangement`;
- citations/title searches for Palásti's 1986 paper;
- generalized orchard / \(t_4(n)\) / maximal fourfold vertex searches.

The initial exact-formula searches missed a decisive non-English source. Zhao
Hui Du's Chinese-language orchard-problem page
([rendered page](https://emathgroup.github.io/blog/orchard-planting-problem/),
[repository source](https://github.com/emathgroup/selectedTopics/blob/master/content/posts/orchard-planting-problem.md))
explicitly describes trimming the unproductive diagonal extremes to form an
octagonal model with

\[
14m+O(1)\quad\text{lines and}\quad 7m^2+O(m)\quad\text{fourfold points}.
\]

The text mistakenly reports the resulting coefficient as \(1/24\), but its own
counts give \(7/14^2=1/28\). Git history dates the insertion of this paragraph to
commit `185219c6c3ac3e160b523fe34bd7225bfc589801` on 2019-10-20, by Du. This
predates the present attack and describes the same octagonal pruning at the
asymptotic level.

The repository proof remains useful because it fixes exact intercept sets,
proves the exact \(7q^2\) count, treats the vertices at infinity, handles generic
padding, and supplies an independent enumerator. None of those refinements
supports advertising \(1/28\) as a new lower coefficient.

## Honest claim level

The defensible wording is:

> We independently rediscovered and exactly verified the \(1/28\) octagonal
> four-direction lower construction. Palásti's printed 1986 coefficient is
> \(7/200\); a 2019 Chinese web source already states asymptotic counts implying
> \(1/28\), despite printing \(1/24\) by arithmetic error.

Do not call this a solution of Erdős #669. It improves one lower bound for the
\(k=4\) case relative to Palásti's paper, but the improvement is prior art. It
leaves a factor-two gap to the Melchior upper bound, as well as the existence and
values of the requested limits.

## Zonotope lower bounds: current novelty verdict

The general construction in ZONOTOPE_CONSTRUCTION.md gives

\[
f_k(n),F_k(n)\geq \frac{n^2}{4A(2k)}-O_k(n).
\]

Its ingredients—zonotope area, Ehrhart counting, and minimum-area direction
sets—are published. Direct exact-formula searches, multigrid/dicing/orchard
searches, and the visible citation trail from Palásti did not locate the
orchard deduction or the coefficients

\[
1/56,\ 1/96,\ 1/160,\ 1/236,\ 1/656
\]

for \(k=5,6,7,8,11\). These exceed Palásti's printed coefficients. The
defensible wording is:

> An apparently unrecorded application of classical lattice-zonotope and
> minimum-area polygon results yields lower coefficients that improve
> Palásti's 1986 table for \(k=5,6,7,8,11\).

This is not a novelty clearance. The \(k=4\) instance was missed until a
Chinese-language webpage was found, so specialist checking of MathSciNet,
zbMATH, orchard surveys, and multigrid literature remains necessary before
publication.
