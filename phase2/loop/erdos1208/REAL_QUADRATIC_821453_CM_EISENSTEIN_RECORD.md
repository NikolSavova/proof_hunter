# The quadratic-821453 CM/Eisenstein record

## 1. Certified result

Let

\[
 E=\mathbb Q(\sqrt{821453}),\qquad
 \omega={1+\sqrt{821453}\over2}.
\]

The bounded-inertia pro-2 tower over `E`, followed by the Eisenstein CM
compositum and one-complex-coordinate disk packing, proves

\[
 \boxed{F_2(n)\ll n^{0.49369313}}.                       \tag{1.1}
\]

This supersedes the `Q(sqrt(43133))` CM exponent `0.49369772`.  A continuous
two-endpoint optimization gives the diagnostic values

\[
 \alpha_*\approx0.4936931243,\qquad w_*\approx40752.90. \tag{1.2}
\]

The certificate instead uses the safely rounded pair

\[
 \alpha=0.49369313,\qquad w_0=40752.95.                 \tag{1.3}
\]

Run

```text
python3 phase2/loop/erdos1208/verify_cm_eisenstein_real_quadratic_821453.py
```

with PARI/GP available.  The verifier performs the exact BNF, S-unit, ray,
prime-ideal, Frobenius, presentation, and 90/150-digit endpoint calculations.

## 2. Exact Kummer and presentation data

The field discriminant is the squarefree integer

\[
 821453=467\cdot1759\equiv5\pmod8.                      \tag{2.1}
\]

PARI's unconditional `bnfcertify` returns one and the certified class number
is one.  Let `T` be the first 219 odd prime ideals, in increasing norm and in
the exact tie order reconstructed by the verifier.  The final ideal has

\[
 (N\mathfrak p,p,\omega\bmod\mathfrak p)
       =(1213,1213,395).                                \tag{2.2}
\]

There is a small but important unit issue here: the generator count is not
inferred from a shorthand such as a full-signature assumption.  PARI's exact
`bnfunits` calculation for this precise set `T` returns 221 generators for
the fundamental S-unit squareclasses (including the unit/torsion data used by
PARI).  Their images under `ideallog` in the exact ray square quotient for

\[
 (4O_E;\text{both real places})                         \tag{2.3}
\]

have rank four.  Thus the kernel consisting of totally positive classes that
are squares modulo 4 has the exact dimension

\[
 d=221-4=217.                                           \tag{2.4}
\]

The verifier does not trust only the ray-group rank: it reads all 221 exact
S-unit generators back as elements `a+b omega`, reconstructs the two sign
bits and the two square-modulo-4 bits independently, and again obtains rank
four.  This explicitly includes the norm-minus-one/fundamental-unit behavior;
no surjectivity of a unit-signature map is assumed.

Use the conservative real-quadratic Shafarevich relation bound
`r_0<=d+1=218`.  Add inertia-square relators at all 219 ideals of `T`, and
Frobenius-square relators at 11,335 useful ideals outside `T`.  Then

\[
 r\le218+219+11335=11772,
 \qquad 4r=47088=217^2-1<d^2.                           \tag{2.5}
\]

Every added relation is a square, hence lies in the Frattini subgroup and
does not lower the generator rank.  The degree-two Golod--Shafarevich test
therefore proves that the quotient is infinite.

## 3. Exact useful-prime test

For an ideal `q` outside `T`, put `Q=N_E(q)`.  If `Q=1 mod 3`, splitting in
the Eisenstein CM step is automatic.  If `Q=2 mod 3`, the exact quadratic
residue functional at `q` must be nonzero on the Kummer kernel; after the
Frobenius-square cap, the residue degree is then exactly two and
`Q^2=1 mod 3`.

The verifier evaluates this condition on the full 221-column S-unit model:
a functional is nonzero on the kernel of the four ray/sign rows precisely
when adjoining it increases their binary row rank.  In the complete selected
prefix there are zero rejections.  Its exact endpoint is

\[
 \#\{\text{useful ideals}\}=11335,
 \qquad
 (N\mathfrak q,p,\omega\bmod\mathfrak q)_{\mathrm{last}}
   =(122527,122527,3683).                                \tag{3.1}
\]

Both rational primes ramifying in `E/Q` are treated as ramified rather than
ordinary split primes.  The ideal above 467 is ideal number 115 and belongs
to `T`.  The ideal above 1759 is the sixtieth ideal outside `T`; because
`1759=1 mod 3`, it is automatically useful.  Characteristic 3 is excluded
from the useful list.

For a useful ideal and local depth `j`, the absolute-degree-normalized cost
and the uniform CM gain are

\[
 c_{\mathfrak q,j}={\log Q\over2},\qquad
 g_{\mathfrak q,j}={1\over4}\log A_j(Q^{-2}).           \tag{3.2}
\]

## 4. Root discriminant and disk constant

The inertia-square caps give ramification index at most two in every finite
layer.  Consequently

\[
 D_L=\sqrt{821453}\prod_{\mathfrak p\in T}
             N_E(\mathfrak p)^{1/4},                   \tag{4.1}
\]

and the exact selected prefix gives

\[
 \log D_L=
 322.2254902582720516650681010254956678\ldots.           \tag{4.2}
\]

The dyadic prime is not in `T`.  Since 3 is inert, its norm-nine ideal is in
`T`; it receives only the ordinary tame inertia cap in the real tower.  Its
CM ramification is handled by the relative-discriminant bound and is not
double-counted.

For `K=L(zeta_3)`, the one-coordinate complex disk calculation has effective
constant

\[
 C_{\rm Eis}={2\sqrt3\over\pi}.                         \tag{4.3}
\]

The certificate replaces it by the rigorous rational upper bound

\[
 C_{\rm Eis}<{71603\over64935},                         \tag{4.4}
\]

obtained from `sqrt(3)<1351/780` and `pi>333/106`.

## 5. Endpoint certificate

For `w=(log n)/(2m)` the two endpoint inequalities use

\[
 F(2\alpha w)\ge
 \log(C_{\rm Eis}D_L)+(2-4\alpha)w+
 \log\left(1+{e^{2(2\alpha-1)w}\over C_{\rm Eis}D_L}\right). \tag{5.1}
\]

At (1.3), after using (4.4) and subtracting the numerical allowance
`10^-25`, the 150-digit margins are

\[
 0.0011660559947093285867629597736\ldots,
 \qquad
 0.0011965374298356548401071428649\ldots.                \tag{5.2}
\]

The right endpoint's active slope is

\[
 0.01905568908395088350\ldots,                           \tag{5.3}
\]

whereas the largest omitted fourth-depth slope is

\[
 0.01571244930718410612\ldots.                           \tag{5.4}
\]

Local marginal monotonicity excludes every deeper item.  With the anchor
`w_0` fixed, the two threshold crossings are

\[
 0.4936931229546471768\ldots,
 \qquad
 0.4936931263645435376\ldots,                            \tag{5.5}
\]

both strictly below the advertised exponent.  Concavity, layer selection,
and the standard placewise rounding then prove (1.1).

## 6. Scope

This is a certified upper-bound improvement inside the bounded-inertia
real-quadratic CM/Eisenstein construction.  It does not settle Erdős 1208 and
remains far above the conjectural cube-root exponent.  The finite base search
that found the field, and the distinction between its theorem-level exact
certificate and the exploratory screen, are recorded separately in
`REAL_QUADRATIC_CM_SEARCH_TO_ONE_MILLION.md`.
