# Erdős 838: good-history transfer attack

## Executive verdict

There is a rigorous geometric analogue of the **lower history count** in
Feige--Kenyon--Kogan and Bal--Cutler--Pebody: endpoint-pair extension bags
generate

`2^{(1/2-o(1))(log_2 n)^2}`

ordered hinged histories.  This is the desired amount of raw multiplicity.

The graph proof's output map does **not** transfer.  Vertices assigned the
same branch sign need not form a cap or cup, even for an exact rational
realizable rank-three signotope.  Nor does a hinged history necessarily form
a split polygon.  Both failures occur on five rational points.  There is also
an infinite rational family in which the whole set is simultaneously a
hinged history and a split polygon but every convex subset omits a linear
number of points.  Thus neither "hinged implies convex up to O(1)" nor
"split implies convex up to O(1)" can repair the map.

The surviving open step is now precise: compress a large family of hinged
histories to shared-endpoint cap/cup pairs with fibre
`2^{O(q log q)}`, using more information than the branch-sign word.  I found
no valid such compression.  Recursively convexifying the two split chains
also fails to give a closed recurrence: split chains have different left
endpoints, and their overlaps/cross-orientations retain unbounded data.

## 1. What the graph proof actually uses

Bal--Cutler--Pebody call `(v_1,...,v_q)` good when, for every i, all later
vertices lie in a single monochromatic neighborhood of `v_i`.  Nested bags
then give a product lower count.  Coloring each `v_i` by that neighborhood
color partitions the chosen vertices into monochromatic cliques.  A fixed
tuple of cliques supports at most `q!` orders, giving the factorial fibre.

Feige--Kenyon--Kogan's General Ramsey Tree uses the same two facts: every
root-to-level-l path splits into two monochromatic cliques, and a fixed
vertex set has at most `(l+1)!` path orders.

The first fact is exactly what fails for triple orientations.  A geometric
endpoint state only controls triples containing its current endpoint pair;
it does not control triples among nonconsecutive vertices bearing the same
sign.

## 2. A geometric good-history count that does transfer

Fix two initial points `x_{-1}<x_0` and a future bag B of m points to their
right.  A t-addition **hinged history** is an ordered increasing sequence
`x_1<...<x_t` such that, for each `0<=i<t`, all of
`x_{i+1},...,x_t` have one common orientation relative to the current pair:

```
chi(x_{i-1},x_i,x_j) = sigma_i  for every j>i.
```

At a state with current pair and an ordered future bag, split the bag into
its negative and positive classes.  Choosing the j-th point of a class as
the next point retains the points of that class after it as the new bag.
This is an exact planar analogue of the nested-neighborhood history rule.

Let `h_t(m)` be the minimum number of t-addition histories over all such
states with m future points.  Then

```
h_1(m)=m,
h_t(m) >= min_{r+b=m}
          (sum_{j=0}^{r-1} h_{t-1}(j)
           + sum_{j=0}^{b-1} h_{t-1}(j)).          (H)
```

The following convenient finite bound follows by induction:

> **History lemma.** For `t>=1`, put `E_t=2^t-2`.  Then
>
> `h_t(m) >= 2^{-binom(t,2)} (m-E_t)_+^t/t!`.

For `t=1` this is equality.  Assuming the result for `t-1`, compare each
tail sum in (H) to the corresponding integral:

```
sum_{j=0}^{r-1}(j-E_{t-1})_+^{t-1}/(t-1)!
 >= (r-E_{t-1}-1)_+^t/t!.
```

For nonnegative x,y, convexity gives `x^t+y^t >= 2^{1-t}(x+y)^t`.
Because `r+b=m` and `E_t=2(E_{t-1}+1)`, substitution in (H) introduces
exactly the further factor `2^{1-t}`.  This proves the lemma.

Take

`t=floor(log_2 m - 2 log_2 log_2 m)`.

Then `E_t=o(m)`, while Stirling gives `log_2(t!)=O(t log t)`.  Hence

```
log_2 h_t(m)
 >= t log_2 m - binom(t,2) - log_2(t!) - o(t)
 = (1/2)(log_2 m)^2 - O(log m log log m).          (HM)
```

Thus the desired coefficient-one-half history mass exists in every ordered
point set, before any use of the four-point signotope axiom.

## 3. The same-sign projection is false

Consider the exact rational points

```
(0,0), (1,93), (2,126), (3,199), (4,232), (5,255).
```

They are in general position.  Starting with the pair `(0,1)`, the entire
increasing sequence is a hinged history with branch signs

```
(-,+,-,-).
```

Nevertheless the negative-class vertices `0,2,3` have

