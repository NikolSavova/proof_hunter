# Rank-aware no-go for the quadratic-880440 genus candidate

## 1. Verdict

The five-dimensional genus bonus granted by the discovery screen does not
survive the norm-prefix localization.  More importantly, restricting a
non-prefix ramified set to preserve some of the genus classes is also too
expensive.  For

\[
 E=\mathbb Q(\sqrt{220110}),\qquad \operatorname {Disc}(E)=880440,
                                                               \tag{1.1}
\]

the companion verifier rigorously excludes every all-square configuration
with

\[
 205\le |T|\le250                                      \tag{1.2}
\]

at the current exponent `0.49369313`, including every non-prefix assignment
classified by its ordinary-class and sign/mod-4 ray colors.

```text
python3 phase2/loop/erdos1208/verify_genus_bonus_880440_rank_aware_no_go.py
```

The conclusion is a no-go for the finite candidate family (1.2), not a
claim about every possible presentation over this field.

## 2. What the genus screen counted

The exact factorization is

\[
 880440=2^3\cdot3\cdot5\cdot11\cdot23\cdot29.         \tag{2.1}
\]

A certified PARI BNF gives

\[
 \operatorname {Cl}(E)\simeq(C_2)^4,qquad
 \operatorname {Cl}^+(E)\simeq(C_2)^5.               \tag{2.2}
\]

Thus the secondary screen's five-dimensional optimistic grant has a real
genus-theoretic source.  But the fifth narrow class is the failure of the
unit signature map: the fundamental unit has norm `+1`.  It is not an
additional ordinary unramified finite Kummer class after positivity has
already been imposed.

For the first 205 odd prime ideals, PARI computes

```text
ordinary S-class group: trivial
S-unit squareclass columns: 207
sign/mod-4 image rank: 4
positive dyadically-unramified kernel dimension: 203
```

Triviality persists under enlarging `S`.  Hence every ordinary norm prefix
in (1.2) has

\[
 d=(|T|+2)-4=|T|-2,                                   \tag{2.3}
\]

not the screened value `|T|+3`.  At the nominated `|T|=216`, for example,
the exact rank is 214 rather than 219.

The same selected-prefix audit was run on the other four leading genus
nominees.  In every case the first 205 ideals already have trivial
ordinary `S`-class group and sign/mod-4 image rank four:

\[
\begin{array}{c|c|c|c}
D&\operatorname {Cl}(E)&\operatorname {Cl}^+(E)&d(205)\\ \hline
963480&C_4\times(C_2)^3&C_4\times(C_2)^4&203\\
937365&(C_2)^4&(C_2)^5&203\\
871080&C_6\times(C_2)^3&C_6\times(C_2)^4&203\\
552552&(C_2)^4&(C_2)^5&203
\end{array}                                           \tag{2.4}
\]

Equation (2.4) is a prefix warning, not the full non-prefix exclusion proved
below only for `D=880440`.

## 3. Ordinary class-color localization

Let `c(p)` be the image of an odd prime ideal in
`Cl(E)/2Cl(E)=F_2^4`.  If the selected colors span a subspace of dimension
`c`, then

\[
 \dim \operatorname {Cl}_S(E)[2]=4-c.                \tag{3.1}
\]

Before the sign/dyadic conditions, the `S`-Kummer squareclass dimension is

\[
 |T|+2+(4-c)=|T|+6-c.                                \tag{3.2}
\]

There are exactly 67 subspaces of `F_2^4`.  For each proper subspace and
each `205<=|T|<=250`, the verifier selects the `|T|` smallest allowed prime
ideals and compares their product exactly.  To make the exclusion strictly
favorable to the competitor, it then:

1. charges only one local condition, using
   \(d=|T|+5-c\), although the two unit columns already have local rank two;
2. declares every outside prime useful; and
3. lets the useful roles reuse the globally smallest ideals, including the
   ideals already used in `T`.

Even this relaxation fails.  At the all-anchor separators, the largest
common endpoint margins in class dimensions `0,1,2,3` are respectively at
most

