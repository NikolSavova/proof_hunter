# Component-surplus pair recursion: exact entropy deficit and a realizable stress family

**Date:** 2026-08-14.  All logarithms are base two.

## 1. Verdict

A component-density surplus does not by itself give a capped two-output
entropy telescope for repair records.  The obstruction survives the full
ACP correlation.  The source--target projection used by marginal recursion
can lose quadratic entropy even when the retained target component has a
fixed positive density surplus; the best pair of direct projections still
loses `Theta(r)` blocker bits, which is fatal to a `2^o(r)` decoder.

For a record `(R,I,p)`, the ordinary source and target faces are

```text
A=R union I,                 T=R union {p}.          (1)
```

Their exact two-projection deficit is

```text
2H(R,I,p)-H(A)-H(T)
 =H(I,p|R)-I(I;p|R).                                (2)
```

Thus conditional near-product structure makes this projection recursion
*worse*, not better: when `I` and `p` are independent given `R`, the missing
amount is all of `H(I,p|R)`.

An unequal-alphabet version of ACP Proposition 26 realizes this sharply.
For every sufficiently divisible `L`, it has rank `r=L/2+O(1)`, record
entropy `3L^2/8+L`, a retained-target marginal whose density exceeds the
record density by `1/2-o(1)`, but projection deficit

```text
3L^2/16+L=Theta(r^2).                               (3)
```

Consequently a capped proof of the component-surplus branch must retain internal
tangent/face capacity while it recurses.  Recursing only on the denser
marginal and treating the other component as a fibre loses a leading
quadratic term.  This is not a counterexample to Erdős 838: the planar
microblocks contain additional internal convex faces.  It is a realizable
obstruction showing that the proposed two-output entropy telescope is
equivalent to recovering precisely that internal all-interval capacity.

## 2. Exact projection identity

Let `G` be any distribution on injective repair records `(R,I,p)`.  No
independence or uniformity is assumed.

> **Lemma 1 (two-projection deficit).**  Suppose the canonical tangent tags
> make the decompositions `A=(R,I)` and `T=(R,p)` recoverable.  Then
>
> ```text
> 2H(G)-H(A)-H(T)
>   =H(I,p|R)-I(I;p|R)
>   =H(I|R,p)+H(p|R,I).                              (4)
> ```

**Proof.**  Since the record is the triple `(R,I,p)`,

```text
H(A)=H(R,I),                 H(T)=H(R,p),            (5)
```

where canonical tangent data distinguishes the displayed components.  By
the entropy chain rule,

```text
H(R,I)+H(R,p)
 =2H(R)+H(I|R)+H(p|R),                              (6)
2H(R,I,p)
 =2H(R)+2H(I,p|R).                                  (7)
```

Subtracting (6) from (7) and using

```text
I(I;p|R)=H(I|R)+H(p|R)-H(I,p|R)                    (8)
```

proves the first equality.  Expanding the two conditional entropies in the
last expression proves the second.  `square`

Without recoverable markings one only has `H(A)<=H(R,I)` and
`H(T)<=H(R,p)`, so the left side of (4) is **at least** the displayed
deficit.  The product construction below uses disjoint labelled
macroblocks, so its decompositions are recoverable and equality holds.

For two independent records `g,h`, the natural output `(A_g,T_h)` has
entropy `H(A)+H(T)`.  Hence (4) is exactly its collision-entropy deficit
relative to the demand `2H(G)`.  Alternating the two orientations does not
alter the deficit.

For clarity, using two sources instead has deficit

```text
2H(G)-2H(A)=2H(p|R,I),                               (8a)
```

and using two targets has deficit `2H(I|R,p)`.  Thus the best choice among
the three direct projection types has deficit

```text
2H(G)-2 max{H(A),H(T)}.                              (8b)
```

This can be smaller than (4).  In the stress family below, two source
outputs lose only the two blockers, namely `2L=Theta(r)` bits.  That is
subquadratic and harmless for a leading-coefficient argument, but it is
still not `o(r)` and therefore does not close capped Hall.  The quadratic
claim in this artifact concerns the mixed source--target recursion forced
when one follows the denser marginal, not every conceivable two-face map.

