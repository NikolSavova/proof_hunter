# P1d concentrated-pocket replacement: exact gain ledger and all-delete barrier

## 1. Status

This note audits one concrete attempt to prove the positive-rank-interval
condition P1d.  The attempted operation is attractive because its arithmetic
has abundant room: replace part of a rank-$r$ source face by a rich convex
face in one tangent pocket.  The arithmetic is correct.  The required planar
merge lemma is false, even when all pocket points enter through one exposed
source edge.

This is therefore a **barrier**, not a new residual target.  The surviving
all-delete state is the rooted-pocket Hall state already isolated elsewhere
in the campaign.

## 2. The exact coefficient ledger

Use the canonical P1 scale

\[
        N=4^k,
        \qquad r=\alpha k,
        \qquad d=\delta k,
        \qquad 0\leq \delta\leq\alpha.
\]

Suppose a rank-$r$ source bank has the binomial-scale exponent

\[
        \log_2 M=(2\alpha-\alpha^2+o(1))k^2.
\]

After deleting $d$ source labels, use a pocket face of rank
$s=(1-\alpha+\delta)k$.  The same binomial asymptotic gives the pocket
exponent

\[
        2\gamma-\gamma^2,
        \qquad \gamma=1-\alpha+\delta.
\]

If the deleted labels are the only decoder ambiguity, their choice costs at
most $2^{(2\delta+o(1))k^2}$.  The resulting normalized exponent is therefore

\[
\begin{aligned}
 E(\alpha,\delta)
   &=(2\alpha-\alpha^2)+(2\gamma-\gamma^2)-2\delta\\
   &=1+2\alpha-2\alpha^2-2(1-\alpha)\delta-\delta^2.
\end{aligned}
\tag{1}
\]

At the critical source rank $\alpha=1/2$, deleting only half the source
($\delta=1/4$) would give

\[
        E(1/2,1/4)=19/16>1.
\tag{2}
\]

Thus any positive mass of such records, with subexponential additional load,
would beat the coefficient-one fixed-size target.  In contrast, full deletion
$\delta=\alpha$ gives

\[
        E(\alpha,\alpha)=1-\alpha^2<1.
\tag{3}
\]

The difference is exactly the desired gain: the geometry must preserve a
nonempty, quantitatively large source trace.

## 3. Exact one-pocket counterexample

Take the following twelve rational (indeed integral) points, listed in
increasing $x$-order:

\[
\begin{array}{c|rrrrrrrrrrrr}
i&0&1&2&3&4&5&6&7&8&9&10&11\\ \hline
y_i&2926687&4112040&-8641570&-1312196&7155532&6305027&
3587334&177486&5991940&2014143&9575052&-2670279.
\end{array}
\tag{4}
\]

Let

\[
        A=\{0,1,2,4\},
        \qquad Q=\{8,9,10,11\}.
\]

The verifier checks all $\binom{12}{3}$ determinants are nonzero and proves:

1. $A$ is convex, with cyclic hull order $(0,2,4,1)$;
2. $Q$ is convex;
3. for every $q\in Q$, $A\cup\{q\}$ is convex and $q$ is inserted between
   the same consecutive hull vertices $2,4$ of $A$;
4. for every nonempty $S\subseteq A$, the union $S\cup Q$ is nonconvex.

Thus all four pocket labels are individually addable through one literal
tangent pocket, but release of the whole pocket requires deleting **all** of
the source.  The failure is hereditary and already occurs before any decoder
or history collision is considered.

This finite witness is not offered as an asymptotic low-face construction.
Its role is to refute the universal local implication

\[
 \text{one concentrated addable pocket}
 \quad\Longrightarrow\quad
 \text{a rich pocket face merges after deleting at most }r/2.
\tag{5}
\]

The scalable universal-dominance cages elsewhere in the bank show that the
same all-delete sign pattern is structurally stable.  Their detached Boolean
banks explain why this local obstruction is not itself a counterexample to
the half lower bound.

## 4. Consequence for P1d

The audit separates the arithmetic from the geometry cleanly:

- a bounded-deletion replacement theorem would have more than enough
  exponent, by (1)--(2);
- even the strongest one-edge pocket localization does not imply such a
  theorem;
- the only unconditional local output can be the pocket face itself, after
  complete deletion of the source, and (3) loses the desired exponent.

Therefore the concentrated branch of P1d cannot be closed by improving the
local deletion fraction.  It must instead pool many all-delete records into
ordinary faces with a globally bounded recovery fibre, or use a genuinely
minimizer-specific mutation/profile inequality that rules out the stationary
all-delete state.  Those are the already recorded rooted-pocket Hall and
multi-point minimizer gates; this note does not rename either one.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/verify_p1d_concentrated_pocket_replacement_barrier.py
```

The script verifies general position, both convex faces, common-edge
insertion, all fifteen nonempty source traces, and the exact exponent ledger.
