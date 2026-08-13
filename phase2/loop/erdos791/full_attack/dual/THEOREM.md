# Component–overlap dual bound for the three-tile model

## Result

Let `I,J,K` be finite sets of nonnegative integers with sizes `a,b,c`.  Suppose
every `q=0,...,m-1` satisfies

```text
q in I+J  or  q in I+K  or  (q-1 in J+K and q in J+K).       (1)
```

Then

```text
m <= ab + ac + bc - min(b,c).                                (2)
```

Consequently, with `ell=a+b+c`,

```text
m <= floor(ell^2/3) - floor(ell/3).                          (3)
```

This is a universal theorem for the exact three-tile predicate, not a
seed-local or bounded-search statement.  It strengthens the raw counting bound
`m <= ab+ac+bc-1` by a linear collision term.  Its asymptotic leading constant
is still `1/3`, so it does not resolve Erdős 791 or beat Kohonen by itself.

## Proof of the type-sensitive bound

Put

```text
X = (I+J) union (I+K),
S = J+K,
E = {q : q-1 in S and q in S}.
```

For a finite integer set `S`, let `r` be its number of maximal consecutive
components.  Every component of length `h` contributes `h-1` adjacent upper
endpoints, hence

```text
|E| = |S|-r <= bc-r.                                         (4)
```

Coverage of zero in (1) forces `0 in I` and at least one of `0 in J`, `0 in K`.

### Exactly `J` contains zero

Assume `0 in J` and `0 notin K`; write `s=min(K)>0`.  Because `0 in I` and
`0 in J`,

```text
K subset I+K subset X,       and       K subset J+K=S.        (5)
```

An element `k in K` fails to belong to `E` only if it is the first point of a
component of `S`.  The minimum `s` begins the first component, so among the
other `c-1` elements of `K`, at most `r-1` can begin components.  Therefore

```text
|X intersect E| >= max(0,c-r).                               (6)
```

Using `|X|<=ab+ac`, (4), and (6),

```text
|X union E|
 <= ab+ac + bc-r - max(0,c-r)
 =  ab+ac+bc-max(c,r)
 <= ab+ac+bc-c.                                               (7)
```

Since the `m` target indices lie in `X union E`, this proves (2) with loss `c`.

### Exactly `K` contains zero

Exchange `J,K` in the preceding argument.  The loss is `b`.

### Both contain zero

Now `I subset (I+J) intersect (I+K)`, so

```text
|X| <= ab+ac-a.                                               (8)
```

Put `U=J union K`.  Since `0 in I,J,K`, we have `U subset X intersect S`.
As in the preceding component argument, at most `r` elements of `U` can be
component starts, and therefore

```text
|X intersect E| >= max(0,|U|-r).
```

Together with (4) and (8), this gives

```text
|X union E| <= ab+ac+bc-a-max(r,|U|)
            <= ab+ac+bc-a-|U|.                               (9)
```

In particular the loss is at least `min(b,c)`.  In the two one-zero cases the
loss is respectively `c` or `b`, so the loss is again at least `min(b,c)`.
If `b=0` or `c=0`, (2) reduces directly to the relevant direct-sum product
bound.  This completes the proof.

The accounting in (4)–(7) is the useful “dual” interpretation: each component
start either spends one possible consecutive edge, or a non-minimal element of
the nonzero-offset family lies in both direct and consecutive coverage and
spends one union slot.  The two deficits add to at least the size of that
family.

## Exact optimization over type counts

Write `L=a+b+c` and, by symmetry, assume `b<=c`.  Since

```text
ab+ac+bc-b = (L^2-Q)/2,
Q = a^2+b^2+c^2+2b = a^2+(b+1)^2+c^2-1,                      (10)
```

the three displayed squares are positive integers with bases summing to
`L+1`.  The minimum sum of three integer squares with fixed sum `N` is attained
when the integers differ by at most one.  If this minimum is `H(N)`, (10)
gives `Q>=H(L+1)-1`.  Substitution into (10), separately for the three residues
of `L mod 3`, gives exactly

```text
max_{a+b+c=L} (ab+ac+bc-min(b,c))
  = floor(L^2/3)-floor(L/3).                                 (13)
```

