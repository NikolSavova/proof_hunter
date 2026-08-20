# The `D=5,277,317` quadratic/CM candidate is an exact prefix no-go

**Status (2026-08-20).**  Exact arithmetic certificate and all-depth endpoint
audit.  This candidate does **not** improve the current certified exponent
`0.49368416`.  The conclusion concerns the bounded-inertia, all-square,
smallest-prefix real-quadratic plus CM/Eisenstein product-disk construction;
it is not an impossibility theorem for every construction over this field.

Verifier:

```bash
python3 phase2/loop/erdos1208/verify_cm_eisenstein_real_quadratic_5277317_no_go.py
```

The optional `--dense` flag recomputes the complete optimistic prefix window
`205 <= T <= 250` and takes several minutes.

## 1. Exact field and localized class arithmetic

Let

\[
 E=\mathbf Q(\sqrt{5,277,317}),\qquad
 5,277,317=613\cdot 8609\equiv5\pmod 8.
\]

PARI/GP `bnfcertify` returns

\[
 \operatorname{Cl}(E)\cong C_{12},\qquad
 \operatorname{Cl}^+(E)\cong C_{12}.
\]

For the smallest-norm prefix with `T=221`, the second selected prime ideal has
norm `11`, residue root `1`, and generates `C_12`.  Localizing at the prefix
therefore kills the entire class group.  PARI's independent `bnfsunit` output
confirms that the localized class group is trivial.  This point disposes of
the possible genus/Kummer bonus suggested by the two prime factors of the
field discriminant: the bonus does not survive the selected set.

The same observation applies to every prefix in the audited window, because
all of them contain that norm-11 class generator.

## 2. Direct squareclass and ray computation

Write `R` for the norm-11 class generator.  A direct basis of
`E(S,2)` is built from

- the two global-unit columns;
- a principal generator of `R^12`;
- for every other selected prime `P`, a principal generator of `P R^e`,
  where `e` is chosen so that `[P]+e[R]=0` in `C_12`.

This gives exactly `T+2=223` columns.  The full-sign and modulo-four ray map
has target `(C_2)^4` and exact rank four.  PARI's columns and a separate
integer reconstruction of the two real signs and modulo-four squareclasses
give the same row space.  Hence

\[
 d=223-4=219=T-2.
\]

The ray image already has rank four at `T=205`, so every larger prefix in the
window also has rank four.  Thus no unaccounted rank gain occurs anywhere in
the dense prefix audit.

## 3. Useful-prime and Golod--Shafarevich audit

For `T=221`, the all-square relation budget is saturated at

\[
 R=\frac{219^2-1}{4}=11,990.
\]

The base and inertia relations consume

\[
 (d+1)+T=220+221=441,
\]

leaving

\[
 N=11,549
\]

Frobenius-square caps.  Every one of the first `11,549` candidate prime ideals
passes the exact mod-three usefulness test; there are zero rejections.  The
endpoint data are

```text
last selected ideal: (1031, 1031, split, root 848)
last useful ideal:   (126547, 126547, split, root 111660)
log root discriminant: 324.3992157962781898377959022289669...
```

Thus the optimistic all-useful model is not concealing a usefulness loss at
the best prefix.

## 4. Exact endpoint verdict

Using the safe rational CM/Eisenstein disk constant

\[
 C_{\rm CM}=\frac{71603}{64935}>\frac{2\sqrt3}{\pi},
\]

the equal-endpoint optimization gives

\[
 \alpha_*(T=221)
 =0.493684649778186556120660238919\ldots,
\]

at anchor

\[
 w_0=41403.6054883594863537970187\ldots.
\]

This is strictly worse than the current certified exponent

\[
 0.49368416.
\]

At `alpha=0.49368416`, the two endpoint margins are respectively

```text
-0.08235260082573373535169679...
-0.16377715522445818270547847...
```

so the failure is not a rounding issue.  The frontier calculation retains
all local increments that can enter either endpoint: the largest omitted
slope is smaller than the terminal active slope.  The verifier repeats the
calculation at 100 and 150 decimal digits.

## 5. Dense neighboring-prefix audit

Every integer `T` in `205..250` was recomputed under the optimistic assumptions

\[
 d=T-2,
 \qquad
 N=\left\lfloor\frac{d^2-1}{4}\right\rfloor-(d+1)-T,
\]

and that every eligible useful ideal is accepted.  The best value is attained
at `T=221`.  The closest neighboring values are

| `T` | optimistic threshold |
|---:|---:|
| 219 | `0.493684710138780986678590676...` |
| 220 | `0.493684738915022555820787707...` |
| **221** | **`0.493684649778186556120660239...`** |
| 222 | `0.493684713172021196888195003...` |
| 223 | `0.493684663437526264336732021...` |
| 224 | `0.493684772464446454580415801...` |

All 46 thresholds exceed `0.49368416`.  Rejections, if present away from the
exactly audited best prefix, can only replace a useful ideal by a later,
larger-norm ideal and therefore cannot rescue the optimistic loss.

## 6. Conclusion and scope

`D=5,277,317` is a genuine near miss, but not a new theorem record.  Its
ordinary and possible genus-enhanced cases collapse to the same exact rank
`d=T-2` because the smallest prefix kills `C_12`.  The best nearby prefix then
misses the current exponent by

\[
 4.89778186556120660238919\times10^{-7}.
\]

The field should therefore be removed from the exact-certification queue for
this construction.  The finite audit makes no assertion about non-prefix
ramification assignments, different inertia presentations, or a different
packing mechanism.
