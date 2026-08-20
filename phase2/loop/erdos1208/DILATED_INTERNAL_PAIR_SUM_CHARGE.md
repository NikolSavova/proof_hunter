# A dilated internal pair-sum charge

> **Status (2026-08-19): disproved.**  Estimate (1.5) is false for genuine
> integral distance-Sidon sets of polynomial height.  The two resonant
> Golomb-ruler arms in `GAUSSIAN_EDGE_VECTOR_TWO_ARM_BARRIER.md` compress
> `Omega(s^4)` records into `O(s^2)` vector keys and force energy
> `Omega(s^6)`.  The identities and projection-sparse branch below remain
> correct, but the global charge is closed as a solution route.

## 1. Outcome

Let `A subset Z^2` be distance-Sidon, `|A|=k`, and suppose that both
coordinate widths of `A` are at most `m`.  Put

\[
 \Sigma=A\mathbin{\oplus}A
 =\{c+d:\{c,d\}\in\tbinom A2\},
 \qquad N=|\Sigma|=\binom k2.                   \tag{1.1}
\]

For a realized directed difference `q=a-b`, let `H_q subset Sigma` be the
set of pair sums `s=c+d` for which

\[
 s+q=e+f                                           \tag{1.2}
\]

is another unordered pair sum and the six points `a,b,c,d,e,f` are
distinct.  Thus `|H_q|=h_6(q)` in
`INTERNAL_SHIFT_PAIR_SUM_GATE.md`.

Write `J(x,y)=(-y,x)` and fix

\[
 \Lambda=3(I+J).
\]

The charge

\[
 \Psi_q:H_q\times\Sigma\longrightarrow\mathbb Z^2,
 \qquad \Psi_q(s,t)=s+\Lambda t                 \tag{1.3}
\]

has `h_6(q) binom(k,2)` records but only `O(m^2)` possible keys.  Its exact
collision energy is

\[
 \boxed{
 \mathcal E_q
 =\sum_{w\in\mathbb Z^2}
    r_{\Sigma-\Sigma}(w)r_{H_q-H_q}(-\Lambda w).} \tag{1.4}
\]

The `w=0` contribution is exactly `N|H_q|`.  Consequently the single
resonance theorem

\[
 \boxed{
 \sum_{w\ne0}r_{\Sigma-\Sigma}(w)
                  r_{H_q-H_q}(-\Lambda w)
 \le k^{o(1)}N|H_q|}                              \tag{1.5}
\]

for every `q in (A-A)^*` would imply

\[
 h_6(q)\le k^{o(1)}{m^2\over k^2},               \tag{1.6}
\]

and hence the full `k<=m^(2/3+o(1))` square-grid upper bound in Erdos
problem 1208.

Estimate (1.5) is unproved.  The value of the reduction is that its
off-diagonal mass is a single coupled dilation resonance between two
uniquely represented pair-sum sets.  It eliminates the forced star before
forming the charge and has much smaller exact loads than the undilated
pair-sum translate on every stored stress.

## 2. Proof of the exact formula and implication

For a finite set `X`, write

\[
 r_{X-X}(z)=|\{(x,x')\in X^2:x-x'=z\}|.
\]

Two records have the same charge precisely when

\[
 s+\Lambda t=s'+\Lambda t',
\]

or, on putting `w=t-t'`,

\[
 s-s'=-\Lambda w.                                \tag{2.1}
\]

Summing independently over the representations of `w` in `Sigma-Sigma`
and of `-Lambda w` in `H_q-H_q` proves (1.4).  Since

\[
 r_{\Sigma-\Sigma}(0)=N,
 \qquad r_{H_q-H_q}(0)=|H_q|,
\]

the diagonal term is exactly `N|H_q|`.

If the coordinate widths of `A` are at most `m`, those of `Sigma` are at
most `2m`.  Each coordinate of `Lambda t` has width at most `12m`, so the
image in (1.3) has at most `(14m+1)^2` keys.  Cauchy--Schwarz and (1.5)
give

\[
 (N|H_q|)^2
 \le |\Psi_q(H_q\times\Sigma)|\mathcal E_q
 \le (14m+1)^2 k^{o(1)}N|H_q|.                  \tag{2.2}
\]

Canceling `N|H_q|` proves (1.6).  The exact identity

\[
 C_6(A)=4\sum_{q\in(A-A)^*}h_6(q)
\]

then gives `C_6(A)<=k^(o(1))m^2`; the repeated-label part of third energy is
`O(k^3)`, and origin localization completes the cube-root deduction.

## 3. Resonance-free branch

Formula (1.4) immediately proves the following exact branch.

**Proposition 3.1.**  If

\[
 \{w\in\Sigma-\Sigma:\Lambda w\in H_q-H_q\}
 =\{0\},                                         \tag{3.1}
\]

then `Psi_q` is injective and

\[
 |H_q|\binom k2\le(14m+1)^2.                    \tag{3.2}
\]

More generally, the left side of (1.5) is exactly the obstruction to
injectivity; there is no loss from Hölder, a maximum-fibre estimate, or an
unweighted inverse theorem.

For an affine presentation `A=T A_0`, (3.1) can be checked in the base
lattice by replacing `Lambda` with `T^(-1)Lambda T`.  Generic affine
distance-separating images have a thin conjugate resonance lattice, which
explains the exact finite-field profiles below.  The hard square-grid branch
has `T=I` and a fully integral resonance map, so Proposition 3.1 does not
dispose of the central case.

## 4. Exact stress profiles

The companion verifier chooses the largest clean internal-shift fibre in
each family and reports

\[
 (k,m,q,|H_q|,N,N|H_q|,|\operatorname{im}\Psi_q|,
   \mathcal E_q,\max\nu_q).
\]

The exact profiles are

\[
\begin{array}{c|r|r|r|r|r}
\text{family}&|H_q|&N|H_q|&|\operatorname{im}\Psi_q|
 &\mathcal E_q&\max\nu_q\\ \hline
\text{closure }30&14&6090&6075&6120&2\\
\text{closure }40&23&17940&17836&18148&2\\
\text{closure }80&63&199080&197022&203248&3\\
\text{closure }120&127&906780&891299&938304&4\\
\text{source }45&22&21780&21573&22200&3\\
\text{perpendicular ruler }40&14&10920&10920&10920&1\\
\text{Costas }22&34&7854&7818&7926&2\\
\text{parabola image }43&171&154413&153120&156999&2
\end{array}                                      \tag{4.1}
\]

Thus the largest normalized energy in the table is

\[
 {938304\over906780}=1.034764\ldots,
\]

on the 120-point closure.  The transformed finite-field parabola, which is
the main ordinary-third-energy obstruction, has normalized energy only
`1.0167...`.  These are falsification data, not a proof of (1.5), and no
claim is made that the constant dilation `3(I+J)` is canonical or optimal.

Run

```text
python3 phase2/loop/erdos1208/verify_dilated_internal_pair_sum_charge.py
```

The verifier uses exact integer arithmetic, checks distance-Sidonicity,
constructs every clean common-centroid record, and recomputes the charge
energies directly.

## 5. Restart target

Prove (1.5).  A proof may choose another fixed nonsingular integral
dilation if useful, since only the absolute constant in the `(14m+1)^2`
box changes.  What cannot be discarded is the coupling: the same `w` must
simultaneously be a difference of two pair sums and, after dilation, a
difference of two starts in one clean internal fibre.  The undilated
autocorrelation and a maximum-load bound both retain known polynomial
obstructions.
