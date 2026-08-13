# Erdős 838: a finite-state barrier for heterogeneous vertical blow-ups

## Result

The natural finite-state extension of the paper's construction cannot improve
the base-2 coefficient `1/2`.  This remains true when

* different macro-points receive different recursively defined child types;
* the macro order type depends on the parent type;
* some types are reflected, so their cap and cup profiles are anti-aligned;
* the rule is periodic or otherwise governed by any fixed finite automaton;
* different parent types have different branching numbers, so block sizes at
  the same depth need not be equal;
* the rational coordinates are perturbed without changing the prescribed
  macro, micro, and mixed-triple orientations.

The proof uses the two-block terms that are usually discarded as lower-order
in an upper-bound calculation.  Inside a recurrent component they couple the
cap exponent of one child to the cup exponent of another.  The cup--cap
theorem forces the sum of those two exponents to be at least `log_2 r`.

This does **not** rule out infinitely many states, depth-dependent rules that
cannot be folded into a finite automaton, or mixed-triple signatures other
than the vertical rule.  Those are now the precise escape routes for a
blow-up construction below `1/2`.

All logarithms below are base two.

## 1. Finite-state vertical systems

Fix an integer `r >= 2` and a finite state set `T`.  For each state `p` choose

1. an `r`-point macro configuration `S_p=(s_{p,1},...,s_{p,r})` in increasing
   x-order; and
2. a label map `ell_p:{1,...,r}->T`.

Put `Q_p(0)` equal to a singleton.  Recursively, `Q_p(d)` is the vertical
composition whose macro set is `S_p` and whose block at macro-position `i` is
a sufficiently small copy of `Q_{ell_p(i)}(d-1)`.  Thus every `Q_p(d)` has
exactly `r^d` points.  The mixed orientations are

* negative when the first two points are in one block;
* positive when the last two points are in one block.

As in the paper, a separate sufficiently small rational epsilon can be chosen
at every finite node.  Hence the recursively specified order type is exactly
realizable for every finite depth.

Write `C_p(d), U_p(d), W_p(d)` for the nonempty cap, cup, and convex-subset
counts of `Q_p(d)`.  If `B` is a subset of macro-indices, write `min B` and
`max B` for its first and last indices.

### Proposition 1 (exact heterogeneous recurrence)

For every state `p` and depth `d>=1`, with `n=r^(d-1)`,

```
C_p(d) = sum_{B cap in S_p}
             C_{ell_p(min B)}(d-1) n^(|B|-1),

U_p(d) = sum_{B cup in S_p}
             U_{ell_p(max B)}(d-1) n^(|B|-1),

W_p(d) = sum_{i=1}^r W_{ell_p(i)}(d-1)
       + sum_{B convex in S_p, |B|>=2}
             C_{ell_p(min B)}(d-1)
             U_{ell_p(max B)}(d-1) n^(|B|-2).
```

#### Proof

The classification in the paper's composition lemma is blockwise and does
not require the blocks to have the same internal order type.  A cap meeting
at least two blocks has an arbitrary nonempty cap in its first occupied block
and one point in every later occupied block.  The cup statement is reflected.
A cross-block convex set has a cap in its first block, a cup in its last
block, and one point in every intermediate block.  Conversely these choices
form the upper and lower hull chains.  All child blocks have the common size
`n`, giving the formulas.  `square`

The script `heterogeneous_audit.py` independently checks these identities
from exact rational coordinates.  Its macro set is nonconvex, its unequal
child types are a 3-cup and a 4-cap, and the labels are `A,B,B,A`.  It obtains

```
epsilon=1/100
direct C,U,W=(498, 323, 1562)
formula C,U,W=(498, 323, 1562)
PASS
```

## 2. Cap and cup growth as maximum cycle means

For macro-position `i` define

```
alpha(p,i) = max {|B|-1 : B is a cap of S_p, min B=i},
beta(p,i)  = max {|B|-1 : B is a cup of S_p, max B=i}.
```

Singletons make both maxima well-defined.  Form the directed transition graph
with an edge `p -> ell_p(i)` for every `p,i`.  Give this edge cap-weight
`alpha(p,i)` and cup-weight `beta(p,i)`; parallel edges are allowed.

Let `a_p(d)` and `b_p(d)` be the largest cap and cup sizes in `Q_p(d)`.
Proposition 1's same classification gives the exact max-plus recurrences

