# An explicit quantitative upper bound for Erdős 1208

## 1. Candidate theorem

Let \(F_2(n)\) have the meaning in `PROBLEM.md`.  The argument below proves,
subject only to the standard Golod--Shafarevich tower input isolated in
Section 5,

\[
  F_2(n)\ll n^{0.49815}.
\]

The new ingredient relative to Lee's draft and Lee--Pohoata--Zhu is a
prime-power amplification lemma.  All logarithms in the optimization are
natural.

## 2. Prime-power isotropic patterns

Let \(F\) be a totally real number field of degree \(m\).  Suppose that a
rational prime \(q\equiv1\pmod4\) splits completely:

\[
 q\mathcal O_F=\prod_{j=1}^m\mathfrak q_j,
 \qquad N\mathfrak q_j=q.
\]

Fix \(K\ge1\).  Hensel lifting gives an integer \(x\) with
\(x^2\equiv-1\pmod {q^{2K}}\).  For each \(a\in\{0,\ldots,K\}\) and each
\(\mathfrak q_j\), impose

\[
 u-xv\in\mathfrak q_j^a,
 \qquad u+xv\in\mathfrak q_j^{K-a}.                 \tag{2.1}
\]

Because the determinant \(2x\) is a \(\mathfrak q_j\)-adic unit, (2.1)
defines an additive subgroup of local index \(q^K\).  Thus each global choice
of the \((K+1)^m\) patterns has index \(q^{Km}\) in \(\mathcal O_F^2\).

For a fixed \((u,v)\), put

\[
 \alpha=\min(v_{\mathfrak q_j}(u-xv),K),\qquad
 \beta =\min(v_{\mathfrak q_j}(u+xv),K).
\]

The allowed values of \(a\) are the integers in
\([K-\beta,\alpha]\).  If there are any, their number is \(h+1\), where
\(h=\alpha+\beta-K\in\{0,\ldots,K\}\).  Moreover

\[
 (u-xv)(u+xv)\in\mathfrak q_j^{K+h}.
\]

The difference between this product and \(u^2+v^2\) is
\((x^2+1)v^2\in\mathfrak q_j^{2K}\).  Since \(K+h\le2K\),

\[
 u^2+v^2\in\mathfrak q_j^{K+h}.                    \tag{2.2}
\]

Hence the local multiplicity \(h+1\) is paid for by the \(h+1\) extra ideal
divisors \(1,\mathfrak q_j,\ldots,\mathfrak q_j^h\) in (2.2).  This is the
prime-power replacement for the two-sign/square-divisor observation in the
squarefree sieve.

For distinct completely split primes \(q_i\), choose the corresponding
Hensel roots \(x_i\), and let the depths be \(K_i\).  Define

\[
 M=\prod_iq_i^{K_i},\quad
 H=\prod_i(K_i+1),\quad
 \Lambda=\prod_i(1+q_i^{-1}+\cdots+q_i^{-K_i}).     \tag{2.3}
\]

## 3. Global sieve inequality

Let \(B\subset\mathcal O_F\) lie in a translate of a Minkowski box of side
\(R\), and let \(A\subset B^2\) be distance-Sidon after projection through one
real embedding.  Every difference has all conjugates bounded by \(R\).

Let \(T\) count triples consisting of an ordered distinct pair from \(A\) and
a global valuation pattern for which the pair difference lies in the
corresponding subgroup.  Summing same-coset pairs over the \(H^m\) patterns
and using Cauchy--Schwarz gives

\[
 H^m\frac{|A|(|A|-M^m)}{M^m}\le T.                \tag{3.1}
\]

For a nonzero algebraic squared distance \(\eta\), the distance-Sidon
condition permits at most two ordered pairs mapping to \(\eta\).  The local
calculation in Section 2 and divisor switching therefore give

\[
 T\le 2\sum_{\mathfrak b\mid M}
 \#\{\eta\in M\mathfrak b:
       |\sigma_j(\eta)|\le2R^2\ (1\le j\le m)\}.   \tag{3.2}
\]

