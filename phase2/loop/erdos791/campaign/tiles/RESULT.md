# Erdős #791 alternate-tile lane: reflected diagonal

## Verdict

This lane found a genuine fourth elementary segment and proved an exact finite
certificate lemma for it.  It did **not** find a placement beating Kohonen's
`85/294` record in the search budget used here.  The result is therefore new
construction machinery and a sharply specified next search, not a resolution
of #791.

The useful new segment is the reflected diagonal

```text
T = {0,t-1,2(t-1),...,t(t-1)}.
```

Unlike an unphased copy of `T`, two bounded translation phases `T` and `T+1`
make its difficult sum with Kohonen's slanted segment tile a complete
`t^2`-block.  This gives a rigorous five-list placement language representing
four geometric directions.  Its general counting ceiling is `3/8`, strictly
above the `1/3` ceiling for Kohonen's three directions.

## Exact fourth-tile lemma

Let `t` be even, `B=t^2`, and

```text
V = [0,t],
H = {it       : 0 <= i < t},
S = {i(t+1)   : 0 <= i < t},
T = {j(t-1)   : 0 <= j <= t},
Q = [0,B-1].
```

Then:

1. `V+T` contains `Q`.
2. `(H+T) union (H+T+B)` contains `Q+B`.
3. Writing `D=S+T`, both

   ```text
   D union (D+B+1)
   (D+1) union (D+B)
   ```

   contain `Q+B`.

The first claim follows because the intervals
`j(t-1)+[0,t]` overlap and run from zero past `B-1`.  For the second,
`H+T` contains a representative of every residue modulo `B`: `j` determines
the residue modulo `t`, and `i` runs through all quotient digits.

Here is a direct proof of the first orientation of claim 3.  Every
`x in Q+B` is written uniquely as

```text
x = at+b,   t <= a <= 2t-1,   0 <= b <= t-1.
```

An element of `D` has the form

```text
i(t+1)+j(t-1) = (i+j)t+(i-j),
0 <= i <= t-1, 0 <= j <= t.
```

Because `t` is even, split according to the parity of `a+b`.

- If `a+b` is even and `a+b <= 2t-2`, take
  `i=(a+b)/2`, `j=(a-b)/2`, proving `x in D`.  If instead
  `a+b >= 2t`, take `i=(a+b-2t)/2`, `j=(a-b+2)/2`, proving
  `x-B-1 in D`.
- If `a+b` is odd and `a-b <= t-1`, take
  `i=(a+b+1-t)/2`, `j=(a-b+1+t)/2`, proving `x in D`.  If instead
  `a-b >= t+1`, take `i=(a+b-t-1)/2`, `j=(a-b-t+1)/2`, proving
  `x-B-1 in D`.

The displayed ranges make all four pairs integral and place them in the
required bounds.  The cases are exhaustive because the relevant quantities
have the indicated parity.  For completeness, the reverse orientation has an
equally short split.  If `a+b` is even, then for `a-b <= t-2` the pair

```text
i=(a+b-t)/2, j=(a-b+t+2)/2
```

represents `x-1`, while for `a-b >= t` the pair

```text
i=(a+b-t)/2, j=(a-b-t)/2
```

represents `x-B`.  If `a+b` is odd, then for `a+b <= 2t-1` the pair

```text
i=(a+b-1)/2, j=(a-b+1)/2
```

represents `x-1`, while for `a+b >= 2t+1` the pair

```text
i=(a+b-2t+1)/2, j=(a-b+1)/2
```

represents `x-B`.  Again parity makes the cases exhaustive and the displayed
bounds put `i,j` in their allowed intervals.  Both orientations are also
checked literally by `verify_reflected_lemma.py`.

## Scalable placement theorem

For finite sets of nonnegative macro coordinates `I,J,K,L0,L1`, define

```text
A_t = (V+B I) union (H+B J) union (S+B K)
      union (T+B L0) union ((T+1)+B L1).
```

Put `ell=|I|+|J|+|K|+|L0|+|L1|`.  Square `q` is certified if at least one of

```text
q in I+J, I+K, or I+L0;
{q-1,q} subset J+K;
{q-1,q} subset J+L0;
q-1 in K+L0 and q in K+L1;
q-1 in K+L1 and q in K+L0.
```

Indeed, the first line uses full-square `V` pairings, the next two use two
consecutive parallelograms, and the last two are exactly the phase-matched
reflected-diagonal lemma.  Therefore, if every `q=0,...,m-1` is certified,

```text
[0,m t^2-1] subset A_t+A_t,
|A_t| <= ell(t+1),
liminf n(k)/k^2 >= m/ell^2.
```

The bounded `+1` phase has no asymptotic size cost.  Ignoring `O(t)` same-type
sums, four geometric types have six useful cross-pairs, so the usual counting
argument gives the ceiling

```text
sum_{r<s} ell_r ell_s <= 3 ell^2/8.
```

This does not say the conservative predicate reaches `3/8`; it only shows the
fourth direction removes Kohonen's structural `1/3` ceiling.

## A rigorous no-go for the naive version

