# Erdős #791: structural generalized-Mrose lane

## Outcome

No placement beating Kohonen was found.  This lane does give a rigorous
description and obstruction for the entire natural block family underlying his
construction, an exact audit of 9,453,780 nearby coherent AP/interval layouts,
and a smaller `(ell,m)=(20,115)` near-record target.  A first claimed
radius-three exclusion around that target was invalidated by adversarial audit
(see Section 4).  These are negative structural results, not a resolution of
Erdős #791.

## 1. The hidden block family

Let `h>=1`, `b>=h+1`, `n>=h`, and `r>=0`, and put

```text
u = (h+1)n + 2h,
B = 2u + h(b-h-1),
D = u + hb + 1.
```

Define

```text
I = {0,h} union (u + h*[0,b-1]),
J = 2h + (h+1)*[0,n-1],
K = [0,h-1] union Union_{v=0}^{r-1} [B+vD,B+vD+h].
```

Then the tile predicate

```text
q in I+J  or  q in I+K  or  {q-1,q} subset J+K
```

certifies `[0,m-1]`, where

```text
ell = n+b+h+2+r(h+1),
m   = 2u+h(b-h-1)+r(u+hb+1).
```

Kohonen's placement is exactly `(h,b,n,r)=(5,6,17,2)`.

### Proof of coverage

The elementary bounded coin lemma is

```text
T={hi+(h+1)j: 0<=i<b, 0<=j<n}
  contains [h(h-1), h(b-1)+(h+1)(n-1)-h(h-1)].
```

Indeed, every integer at least `h(h-1)` is a nonnegative combination of the
coprime integers `h,h+1` (the Frobenius number is `h(h-1)-1`), and its canonical
representation can take the `h`-coefficient `i` in `[0,h]`. Write it as
`x=hi+(h+1)j`. If `j<n`, it is already in the required box. Otherwise choose
the least `k` with `j-hk<=n-1`; then `j-hk>=n-h>=0`. Replace `(i,j)` by
`(i+(h+1)k,j-hk)`, which represents the same integer. If its first coefficient
were at least `b`, then `x>=hb+(h+1)(n-h)`, one beyond the asserted upper
endpoint in the worst case, a contradiction. Thus both coefficients lie in
the required ranges. Reflection about `max(T)` gives the other endpoint.

Now `I_low+K_low=[0,2h-1]`.  For every `j in J`, the two direct squares at
`j,j+h` together with the consecutive `J+K_low` parallelograms cover
`[j,j+h]`.  Successive `j` differ by `h+1`, so this covers through `u-1`.
The high AP in `I` plus `K_low` covers `[u,u+hb-1]`.  The bounded coin lemma
shows that `I_high+J` continues the coverage through

```text
B-1 = 2u+h(b-h-1)-1.
```

Finally, a high K block `[C,C+h]` gives direct `I_low+K` coverage through
`C+2h`, consecutive `J+K` coverage through `C+u-1`, and direct `I_high+K`
coverage through `C+u+hb=C+D-1`.  Thus the `r` blocks beginning at
`B,B+D,...` concatenate without gaps.

## 2. Exact obstruction inside the whole family

**Proposition.** Every member of the block family satisfies

```text
m/ell^2 <= 85/294,
```

with equality only at Kohonen's parameters `(h,b,n,r)=(5,6,17,2)`.

For fixed `ell,h,r`, replacing one unit of `b` by one unit of `n` increases
`m` by `h+r+2>0`.  Hence the maximum has `b=h+1`.  Write

```text
a=h+1,  s=r+2,  L=ell,  c=s^2-s+2.
```

Then `n=L-sa-1`, `L>=(s+1)a`, and

```text
m = saL - ca^2 + 2a - s - 2.                         (1)
```

For `B=ca^2-2a>0`, maximizing `(saL-B)/L^2` over real `L>0` gives

```text
m/L^2 < s^2/[4(c-2/a)].                              (2)
```

The right side is at most `85/294` whenever

```text
a >= 680/(46s^2-340s+680).
```

The denominator is positive for every integer `s>=2`.  It leaves only these
finite exceptions: `s=2,a=2..3`; `s=3,a=2..9`; `s=4,a=2..12`;
`s=5,a=2..5`; and `s=6,a=2`.  For fixed `(s,a)`, (1) is unimodal in `L`,
with real maximum at

```text
L*=2(ca^2-2a+s+2)/(sa),
```

so checking the boundary `L=(s+1)a` and the two integers bracketing `L*` is
exhaustive.  The maxima in the five exceptional rows are respectively

