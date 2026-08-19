# Ambient third energy and the equal-centroid gate

## 1. Outcome

Let

\[
 A\subset[0,m]^2\cap\mathbb Z^2,
 \qquad |A|=k,
\]

be distance-Sidon.  Put

\[
 H(\theta)=|\widehat{1_A}(\theta)|^2,
 \qquad
 E_3^+(A)=\int_{\mathbb T^2}H(\theta)^3\,d\theta.
\]

There is a particularly small sufficient theorem for the conjectural
cube-root upper bound:

\[
 \boxed{E_3^+(A)\le k^{3+o(1)}+m^{2+o(1)}.}       \tag{1.1}
\]

This is an unproved gate, not a theorem.  It is stronger and more scalar
than the ambient cross-sum energy estimate: (1.1) by itself gives

\[
 k\le m^{2/3+o(1)},                              \tag{1.2}
\]

and hence the expected upper bound in Erdos problem 1208.

After the automatic repeated-label contribution is removed, (1.1) has an
exact finite-combinatorial form.  For a lattice vector `s`, let

\[
 t_s=\#\{T\in\tbinom A3:\sum_{a\in T}a=s\}.      \tag{1.3}
\]

Then the genuinely new theorem is

\[
 \boxed{
 \sum_s t_s(t_s-1)\le k^{3+o(1)}+m^{2+o(1)}.}    \tag{1.4}
\]

In fact all current stresses satisfy the sharper experimental estimate
`36 sum_s t_s(t_s-1)=O(m^2)`.  The quantity on the left counts ordered
six-distinct equal-triple-sum configurations; geometrically, it counts
pairs of disjoint triangles with the same centroid.  Thus the direct problem
has been reduced to an ambient bound for equal-centroid triangle matchings.

No proof of (1.4) is asserted below.  Its value is that it removes the
quarter-turn bookkeeping and isolates one scalar, six-point incidence
population which survives all known obstructions at exactly the right
height scale.

## 2. Origin localization proves the implication

Translate `A` so that each coordinate range is at most `m`.  On

\[
 |\theta_1|,|\theta_2|\le {1\over16m},
\]

all phases of `hat 1_A(theta)` lie in an arc of angular length at most
`pi/4`.  A common rotation therefore gives

\[
 H(\theta)\ge {k^2\over2}.                       \tag{2.1}
\]

The frequency square has area `1/(64m^2)`, so

\[
 \boxed{E_3^+(A)\ge {k^6\over512m^2}.}           \tag{2.2}
\]

Combining (2.2) with (1.1), and splitting according to the larger term on
the right of (1.1), gives either

\[
 k^6/m^2\le k^{3+o(1)}
\]

or

\[
 k^6/m^2\le m^{2+o(1)}.
\]

Both alternatives give (1.2).  Since an `m` by `m` grid has `n=m^2`
points, this is `F_2(n)<=n^(1/3+o(1))`; the universal lower bound of
Clemen--Fuehrer--Roche-Newton then determines the power-law order.

The same gate implies the preceding ambient cross-sum estimate.  Indeed,
with `H_J(theta)=H(J theta)`, pointwise AM--GM gives

\[
 H^2H_J^2\le\frac12(H^3H_J+HH_J^3).
\]

The two integrals on the right are equal after rotating the torus, and
`H_J<=k^2`.  Hence

\[
 \boxed{E^+(A+JA)\le k^2E_3^+(A).}              \tag{2.3}
\]

Thus (1.1) gives exactly
`E^+(A+JA)<=k^(5+o(1))+m^(2+o(1))k^2`.

## 3. Exact complete-difference expansion

Distance-Sidonicity implies vector-Sidonicity.  Put

\[
 D=A-A,\qquad N=|D|=k(k-1)+1,
 \qquad \lambda=\widehat{1_D},\qquad c=k-1.
\]

The endpoint identity is

\[
 H=c+\lambda.                                    \tag{3.1}
\]

Since `D` is symmetric and contains zero,

\[
 \int\lambda=1,\qquad \int\lambda^2=N.          \tag{3.2}
\]

Moreover

\[
 T(D):=\int\lambda^3
 =\#\{(x,y,z)\in D^3:x+y+z=0\}.                 \tag{3.3}
\]

Expanding (3.1) gives the exact identity

\[
 \boxed{
 E_3^+(A)=c^3+3c^2+3cN+T(D).}                   \tag{3.4}
\]

The first three terms are `O(k^3)`.  Therefore (1.1) is equivalent, up to
the harmless `k^(3+o(1))` term, to

\[
 T(A-A)\le k^{3+o(1)}+m^{2+o(1)}.               \tag{3.5}
\]

This makes the load-bearing hypothesis explicit.  Canonical symmetric
radial transversals have far more than the right side of (3.5); see
`RADIAL_ADDITIVE_TRIPLE_AUDIT.md`.  The missing input is that `D` is the
complete endpoint-decorated difference set of one distance-Sidon set.

## 4. Repeated labels are automatic

An ordered third-energy configuration is

\[
 a_1+a_2+a_3=b_1+b_2+b_3.                       \tag{4.1}
\]