```
a_p(d) = max_i (a_{ell_p(i)}(d-1) + alpha(p,i)),
b_p(d) = max_i (b_{ell_p(i)}(d-1) + beta(p,i)).       (1)
```

Let `K` be a sink strongly connected component of the transition graph.  Let
`rho_C` and `rho_U` be the maximum cycle means in `K` for the alpha- and
beta-weights.  Standard path decomposition (delete cycles, leaving a bounded
simple path) applied to (1) gives, uniformly for `p in K`,

```
a_p(d) = rho_C d + O(1),
b_p(d) = rho_U d + O(1).                            (2)
```

There is an equally useful enumerative version.  Grouping the first formula
of Proposition 1 by its first macro-index gives fixed positive polynomials of
degrees `alpha(p,i)`.  Consequently

```
log C_p(d)
 = max_i [log C_{ell_p(i)}(d-1)
          + alpha(p,i)(d-1) log r] + O(1).          (3)
```

The error is uniform because there are finitely many fixed polynomials and
states.  Expanding (3) along a path produces weighted prefix sums.  If
`x_1,x_2,...` are the edge weights, then

```
sum_{t=1}^d (d-t)x_t = sum_{s=1}^{d-1}(x_1+...+x_s).
```

Every prefix weight is at most `rho_C s+O(1)`, while repetitions of a
maximum-mean cycle attain this up to `O(1)`.  Therefore

```
log C_p(d) = (rho_C log r / 2)d^2 + O(d),
log U_p(d) = (rho_U log r / 2)d^2 + O(d).           (4)
```

No probabilistic or smooth asymptotic assumption enters (2)--(4): all edge
weights are fixed nonnegative integers.

## 3. The barrier theorem

### Theorem 2 (finite-state coefficient barrier)

For every finite-state vertical system above and every initial state `p`,

```
liminf_{d->infinity}
  log W_p(d) / (log |Q_p(d)|)^2 >= 1/2.             (5)
```

Thus no finite-state choice of nonuniform child labels, reflected types,
type-dependent templates, or periodic anti-alignment can beat the paper's
coefficient `1/2`.

#### Proof

First take `p` in a sink strongly connected component `K`.  Apply the
Erdős--Szekeres cup--cap theorem to the `r^d`-point set `Q_p(d)`.  In the
notation of (2),

```
r^d <= binom(a_p(d)+b_p(d)-2, a_p(d)-1)
    <= 2^(a_p(d)+b_p(d)-2).
```

After division by `d` and passage to the limit, this yields

```
rho_C + rho_U >= log r.                            (6)
```

Because `K` is a sink, every child label of every parent in `K` also lies in
`K`.  Choose any two macro-positions `i<j`.  The two-point macro-subset
`{i,j}` is convex, so Proposition 1 contains the term

```
C_{ell_p(i)}(d-1) U_{ell_p(j)}(d-1).
```

All states in `K` have the common cycle means `rho_C,rho_U`.  Equations (4)
and (6) therefore give

```
log W_p(d)
 >= ((rho_C+rho_U)log r/2)(d-1)^2 + O(d)
 >= ((log r)^2/2)d^2 + O(d).
```

Since `log |Q_p(d)|=d log r`, this proves (5) for `p in K`.

For an arbitrary initial state, follow a directed path of some fixed length
`h` into a reachable sink component.  The corresponding depth-`h` descendant
block is a copy of `Q_q(d-h)` for a state `q` in that component.  Every convex
subset of the descendant remains a convex subset of the whole set, so
`W_p(d)>=W_q(d-h)`.  A fixed shift of `d` does not change the normalized
quadratic coefficient.  This proves (5).  `square`

## 4. Unequal branching and unequal block sizes

The equal-`r` assumption makes the mechanism transparent, but it is not
needed.

### Theorem 3 (general finite-state vertical barrier)

Let state `p` have an arbitrary fixed macro size `r_p>=2`, macro order type
`S_p`, and labels `ell_p(1),...,ell_p(r_p)`.  Define `Q_p(d)` recursively as
before.  The different child states may now have different cardinalities at
the same depth.  Then, for every initial state `p`,

```
liminf_{d->infinity}
  log W(Q_p(d)) / (log |Q_p(d)|)^2 >= 1/2.         (7)
```

