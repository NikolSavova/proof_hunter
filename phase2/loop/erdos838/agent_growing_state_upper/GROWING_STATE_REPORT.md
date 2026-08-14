# Erdős 838: growing-state upper-construction attack

**Date:** 2026-08-13
**Verdict:** no stretchable family with coefficient below `1/2` was found.
The search did produce substantially better finite stretchable trace records,
but they do not come with a stable recursion and are not an asymptotic upper
construction.  The rigorous asymptotic output is a new `1/2` barrier for
depth-varying vertical towers with arbitrary, unbounded, possibly
indecomposable macro types, provided the logarithmic scale mesh vanishes.

All logarithms below are base two.

## 1. Exact finite search

`growing_macro_search.py` evolves integral height vectors with `x_i=i`.  Each
candidate is therefore stretchable.  Slopes are sorted as exact `Fraction`s,
the reverse-product trace is evaluated with integer transvection products,
and every retained record is re-evaluated with graded polynomial products.
The cap, cup, and convex profiles are recovered independently from those
graded products; through size 11 they are additionally checked by a complete
subset census.

The strongest run used 20,000 coordinate mutations/restarts at each size.  It
gave the following records.

| `N` | exact `V` | `log V/(log N)^2` | largest cap | largest cup | nonzero convex profile |
|---:|---:|---:|---:|---:|---|
| 9 | 169 | 0.736521374610 | 4 | 5 | `9,36,84,36,4` |
| 10 | 248 | 0.720801779097 | 5 | 5 | `10,45,120,64,9` |
| 12 | 513 | 0.700501536376 | 5 | 6 | `12,66,220,173,37,5` |
| 14 | 963 | 0.683735178482 | 6 | 6 | `14,91,364,356,124,14` |
| 16 | 1772 | 0.674447680535 | 7 | 7 | `16,120,560,697,327,48,4` |
| 18 | 3012 | 0.664614884182 | 7 | 6 | `18,153,816,1270,634,117,4` |
| 20 | 5155 | 0.660191417015 | 7 | 6 | `20,190,1140,2508,1122,171,4` |

These improve the earlier Gate-A heuristic values at every displayed size;
for example, the previous `N=20` value was `20424`.  This is a useful search
result, but not evidence strong enough to claim a sub-`1/2` family:

* each size was optimized independently;
* no coordinate recursion or compatible deletion chain emerged;
* the normalized value is still `0.66019` at `N=20`;
* the Erdős--Szekeres threshold changes only at sparse sizes, so a finite run
  in this range cannot determine the quadratic coefficient.

The exact integral coordinates, complete root orders, profiles, and integer
counts are in `LARGE_MACRO_CERTIFICATE.json`.  Recheck them with

```bash
python3 phase2/loop/erdos838/agent_growing_state_upper/growing_macro_search.py \
  check phase2/loop/erdos838/agent_growing_state_upper/LARGE_MACRO_CERTIFICATE.json
```

The separate `GROWING_SEARCH_CERTIFICATE.json` applies the exact vertical
composition recurrence to a schedule of independently optimized macros of
sizes `4,5,...,12`.  Its normalized values bottom out at
`0.665021634586` at the 120-point third level and then increase.  Thus the
naive heterogeneous-size schedule does not turn the finite records into a
candidate family.

## 2. A barrier beyond finite state

The finite-state theorem does not cover a new macro order type of growing
size at every depth.  The following theorem does.  In particular, the macros
below may be macroscopically indecomposable as order types; only their scale
relative to the accumulated construction is restricted.

Let `S_d` be an arbitrary rational general-position point set with
`r_d>=2` points.  Put `Q_0` equal to a singleton and define

```text
Q_d = S_d[Q_(d-1)],
```

where every macro point receives the same sufficiently thin vertical copy of
`Q_(d-1)`.  Neither `S_d` nor `r_d` is required to repeat.  Write