Here \(\mathfrak b\mid M\mathcal O_F\) means an ideal whose exponent at every
prime ideal \(\mathfrak q_{i,j}\) is chosen independently between \(0\) and
\(K_i\), and whose other exponents vanish.  For a fixed pair, the product of
the local pattern multiplicities equals the number of such \(\mathfrak b\)
for which \(M\mathfrak b\mid\eta\); this justifies the divisor switch in
(3.2).  If \(\mathfrak a\) is an integral ideal, the sup-norm packing lemma
gives

\[
 \#\{\eta\in\mathfrak a:|\sigma_j(\eta)|\le Y\}
 \le\left(1+\frac{2Y}{(N\mathfrak a)^{1/m}}\right)^m.       \tag{3.3}
\]

Assume \(R\ge M\).  Since
\((N(M\mathfrak b))^{1/m}=M(N\mathfrak b)^{1/m}\) and
\((N\mathfrak b)^{1/m}\le M\), equations (3.2)--(3.3) yield

\[
 T\le2\left[
   \frac{R^2\Lambda}{M}
   \left(4+\frac{M^2}{R^2}\right)
 \right]^m.                                         \tag{3.4}
\]

Indeed,
\(\sum_{\mathfrak b\mid M}(N\mathfrak b)^{-1}=\Lambda^m\).
Comparing (3.1) and (3.4), and using
\((|A|-M^m)^2\le |A|(|A|-M^m)\) when \(|A|\ge M^m\), proves the master bound

\[
 \boxed{
 |A|\le M^m+\sqrt2R^m
 \left[\frac{\Lambda}{H}
 \left(4+\frac{M^2}{R^2}\right)\right]^{m/2}.}      \tag{3.5}
\]

Total reality is used here to ensure that \(u^2+v^2=0\) only when
\(u=v=0\).  Injectivity of a real embedding makes equality of the algebraic
squared distances equivalent to equality of their projected Euclidean
squared distances.

## 4. Exponent optimization

Suppose an infinite tower supplies degrees \(m=2^j\), root discriminant at
most \(D\), and all primes in (2.3) split completely.  Averaging a translated
Minkowski box gives

\[
 |B|\ge(R/\sqrt D)^m.
\]

For a prescribed \(n\), take
\(R=\sqrt D\,n^{1/(2m)}\); then \(|B^2|\ge n\), so an arbitrary \(n\)-point
subset is available.

Put \(L=\log M\).  Provided \(H>\Lambda(4D+1)\), define

\[
 y=\frac{-1+\sqrt{1+16DH/\Lambda}}{8D}>1,
 \qquad r=\log y,
 \qquad a=L+r/2.                                    \tag{4.1}
\]

The number \(y\) is the positive solution of
\(4Dy^2+y=H/\Lambda\).  Choose the unique dyadic \(m\) satisfying

\[
 \frac{\log n}{4a}<m\le\frac{\log n}{2a}.           \tag{4.2}
\]

For large \(n\), (4.2) also makes \(R\ge M\).  The first term in (3.5) is at
most \(n^{L/(2a)}\).  Since
\(\log n/(2m)\ge a\), (4.1) implies

\[
 \frac{D\Lambda}{H}\left(4+\frac{M^2}{R^2}\right)
 \le y^{-2}.
\]

The second term of (3.5) is therefore at most a constant times
\(n^{1/2}e^{-rm}\), which by (4.2) is at most
\(n^{1/2-r/(4a)}\).  The two exponents are equal, giving

\[
 F_2(n)\ll n^{1/2-\varepsilon},
 \qquad
 \boxed{\varepsilon=\frac{r}{4L+2r}}.               \tag{4.3}
\]

## 5. Explicit tower certificate

Take

\[
 \mathcal T=\{3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61\}.
\]

Since \(\mathcal T\) contains primes congruent to \(3\pmod4\), the standard
generator-rank formula for the maximal totally real pro-2 extension unramified
outside \(\mathcal T\) gives \(d=|\mathcal T|-1=16\).  Its Frattini field is
the maximal totally real elementary \(2\)-extension unramified outside
\(\mathcal T\).  One basis of its square classes is

\[
 5,13,17,29,37,41,53,61,21,33,57,69,93,129,141,177. \tag{5.1}
\]