Equality in this integer optimization is witnessed respectively by type
counts `(n,n,n)`, `(n,n,n+1)`, and `(n+1,n,n+1)` when `L` is `3n`, `3n+1`,
and `3n+2` (with the evident empty-type interpretation at `L=2`).

Empty `J` or `K` gives at most `floor(L^2/4)`, which is no larger.  The script
checks the integer optimization exhaustively through `L=250`.

## Exact two-state carry relaxation: optimum remains `1/3`

A natural finite-state refinement separates every type and every target sum by
parity.  Let `s_0,s_1` be the relaxed capacities of the even and odd parts of
`J+K`.  An adjacent edge ending in either parity consumes one sum of each
parity, so the relaxed consecutive capacity in each target parity is at most
`min(s_0,s_1)`.  Direct even/odd capacities are the corresponding parity
products.

This relaxation has the following exact rational primal point at density
`rho=1/3`:

```text
I_even=I_odd=J_even=J_odd=K_even=K_odd=1/6,
direct capacity in each parity     = 1/9,
J+K capacity in each parity        = 1/18,
consecutive capacity in each parity= 1/18,
required coverage in each parity   = rho/2 = 1/6.
```

It also has a matching elementary dual.  Summing the two parity coverage
constraints gives

```text
rho <= i(j+k) + 2 min(s_0,s_1)
    <= i(j+k) + jk
    =  ij+ik+jk
    <= 1/3,
```

where the final inequality has the exact SOS certificate

```text
1/3-(ij+ik+jk)
  = ((i-j)^2+(i-k)^2+(j-k)^2)/6 >= 0
```

for `i+j+k=1`.  Thus the naive mod-2 carry model is solved exactly, but it
provably cannot lower the leading `1/3` ceiling.  More states are useful only
if they retain compatibility between the same placements across convolution
cells; independent bin capacities will repeat this false freedom.

## Prefix hierarchy and failed completeness bridge

For every `t<=m`, let

```text
a_t = |I intersect [0,t-1]|,
b_t = |J intersect [0,t-1]|,
c_t = |K intersect [0,t-1]|.
```

Every witness for an index below `t` uses coordinates below `t`, so applying
(2) to the restricted sets gives the necessary finite-state hierarchy

```text
t <= a_t b_t + a_t c_t + b_t c_t - min(b_t,c_t).             (14)
```

This hierarchy is **not sufficient**.  The realizable profile

```text
I=[0,6], J=[0,5], K=[0,6]
```

satisfies (14) for every `t<=127`, and its terminal type bound is 127, but its
true tile prefix is only 13.  Thus a bin/count LP based only on cumulative
populations can falsely admit a density near `1/3`; it needs convolution/carry
compatibility, not merely prefix capacities.

## Sharpness and adversarial checks

The type-sensitive bound cannot be lowered by even one universally.  For every
`b>=1`, take

```text
I={0},  J=[0,b-1],  K={b}.
```

Then `I+J=[0,b-1]`, `I+K={b}`, and consecutive `J+K` coverage is
`[b+1,2b-1]`.  Hence `m=2b`, exactly equal to (2).

`collision_bound.py` additionally checks (2) over all 98,304 normalized triples
of subsets of `[0,5]`; 76 attain equality.  Because the both-zero proof is the
subtle case, it was separately checked on all 2,097,152 triples of zero-containing
subsets of `[0,7]`.  The script also reproduces the exact type envelope through
250 and emits a record-target census in `DUAL_RESULTS.json`.

## Consequences for the finite record targets

For `ell=18,...,24`, raw capacity counting eliminates 450 of the 706 canonical
positive `J/K`-unordered splits.  Bound (2) eliminates 496, an additional 46
without SAT.  At the priority `ell=20,m=116` target it eliminates 66 of 90
splits, leaving 24.  At `ell=42,m=511` it eliminates 294 of 420, leaving 126.

These eliminations are exact global nonexistence results for the excluded type
splits.  They do not constrain the main balanced splits enough: the type-free
envelope at `ell=20` is 127, while (2) gives 126 for the priority `(6,7,7)`
split; it gives 544 for Kohonen's `(8,17,17)` split at `ell=42`.
