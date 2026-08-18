# The centered residual as a pair-sum graph and a six-role design

## Status

Let `A` be a planar distance-Sidon set, `|A|=k`, put

\[
 D^*=(A-A)\setminus\{0\},
 \qquad J(x,y)=(-y,x),
\]

and write

\[
 C(A)=\#\{(d,u,v)\in(D^*)^3:u+v=Jd\}.           \tag{0.1}
\]

This is the positive centered residual in
`TWO_SIDED_ROTATED_SUPPORT_AUDIT.md`:

\[
 \mathcal E_J(A)=2k^3-k^2+C(A).                  \tag{0.2}
\]

This note gives three exact refinements.

1. `C(A)` is a weighted edge count inside the unordered pair-sum set
   `A\oplus A`.
2. Relations involving at most five point labels contribute only `O(k^3)`.
   The hard term really consists of six distinct endpoints.
3. If no two fixed labels in two fixed roles occur together more than `t`
   times in the six-point transverse relation system, the
   Dvir--Saraf--Wigderson design theorem gives

   \[
    C_{6,\mathrm{tr}}(A)\le 864t k^2.             \tag{0.3}
   \]

Thus a role-pair codegree bound `t<=k^(1+o(1))` would prove the desired
cubic residual estimate.  Exact adversaries show why (0.3) is not itself the
solution: one constituent edge can occur in `Theta(k^2)` relations.  In all
tested adversaries the large codegree is confined to the endpoint pairs of
the three constituent edges, while cross-edge role pairs stay linear.  This
rederives the surviving fourth-moment/fixed-edge gate from a different
direction.

The exact identities, endpoint profiles, role-pair codegrees, and modular
rank claims in this note are checked by
`verify_centered_residual_design_dichotomy.py`.

## 1. The weighted pair-sum identity

Distance-Sidon implies vector-Sidon, so every unordered sum of two points,
with repetition allowed, has a unique unordered representation.  Put

\[
 Q=A\oplus A=\{a+b:a,b\in A,\ a\le b\},
 \qquad |Q|={k(k+1)\over2},                       \tag{1.1}
\]

and give `q in Q` weight

\[
 w(q)=
 \begin{cases}
  1,&q=2a,\\
  2,&q=a+b,\ a\ne b.
 \end{cases}                                      \tag{1.2}
\]

Then

\[
 \boxed{
 C(A)=\sum_{\substack{p,q\in Q\\p-q\in JD^*}}w(p)w(q).}       \tag{1.3}
\]

Indeed, write

\[
 u=c-e,\qquad v=x-y.
\]

The relation `u+v=Jd` is exactly

\[
 (c+x)-(e+y)=Jd.                                  \tag{1.4}
\]

The weights in (1.2) count the possible ordered assignments of the two
summands to `(c,x)` and `(e,y)`.  Conversely, each weighted choice in (1.3)
recovers `u,v`, and the vector `d` has a unique ordered endpoint pair.

There is no hidden shared endpoint between the two pair-sums in (1.3).  If
the multisets underlying `p` and `q` shared a point, then `p-q` would be a
nonzero member of `D`.  But `p-q` also lies in `JD`, contradicting

\[
 D\cap JD=\{0\}.                                  \tag{1.5}
\]

Thus (1.3) is simultaneously a pair-sum graph, a midpoint graph after
division by two, and the exact centered Fourier residual.

## 2. Endpoint overlap costs only `O(k^3)`

Represent a relation in (0.1) by its three uniquely oriented `A`-edges.
If their endpoint union has size at most five, some two of the three edges
share an endpoint.  Choose:

* the two edge roles, in at most three ways;
* which endpoint is shared in each edge, in at most four ways; and
* the common endpoint and the two other endpoints, in at most `k^3` ways.

These data determine the two directed edge vectors.  Equation (0.1)
determines the third vector, and vector-Sidonicity determines its ordered
endpoint pair in at most one way.  Hence

\[
 C_{\le5}(A)\le12k^3.                             \tag{2.1}
\]

After the separate parallel/line branch, it is therefore enough to control
the six-distinct transverse term `C_(6,tr)(A)`.  The exact closure profiles
show that this cleanup is necessary but not sufficient:

\[
\begin{array}{c|r|rrrr}
k&C(A)&|V|=3&|V|=4&|V|=5&|V|=6\\ \hline
20&5,564&4&252&2,004&3,304\\
30&26,472&8&640&7,088&18,736\\
40&73,282&8&1,170&15,664&56,440\\
60&259,724&8&1,920&39,156&218,640
\end{array}                                       \tag{2.2}
\]

At `k=60`, 218,516 of the 218,640 six-distinct relations are transverse.
The hard mass is genuinely a six-point transverse configuration.

## 3. The six-role coefficient matrix

It is convenient to write a collision of two off-diagonal triples as

\[
 a_0+J(b_0-c_0)=a_1+J(b_1-c_1).                  \tag{3.1}
\]

After identifying the plane with the Gaussian line, every six-distinct
transverse collision supplies the homogeneous row

\[
 a_0+i b_0-i c_0-a_1-i b_1+i c_1=0.             \tag{3.2}
\]