`chi(0,2,3)=+`.

Therefore the vertices at negative history levels do not form a cap.  This
is the exact point at which the graph proof breaks: in a good graph history,
the color attached to an earlier vertex controls all its edges to later
same-color vertices; here the sign attached to a level controls only triples
containing that level's current hinge pair.

The witness satisfies the one-change axiom because it comes from rational
coordinates, so passage from arbitrary triple colorings to realizable
signotopes does not repair the issue.

## 4. Hinged need not even be split

The five exact rational points

```
(0,0), (1,41), (2,42), (3,93), (4,134)
```

form a hinged history with sign word `(-,+,-)`.  Exhausting every cap A and
cup U sharing the rightmost point shows that no pair satisfies

`A union U = {0,1,2,3,4}`.

Thus a hinged history is not automatically a split polygon.  Any proposed
map "history -> its split support" is undefined already at five points.
Adding a bounded number of state bits might repair individual histories,
but no canonical repair with subquadratic fibre follows from the hinge word.

## 5. Split and hinged sets can have a linear convexity deficit

There is a transparent infinite rational family.  Let `n>=4`, `M>2n`, and
choose alternating signs `sigma_i in {-1,+1}` for `0<=i<=n-3`.  Put

```
x_i=i,
y_i=sigma_i M^(n-i)  for i<=n-3,
y_{n-2}=y_{n-1}=0.
```

A sufficiently large rational shear can be added if increasing y-order is
desired; orientations are unaffected.  Dominance of the earliest power of M
gives, for every `i<j<k`,

```
chi(i,j,k)=sigma_i.                               (F)
```

(The determinant's `y_i` term has magnitude at least `M^(n-i)`, while the
sum of later terms is less than `2n M^(n-i-1)`.)  Hence the full sequence is
a hinged history: every future vertex has sign sigma_i relative to `(i,i+1)`.

It is also a split polygon covering all n vertices.  Take the rightmost
vertex in both chains; put every negative-sigma vertex in the cap and every
positive-sigma vertex in the cup, assigning the final unlabelled vertex as
needed.  By (F), every triple in either chain has the sign of its least
vertex, hence the required constant sign.

But a convex subset is the union of a cap and cup with the same two
endpoints l<r.  If `sigma_l=-`, the cup has size at most two: any third
cup point would form a triple whose least vertex is l and hence has negative
sign.  Every cap vertex other than its two largest vertices must have
negative sigma, again by (F).  The case `sigma_l=+` is symmetric.  Counting
the alternating signs in the relevant suffix proves that the largest convex
subset has size

```
ceil(n/2)+1  (up to parity convention),
```

as confirmed exactly for `4<=n<=14`; in particular the deficit is
`floor(n/2)-1`, not `O(1)`.  Examples begin

```
n:                  4 5 6 7 8 9 10 11 12 13 14
largest convex set: 3 4 4 5 5 6  6  7  7  8  8
```

This falsifies both shortcuts requested in the task:

* a hinged configuration need not have all but O(1) points convex;
* even a split configuration need not have all but O(1) points convex.

## 6. Can one recursively convexify the two split components?

The preceding family explains why the obvious recursion stalls.  A split
support consists of a cap and cup sharing only the **right** endpoint.  To
make a convex polygon, the two boundary chains must share both endpoints.
Selecting or recursively convexifying many points inside each chain does not
force their left endpoints to agree.  In the family (F), the discrepancy is
not local: it persists across Theta(n) alternating levels.

Moreover, the data needed to repair one split support are not captured by
the two component cardinalities.  One must know cross-orientations between
the chosen cap and cup vertices to decide which left endpoint can be shared.
After a recursive choice these cross-orientations change, so no recurrence
depending only on `(size, cap-count, cup-count)` closes.  The alternating
family realizes this obstruction at every scale and loses about half the
vertices at the first convexification.

This does not prove that a more elaborate weighted recursion is impossible;
it proves that a recursion charging only a constant deletion per split, or
using only component sizes/history colors, is false.

## 7. Fibre accounting: what is and is not rigorous

The history lemma supplies the lower side of an FKK-style sandwich.  A
length-q hinged history has an underlying q-element vertex set and an order,
so the completely trivial fibre over any fixed output support is at most
`q!`.  The problem is not ordering multiplicity but the lack of a valid
output: the sign classes are not caps/cups, a history may not be split, and a
split support need not yield a comparable convex set.

If one could define from every history a shared-endpoint cap/cup pair while
retaining all but `O(log q)` or otherwise only `2^{O(q log q)}` choices per
output, then (HM) would prove the endpoint multiplicity conjecture at
coefficient `1/2`.  The witnesses above rule out maps based only on:

