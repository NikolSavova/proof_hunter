# Erdős #791 closure attempt: phased reflected-direction theory

## Outcome

No construction in this lane beats Kohonen's `85/294`.  The closure attempt
did, however, produce three exact results:

1. the complete set of minimal one/two-translate macro clauses used here for
   the two phases of the reflected segment, including four clauses omitted in
   the first campaign;
2. a perfect periodic alternating-phase `K/L` gadget with an exact literal
   certificate, together with a `1/4` obstruction for that gadget in
   isolation;
3. a global, unbounded optimization theorem for the generalized
   arithmetic-block staircase containing Kohonen's construction.  Its ratio
   is at most `85/294`, with equality uniquely at Kohonen's parameters.

Thus the obvious periodic and staircase architectures are now closed.  A
record in the phased language would have to **interleave** the periodic `K/L`
digit gadget with the `I/J` staircase so that the same macro segments serve
both architectures; appending or serially concatenating them cannot work.

## 1. Enlarged minimal phased reflected predicate

For even `t`, put `B=t^2` and

```text
V  = [0,t],
H  = {it       : 0 <= i < t},
S  = {i(t+1)   : 0 <= i < t},
T0 = {j(t-1)   : 0 <= j <= t},
T1 = T0+1.
```

For macro-coordinate sets `I,J,K,L0,L1`, form

```text
A_t = (V+B I) union (H+B J) union (S+B K)
      union (T0+B L0) union (T1+B L1).
```

Writing, for example, `IL0=I+L0`, square `q` is certified by any of

```text
q in IJ or IK or IL0;
q-1,q in JK;
q-1,q in JL0;
q-1 in IL0 and q in IL1;
q-1,q in IL1;
q-1 in JL1 and q in JL0;
q-1,q in JL1;
q-1 in KL0 and q in KL1;
q-1 in KL1 and q in KL0.
```

The last four `V/H` phase clauses are material: they were absent in the first
alternate-tile pass.  Their elementary proofs are short.

- `V+T0=[0,t^2]`.  Consequently two consecutive copies of `V+T1`, or a
  previous `V+T0` and current `V+T1`, cover the next square.
- The usual two consecutive `H+T0` copies cover the next square.  The same is
  true for `H+T1`: shifting both shapes loses the left endpoint but gains the
  right, and the left endpoint is already in the previous shifted shape.
- For the mixed `H` clause,

  ```text
  (H+T1) union (H+T0+B) contains [B,2B-1].
  ```

  Write `x=at+b`.  If `b=0`, then `x-B in H+T0`.  If `b>0` and
  `a+b>=2t-1`, choose `j=t-b` to put `x-B` in `H+T0`; if
  `a+b<=2t-1`, choose `j=t-b+1` to put `x-1` in `H+T0`, hence `x` in
  `H+T1`.
- The two alternating `S/T` clauses are the parity lemma proved in the first
  campaign: if `D=S+T0`, both `D union (D+B+1)` and
  `(D+1) union (D+B)` contain `[B,2B-1]`.

`phased_lemma_verify.py` checks every elementary inclusion for all
`2<=t<=100`; every even `t` passes.  `test_phased_predicate.py` then generates
160 random macro placements and checks every abstractly certified square
against the literal integer sumset for `t=2,4,6,8`.

## 2. A perfect periodic phase gadget

The alternating clause has a clean digit architecture.  For arbitrary
positive integers `k,h`, take

```text
K  = 2[0,k-1],
L0 = 2k[0,h-1],
L1 = 1+2k[0,h-1].
```

Then

```text
K+L0 = {0,2,...,2kh-2},
K+L1 = {1,3,...,2kh-1}.
```

Hence alternating phases certify every square `1,...,2kh-1`.  Adding the
two anchors `I=J={0}` certifies square zero, giving an explicit scalable
certificate

```text
m = 2kh,       ell = k+2h+2.
```

The recorded instance `k=10,h=5` has `(ell,m)=(22,100)`.  Its abstract
prefix is exactly 100 and literal `A_t+A_t` checks pass for `t=2,4,6`.

This is a perfect use of all `K/L` cross-pairs, but it cannot itself approach
the record:

```text
(k+2h)^2 - 8kh = (k-2h)^2 >= 0,
```

so `2kh/(k+2h)^2 <= 1/4` even before paying for the anchors.  More generally,
grafting any disjoint gadget of density at most `1/4` onto a basis already at
`85/294>1/4` strictly lowers the ratio.  The phase gadget must reuse the old
`I/J` segments, not live in a separate tail.

## 3. Global obstruction for the arithmetic-block staircase

Here is the broad serial architecture suggested by Kohonen's proof.  Let

