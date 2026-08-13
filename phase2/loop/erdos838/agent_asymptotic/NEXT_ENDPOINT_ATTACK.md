# A multiscale reset proof of the max-endpoint one-turn theorem

All logarithms in this note are base two.  Let `T` be an ordered full
binary strong-decomposition tree, and put `n=|T|`, `L=log n`.  Recall the
exact max-plus quantities

\[
\begin{aligned}
 X_T&=\max\{(b+1)X_A,X_B\},\\
 Y_T&=\max\{Y_A,(a+1)Y_B\},\\
 M_T&=\max\{M_A,M_B,X_AY_B\}                     \tag{1}
\end{aligned}
\]

at `T=A prec B`; we use the harmless auxiliary convention `M>=1`.  Write
`x=log X`, `y=log Y`, and `m=log M`.

This note proves the following theorem.  It improves the previous `1/3`
stopping-time bound all the way to the sharp quadratic coefficient.  The
error obtained by this first implementation is `O(L^(3/2))`, rather than
the conjectured `O(L log L)`.

> **Theorem (weighted one-turn alignment).**  Every ordered full binary
> strong-decomposition tree with `n` leaves satisfies
> \[
>  \boxed{\quad
>  m(T)\ge {1\over2}(\log n)^2-O((\log n)^{3/2}).
>  \quad}                                          \tag{2}
> \]
> Consequently its number `W(T)` of nonempty convex subsets satisfies the
> same lower bound logarithmically.

The mechanism is a repeated endpoint **reset**.  One anti-aligned glue can
hide the forward product, but in doing so it makes both endpoint maxima of
the parent large.  At each later macroscopic attachment, one of those two
coordinates is used in the forward product and then increases by a fixed
amount.  Alternating attachment sides can split the increases between the
two coordinates, but cannot erase them.

## 1. Three elementary inputs

We use only the following already-audited consequences of (1).

First, the cap--cup product theorem and `C<=nX`, `U<=nY` give, for every
`s`-leaf subtree `S`,

\[
 x(S)+y(S)\ge {1\over2}(\log s)^2-3\log s.       \tag{3}
\]

Second, each fixed-left-endpoint cap family is partitioned by its right
endpoint: explicitly, `x(s)=1+sum_(t>s)c(s,t)`, where the one is the
singleton.  Since the two-point cup on the same endpoints is always
available, every summand is at most the actual endpoint product.  With the
auxiliary convention `M=max(1,M_actual)`, this gives

\[
 X(S)\le sM(S),\qquad Y(S)\le sM(S).             \tag{4}
\]

In particular, if `S` is a subtree of `T` and `mu=m(T)`, then

\[
 x(S),y(S)\le \mu+L.                              \tag{5}
\]

Third, both endpoint maxima are monotone on passing from a child to its
parent.  This is immediate from the first two recurrences in (1).

We will also use

\[
 M\le W\le n+n^2M\le 2n^2M,                     \tag{6}
\]

so that a lower bound on `log W` gives the same bound on `m`, with a loss
of at most `2L+1`.

## 2. A single reset

Here is the algebra which will be iterated.  Fix numbers `F,mu`, and suppose
both children `A,B` of a node satisfy

\[
 x_A+y_A\ge F,\quad x_B+y_B\ge F,
 \qquad x_A,y_A,x_B,y_B\le\mu+L.                 \tag{7}
\]

Put

\[
 D=F-\mu,qquad \ell=D-L.                        \tag{8}
\]

Then every coordinate in (7) is at least `ell`.  If the forward term at
this node is at most `2^mu`, then

\[
 x_A+y_B\le\mu.                                  \tag{9}
\]

Using (7)--(9),

\[
 x_B\ge F-y_B\ge F-(\mu-x_A)\ge D+\ell=2D-L,
\]

and symmetrically `y_A>=2D-L`.  Hence the parent `P` satisfies

\[
 \boxed{x_P,y_P\ge h_0:=2D-L.}                  \tag{10}
\]

This is the first reset: although the paid cross was small, the *reverse*
coordinates inherited by the parent are both large.

Now suppose a later ancestor glue has one child `H` containing `P` and an
opposite child `Q` satisfying the same bounds (7).  If `H` is the left
child, then

\[
 x_H+y_Q\le\mu,qquad
 x_Q\ge F-y_Q\ge F-\mu+x_H=D+x_H.               \tag{11}
\]

Thus the parent inherits `y_H` and has its `x`-coordinate increased by at
least `D`.  If `H` is the right child, the reflected statement holds: its
`y`-coordinate increases by at least `D`, while `x_H` persists.

