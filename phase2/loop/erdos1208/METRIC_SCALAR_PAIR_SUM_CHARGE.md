# A metric scalar charge for the clean pair-sum fibre

## 1. Exact reduction

Let `A subset Z^2` be distance-Sidon, let `|A|=k`, and suppose that both
coordinate widths of `A` are at most `m`.  Write

\[
 \Sigma=A\mathbin\oplus A,
 \qquad N=|\Sigma|=\binom k2,
\]

and let `H_q subset Sigma` be the clean start set for a realized directed
difference `q`, as in `DILATED_INTERNAL_PAIR_SUM_CHARGE.md`.  Every
`s in Sigma` has a unique unordered representation `s=a+b`.  Define its
canonical metric label

\[
 \delta(s)=|a-b|^2.                              \tag{1.1}
\]

Distance-Sidonicity makes `delta` injective on `Sigma`.  Fix a positive
integer `C`; the useful numerical choice below is `C=18`.  Consider

\[
 \Phi_{q,C}:H_q\times\Sigma\longrightarrow\mathbb Z,
 \qquad
 \Phi_{q,C}(s,t)=\delta(s)+C\delta(t).           \tag{1.2}
\]

This charge has `hN` records, where `h=|H_q|`, and only `O_C(m^2)` possible
integer values.  If

\[
 B_q=\delta(H_q),\qquad D=\delta(\Sigma),
\]

and `r_(X-X)(z)=|{(x,x') in X^2:x-x'=z}|`, its collision energy is exactly

\[
 \boxed{
 \mathcal M_{q,C}
 =\sum_{r\in\mathbb Z}
   r_{B_q-B_q}(Cr)r_{D-D}(-r).}                 \tag{1.3}
\]

The `r=0` contribution is exactly `hN`, because both metric-label maps are
injective.  Consequently the estimate

\[
 \boxed{\mathcal M_{q,C}\le m^{o(1)}hN}          \tag{1.4}
\]

for every clean fibre would prove

\[
 h\le {m^{2+o(1)}\over k^2}.                   \tag{1.5}
\]

Summing (1.5) over the `k(k-1)` realized directed differences and using the
exact identity

\[
 C_6(A)=4\sum_q |H_q|
\]

gives the ambient equal-centroid bound and hence

\[
 |A|\le m^{2/3+o(1)}.
\]

Thus (1.4) would resolve the square-grid order and Erdős problem 1208.  It
is currently unproved.

### Proof of the implication

Equation (1.3) is obtained by expanding equality of two values in (1.2):

