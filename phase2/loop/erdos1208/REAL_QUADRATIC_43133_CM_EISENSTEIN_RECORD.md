# A stronger quadratic-base CM/Eisenstein record

## 1. Certified result

Let

\[
 E=\mathbb Q(\sqrt{43133}),\qquad
 \omega={1+\sqrt{43133}\over2}.
\]

The bounded-inertia pro-2 tower over `E`, followed by the Eisenstein CM
compositum and one-complex-coordinate disk packing, proves

\[
 \boxed{F_2(n)\ll n^{0.49369772}}.                       \tag{1.1}
\]

This supersedes the `Q(sqrt(1949))` CM exponent `0.49371148` by about
`1.376e-5`.  For the chosen arithmetic data, the continuous two-endpoint
threshold diagnostic is

\[
 \alpha_*\approx0.4936977138,\qquad
 w_*\approx42282.82.                                    \tag{1.2}
\]

These final optimization digits are diagnostic only.  The finite certificate
uses the safely rounded values

\[
 \alpha=0.49369772,\qquad w_0=42282.88.                 \tag{1.3}
\]

Run

```text
python3 phase2/loop/erdos1208/verify_cm_eisenstein_real_quadratic_43133.py
```

with PARI/GP available.  It was certified with GP 2.17.4 and Python 3.  The
script runs exact BNF, S-unit, ray-group, and finite-field calculations, then
independently performs the prime enumeration, sparse Kummer-kernel Frobenius
tests, relation budget, and 90/150-digit endpoint calculation.

## 2. Exact Kummer and Golod--Shafarevich data

PARI's unconditional `bnfcertify` check proves that `E` has class number one.
Let `T` be the first 223 odd prime ideals, in increasing norm and the exact
tie order reconstructed by the verifier.  The final ideal is

\[
 (N\mathfrak p,p,\omega\bmod\mathfrak p)=(1163,1163,646). \tag{2.1}
\]

The exact fundamental-S-unit calculation gives 225 squareclass generators.
Map them to the ray square quotient for modulus

\[
 (4O_E;\text{both real places}).                         \tag{2.2}
\]

This quotient is `(Z/2)^4`, and the 225 columns have rank four.  Therefore
the totally positive, square-modulo-4 Kummer kernel has dimension

\[
 d=225-4=221.                                           \tag{2.3}
\]

The verifier expands an exact basis of all 221 kernel classes.  Independently
of the ray-group calculation it checks, with integer sign tests, that every
basis element is positive at both real embeddings, and by exhaustive
arithmetic in `O_E/4O_E` that every one is a unit square modulo 4.  Hence the
associated quadratic extensions are totally real and unramified at the
dyadic prime.

Use the conservative quadratic-base Shafarevich bound `r_0<=d+1=222`.
Square-cap inertia at all 223 primes of `T`.  Outside `T`, select 11,765
prime ideals and square-cap their Frobenius elements.  The resulting
presentation has

\[
 r\le222+223+11765=12210,
 \qquad 4r=48840=221^2-1<d^2.                           \tag{2.4}
\]

All added relators are squares and therefore lie in the Frattini subgroup;
the generator rank remains 221.  The degree-two Golod--Shafarevich test makes
the quotient infinite.

## 3. Correct Eisenstein useful-prime test

For a prime ideal `q` of `E` outside `T`, write `Q=N_E(q)`.  In a
Frobenius-square-capped layer the relative residue degree is one or two.  A
prime above `q` splits in the CM compositum `L(zeta_3)/L` exactly when

\[
 Q^f\equiv1\pmod3.                                      \tag{3.1}
\]

Thus `Q=1 mod 3` is automatic.  When `Q=2 mod 3`, the Frobenius functional
must be nonzero on the 221-dimensional Kummer kernel; the square cap then
forces exact order two and `f=2`.

The verifier tests this without a probabilistic assumption.  For every such
prime it searches the displayed sparse kernel basis until it finds a
quadratic nonresidue.  Across the entire useful prefix it needs at most 12
basis elements, and there are zero rejections.  The exact prefix data are

\[
 \#\{\text{useful ideals}\}=11765,\qquad
 N\mathfrak q_{\rm last}=129629.                         \tag{3.2}
\]

The rational prime 43,133 ramifies in `E/Q`, lies outside `T`, and must not be
silently treated as an ordinary split prime.  Its residue map is
`omega -> 1/2`; it passes the kernel test and is useful ideal number 4,191.
The verifier checks this edge case explicitly.

For a useful ideal and local depth `k`, the exact absolute-degree-normalized
cost and uniform CM gain are

