# A new quadratic/CM tower record from `D=11,235,917`

**Certified conclusion (2026-08-20).**  The bounded-inertia totally real
pro-2 tower over

\[
 E=\mathbf Q(\sqrt{11,235,917})
\]

combined with the CM/Eisenstein product-disk packing gives

\[
 \boxed{F_2(n)\ll n^{0.49368323}}.
\]

This strictly improves the previous certified exponent `0.49368416`.

Canonical verifier:

```bash
python3 phase2/loop/erdos1208/verify_cm_eisenstein_real_quadratic_11235917.py
```

The verifier requires PARI/GP.  PARI certifies the class, localized class,
S-unit, and ray computations; Python independently checks the resulting
Kummer elements, every useful prime, the Golod--Shafarevich budget, and both
all-depth packing endpoints at 100 and 150 decimal digits.

## 1. Field arithmetic

The field discriminant is

\[
 D=11,235,917=7\cdot11\cdot337\cdot433\equiv5\pmod8.
\]

PARI/GP `bnfcertify` gives

\[
 \operatorname{Cl}(E)\cong C_{14}\times C_2,
 \qquad
 \operatorname{Cl}^+(E)\cong C_{14}\times C_2\times C_2.
\]

For the `T=217` smallest-norm prime-ideal prefix, `bnfsunit` certifies that
the localized class group is trivial.  There are therefore exactly
`T+2=219` S-unit squareclass columns before imposing the full-sign and
modulo-four local conditions.

The corresponding ray quotient is `(C_2)^4`, and the exact ray matrix has
rank four.  Consequently the Kummer generator rank is

\[
 d=219-4=215=T-2.
\]

As a guard against a hidden genus-rank change, the same computation was made
at `T=205` and `T=211`: the localized class group is already trivial and the
ray rank is already four.  Enlarging the prefix cannot undo either fact.

## 2. Independent Kummer-kernel audit

PARI returns a 215-column basis of the exact kernel of the sign/modulo-four
map.  The verifier expands each factored S-unit into the integral basis
`1,omega`, where

\[
 \omega^2-\omega-\frac{D-1}{4}=0.
\]

Python then checks, using integer arithmetic, that all 215 elements are

- positive at both real embeddings; and
- squares in the odd unit group modulo four.

Thus the computed kernel really satisfies the local conditions used in the
tower presentation, independently of PARI's ray-column encoding.

## 3. Relations and useful primes

With `d=215`, choose

\[
 T=217,
 \qquad
 N=11,123.
\]

The total relation bound is

\[
 R=(d+1)+T+N=216+217+11,123=11,556,
\]

and hence

\[
 4R=46,224=215^2-1<215^2.
\]

This is the exact all-square Golod--Shafarevich budget.

Every one of the first `N=11,123` candidate Frobenius-square caps is useful.
For norms congruent to two modulo three, the verifier evaluates the
corresponding quadratic-character functional on the exact 215-element
Kummer basis.  There are zero rejections, and no functional requires more
than 11 basis trials before a nonsquare is found.

The endpoint ideal data are

```text
last selected ideal: (1063, 1063, split, root 963)
last useful ideal:   (121951, 121951, split, root 70091)
```

## 4. Root discriminant and product-disk endpoint

Order-four inertia at every selected prime gives the real-tower root
discriminant contribution used by the established bounded-inertia master
inequality.  The exact logarithmic value is

\[
 \log \operatorname{rd}
 =318.9527585916460414427765165054094796268574\ldots.
\]

For the CM/Eisenstein disk step the verifier uses the safe rational bound

\[
 \frac{2\sqrt3}{\pi}<\frac{71603}{64935}.
\]

The equal-endpoint optimization gives

\[
 \alpha_*
 =0.4936832199308881880151091959337012970826\ldots
\]

at

\[
 w_0
 =39928.0042927813500116653540785292798324\ldots.
\]

The advertised safe rounding `alpha=0.49368323` lies above this threshold.
At that exponent the two endpoint margins are

```text
0.001632817036815572250219059375...
0.003247075212037706995029833562...
```

The endpoint derivatives have opposite signs, so the equalized point is the
correct lower-envelope optimum.  The largest omitted local slope is

```text
0.009999973433845534938505168416...
```

while the two terminal active slopes are approximately `0.0306672` and
`0.0191268`.  Therefore no omitted deeper increment can enter either greedy
frontier.  The verifier repeats the calculation at 100 and 150 digits and
also brackets both fixed-anchor endpoint roots strictly below the advertised
exponent.

## 5. Nearby-count optimization

An independent optimistic scan of every integer `T` in `211..225` used the
exact rank formula `d=T-2` and provisionally accepted every useful prime.
The unique best count was `T=217`.  Selected values are:

| `T` | optimistic threshold |
|---:|---:|
| 213 | `0.493683507947298509720199496...` |
| 214 | `0.493683475180607476552263712...` |
| 215 | `0.493683324505964782915225928...` |
| 216 | `0.493683331983537268209869432...` |
| **217** | **`0.493683219930888188015109196...`** |
| 218 | `0.493683335266657028507534024...` |
| 219 | `0.493683327116127874285486962...` |
| 220 | `0.493683484245977546993322888...` |
| 221 | `0.493683526743406493039549467...` |

Since the exact `T=217` usefulness audit has zero rejections, its optimistic
and actual configurations coincide.

## 6. Scope

The theorem is conditional only on the previously proved bounded-inertia
pro-2 presentation and CM/Eisenstein product-disk master inequality used by
the earlier record certificates.  Within that framework, every field-specific
input is reconstructed and checked here.  No assertion is made that
`D=11,235,917` is globally optimal among larger real-quadratic fields.
