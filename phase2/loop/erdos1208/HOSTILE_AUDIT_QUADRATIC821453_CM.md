# Hostile audit of the quadratic-821453 CM record

## 1. Verdict

The candidate survives an independent exact reconstruction.  In the
bounded-inertia plus Eisenstein-CM construction, take

\[
 E=\mathbb Q(\sqrt{821453}),\qquad t=219,qquad d=217,
 \qquad N=11335.                                      \tag{1.1}
\]

The certified endpoint gives

\[
 \boxed{F_2(n)\ll n^{0.49369313}}.                    \tag{1.2}
\]

This improves the preceding `0.49369772` exponent.  The safe-rational
continuous threshold is

```text
0.49369312444406914824...
```

The small difference from scans reporting approximately
`0.49369312432` is explained by the verifier's rational upper bound
`71603/64935` for `2 sqrt(3)/pi`.  The rounded theorem exponent
`0.49369313` has much more slack than that difference.

The companion verifier is

```text
python3 phase2/loop/erdos1208/verify_hostile_quadratic821453_cm.py
```

It requires PARI/GP.  PARI certifies the BNF and produces exact integer
Kummer representatives; the script independently checks their signs and
modulo-four square conditions, every useful-prime test, the GS relation
count, the endpoint, and all possible ray-rank changes.

## 2. Exact field and Kummer data

The discriminant factors as

\[
 821453=467\cdot1759,qquad 821453\equiv5\pmod8,
 \qquad821453\equiv2\pmod3.                           \tag{2.1}
\]

Both factors are prime and the discriminant is squarefree.  With

\[
 \omega={1+\sqrt{821453}\over2},\qquad
 \omega^2=\omega+205363,                              \tag{2.2}
\]

PARI's certified BNF gives

\[
 h_E=1,qquad h_E^+=2.                                 \tag{2.3}
\]

Thus there is no norm-minus-one unit.  The verifier also checks directly
that PARI's displayed fundamental-unit conjugate has norm one and is
positive at both real places.

Order odd prime ideals by norm, keeping both conjugate ideals above a split
rational prime.  Let `T` be the first 219.  Its last member is

\[
 (1213,1213,\text{split root }395).                    \tag{2.4}
\]

The two unit squareclasses and 219 valuation squareclasses give 221
columns.  Positivity at two real places and the unit-square condition
modulo `4 O_E` have exact rank four.  Consequently the safe Kummer kernel
has dimension

\[
 d=221-4=217.                                         \tag{2.5}
\]

PARI outputs an explicit basis of all 217 kernel classes.  The verifier
checks, with integer arithmetic, that every one is positive at both real
embeddings and lies in one of the three unit-square residues in
`(O_E/4O_E)^*`.  Therefore the corresponding elementary quadratic
extension is totally real, dyadically unramified, and ramified only in
`T`.

## 3. Relation and useful-prime budget

Use the safe real-quadratic Shafarevich bound

\[
 r_0\le d+1=218.                                      \tag{3.1}
\]

Add one inertia-square relation at each of the 219 primes in `T` and one
Frobenius-square relation at each of `N=11335` useful primes.  Then

\[
 r\le218+219+11335=11772,
 \qquad 4r=217^2-1.                                  \tag{3.2}
\]

The strict quadratic Golod--Shafarevich test therefore gives an infinite
quotient.

For a prime ideal of norm `Q`, the Eisenstein CM step is automatic when
`Q=1 mod 3`.  When `Q=2 mod 3`, its Frobenius functional must be nonzero on
the 217-dimensional Kummer kernel; after the square cap this forces exact
relative residue degree two.  The verifier evaluates this condition on
the exact kernel and finds

\[
 \boxed{0\text{ rejections before all }11335
 \text{ useful ideals are collected}.}               \tag{3.3}
\]

The last useful ideal is

\[
 (122527,122527,\text{split root }3683),               \tag{3.4}
\]

and at most 12 kernel representatives are inspected in any nontrivial
test.  Of the two base-ramified rational primes, the ideal above 467 is the
115th ideal and lies in `T`; the ideal above 1759 is outside `T`, is
automatically CM-useful because `1759=1 mod 3`, and occurs in useful
position 60.

## 4. Endpoint certificate

Order-two inertia contributes `N(p)^(1/4)` to the absolute root
discriminant.  The verifier obtains

\[
 \log D_L=
 322.2254902582720516650681010254956678839\ldots .    \tag{4.1}
\]

For each useful ideal of norm `Q`, it forms the full all-depth local
frontier with

\[
 c(Q)={\log Q\over2},\qquad
 g_j(Q)={1\over4}\log A_j(Q^{-2}).                    \tag{4.2}
\]

