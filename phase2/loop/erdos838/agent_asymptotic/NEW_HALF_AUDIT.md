# Adversarial audit of the new `1/2` blow-up theorem

## Verdict

I found **no mathematical flaw** in `proof_blowup_half.md`.  The exact
substitution recurrence, its quadratic asymptotic, the deletion argument for
arbitrary `N`, and the final order of quantifiers all survive independent
derivation.

There is also a useful barrier beyond the one-fixed-template statement in the
draft.  Arbitrary nonstationary homogeneous templates cannot beat `1/2` if
no single template supplies a macroscopic fraction of the final logarithmic
size.  This covers stationary, periodic, finite-menu, and slowly growing
template schedules.  Polynomial random thinning of a fixed-template iterate
also preserves rather than improves its coefficient.

The remaining loophole is precise: heterogeneous or rapidly growing
Baek--Balko-style clusters can deliberately anti-align cap mass and cup mass.
Their exact count has a weighted formula below, but the cap--cup size theorem
alone does not close that formula.  I found no construction below `1/2`, nor
a valid barrier for this unrestricted heterogeneous class.

All logarithms below are base two.

## 1. Fixed-template recurrence, reconstructed

Let `S` have `r>=2` points, largest cap size `a`, and largest cup size `b`.
Put

\[
 p=a-1,\qquad q=b-1,\qquad \ell=\log r.
\]

For the iterates `Q_d=S[Q_{d-1}]`, `Q_0` a singleton, write
`N_d=r^d` and let `C_d,U_d,W_d` denote the nonempty cap, cup, and convex
counts.  Define the fixed polynomials

\[
 F_C(x)=\sum_{j\geq1}c_j(S)x^{j-1},\quad
 F_U(x)=\sum_{j\geq1}u_j(S)x^{j-1},\quad
 F_W(x)=\sum_{j\geq2}v_j(S)x^{j-2}.
\]

The composition lemma gives exactly

\[
\begin{aligned}
 C_d&=C_{d-1}F_C(r^{d-1}),\\
 U_d&=U_{d-1}F_U(r^{d-1}),                         \tag{1}\\
 W_d&=rW_{d-1}+C_{d-1}U_{d-1}F_W(r^{d-1}).
\end{aligned}
\]

Because a largest cap exists and every coefficient is nonnegative, for
`x>=1`

\[
 x^p\leq F_C(x)\leq C(S)x^p.                       \tag{2}
\]

The analogous bound holds for `F_U` with degree `q`.  Summing the logarithms
in (1) therefore gives the two-sided estimates

\[
\begin{aligned}
 \log C_d&=\frac{p\ell}{2}d(d-1)+O_S(d),\\
 \log U_d&=\frac{q\ell}{2}d(d-1)+O_S(d).           \tag{3}
\end{aligned}
\]

There is no hidden uniformity issue here: `S` is fixed when `d` tends to
infinity.  Also `F_W` is nonzero because
`v_2(S)=binom(r,2)>0`, and it has fixed degree.  The last cross term in (1)
and the crude upper bound `F_W(x)<=W(S)x^{r-2}` give

\[
 \log W_d=\frac{(p+q)\ell}{2}d^2+O_S(d).           \tag{4}
\]

For completeness, unrolling the last recurrence writes `W_d` as a sum of
`d` cross terms multiplied by residual powers of `r`, plus `r^dW_0`.
The logarithm of the term born at level `t` is at most

\[
 \frac{(p+q)\ell}{2}t^2+O_S(t)+(d-t)\ell.
\]

The maximum is at `t=d-O_S(1)` and the extra logarithm of the number of terms
is `O(log d)`.  This justifies the sentence in the draft that unrolling costs
only `O_S(d)`.

Dividing (4) by `(d ell)^2` gives the exact native-size coefficient

\[
 \rho(S)=\frac{a+b-2}{2\log r}.                    \tag{5}
\]

The cap--cup theorem gives

\[
 r\leq {a+b-2\choose a-1}\leq2^{a+b-2},           \tag{6}
\]

so every fixed template has `rho(S)>=1/2`.

## 2. Arbitrary `N` and the quantifiers

Fix the template `S` first.  For a requested `N`, take

\[
 d=\lceil\log_rN\rceil,
 \qquad N\leq r^d<rN,
\]

and retain any `N` points of `Q_d`.  Every convex subset of the retained set
was already a convex subset of `Q_d`, so

\[
 f(N)\leq W_d+1.
\]

Since `d ell=log N+O_S(1)`, (4) proves

\[
 \limsup_{N\to\infty}\frac{\log f(N)}{(\log N)^2}
 \leq\rho(S).                                      \tag{7}
\]

Now use the balanced template

