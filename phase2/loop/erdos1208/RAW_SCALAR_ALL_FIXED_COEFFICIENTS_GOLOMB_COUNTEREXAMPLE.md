# Dense Golomb rulers kill every fixed positive scalar coefficient

## 1. Verdict

Changing the coefficient from `C=18` to `C=3` does not salvage the metric
scalar charge.  In fact, for **every fixed positive integer `C`**, there
are polynomial-height integral distance-Sidon sets for which

\[
 \boxed{
 \sum_q\bigl(\mathcal M_{q,C}-N|H_q|\bigr)
 =\Omega_C(k^6\sqrt{\log k}),}                 \tag{1.1}
\]

whereas the proposed master bound is

\[
 m^{o(1)}Nk^3=k^{5+o(1)}.                       \tag{1.2}
\]

The counterexample is just a dense collinear Golomb ruler.  No planted
copy or norm-ratio swap is needed.

For `C=3`, the hoped-for anisotropic observation is correct but points in
the wrong direction: `|v|^2=3|w|^2` has no nonzero integral solutions.
Nevertheless the values `x^2+3y^2` occupy only
`O(X/sqrt(log X))` integers up to `X`.  The resulting global compression,
combined with the `Omega(k^6)` clean-fibre second moment of a dense Golomb
ruler, forces (1.1).

Thus all fixed-`C` versions of `METRIC_SCALAR_PAIR_SUM_CHARGE` and every
tail, determinant, endpoint, or common-translation gate derived from those
scalar master bounds are superseded.  This does **not** disprove Erdos
Problem 1208; it disproves this proof architecture.

## 2. The norm-value support theorem

For fixed `C>=1`, put

\[
 V_C(X)=\#\{n\le X:n=x^2+Cy^2
                    \text{ for some }x,y\in\mathbb Z\}. \tag{2.1}
\]

The classical Bernays theorem for primitive positive definite binary
quadratic forms gives

\[
 \boxed{V_C(X)=O_C\left({X\over\sqrt{\log X}}\right).}   \tag{2.2}
\]

More precisely, Bernays proved an asymptotic constant times
`X/sqrt(log X)` for integers represented by a fixed primitive positive
definite binary quadratic form.  Applied to `[1,0,C]`, this gives (2.2).
The original reference is P. Bernays, *Uber die Darstellung von positiven,
ganzen Zahlen durch die primitiven binaren quadratischen Formen einer
nicht-quadratischen Diskriminante*, Gottingen dissertation, 1912.  Only the
upper bound in (2.2) is used here.

### Elementary arithmetic mechanism for `C=3`

If a prime `p congruent 2 (mod 3)` divides `x^2+3y^2`, then `p` occurs to
even exponent.  For odd `p`, `-3` is a quadratic nonresidue modulo such a
prime.  Hence divisibility by `p` forces `p|x` and `p|y`, and division by
`p^2` iterates.  For `p=2`, equal parity gives the same even-valuation
conclusion directly modulo eight.

Therefore every represented integer lies in

\[
 \mathcal S_3=
 \{n:v_p(n)\text{ is even for every }p\equiv2\pmod3\}.  \tag{2.3}
\]

The Dirichlet series of this multiplicative set is

\[
 \sum_{n\in\mathcal S_3}n^{-s}
 =\prod_{p=3\text{ or }p\equiv1(3)}(1-p^{-s})^{-1}
  \prod_{p\equiv2(3)}(1-p^{-2s})^{-1}.           \tag{2.4}
\]

The primes `p congruent 2 (mod 3)` have Dirichlet density `1/2`.
The standard Landau/Selberg--Delange estimate for (2.4), equivalently the
elementary half-dimensional sieve, gives

\[
 |\mathcal S_3\cap[1,X]|=O(X/\sqrt{\log X}),      \tag{2.5}
\]

which proves (2.2) for `C=3` without invoking the full Bernays theorem.
The statement `|v|^2=3|w|^2` is the special case that the 3-adic valuation
of a sum of two squares is even, so the two sides cannot differ by one.

For general fixed `C`, inert primes in the imaginary quadratic field
attached to the squarefree part of `-C` give the same density-`1/2`
obstruction.  Bernays packages this uniformly, including square factors
and the finitely many ramified primes.

## 3. Dense Golomb clean core

Take a dense integer Golomb ruler

\[
 B_k\subset[0,L],\qquad |B_k|=k,qquad L=O(k^2), \tag{3.1}
\]

and put

\[
 A_k=\{(b,0):b\in B_k\}.                        \tag{3.2}
\]

This is an integral distance-Sidon set in a square of side

\[
 m=O(k^2).                                       \tag{3.3}
\]

