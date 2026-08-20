# The raw two-scale distance-gap correlation is necessarily large

## Status

This note closes one proposed arithmetic shortcut, but not the endpoint-rich
tail that occurs in the current low-codegree branch.

Let $A\subseteq\{0,\ldots,m\}^2$ be distance-Sidon, let

\[
 D=\{\lVert a-b\rVert^2:\{a,b\}\in {A\choose 2}\},
 \qquad N=|D|={k\choose2},
\]

and put

\[
 R_D(r)=|\{(x,x')\in D^2:x-x'=r\}|.
\]

The hoped-for unrestricted estimate

\[
 \sum_rR_D(r)R_D(-18r)\le m^{o(1)}N^2                 \tag{1}
\]

is false even for genuine integral planar distance-Sidon sets.  In fact there
are such sets for which the left side is $\Omega(kN^2)$.  This is not a
Gaussian-divisor issue: it is forced by the one-dimensional range of the
charge $x+18y$.

The determinant-qualified *weighted* version remains large whenever the
determinant cutoff and richness threshold are $o(k)$, up to the Gaussian
divisor loss.  By contrast, the *unweighted* target-rich sum can still
conceivably have the $N^2$-scale upper bound needed by the live proof branch.

## 1. Exact charge identity and range lower bound

Define

\[
 E_{18}(D)=\sum_rR_D(r)R_D(-18r).
\]

For $s\in\mathbb Z$, let

\[
 L(s)=|\{(x,y)\in D^2:x+18y=s\}|.
\]

Then

\[
 E_{18}(D)=\sum_s L(s)^2.                              \tag{2}
\]

Indeed, a collision $x+18y=x'+18y'$ is equivalent to
$y-y'=r$ and $x-x'=-18r$.  Since every squared distance is an
integer in $[1,2m^2]$, the support of $L$ has at most $38m^2+1$
elements.  Also $\sum_sL(s)=N^2$.  Cauchy--Schwarz therefore gives the
unconditional lower bound

\[
 \boxed{E_{18}(D)\ge \frac{N^4}{38m^2+1}.}             \tag{3}
\]

Consequently, (1) by itself would imply $N\le m^{1+o(1)}$, or
$k\le m^{1/2+o(1)}$.  A correlation estimate this strong cannot hold in
the cube-root problem.

## 2. Genuine asymptotic counterexamples

Clemen, Führer and Roche-Newton prove that every finite planar point set
$P$ has a subset $P'$ of size $\Omega(|P|^{1/3})$ whose pairwise
distances are all distinct:

> Felix Christian Clemen, Jakob Führer, Oliver Roche-Newton,
> *Geometric Sidon Problems*, arXiv:2606.05841 (2026),
> <https://arxiv.org/abs/2606.05841>.

Apply their theorem to the full integer grid
$P=\{0,\ldots,m\}^2$.  This gives genuine integral distance-Sidon sets
with

\[
 k\gg m^{2/3}.
\]

For these sets, $N={k\choose2}\gg k^2$, and (3) gives

\[
 \frac{E_{18}(D)}{N^2}
 \gg \frac{k^4}{m^2}
 \gg k.
\]

Thus

\[
 \boxed{E_{18}(D)\gg kN^2}                             \tag{4}
\]

along an infinite family.  Since the $r=0$ contribution is only $N^2$,
the same lower bound holds for the off-diagonal correlation

\[
 E_{18}^{\ne0}(D)=\sum_{r\ne0}R_D(r)R_D(-18r)
\]

after changing the absolute constant.  This is a polynomial, not a
subpolynomial, violation of (1).

This also explains why modular or Gaussian factorization cannot repair the
raw estimate.  Such arguments may make every *decorated* cell small, but
there are only $O(m^2)$ possible undecorated scalar charges carrying
$N^2$ records.

## 3. What survives determinant truncation

For each $d\in D$, let $v_d\in\mathbb Z^2$ be either orientation of the
unique edge vector realizing $d$.  Decorate a gap by doubled signed area:

\[
 R_D(r,a)=|\{(d,d')\in D^2:
 d-d'=r,\ 2\det(v_d,v_{d'})=a\}|.
\]

For $r\ne0$, the standard Gaussian factorization

\[
 ((v_d-v_{d'})_x+i(v_d-v_{d'})_y)
 ((v_d+v_{d'})_x-i(v_d+v_{d'})_y)=r-ia
\]

