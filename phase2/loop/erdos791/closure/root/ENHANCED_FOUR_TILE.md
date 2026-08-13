# Two omitted phase-one pairings

Let `t` be even, `B=t^2`,

```text
V=[0,t],  H={it:0<=i<t},  T={j(t-1):0<=j<=t},  T1=T+1.
```

Besides the phase lemmas in `campaign/tiles/RESULT.md`, one has

```text
(V+T1) union (V+T1+B) contains [B,2B-1],
(H+T1) union (H+T1+B) contains [B,2B-1].
```

For the first assertion, the intervals `j(t-1)+[0,t]` overlap and show
`V+T=[0,B]`.  Hence `V+T1=[1,B+1]`; two translates contain the required
block.

For the second, the unshifted reflected-diagonal lemma gives

```text
(H+T) union (H+T+B) contains [B,2B-1].
```

After shifting by one this contains `[B+1,2B]`.  The missing endpoint `B`
also belongs to `H+T1`, since

```text
B-1=(t-1)t+(t-1) belongs to H+T.
```

Thus the scalable five-list predicate can additionally certify square `q`
whenever either

```text
{q-1,q} subset I+L1,   or   {q-1,q} subset J+L1.
```

There are two further mixed-phase clauses.  Since `V+T=[0,B]`, a phase-zero
copy at macro position `q-1` supplies the left endpoint of square `q`, while a
phase-one copy at `q` supplies the rest.  Hence square `q` is also certified by

```text
q-1 in I+L0 and q in I+L1.
```

For the horizontal/reflected pair, one has

```text
(H+T+B) union (H+T+1) contains [B,2B-1].
```

Indeed write `x=at+b` with `t<=a<=2t-1` and `0<=b<t`.  If `b=0`, then
`x-B in H+T`.  For `b>0`, if `a+b>=2t-1`, use `j=t-b` to represent `x-B`;
if `a+b<=2t-1`, use `j=t-b+1` to represent `x-1`.  The corresponding
horizontal coefficient lies in `[0,t-1]`.  Thus one may also certify `q` by

```text
q-1 in J+L1 and q in J+L0.
```

`enhanced_four_tile_cp_sat.py` encodes this enlarged predicate exactly and
checks any witness by literal expansion for several even `t`.
