# Cross-sum energy: exact diagonal removal and the fixed rich tail

## 1. Outcome

Let `A subset Z^2` be distance-Sidon, put

\[
 k=|A|,\qquad D=A-A,\qquad N=|D|=k(k-1)+1,
\]

and let `J(x,y)=(-y,x)`.  The cross sum

\[
 B=A+JA
\]

is direct and has `k^2` elements.  This note makes two reductions in the
ambient energy gate exact.

First, if

\[
 R(q)=|D\cap(D+q)|,\qquad
 E_\perp(D)=\sum_qR(q)R(Jq),
\]

then

\[
 \boxed{
 E^+(B)=E_\perp(D)-N^2+(2k^2-k)^2
       +4(k-1)\sum_{q\in D\setminus\{0\}}R(Jq).}
 \tag{1.1}
\]

In particular,

\[
 \boxed{E^+(B)\le E_\perp(D)+8k^5.}             \tag{1.2}
\]

Thus the weighted autocorrelation of `A` costs only an automatic fifth-power
term; the hard quantity is the unweighted orthogonal energy of the complete
difference set.

Second, every energy configuration in which two of its eight endpoint
variables agree contributes only `O(k^5)` in total.  Therefore the proposed
ambient estimate

\[
 E^+(A+JA)\le k^{5+o(1)}+m^{2+o(1)}k^2           \tag{1.3}
\]

has a single genuinely new component: bound the configurations with eight
distinct endpoints.  Equivalently, after the elementary low-overlap removal
in Section 4, it is enough to bound the fixed jointly rich tail

\[
 \sum_{\substack{q\ne0\\R(q)>\sqrt N,
                         R(Jq)>\sqrt N}}
 R(q)R(Jq).                                     \tag{1.4}
\]

This is a reduction, not a proof of (1.3).

## 2. Exact autocorrelation expansion

Vector-Sidonicity gives the weighted difference function

\[
 r_A=k\delta_0+1_{D\setminus\{0\}}
    =1_D+(k-1)\delta_0.                         \tag{2.1}
\]

Write `c=k-1`.  Since `D` is symmetric,

\[
 (r_A\circ r_A)(q)
 =R(q)+2c1_D(q)+c^2\delta_0(q).                 \tag{2.2}
\]

The direct sum `B=A+JA` has autocorrelation

\[
 r_B(t)=\sum_{x+Jy=t}r_A(x)r_A(y),
\]

and Parseval, or a direct coefficient expansion, gives

\[
 E^+(B)=\sum_q(r_A\circ r_A)(q)
                    (r_A\circ r_A)(Jq).         \tag{2.3}
\]

Distance-Sidonicity also gives

\[
 D\cap JD=\{0\}.                                \tag{2.4}
\]

At zero, `(r_A circ r_A)(0)=2k^2-k`.  Away from zero the product of the two
indicator terms in (2.2) vanishes by (2.4).  Expanding (2.3), and using the
rotation and sign symmetry to identify the two cross terms, proves (1.1).

Finally,

\[
 \sum_{q\in D\setminus\{0\}}R(Jq)
 \le\sum_qR(q)=N^2.
\]

Together with `N<=k^2`, this proves (1.2), with considerable room in the
constant.

## 3. Every repeated-endpoint configuration is fifth-power

An ordered energy configuration is an eight-tuple

\[
 (a_1,a_2,a_3,a_4,b_1,b_2,b_3,b_4)\in A^8
\]

satisfying

\[
 a_1+a_2-a_3-a_4
 =J(b_3+b_4-b_1-b_2).                           \tag{3.1}
\]

There are 28 possible selected equalities between two endpoint roles.  Fix
one of them and merge the selected variables.  Every coefficient in (3.1)
is one of `+/-I,+/-J`.

If the two merged coefficients do not cancel, the resulting equation has
seven variables with nonzero nonsingular integral matrix coefficients.  If
they cancel, the common variable is free and the remaining equation has six
such variables.

The following standard Fourier estimate handles both cases.  If `A` is
vector-Sidon and `M_1,...,M_s` are nonsingular integral two-by-two matrices,
then, for `4<=s<=7`,

\[
 \#\{(x_1,\ldots,x_s)\in A^s:
                  M_1x_1+\cdots+M_sx_s=0\}
 \le 2k^{s-2}.                                  \tag{3.2}
\]

Indeed, write the count as a torus integral of the corresponding
exponential sums.  The endomorphism
`theta -> M_j^T theta` preserves Haar measure, while vector-Sidonicity gives

\[
 \int_{\mathbb T^2}|\widehat{1_A}(\theta)|^4d\theta
 =2k^2-k.                                       \tag{3.3}
\]

Put four factors in `L^4` and bound the remaining factors by `k`.  Holder's
inequality proves (3.2).

For a noncancelling merge, (3.2) with `s=7` gives at most `2k^5`
configurations.  For a cancelling merge, (3.2) with `s=6`, followed by the
`k` choices of the free variable, gives the same bound.  A union bound over
the 28 role pairs proves

\[
 \boxed{\#\{\text{energy configurations with a repeated endpoint}\}
        \le56k^5.}                              \tag{3.4}
\]

The union bound deliberately overcounts tuples having several endpoint
equalities.  Only the exponent matters.

This lemma uses only vector-Sidonicity.  The remaining eight-distinct term
is precisely where uniqueness of Euclidean lengths, rather than merely
directed differences, must enter.

## 4. The automatic low-overlap contribution

Put

\[
 \mathcal P=\{q\ne0:R(q)>\sqrt N,
                       R(Jq)>\sqrt N\}.         \tag{4.1}
\]

The zero shift contributes `N^2`.  On shifts with `R(q)<=sqrt(N)`, the
orthogonal energy is at most

\[
 \sqrt N\sum_qR(Jq)=N^{5/2}.
\]

The symmetric class with `R(Jq)<=sqrt(N)` costs the same.  Hence

\[
 \boxed{
 E_\perp(D)\le N^2+2N^{5/2}
       +\sum_{q\in\mathcal P}R(q)R(Jq).}         \tag{4.2}
\]

Since `N asymp k^2`, the first two terms are already `O(k^5)`.  Combining
(1.2), (3.4), and (4.2) isolates the same hard population in three exact
languages:

1. eight-distinct endpoint solutions of (3.1);
2. the jointly `sqrt(N)`-rich orthogonal translation tail (1.4); and
3. cross-fibre reuse in the opposite-endpoint charge.

The fixed cutoff is weaker than the support-adaptive cutoff `S/N` when
`S=|D+D|` is large, but it is the natural cutoff for the ambient correction
`m^2N`.  A proof that

\[
 \sum_{q\in\mathcal P}R(q)R(Jq)
 \le N^{5/2+o(1)}+m^{2+o(1)}N                  \tag{4.3}
\]

would establish the ambient cross-sum gate and resolve the cube-root
exponent.

## 5. Verification

`verify_cross_sum_diagonal_and_rich_tail.py` checks, in exact integer
arithmetic:

* directness of `A+JA`;
* identity (1.1);
* the fixed rich-tail decomposition (4.2);
* the literal split of every energy tuple into eight-distinct and
  repeated-endpoint configurations; and
* the numerical bound (3.4).

The stored regression families include the relation-closure witness, a
determinant-prime Costas set, and a small perpendicular-ruler set.