Let `t=2h`, and let `D=S+T` but allow only macro translations by `B`, with no
`+1` phase.  Then

```text
|(Q+B) minus (D union (D+B))| = floor((t-1)^2/4).
```

Indeed, for `x=at+b` as above, the missing even-parity points are exactly

```text
a+b >= 2t and a-b <= t-2,
```

and the missing odd-parity points are exactly

```text
a-b >= t+1 and a+b <= 2t-3.
```

Each is a parity triangle containing `h(h-1)/2` lattice points.  Their total
is `h(h-1)=t(t-2)/4=floor((t-1)^2/4)`.  In particular the uncovered fraction
tends to `1/4`.  So simply adjoining the reflected diagonal to Kohonen's original
integer-macro placement language cannot make `S+T` a square tile: the bounded
phase correction is essential, not cosmetic.

There is also a finite exact audit of the natural local repair

```text
T_e = {j(t-1)+e_j},  e_j in {0,1}, e_0=0.
```

For every `2 <= t <= 18`, exhaustive enumeration shows that no perturbation
which retains all `t` residue classes modulo `t` (the basic `H+T`
transversality condition) improves the cyclic `S+T` footprint over the
unperturbed reflected diagonal.  This is only a bounded theorem, but it rules
out the most obvious attempt to hide the phase inside one jagged segment.

## Search performed

`four_tile_cp_sat.py` encodes the sufficient predicate above exactly.  It
first recovered Mrose's known `(ell,m)=(7,14)` certificate as an independent
model check.  An exhaustive sweep over **every type split** proves within this
finite model that no record exists at `ell=7,m=15` (210 splits) or
`ell=8,m=19` (330 splits).  Coordinates above `m-1` cannot witness a square
below `m`, so the coordinate box loses no solutions.  All 540 solver calls
returned `INFEASIBLE`, not `UNKNOWN`; the detailed ledgers are
`all_splits_ell7_m15.json` and `all_splits_ell8_m19.json`.  As elsewhere,
OR-Tools supplies no portable UNSAT proof, so these are exact rerunnable solver
conclusions rather than formally checkable proof certificates.

At the first record-breaking targets for three larger balanced-ish
splits it returned `UNKNOWN` after 180 seconds each:

| counts `(I,J,K,L0,L1)` | `ell` | target `m` | threshold | status |
|---|---:|---:|---:|---|
| `(5,5,4,2,2)` | 18 | 94 | 94 | UNKNOWN |
| `(6,6,4,2,2)` | 20 | 116 | 116 | UNKNOWN |
| `(7,7,6,2,2)` | 24 | 167 | 167 | UNKNOWN |

These are not nonexistence results.  The deterministic annealer also failed
to hit the thresholds; best prefixes in four million proposals per split were
`70`, `82`, and `117`.  Those low values mainly show that generic local moves
do not discover the required block architecture.  They are not evidence that
the family is intrinsically weak.  The exact outputs are `cp2_*.json` and
`anneal2_*.json`.

Three local searches at `ell=42`, obtained by replacing a few Kohonen segments
with phased reflected diagonals, likewise stayed well below `511`.  Their best
prefixes were `367`, `325`, and `320` for splits `(8,17,15,1,1)`,
`(8,16,16,1,1)`, and `(8,15,15,2,2)`.  These are lower priority than a
structured search because even deleting one of Kohonen's carefully placed
segments destroys a long interval.

## Prioritized continuation

1. **Search arithmetic blocks, not coordinates.**  Parameterize each list as
   a union of short intervals/progressions, including an alternating phase
   chain in `K+L`.  Kohonen's certificate is entirely built from such blocks;
   coordinate annealing destroys them.
2. **Exploit phase alternation explicitly.**  Force `K+L0` and `K+L1` to form
   alternating consecutive sum intervals.  Then `r` reflected pair-sums yield
   about `r-1` whole squares rather than isolated partial diamonds.
3. **Run a portfolio CP-SAT with hints and symmetry breaking** over all type
   splits for `ell=18..30`, targeting `floor(85 ell^2/294)+1`.  The present
   model has no architecture hints and all threshold runs timed out.
4. **Only then generalize slopes.**  For `T_c={j(t-c)}`, the pairs `H+T_c` and
   `S+T_c` have lattice indices `c` and `c+1`; bounded phases modulo these
   indices may tile, but the search language has `c(c+1)` phase labels.  The
   reflected case `c=1` is the smallest and cleanest member and should be
   exhausted first.

## Reproduction

```bash
python3 verify_reflected_lemma.py --through 100
python3 audit_reflected_family.py --through 18
python3 four_tile_search.py --counts 5,5,4,2,2 --limit 94 --bound 93

# Optional exact solver dependency:
python3 -m venv /tmp/tiles-venv
/tmp/tiles-venv/bin/pip install ortools
/tmp/tiles-venv/bin/python four_tile_cp_sat.py \
  --counts 5,5,4,2,2 --target 94 --seconds 300
```

All statements about record-breaking feasibility remain negative or
`UNKNOWN`; nothing here should be presented as an improvement to `85/294`.