\[
 r_k={2k-4\choose k-2},\qquad a_k=b_k=k-1.
\]

For **every fixed** `k`, the same global limsup in (7) is bounded by

\[
 \rho_k=\frac{k-2}{\log {2k-4\choose k-2}}.
\]

It follows that it is bounded by `inf_k rho_k`.  Stirling gives
`rho_k -> 1/2`.  Thus the proof never needs a nonuniform choice `k=k(N)`;
the order of limits in the draft is valid.

## 3. A nonstationary homogeneous-template barrier

The fixed-template barrier extends substantially.  Let `S_t` be an arbitrary
template of size `r_t`, largest cap `a_t`, and largest cup `b_t`, and form

\[
 Q_t=S_t[Q_{t-1}].
\]

Put

\[
 \ell_t=\log r_t,\quad
 L_t=\log|Q_t|=\sum_{i\leq t}\ell_i,\quad
 \sigma_t=a_t+b_t-2.
\]

No upper estimates and no control of the template coefficients are needed
for the following lower bound.  The leading monomials in the cap and cup
polynomials imply

\[
\begin{aligned}
 \log C_{d-1}&\geq\sum_{t<d}(a_t-1)L_{t-1},\\
 \log U_{d-1}&\geq\sum_{t<d}(b_t-1)L_{t-1}.
\end{aligned}
\]

The two-point macro-subsets at level `d` give
`W_d>=C_{d-1}U_{d-1}`.  Hence

\[
 \log W_d\geq\sum_{t<d}\sigma_tL_{t-1}.            \tag{8}
\]

By the cap--cup theorem, `sigma_t>=ell_t`.  Consequently

\[
\begin{aligned}
 \log W_d
 &\geq\sum_{t<d}\ell_tL_{t-1}\\
 &=\frac12\left(L_{d-1}^2-\sum_{t<d}\ell_t^2\right). \tag{9}
\end{aligned}
\]

This proves:

> **Small-step barrier.** If
> `max_{t<=d} ell_t=o(L_d)`, then
> \[
> \liminf_{d\to\infty}\frac{\log W(Q_d)}{L_d^2}\geq\frac12.
> \]

Indeed, `sum ell_t^2 <= (max ell_t) sum ell_t=o(L_d^2)` and
`L_{d-1}/L_d->1`.  The condition includes:

- one fixed template;
- any periodic schedule;
- arbitrary schedules from a finite menu;
- template sizes growing subexponentially relative to the accumulated size;
- slowly varying balanced Pascal or Baek--Balko templates, when they are used
  homogeneously at each level.

Vertical lexicographic composition is associative at the order-type level.
Thus a periodic schedule can alternatively be grouped into one composite
template and reduced directly to (5).

The hypothesis is real.  If some `ell_d` is comparable to `L_d`, the square
sum in (9) is macroscopic.  Such a schedule imports a new, rapidly growing
primitive template at those levels; controlling its full cap/cup/convex
profile is exactly the remaining loophole, rather than a failure of the
fixed-template proof.

There is a quantitative version of this dichotomy.  If
`Delta_d=max_{t<=d}ell_t` and `delta_d=Delta_d/L_d<1/2`, then (9) implies

\[
 \frac{\log W_d}{L_d^2}
 \geq\frac12(1-\delta_d)(1-2\delta_d).             \tag{9a}
\]

Thus beating `1/2` by a fixed `epsilon` through native nonstationary iterates
requires `delta_d=Omega(epsilon)` infinitely often: some newly introduced
template must contain a fixed power of all points present after that level.
This rules out a hidden improvement coming from gentle parameter tuning.

## 4. Polynomial random thinning does not improve a fixed template

Introduce weighted partition functions

\[
 C_d(z)=\sum_jc_j(Q_d)z^j,
 \quad U_d(z)=\sum_ju_j(Q_d)z^j,
 \quad W_d(z)=\sum_jv_j(Q_d)z^j.
\]

The same exact decomposition gives

\[
\begin{aligned}
 C_d(z)&=C_{d-1}(z)F_C(r^{d-1}z),\\
 U_d(z)&=U_{d-1}(z)F_U(r^{d-1}z),                 \tag{10}\\
 W_d(z)&=rW_{d-1}(z)+C_{d-1}(z)U_{d-1}(z)
                         F_W(r^{d-1}z).
\end{aligned}
\]

Take `z=r^{-delta d}` for fixed `0<=delta<1`.  Factors with
`t<=delta d+O(1)` have bounded arguments, while later factors contribute
their leading degrees.  The same two-sided argument as above yields

\[
 \log W_d(z)=
 \frac{(p+q)\ell}{2}(1-\delta)^2d^2+O_S(d).       \tag{11}
\]

