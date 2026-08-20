# Hostile audit of the quadratic-6999893 CM construction

## 1. Verdict

The candidate survives exact arithmetic and yields a substantial new record.
The exact nearby-count optimization moves from the preliminary `T=221` to

\[
 E=\mathbb Q(\sqrt{6999893}),\qquad
 T=219,qquad d=217,qquad N=11335.                  \tag{1.1}
\]

The bounded-inertia Eisenstein-CM construction certifies

\[
 \boxed{F_2(n)\ll n^{0.49368416}}.                   \tag{1.2}
\]

The safe-constant continuous threshold is

```text
0.493684157373636255830104489798...
```

The independent verifier is

```text
python3 phase2/loop/erdos1208/verify_hostile_quadratic6999893_cm.py
```

It certifies the field with PARI/GP, constructs the `C_4`-aware nested S-unit
basis explicitly, independently rebuilds the safe local kernel, performs the
full CM scan, and recomputes every endpoint for `215<=T<=227`.  The winning
endpoint is repeated at both 100 and 150 decimal digits.

## 2. Exact field and class arithmetic

The fundamental discriminant factors as

\[
 6999893=31\cdot349\cdot647,
 \qquad6999893\equiv5\pmod8.                         \tag{2.1}
\]

With

\[
 \omega={1+\sqrt{6999893}\over2},\qquad
 \omega^2=\omega+1749973,                            \tag{2.2}
\]

PARI's certified BNF gives

\[
 \operatorname {Cl}(E)\simeq C_4,qquad
 \operatorname {Cl}^+(E)\simeq C_4\times C_2.       \tag{2.3}
\]

The second odd prime ideal in norm order is

\[
 R=(13,13,\text{split root }6),                      \tag{2.4}
\]

and has class coordinate one, hence generates `C_4`.  The ordinary S-class
group is already trivial at `T=215` and remains trivial through `T=227`.

The verifier constructs one nested squareclass basis as follows:

1. the two global unit squareclasses;
2. a generator of `R^4`, retaining the nontrivial `Cl(E)[2]` squareclass;
3. for every other selected ideal `P` of class coordinate `a`, a generator
   of `P R^e`, with `a+e=0 mod 4`.

The parity valuation vectors in item 3 are independent on the non-`R`
coordinates, while the `R^4` generator supplies the class-torsion kernel.
The exact Kummer sequence therefore gives `T+2` independent squareclasses
for every nested prefix.

At the winning count, the last ramified ideal is

\[
 (1063,1063,\text{split root }335).                  \tag{2.5}
\]

## 3. Independent safe-kernel reconstruction

For modulus `(4 O_E; both real places)`, PARI gives local quotient `(C_2)^4`
and image rank four.  Independently, the verifier computes

- both exact real-embedding signs; and
- every unit-square coset in `O_E/4 O_E` using the multiplication law in
  the integral basis `(1,omega)`.

The resulting four-row space agrees exactly with PARI's row space on the
entire nested basis.  It has rank four at every audited count.  At `T=219`,
the verifier explicitly constructs its nullspace and obtains

\[
 d=(219+2)-4=217.                                    \tag{3.1}
\]

Thus the corresponding elementary quadratic extension is totally real,
dyadically unramified, and ramified only at the selected odd ideals.

## 4. Exact CM usefulness and relation budget

For every candidate norm `Q=2 mod 3`, the exact quadratic-residue functional
is evaluated on all 221 S-unit basis elements.  The ideal is useful exactly
when the functional raises the local-row rank.  At the winner, this test is
also checked against every vector of the explicit safe-kernel basis.  Norms
`Q=1 mod 3` are automatically useful.

The winning exact scan gives

\[
 \boxed{11335\text{ useful ideals and }0\text{ rejections}}, \tag{4.1}
\]

ending at

\[
 (124951,124951,\text{split root }98332).             \tag{4.2}
\]

The safe base-relation charge is `d+1=218`.  With 219 inertia-square and
11,335 Frobenius-square relations,

\[
 r\le218+219+11335=11772,
 \qquad4r=47088=217^2-1<217^2.                       \tag{4.3}
\]

Hence the strict quadratic Golod--Shafarevich inequality proves an infinite
quotient.

## 5. Exact nearby-count optimization

Every count in the dense interval has full local rank and zero CM rejections.
The exact thresholds are

\[
\begin{array}{c|c|c|c}
T&d&N&\alpha_*\\ \hline
215&213&10913&0.4936842235862493\\
216&214&11017&0.4936842465664361\\
217&215&11123&0.4936841685661151\\
218&216&11228&0.4936842169393867\\
219&217&11335&\mathbf{0.4936841573736363}\\
220&218&11441&0.4936842209036942\\
221&219&11549&0.4936841760308516\\
222&220&11656&0.4936842520877087\\
223&221&11765&0.4936842382433456\\
224&222&11873&0.4936843463579133\\
225&223&11983&0.4936843519942202\\
226&224&12092&0.4936844749406231\\
227&225&12203&0.4936845112860512.
\end{array}                                           \tag{5.1}
\]

Thus `T=219` is the unique exact winner in the audited window.  In
particular, the original optimistic `T=221` lead was arithmetically sound but
not count-optimal.

## 6. Root discriminant and all-depth endpoint

For the winning prefix,

\[
 \log D_L={1\over2}\log6999893
 +{1\over4}\sum_{\mathfrak p\in T}\log N\mathfrak p
 =322.0443044312204946839811082606199\ldots .         \tag{6.1}
\]

The verifier uses the rigorous geometric bound

\[
 {2\sqrt3\over\pi}<{71603\over64935}                \tag{6.2}
\]

and the complete active local frontier

\[
 c(Q)={\log Q\over2},\qquad
 g_j(Q)={1\over4}\log A_j(Q^{-2}).                   \tag{6.3}
\]

The equal-endpoint anchor is

```text
40670.9061212898227878623498934...
```

At the advertised exponent `0.49368416`, the endpoint margins are

```text
0.0004338012999378680696513181263...
0.0008626918489714107605311065297...
```

at both 100- and 150-digit precision.  Their active slopes are

```text
0.03058947406605971961958067202...
0.01909605634518910835603577714...
```

while the maximum omitted slope is
`0.00999981994839345639249736015...`.  No deeper local role is active.  The
scale-one derivative is positive and the scale-two derivative is negative.
The two fixed-anchor endpoint roots are

```text
0.4936841573736362558301043684349...
0.4936841573736362558301018165366...
```

both strictly below the advertised exponent.

## 7. Scope

This certifies the displayed norm-prefix construction and the complete dense
count window `215<=T<=227`.  It does not claim optimality over nonprefix
assignments, mixed inertia orders, other fields, or different pro-2
presentations.  Every arithmetic, class-torsion, kernel, CM, relation-count,
root-discriminant, and endpoint gate needed for the new record survives.
