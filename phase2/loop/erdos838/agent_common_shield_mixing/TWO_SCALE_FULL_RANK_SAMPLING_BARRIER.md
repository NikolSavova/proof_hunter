# Two-scale full-rank sampling: the sharp recurrence and its `1/4` fixed point

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

Using the full large-rank portion of every random restriction does not
improve the unconditional coefficient `1/4` with the currently proved
inputs.  The exact hypergeometric lift gives a sharp recurrence.  If
`t=n^alpha` and every `t`-point restriction has

\[
       2^{(c-o(1))(\log t)^2}
\]

faces in ranks at least `lambda log t`, then

\[
 \boxed{
 \log V(P)\ge
 [c\alpha^2+\lambda\alpha(1-\alpha)-o(1)](\log n)^2.}  \tag{1}
\]

At the live value `c=1/4`, optimizing (1) beats `1/4` **if and only if**

\[
                              \lambda>{1\over2}.         \tag{2}
\]

For `lambda>1/2`, the exact optimized coefficient and gain are

\[
 \Phi(\lambda)={\lambda^2\over4(\lambda-1/4)},\qquad
 \Phi(\lambda)-{1\over4}
 ={(\lambda-1/2)^2\over4(\lambda-1/4)}.                 \tag{3}
\]

No established universal theorem supplies a quadratic-size face portion
above `(1/2+delta)log t`.  The total-count/entropy argument supplies mean
rank only `(1/4-o(1))log t`; the hard rank-width theorem concentrates a
constant-density slice near that mean rather than moving it; and optimized
hull activity supplies exterior labels, most of which may be blocked and
therefore do not raise rank.

The full Erdős--Szekeres rank profile is an exact fixed point, not merely a
one-witness artefact.  At internal rank `k=theta log t`, its exponent after
lifting is

\[
 \alpha^2\theta(1-\theta)
 +\alpha(1-\alpha)\theta
 =y(1-y),\qquad y=\alpha\theta.                         \tag{4}
\]

Summing all `O(log n)` guaranteed ranks changes only a subquadratic term;
the maximum of (4) is exactly `1/4`.

There is an exact coherent barrier to every recurrence using only total
mass, mean/width, downward closure, and the proved exterior-supply scalar
inequality: complete logarithmic rank truncations.  They are not planar for
rank at least four, and that distinction is load-bearing.  Producing an
actual planar family with coefficient `1/4` would resolve the open upper-gap
problem, so no such realizable extremal barrier is claimed.  What is proved
is that the proposed sampling recursion cannot exploit planarity until one
adds a quantitative planar rank-repair theorem ruling out this shelf.

Thus this bounded attack yields no epsilon improvement.  It isolates the
exact sufficient new input:

> a fixed `delta>0` and a quadratic-exponent portion of the restriction
> face family at ranks at least `(1/2+delta)log t`, or an equivalent product
> bank which contributes the gain in (3) after overlap.

## 1. Exact rank-resolved restriction identity

Let `v_k(P)` be the number of ordinary rank-`k` faces.  Choose a uniformly
random `t`-subset `T` of an `n`-point configuration and put

\[
 a_k=\mathbb E_T v_k(P[T]).                              \tag{5}
\]

A fixed rank-`k` face is contained in `T` with probability

\[
 \pi_{n,t}(k)={\binom{n-k}{t-k}\over\binom nt}
              ={\binom tk\over\binom nk}.               \tag{6}
\]

Therefore, writing `V_{<=t}(P)=sum_(k<=t)v_k(P)`,

\[
 \boxed{a_k=v_k(P)\pi_{n,t}(k),\qquad
 V(P)\ge V_{\le t}(P)=
 \sum_{k\le t}{a_k\over\pi_{n,t}(k)}.}                \tag{7}
\]

Equation (7) is the sharp two-scale recurrence.  It retains the complete
visible rank distribution; no choice of one Erdős--Szekeres witness has
been made.  The inequality only discards ambient ranks above `t`, none of
which are used in the logarithmic-rank arguments below.
Since

\[
 {1\over\pi_{n,t}(k)}={\binom nk\over\binom tk}
 \ge(n/t)^k,                                             \tag{8}
\]

if `sum_(k>=q)a_k>=H`, then

\[
                         V(P)\ge H(n/t)^q.               \tag{9}
\]

Take `t=n^(alpha+o(1))`,
`q=(lambda+o(1))log t`, and
`H=2^((c-o(1))(log t)^2)`.  Substitution proves (1).

There is also a profile form.  Suppose that at internal relative rank
`x=k/log t` the expected restriction count has exponent

\[
                         \log a_k\ge
             (g(x)-o(1))(\log t)^2.                     \tag{10}
\]

Then (7)--(8) give

\[
 \boxed{
 {\log V(P)\over(\log n)^2}
 \ge\sup_x\{\alpha^2g(x)+\alpha(1-\alpha)x\}-o(1).}    \tag{11}
\]

Only `O(log n)` ranks are relevant to all presently guaranteed profiles,
so replacing the supremum by their sum cannot change the leading
coefficient.

## 2. Optimization of a large-rank portion

Put