shows uniformly that

\[
 R_D(r,a)\le G(m),\qquad
 G(m)=\exp\!\left(O\!\left(\frac{\log m}{\log\log m}\right)\right)
 =m^{o(1)}.                                             \tag{5}
\]

This assertion retains endpoint realizability: every member of a cell is the
actual unique edge for its distance label.  The estimate follows by counting
Gaussian divisors of the nonzero integer $r-ia$; parity and bounding-box
conditions can only reduce the count.

For an integer cutoff $L\ge0$, put

\[
 U_L(r)=\sum_{|a|>L}R_D(r,a),\qquad
 B_L=(2L+1)G(m).
\]

Equation (5) implies, for every $r\ne0$,

\[
 R_D(r)\le U_L(r)+B_L.                                  \tag{6}
\]

Multiplying (6) by $R_D(-18r)$ and summing gives the exact useful
consequence

\[
 \boxed{
 \sum_{r\ne0}U_L(r)R_D(-18r)
 \ge E_{18}^{\ne0}(D)-B_LN^2.}                         \tag{7}
\]

If $T\ge0$, the portion with $U_L(r)<T$ is at most $TN^2$.  Hence

\[
 \boxed{
 \sum_{\substack{r\ne0\\U_L(r)\ge T}}
 U_L(r)R_D(-18r)
 \ge E_{18}^{\ne0}(D)-(B_L+T)N^2.}                    \tag{8}
\]

For the grid subsets from Section 2, (8) is $\Omega(kN^2)$ whenever
$B_L+T=o(k)$.  Thus neither the raw correlation nor this
determinant-qualified **weighted** correlation admits a universal
$m^{o(1)}N^2$ upper bound in that regime.

## 4. The unweighted rich tail is not disproved

Because $U_L(r)\le R_D(r)\le N$, (8) only yields

\[
 \sum_{\substack{r\ne0\\U_L(r)\ge T}}R_D(-18r)
 \ge
 \frac{E_{18}^{\ne0}(D)-(B_L+T)N^2}{N}.                \tag{9}
\]

On the counterexample sequence and under $B_L+T=o(k)$, this is merely
$\Omega(kN)$, which is much smaller than $N^2\asymp k^4$.  Therefore the
present argument does **not** contradict a bound of the form

\[
 \sum_{r:U_L(r)\ge T}R_D(-18r)\le m^{o(1)}N^2.
\]

That unweighted, endpoint-realized reciprocal tail is the smallest version
of the two-scale arithmetic lemma still capable of helping the proof.

For the adaptive cutoff $L=N/h$, the error in (7) is
$B_LN^2\ll G(m)(N/h)N^2$.  The forced lower bound from (4) survives only
when

\[
 h\gg G(m)\frac Nk\asymp G(m)k.
\]

So this no-go automatically reaches the very-heavy-fibre range, but not the
critical $h\asymp k$ range once the divisor loss is retained.

## 5. Finite exact stress

The verifier computes both sides of (2), checks the range Cauchy inequality,
and checks (6)--(8) directly on several distance-Sidon certificates.  The
following raw profiles are useful diagnostics:

| family | $k$ | $N$ | $E_{18}$ | $E_{18}/N^2$ |
|---|---:|---:|---:|---:|
| closure | 20 | 190 | 77,246 | 2.140 |
| closure | 40 | 780 | 2,346,900 | 3.857 |
| Costas transform | 22 | 231 | 73,247 | 1.373 |
| modular parabola transform | 43 | 903 | 897,791 | 1.101 |
| ruler transform | 40 | 780 | 624,164 | 1.026 |

These finite values are not used as an asymptotic counterexample.  The
rigorous asymptotic obstruction is (3) plus the grid-subset theorem.

Verification:

```bash
python phase2/loop/erdos1208/verify_two_scale_distance_gap_correlation_no_go.py
```

## Conclusion

The broad arithmetic finish
“prove the whole two-scale distance-gap correlation is $N^2m^{o(1)}$”
is impossible.  The charge range itself forces $\Omega(kN^2)$ energy on
known genuine grid examples.  Determinant decoration only moves this mass
among $m^{o(1)}$-sized cells and does not remove it from the weighted sum.
Any viable continuation must discard the large $U_L(r)$ weight and control
the reciprocal **set of rich gaps**, or use additional endpoint/source
structure absent from $D$ alone.