There are 15 possible equalities between two of the six endpoint roles.
Fix one.  If the merged variables occur on opposite sides, their
coefficients cancel; the common variable is free and the remaining
four-variable equation is bounded by the additive energy

\[
 E^+(A)=2k^2-k.
\]

If the variables occur on the same side, the merged coefficient is `2I`.
Four of the five Fourier factors may be put in `L^4`, while the fifth is
bounded by `k`; the torus map `theta -> 2theta` preserves Haar measure.
This again gives at most `2k^3` solutions.  A union bound proves

\[
 \boxed{
 \#\{\text{configurations in (4.1) with a repeated label}\}
 \le30k^3.}                                      \tag{4.2}
\]

Consequently only the six-distinct configurations can obstruct (1.1).

There is an exact unordered description.  Because `A` is vector-Sidon, two
different three-subsets having the same sum cannot share a point: after
removing a shared point, equality of the remaining pair sums identifies the
two unordered pairs.  Thus every family counted by `t_s` is a matching of
three-subsets, and every pair of its members is disjoint.  Ordering the two
triples in all `3!` ways gives

\[
 \boxed{
 C_6(A)=36\sum_s t_s(t_s-1),}                   \tag{4.3}
\]

where `C_6(A)` is the number of ordered six-distinct solutions of (4.1).
Equations (4.2)--(4.3) prove the equivalence between (1.1) and (1.4).

## 5. A natural scalar charge and its limitation

For one collision `T,U` with common sum `s`, define the relative inertia

\[
 I(T)=3\sum_{a\in T}|a|^2-|s|^2
     =\sum_{\{a,b\}\in\binom T2}|a-b|^2.        \tag{5.1}
\]

Then

\[
 \mathcal I(T,U)=I(T)+I(U)                      \tag{5.2}
\]

is a nonnegative integer of size `O(m^2)`.  It is also half the sum of all
15 squared distances among the six points `T union U`: the two triples have
the same centroid, and the standard variance identity gives

\[
 \sum_{\{x,y\}\in\binom{T\cup U}2}|x-y|^2
 =2\mathcal I(T,U).                              \tag{5.3}
\]

This is a compelling candidate charge into an `O(m^2)` universe.  It is
nearly injective on every stored stress: its maximum loads on closure 120,
the perpendicular ruler, Costas 22, and the transformed parabola 127 are
respectively `3,1,2,3`.

That computation is evidence, not a multiplicity theorem.  Distinctness of
the 15 individual distances does not by itself make their sum unique, and
no subpolynomial load bound for (5.2) has been proved.  A successful proof
may instead need a size-biased bound on its charge fibres, or a second
endpoint-sensitive charge for the rare high-inertia loads.

## 6. Exact stress profiles

The verifier records:

\[
\begin{array}{c|r|r|r|r|r}
\text{family}&k&m&E_3^+(A)&C_6(A)&
 E_3/(k^3+m^2)\\ \hline
\text{closure }30&30&150&172{,}866&15{,}264&3.4922\ldots\\
\text{closure }40&40&223&427{,}252&49{,}680&3.7567\ldots\\
\text{closure }80&80&719&3{,}596{,}786&544{,}536&3.4955\ldots\\
\text{closure }120&120&1514&12{,}824{,}964&2{,}489{,}760&3.1901\ldots\\
\text{source }45&45&324&586{,}101&51{,}336&2.9887\ldots\\
\text{perpendicular ruler }40&40&3202&396{,}988&19{,}656&0.0384\ldots\\
\text{Costas }22&22&131&106{,}222&37{,}368&3.8196\ldots\\
\text{parabola image }127&127&20831&86{,}658{,}955&72{,}011{,}880&0.1987\ldots
\end{array}                                      \tag{6.1}
\]

The six-distinct normalization is even sharper.  The values of `C_6/m^2`
for closure `40,80,120` are

\[
 0.9990\ldots,\quad1.0533\ldots,\quad1.0861\ldots.
\]

Thus the purpose-built closure adversary lands directly on the conjectural
ambient scale rather than merely staying below it.  The transformed
finite-field parabola, which has third energy of order `k^4`, is also paid
for by its quadratic geometric height `m^2`.

Run

```text
python3 phase2/loop/erdos1208/verify_ambient_third_energy_centroid_gate.py
```

for exact distance checks, third-energy counts, the complete-difference
expansion (3.4), the centroid-matching identity (4.3), the origin lower
bound in integer form, and the inertia-charge profiles.

## 7. Restart target

The clean next theorem is the **ambient centroid-matching bound** (1.4).
Two promising proof interfaces retain all essential information:

1. prove a size-biased `O(m^(2+o(1)))` bound for the relative-inertia charge
   (5.2), with a separate structured analysis of its high-load fibres; or
2. view each common-sum class as a matching of three-subsets and prove that
   many large matching classes force either a repeated Euclidean distance
   or geometric height `m` large enough to pay their squared mass.

Unlike a generic third-energy inverse theorem, either route must keep the
quadratic norm injective on all realized differences.  The unstretched
finite-field parabola shows that vector-Sidonicity and general position alone
permit `E_3=Theta(k^4)` in a linear-height box.