Every radicand in (5.1) is positive, squarefree and \(1\pmod4\), and their
prime-incidence vectors have rank 16 over \(\mathbb F_2\).  Their compositum is
therefore exactly the Frattini field.  The 47 primes recorded in
`verify_explicit.py` are \(1\pmod4\) and every number in (5.1) is a quadratic
residue modulo each of them.  Thus all 47 split in the Frattini field and in
\(\mathbb Q(i)\).  Adding relations that kill their Frobenius elements leaves
the generator rank 16 and gives relation rank at most

\[
 16+47=63<16^2/4=64.
\]

The strict Golod--Shafarevich inequality therefore supplies an infinite
totally real pro-2 extension, ramified only at \(\mathcal T\), in which these
47 primes split completely.  Since all ramification is tame, its finite
layers have root discriminant at most

\[
 D=\prod_{p\in\mathcal T}p=58644190679703485491635. \tag{5.2}
\]

An index-2 filtration supplies layers of every degree \(2^j\), as required in
Section 4.

Assign depths \(9,8\), then depth 7 to the next 15 primes, and depth 6 to the
remaining 30.  The verifier recomputes

\[
 \begin{aligned}
 \log H&=94.0687372671872,\\
 \Lambda&=1.00000216058184,\\
 \log M&=5427.60766338395,\\
 r&=20.1283326365318,\\
 \varepsilon&=0.000925411337191441.
 \end{aligned}
\]

Since \(1/2-\varepsilon=0.4990745886\ldots<0.4991\), (4.3) first gives the
intermediate safe exponent \(0.4991\).  Sections 7--8 improve it by adapting
the modulus to the dyadic phase and enlarging the tower.  This intermediate
claim does not depend on trusting the last decimals:
\(r>20\) and \(L<5428\) imply

\[
 \varepsilon>\frac{20}{4\cdot5428+40}>0.0009.
\]

## 6. Verification and honest status

Run

```bash
python3 phase2/loop/erdos1208/verify_explicit.py
```

It deterministically checks primality, all \(47\times16\) Legendre symbols,
the square-class rank, the Golod--Shafarevich rank inequality, (5.2), and the
numerical optimization.

What it does not machine-check is the standard class-tower relation-rank
input or the symbolic proof in Sections 2--4.  These require independent
mathematical refereeing.  As of 2026-08-13, targeted searches found no prior
prime-power version of this sieve.  Until expert review and a broader
MathSciNet search, the correct label is **apparently new candidate partial
result**, not established novelty.

## 7. Adaptive moduli remove most of the dyadic loss

Section 4 uses one fixed depth vector for every \(n\).  This is unnecessarily
restrictive: the point set witnessing the upper bound may depend on \(n\), so
the depths \(K_i\), and hence \(M,H,\Lambda\), may also depend on \(n\).

Put

\[
 w=\frac{\log n}{2m},\qquad L=\log M,
 \qquad z(w)=\frac{e^{2(L-w)}}D.
\]

Thus \(R=\sqrt D e^w\), and \(z=M^2/R^2\).  The two terms in the master bound
(3.5), apart from their absolute coefficients, have exponents

\[
 E_1(w)=\frac{L}{2w},                               \tag{7.1}
\]

and

\[
 E_2(w)=\frac12+\frac{C(w)}{4w},\qquad
 C(w)=\log\frac{D\Lambda}{H}+\log(4+z(w)).          \tag{7.2}
\]

Take \(\alpha=0.49826\).  The certificate `verify_adaptive.py` lists 23
depth vectors and a closed interval for each one.  For a row ([a,b]), it
checks

\[
 \frac L{2a}<\alpha,                                \tag{7.3}
\]

and

\[
 C(b)<(4\alpha-2)b.                                 \tag{7.4}
\]

The first exponent is decreasing, so (7.3) controls \(E_1\) throughout the
row.  For the second, differentiation gives

\[
 \frac{d}{dw}\bigl(C(w)-(4\alpha-2)w\bigr)
 =2-4\alpha-\frac{2z(w)}{4+z(w)}.                  \tag{7.5}
\]

