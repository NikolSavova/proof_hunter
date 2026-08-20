# Global local-depth envelope at rank 715

## Result

This note strengthens the quadratic-Frobenius construction by globally
sorting its first three prime-power increments instead of forcing the coarse
schedule “all first increments, then all second increments.”  Together with
`proof_frobenius_order_two.md` and the non-uniform master inequality in
`proof_placewise_depths.md`, it proves

\[
  \boxed{F_2(n)\ll n^{0.494586}.}
\]

The finite certificate is
`verify_frobenius_all_depth_rank715.py`.

## 1. Arithmetic presentation

Let (T) be the first 716 odd rational primes.  Its positive odd quadratic
discriminant space has dimension 715, with the usual basis consisting of the
singleton primes (p\equiv1\pmod4\) and the products (3p) for
\(p\equiv3\pmod4\), (p\ne3).  Select the first 127,091 useful unramified
primes under the order-two Frobenius criterion.  Killing their Frobenius
squares gives

\[
 d=715,\qquad
 r\le715+127091=127806<\frac{715^2}{4}=127806.25.       \tag{1}
\]

Hence the quotient is infinite by Golod--Shafarevich.  Every selected prime
has residue degree at most two in the tower, and the root discriminants are
bounded by

\[
 D=\prod_{p\in T}p,
 \qquad
 \log D=5321.8375022300604190104720502471602772\ldots . \tag{2}
\]

The last ramified and useful primes are respectively 5,431 and 1,695,439.
The verifier checks the prime lists, the square-class rank, the useful-prime
criterion, and the strict integer inequality in (1).

## 2. The third local increment

For a selected rational prime (q), use the residue-degree-two lower gains

\[
 \Delta_q(k)=\frac12\log\left(
 \frac{(k+1)S_{k-1}(q^{-2})}{kS_k(q^{-2})}
 \right),
 \qquad S_k(t)=1+t+\cdots+t^k,                   \tag{3}
\]

for (k=1,2,3).  The cost of each increment is (log q).  Formula (3) is
also a valid lower bound when a prime has residue degree one.  The cases
(k=1,2) are proved in `proof_frobenius_order_two.md`.  For (k=3), put

\[
 A(t)=\frac{4(1+t+t^2)}{3(1+t+t^2+t^3)}.
\]

The required comparison is (A(t)^2\ge A(t^2)).  Direct expansion gives

\[
\begin{split}
 A(t)^2-A(t^2)
  ={}&\frac{4(1-t)^2}{9(1+t+t^2+t^3)^2
     (1+t^2+t^4+t^6)}\\
 &\mathrel{}\times
 (1+4t+11t^2+16t^3+20t^4+16t^5\\
 &\hspace{35mm}{}+11t^6+4t^7+t^8),
\end{split}                                      \tag{4}
\]

which is nonnegative for (0<t<1).  Taking logarithms of (4) proves the
residue-degree comparison.

Sort all (3\cdot127091) items by decreasing ratio
\(Delta_q(k)/\log q\).  The certificate verifies that every depth-(k)
item follows its depth-((k-1)) predecessor for the same prime.  Fractional
use of the final item is realized across the prime ideals above (q) by the
placewise rounding lemma.  Consequently the resulting cost--gain function
(F(L)) is increasing, concave, and available uniformly in the tower.

## 3. Dyadic phase certificate

Take

\[
  \alpha=0.494586,\qquad w_0=1040100.
\]

As in the earlier proofs, it suffices at scale (w) to have

\[
 F(2\alpha w)\ge
 \log(4D)+(2-4\alpha)w+
 \log\!\left(1+\frac{e^{2(2\alpha-1)w}}{4D}\right).       \tag{5}
\]

The difference between the two sides is concave in (w), so checking
(w_0) and (2w_0) certifies the entire dyadic phase interval.  After a
numerical allowance of (10^{-25}), the endpoint margins are

\[
  3.0585418857\ldots,qquad 3.3206766043\ldots .            \tag{6}
\]

At the left endpoint the path uses 80,361 first increments.  At the right
endpoint it uses all 127,091 first increments, 30,938 second increments, and
396 third increments, followed by a fractional item.  This is the small
interleaving missed by the two-stage rank-725 certificate.

For every sufficiently large (n), choose a degree-(2^j) layer with

\[
  w=\frac{\log n}{2[K:\mathbb Q]}\in[w_0,2w_0).
\]

Concavity, (5), and the placewise rounding lemma give

\[
  |A|\le(1+\sqrt2)n^{0.494586}
\]

for every distance-Sidon subset of the constructed (n)-point planar set.
The finite initial range is absorbed into the implied constant.

## 4. Scope

This is a further explicit upper-bound improvement, not a resolution of the
order of magnitude.  `RANK715_ARITHMETIC_INPUT_AUDIT.md` maps the tame
totally-real presentation theorem to this quotient, proves the existence of
Galois layers of every sufficiently large dyadic degree with kernels inside
the Frattini subgroup, and checks the residue-degree interface with the
symbolic master inequality.  Integer arithmetic in the verifier is exact;
logarithms and exponentials are evaluated with 80-digit `Decimal` arithmetic.
The smallest endpoint margin exceeds three, far above the stated numerical
allowance.