A uniformly random subset of size
`n=N_d^{1-delta+o(1)}` contains an expected

\[
 \sum_jv_j(Q_d)\frac{(n)_j}{(N_d)_j}
\]

convex subsets.  The largest convex subset of `Q_d` has size `O_S(d)`, and
uniformly for those `j`,

\[
 \frac{(n)_j}{(N_d)_j}=z^j\exp(o(1)).
\]

Thus the first-moment thinning calculation has the same coefficient
`rho(S)` after normalization by `(log n)^2`; the factor `(1-delta)^2`
cancels.  Random polynomial thinning does not beat `1/2`.  This does not
exclude a highly structured exceptional subset, which would constitute a
new construction rather than the routine thinning argument.

## 5. Exact heterogeneous formula and the Baek--Balko loophole

Let a macro set `S=(s_1,...,s_r)` be vertically blown up by possibly
different clusters `Q_i`, of sizes `n_i`.  The same four orientation rules
give exact nonempty totals

\[
 C(P)=\sum_{\substack{B\subseteq S\\B\text{ a cap}}}
 C(Q_{\min B})\prod_{j\in B\setminus\{\min B\}}n_j,             \tag{12}
\]

\[
 U(P)=\sum_{\substack{B\subseteq S\\B\text{ a cup}}}
 U(Q_{\max B})\prod_{j\in B\setminus\{\max B\}}n_j,           \tag{13}
\]

and

\[
\begin{split}
 W(P)={}&\sum_iW(Q_i)\\
 &+\sum_{\substack{B\subseteq S\text{ convex}\\|B|\geq2}}
 C(Q_{\min B})U(Q_{\max B})
 \prod_{j\in B\setminus\{\min B,\max B\}}n_j.                 \tag{14}
\end{split}
\]

In particular, the unavoidable two-block contribution is

\[
 W(P)\geq\sum_iW(Q_i)+\sum_{i<j}C(Q_i)U(Q_j).       \tag{15}
\]

Baek and Balko's `(X,Y)`-blow-up is a heterogeneous almost-vertical
composition of this form.  Their constraints control cluster sizes and the
maximum allowable left/right chain lengths; their objective maximizes only
the total number of points.  It does **not** determine any of the weighted
quantities in (12)--(14).  Therefore their size theorem by itself provides
no coefficient below `1/2` for Erdős 838.

Formula (15) also identifies the only plausible advantage of heterogeneous
clusters: put cup-heavy clusters on the left and cap-heavy clusters on the
right, suppressing the forward products `C(Q_i)U(Q_j)`.  The reverse products
do not occur.  This is the same anti-alignment obstruction visible in the
binary strong-glue recurrence

\[
 W(A\prec B)=W(A)+W(B)+C(A)U(B).
\]

A barrier for unrestricted Baek--Balko blow-ups would therefore require a
new weighted cap/cup alignment theorem.  Maximum cap and cup sizes alone are
insufficient for the argument.  I do not see a valid reduction of this
heterogeneous case to (6), and I found no parameter schedule giving a
certified coefficient below `1/2`.

## 6. Exact finite probes

`nonstationary_probe.py` generates full cap, cup, and convex cardinality
profiles of central Pascal cells by exact integer recurrences and composes
different cells in arbitrary order.  Representative results are:

| macro sequence | log2 final size | log2 W / (log2 size)^2 |
|---|---:|---:|
| `2,4,8,16,32,64` | 113.197569 | 0.574369847 |
| `64,32,16,8,4,2` | 113.197569 | 0.618604776 |
| `4,16,64` | 76.905304 | 0.604234300 |

The order matters substantially, confirming that the nonstationary question
is not cosmetic.  None of these aggressive growing-template schedules beats
`1/2`; increasing macro sizes from inside to outside performs better than the
reverse order in this sample.

Reproduce with

```sh
python3 phase2/loop/erdos838/agent_asymptotic/nonstationary_probe.py
```

## 7. Recommended repairs and next construction experiment

The theorem itself needs no repair.  Two presentation improvements would
make it harder to misread:

1. replace the informal unrolling sentence after equation (5) by the explicit
   cross-term bound given in Section 1 above;
2. state explicitly that `k` is fixed before taking the limsup in `N`, and
   only afterward is `k` sent to infinity.

For a serious attempt below `1/2`, implement (12)--(14) as a weighted dynamic
program over Baek--Balko's integer variables `(x_i,y_i)`, retaining Pareto
states for `(size,C,U,W)` rather than maximizing size alone.  The search must
allow cap/cup anti-alignment and rapidly growing outer templates; stationary,
periodic, finite-menu, slow-growth, and routine random-thinning variants are
already blocked by the arguments above.