The verifier checks \(z(a)/2<2-4\alpha\).  Since \(z\) is decreasing and
\(2z/(4+z)<z/2\), (7.5) is positive on the row.  Hence (7.4) controls
\(E_2\) throughout it.  The same check gives \(z(a)<1\), so \(R\ge M\), as
required by (3.5).

The 23 certified intervals overlap and cover

\[
 [4024.0,8054.7]\supset[4024.0,8048.0].            \tag{7.6}
\]

For every sufficiently large \(n\), choose a dyadic tower degree \(m=2^j\)
so that

\[
 w=\frac{\log n}{2m}\in[4024.0,8048.0).
\]

This is possible because consecutive degrees double, and therefore
consecutive values of \(w\) halve.  Select the depth vector whose certified
interval contains \(w\).  Equations (3.5) and (7.1)--(7.6) give

\[
 |A|\le n^\alpha+\sqrt2n^\alpha
       =(1+\sqrt2)n^{0.49826}.
\]

The averaging construction supplies at least \(n\) ambient points exactly as
in Section 4.  Enlarging the implied constant handles bounded \(n\), proving

\[
 \boxed{F_2(n)\ll n^{0.49826}.}                   \tag{7.7}
\]

The adaptive calculation is a finite explicit certificate, not a heuristic
optimization.  The smallest first-exponent margin exceeds
\(1.7\cdot10^{-7}\), and the smallest transformed second-exponent margin
exceeds \(2.5\cdot10^{-5}\), far above the 80-digit decimal rounding scale
used by the verifier.

## 8. A stronger rank-17 tower certificate

The rank-16 tower above is a useful independent fallback, but it is not the
best explicit choice.  Enlarge the ramification set to

\[
 \mathcal T_{17}=\{3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67\}.
                                                               \tag{8.1}
\]

The corresponding totally real Frattini square classes have the independent
basis

\[
 5,13,17,29,37,41,53,61,
 21,33,57,69,93,129,141,177,201,                 \tag{8.2}
\]

of rank 17 over \(\mathbb F_2\).  The exact verifier
`verify_adaptive_rank17.py` lists 55 rational primes \(q\equiv1\pmod4\)
and checks that every member of (8.2) is a quadratic residue modulo every
one.  Hence these primes split in the Frattini field and in
\(\mathbb Q(i)\).  Killing their Frobenius elements gives the presentation
bound

\[
 d=17,\qquad r\le17+55=72,qquad 4r\le288<289=d^2. \tag{8.3}
\]

The same strict Golod--Shafarevich argument used in Section 5 therefore
supplies an infinite totally real pro-2 tower, with all 55 primes splitting
completely and with root discriminant bounded by

\[
 D_{17}=\prod_{p\in\mathcal T_{17}}p
 =3929160775540133527939545.                       \tag{8.4}
\]

Apply the prime-power lemma and master bound (3.5) to this tower.  With

\[
 \alpha=0.49815,
\]

the verifier gives 27 fixed depth vectors and overlapping safe intervals
covering

\[
 [4365.9,8780.9]\supset[4365.9,8731.8].           \tag{8.5}
\]

For each interval it performs exactly the endpoint and monotonicity checks
(7.3)--(7.5), now using \(D_{17}\) and the 55-prime values of
\(M,H,\Lambda\).  Given sufficiently large \(n\), choose a dyadic degree
\(m\) with

\[
 \frac{\log n}{2m}\in[4365.9,8731.8)
\]

and use the row containing this phase.  The master bound gives

\[
 |A|\le(1+\sqrt2)n^{0.49815}.
\]

Thus the stronger explicit conclusion is

\[
 \boxed{F_2(n)\ll n^{0.49815}.}                   \tag{8.6}
\]

The finite certificate checks primality of all ramified and split primes,
935 Legendre symbols, the square-class rank, (8.3), (8.4), all interval
overlaps, \(R\ge M\), and both exponent inequalities at 80 decimal digits.
The smallest two endpoint margins exceed \(5.5\cdot10^{-7}\) and
\(4.2\cdot10^{-5}\), respectively.  Repeating the calculation at 150 digits
gives the same signs.  As with the rank-16 version, the class-tower theorem
and the symbolic proof of (3.5) remain mathematical rather than formalized
inputs.
