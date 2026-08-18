# The orthogonal two-support gate

## Status

Let `A subset [m]^2` be distance-Sidon, put

\[
 D=A-A,\qquad N=|D|=|A|(|A|-1)+1,
\]

and let `J(x,y)=(-y,x)`.  There is a particularly clean sufficient theorem
for the conjectural cube-root upper bound:

\[
 \boxed{|D+D|\,|D+JD|\ge N^{3-o(1)}.}             \tag{0.1}
\]

Both factors in (0.1) lie in a box of `O(m^2)` lattice points.  Hence (0.1)
would give

\[
 N^{3-o(1)}\ll m^4,
 \qquad |A|\le m^{2/3+o(1)},                     \tag{0.2}
\]

and therefore `F_2(n)<=n^(1/3+o(1))` on taking `n=m^2`.

This formulation has an advantage over the preceding transverse-moment
gate: it automatically rewards both possible structures.  A line-like
difference set has small `D+D` but nearly quadratic `D+JD`; a genuinely
two-dimensional difference set may reverse or balance the two factors.  No
separate parallel/transverse splice appears in (0.1).

Equation (0.1) is not proved.  The most immediate second-moment route to it
is also false.  This note derives that route exactly and gives an asymptotic
distance-Sidon counterexample to the proposed moment estimate.  The product
gate itself survives that counterexample and all stored adversaries.

## 1. Why the exponent is exact

The difference set is contained in `[-m+1,m-1]^2`, so

\[
 |D+D|\le (4m-3)^2,
 \qquad |D+JD|\le (4m-3)^2.                      \tag{1.1}
\]

Write `k=|A|`.  Distance-Sidonicity implies oriented-difference uniqueness,
and therefore

\[
 N=k(k-1)+1=k^{2+o(1)}.                          \tag{1.2}
\]

Combining (0.1), (1.1), and (1.2) proves (0.2).  More generally, a bound

\[
 |D+D|\,|D+JD|\ge N^{2+\eta-o(1)}                \tag{1.3}
\]

would give

\[
 |A|\le m^{2/(2+\eta)+o(1)}.
\]

Thus any fixed `eta>0` would already be a new fixed-power upper mechanism,
while `eta=1` is exactly the full cube-root theorem.

Abstract direct-sum theory cannot prove (0.1).  Dense Golomb rulers give
co-Sidon pairs whose ordinary and mixed difference supports are both only
quadratic in the number of marks.  The load-bearing information is still
that `JD` is the quarter-turn of the complete difference set of the same
Euclidean distance-Sidon set.

## 2. A three-variable incidence model

For `q in D-D`, put

\[
 R_D(q)=|\{(x,y)\in D^2:y-x=q\}|.                \tag{2.1}
\]

For `s in D+D` and `t in D+JD`, define

\[
 F(s,t)=\#\{d\in D:s-d\in D,\ -J(t-d)\in D\}.  \tag{2.2}
\]

Choosing `d,e,g in D` and setting

\[
 s=d+e,\qquad t=d+Jg
\]

shows exactly that

\[
 \sum_{s,t}F(s,t)=N^3.                            \tag{2.3}
\]

The second moment also has an exact closed form.  If two representations in
one fibre use `d` and `d+q`, then their other two coordinates differ by
`-q` and `Jq`.  Consequently

\[
 \boxed{
 \sum_{s,t}F(s,t)^2
   =\Xi(D):=\sum_q R_D(q)^2R_D(Jq).}              \tag{2.4}
\]

The symmetry `R_D(-q)=R_D(q)` and the substitution `q -> -Jq` also give

\[
 \sum_qR_D(q)^2R_D(Jq)
 =\sum_qR_D(q)R_D(Jq)^2.                          \tag{2.5}
\]

Cauchy--Schwarz and `supp(F) subset (D+D)x(D+JD)` yield

\[
 |D+D|\,|D+JD|\ge {N^6\over\Xi(D)}.              \tag{2.6}
\]

It was therefore tempting to conjecture

\[
 \Xi(D)\le N^{3+o(1)}.                            \tag{2.7}
\]

This would prove (0.1).  The zero translation alone contributes exactly
`R_D(0)^3=N^3`, and every compact closure, generic-parabola, and sparse-ruler
test initially remained within a constant factor of this baseline.

## 3. Dense perpendicular rulers disprove the moment estimate

The estimate (2.7) is false by a full power even for genuine integral
distance-Sidon sets.

Take a Golomb ruler `R` with `2s` marks in an interval of length `O(s^2)`;
the Erdos--Turan construction supplies such rulers.  Split its marks into
two `s`-sets `X,Y`.  Put `X` on the horizontal axis and a translate of `Y`
on the vertical axis:

\[
 A_C=\{(x,0):x\in X\}\cup\{(0,C+y):y\in Y\}.     \tag{3.1}
\]

The internal horizontal and vertical distance spectra are disjoint because
`X union Y` is one Golomb ruler.  Cross-distance equalities are nonzero
polynomial conditions in `C`; two distinct cross pairs give a nonconstant
linear condition unless they are already the same pair.  Equalities between
a cross distance and an internal distance are also nonzero polynomial
conditions.  An integer `C` outside the finite bad set therefore makes
`A_C` distance-Sidon.

Let

\[
 P=X-X,\qquad Q=Y-Y.
\]

Both have `Theta(s^2)` elements and lie in an interval of length `O(s^2)`.
Moreover

\[
 P\times\{0\}\subset D,
 \qquad \{0\}\times Q\subset D.                 \tag{3.2}
\]

For a scalar shift `h`, (3.2) gives