1. the sign word;
2. the two sign classes;
3. the unrefined split support; or
4. constant-size endpoint repairs.

A successful map must use the full nested bag/order-type data and exploit
the one-change axiom quantitatively, not merely qualitatively.

## Bottom line

The FKK/BCP method transfers halfway.  The geometric nested-bag process has
the full coefficient-one-half multiplicity, with an explicit finite bound.
Its compression into convex subsets is precisely the missing theorem, and
the most natural split/hinged compressions are false even over exact rational
point configurations.

---

## 8. Second-stage attack: enriching the state

The natural next relaxation is to ask only that every hinged history be the
disjoint union of one cap and one cup, without requiring common endpoints.
Then a history would map to `(cap,cup)` with at most `2^q` choices of the
partition, proving a coefficient-`1/2` lower bound for the product `C(P)U(P)`.
This statement is also false, already for seven rational points.

Take `x_i=i` and

```
(y_0,...,y_6)=(-304,-291,-153,-180,-171,-36,-45).
```

The five hinge classes are respectively

```
(+,-,+,+,-);
```

that is, for each `0<=i<=4`, every `j>=i+2` has the displayed common sign
`chi(i,i+1,j)`.  All 35 determinants are nonzero.  Exhausting all `2^7`
colorings of the vertices finds no coloring for which the negative class is
a cap and the positive class is a cup.  The largest convex subset happens to
have six points, so this is specifically a failure of the two-chain cover,
not merely a tiny convexity number.

The coordinates were obtained by an exact recursive tangent construction:
given a rational hinged suffix, prepend a rational point strictly above or
below all finitely many secant thresholds.  Thus the obstruction is robust
under perturbation and is not a numerical accident.

### A useful propagation identity, but not enough

Let `v_0<...<v_{q-1}` be hinged with hinge signs `sigma_i`.  For
`i+1<j<k`, apply the signotope axiom to `(v_i,v_{i+1},v_j,v_k)`.  Its sign
sequence is

```
(sigma_i, sigma_i, chi(i,j,k), chi(i+1,j,k)).
```

Consequently

```
chi(i,j,k) != sigma_i
    ==> chi(i+1,j,k)=chi(i,j,k).                  (P)
```

So a defect from the local hinge color propagates one step to the right.
This is the exact extra information supplied by rank-three realizability.
The seven-point example satisfies (P) everywhere but remains uncolorable by
one cap and one cup.  Thus one-change propagation alone does not provide the
desired two-chain state invariant.

Hingedness alone does not even improve the local Erdős--Szekeres guarantee.
The seven integer points with `x_i=i` and

```
(y_0,...,y_6)=(26247,14652,13424,-8160,2640,2688,1680)
```

have hinge word `(+,-,+,-,-)`, all determinants nonzero, and no convex
five-subset (their largest convex subset has size four).  Thus a local
dichotomy of the form "either the history compresses, or the history itself
has an unusually large convex subset" is false at the first nontrivial
scale.  Any compensation must aggregate paths across many histories or use
points in their residual bags.

This persists through the sharp eight-point obstruction for a pentagon:

```
x_i=i,  (y_0,...,y_7)=(-10,-31,-11,-17,-5,-7,3,-5).
```

Its hinge word is the fully alternating `(+,-,+,-,+,-)`, every determinant
is nonzero, and exhaustive exact checking again finds maximum convex size
four.  Hence the class of hinged histories already contains an extremal
eight-point set with no convex pentagon.

### The hinge word itself has large hidden entropy

Enumeration of abstract rank-three signotopes compatible with a fixed full
hinged sequence gives the following maximum fibres over a hinge-sign word:

```
number of vertices:       3   4   5    6    7
maximum order-type fibre: 1   2   7   45  528
```

The maximum is attained by alternating hinge words.  These figures are not
an asymptotic theorem, but they warn against treating the binary word as the
state: already at seven vertices it suppresses hundreds of distinct legal
triple-sign patterns, including different cap/cup-cover behavior.

## 9. No contained-extraction map can have a small fibre

The alternating least-index family gives a rigorous obstruction to a much
broader class of history maps.  Use `N` alternating sign-labelled vertices
in the rational family (F), followed by the two terminal vertices.  Every
increasing subset is a hinged history.  Consider histories of even size q
chosen from the labelled vertices and containing exactly `q/2` vertices of
each sigma sign.  Their number is

```
binom(floor(N/2),q/2) binom(ceil(N/2),q/2).
```