```text
r >= 1, u >= r+1, s >= r, z >= 0,
A = 2r+(r+1)s,
B0 = ru+2(r+1)s+3r-r^2,
D = ru+(r+1)s+2r+1.
```

Use

```text
I = {0,r} union (A+r[0,u-1]),
J = 2r+(r+1)[0,s-1],
K = [0,r-1] union Union_{n=0}^{z-1} (B0+nD+[0,r]),
L0=L1=empty.
```

Any high dense block may instead be assigned to `L0`; its `I/J` square
clauses are identical.  Thus the ansatz includes serial use of the reflected
fourth direction.  A monochromatic `L1` high block cannot serve as a local
serial block: its two-consecutive rules omit the first square of each local
sum interval.  Alternating `L0/L1` macro digits are instead covered by the
periodic architecture in §2.

The coprime-step identity

```text
r[0,u-1] + (r+1)[0,s-1]
contains [r(r-1), r(u-1)+(r+1)(s-1)-r(r-1)]
```

holds when `u>=r+1,s>=r`.  Together with the interval blocks, it proves that
the placement certifies

```text
ell = u+s+r+2+z(r+1),
m   = B0+zD.
```

This is an unbounded four-parameter family, not a finite search box.  Its
optimization is exact.  Define

```text
x = u-r-1,
a = r+1,
y = s+x-(3r+2),
w = z-2.
```

Direct expansion gives

```text
85 ell^2 - 294 m
= 294x(r+z+2)
  +49(a-6)^2 +85y^2+14ay
  +85a^2w^2 +(14a^2+294)w -124awy.                 (*)
```

The first term is nonnegative.  For `w != 0`, minimize the remaining
expression over real `y`.  Up to the positive factor `147/85`, the lower
bound is

```text
P = 23a^2w^2+14a^2w+28a^2-340a+170w+1020.
```

Since `z>=0`, either `w=-2`, `w=-1`, or `w>=1`.

- `w=-2`: `P=92a^2-340a+680>0`;
- `w=-1`: `P=37a^2-340a+850>0`;
- `w>=1`: `P` increases with `w`, and
  `P>=65a^2-340a+1190>0`.

Each displayed quadratic has positive leading coefficient and negative
discriminant.  If `w=0`, the remaining expression is

```text
49(a-6)^2+85y^2+14ay.
```

Minimization over real `y` is positive for every integral `a` except possibly
`a=6`.  At `a=6` it becomes `y(85y+84)`, nonnegative for integral `y`, with
equality only at `y=0`.  Equality in (*) also forces `x=0`.  Therefore

```text
m/ell^2 <= 85/294,
```

with equality uniquely at

```text
(r,u,s,z)=(5,6,17,2),   (ell,m)=(42,510).
```

This recovers Kohonen's construction.  Reassigning its final dense block from
`K` to `L0` gives a genuine four-direction certificate with the same ratio;
the literal expansion passes for `t=2,4,6`.  Adding one more reflected dense
block gives the natural near miss `(ell,m)=(48,653)`, whereas a record would
require `m>=667`; its literal checks also pass.

## What this closes—and what it does not

Closed rigorously:

- the complete local phased tile rules;
- pure periodic parity-digit `K/L` constructions;
- isolated or disjoint-tail use of such periodic gadgets;
- the full unbounded coprime-step/dense-block serial staircase, including
  arbitrary `r,u,s,z` and serial `L0` substitution.

Not closed:

- a genuinely interleaved multiscale construction in which the same phased
  `L` placements simultaneously participate in a parity `K/L` digit rectangle
  and in long `I/L` or `J/L` sum intervals;
- arbitrary unions of arithmetic progressions with several incommensurate
  scales;
- the complete five-list finite predicate.

The most concrete remaining constructive route is therefore narrow: solve a
mixed-radix compatibility problem in which `K+L0` and `K+L1` alternate by
parity while `I+L` or `J+L` lands in a different, adjacent macro interval.
Merely adding more serial dense blocks, more isolated parity gadgets, or a
disjoint tail is now ruled out.

## Reproduction

```bash
cd phase2/loop/erdos791/closure/tiles

python3 phased_lemma_verify.py --through 100
python3 -m unittest -v test_phased_predicate.py

python3 periodic_phase_gadget.py --k 10 --h 5
python3 phased_verify.py periodic_gadget_check.json --direct-t 2 4 6

python3 staircase_family.py --r 5 --u 6 --s 17 --z 2
python3 staircase_family.py --r 5 --u 6 --s 17 --z 2 --last-as-l0
python3 phased_verify.py phased_staircase_42_510.json --direct-t 2 4 6
python3 phased_verify.py phased_staircase_48_653.json --direct-t 2 4 6
```

No file in this lane claims a new #791 record.