```text
s=2: 32/121
s=3: 15/52
s=4: 85/294  (a,L)=(6,42)
s=5: 553/1936
s=6: 3/11.
```

This proves the proposition.  `family_analysis.py` independently constructs
and verifies the placements and exhausts 270,114 parameter tuples through
`ell<=100`; its output is `FAMILY_SEARCH_ELL100.json`.

## 3. Why the obvious mixed-radix blow-up loses density

Let a tile placement of size `ell` certify `m` squares, with every useful macro
coordinate normalized into `[0,m-1]`, and let an ordinary
finite additive 2-basis `X` of size `s` have `[0,R] subset X+X`.  Replacing
each of `I,J,K` by all translates at offsets `mX` certifies
`m(R+1)` squares and uses exactly `ell*s` typed segments: distinct radix blocks
are disjoint because their normalized coordinates lie in `[0,m-1]`. The local
tile witness is reused inside each mixed-radix block; at a block start, square
zero already has a direct `I+J` or `I+K` witness.

Thus the density is multiplied by `(R+1)/s^2`.  Counting unordered pairs gives
`R+1<=s(s+1)/2`, so every nontrivial (`s>=2`) blow-up multiplies density by at
most `(s+1)/(2s)<=3/4`.  It cannot improve Kohonen.  This rules out the most
natural composition/concatenation idea, though not every conceivable typed
composition.

## 4. Exact and computational audits

### Coherent AP/interval template at ell=42

`template_exhaust.cpp` exhausts

```text
I={0,5} union (is+id*[0,5]),
J=js+jd*[0,16],
K=[0,4] union [k1,k1+5] union [k2,k2+5]
```

over `is=96..130`, `id=4..7`, `js=6..14`, `jd=5..7`,
`k1=205..245`, and `k2=340..400`.  All 9,453,780 layouts were checked against
all 511 target squares.  The best encountered was Kohonen, with 510 of 511
squares and prefix 510; no `m=511` placement occurred.  Raw output:
`TEMPLATE_EXHAUST.txt`.

`structural_search.cpp` also makes coordinated AP-start, AP-spacing, interval-
start, and block-size moves.  A 2,000,000-proposal run found no improvement.

### Smaller one-square-short target

The family member `(h,b,n,r)=(3,4,7,1)` has

```text
(ell,m)=(20,115), counts (|I|,|J|,|K|)=(6,7,7).
```

Beating Kohonen at `ell=20` requires `m=116`, so this is another one-square
target but has less than half as many placement coordinates as `42,511`.
`sat_lean.py` attempted an independent clause-level CP-SAT encoding, but its
radius claims are **invalid**: it forces `0 in J` while measuring Hamming
distance from the unswapped family seed, whose `J` omits 0 and `K` contains 0.
Indeed the known valid `m=115` seed is `INFEASIBLE` under its radius-zero model.
Therefore `CP_SAT_20_116_RADIUS3.json` does not exclude the claimed radius-three
ball and is retained only as an audit artifact.  Radius four was likewise
`UNKNOWN` after 120 seconds, 3,085,209 branches, and
326,833 conflicts (`CP_SAT_20_116_RADIUS4.json`), so it yields no conclusion.
The unrestricted fixed-split search was also `UNKNOWN` after 60 seconds and
2,094,454 branches (`CP_SAT_20_116_6_7_7.json`).  For comparison, the natural
`(ell,m)=(26,195)` seed has split `(7,10,9)`; unrestricted target `m=196`
remained `UNKNOWN` after 180 seconds (`CP_SAT_26_196_7_10_9.json`).

The seed itself passes both the abstract tile verifier and literal `A_t+A_t`
checks in `family_20_115.json`.  As at `ell=42`, shifting the final K interval
right by one fills the new boundary square but transports the unique hole to
the former start of that interval (square 68 here).

## 5. Honest next mathematical move

The exact obstruction shows that adjusting the lengths of Kohonen's existing
modules cannot win: a record requires breaking a module seam, using a genuinely
non-AP block, or changing the tile alphabet.  The most economical remaining
finite target is unrestricted `(ell,m)=(20,116)`, not `(42,511)`.  The corrected
proof-producing model in `../sat/` now excludes replacement radii 1 through 4
around the `(6,7,7)` seed, but the unrestricted split remains open.  A global
SAT result for this fixed split should therefore precede more search at 42.
An UNSAT result for all type splits at ell 20 would not resolve #791, but a SAT
result would immediately improve the asymptotic record.
