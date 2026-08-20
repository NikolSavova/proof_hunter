# Hostile audit of the quadratic-3200972 CM construction

## 1. Verdict

The candidate survives an independent exact reconstruction and improves the
certified upper exponent again.  Take

\[
 E=\mathbb Q(\sqrt{800243}),\qquad
 \operatorname {Disc}(E)=3200972,qquad
 T=215,quad d=213,quad N=10913.                    \tag{1.1}
\]

The bounded-inertia Eisenstein-CM construction gives

\[
 \boxed{F_2(n)\ll n^{0.49368759}}.                   \tag{1.2}
\]

Using the safe rational geometric constant, the optimized continuous
threshold is

```text
0.493687585311887412008556617096...
```

The companion verifier is

```text
python3 phase2/loop/erdos1208/verify_hostile_quadratic3200972_cm.py
```

It requires PARI/GP.  PARI certifies the field and produces exact principal
generators.  Python independently reconstructs the even-basis sign/dyadic
kernel, scans every CM functional, checks the Golod--Shafarevich budget, and
recomputes the endpoint at 100 and 150 digits.  It also audits every nearby
integer count `211<=T<=221` rather than trusting the floating count
optimization.

## 2. Field and nested S-unit basis

The radicand `800243` is prime and is `3 mod 4`, so

\[
 \mathcal O_E=\mathbb Z[\theta],\qquad
 \theta=\sqrt{800243},qquad \operatorname {Disc}(E)=4\cdot800243.
                                                               \tag{2.1}
\]

PARI's certified BNF gives

\[
 \operatorname {Cl}(E)\simeq C_{15},qquad
 \operatorname {Cl}^+(E)\simeq C_{30}.              \tag{2.2}
\]

The norm-19 ideal with residue root `theta=1 mod 19` has class coordinate
`8`, hence generates `C_15`.  It is the sixth odd prime ideal in norm order.
Consequently the ordinary S-class group is already trivial at `T=211` and
remains trivial throughout the audited window.

The verifier constructs one nested squareclass basis through `T=221`.
Let `R` denote the norm-19 class generator.  The basis consists of

1. the two global unit squareclasses;
2. a generator of `R^15`; and
3. for every other selected ideal `P` of class coordinate `a`, a generator
   of `P R^e`, where `a+8e=0 mod 15`.

The parity valuation vectors are triangular: the `R^15` generator supplies
the `R` coordinate and every other generator supplies its own `P` coordinate,
possibly plus `R`.  Thus a prefix of length `T` has exactly `T+2`
independent S-unit squareclasses.

For the winner, the last member of `T` is

\[
 (1091,1091,\text{split root }605).                  \tag{2.3}
\]

## 3. Independent safe-kernel reconstruction

PARI gives the sign/modulo-four quotient `(C_2)^4` and ray-image rank four.
The verifier independently works in

\[
 (\mathbb Z/4\mathbb Z)[\theta]/(\theta^2-800243).
\]

This ring has eight units, two unit squares, and four square cosets.  Combining
their two quotient bits with the two exact real-embedding signs gives four
rows.  Their row space agrees exactly with PARI's row space on all 223 nested
basis elements, and has rank four for every audited prefix.  At `T=215`, the
verifier explicitly constructs the nullspace basis and obtains

\[
 d=(215+2)-4=213.                                    \tag{3.1}
\]

These are precisely the totally positive squareclasses that are squares
modulo `4 O_E`; their elementary quadratic extension is totally real,
dyadically unramified, and ramified only at `T`.

## 4. Exact CM scan and relation budget

For norm `Q=1 mod 3`, Eisenstein CM-usefulness is automatic.  For
`Q=2 mod 3`, the verifier evaluates the exact quadratic-residue functional
on the nested S-unit basis.  It accepts the ideal exactly when adjoining the
functional raises the four-row rank.  At the winning count it also checks
the equivalent dot-product test against the explicit 213-vector kernel
basis.

The result at `T=215` is

\[
 \boxed{10913\text{ useful ideals and }0\text{ rejections}}, \tag{4.1}
\]

with last useful ideal

\[
 (119359,119359,\text{split root }113172).            \tag{4.2}
\]

The safe real-quadratic Shafarevich charge is `d+1=214`.  With one
inertia-square relation per member of `T` and one Frobenius-square relation
per useful ideal,

\[
 r\le214+215+10913=11342,
 \qquad4r=45368=213^2-1<213^2.                       \tag{4.3}
\]

The strict quadratic Golod--Shafarevich test therefore proves an infinite
quotient.

## 5. Exact nearby-count optimization

Every count from 211 through 221 has trivial S-class group, ray rank four,
and zero CM rejections.  Their exact safe-constant thresholds are

\[
\begin{array}{c|c|c|c}
T&d&N&\alpha_*\\ \hline
211&209&10499&0.4936878760443372\\
212&210&10601&0.4936878630383672\\
213&211&10705&0.4936877133570425\\
214&212&10808&0.4936877117008696\\
215&213&10913&\mathbf{0.4936875853118874}\\
216&214&11017&0.4936876660186084\\
217&215&11123&0.4936876203226994\\
218&216&11228&0.4936877403426992\\
219&217&11335&0.4936877389416217\\
220&218&11441&0.4936878713288637\\
221&219&11549&0.4936878895761646.
\end{array}                                           \tag{5.1}
\]

Thus `T=215` is the exact unique winner in the dense nearby window; neither
the preliminary `T=217` nor a parity-neighboring count is competitive.

## 6. Root discriminant and endpoint

The verifier obtains

\[
 \log D_L={1\over2}\log3200972
 +{1\over4}\sum_{\mathfrak p\in T}\log N\mathfrak p
 =314.2108039946895731204827125815530\ldots .         \tag{6.1}
\]

It uses the rigorous upper bound

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
39223.8113252178896353028331981...
```

At the advertised exponent `0.49368759`, the 100- and 150-digit endpoint
margins are

```text
0.0007468374152892388744414644603...
0.0014851510032797045115949112286...
```

The active slopes are

```text
0.03071158948490050365865413083...
0.01912310012427806547979998554...
```

while the largest omitted slope is only
`0.00999969124866842964773938584...`.  The scale-one derivative is positive
and the scale-two derivative is negative.  Finally, the two fixed-anchor
roots are bracketed at

```text
0.4936875853118874120085565022998...
0.4936875853118874120085539752394...
```

both strictly below the advertised rounded exponent.

## 7. Scope

This certifies the displayed prefix construction and the exact dense count
window `211<=T<=221`.  It does not claim optimality over nonprefix choices,
mixed inertia orders, other quadratic fields, or different pro-2
presentations.  All arithmetic, kernel, CM, relation-count, root-discriminant,
and endpoint gates for the new record survive the hostile audit.
