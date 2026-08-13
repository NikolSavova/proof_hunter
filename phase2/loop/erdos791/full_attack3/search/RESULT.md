# Erdős #791 full attack 3: exact point-footprint search

## Verdict

This lane did not resolve Erdős #791. It did produce the requested finite
seven-chromatic tile language, with a portable proof, and an exact carry-state
baseline showing where affine-line and triangle mechanisms do or do not make
nonlocal cycles.

The strongest positive finite statement is:

> Inside a `3^2` block there are fourteen four-point microtypes whose
> direct-complete compatibility graph has chromatic number exactly seven.

Here two microtypes are adjacent when their ordinary integer sum contains
every point of `[0,8]`. The graph has 59 edges and clique number six. Thus the
seven-chromatic behavior is not merely a displayed `K7`. It is also
vertex-critical: deleting any one of its fourteen vertices leaves an explicit
six-coloring, all stored and checked in the certificate.

This clears the chromatic target from the full-attack-2 obstruction at one
finite scale. It does **not** clear the asymptotic target: four points at
`t=3` have footprint cost ratio `4/3`, while closure needs a family with
microtype size `t+o(t)` as `t` tends to infinity.

## Exact chromatic certificate

`CHROMATIC_CORE.json` contains the fourteen types, all 59 independently
recomputed edges, all nonedges with a missing-point witness, and a checked
seven-coloring.

The lower bound is the standard six-coloring CNF:

```text
84 variables, 578 clauses
CNF SHA-256 39a4712886801de0bbd8cdaa4b7d423ac4746407f40cb45083cb2b194d25c7aa
```

CaDiCaL 3.0.1 returned UNSAT (`exit 20`). A fresh `drat-trim` run returned
`s VERIFIED` (`exit 0`), using 5,987 core lemmas and 153,824 resolution steps.
The compressed proof is `chromatic_core_6color.drat.gz`; exact hashes and
commands are in `CHROMATIC_DRAT_AUDIT.json`.

## Cheap exhaustive baseline

`exhaustive_baseline.py` exhausts every zero-containing microtype of size `t`
or `t+1` for `t=3,4` and builds the direct-complete compatibility graph.

| `t` | vertices | edges | exact clique number | checked coloring upper bound |
|---:|---:|---:|---:|---:|
| 3 | 84 | 362 | 6 | 7; the induced core and DRAT prove this is exact |
| 4 | 1,820 | 6,357 | 3 | 6 |

Allowing `t+2` points at `t=4` yields an explicit direct-complete `K7`; all
21 pair edges are independently decoded. The bounded CP-SAT continuation
also found fixed-initial-interval `K7` witnesses at `(t,size)=(5,8)` and
`(6,10)`. It returned `UNKNOWN`, not UNSAT, for `(5,7)`, `(6,9)`, and `(7,11)`
in ten seconds per case. These finite witnesses suggest overhead growing like
`t-2` in the discovered series, which is far too expensive; no such law is
claimed.

A more targeted lift keeps the exact 59-edge topology of the seven-chromatic
core and gives every one of its fourteen types `t+1` points. With type zero
normalized to the initial interval `[0,t]`, CP-SAT proves the model infeasible
at `t=4,5,6`; it returns `UNKNOWN` at `t=7` after 30 seconds. These are exact
solver conclusions inside the stated normalization, but there is no portable
UNSAT proof and the normalization is not known to be without loss of
generality. `CORE_LIFT_RESULTS.json` records the bounds.

## Exact carry automata

For microtypes in `[0,B)`, `footprint_core.py` records the low footprint in
the current `B=t^2` block and the carry-one footprint in the following block.
A transition `e -> f` is legal exactly when

```text
carry(e) union low(f) = [0,B-1].
```

`affine_line_automaton.py` enumerates every affine grid line
`j=a*i+c (mod t)` together with all horizontal translates. Among partial
single-pair events it finds no nontrivial strongly connected component at
`t=3,5,7,11` (up to 8,645 events and 125,221 transitions). This is an exact
finite negative result only.

There is also a useful symbolic explanation for the exact-size states. If two
`t`-point types have all `t^2` residues represented modulo `B=t^2`, their low
and carry masks partition the block. Hence, between two such events,

```text
e -> f  iff  low(e) is a subset of low(f).
```

A periodic cycle of such exact events therefore has one fixed low footprint;
nonconstant cycles require redundant representations or unions of events.

`subset_cycle_audit.py` consequently enumerates unions of up to three pair
events on the origin affine-line roles. At `t=3,5,7` it finds no alternating
two-cycle involving a nonstationary state. In contrast, it exactly recovers
the known `H-S-T` alternating triangle cycle for every even `4<=t<=20`:

```text
A = {H+S, H+T},     B = {S+T},
A -> B and B -> A,  while B -> B fails.
```

This identifies the triangle as a genuinely different carry mechanism, but
the search found no higher-role affine analogue in the stated finite scope.

The stationary affine cycle is also expanded into literal integer sets and
checked for six blocks at `t=3,5,7,11`. Those checks validate the automaton;
the construction has linear macro role cost and is not competitive for #791.

## Falsifiable conjectures mined from the exact cores

The computations suggest two deliberately narrow next targets, neither of
which is claimed as a theorem.

1. For `t>=4`, the direct-complete graph on all zero-containing `(t+1)`-point
   subsets of `[0,t^2)` is six-colorable. The only fully enumerated supporting
   case is `t=4`, where even the larger mixed `t`/`t+1` graph has a checked
   six-coloring; the normalized topology failures at `t=5,6` are much weaker
   evidence. A counterexample at `t=5` would be more valuable than another
   large-t heuristic.
2. In the origin-affine-line language, every two-cycle made from unions of at
   most three pair events contains only already-stationary states. This is
   exact at `t=3,5,7`; longer subset-state cycles were not enumerated. The
   unwrapped `H-S-T` family shows that the affine restriction is essential.

The first conjecture would rule out the simplest direct-only, overhead-one
route to `r>=7`; it would not rule out other `t+O(1)` overheads or nonlocal
carry languages.

## Reproduction

From this directory:

```bash
python3 exhaustive_baseline.py --output BASELINE_RESULTS.json
python3 affine_line_automaton.py --output AFFINE_LINE_AUTOMATON_RESULTS.json
python3 subset_cycle_audit.py --output SUBSET_CYCLE_RESULTS.json
python3 chromatic_core.py --output CHROMATIC_CORE.json --cnf /tmp/core.cnf
python k7_interval_cpsat.py --seconds 10 --output K7_CPSAT_RESULTS.json
python core_lift_cpsat.py --seconds 30 --output CORE_LIFT_RESULTS.json
```

The CP-SAT scripts require OR-Tools. All positive decoded footprints and
literal sumsets are rechecked without consulting solver variables.
