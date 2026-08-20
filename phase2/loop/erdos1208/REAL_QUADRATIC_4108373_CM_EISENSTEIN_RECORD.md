# The quadratic-4108373 CM/Eisenstein record

## 1. Certified result

Let

\[
 E=\mathbb Q(\sqrt{4108373}),\qquad
 \omega={1+\sqrt{4108373}\over2}.
\]

The bounded-inertia pro-2 tower over `E`, followed by the Eisenstein CM
compositum and one-complex-coordinate disk packing, proves

\[
 \boxed{F_2(n)\ll n^{0.49368647}}.                       \tag{1.1}
\]

This improves the certified `Q(sqrt(3200972))` exponent `0.49368759` and the
earlier `Q(sqrt(2278757))` exponent `0.49368818`.  The exact continuous
two-endpoint diagnostic for the selected arithmetic configuration is

\[
 \alpha_*=0.49368645980967580885906286608\ldots,
 \qquad
 w_*=39963.8976671829913854\ldots.                       \tag{1.2}
\]

The theorem uses the safely rounded exponent `0.49368647`.  Run

```text
python3 phase2/loop/erdos1208/verify_cm_eisenstein_real_quadratic_4108373.py
```

with PARI/GP available.  The verifier performs the exact BNF, class,
localized class, S-unit, ray, prime-ideal, Frobenius, presentation, and
100/150-digit all-depth endpoint calculations.

## 2. Exact field and Kummer data

The fundamental field discriminant is

\[
 4108373=17\cdot67\cdot3607\equiv5\pmod8.                \tag{2.1}
\]

PARI's unconditional `bnfcertify` returns one.  The ordinary class group is
`C_2`, the narrow class group has order four and structure `C_2 x C_2`, and
the exact S-class group for the selected prefix is trivial.

Let `T` be the first 217 odd prime ideals in increasing norm, with the exact
tie order reconstructed by the verifier.  The final ideal has

\[
 (N\mathfrak p,p,\omega\bmod\mathfrak p)
   =(1117,1117,1020).                                    \tag{2.2}
\]

The verifier does not infer the Kummer rank from a class-number-one shortcut.
It selects the first nonprincipal ideal `R`, which is the ideal of norm 11
with residue `omega -> 4`.  It uses a generator of `R^2`; for every other
nonprincipal selected ideal `P`, it uses a generator of `PR`; and for every
principal `P`, it uses a generator of `P`.  Together with the two global-unit
columns, these give an explicit 219-column basis of the S-unit squareclasses.

PARI maps these columns into the exact ray square quotient for

\[
 (4O_E;\text{both real places}),                         \tag{2.3}
\]

which is `(Z/2)^4`; the image has rank four.  Python independently
reconstructs the two real-sign bits and the two square-modulo-4 bits from the
219 integral elements and obtains exactly the same four-dimensional row
space.  Therefore the totally positive, square-modulo-4 Kummer kernel has

\[
 d=219-4=215.                                           \tag{2.4}
\]

This explicitly handles the norm-minus-one unit and dyadic conditions; no
full-signature assumption is used.

## 3. Useful ideals and Golod--Shafarevich budget

For an ideal `q` outside `T`, write `Q=N_E(q)`.  If `Q=1 mod 3`, it is
automatically useful in the Eisenstein CM step.  If `Q=2 mod 3`, the exact
quadratic residue functional must be nonzero on the Kummer kernel.  The
verifier evaluates that functional on every one of the 219 displayed
squareclass generators and tests whether it increases the rank of the four
ray/sign rows.

The full required prefix has zero rejections:

\[
 \#\{\text{useful ideals}\}=11123,
 \qquad
 (N\mathfrak q,p,\omega\bmod\mathfrak q)_{\rm last}
   =(121367,121367,69978).                               \tag{3.1}
\]

The prime 3 is inert, so its norm-nine ideal is in `T` and characteristic 3
is excluded from the useful list.  The ramified ideals above 17 and 67 are
also in `T`.  The ramified ideal above 3607 is ideal 291 outside `T`; since
`3607=1 mod 3`, it is automatically useful.  Thus ramified rational primes
are not silently treated as ordinary split primes.

Use the conservative real-quadratic relation bound `r_0<=d+1=216`, add an
inertia-square relation at every ideal of `T`, and add a Frobenius-square
relation at every selected useful ideal.  Then

\[
 r\le216+217+11123=11556,
 \qquad 4r=46224=215^2-1<d^2.                           \tag{3.2}
\]

All added relators are squares and hence lie in the Frattini subgroup, so the
generator rank remains 215.  The degree-two Golod--Shafarevich inequality
therefore makes the quotient infinite.

## 4. Root discriminant and endpoint certificate

The inertia-square caps give ramification index at most two in every finite
layer.  Consequently

\[
 D_L=\sqrt{4108373}\prod_{\mathfrak p\in T}
             N_E(\mathfrak p)^{1/4},                   \tag{4.1}
\]

and the exact selected prefix gives

\[
 \log D_L=
 317.6510581919590472759259853116048183\ldots.          \tag{4.2}
\]

For `K=L(zeta_3)`, the one-coordinate complex disk calculation has effective
constant

\[
 C_{\rm Eis}={2\sqrt3\over\pi}
       <{71603\over64935}.                              \tag{4.3}
\]

The rational inequality is checked from `sqrt(3)<1351/780` and
`pi>333/106`.  The verifier builds every local depth whose slope can matter,
sorts the complete product-disk frontier, and proves that the largest omitted
slope is

\[
 0.0099998199483934563924973601\ldots                   \tag{4.4}
\]

and is below both active endpoint slopes.  At the safe exponent in (1.1),
the 150-digit endpoint margins after the `10^-25` numerical allowance are

\[
 0.0016539510883490886500713317\ldots,
 \qquad
 0.0032890914979972110365601016\ldots.                  \tag{4.5}
\]

At the optimized anchor, the two fixed-anchor threshold crossings are

\[
 0.4936864598096758088590630059\ldots,
 \quad
 0.4936864598096758088590604643\ldots,                  \tag{4.6}
\]

both strictly below `0.49368647`.  Concavity, layer selection, and the
standard placewise rounding complete (1.1).

## 5. Nearby ideal-count audit and scope

Under the optimistic all-useful model, exact high-precision endpoint
optimization over the nearby counts gives

\[
\begin{array}{c|c}
|T|&\text{threshold}\\ \hline
212&0.4936866610609482\\
213&0.4936865405847247\\
214&0.4936865745046005\\
215&0.4936864859482318\\
216&0.4936865354284673\\
217&0.4936864598096758\\
218&0.4936865503434538\\
219&0.4936865198690187\\
220&0.4936866489886103\\
221&0.4936866662073596\\
222&0.4936868157413765\\
223&0.4936868519916800
\end{array}                                             \tag{5.1}
\]

Thus 217 is the strict local winner in this audited range; unlike an
optimistic filter, its all-useful assumption is then proved exactly by the
zero-rejection computation in Section 3.

This is a certified upper-bound improvement inside the bounded-inertia
real-quadratic CM/Eisenstein construction.  It does not settle Erdos 1208 and
remains far above the conjectural cube-root exponent.  The broad-to-dense
finite search that found the field is recorded separately; it is not an
asymptotic optimality theorem for real-quadratic bases or for other arithmetic
tower constructions.
