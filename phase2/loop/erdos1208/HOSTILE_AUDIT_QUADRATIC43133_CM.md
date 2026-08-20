# Hostile audit of the quadratic-43133 CM construction

## 1. Verdict

The candidate survives an independent reconstruction.  With

\[
 E=\mathbb Q(\sqrt{43133}),                              \tag{1.1}
\]

the 223-ideal bounded-inertia tower, exact mod-3 useful-ideal test, and
CM/Eisenstein one-coordinate packing prove

\[
 \boxed{F_2(n)\ll n^{0.49369772}}.                      \tag{1.2}
\]

This is a material improvement over the preceding `0.493711480` record.
The audit did not reuse a claimed class number, Kummer matrix, useful list,
or endpoint from the discovery scan.  The companion verifier embeds its own
principal-generator certificate and rebuilds every finite calculation:

```text
python3 phase2/loop/erdos1208/verify_hostile_quadratic43133_cm.py
```

The optimized continuous threshold is approximately `0.49369771382`.  The
exact proof uses

\[
 \alpha=0.49369772,\qquad w_0=42282.8215.              \tag{1.3}
\]

## 2. Ring of integers, class number, and signatures

Put

\[
 \omega={1+\sqrt{43133}\over2},\qquad
 \omega^2=\omega+10783.                                \tag{2.1}
\]

The verifier checks that 43,133 is squarefree and prime.  It is `5 mod 8`,
so `O_E=Z[omega]`, the field discriminant is 43,133, and 2 is inert and
unramified.

Minkowski's bound for a real quadratic field is

\[
 {1\over2}\sqrt{43133}<104.                            \tag{2.2}
\]

The only odd rational primes producing prime ideals of norm below 104 are:

* inert `3,5,7`, whose ideals `(p)` are principal and have norms `p^2`;
* split
  `13,17,23,37,41,43,47,53,59,71,89,97,101,103`.

The verifier contains an explicit element of norm `+p` or `-p` for every
split prime in the second list.  Its conjugate generates the other ideal.
The inert dyadic ideal `(2)` is also principal.  Every prime ideal below the
Minkowski bound is therefore principal, so

\[
 h_E=1.                                                \tag{2.3}
\]

An exact norm-minus-one unit is

\[
 \epsilon=
 11516800325138112653+111443097178087930\,\omega.      \tag{2.4}
\]

Indeed, direct integer arithmetic gives `N(epsilon)=-1`.  Its two signs are
`(+,-)`, while `-1` has signs `(-,-)`, so these two units have full signature
rank.  Since the unit rank is one, a norm-minus-one unit represents the
nontrivial free-unit squareclass; hence `-1,epsilon` generate the full
two-dimensional unit squareclass space.

## 3. Exact 221-dimensional Kummer kernel

Order odd prime ideals of `E` by norm, retaining both ideals over split
rational primes and using the verifier's root tie order.  Let `T` be the
first 223 ideals.  Its last member is

\[
 (1163,1163,\text{split root }646).                     \tag{3.1}
\]

Class number one supplies one independent valuation squareclass for every
ideal in `T`.  Together with `-1` and `epsilon`, this gives 225 independent
columns.  To avoid the dyadic prime and infinity, impose:

1. positivity at both real embeddings; and
2. membership in the unit-square coset modulo `4O_E`.

The verifier constructs `(O_E/4O_E)^*` directly.  It has 12 elements, its
square subgroup has three elements, and its square-coset quotient has rank
two.  On the 225 explicit Kummer generators, the combined two-sign/two-
dyadic matrix has exact rank four.  Therefore

\[
 \dim\ker C=225-4=221.                                 \tag{3.2}
\]

Every kernel class is totally positive and congruent to a unit square
modulo 4, so its quadratic extension is totally real, unramified above 2,
and unramified outside `T`.  Thus the maximal tame totally real pro-2 group
has generator rank at least 221.

The verifier does not trust a principal-ideal oracle here.  It embeds one
explicit `a+b omega` for each of the 108 split rational primes occurring in
`T`, checks `|N(a+b omega)|=p`, and uses the residue root to select the
correct conjugate prime ideal.  Inert generators are the rational elements
`p`.  Thus every sign and mod-4 column is tied to an exact ideal generator.

## 4. Relation and root-discriminant budget

Use the conservative real-quadratic Shafarevich bound

\[
 r_0\le d+1=222.                                       \tag{4.1}
\]

Add one inertia-square relation at every ideal in `T` and one
Frobenius-square relation at each of 11,765 useful ideals.  The total is

\[
 r\le222+223+11765=12210,\qquad
 4\cdot12210=221^2-1.                                  \tag{4.2}
\]

Hence the quotient is infinite by the strict quadratic
Golod--Shafarevich inequality.  If the actual generator rank exceeds the
certified lower bound, the gap only increases because
`d^2-4(d+1+223+11765)` is increasing for `d>=221`.