Use six disjoint role copies of `A` as columns.  For two distinct roles
`r,s` and fixed labels `p,q in A`, let

\[
 t_{rs}(p,q)=
 \#\{\text{six-distinct transverse rows}:x_r=p,\ x_s=q\},
 \qquad
 t=\max_{r<s,p,q}t_{rs}(p,q).                    \tag{3.3}
\]

### Proposition 3.1

For every vector-Sidon `A`,

\[
 \boxed{C_{6,\mathrm{tr}}(A)\le864t k^2.}        \tag{3.4}
\]

### Proof

Write `R=C_(6,tr)(A)`.  Starting with the `R` rows, repeatedly delete an active
role-label column of degree less than

\[
 \tau={R\over12k},                               \tag{3.5}
\]

together with all incident rows.  There are at most `6k` columns, so fewer
than `R/2` rows are deleted.  The remaining matrix has `m>=R/2` rows, every
row has six nonzero entries, every active column has degree at least `tau`,
and every two columns meet in at most `t` rows.

The improved design-matrix theorem of Dvir--Saraf--Wigderson gives, for a
`(q,tau,t)` design matrix,

\[
 \operatorname{corank}M
 \le {m t q(q-1)\over\tau^2}.                     \tag{3.6}
\]

Here `q=6` and `m<=R`, hence

\[
 \operatorname{corank}M
 \le {30Rt\over(R/(12k))^2}
 = {4320t k^2\over R}.                            \tag{3.7}
\]

Every one of the six roles remains active.  Assigning a constant `c_r` to
all active columns of role `r` is in the kernel whenever

\[
 c_0+i c_1-i c_2-c_3-i c_4+i c_5=0.             \tag{3.8}
\]

This is a five-dimensional kernel, so the left side of (3.7) is at least
five.  Rearranging proves (3.4).  QED.

The theorem used in (3.6) is Theorem 1.3 of Dvir--Saraf--Wigderson,
*Improved rank bounds for design matrices and a new proof of Kelly's
theorem*, <https://arxiv.org/abs/1211.0330>.

For a noncollapsed planar realization there are normally two further kernel
directions: the coordinate vector itself, repeated in all roles, and the
role-signed complex conjugate coordinate.  The constant five-dimensional
kernel is enough for (3.4), so no noncollinearity qualification is needed.

## 4. Exact saturation and the exceptional endpoint pairs

On the 20-point closure witness the full six-role matrix has rank `113` on
`120` columns.  On the 60-point witness it has rank `353` on `360` columns.
Thus both have exactly the seven unavoidable kernel directions just
described.  Ordinary support rank is already saturated by legal
distance-Sidon configurations; there is no spare nullity from which to force
a contradiction.

The role-pair data identify the obstruction more sharply.  In the role order

\[
 (a_0,b_0,c_0,a_1,b_1,c_1),                      \tag{4.1}
\]

the three constituent-edge endpoint pairs are

\[
 (a_0,a_1),\qquad(b_0,c_0),\qquad(b_1,c_1).      \tag{4.2}
\]

The exact maxima are:

\[
\begin{array}{c|r|r|c|r}
\text{witness}&k&C_{6,\mathrm{tr}}&\text{three maxima in (4.2)}
 &\text{largest cross-role maximum}\\ \hline
\text{closure}&60&218,516&(180,292,292)&293\\
\text{compact anchor}&117&157,960&(3,880,34,34)&289\\
\text{fixed colour}&65&38,368&(802,29,29)&74\\
\text{hybrid}&45&52,664&(188,114,114)&114
\end{array}                                       \tag{4.3}
\]

The compact-anchor and fixed-colour witnesses therefore disprove a uniform
`t=k^(1+o(1))` theorem: one realized constituent edge can have quadratic
role-pair codegree.  Nevertheless, their total six-point mass remains below
the cubic scale.  The issue is the distribution of these heavy edge pairs,
not their individual maximum.

This is exactly the row/colour moment gate in a new language.  Fixing one of
the three pairs in (4.2) fixes one directed edge of `A`; its codegree is the
corresponding local residual multiplicity.  Squaring and summing these
codegrees gives the fourth moments in
`TRANSVERSE_SECOND_MOMENT_GATE.md`.

## 5. What remains

Proposition 3.1 closes the branch in which all two-role codegrees are nearly
linear.  It does not control the heavy constituent-edge branch, and the
standard design theorem cannot simply replace maximum codegree by average
codegree: Dvir--Saraf--Wigderson explicitly record block-diagonal examples
showing that such a replacement is false for arbitrary designs.

The next useful theorem must exploit the special form of the three
exceptional pairings in (4.2).  Two equivalent targets are:

1. the existing radial moment estimate

   \[
    \sum_{d\in D} r(d)^2\le k^{4+o(1)};           \tag{5.1}
   \]

2. a tailored rank/spectral theorem for (3.2) in which the three high
   pair-codegree blocks are incidence matrices of realized `A`-edges and a
   supercritical block forces two non-antipodal edges to have equal norm.

The second formulation explains precisely what a successful refinement of
the design method must add: Euclidean radial rigidity.  Ordinary rank,
average codegree, and endpoint-overlap cleanup are now exhausted.