#### Proof

Fix the initial state `p_0`, discard states not reachable from it, and let `M`
be the resulting nonnegative integer substitution matrix

```
M[p,q] = number of positions i with ell_p(i)=q.
```

Every row sum is `r_p>=2`, so

```
M 1 >= 2 1,             M^d 1 >= 2^d 1.
```

Thus the spectral radius `Lambda=rho(M)` is at least two.  In Frobenius
normal form, `Lambda` is the maximum spectral radius of a diagonal strongly
connected block.  Choose a block `K` attaining it.  This component need not
be a sink.

The size vector is exactly `N(d)=M^d 1`.  Standard finite nonnegative-matrix
growth gives

```
log N_{p_0}(d) = d log Lambda + O(log d).          (8)
```

For completeness, a fixed transition path from `p_0` into `K`, followed by
growth inside `K`, gives the lower bound.  Frobenius normal form gives the
upper bound: passage through several diagonal blocks with the same spectral
radius contributes at most a fixed polynomial in `d`.

For `q in K`, put

```
I_q = {i : ell_q(i) lies in K}.
```

Strong connectivity makes `I_q` nonempty.  Define `R_q(0)` to be one point
and construct `R_q(d)` by retaining exactly the positions in `I_q`, placing
`R_{ell_q(i)}(d-1)` in them.  It is an induced subset of `Q_q(d)`.  Its size
vector is

```
m(d)=M_K^d 1,                                      (9)
```

where `M_K` is the irreducible diagonal block indexed by `K`.  Deleting
outgoing children leaves this diagonal block unchanged, so
`rho(M_K)=Lambda`.

Periodicity creates no exceptional depths.  Let `v>0` be a right Perron
vector of `M_K`, and choose constants `a,b>0` with

```
a v <= 1 <= b v
```

coordinatewise.  Positivity and `M_K v=Lambda v` give, for every `d>=0`,

```
a Lambda^d v <= M_K^d 1 <= b Lambda^d v.
```

Consequently, uniformly in `q in K` and at every depth,

```
log |R_q(d)| = d log Lambda + O(1).               (10)
```

For `q in K` and `i in I_q`, define

```
alpha(q,i) = max {|B|-1 : B is a cap in the restricted macro,
                              B subseteq I_q, min B=i},
beta(q,i)  = max {|B|-1 : B is a cup in the restricted macro,
                              B subseteq I_q, max B=i}.
```

Give the internal edge `q -> ell_q(i)` these cap and cup weights.  Let
`rho_C,rho_U` be their respective maximum cycle means on the strongly
connected internal multigraph.  If `a_q(d),b_q(d)` denote the largest cap and
cup sizes in `R_q(d)`, the block classification gives exactly

```
a_q(d) = max_{i in I_q}(a_{ell_q(i)}(d-1)+alpha(q,i)),
b_q(d) = max_{i in I_q}(b_{ell_q(i)}(d-1)+beta(q,i)).      (11)
```

Deleting cycles from a path and repeating a maximum-mean cycle yields,
uniformly in `q in K`,

```
a_q(d)=rho_C d+O(1),       b_q(d)=rho_U d+O(1).   (12)
```

The heterogeneous form of Proposition 1 replaces each power of the common
block size by a product of the actual intermediate block sizes.  For example,

```
C_p(d) = sum_{B cap in S_p}
 C_{ell_p(min B)}(d-1)
 product_{i in B, i != min B} N_{ell_p(i)}(d-1). (13)
```

For the restricted construction, (10) says that every additional occupied
block at depth `d-1` contributes
`(d-1)log Lambda+O(1)` to the logarithm.  Grouping terms by their first
occupied block therefore gives

```
log C(R_q(d))
 = max_{i in I_q}[log C(R_{ell_q(i)}(d-1))
                  +alpha(q,i)(d-1)log Lambda]+O(1),       (14)
```

with a uniform error, and analogously for cups.  Expanding (14) along a path
with edge weights `x_1,...,x_d`, its quadratic part is

```
log Lambda sum_{t=1}^d (d-t)x_t
 = log Lambda sum_{s=1}^{d-1}(x_1+...+x_s).
```

