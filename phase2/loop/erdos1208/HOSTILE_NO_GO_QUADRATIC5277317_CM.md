# Hostile no-go audit of the `D=5277317` quadratic-CM screen hit

## Verdict

The apparent `D=5277317` improvement is a genus-bonus false positive.  The
optimistic screen grants one extra safe generator and obtains a strongly
positive endpoint, but the exact norm-prefix localization kills the entire
ideal class group.  The true safe generator rank is therefore one smaller.

After this correction, every norm-prefix count

\[
205\leq T\leq250
\]

fails at the current record exponent

\[
\alpha=0.49368416,
\]

even after every possible useful-role prime ideal is declared useful.  The
best exact-rank count is

\[
T=221,\qquad d=219,\qquad N=11549,
\]

and its optimized endpoint margin, using a packing constant favorable to the
candidate, is

\[
-0.10475959990594471345\ldots.
\]

Thus no Kummer usefulness rejection is needed to kill the field.

## Why the fast screen was fooled

The fundamental discriminant factors as

\[
5277317=613\cdot8609.
\]

The optimistic genus envelope consequently grants one additional squareclass.
At `T=222` it uses

\[
d=221,qquad N=11766,
\]

and the relaxed endpoint has margin

\[
+1.7213023903495678391\ldots.                       \tag{2.1}
\]

This is a real numerical effect rather than floating-point noise.  It is,
however, arithmetically unrealizable for the norm-prefix set.

PARI/GP certifies

\[
\operatorname{Cl}(K)\simeq C_{12},
\qquad
\operatorname{Cl}^+(K)\simeq C_{12},
\]

and a four-dimensional sign/mod-4 ray quotient.  Already at `T=205`, the
localized `S`-class group is trivial, the pre-ray S-unit squareclass basis has
dimension `207=T+2`, and its ray image has full rank four.  Triviality of the
localized class group and full ray rank persist when more prime ideals are
added.  Hence throughout `205<=T<=250`,

\[
d=(T+2)-4=T-2.                                      \tag{2.2}
\]

In particular, at `T=222` the exact basis has 224 columns and ray rank four,
so the true value is `d=220`, not 221.  The verifier also directly repeats the
PARI calculation at `T=221`, `222`, and `250`.

## Favorable all-useful exclusion

For each count the verifier saturates the strict quadratic
Golod--Shafarevich ceiling:

\[
N_T=left\lfloor\frac{d^2-1}{4}\right\rfloor-(d+1)-T,
\qquad d=T-2.
\]

It then gives the candidate the first `N_T` unramified prime ideals without
performing any CM residue or Kummer usefulness test.  This is an optimistic
relaxation: the exact useful set can only be smaller or have larger norms.

The sweep uses the favorable rational lower bound

\[
\frac{11978}{10863}<\frac{2\sqrt3}{\pi}.
\]

Lowering this packing constant decreases the endpoint right-hand side and
increases the candidate's margin.  Failure with this constant therefore
implies failure with the true Eisenstein constant.

For every count, the two endpoint margins are equalized.  The scale-one
derivative is positive and the scale-two derivative is negative, so concavity
certifies the global maximum of their lower envelope.  The active local slopes
also exceed every omitted depth-nine slope, making the calculation all-depth.

The leading cells are:

| rank | `T` | `d` | `N_T` | favorable margin |
|---:|---:|---:|---:|---:|
| 1 | 221 | 219 | 11549 | `-0.1047596000` |
| 2 | 223 | 221 | 11765 | `-0.1094398361` |
| 3 | 219 | 217 | 11335 | `-0.1158096893` |
| 4 | 222 | 220 | 11656 | `-0.1192817271` |
| 5 | 220 | 218 | 11441 | `-0.1228344322` |

Every one of the 46 audited counts has favorable margin below `-0.10`.
The leading `T=221` cell is independently recomputed with 100-digit Decimal
arithmetic, giving the displayed `-0.104759599905...` margin.  The verifier
also recomputes the unrealizable genus-relaxed cell (2.1) at the same
precision, so the screen failure mechanism is explicit.

## Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_hostile_quadratic5277317_cm_no_go.py
```

Expected final line:

```text
D=5277317 genus-screen false positive: CERTIFIED
```

The verifier checks the certified BNF, exact localized class and ray ranks,
the favorable rational constant, the 46-count all-depth sweep, and both
high-precision endpoint cells.

## Scope

This kills the advertised **norm-prefix, all-square quadratic-CM screen hit**
for counts `205..250`.  It does not claim that every nonprefix assignment in
this field has the same localized class group, nor does it address different
inertia orders or presentations.  Because the exact norm-prefix candidate
already fails under the all-useful relaxation, constructing its detailed
Kummer kernel and usefulness list would not change the verdict and is
intentionally omitted.
