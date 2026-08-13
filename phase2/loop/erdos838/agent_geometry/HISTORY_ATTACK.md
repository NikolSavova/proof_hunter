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
