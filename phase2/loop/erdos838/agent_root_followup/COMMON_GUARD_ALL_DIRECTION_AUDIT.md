# A common-guard ramp does not reset in the first exact projection audit

**Date:** 2026-08-15.  Counts are nonempty and logarithms are base two.

## Verdict

The exact 14-point common-guard wrapper from
`agent_common_shield_mixing/COMMON_GUARD_PROFILE_RAMP_BARRIER.md` has

\[
                         V=1914.
\]

Its natural chart proves that the planar wrapper realizes the heterogeneous
first-cap/last-cup recurrence.  A possible recursive escape was to rotate
the completed wrapper before using it as a child: perhaps a new projection
would split the convex macro shell into complementary arcs and reduce the
cap--cup product to the 64 atomic guard transversals.

That reset fails strongly in this first exact case.  Exhausting all 174
generic projection chambers gives

\[
 \min_{\xi} C_\xi U_\xi=549\cdot286=157014,
 \qquad
 \max_{\xi} C_\xi U_\xi=289047,                         \tag{1}
\]

and

\[
                    \min_\xi\max(C_\xi,U_\xi)=412.     \tag{2}
\]

Thus every projection retains far more endpoint energy than the atomic
source bank.  The ratio in (1) is not inferred numerically: the verifier
uses exact rational coordinates, enumerates projection chambers by the
critical values of `x+t y`, and counts cap/cup chains by an independent
integer dynamic program.

The same conclusion survives the stronger finite mutation test from
`MINIMIZER_COMMON_GUARD_PROFILE_MUTATIONS.md`.  Its cup--interior--cap
profile word is the exact minimum over all `5^3` rooted four-point profile
words and has `V=1561`.  Across its 174 projection chambers (172 distinct
profiles),

\[
       \min_\xi C_\xi U_\xi=251\cdot539=135289,
       \qquad \min_\xi\max(C_\xi,U_\xi)=397.           \tag{3}
\]

This remains a finite obstruction, but it shows that even wrapper-local
minimality does not produce a cheap reset chamber.

This is a finite theorem, not an asymptotic all-direction bound.  Its value
is to identify the next sharp question.  The scalar quarter ramp only tracks
one rooted chart.  A recursively realizable sub-half construction needs the
same completed order type to offer a new chart whose endpoint product loses
a quadratic exponent.  The exact audit instead suggests the positive
target

> **direction-uniform endpoint-energy target:** a common-guard wrapper with
> a quadratic singleton source layer or quadratic local reservoir has
> `C_xi U_xi >= 2^{(1/2-o(1))(log n)^2}` in every generic projection
> chamber, unless an already-macroscopic child pays the coefficient-half
> bound.

Proving that target would close the only noncircular recursive use of the
formal quarter ramp.  Refuting it with an all-scale rational family would
give the first credible route to a sub-half upper construction.  The
strong-tree endpoint-reset theorem does close the special case in which
every rechart preserves a compatible ordered decomposition, but arbitrary
projection chambers need not do so: exact Pascal-cell audits retain only
two compatible chambers out of 26--198.  No strong-tree conclusion is
claimed here for the other chambers.

## Verification

Run

```bash
python3 phase2/loop/erdos838/agent_root_followup/verify_common_guard_all_direction.py
```

The expected output is

```text
PASS: interior-wrapper faces=1914, chambers=174, min CU=157014; mutation-minimizer faces=1561, chambers=174, min CU=135289
```