At

\[
 \alpha=0.49369313,\qquad w_0=40752.9517,             \tag{4.3}
\]

the left and right endpoint margins, after subtracting `10^-25`, are

```text
0.00117455846108839680...
0.00117473610479516014...
```

The active slopes are respectively

```text
0.03061510174469776385...
0.01905568908395088350...
```

and the maximum fourth-depth slope is about `0.01571245`, below the active
right slope.  Thus no omitted deeper local role is active.  At the fixed
anchor (4.3), the two endpoint zeros are

```text
0.49369312290327526107...
0.49369312643078295828...
```

The slightly better equal-endpoint anchor is
`40752.90071209...`, giving the safe-rational threshold in Section 1.

## 5. The non-prefix ray-rank issue

This audit found and then closed a real trap in the discovery logic: an
arbitrary non-prefix choice of 219 ramified ideals need not keep the
four-row ray-condition rank.

The exact ray group for modulus `(4 O_E; both real places)` is
`(C_2)^4`.  The two unit columns have rank two.  Modulo their span, the
prime-ideal columns therefore have four colors in `F_2^2`.  If the selected
colors span a quotient subspace of dimension `s`, then

\[
 \operatorname {rank}C=2+s,qquad d=219-s.            \tag{5.1}
\]

There are exactly three quotient lines and one zero subspace.  The
verifier treats all of them, not merely the prefix.  Its all-square results
are:

\[
\begin{array}{c|c|c|c|c|c|c}
\operatorname {rank}C&d&N&\text{prefix deletions}&
\text{last }N\mathfrak p&\log D_L&\alpha_*\\ \hline
4&217&11335&0&1213&322.2254903&0.49369312444\\
3&218&11442&95&3089&366.7277907&0.49386496357\\
3&218&11442&108&3389&371.7135811&0.49388484060\\
3&218&11442&117&3467&373.8461657&0.49389386701\\
2&219&11551&160&8009&422.2268228&0.49406716818
\end{array}                                           \tag{5.2}
\]

Here `prefix deletions` is the number of ideals among the original first
219 that must be discarded before all selected columns can lie in the
specified subspace.  In particular, a one-for-one local perturbation cannot
produce the bonus: every one of the `219*81=17739` swaps with one of the
next 81 ideals retains rank four.  The script also checks rank four for all
ordinary prefixes from 205 through 250.

Table (5.2) is an arbitrary-assignment exclusion, not just a minimum-root-
discriminant heuristic.  For completeness, at frontier slope `lambda` put

\[
 V_\lambda(Q)=\sum_{j\ge1}
   \left(g_j(Q)-{\lambda\log Q\over2}\right)_+.       \tag{5.3}
\]

The all-depth exchange inequalities already used in the `D=43133` lock are
field-independent for `Q>=9`: `V_lambda(Q)` is nonincreasing, and whenever
`K` terms are active,

\[
 V_\lambda'(\log Q)>-{1\over4\log Q}.                \tag{5.4}
\]

The verifier rechecks the strict rational inequality behind (5.4).  Also,
through every case in (5.2), the root-discriminant tangent has

\[
 \rho>{1\over\log9}.                                  \tag{5.5}
\]

It follows that `rho log(Q)/4+V_lambda(Q)` increases with `Q`.
Successive role exchanges therefore show that, inside each fixed ray-color
subspace, the optimistic optimum uses the 219 smallest allowed ideals for
inertia and the first `N` remaining ideals for useful roles.  Every
remaining ideal is declared useful in this comparison, even if its actual
CM/Kummer test might fail, so this is favorable to the competitor.

Finally, at `alpha=0.49369313` the four rank-dropping rows have both
endpoint margins negative at a separator, with positive left derivative
and negative right derivative.  Concavity excludes every anchor.  The
smallest absolute margin is over 29, so numerical precision is irrelevant.

## 6. Neighbor and scope

As a neighboring cross-check, the first 221 ideals have last member

```text
(1223,1223,split root 34),
```

retain ray rank four, and give `(d,N)=(219,11549)`.  Their safe-rational
optimized threshold is approximately `0.4936931721`, slightly worse than
the `t=219` certificate.

No arithmetic or endpoint flaw was found.  The audit proves the displayed
record inside the already established bounded-inertia and CM/Eisenstein
framework.  It also locks arbitrary all-square ramified-prime assignments
for this field.  It does not claim that `D=821453` is optimal among all
base fields or all pro-2 presentations, and it does not by itself resolve
Erdos problem 1208; it improves the constructive upper-bound exponent.