\[
 \delta(s)-\delta(s')
   =C\bigl(\delta(t')-\delta(t)\bigr).
\]

Both labels lie in `[1,2m^2]`, so (1.2) has at most
`2(C+1)m^2+1` values.  Cauchy--Schwarz and (1.4) give

\[
 (hN)^2
 \le (2(C+1)m^2+1)m^{o(1)}hN.
\]

Cancel `hN` and use `N asymp k^2` to obtain (1.5).  The standard origin
localization of third additive energy completes the displayed cube-root
deduction.

## 2. Why this retains information missing from the vector charge

The earlier charge `s+3(I+J)t` sees the endpoint sums but not their
Euclidean separation.  In contrast, (1.1) is precisely the globally unique
squared-distance label of the canonical edge represented by `s`.  The
finite-field parabola therefore does not automatically transfer as a
counterexample: an integral affine map which separates its Euclidean
distances also changes every label in (1.2).

The coefficient `18` is the norm multiplier of `3(I+J)`, but the reduction
works for every fixed positive integer `C`.  Larger fixed coefficients look
slightly more injective in finite data, but no asymptotic claim follows from
that observation.

## 3. A rigorous collinear branch

**Proposition 3.1.**  Estimate (1.4) holds when `A` is collinear.

After translation, write the points as `r v`, where `v` is a fixed primitive
integral vector and the integers `r` form a Golomb ruler.  Every metric label
is

\[
 \delta=|v|^2 d^2,
\]

where the positive ruler differences `d` are all distinct.  A fibre of
(1.2) is therefore contained in the set of positive integer solutions of

\[
 x^2+C y^2=n.                                    \tag{3.1}
\]

For fixed `C`, the representation number of the positive-definite binary
quadratic form in (3.1) is `n^{o(1)}`.  This follows, for example, from the
standard ideal-divisor bound in the fixed quadratic order of discriminant
`-4C`; the finitely many imprimitive factors only change the constant.
Since `n=O_C(m^2)`, every load of (1.2) is `m^{o(1)}`.  Hence its second
moment is at most `m^{o(1)}hN`, proving the proposition.

This branch is already covered by the stronger projection theorem, but it
is useful evidence that the scalar charge interacts correctly with the
classical Golomb-ruler obstruction.

## 4. A scalable exact stress: the integer parabola

The family

\[
 P_r=\{(j,j^2):0\le j<r\}                       \tag{4.1}
\]

is itself distance-Sidon.  Indeed, for `i>j` put

\[
 u=i-j,\qquad v=i+j.
\]

The squared distance is

\[
 d=u^2(1+v^2)=(uv)^2+u^2.                      \tag{4.2}
\]

Because `1<=u<=v`,

\[
 (uv)^2<d<(uv+1)^2.
\]

Thus `floor(sqrt(d))=uv`, after which (4.2) recovers
`u^2=d-(uv)^2`, then `u,v`, and finally the unordered pair `{i,j}`.

The exact verifier constructs the largest clean fibre for (4.1).  At
`r=10,15,20,25,30,40,50`, the normalized scalar-charge energies for `C=18`
are respectively

\[
 1, 1.00816\ldots, 1.00827\ldots, 1.01394\ldots,
 1.01275\ldots, 1.01144\ldots, 1.01199\ldots .
\]

The maximum loads are at most three.  This is a scalable falsification test,
not a proof of (1.4); the parabola lies in a box of side `Theta(r^2)` and is
well below the cube-root-critical density.

## 5. Exact finite profiles

For the largest clean fibre of each stored family, the verifier reports

\[
 (k,m,q,h,N,hN,|\operatorname{im}\Phi|,
   \mathcal M_{q,18},\max\Phi^{-1}).
\]

\[
\begin{array}{c|r|r|r|r}
\text{family}&hN&|\operatorname{im}\Phi|&\mathcal M_{q,18}&\max\Phi^{-1}\\ \hline
\text{closure }30&6090&5964&6342&2\\
\text{closure }40&17940&16732&20592&4\\
\text{closure }80&199080&188394&221584&4\\
\text{closure }120&906780&851608&1023788&6\\
\text{source }45&21780&21364&22612&2\\
\text{perpendicular ruler }40&10920&10911&10938&2\\
\text{Costas }22&7854&7601&8382&3\\
\text{parabola image }43&154413&153065&157133&3
\end{array}
\]

The largest normalized energy in the table is `1.147826...` on closure 40;
closure 120 is `1.129036...`.  These profiles are substantially less rigid
than the vector charge but remain at constant scale on every present stress.

Run

```text
python3 phase2/loop/erdos1208/verify_metric_scalar_pair_sum_charge.py
```

## 6. Exact remaining theorem

The live target is (1.4), or just its aggregate consequence

\[
 \sum_q|H_q|\le m^{o(1)}(k^2+m^2).
\]

One cannot replace `B_q` by the whole squared-distance set and appeal only
to additive energy: the closure profiles have much larger global distance
energy, while the restricted clean fibres remain nearly diagonal.  A proof
must use simultaneously that

1. `B_q` consists of source-edge labels in one clean pair-sum translate;
2. every label in `D` has one endpoint edge; and
3. all labels are norms of integral planar differences.

The next inverse step is to show that polynomial cross-additive energy
between `B_q` and `C D` forces two distinct endpoint differences to have the
same norm.  That conclusion is forbidden by distance-Sidonicity.