```text
-152.72, -102.76, -56.29, -14.24.
```

Thus no proper ordinary-class subspace can preserve enough genus rank to
compete.

## 4. Full class span but reduced local-ray span

The remaining subtlety is a set whose ordinary colors span all four class
dimensions but whose sign/mod-4 obstruction has lower rank.

PARI gives the exact ray group for modulus `(4 O_E; both real places)`:

\[
 B\simeq C_4\times(C_2)^5,qquad B/2B\simeq F_2^6.    \tag{4.1}
\]

Write `b(p)` for the six-bit ray color.  For a set whose ordinary colors
span all of `F_2^4`, the `S`-class group is trivial.  The image of the
valuation-relation space in the two-dimensional local quotient has rank

\[
 q=\operatorname {rank}\langle b(\mathfrak p):
       \mathfrak p\in T\rangle-4.                    \tag{4.2}
\]

The two unit columns have exact local rank two, so

\[
 d=|T|-q.                                             \tag{4.3}
\]

Reducing `q` from its generic value two forces all ray colors into a
four- or five-dimensional subspace of `F_2^6`.  There are exactly

\[
 {6\brack4}_2=651,qquad {6\brack5}_2=63              \tag{4.4}
\]

such subspaces.  The verifier enumerates all 714, retains only those whose
ordinary projection has rank four, and again uses the independently
minimized ramified product together with globally reusable useful ideals.
Across the full interval (1.2), the largest common endpoint margins are

```text
ray rank 4:  -59.30
ray rank 5:  -17.43.
```

Hence every rank-reducing full-class non-prefix assignment is excluded.

## 5. Generic full ray rank and the small-prime exchange

If the selected ray colors span all six dimensions, (4.3) gives
`d=|T|-2`.  No color restriction remains.  The usual all-depth assignment
dual then puts the smallest ideals in `T` and the first remaining ideals in
the useful role.

There is one point not covered verbatim by the earlier `D=43133` exchange
proof: this field has prime-ideal norms `3,5,7`, whereas the convenient
uniform useful-value estimate began at norm nine.  At each of the 92 exact
endpoint tangents (two endpoints for every `|T|`), the verifier checks

\[
 V_\lambda(3)>V_\lambda(5)>V_\lambda(7)>V_\lambda(9) \tag{5.1}
\]

and

\[
 {\rho\log3\over4}+V_\lambda(3)
 <{\rho\log5\over4}+V_\lambda(5)
 <{\rho\log7\over4}+V_\lambda(7)
 <{\rho\log9\over4}+V_\lambda(9).                   \tag{5.2}
\]

It also checks `rho>1/log 3`.  For `Q>=9`, the exact rational inequality
from the all-depth exchange theorem proves that `V_lambda(Q)` decreases,
while

\[
 {\rho\log Q\over4}+V_\lambda(Q)
\]

increases.  Thus (5.1)--(5.2) bridge the only exceptional norms and certify
the prefix assignment globally.

Using the favorable rational lower bound

\[
 {11978\over10863}< {2\sqrt3\over\pi},                \tag{5.3}
\]

the worst common endpoint margin over all 46 prefix configurations is

```text
-1.6761378026886...
```

Smaller geometric constant means a smaller endpoint right side, so (5.3)
is favorable to the rejected construction.

For every cell above, the verifier chooses a separator where the two
endpoint margins agree, checks that both are negative, and verifies positive
left derivative and negative right derivative.  Concavity then excludes
every anchor.  The endpoint margin increases with the proposed exponent,
so exclusion at `0.49369313` also excludes every stronger exponent.

## 6. Scope

The result kills the exact leading genus candidate throughout the dense
`205..250` all-square window, with arbitrary prime-ideal reassignment and
all class/ray rank changes retained.  It also explains why the four nearby
genus leaders fail on their norm prefixes.  It does not exclude mixed
inertia orders, a ramified count outside the tested interval, or a different
pro-2 presentation.

