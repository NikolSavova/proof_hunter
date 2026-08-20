# Exact quadratic-base CM record at exponent `0.49368647`

## Theorem

The bounded-inertia real-quadratic/Eisenstein-CM construction, inserted into
the tower-to-distance argument of `proof_prime_power.md`, gives

\[
F_2(n)\ll n^{0.49368647}.
\]

The underlying real quadratic field is

\[
E=\mathbf Q(\sqrt{4,108,373}),
\]

with 217 norm-prefix ramified odd prime ideals, safe Kummer generator rank 215,
and 11,123 useful Frobenius-square caps.  The exact optimized endpoint is

\[
\alpha_*=0.4936864598096758088590628660819\ldots,
\]

so the displayed exponent has positive certified slack.

## Field and Kummer arithmetic

The discriminant factors as

\[
4,108,373=17\cdot67\cdot3607,
\]

is squarefree, and is congruent to 5 modulo 8.  PARI/GP certifies

\[
\operatorname{Cl}(E)\cong C_2,
\qquad h(E)=2,
\qquad h^+(E)=4.
\]

For the first `T=217` odd prime ideals, the exact localized data are:

- localized `S`-class group trivial;
- 219 `S`-unit squareclass columns;
- sign/mod-4 ray quotient `[2,2,2,2]`;
- ray constraint rank four;
- positive, mod-4-square kernel dimension `219-4=215`;
- final ramified ideal `(norm,root)=(1117,1020)`.

The same localized class triviality and full ray rank already hold at `T=213`,
so the nearby count comparison uses the same exact formula `d=T-2`.

## Golod--Shafarevich budget

With `d=215`, the strict all-quadratic relation ceiling is

\[
R_{\max}=\left\lfloor\frac{215^2-1}{4}\right\rfloor=11,556.
\]

The conservative Shafarevich presentation costs `d+1=216` relations.  Imposing
square relations on all 217 tame inertia generators and on 11,123 useful
Frobenius elements gives

\[
216+217+11,123=11,556=R_{\max}.
\]

At `y=2/215` the weighted GS polynomial is strictly negative, so the capped
pro-2 quotient remains infinite.

## Exact CM usefulness scan

The verifier asks PARI for an exact basis of the 215-dimensional
positive/mod-4-square Kummer kernel.  For a prime ideal of norm congruent to 2
modulo 3, it evaluates the basis elements at the exact residue root and searches
for a quadratic nonresidue.  Norms congruent to 1 modulo 3 are automatic.

All 11,123 required ideals pass.  There are no rejected ideals; among 5,560
nonautomatic tests the maximum search length is 15 basis elements.  The last
useful ideal has

\[
(N\mathfrak q,\text{root})=(121367,69978).
\]

Thus the optimistic all-useful stream seen by the discovery scanner is the
actual useful stream for the entire certified prefix.

## Root discriminant and endpoint

The real-tower contribution is

\[
\log\operatorname{rd}
=\frac12\log(4,108,373)
 +\frac14\sum_{j\le217}\log N\mathfrak p_j
=317.6510581919590472759259853\ldots.
\]

Using the adverse rational bound

\[
\frac{2\sqrt3}{\pi}<\frac{71603}{64935}
\]

and `alpha=0.49368647`, the two endpoint margins are respectively

```text
0.001653951088349088650071331725...
0.003289091497997211036560101621...
```

Their derivatives have the required signs, greater than `0.0050169` on the
left and less than `-0.0127695` on the right.  The maximum fourth-depth slope is
`0.01582551`, below the smaller active slope `0.01911067`, so the three-depth
scanner frontier is exact at the decisive endpoints.  The independent
all-depth frontier gives the same result.

The complete endpoint calculation is repeated at both 90- and 150-digit
Decimal precision; the threshold and anchor agree far beyond the displayed
digits.

## Nearby ramified counts

Giving every formal prime the favorable status of useful produces the exact
norm-prefix thresholds

| `T` | `d` | threshold |
|---:|---:|---:|
| 213 | 211 | `0.4936865405847246860...` |
| 215 | 213 | `0.4936864859482317721...` |
| **217** | **215** | **`0.4936864598096758089...`** |
| 219 | 217 | `0.4936865198690186834...` |
| 221 | 219 | `0.4936866662073595852...` |
| 223 | 221 | `0.4936868519916800232...` |
| 225 | 223 | `0.4936871392895276881...` |

Consequently `T=217` is the unique optimum in this nearby window.  Since all
other rows were granted the all-useful relaxation, their exclusion does not
depend on an unperformed CM usefulness test.

## Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_quadratic4108373_cm_exact_record.py
```

The verifier independently checks the factorization and fundamental
discriminant, certified BNF/narrow/localized class data, exact ray kernel,
every useful-prime test, strict GS budget, all-depth endpoint, 90/150 precision
agreement, and nearby count table.  Expected final line:

```text
Q(sqrt(4108373)) CM F_2(n) << n^0.49368647: CERTIFIED
```

## Scope

This is a rigorous improvement inside the established bounded-inertia
quadratic-base CM construction.  It does not prove that this discriminant is
globally optimal, does not lock arbitrary nonprefix ramification assignments,
and does not resolve Erdos problem 1208 completely.  The fast scanner remains
a discovery tool; this certificate no longer depends on its floating-point or
depth/finalist heuristics.
