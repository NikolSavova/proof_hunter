# Adversarial audit of `NEXT_ENDPOINT_ATTACK.md`

Date: 2026-08-13. All logarithms are base two.

## Verdict

**The claimed theorem is valid (as an asymptotic theorem).** I independently
reconstructed the endpoint recurrences, the reset iteration, and the
heavy-path dichotomy. I found no quantifier, orientation, nesting, or
stopping-time gap that affects the result

\[
 \log M(T)\ge \tfrac12(\log n)^2-O((\log n)^{3/2})
\]

for every ordered strong-decomposition tree.

There are three presentation repairs worth making before this is treated as
a polished proof:

1. The proof of `X<=nM` and `Y<=nM` omits the singleton endpoint family in
   its prose. One must write `X=1+sum_t c(s,t)` and use the auxiliary
   convention `M=max(1,M_actual)`.
2. The theorem should explicitly start with sufficiently large `L`. This is
   needed so that the stopping threshold is above one, `Delta<L`, and the
   displayed `F` is useful. All smaller `n` are absorbed into the absolute
   constant in the `O` term.
3. `endpoint_reset_certificate.py` checks only the first-reset inequalities
   on integer log-states. It is a useful arithmetic smoke test, not a
   certificate of the nesting and heavy-path portions of the theorem.

None is a mathematical failure of the asymptotic argument.

## 1. Exact endpoint conventions and recurrences

For a fixed left endpoint `s`, let `x(s)` count caps with left endpoint `s`,
including the singleton `{s}`. Define `y(t)` symmetrically for cups with
right endpoint `t`, and put

\[
 X=\max_s x(s),\qquad Y=\max_t y(t),\qquad
 M=\max\left(1,\max_{s<t}c(s,t)u(s,t)\right).
\]

At a leaf, `(X,Y,M)=(1,1,1)`. At `T=A prec B`, with sizes `a,b`, the
auxiliary `M` obeys the exact same recurrence as the actual endpoint
maximum:

\[
\begin{aligned}
X_T&=\max((b+1)X_A,X_B),\\
Y_T&=\max(Y_A,(a+1)Y_B),\\
M_T&=\max(M_A,M_B,X_AY_B).
\end{aligned}
\]

The last claim remains exact with the auxiliary ones because the crossing
term `X_A Y_B` is at least one. In particular, `M(S)<=M(T)` for every
subtree `S` of `T`, and both `X` and `Y` are nondecreasing on moving from a
child to its parent, regardless of which side the child occupies.

For the fixed endpoint attaining `X`, the exact partition is

\[
 x(s)=1+\sum_{t>s}c(s,t).
\]

The two-point cup on `(s,t)` gives `u(s,t)>=1`, so every summand is at most
`M`. Hence

\[
 X\le 1+(n-1)M\le nM,
\]

and symmetrically `Y<=nM`. This supplies the coordinate ceiling used in the
reset argument: if `mu=log M(T)`, then for every subtree `S`,

\[
 x(S),y(S)\le \mu+L,\qquad L=\log n.
\]

The endpoint decomposition of a convex subset also gives

\[
 W=n+\sum_{s<t}c(s,t)u(s,t),
\]

and therefore `M<=W<=n+n^2M<=2n^2M`. Thus a pure-comb lower bound on `W`
can legitimately be converted back to one on `M` with loss at most
`2L+1`.

Finally, the already proved cap--cup product estimate

\[
 \log C(S)+\log U(S)\ge \tfrac12(\log |S|)^2-\log |S|
\]

together with `C<=|S|X` and `U<=|S|Y` gives exactly

\[
 x(S)+y(S)\ge \tfrac12(\log |S|)^2-3\log |S|.
\]

## 2. Independent reconstruction of the reset

Fix the root value `mu=log M(T)`. Suppose both children of a selected node
have radial sum at least `F` and all four coordinates are at most `mu+L`.
Put

\[
 D=F-\mu,\qquad \ell=D-L.
\]

Every coordinate is at least `ell`: for example
`x>=F-y>=F-(mu+L)=ell`. The forward crossing term at every node of `T` is
one of the candidates in the root maximum `M(T)`, so at a node `A prec B`

\[
 x_A+y_B\le\mu.
\]

Consequently

\[
 x_B\ge F-y_B\ge F-(\mu-x_A)\ge D+\ell=2D-L,
\]

and symmetrically `y_A>=2D-L`. The selected parent therefore has both
coordinates at least

\[
 h_0=2D-L.
\]

Now pass to a later selected ancestor. Let `H` be the child containing the
previous selected node and `Q` the other child. The accumulated coordinates
created below are present in `H` by coordinatewise monotonicity through all
intermediate nodes.