Order-two relative inertia contributes exponent `1/4` per base ideal norm,
so the absolute root-discriminant bound is

\[
 D_L=\sqrt{43133}\prod_{\mathfrak p\in T}
       N_E(\mathfrak p)^{1/4}.                          \tag{4.3}
\]

The exact 100-digit computation gives

\[
 \log D_L=
 331.6124924085130132231992219788157376\ldots.         \tag{4.4}
\]

For the CM compositum `L(zeta_3)`, the relative discriminant divides
`3O_L`, and the unscaled complex Minkowski covolume is
`2^{-[L:Q]}sqrt(|Disc(L(zeta_3))|)`.  Thus the relative discriminant and
complex covolume combine exactly into the already audited effective
constant

\[
 C_{\rm Eis}={2\sqrt3\over\pi}<{71603\over64935}.      \tag{4.5}
\]

There is no additional `sqrt(3)` factor in (4.3).

## 5. Exact mod-3 useful-ideal audit

Let `q` be a prime ideal of `E` outside `T`, with norm `Q`.  A
Frobenius-square cap gives relative residue degree `f in {1,2}` in retained
layers.  A prime above `q` splits in the Eisenstein CM extension precisely
when

\[
 Q^f\equiv1\pmod3.                                     \tag{5.1}
\]

Therefore `Q=1 mod 3` is automatically admissible.  When `Q=2 mod 3`, the
Frobenius must be nonzero on the exact Kummer kernel, so that its square cap
forces exact order two.  If `lambda_q` is its quadratic-residue row on all
225 generators, this condition is exactly

\[
 \operatorname {rank}\binom C{\lambda_{\mathfrak q}}>4. \tag{5.2}
\]

The independent scan evaluates (5.2) ideal by ideal and finds

\[
 \boxed{0\text{ rejections before }11765\text{ useful ideals}.} \tag{5.3}
\]

The last useful ideal is

\[
 (129629,129629,\text{split root }2193).                \tag{5.4}
\]

The unique base ideal over 43,133 is outside `T`, has norm `2 mod 3`, and
occurs at zero-based useful position 4,190.  It is treated separately as a
ramified ideal of `E/Q`: modulo it,

\[
 \omega\longmapsto {1\over2}.
\]

Its exact Frobenius row is nonzero on the 221-dimensional kernel.  Thus the
base ideal is not silently accepted using the split-prime formula.

For a full prime-ideal orbit, the absolute-degree-normalized local marginal
is

\[
 c_{\mathfrak q,k}={\log Q\over2},\qquad
 g_{\mathfrak q,k}={1\over4}\log A_k(Q^{-2}).           \tag{5.5}
\]

This retains the exact prime-ideal normalization; there is no factor-two
amplification from the quadratic base.

## 6. Independent all-depth endpoint certificate

Let `F` be the globally sorted fractional frontier formed from (5.5).  With
the CM constant (4.5), the endpoint inequality is

\[
 F(2\alpha w)\ge
 \log(C_{\rm Eis}D_L)+(2-4\alpha)w+
 \log\left(1+{e^{2(2\alpha-1)w}\over C_{\rm Eis}D_L}\right).
                                                               \tag{6.1}
\]

At the exact values (1.3), after subtracting `10^-25`, the two dyadic
endpoint margins are

\[
 0.00106062470672\ldots,\qquad
 0.00210947043875\ldots.                               \tag{6.2}
\]

The fixed-anchor endpoint zeros are independently bracketed at

\[
 0.49369771382320730579\ldots,\qquad
 0.49369771382258912981\ldots.                         \tag{6.3}
\]

At the right endpoint the active slope is
`0.0190310817846...`, while the maximum omitted fourth-depth slope is
`0.0157605409660...`.  Marginal monotonicity excludes every later depth.
The right prefix contains 11,765 first-depth, 4,126 second-depth, and 92
third-depth full items before its fractional item.

Concavity on `[w_0,2w_0]`, dyadic layer selection, and placewise rounding
now prove (1.2).

## 7. Scope of the audit

No flaw was found.  The class-number proof, full unit signatures, exact
Kummer rank, exceptional base-ideal row, zero-rejection useful prefix,
root-discriminant exponent, CM covolume, and all-depth endpoint all survive
independent reconstruction.

As a neighboring cross-check, the same independent code also audited the
weaker `T=231`, `d=229`, `N=12649` configuration: it again found no useful
rejections and recovered threshold `0.493698124...`.  The theorem stated
here uses the strictly better `T=223` certificate.

The result is still an upper-bound improvement, not a solution of Erdős
#1208: the exponent remains far above the conjectural `1/3`.  Its importance
is that the improvement is roughly `1.38e-5`, much larger than the preceding
ninth-decimal cap and prefix optimizations.
