# Hostile audit of the quadratic-2278757 CM construction

## 1. Verdict

The new candidate survives an independent reconstruction and improves the
certified upper exponent.  In the bounded-inertia Eisenstein-CM construction,
take

\[
 E=\mathbb Q(\sqrt{2278757}),\qquad T=223,qquad d=221,
 \qquad N=11765.                                      \tag{1.1}
\]

The exact endpoint certificate gives

\[
 \boxed{F_2(n)\ll n^{0.49368818}}.                   \tag{1.2}
\]

The optimized continuous threshold, using the safe rational geometric
constant, is

```text
0.49368816734324590927214820...
```

This strictly improves the preceding `0.49369313` theorem.

The companion verifier is

```text
python3 phase2/loop/erdos1208/verify_hostile_quadratic2278757_cm.py
```

It requires PARI/GP.  The verifier independently constructs the
class-number-two S-unit basis, rebuilds its sign/modulo-four kernel with
integer arithmetic, checks every CM-usefulness functional, verifies the
Golod--Shafarevich budget, and recomputes the all-depth endpoint at 100 and
150 decimal digits.

## 2. Exact field and S-unit arithmetic

The fundamental discriminant factors as

\[
 2278757=13\cdot59\cdot2971,
 \qquad 2278757\equiv5\pmod8.                        \tag{2.1}
\]

With

\[
 \omega={1+\sqrt{2278757}\over2},\qquad
 \omega^2=\omega+569689,                             \tag{2.2}
\]

PARI's certified BNF gives

\[
 \operatorname {Cl}(E)\simeq C_2,qquad
 \operatorname {Cl}^+(E)\simeq(C_2)^2.              \tag{2.3}
\]

Order odd prime ideals by norm, retaining both conjugate ideals above each
split rational prime.  The first 223 have last member

\[
 (1109,1109,\text{split root }152).                  \tag{2.4}
\]

They kill the ordinary class group.  The first nonprincipal member is the
norm-19 ideal

\[
 R=(19,19,\text{split root }4),                      \tag{2.5}
\]

which generates `Cl(E)=C_2`.

The verifier does not rely on a black-box reduced S-unit basis.  It constructs
the 225 independent squareclasses from

1. the two global unit squareclasses;
2. a generator of \(R^2\);
3. a generator of each principal \(S\)-prime \(P\); and
4. a generator of \(PR\) for each other nonprincipal \(S\)-prime \(P\).

The valuation vectors, together with the class-torsion class represented by
the generator of `R^2`, prove independence via the exact Kummer sequence.

For modulus `(4 O_E; both real places)`, PARI gives ray quotient
`(C_2)^4`.  Its image on the displayed S-unit basis has rank four.  The
verifier independently reconstructs the two exact signs and the unit-square
cosets modulo `4 O_E`; the resulting four-row space agrees exactly with
PARI's row space.  It then explicitly constructs a basis for the nullspace,
obtaining

\[
 \dim V_S=225-4=221.                                 \tag{2.6}
\]

Every class in this kernel is totally positive and square modulo four, so
the associated elementary quadratic extension is totally real, dyadically
unramified, and ramified only at the selected 223 odd ideals.

## 3. Exact CM-usefulness and Golod--Shafarevich budget

For a candidate prime ideal of norm `Q`, the Eisenstein CM condition is
automatic when `Q=1 mod 3`.  If `Q=2 mod 3`, reduction modulo the prime gives
a quadratic-residue functional on the 225-dimensional S-unit space.  This
prime is useful precisely when the functional is nonzero on the
221-dimensional safe kernel.

The verifier checks this in two equivalent exact ways for every nontrivial
case:

- adjoining the functional must raise the rank of the four local rows;
- its dot product with at least one displayed kernel basis vector must be
  nonzero.

Both tests agree throughout.  The result is

\[
 \boxed{11765\text{ useful ideals and }0\text{ rejections}}. \tag{3.1}
\]

The last useful ideal is

\[
 (128591,128591,\text{split root }112589).             \tag{3.2}
\]

Use the safe real-quadratic Shafarevich charge

\[
 r_0\le d+1=222.                                     \tag{3.3}
\]

Adding one inertia-square relation at each of the 223 members of `T` and one
Frobenius-square relation at each useful ideal gives

\[
 r\le222+223+11765=12210,
 \qquad4r=48840=221^2-1<221^2.                       \tag{3.4}
\]

Thus the strict quadratic Golod--Shafarevich inequality proves that the
resulting quotient is infinite.

## 4. Root discriminant and endpoint

Order-two tame inertia contributes `N(P)^(1/4)` to the absolute root
discriminant.  The verifier obtains

\[
 \log D_L={1\over2}\log2278757
     +{1\over4}\sum_{\mathfrak p\in T}\log N\mathfrak p
 =328.9023201108733322545453172460507\ldots .         \tag{4.1}
\]

The Eisenstein one-coordinate disk construction uses the safe upper bound

\[
 {2\sqrt3\over\pi}<{71603\over64935}.                \tag{4.2}
\]

For every useful ideal of norm `Q`, the verifier forms the all-depth local
frontier with

\[
 c(Q)={\log Q\over2},\qquad
 g_j(Q)={1\over4}\log A_j(Q^{-2}).                   \tag{4.3}
\]

The equal-endpoint optimization gives

\[
 w_0=42181.88468481482562429262\ldots                \tag{4.4}
\]

and the threshold quoted in Section 1.  At the advertised rounded exponent
`alpha=0.49368818`, the two endpoint margins are

```text
0.0021681240908213362124278540262...
0.0043117690115405944376147960876...
```

at both 100- and 150-digit precision.  Their active frontier slopes are

```text
0.03051319985700102549562834181...
0.01905046157918761239659015450...
```

whereas the largest omitted slope is only

```text
0.00999969124866842964773938584...
```

so no deeper local role is active.  The scale-one derivative is positive
and the scale-two derivative is negative.  The two fixed-anchor endpoint
roots independently bracket at

```text
0.49368816734324590927214838414711...
0.49368816734324590927214828770566...
```

both strictly below `0.49368818`.

## 5. Scope

This note certifies the displayed norm-prefix construction and the resulting
upper exponent.  It does not claim optimality over other real quadratic
fields, nonprefix ramification assignments, mixed inertia orders, or other
pro-2 presentations.  Its purpose is hostile verification of the new record:
all arithmetic, CM, relation-count, discriminant, and endpoint gates survive.