At every such ancestor glue the coordinate of `H` used in the forward term
is paired with an opposite-child coordinate at least `ell`.  Therefore, if
one attachment direction has occurred `q` times after the first reset, its
`q`-th occurrence gives

\[
 \mu\ge h_0+(q-1)D+\ell=(q+2)D-2L.              \tag{12}
\]

Substituting `D=F-mu` yields the useful closed form

\[
 \boxed{\quad
 \mu\ge {q+2\over q+3}F-{2L\over q+3}.
 \quad}                                          \tag{13}
\]

No scalar local Bellman inequality is being asserted here.  Formula (13)
retains which coordinate was increased and amortizes the increases over a
nested sequence of glues.

## 3. Finding many reset nodes or many pure combs

Let

\[
 R=\lceil\sqrt L\rceil,qquad \lambda=\log L.    \tag{14}
\]

Starting at the root, repeatedly follow a larger child.  Write `s_i` for
the discarded sibling size and `n_i` for the current subtree size.  Stop at
the first `t` such that

\[
 n_t<n/2^{4R}.                                   \tag{15}
\]

Call a level **large** if

\[
 s_i\ge n_i/L^2.                                 \tag{16}
\]

If there are fewer than `R` large levels, all other levels have
`z_i=s_i/n_i<1/L^2`.  Since the followed child is larger,
every level loses at most one bit of size.  Also, for large `L`,

\[
 \log(n_i/n_{i+1})=-\log(1-z_i)\le 2/L^2        \tag{17}
\]

at a nonlarge level.  The total loss before stopping is more than `4R`
bits, while the fewer than `R` large levels account for less than `R`.
Consequently there are more than

\[
 {3\over2}RL^2                                   \tag{18}
\]

nonlarge levels.  At least half have their discarded sibling on the same
side of the followed path.  Fix one leaf in every such sibling and one leaf
below the stopping point.  Every subset of the same-side sibling leaves,
together with the terminal leaf, is a pure left or pure right comb.  Hence

\[
 \log W(T)>{3\over4}RL^2,                        \tag{19}
\]

which, by (6), is far stronger than (2).

It remains to consider the case of at least `R` large levels.  At every
large level before stopping, both children have at least

\[
 2^{L-\Delta}\quad\hbox{leaves},
 \qquad \Delta=4R+2\lambda+1.                   \tag{20}
\]

Indeed the followed child has at least `n_i/2`, while (16) bounds the
discarded sibling; before stopping `n_i>=n/2^(4R)`.

Thus (3) gives, uniformly for both children of every selected large node,

\[
 x+y\ge F:={1\over2}(L-\Delta)^2-3L.             \tag{21}
\]

Select `R` large nodes and order them from deepest to highest.  The deepest
node supplies the first reset (10).  At each later node, the child
containing the preceding selected node is `H`, and the other child is `Q`.
Monotonicity carries the accumulated endpoint coordinates through any
intermediate nodes.  Of the `R-1` later attachments, one direction occurs
at least

\[
 q=\left\lceil{R-1\over2}\right\rceil            \tag{22}
\]

times.  If `mu>=F-L`, then (2) follows immediately from (14), (20), and
(21).  Otherwise `D=F-mu>L`, so all lower bounds in the reset calculation
are positive, and (13) applies.  We obtain

\[
 \mu\ge F-{F\over q+3}-{2L\over q+3}.            \tag{23}
\]

Since `R=Theta(sqrt L)`, `Delta=O(sqrt L)`, and `F<=L^2/2`, both alternatives
give

\[
 \mu\ge {1\over2}L^2-O(L^{3/2}),                 \tag{24}
\]

as claimed.

The estimates above were written for all sufficiently large `L` (so, for
example, `L-Delta>3` and (17) holds with the displayed constant).  The
finitely many smaller values are absorbed by enlarging the absolute
constant in the `O(L^(3/2))` term.

## 4. What this proves, and what it does not

The theorem proves the sharp coefficient `1/2` for **every strong
decomposition tree**, not merely for homogeneous or stationary blow-ups.
In particular there is no nonstationary anti-aligned strong-tree
construction below `1/2`.  The artificial states which defeat fixed local
quadratic Bellman profiles are harmless globally: repeatedly realizing
such resets forces (12), while avoiding reset nodes creates the pure-comb
explosion (19).

This closes the `Tree alignment conjecture` at the coefficient level, with
error `O((log n)^(3/2))`.  It does **not** by itself prove Erdős 838 for an
arbitrary planar point set: the strong-tree recurrence (1) is an exact
special class.  The remaining full-problem lower bound still needs either
a decomposition/regularization theorem reducing arbitrary order types to
large strong pieces with negligible loss, or an endpoint-history argument
which recreates the same reset mechanism without strong glues.
