# Frobenius fourth powers and mixed-depth Golod--Shafarevich budgets

## 1. Pure fourth-power quotient

In a pro-2 group, a relator (g^4) has Zassenhaus degree at least four.
Starting from a tame presentation with generator rank (d) and at most (d)
quadratic relations, (N) Frobenius fourth-power relations are certified by

\[
  1-dt+dt^2+Nt^4<0.                              \tag{1}
\]

The exact continuous capacity is obtained at

\[
  t_d=\frac{3-\sqrt{9-32/d}}4,
\]

and is asymptotic to

\[
  N_{4,\max}\sim\frac{27}{256}d^4.
\]

In the resulting quotient the selected Frobenius elements have order at most
four.  For (q\equiv3\pmod4), retaining a nonzero Frattini class guarantees
that the order is even, so (-1) is a square in the residue field.  The worst
residue degree is four.  A depth-one prime therefore contributes

\[
  \frac14\log\frac{2}{1+q^{-4}}
\]

per absolute field degree, and the second increment contributes

\[
  \frac14\log
  \frac{3(1+q^{-4})}{2(1+q^{-4}+q^{-8})}.
\]

An exact-prime exploratory sweep gives:

| rank `d` | fourth-power relators | last prime | continuous exponent | dyadic exponent |
|---:|---:|---:|---:|---:|
| 8 | 177 | 1,117 | 0.49705 | 0.49827 |
| 10 | 543 | 4,019 | 0.49590 | 0.49614 |
| 12 | 1,289 | 10,687 | 0.49562 | 0.49583 |
| 15 | 3,555 | 33,349 | 0.49574 | 0.49576 |
| 20 | 12,578 | 135,277 | 0.49592 | 0.49594 |
| 40 | 234,806 | 3,268,901 | 0.49629 | 0.49631 |
| 60 | 1,247,184 | 19,608,467 | 0.49648 | 0.49650 |

The best sampled point is already weaker than the square-Frobenius result
`0.4947`.  The fourth-degree relation budget does not compensate for the
factor-two residue-degree loss and the larger useful primes.

## 2. The apparent free fourth-power block at rank 400

There is a striking integer slack in the certified rank-400 square quotient.
With

\[
  N_2=39599,\qquad t=\frac2{400},
\]

one may add

\[
  N_4=39999
\]

fourth-power relations and still have

\[
  1-400t+(400+N_2)t^2+N_4t^4<0.                 \tag{2}
\]

Numerically the left side is (-6.25\cdot10^{-10}).  Thus the existing
39,599 residue-degree-two primes can be retained and the next 39,999 primes
can simultaneously be forced to residue degree at most four.

This does **not** improve the dyadic certificate.  When all local increments
are sorted by gain per `log q` cost, every second-depth increment at the
square-constrained primes comes before the first-depth increment at any of
the new fourth-power primes:

\[
  \frac{\frac12\log(3/2)}{\log q_{N_2}}
  >
  \frac{\frac14\log2}{\log q_{N_2+1}}.
\]

The tight dyadic interval for the current theorem uses all first increments
and only about 18,000 of the second square-prime increments.  It never reaches
the new fourth-power block.  Recomputing the full concave envelope gives the
same dyadic threshold, approximately

\[
  0.4946539833.
\]

The continuous one-scale threshold is approximately `0.49428526`, but this
was already available before the fourth-power block becomes active; it cannot
cover all (n) because the degrees remain dyadic.

## 3. Verdict

Fourth-power Frobenius relations are valid and give an enormous formal
relation budget, but their local increments lie below the portion of the
square-prime concave envelope that controls the theorem.  Pure and hybrid
versions both lose.  Higher powers (g^{2^a}) worsen the entropy-to-log-cost
ratio further: the relation budget grows like (d^{2^a}), but the residue
degree and the logarithm of the last useful prime each acquire a factor
(2^a).