Every length-`s` prefix has weight at most `rho_C s+O(1)`, and a bounded
entrance followed by repetitions of a maximum-mean cycle attains this up to
`O(1)`.  The per-step log-sum error contributes only `O(d)`.  Hence,
uniformly in `q in K`,

```
log C(R_q(d)) = (rho_C log Lambda/2)d^2 + O(d),
log U(R_q(d)) = (rho_U log Lambda/2)d^2 + O(d).   (15)
```

Apply the cup--cap theorem to `R_q(d)`.  Equations (10) and (12) give

```
|R_q(d)|
 <= binom(a_q(d)+b_q(d)-2, a_q(d)-1)
 <= 2^(a_q(d)+b_q(d)),
```

and therefore

```
rho_C+rho_U >= log Lambda.                        (16)
```

Some row of `M_K` has internal row sum at least two.  Otherwise every row
sum would be one; irreducibility and integrality would make `M_K` the
permutation matrix of one directed cycle, whose spectral radius is one,
contrary to `Lambda>=2`.  Fix such a state `q_*` and two distinct retained
positions `i<j`.  They may have the same label.  The two-point macro-index set
is convex, so every cap of `R_{ell(i)}(d-1)` together with every cup of
`R_{ell(j)}(d-1)` gives a distinct convex subset of `Q_{q_*}(d)`.  By
(15)--(16),

```
log W(Q_{q_*}(d))
 >= log C(R_{ell(i)}(d-1))+log U(R_{ell(j)}(d-1))
 >= ((log Lambda)^2/2)d^2+O(d).                  (17)
```

Uniformity of (15) matters here: the maximum cap and cup cycles need not pass
through the two selected child states, but strong connectivity supplies
bounded entrances whose cost is absorbed by `O(d)`.

Finally, there is a fixed transition path of some length `h` from `p_0` to
`q_*`.  Following the corresponding child occurrence at each level identifies
a descendant block in `Q_{p_0}(d)` isomorphic to `Q_{q_*}(d-h)`.  Hence

```
W(Q_{p_0}(d)) >= W(Q_{q_*}(d-h)).                 (18)
```

Combining (8), (17), and (18),

```
log W(Q_{p_0}(d)) / (log |Q_{p_0}(d)|)^2
 >= [((log Lambda)^2/2)(d-h)^2+O(d)]
    /(d log Lambda+O(log d))^2
 = 1/2-o(1).
```

This proves (7).  `square`

No sink or primitivity assumption was used.  If several reachable components
have the same maximal spectral radius, the polynomial factor already allowed
in (8) is harmless on the log-squared scale.

## 5. What the computation did and did not find

`multitype_search.py` implements Proposition 1 and the exact maximum-cycle-
mean coefficient for two states.  It exhaustively enumerates all two-state
label maps for sampled realizable macro order types and their vertical
reflections.  The finite-depth log-sum-exp recurrence independently converges
to the tropical value.  As Theorem 2 predicts, no sub-`1/2` system exists.

For the six-point balanced Pascal macro `T_{4,2}`, every tested labeling has
coefficient

```
4 / (2 log_2 6) = 0.7737056144690833...,
```

including mirror-paired rules designed to put cap-rich and cup-rich types in
opposite positions.  The label invariance in this balanced example is not the
proof of Theorem 2; it is only a useful executable sanity check.

From this directory, the reproducible checks are

```
python3 -m py_compile multitype_search.py heterogeneous_audit.py
python3 heterogeneous_audit.py
python3 multitype_search.py --r 5 --samples 3 --depth 40 --top 5 --mirror
```

The first search column is the exact tropical coefficient; the last is the
finite-depth ratio, which approaches it with the expected linear correction.

## 6. Consequence for the next construction search

The obstruction is not merely that a particular two-state idea failed.  At a
recurrent scale, the cup--cap theorem prices cap and cup growth jointly, and
the convex two-block term couples them before endpoint anti-alignment can hide
one of the two rates.  A strict improvement must therefore break at least one
of the theorem's structural inputs:

1. use genuinely depth-growing state complexity;
2. use genuinely depth-dependent thinning or scale choices not captured by a
   finite substitution matrix; or
3. change the mixed-triple geometry so that a two-block convex set is not
   counted by a cap of the left child times a cup of the right child.

The third route is the most geometric.  Merely rotating, reflecting, or
periodically relabeling templates inside the existing vertical order-type
composition cannot work.