\[
 c_{\mathfrak q,k}={\log Q\over2},\qquad
 g_{\mathfrak q,k}={1\over4}\log A_k(Q^{-2}).            \tag{3.3}
\]

There is no prime-ideal multiplicity amplification.

## 4. Root discriminant and CM disk constant

Inertia square caps give `e_p<=2` in every finite layer, hence

\[
 D_L=\sqrt{43133}\prod_{\mathfrak p\in T}
       N_E(\mathfrak p)^{1/4},                           \tag{4.1}
\]

and the exact selected prefix gives

\[
 \log D_L=
 331.6124924085130132231992219788157375\ldots.           \tag{4.2}
\]

The dyadic prime is excluded from `T`.  Since 3 is inert in `E`, the unique
ideal above 3 has norm 9 and does lie in `T`; it is an ordinary odd tame
inertia cap in the real tower.  Characteristic 3 is excluded from the useful
Frobenius list.  Its additional ramification in the CM step is accounted for
only through the relative-discriminant bound below, so it is neither omitted
nor counted twice.

For `K=L(zeta_3)`, the relative order `O_L[zeta_3]` has discriminant
`-3O_L`, so

\[
 |Disc(K)|\le Disc(L)^2 3^{[L:Q]}.                       \tag{4.3}
\]

The unscaled complex Minkowski covolume and planar disk area combine to the
effective one-coordinate constant

\[
 C_{\rm Eis}={2\sqrt3\over\pi}.                         \tag{4.4}
\]

The certificate uses the rational upper bound

\[
 C_{\rm Eis}<{71603\over64935},                         \tag{4.5}
\]

deduced from `sqrt(3)<1351/780` and `pi>333/106`.  The factor `sqrt(3)` is
already contained in (4.4); it is not inserted again into (4.1).

The CM norm-divisor switch uses

\[
 \eta=z\bar z=N_{K/L}(z)\in O_L.                        \tag{4.6}
\]

Every real embedding sends `eta` to the corresponding squared complex
absolute value.  Equality in the distinguished planar embedding forces
equality in `L`, so the distance-Sidon multiplicity argument and the local
split-prime divisor patterns carry over unchanged.

## 5. Endpoint certificate

With

\[
 w={\log n\over2m},\qquad L_0=2\alpha w,
\]

the two endpoint conditions are instances of

\[
 F(2\alpha w)\ge
 \log(C_{\rm Eis}D_L)+(2-4\alpha)w+
 \log\left(1+{e^{2(2\alpha-1)w}\over C_{\rm Eis}D_L}\right). \tag{5.1}
\]

At (1.3), after replacing `C_Eis` by (4.5) and subtracting `10^-25`, the
150-digit endpoint margins are

\[
 0.0013481280484140390874459401787\ldots,
 \qquad
 0.0013585741933157831762958068957\ldots.                \tag{5.2}
\]

At the right endpoint the active slope is

\[
 0.01903108178461475143\ldots,                           \tag{5.3}
\]

whereas the largest omitted fourth-depth slope is

\[
 0.01576054096599877036\ldots.                           \tag{5.4}
\]

Local marginal monotonicity excludes every deeper item.  The fixed-anchor
roots are `0.493697712148876...` and `0.493697716021533...`, both strictly
below the safe headline (1.1).  Concavity, dyadic layer selection, and
placewise rounding then prove the result.

## 6. Search audit and scope

`scan_cm_eisenstein_real_quadratic_bases.cpp` reconstructs actual prime-ideal
norm sequences for all 30,394 positive fundamental discriminants at most
100,000.  It first applies the deliberately optimistic assumptions that the
standard four sign/dyadic conditions are the only Kummer loss and that every
outside prime is useful, then densely rescans the leading bases over nearby
ramified-ideal counts.  This found `D=43133`; the exact verifier subsequently
certified every input used in (1.1).

The closest optimistic competitors in the leading dense rescan were

\[
\begin{array}{c|c|c}
D&\text{best nearby }|T|&\text{all-useful threshold}\\ \hline
43133&223&0.49369771370\\
68312&225&0.49369867570\\
50237&225&0.49369905334\\
66965&225&0.49369928043\\
72509&223&0.49369992866
\end{array}                                             \tag{6.1}
\]

Exact `bnfcertify`/S-unit/ray calculations on these leading bases reproduce
the assumed generator losses.  Since “all useful” is already more favorable
than any honest mod-3 prefix, none of the four displayed competitors can beat
(1.1).

The broad scan is an explicit finite search audit, not a theorem that no
unscanned field or more exotic Kummer presentation can improve the exponent.
The construction remains far above the conjectural cube-root scale; the gain
is a real upper-bound record inside the current arithmetic-tower family, not
a resolution of Erdos 1208.
