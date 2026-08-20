# The quadratic-6999893 CM/Eisenstein record

## 1. Certified result

Let

\[
 E=\mathbb Q(\sqrt{6999893}),\qquad
 \omega={1+\sqrt{6999893}\over2}.
\]

The bounded-inertia pro-2 tower over `E`, followed by the Eisenstein CM
compositum and one-complex-coordinate disk packing, proves

\[
 \boxed{F_2(n)\ll n^{0.49368416}}.                       \tag{1.1}
\]

This strictly improves the certified `Q(sqrt(4108373))` exponent
`0.49368647`.  The exact continuous two-endpoint diagnostic for the selected
arithmetic configuration is

\[
 \alpha_*=0.49368415737363625583010448980\ldots,
 \qquad
 w_*=40670.9061212898227879\ldots.                       \tag{1.2}
\]

The theorem uses the safely rounded exponent `0.49368416`.  Run

```text
python3 phase2/loop/erdos1208/verify_cm_eisenstein_real_quadratic_6999893.py
```

with PARI/GP available.  The verifier performs the exact BNF, class,
localized class, explicit S-unit, ray, prime-ideal, Frobenius, presentation,
and 100/150-digit all-depth endpoint calculations.

## 2. Exact cyclic-four Kummer data

The fundamental field discriminant is

\[
 6999893=31\cdot349\cdot647\equiv5\pmod8.                \tag{2.1}
\]

PARI's unconditional `bnfcertify` returns one.  The ordinary class group is
`C_4`, the narrow class group is `C_4 x C_2`, and the exact S-class group for
the selected prefix is trivial.

Let `T` be the first 219 odd prime ideals in increasing norm, with the exact
tie order reconstructed by the verifier.  The final ideal has

\[
 (N\mathfrak p,p,\omega\bmod\mathfrak p)
   =(1063,1063,335).                                     \tag{2.2}
\]

The nontrivial `C_4` class group is handled explicitly rather than absorbed
into a rank heuristic.  Choose the first selected ideal `R` whose class
generates `C_4`; it is the ideal of norm 13 with `omega -> 6`.  The verifier
uses a principal generator of `R^4`.  For each other selected ideal `P` of
class `c`, it chooses `0<=e<4` with

\[
 [P]+e[R]=0\quad\hbox{in }C_4                              \tag{2.3}
\]

and uses a principal generator of `P R^e`.  Together with the two global-unit
columns, these give 221 explicit S-unit squareclass generators.  Among the
218 nonreference ideals, the class-coordinate counts `0,1,2,3` are

\[
 (57,54,52,55).                                         \tag{2.4}
\]

PARI maps all 221 columns into the exact ray square quotient for

\[
 (4O_E;\text{both real places}),                         \tag{2.5}
\]

which is `(Z/2)^4`; the image has rank four.  Python independently
reconstructs the two real-sign bits and two square-modulo-4 bits from the
displayed algebraic integers and obtains the same row space.  Hence the
totally positive, square-modulo-4 Kummer kernel has exact dimension

\[
 d=221-4=217.                                           \tag{2.6}
\]

This calculation includes the norm-minus-one unit and dyadic constraints;
no class-number-one or full-signature shortcut is used.

## 3. Useful ideals and Golod--Shafarevich budget

For an ideal `q` outside `T`, write `Q=N_E(q)`.  If `Q=1 mod 3`, it is
automatically useful in the Eisenstein CM step.  If `Q=2 mod 3`, its exact
quadratic residue functional must be nonzero on the Kummer kernel.  The
verifier evaluates each functional on all 221 displayed squareclasses and
checks whether it increases the rank of the four ray/sign rows.

The complete required prefix has zero rejections:

\[
 \#\{\text{useful ideals}\}=11335,
 \qquad
 (N\mathfrak q,p,\omega\bmod\mathfrak q)_{\rm last}
   =(124951,124951,98332).                               \tag{3.1}
\]

The prime 3 is inert, so its norm-nine ideal is in `T` and characteristic 3
is excluded from the useful list.  The three ramified rational primes are
also all in `T`: their global ideal positions are 7, 95, and 161 for
`p=31,349,647`, respectively.  They are treated as ramified ideals rather
than ordinary split primes.

Use the conservative real-quadratic relation bound `r_0<=d+1=218`, add an
inertia-square relation at every ideal of `T`, and add a Frobenius-square
relation at every selected useful ideal.  Then

\[
 r\le218+219+11335=11772,
 \qquad 4r=47088=217^2-1<d^2.                           \tag{3.2}
\]

All added relators are squares and hence lie in the Frattini subgroup, so the
generator rank remains 217.  The degree-two Golod--Shafarevich inequality
therefore proves that the quotient is infinite.

## 4. Root discriminant and endpoint certificate

The inertia-square caps give ramification index at most two in every finite
layer.  Thus

\[
 D_L=\sqrt{6999893}\prod_{\mathfrak p\in T}
             N_E(\mathfrak p)^{1/4},                   \tag{4.1}
\]

and the exact prefix gives

\[
 \log D_L=
 322.0443044312204946839811082606199259\ldots.          \tag{4.2}
\]

For `K=L(zeta_3)`, the one-coordinate complex disk calculation has effective
constant

\[
 C_{\rm Eis}={2\sqrt3\over\pi}
       <{71603\over64935},                              \tag{4.3}
\]

where the rational upper bound follows from `sqrt(3)<1351/780` and
`pi>333/106`.

The verifier includes every local depth whose slope can enter either product
disk endpoint.  The largest omitted slope is

\[
 0.0099998199483934563924973601\ldots,                  \tag{4.4}
\]

strictly below both active endpoint slopes.  At the safe exponent in (1.1),
the 150-digit margins after the `10^-25` allowance are

\[
 0.0004338012999378680696513181\ldots,
 \qquad
 0.0008626918489714107605311065\ldots.                  \tag{4.5}
\]

At the optimized anchor, the two fixed-anchor threshold crossings are

\[
 0.4936841573736362558301043684\ldots,
 \quad
 0.4936841573736362558301018165\ldots,                  \tag{4.6}
\]

both strictly below `0.49368416`.  Concavity, layer selection, and the
standard placewise rounding complete (1.1).

## 5. Nearby ideal-count audit and scope

The optimistic all-useful high-precision thresholds near the winner are

\[
\begin{array}{c|c}
|T|&\text{threshold}\\ \hline
216&0.4936842465664361\\
217&0.4936841685661151\\
218&0.4936842169393867\\
219&0.4936841573736363\\
220&0.4936842209036942\\
221&0.4936841760308516\\
222&0.4936842520877087\\
223&0.4936842382433456
\end{array}                                             \tag{5.1}
\]

Thus 219 is the strict local winner in the audited range.  Its all-useful
assumption is then proved exactly by the zero-rejection calculation in
Section 3.

This is a certified upper-bound improvement inside the bounded-inertia
real-quadratic CM/Eisenstein construction.  It does not settle Erdos 1208 and
remains far above the conjectural cube-root exponent.  The ongoing bounded
base-field search is a separate finite audit and may supersede this checkpoint;
neither it nor this note claims asymptotic optimality over real-quadratic
bases, ideal assignments, or other tower constructions.