As observed in Section 5, a convex subset whose least vertex has sign s can
contain, apart from its last two vertices, only vertices of sign s.  Hence
every convex subset *contained in one of these balanced histories* has size
at most `q/2+2`.

It follows by pigeonhole that any map which assigns to each balanced history
a convex subset contained in that history has a fibre of size at least

```
 binom(floor(N/2),q/2) binom(ceil(N/2),q/2)
 -------------------------------------------------- .          (FIB)
 sum_{j<=q/2+2} binom(N,j)
```

For `q=Theta(log N)`, the base-2 logarithm of (FIB) is

```
(q/2) log N - O(q log q),
```

which is quadratic in q, not `O(q log q)`.  This rules out **every**
subquadratic-fibre extraction whose output is required to use only history
vertices, regardless of how much finite state or one-change bookkeeping the
map carries.

A successful history proof must therefore be nonlocal: in the bad mixed
histories it must use convex subsets elsewhere in the ambient point set.  In
the least-index family such subsets abound (each sign class supplies an
exponential family of caps/cups), but finding an analogous abundance
dichotomy for a general realizable signotope is essentially the missing
lower-bound theorem.

## 10. Two-sided shared-endpoint histories

Maintaining a genuine convex subset at every step also loses the desired
branching.  If the current upper and lower chains share right endpoint t,
with preceding vertices a and b, a new point x to the right retains all
current vertices precisely when

```
chi(a,t,x)=-  and  chi(b,t,x)=+.
```

These are two simultaneous orientation conditions.  A one-condition hinge
step has a guaranteed half-bag; the shared-endpoint step is an intersection
and has no positive-fraction guarantee.  Points outside that intersection
can be incorporated only by popping old hull vertices, returning to the
large-fibre contained-extraction obstruction above.  The four-point
one-change axiom controls the order in which pops occur but does not prevent
them: the seven-point uncolorable history is an exact small witness.

Thus neither of the two evident enrichments closes:

1. carrying two unaligned cap/cup components fails at seven points;
2. carrying aligned hull chains destroys the half-bag recurrence.

This is the current precise stopping point for the direct history transfer.

All fixed witnesses, the least-index orientation formula, split covers, and
convexity numbers are checked with exact integer determinants by

```bash
python3 phase2/loop/erdos838/agent_geometry/audit_history_obstructions.py
```

## 11. A rigorous, but incomplete, nonlocal dichotomy

There is one useful global consequence of the run structure.  Let
`H_{q,<=r}(P)` be the number of q-vertex hinged subsets whose hinge-sign word
has at most r maximal constant runs.  Every constant run on hinge indices
`a,...,b` makes the vertex interval `v_a,...,v_{b+2}` a genuine cap or cup.
Indeed, the consecutive secant slopes on that interval are strictly
monotone, and hence every earlier secant slope lies strictly on the same
side of every later one.

The ordered tuple of maximal run chains reconstructs the history: adjacent
chains overlap in the two vertices at the sign change, and their sorted
union is the original history.  Therefore, writing `C(P),U(P)` for the
numbers of nonempty caps and cups,

```
H_{q,<=r}(P) <= sum_{j=1}^r (C(P)+U(P))^j
              <= r(C(P)+U(P))^r.                 (RUN)
```

Since every cap and every cup is itself convex,

```
V(P) >= max(C(P),U(P))
     >= (1/2)(H_{q,<=r}(P)/r)^(1/r).              (D1)
```

Thus histories with a bounded number of sign changes do compress globally;
the hard mass must lie in histories with an unbounded number of alternating
runs.  The exponent `1/r` in (D1) is too expensive for the target when
`r` grows, so this is a localization of the obstruction rather than the
desired theorem.

The exact least-index family shows what the hoped-for second side of the
dichotomy should look like.  Although its balanced histories defeat every
contained extraction, the ambient configuration is extremely far from
extremal.  If it has `N_-` negative and `N_+` positive sign-labelled
vertices followed by the two terminal vertices, then every subset of the
negative vertices together with either terminal subset is a cap, and the
positive analogue is a cup.  Consequently

```
V(P) >= max(2^(N_-+2)-1, 2^(N_++2)-1)
     = 2^(N/2+2-O(1)).                            (D2)
```

So the strongest known contained-compression obstruction automatically
triggers an exponentially larger *nonlocal* supply of convex subsets.  What
is not yet proved is the general stability statement suggested by (D2):
that enough alternating histories, or enough failures of same-sign
transitivity, force a comparable global cap/cup partition function.  The
seven-point witness shows that this cannot be proved by assigning only one
cap and one cup to each history; extra paths outside the selected history
must enter the charge.
