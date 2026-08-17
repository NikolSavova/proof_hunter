# Odd-degree phase filling for the pro-2 tower

## The mechanism

The quadratic-Frobenius construction supplies fields of degree (2^j).
This dyadic spacing is a genuine loss: for a prescribed (n), the scale

\[
  w=\frac{\log n}{2[K:\mathbb Q]}
\]

can move through an interval of multiplicative length two.  A natural way to
fill the gaps is to composite the pro-2 layers with fixed totally real fields
of odd degree.

This mechanism is rigorous.  For example, let (L_s) be a cyclic totally
real field of odd degree (s), linearly disjoint from the pro-2 tower.  Then

\[
  [K_jL_s:\mathbb Q]=s2^j.
\]

If all useful rational primes split completely in (L_s), their residue
degrees in the compositum remain at most two and the local sieve is unchanged.
Choosing (L_s) inside a real cyclotomic field ramified only at one of the
already ramified primes does not enlarge the crude root-discriminant product
bound: the compositum is still tame and ramified over the same rational set.

The phases from

\[
  s\in\{1,3,5,7,9,11,13,15\}
\]

give the normalized degree positions

\[
  1,\frac98,\frac54,\frac{11}8,\frac32,
  \frac{13}8,\frac74,\frac{15}8,
\]

so the maximum successive ratio falls from (2) to (9/8).

Concrete cyclic choices are supplied by conductors

\[
  7,11,29,19,23,53,31

\]

for degrees (3,5,7,9,11,13,15), respectively.  For every case except
degrees 7 and 13 this is the full real cyclotomic field.  In degrees 7 and
13 it is the unique indicated cyclic subfield.

## Why it loses

Complete splitting in a cyclic degree-(s) field has density (1/s).
The square-relator budget remains fixed, so the useful rational primes become
larger.  Their local entropy is essentially unchanged, while every depth
increment costs `log q`.  This Chebotarev thinning outweighs the improved
degree mesh.

For the rank-400 presentation and its 39,599 square relators, the last useful
prime in each family is:

| odd degree `s` | last useful prime |
|---:|---:|
| 1 | 479,939 |
| 3 | 1,572,577 |
| 5 | 2,725,669 |
| 7 | 8,228,461 |
| 9 | 5,130,001 |
| 11 | 6,372,749 |
| 13 | 7,601,897 |
| 15 | 8,864,761 |

An 80-bit floating exploratory sweep of the same two-stage master inequality
gave the following minimum exponents when each family is required by itself
to cover a full dyadic phase.  These are optimization diagnostics, not the
publication-grade `Decimal` certificate used for the (0.4947) theorem.

| `s` | approximate best exponent at rank 400 |
|---:|---:|
| 1 | 0.494654 |
| 3 | 0.495130 |
| 5 | 0.495326 |

The auxiliary families are therefore not even active at the exponent where
the base family is tight.  Allowing each family to cover only its short
natural arc on the logarithmic degree circle does not help: near exponent
0.494654, every (s>1) family has an empty feasible scale interval, while
the (s=1) interval alone is just becoming long enough to cover the circle.

The rank was also varied.  The best sampled dyadic exponents were near rank
800 for (s=1) (about 0.494588), rank 800 for (s=3) (about 0.495026), and
rank 1000 for (s=5) (about 0.495206).  Increasing the relation budget does
not reverse the ordering.

## Endpoint verdict

Fixed odd-degree composita are a valid way of obtaining dense degree phases,
but complete splitting spends more local entropy than the phase improvement
recovers.  They do not improve the current explicit exponent.

One can include non-split primes with gain divided by their odd residue
degree.  This only inserts a few very small primes ahead of late second-depth
increments; it cannot repair the first-depth entropy deficit responsible for
the empty feasible intervals.  A successful dense-degree construction would
need an odd-degree auxiliary tower sharing the useful primes without the
`1/s` Chebotarev loss, which is precisely the obstruction already encountered
in the pro-3 and base-change audits.
