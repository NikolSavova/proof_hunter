# Rank-aware no-go for the genus leaders 963480 and 937365

## 1. Verdict

The next two genus-screen leaders after `D=880440` do not survive an exact
rank-aware audit.  For

\[
 E_1=\mathbb Q(\sqrt{240870}),\quad \operatorname {Disc}(E_1)=963480,
 \qquad
 E_2=\mathbb Q(\sqrt{937365}),\quad \operatorname {Disc}(E_2)=937365,
                                                               \tag{1.1}
\]

the companion verifier excludes every all-inertia-square configuration with

\[
 205\le |T|\le250                                    \tag{1.2}
\]

at the current exponent `0.49369313`.  This includes every nonprefix choice
of ramified prime ideals, partitioned by its exact ordinary-class and ray
Frattini spans.

```text
python3 phase2/loop/erdos1208/verify_genus_bonus_963480_937365_rank_aware_audit.py
```

PARI/GP certifies the number-field data and exact ideal colors.  Python
independently enumerates all relevant color subspaces, minimizes ramified
products, and verifies the continuous endpoint exclusions.

## 2. Certified arithmetic

The discriminants factor as

\[
 963480=2^3\cdot3\cdot5\cdot7\cdot31\cdot37,
 \qquad
 937365=3\cdot5\cdot11\cdot13\cdot19\cdot23.        \tag{2.1}
\]

PARI's `bnfcertify` succeeds and gives

\[
\begin{array}{c|c|c|c}
D&\operatorname {Cl}(E)&\operatorname {Cl}^+(E)&
 \operatorname {Cl}_{(4;\infty,\infty)}(E)\\ \hline
963480&C_4\times(C_2)^3&C_4\times(C_2)^4&C_8\times(C_2)^5\\
937365&(C_2)^4&(C_2)^5&C_{12}\times(C_2)^5.
\end{array}                                           \tag{2.2}
\]

Thus both ordinary class groups have four-dimensional Frattini quotient,
and both ray groups have six-dimensional Frattini quotient.  The image of
the two global unit squareclasses in the sign/modulo-four local quotient has
rank two for `D=963480` and rank one for `D=937365`.

For the first 205 odd prime ideals, both exact computations give

```text
ordinary S-class group: trivial
S-unit squareclass columns: 207
sign/mod-4 image rank: 4
safe Kummer kernel dimension: 203
```

The ordinary prefixes therefore have `d=T-2`, not the genus screen's
optimistic `T+3`.  Full local rank persists under every larger prefix.

## 3. Exhaustive class/ray partition

Let `c(p)` be the image of a prime ideal in
`Cl(E)/2 Cl(E) = F_2^4`, and let `b(p)` be its image in the ray Frattini
quotient `B/2B = F_2^6`.  Every assignment lies in exactly one of the
following branches.

### 3.1 Proper ordinary-class span

If the selected ordinary colors span dimension `c<4`, the exact pre-local
S-unit squareclass dimension is

\[
 |T|+2+(4-c)=|T|+6-c.                               \tag{3.1}
\]

The verifier enumerates all 67 subspaces of `F_2^4`.  In each subspace and
for every `T` in (1.2), it takes the `T` smallest permitted ideals.  It then
grants the competitor the rank

\[
 d=|T|+5-c,                                          \tag{3.2}
\]

subtracting only one local condition even when the certified global-unit
rank is two.  It also declares every outside ideal useful and allows useful
roles to reuse the globally smallest ideals, including ideals already in
`T`.  Hence this is strictly more favorable than any actual construction.

The largest common endpoint margins are

\[
\begin{array}{c|rrrr}
D&c=0&c=1&c=2&c=3\\ \hline
963480&-148.99&-99.48&-56.16&-14.69\\
937365&-150.22&-106.34&-62.09&-16.01.
\end{array}                                           \tag{3.3}
\]

### 3.2 Full ordinary span but proper ray span

If the ordinary colors span all four dimensions, the pre-local dimension is
`T+2`.  A proper ray Frattini span then has dimension four or five.  The
verifier enumerates all

\[
 {6\brack4}_2=651,\qquad {6\brack5}_2=63             \tag{3.4}
\]

such ray subspaces, retaining only assignments with full ordinary span.
Rather than rely on a delicate exact formula involving the `C_4` or
`C_{12}` coordinate, it subtracts **only** the independently certified
global-unit local rank.  Thus it grants

\[
 d=|T| \quad(D=963480),qquad
 d=|T|+1 \quad(D=937365)                              \tag{3.5}
\]

in both the four- and five-dimensional ray branches, and ignores every
additional local obstruction.  Even under this relaxation, the largest
margins are

\[
\begin{array}{c|rr}
D&\dim\langle b(T)\rangle=4&\dim\langle b(T)\rangle=5\\ \hline
963480&-56.89&-15.39\\
937365&-54.74&-10.58.
\end{array}                                           \tag{3.6}
\]

### 3.3 Full ray span

If the selected ray colors span `B/2B`, the selected ideals generate the
entire finite ray group by the Frattini theorem.  Relations among their
ordinary ideal classes therefore realize the whole quotient of the four
local conditions by the global-unit image.  The sign/modulo-four image has
exact rank four, so

\[
 d=|T|-2.                                             \tag{3.7}
\]

No color restriction remains.  The all-depth role-exchange theorem puts the
smallest ideals in `T` and the first remaining ideals in the useful role.
The verifier rechecks the exceptional norms below nine at both endpoint
tangents.  The worst full-ray prefixes are

\[
\begin{array}{c|c|c|c|r}
D&T&d&\text{last norm in }T&\text{common margin}\\ \hline
963480&223&221&1187&-1.99918800\\
937365&223&221&1171&-2.06323591.
\end{array}                                           \tag{3.8}
\]

## 4. Endpoint rigor

Every comparison uses the favorable rational lower bound

\[
 {11978\over10863}< {2\sqrt3\over\pi}.               \tag{4.1}
\]

A smaller geometric constant lowers the endpoint right side and therefore
helps the rejected candidate.  At every one of the audited separators, both
endpoint margins are negative, the scale-one derivative is positive, and
the scale-two derivative is negative.  Piecewise-linear frontier concavity
and convexity of the subtracted log-sum-exp term then exclude every
continuous anchor.  The maximum omitted local slope is below both active
slopes, so all deeper local levels are inactive.

The margin increases with the proposed exponent.  Exclusion at
`0.49369313` therefore excludes every stronger exponent.

## 5. Scope

This is an exact finite no-go for both fields, arbitrary prime-ideal
assignment, all class/ray rank branches, and every `205<=T<=250` in the
all-square inertia/Frobenius presentation.  It does not rule out mixed
inertia orders, ramified counts outside this window, or a different pro-2
presentation.  Within the audited family, neither genus leader improves the
certified `D=821453` construction.