* If `H` is the left child, the paid cross gives `x_H+y_Q<=mu`. Since
  `x_Q+y_Q>=F`, one has `x_Q>=D+x_H`. The parent therefore has its
  `x`-coordinate increased by at least `D`, while its `y`-coordinate is not
  decreased.
* If `H` is the right child, the cross is `x_Q+y_H<=mu`. The reflected
  argument gives `y_Q>=D+y_H`; the parent's `y` increases by at least `D`
  while `x` is not decreased.

This explicitly checks the potentially delicate orientation point. Events
of the other orientation cannot erase increments already accumulated in a
coordinate. Therefore, on the `q`-th occurrence of one orientation, the
coordinate of `H` appearing in that forward cross is at least
`h_0+(q-1)D`, while the required coordinate of `Q` is at least `ell`. The
root maximum hence satisfies

\[
 \mu\ge h_0+(q-1)D+\ell=(q+2)D-2L.
\]

Substitution of `D=F-mu` gives

\[
 \mu\ge \frac{q+2}{q+3}F-\frac{2L}{q+3}.
\]

Thus the repeated-reset inequality survives arbitrary intermediate nodes
and arbitrary interleaving of the two attachment orientations.

## 3. Heavy-path dichotomy

Let `R=ceil(sqrt(L))` and follow a larger child until the first current size
below `n/2^(4R)`. At a level with discarded-sibling proportion `z`, the log
size loss is `-log(1-z)`. A large level has `z>=1/L^2`; every level loses at
most one bit because the followed child is a larger child. At a nonlarge
level, for large `L`,

\[
 -\log(1-z)\le 2z<2/L^2.
\]

If fewer than `R` levels are large and `N_0` is the number of nonlarge
levels before the stop, then

\[
 4R<R+2N_0/L^2,
\]

so `N_0>(3/2)RL^2`. At least `N_0/2` discarded siblings occur on the same
side of the path. Fix one leaf in each such sibling and one terminal leaf.
If these are right siblings, choosing or omitting each fixed leaf is exactly
the iterative cap extension represented by the factor `(b+1)` in the `X`
recurrence. If they are left siblings, it is the reflected cup extension in
the `Y` recurrence. Hence all `2^(N_0/2)` choices are distinct convex
subsets. This verifies both the cap/cup orientation and the exponent in the
pure-comb branch.

If at least `R` levels are large, every child of each selected large node
has size at least

\[
 2^{L-\Delta},\qquad
 \Delta=4R+2\log L+1.
\]

The followed child has size at least `n_i/2`, and the sibling at least
`n_i/L^2`, while every pre-stop `n_i>=n/2^(4R)`. Thus both children at each
of `R` nested selected nodes have radial sum at least

\[
 F=\tfrac12(L-\Delta)^2-3L.
\]

The deepest selected node gives the first reset. At each higher selected
node, the child containing it carries the accumulated state. Among the
remaining `R-1` nodes, one orientation occurs at least
`q=ceil((R-1)/2)` times, exactly as required by the reset lemma.

The case split is exhaustive. If `mu>=F-L`, the desired estimate is
immediate. Otherwise `D=F-mu>L`, so in particular `ell>0`, and the reset
calculation applies without a sign issue.

## 4. Explicit asymptotic constant

The note only needs big-O, but an explicit coarse form confirms all
quantifiers. For `L>=128`,

\[
 \Delta\le 8\sqrt L<L,
 \qquad
 0\le F\le \tfrac12L^2,
 \qquad
 F\ge \tfrac12L^2-8L^{3/2}.
\]

Also `q+3>=sqrt(L)/2`. Thus the immediate alternative gives

\[
 \mu\ge F-L\ge \tfrac12L^2-9L^{3/2},
\]

while the reset alternative gives, coarsely,

\[
 \mu\ge F-\frac{F+2L}{q+3}
 \ge \tfrac12L^2-10L^{3/2}.
\]

The pure-comb branch is much stronger. Enlarging the constant absorbs the
finitely many `L<128`. Therefore the proof can, if desired, state the
fully quantified conclusion

\[
 \log M(T)\ge \tfrac12(\log n)^2-C(\log n)^{3/2}
\]

for an absolute `C` (the above calculation makes `C=10` work for the
large-`L` portion).

## 5. Certificate audit

I ran

```text
python3 endpoint_reset_certificate.py --box 12 --logs 100 400 1000 10000
```

It exhaustively accepted 24,578 admissible integer states in that box. The
reported normalized deficits `(.5L^2-lower)/L^(3/2)` at the four log sizes
were approximately `4.37, 4.89, 5.05, 5.08`, consistent with the symbolic
bound.

The script does not encode tree states, repeated orientations, the
heavy-path stopping argument, or real-valued exhaustive states. Its value is
therefore limited to catching algebra/sign mistakes in the first reset and
printing the chosen asymptotic formula. The proof above, rather than the
script, certifies the theorem.