\[
 R_D((h,0))\ge R_P(h),
 \qquad R_D((0,h))\ge R_Q(h).                   \tag{3.3}
\]

The cross additive energy of `P,Q` satisfies

\[
 \sum_hR_P(h)R_Q(h)
 \ge {|P|^2|Q|^2\over |P+Q|}
 \gg s^6.                                       \tag{3.4}
\]

Weighted Cauchy--Schwarz now gives

\[
 \sum_hR_P(h)^2R_Q(h)
 \ge {\bigl(\sum_hR_P(h)R_Q(h)\bigr)^2
       \over \sum_hR_Q(h)}
 \gg {s^{12}\over s^4}=s^8.                    \tag{3.5}
\]

Equations (2.4), (3.3), and (3.5) imply

\[
 \boxed{\Xi(D)\gg s^8\asymp N^4,}               \tag{3.6}
\]

because `|A_C|=2s` and `N=Theta(s^2)`.  Thus (2.7) fails by the largest
possible power.  This is the same parallel obstruction that invalidated the
size-only rotated-energy theorem, now detected one level higher.

Importantly, (3.6) does **not** disprove (0.1).  Dense perpendicular rulers
have very large two-support product: the quarter-turn turns one arm's
additive structure into transverse expansion.  What fails is only the use of
the global `L^2` fibre bound (2.7) to prove that product estimate.

## 4. Exact calibration

The verifier checks (2.3)--(2.4) directly on the eight-point closure prefix
and records the following exact profiles.

\[
\begin{array}{c|r|r|r|r|r}
\text{family}&N&|D+D|&|D+JD|&\Xi(D)&
 |D+D||D+JD|/N^3\\ \hline
\text{closure }k=20&381&16097&24305&90168653&7.0740\ldots\\
\text{parabola }p=31&931&9779&866761&806954491&10.5037\ldots\\
\text{dense perpendicular }k=40&1561&431225&1413381&4794246337&160.2339\ldots
\end{array}                                      \tag{4.1}
\]

For the transformed finite-field parabola, `Xi(D)=N^3` exactly: all nonzero
ordinary translation differences miss their quarter-turns.  The closure and
perpendicular examples have nontrivial excess, while their support products
remain safely above the conjectural threshold.

Run

```text
python3 phase2/loop/erdos1208/verify_orthogonal_two_support_gate.py
```

## 5. Correct restart point

The live global theorem is (0.1), not the false moment majorant (2.7).
There are two plausible ways to proceed.

1. Prove the product inequality directly by an additive-structure
   dichotomy: small `D+D` must force expansion of `D+JD`, while simultaneous
   smallness would create a quarter-turn-stable rank-two model incompatible
   with Euclidean radial uniqueness of the complete difference set.
2. Split the fibres in (2.2) into parallel ruler-like components and a
   transverse remainder.  The parallel component must be paid for by the
   *cardinality* of the opposite support rather than by its second moment;
   only the transverse remainder should satisfy an `N^(3+o(1))` moment
   theorem.

This gate is not yet known to be easier than the decorated-parallelogram
theorem.  Its concrete advantage is that it packages the missing line-rich
splice and the transverse expansion into one scale-perfect inequality.

## 6. A weaker local fibre theorem would already give exponent `2/5`

There is a useful intermediate target between the present `0.494586` theorem
and the full product estimate (0.1).  For `t in D+JD`, define the fixed-row
fibre

\[
 E_t=\{e\in D:t-e\in JD\},\qquad r_t=|E_t|.       \tag{6.1}
\]

Let `r=max_t r_t`, and choose `t` attaining the maximum.  Since the `r_t`
are the representation multiplicities of `D+JD`,

\[
 |D+JD|\ge {N^2\over r}.                          \tag{6.2}
\]

The affine quarter-turn

\[
 E'_t=J(E_t-t)
\]

is also a subset of `D`.  Ruzsa's triangle inequality, applied to
`E_t,D,E'_t`, therefore gives

\[
 |E_t-JE_t|N=|E_t-E'_t|N
 \le |E_t-D|\,|D-E'_t|
 \le |D+D|^2.                                    \tag{6.3}
\]

(The first equality ignores the fixed translation `Jt`.)  Consequently the
local statement

\[
 \boxed{|E_t-JE_t|\ge |E_t|^{2-o(1)}
 \quad\hbox{for every }t}                        \tag{6.4}
\]

would imply `r<=|D+D|N^(-1/2+o(1))`.  Combining this with (6.2) yields

\[
 |D+D|\,|D+JD|\ge N^{5/2-o(1)}.                 \tag{6.5}
\]

Since both supports are `O(m^2)`, (6.5) gives

\[
 |A|\le m^{4/5+o(1)},
 \qquad F_2(n)\le n^{2/5+o(1)}.                 \tag{6.6}
\]

Thus (6.4), while not a full solution, would be a major unconditional upper
improvement.  It is only a conjectural local lemma at present.  Exact maximum-
fibre checks give

\[
\begin{array}{c|r|r|r}
\text{family}&r&|E_t-JE_t|&|E_t-JE_t|/r^2\\ \hline
\text{closure }k=20&56&2303&0.734375\\
\text{parabola }p=31&1&1&1\\
\text{dense perpendicular }k=40&97&9409&1
\end{array}                                      \tag{6.7}
\]

Larger stored closure tests keep the last ratio above `0.5`, but that is
evidence rather than a theorem.  The next falsification task is to test (6.4)
against scalable fixed-row six-biclique and eight-corner completion families.
If it survives, the proof problem is to show that a collision
`e_1-Je_2=e_3-Je_4` cannot have high multiplicity inside one fibre without
creating a repeated Euclidean norm in the original complete difference set.