Let `h_q=|H_q|` be its literal six-distinct clean fibres and
`H=sum_q h_q`.  The standard dense-Golomb triple-sum argument gives

\[
 H=\Omega(k^4).                                  \tag{3.4}
\]

Indeed, there are `Theta(k^3)` unordered triples but only `O(k^2)`
possible triple sums.  Cauchy gives `Omega(k^4)` distinct equal-sum pairs.
Two different triples with equal sum are disjoint, since cancelling a
common mark would contradict pair-sum uniqueness.  Distinguishing endpoints
therefore gives literal clean starts.

There are at most `k(k-1)` nonzero directed differences `q`.  Hence

\[
 \boxed{
 \sum_qh_q^2\ge {H^2\over k(k-1)}=\Omega(k^6).}  \tag{3.5}
\]

## 4. Scalar compression on every fibre

Every canonical edge label of (3.2) is `x^2` for an integer
`1<=x<=L`.  For a fixed fibre, the charge

\[
 \Phi_{q,C}(s,t)=\delta(s)+C\delta(t)             \tag{4.1}
\]

therefore has values of the form

\[
 x^2+Cy^2\le(1+C)L^2=O_C(k^4).                  \tag{4.2}
\]

By (2.2), the total number of possible charge values, even before
restricting `x,y` to ruler differences, is at most

\[
 O_C\left({k^4\over\sqrt{\log k}}\right).        \tag{4.3}
\]

The fibre supplies `h_qN` records.  Cauchy--Schwarz and (4.3) give

\[
 \boxed{
 \mathcal M_{q,C}
 \ge c_C h_q^2\sqrt{\log k}}                    \tag{4.4}
\]

for an absolute positive `c_C` depending only on the fixed coefficient.
Summing (4.4) and using (3.5),

\[
 \sum_q\mathcal M_{q,C}
 \ge\Omega_C(k^6\sqrt{\log k}).                 \tag{4.5}
\]

The exact identical-record diagonal is `NH`.  Since `N=Theta(k^2)`,
`H<=k(k-1)N=O(k^4)`, and therefore

\[
 NH=O(k^6).                                      \tag{4.6}
\]

The square-root logarithm in (4.5) dominates (4.6), proving (1.1).
Finally, (3.3) gives `m^(o(1))=k^(o(1))`, while

\[
 Nk^3=\Theta(k^5).                               \tag{4.7}
\]

Thus the violation is a full factor `k^(1-o(1))` (and in fact has an
additional `sqrt(log k)` in this lower bound).

## 5. Exact `C=3` profiles

The verifier computes the original raw aggregate exactly on Ruzsa rulers
scaled by six.  Scaling does not change scalar collisions; it makes every
source squared-gap divisible by three.

\[
\begin{array}{c|r|r|r|r|c}
p&k&H&\sum_qh_q^2&\sum_q\mathcal X_q&
 (\sum_q\mathcal X_q)/(Nk^3)\\ \hline
31&30&82,746&8,233,370&10,564,022&0.899448\\
59&58&1,251,486&496,787,794&666,321,296&2.065984\\
83&82&5,263,452&4,373,119,600&6,432,929,994&3.513164.
\end{array}                                             \tag{5.1}
\]

The ratios grow rather than stabilize.  This is the finite signature of
the asymptotic support-compression proof, and explains why smaller closure,
Costas, parabola, and sparse-ruler stresses did not expose the failure.
Those families do not simultaneously have dense-Golomb clean second moment
and dense one-dimensional norm support.

The verifier also checks the inert-prime even-valuation condition on every
sampled value `x^2+3y^2<=10,000`.

Run

```text
PYTHONPATH=phase2/loop/erdos1208 \
python3 phase2/loop/erdos1208/verify_raw_scalar_all_coefficients_golomb_counterexample.py
```

## 6. Consequence

The following are now invalid as universal master targets for every fixed
positive coefficient `C`:

\[
 \mathcal M_{q,C}\le m^{o(1)}N(h_q+k)
 \quad\text{after aggregate summation},          \tag{6.1}
\]

and

\[
 \sum_q(\mathcal M_{q,C}-Nh_q)
 \le m^{o(1)}Nk^3.                               \tag{6.2}
\]

The proof does not necessarily refute every pointwise form of (6.1): the
counterexample is powered by the sum of the clean-fibre second moments.
It decisively refutes the aggregate statement actually needed for the
cube-root deduction.

A coefficient depending polynomially on `k` is outside this theorem, but
would enlarge the charge range and invalidate the fixed-box constants in
the original reduction.  No fixed anisotropic coefficient avoids the
dense-Golomb norm-value compression.