\[
 R_{c,\lambda}(\alpha)
 =c\alpha^2+\lambda\alpha(1-\alpha)
 =\lambda\alpha-(\lambda-c)\alpha^2.                   \tag{12}
\]

If `lambda<=2c`, the maximum on `0<alpha<=1` is attained at `alpha=1` and
equals `c`.  If `lambda>2c`, the maximizer is

\[
                 \alpha_*={\lambda\over2(\lambda-c)}<1,
 \qquad
 \max R_{c,\lambda}={\lambda^2\over4(\lambda-c)}.       \tag{13}

For `c=1/4`, equations (2)--(3) follow.  Note the strength of the required
input.  A tail beginning at `(1/4+delta)log t`, or even at
`(1/2-o(1))log t`, does not improve the coefficient.  It must cross one
half by a fixed amount.

More generally, if the tail itself has coefficient `g` rather than the
full `c`, its contribution is

\[
                         g\alpha^2+lambda\alpha(1-\alpha).        \tag{14}
\]

This is the exact objective against which any proposed large-rank theorem
should be measured.

## 3. The whole Erdős--Szekeres profile still telescopes

The modern threshold theorem and hereditary double counting give, for
every fixed `0<theta<1`,

\[
 \log v_{\theta\log t}(P[T])
 \ge[\theta(1-\theta)-o(1)](\log t)^2.                  \tag{15}

Insert `g(theta)=theta(1-theta)` into (11).  With
`y=alpha theta`,

\[
 \begin{aligned}
 &\alpha^2\theta(1-\theta)
       +\alpha(1-\alpha)\theta\\
 &\hspace{20mm}=\alpha\theta-\alpha^2\theta^2
 =y(1-y).                                               \tag{16}
 \end{aligned}

When `alpha>=1/2`, the available interval `0<y<alpha` contains `y=1/2`,
so the optimized coefficient is exactly `1/4`.  For `alpha<1/2`, it is
`alpha(1-alpha)<1/4`.  This proves that using every guaranteed rank at the
first scale, and summing them after lifting, still stops at `1/4`.

Repeated scales do not help.  If the final relative rank is `y`, every
intermediate containment factor telescopes to

\[
                     {\binom nk\over\binom{m_{final}}k},            \tag{17}
\]

so the same `y(1-y)` profile results.  This is an equality of binomial
coefficients, not an asymptotic loss.

## 4. Mean information gives exactly the same threshold

Let

\[
 A=\sum_ka_k,qquad \bar k={\sum_kka_k\over A}.          \tag{18}

The reciprocal containment factors in (7) are increasing and
log-convex in `k`.  Jensen, with linear interpolation between adjacent
integer ranks, gives

\[
                    V(P)\ge A(n/t)^{\bar k}.             \tag{19}

Thus if `A>=2^((c-o(1))(log t)^2)` and
`bar k>=(lambda-o(1))log t`, one recovers precisely (1).

Entropy subadditivity supplies only

\[
 \log V(P[T])\le
 \mu(T)\log{e t\over\mu(T)},                            \tag{20}

so the known coefficient-`c` lower bound implies

\[
                         \mu(T)\ge(c-o(1))\log t.        \tag{21}

At `c=1/4`, (21) is a factor two below the threshold (2).  The
restriction-peak curvature theorem does not raise it: it shows that at a
peak the half-weight and uniform means differ by at most one, while the
only unconditional lower edge remains `(1/4-o(1))log t`.

The hard rank-width theorem likewise does not help the recurrence.  It
produces a constant-density slice at

\[
                              r=\mu(T)+O(1),             \tag{22}

so in the worst allowed case it makes (19) nearly sharp at rank
`(1/4+o(1))log t`.

## 5. Downward closure and the coherent shelf barrier

There is a finite sharpness statement behind the shelf.  Fix `t`, a mass
`H`, and increasing nonnegative rank prices `b_0<=...<=b_t`.  Among all
vectors

\[
             0\le f_k\le\binom tk,\qquad \sum_k f_k=H,             \tag{23a}
\]

the minimum of `sum_k b_k f_k` is obtained by filling ranks from zero
upward: all levels below one cutoff are full, the cutoff level is partially
full, and all higher levels are empty.  Indeed, moving one unit from a
higher occupied rank to a lower unfilled rank cannot increase the
objective.  The minimizer is itself the profile of a downset (take every
lower level and any required number of cutoff sets).  Thus neither
fractional averaging over restrictions nor downward closure improves the
worst-case rank allocation supplied by total mass alone.

For the lift, `b_k=binom(n,k)/binom(t,k)` is increasing.  If
`log H=(c-o(1))(log t)^2`, the greedy cutoff is
`r=(c+o(1))log t`.  With `t=n^alpha`, its lifted leading exponent is

\[
 c\alpha^2+c\alpha(1-\alpha)=c\alpha.                 \tag{23b}
\]

This is weaker than invoking the coefficient-`c` theorem directly at
scale `n`.  Any recursive gain must therefore force mass above the greedy
cutoff, rather than merely retain all ranks.

For an `N`-element abstract ground set, let

\[
              \mathcal U_{N,r}=\{A\subseteq[N]:|A|\le r\}.         \tag{23}

This is hereditary, and every `t`-restriction has exact profile

\[
                    v_k(T)=\binom tk\quad(0\le k\le r).            \tag{24}

When `r=(c+o(1))log t` and `t` is polynomially large compared with `r`,
the top level dominates:

\[
 \log V(T)=(c+o(1))(\log t)^2,qquad
 \mu(T)=r-o(1),qquad \operatorname{Var}|A|=o(1).       \tag{25}

Using the **full** profile (24) in (7) gives exactly

\[
 \sum_{k=0}^r\binom tk{\binom nk\over\binom tk}
 =\sum_{k=0}^r\binom nk.                                \tag{26}

Thus every two-scale and multiscale sampling calculation on this coherent
shelf merely reconstructs the same truncation at the ambient scale.  For
`t=n^alpha` its leading coefficient is `c alpha`, agreeing with (1) at
`lambda=c`; no hidden full-profile gain exists.

The optimized hull-activity scalar bound is also consistent with the
shelf.  A rank-`r` family of size approximately `binom(t,r)` is permitted
average exterior supply `qbar=t-r`, because

\[
                  \Psi(r,t-r)=\log\binom tr+O(\log t).             \tag{27}

It is therefore possible at the level of every proved inequality for
almost all supplied exterior labels to be blocked.  Exterior supply becomes
a rank improvement only after an EIC/capped-Hall repair theorem, which is
exactly the still-open geometric gate.

The truncation (23) is not a planar affine convexity when `r>=4`.  If every
four-set were a face, planar Caratheodory would force every point to be
extreme and hence every subset to be a face.  This explains both the force
and the limitation of the barrier:

* it is an exact scalable countermodel to the sampling recurrence plus all
  present scalar rank/width/exterior inequalities; but
* ruling it out quantitatively for planar face complexes is essentially the
  missing rank-repair theorem, not something supplied by random sampling.

A realizable planar family with total coefficient `1/4` is not known; such
a construction would close the current lower/upper coefficient gap.  The
stationary strong-glue families provide a realizable calibration at
coefficient `1/2`: their exact weighted face enumerators retain coefficient
`1/2` under every polynomial thinning.  Hence the sampling operator itself
has no intrinsic coefficient gain even on scalable planar families, though
this calibration does not assert a planar `1/4` extremizer.

## 6. Why exterior supply does not change the recurrence yet

At a rank `r=rho log t` carrying a quadratic-exponent face family, optimized
hull activity gives the scale-correct lower bound

\[
                         \log qbar\gtrsim {\log V(T)\over r}.       \tag{28}

At the hard values `c=1/4`, `rho=1/4`, this can be linear in `t`: the shelf
has plenty of exterior labels.  But the exact identity is

\[
                              q(A)=u(A)+e(A),            \tag{29}

where only the addable labels `u(A)` create rank-`r+1` faces; `e(A)` are
blocked by rooted four-circuits.  The proved low-label tail deliberately
passes to the residual in which `e(A)` is large.  It does not turn those
labels into convex extensions.

Consequently exterior supply supplies no positive term in (11) without a
bounded-congestion repair or mixed-face bank.  Inserting `qbar` as though it
were `u` would be invalid; exact planar regressions with `q>u` are already
banked.  The conditional radial-product theorem can improve `1/4` to
`3/8`, but extraction of a positive-log-scale recoverable product from an
arbitrary dense cell is unproved.  It therefore cannot be entered into an
unconditional sampling recurrence.

## 7. Exact boundary for an epsilon improvement

The full-rank calculation leaves three quantitatively sufficient exits:

1. **High-rank mass:** for some fixed `delta>0`, every relevant
   `t`-restriction has `2^((1/4-o(1))(log t)^2)` faces at ranks at least
   `(1/2+delta)log t`.  Equation (3) gives an explicit epsilon.
2. **Profile excess:** a rank profile `g(x)` for which the supremum in (11)
   exceeds `1/4` at some `alpha<1`.
3. **Blocked-label product:** convert the exterior supply in (28) into
   `2^(Omega((log t)^2))` additional recoverable ordinary outputs with
   subquadratic overlap.

None is currently proved universally.  In particular, “use all large
faces in the random restriction” is not a fourth exit: equations (7),
(11), and (16) already do exactly that.

## 8. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_two_scale_full_rank_sampling.py
```

The checker performs five exact audits:

1. on the rational nine-point planar instance, it enumerates every face and
   every fixed-size restriction and verifies (5)--(7) rank by rank;
2. it checks the algebraic profile identity (16) on a dense rational grid
   and verifies the exact `1/4` maximum;
3. it verifies the threshold and gain formulas (2)--(3); and
4. it solves the finite capacity-constrained rank-allocation problem and
   checks the greedy low-rank optimum; and
5. on complete finite truncations it checks the full-rank identity (26),
   the two-scale and three-scale telescoping, and top-rank concentration.

The result is a rigorous no-gain theorem for the proposed recurrence and an
exact target for the missing planar input, not a claim that coefficient
`1/4` is optimal for planar point sets.