## 3. A fixed-surplus planar product cell

Take `L` divisible by four and put

```text
a=b=L/4,                     u=3L/4,                (9)
```

where `a` is the number of retained internal macroblocks, `b` the number of
hidden internal macroblocks, every such block has alphabet size `2^u`, and
the outward-blocker cloud has size `2^L`.

Use the fixed-outer-cell lens construction of ACP Proposition 26, allowing
different finite microcluster sizes.  Its proof uses only strict open sign
conditions, so the retained blocks, hidden blocks, and apex cluster may be
assigned the sizes above independently.  Every triple

```text
(R,I,p) in [2^u]^a times [2^u]^b times [2^L]        (10)
```

is an outward-successor repair record with common canonical prefix,
`A=R union I` convex, and `T=R union {p}` convex.  The three coordinates in
(10) are independent under the uniform record law.

The exact entropies are

```text
H(G)=(a+b)u+L=3L^2/8+L,                            (11)
H(T)=au+L=3L^2/16+L,                               (12)
H(I)=bu=3L^2/16.                                   (13)
```

Ignoring the `O(1)` fixed guards, their rank parameters are

```text
R_0=a+b+1=L/2+1,       tau=a+1=L/4+1,       kappa=b=L/4.
                                                               (14)
```

Put `rho=H(G)/R_0`.  Relative to the common baseline `u=3L/4`,

```text
rho-u=L/(2L+4),
H(T)/tau-u=L/(L+4).                                  (15)
```

Therefore the retained-target density surplus is exactly

```text
H(T)/tau-rho
 =L^2/((L+4)(2L+4)) -> 1/2.                         (16)
```

This is a genuine fixed-gap component-surplus branch.  But conditional
independence in (10) gives

```text
I(I;p|R)=0,
H(I,p|R)=bu+L=3L^2/16+L.                            (17)
```

Equations (4) and (17) prove the quadratic deficit (3).

## 4. Why the local endpoint code also detects the obstruction

Each internal terminal block has size `q=2^u`, whereas the blocker cloud
has size `y=2^L`.  The symmetric one-slot decoder of
`TWO_RECORD_UNCROSSING.md` has exact fibre

```text
K=ceil(q^2 y^2/s(q)^2),
s(q)=1+q+binom(q,2).                                  (18)
```

Since `s(q)<=q^2` and `s(q)>=q^2/2`,

```text
2^(2(L-u)) <= K <= 4*2^(2(L-u))+1.                   (19)
```

Here `L-u=L/4`, so

```text
K=2^(L/2+O(1))=2^Theta(r),                           (20)
```

not `2^o(r)`.  The blocker surplus is therefore visible in both exact
audits: marginal projection loses `Theta(r^2)` entropy, while a single
terminal endpoint spend retains an exponential-in-`r` fibre.

The actual planar configuration is not an HTR counterexample.  It has `a+b`
internal strong blocks and all their descendant cap/cup and multi-interval
faces.  Any successful component-surplus recursion must use those faces to
transport the residual law in (17).  Forgetting them reduces the realizable
cell to the already-killed scalar/vector recurrence.

## 5. Precise remaining theorem

The component-surplus branch needs more than the rank-slice statement
“`T` has higher density.”  A sufficient recursive theorem must attach to
that child a second face-valued code for the conditional law `(I,p)|R`, with
total collision exponent

```text
H(I,p|R)-I(I;p|R)+o(r).                              (21)
```

In the product cell, (21) is supplied only by multiplying internal tangent
reservoirs across blocks.  In a general ACP family this is exactly the
hierarchical all-interval/strong-block gate.  Thus the component-surplus
pair recursion has not been independently closed; the stress family proves
that any purported proof using only marginal entropy, rank slicing, and the
two direct projections is false by a quadratic margin.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_all_interval_isoperimetry/verify_component_surplus_pair.py
```

The script checks (11)--(20) with exact rational arithmetic for a range of
divisible `L`.