```text
l_d = log r_d,             L_d = sum_(t<=d) l_t = log |Q_d|,
eta_d = max_(t<=d) l_t/L_d.
```

> **Theorem (vanishing-mesh growing-macro barrier).**  Every such tower
> satisfies the finite quantitative bound
>
> ```text
> log W(Q_d)
>   >= 1/2 [ (L_d-l_d)^2 - sum_(t<d) l_t^2 ]
>   >= 1/2 (1-3 eta_d+eta_d^2) L_d^2.             (1)
> ```
>
> Consequently, if `eta_d -> 0`, then
>
> ```text
> liminf log W(Q_d)/(log |Q_d|)^2 >= 1/2.         (2)
> ```

### Proof

Let `C_d,U_d,W_d` be the nonempty cap, cup, and convex-subset counts of
`Q_d`, and let `a_d,b_d` be the largest cap and cup sizes in `S_d`.  The exact
vertical substitution identities give, with `n=|Q_(d-1)|`,

```text
C_d = C_(d-1) sum_(B cap in S_d) n^(|B|-1),
U_d = U_(d-1) sum_(B cup in S_d) n^(|B|-1).       (3)
```

Choosing a largest cap and a largest cup in the two sums gives

```text
log(C_d U_d)
 >= log(C_(d-1)U_(d-1))+(a_d+b_d-2)L_(d-1).      (4)
```

The cup--cap theorem applied to `S_d` says

```text
r_d <= binom(a_d+b_d-2,a_d-1) <= 2^(a_d+b_d-2),
```

so `a_d+b_d-2>=l_d`.  Iterating (4) from the singleton yields

```text
log(C_j U_j)
 >= sum_(t<=j) l_t L_(t-1)
  = 1/2 [L_j^2-sum_(t<=j)l_t^2].                 (5)
```

Every two macro points form a convex support.  The exact convex recurrence
therefore contains a term `C_(d-1)U_(d-1)`, regardless of the order type of
`S_d`.  Thus `W_d>=C_(d-1)U_(d-1)`.  Equation (5) with `j=d-1` proves the
first inequality in (1).  Finally,

```text
L_(d-1) >= (1-eta_d)L_d,
sum_(t<d)l_t^2 <= eta_d L_d^2,
```

which proves the second inequality.  This proves (1)--(2).

For stretchability, at every finite depth all relevant determinant signs are
strict at scale zero.  A sufficiently small positive rational vertical scale
preserves the macro, micro, and mixed-triple signs.  Iterating this choice
gives exact rational coordinates for every finite `Q_d`.

## 3. What this rules out

This theorem is genuinely stronger than the finite-state barrier in one
direction:

* the number of effective macro states may grow without bound;
* branching `r_d` may grow without bound;
* every `S_d` may be a new indecomposable order type;
* the scale schedule may be aperiodic and chosen adversarially.

For example, it covers arbitrary indecomposable macros with `r_d` polynomial,
exponential, or otherwise growing in `d`, whenever
`log r_d=o(sum_(t<=d)log r_t)` uniformly in the maximum-mesh sense above.

The theorem also identifies the exact remaining escape hatch.  A
below-`1/2` tower using the standard vertical mixed-triple rule must have a
subsequence of **macroscopic template jumps**:

```text
limsup_d max_(t<=d) log r_t/log |Q_d| > 0.        (6)
```

The argument does not rule out (6), genuinely heterogeneous children inside
one level, or a different mixed-triple geometry that destroys the two-block
term.  Those are honest open construction routes.  The finite coordinate
records above do not currently supply any of them.

## 4. Crisp verdict

No asymptotic upper construction below `1/2` was obtained.  The finite
coordinate evolution is substantially better than the previous braid search
and should be retained, but it is only a collection of exact records.  The
rigorous new result is the vanishing-mesh barrier (1): unbounded state and
indecomposable macros alone are insufficient; any successful vertical
construction must make repeated macroscopic jumps or abandon the standard
two-block mixed-triple coupling.
