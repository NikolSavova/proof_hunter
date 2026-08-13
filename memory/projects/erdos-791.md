# Erdős #791

**Status:** Active/open after three full attacks (2026-08-13).  No numerical record improvement and no
proof that the normalized limit exists.

## Hot state

- Normalization: `R(k)` is the largest initial interval covered by a `k`-element additive 2-basis;
  the goal is `alpha_-=alpha_+` for its normalized liminf/limsup.
- Published window: `85/294 <= alpha_- <= alpha_+ <= 0.4585`.
- Latest theorem: for every fixed `r`, exact `t+O_r(1)` modular tiles give a `K_r` current-role
  compatibility language with carry self-loops.
- Decisive gap: temporal cross-state compatibility.  Static colors are no longer the obstacle.
- Full closure would follow from a `k+o(k)` transition-compatible role assignment on limsup-extremal
  bases, or from holes contained in `U+V` with `|U|+|V|=o(k)` via the rank-one absorber.

## Read first

1. `phase2/loop/erdos791/HANDOFF_20260813.md` — complete context, failed routes, exact traps, ideas,
   reproduction, and next work.
2. `phase2/loop/erdos791/full_attack3/FULL_ATTACK3_RESULT.md` — latest synthesis.
3. `phase2/loop/erdos791/full_attack3/AUDIT.md` — independent audit.

## Next action

Build a transition-aware optimizer that jointly chooses one representation per target, coordinate
roles, and ordered carry-state transitions; in parallel, optimize alternative integer lifts by the
additive-rectangle complexity of transition residuals.  Do not restart static clique search.
