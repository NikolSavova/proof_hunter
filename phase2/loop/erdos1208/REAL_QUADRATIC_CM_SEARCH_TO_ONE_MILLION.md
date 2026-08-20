# Finite real-quadratic CM screen through discriminant one million

## 1. What was searched

The reproducible floating-point program

```text
phase2/loop/erdos1208/scan_cm_eisenstein_real_quadratic_bases.cpp
```

was extended to accept compile-time discriminant intervals, exponent targets,
ramified-ideal grids, finalist counts, and an optional optimistic genus-rank
bonus.  For every positive fundamental discriminant `D<=1,000,000` it builds
the actual sequence of odd prime-ideal norms in `Q(sqrt(D))`: one ideal at a
ramified rational prime, two at a split prime, and one norm-`p^2` ideal at an
inert prime.  Thus the discriminant and prime-ideal costs in this screen are
field-specific rather than density approximations.

The main run covered all 303,957 positive fundamental discriminants in ten
disjoint intervals.  At every field it tested

```text
|T| = 215, 219, 223, 227, 231, 235, 239, 243,
```

then rescanned every integer `205<=|T|<=250` for the 100 strongest fields in
each 100,000-discriminant interval.  It used the exact CM constant
`2 sqrt(3)/pi`, the ordinary model `d=|T|-2`, the conservative base relation
charge `d+1`, and the deliberately favorable assumption that every eligible
outside prime ideal is useful.  Its target was the previous continuous
threshold `0.4936977138`.

A representative interval is reproduced by

```text
clang++ -O3 -std=c++17 \
  -DSCREEN_D_MIN=800001 -DSCREEN_D_LIMIT=900000 \
  -DSCREEN_ALPHA=0.4936977138 \
  -DSCREEN_BROAD_T_MIN=215 -DSCREEN_BROAD_T_MAX=243 \
  -DSCREEN_BROAD_T_STEP=4 -DSCREEN_FINALISTS=100 \
  phase2/loop/erdos1208/scan_cm_eisenstein_real_quadratic_bases.cpp \
  -o /tmp/cm_screen && /tmp/cm_screen
```

## 2. Outcome

The screen found thirteen fields with positive floating margin at the old
target.  Their margins at `alpha=0.4936977138`, after the dense local
`|T|` rescan, were

\[
\begin{array}{c|r}
D&\text{screen margin}\\ \hline
821453&0.97665934\\
979277&0.5110506\\
994733&0.4158480\\
544268&0.2431759\\
213173&0.2423061\\
988093&0.1842656\\
745244&0.1597466\\
494277&0.1417842\\
863957&0.1186013\\
880293&0.1169394\\
683709&0.1103622\\
809565&0.0753329\\
992917&0.0265561
\end{array}                                             \tag{2.1}
\]

For comparison, `D=43133` had margin about `2.17e-5` at the same target.
The large separation of `D=821453` triggered exact certification rather than
further reliance on the floating screen.

The exact local reoptimization for `D=821453` chose `|T|=219`, not the broad
grid's neighboring coarse representative.  PARI/GP then proved class number
one and the exact S-unit/ray metadata

\[
 \#S\text{-unit generators}=221,
 \quad \operatorname{rank}(\text{sign/ray image})=4,
 \quad d=217.                                           \tag{2.2}
\]

The full mod-3 Frobenius scan found 11,335 useful ideals and zero rejections.
The independent high-precision verifier certifies

\[
 F_2(n)\ll n^{0.49369313}.                              \tag{2.3}
\]

The exact proof, including the two ramified rational-prime edge cases and
the norm-minus-one unit/sign audit, is in
`REAL_QUADRATIC_821453_CM_EISENSTEIN_RECORD.md` and
`verify_cm_eisenstein_real_quadratic_821453.py`.

## 3. Secondary genus-rank filter

The ordinary `d=|T|-2` model can miss fields whose 2-class group supplies
additional Kummer classes.  The scanner therefore has a deliberately
over-generous secondary mode

```text
-DSCREEN_GRANT_GENUS_BONUS=1
```

which adds `max(0,omega(D)-1)` to `d` while continuing to charge `d+1` base
relations.  This is only a candidate filter: genus theory describes
unramified quadratic classes, but a class can be lost after the precise
S-local and ray/sign conditions are imposed.  A positive result in this mode
must be followed by an exact class-group, S-unit, and ray-class computation;
it is not a theorem by itself.

The bounded secondary run used `|T|=219` as its broad filter, followed by the
same dense `205..250` rescan for the top 100 fields in each 200,000 interval.
It flagged 17,486 fields with nonnegative broad-grid margin at the new safe
target `alpha=0.49369313`.  The leading dense-rescan candidates were

\[
\begin{array}{c|c|c|c|r}
D&\omega(D)-1&|T|&d&\text{optimistic margin}\\ \hline
880440&5&216&219&7.60008\\
963480&5&220&223&7.28058\\
937365&5&220&223&7.20123\\
871080&5&218&221&7.18302\\
552552&5&218&221&6.84735
\end{array}                                             \tag{3.1}
\]

For example,

\[
880440=2^3\cdot3\cdot5\cdot11\cdot23\cdot29.           \tag{3.2}
\]

Thus this secondary screen does identify a concrete next arithmetic audit:
compute the exact 2-class/Kummer group and the precise S-unit ray kernel for
`Q(sqrt(880440))` and the nearby leaders.  No exponent from (3.1) is claimed
here.  In particular, the five granted genus dimensions need not all survive
the chosen S-local and sign/dyadic conditions, and useful-prime rejection has
not been checked for these fields.

## 4. Scope and limitations

This is a finite computational search audit, not an asymptotic dominance
theorem for real-quadratic bases and not a proof that `D=821453` is optimal
outside the tested configurations.  In particular:

1. only `D<=1,000,000` was screened;
2. the broad-to-dense finalist filter is a stated finite procedure, not an
   interval proof over every possible `|T|`;
3. the all-useful assumption makes the primary screen optimistic, but the
   ordinary generator formula can miss genuine class-group contributions;
4. floating-point screening is used only to nominate fields; (2.3) rests
   solely on the exact standalone verifier.

Within those explicit limits, the search does answer the bounded question:
the old `D=43133` record is not the best field in the stated million-field
screen, and `D=821453` yields a fully certified improvement.
