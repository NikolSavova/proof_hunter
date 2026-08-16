# The 1+3 interval fibre: exact visible/hidden Kraft factorization and a literal weighted rectangle barrier

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The rooted visible-hull/hidden-pocket identity gives an exact two-record
description of the remaining `1+3` interval fibre, but it does not by
itself give the required one-face decoder or a subpower-congestion weighted
Hall telescope.

For a left endpoint `ell` and an interval face `W`, let `V_ell(W)` be the
vertices of `conv(W union {ell})`, and put

\[
             Z_\ell(W)=W-V_\ell(W).                              \tag{1}
\]

The visible set `V_ell(W)` and the hidden trace `Z_ell(W)` are both
ordinary faces, and together they recover `W`.  For a fixed visible hull
the hidden choices form an exact Boolean fibre, giving the rooted Kraft
identity

\[
             (1+z)^m=\sum_Hz^{|H|}(1+z)^{|I(H)|}.                 \tag{2}
\]

This is a genuine weighted equality, not a loss.  Its limitation is
coexistence: every nonempty hidden trace is inside the visible rooted
polygon, so adjoining it back to the visible endpoint face is nonconvex.
The identity therefore produces a pair code, not one ordinary mixed face.

There is an exact scalable planar barrier with the actual literal
depth-zero weights.  A rational convex conic is split into an upper visible
arc `X` and a lower hidden arc `Y`; take `|X|=|Y|=3s` and let both
choices range over their rank-`s` layers.  These choices are independent
interval faces.  Endpoint
clusters `L,R` give the full record rectangle

\[
 \mathcal R=L\times R\times{X\choose s}\times{Y\choose s}.       \tag{3}
\]

Every record has the same fixed canonical left-role `1+3` trace.  The
natural ordinary one-face projections are:

* the rooted visible hull;
* the selected hidden trace;
* the full interval face `W`; and
* the endpoint edge.

For uniform record weight, which is exactly the literal depth-zero tilt
because $h_{0,e}=1$, their cardinalities and loads form a complete
rectangle.  If `|L|=|R|=2^s`, then even arbitrary fractional
routing among all four projection banks has maximum normalized load

\[
                         \Omega(2^{2s})=\Omega(n^2).                \tag{4}
\]

Thus neither choosing the visible output, descending to the hidden output,
falling back to `W`, nor falling back to the endpoint edge yields a
subpower global decoder.  In fact the same family defeats every
**subset-valued** one-face decoder: allowing an arbitrary ordinary output
contained in the record still forces normalized load
`Omega(n/log n)`.  This regression also defeats the parabola special case:
there the visible alphabet collapses to successive endpoint pairs and the
hidden fibre is the full middle Boolean layer.

The barrier is not a counterexample to the global KL bound.  It does not
rule out an output importing a new external reservoir label, nor an output
using source chronology or marks not present in the record.  Those are the
precise remaining ways around the capacity obstruction.

Finally, recursion cannot assume that the hidden child has a favorable
face complex.  Singleton-reset projective universality transfers an
arbitrary rational planar order type into a full hidden pocket without
changing any of its detached convex subsets.  Hence an iteration which
uses only the child face complex is coefficient-equivalent to restarting
Erdos 838 itself.

The exact verifier is

```text
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_visible_hidden_interval_kraft_barrier.py
```

It checks the conic rectangle with rational arithmetic, verifies the fixed
trace, all visible and hidden fibres, constant-rank literal weights, exact
projection loads, and the fractional capacity lower bound.  It also reruns
an exact parabola visible-pair stress test and an arbitrary-order-type
singleton reset transfer.

## 1. Exact visible-hull fibre

Fix roots `p,q` and a finite side cloud `Q` of size `m` in one open
halfplane of their line, in general position.  For `S subset Q`, define

\[
 h(S)=\operatorname{vert}\operatorname{conv}(S\cup\{p,q\})
                   -\{p,q\}.                                      \tag{5}
\]

For a rooted visible hull `H`, let

\[
 I(H)=Q\cap\operatorname{int}
                  \operatorname{conv}(H\cup\{p,q\}).              \tag{6}
\]

The exact fibre theorem is

\[
                    h^{-1}(H)=\{H\cup Z:Z\subseteq I(H)\}.         \tag{7}
\]

Indeed every nonvertex is strictly inside the rooted polygon, while adding
any subset of its strict interior changes no hull vertex.  Summing
`z^(|H|+|Z|)` proves (2) coefficientwise.

For the interval application, the fixed `1+3` trace supplies two witness
roots in `W`, the bad endpoint belongs to the visible rooted hull, and the
hidden circuit label belongs to `I(H)`.  Equation (7) is therefore the
precise proposed reset.

The decoder inside one fixed hull is perfect: outputting the actual hidden
trace `Z` and retaining `H` as fixed side information recovers the record.
The global problem is that distinct visible states can use the same hidden
output.  Conversely, outputting `H` erases all `2^{|I(H)|}` members of its
Boolean fibre.  Formula (2) balances these two alternatives but does not
merge them into one face.

## 2. A rational full rectangle

Take two rational conic vertices

\[
                         a=(-1,0),\qquad b=(1,0),                    \tag{8}
\]

an upper conic arc `X`, and a lower conic arc `Y`, in the cyclic order

\[
                         a,\ Y,\ b,\ X.                              \tag{9}
\]

All points lie on one strictly convex conic, so every subset is ordinary.
Choose `ell_0` strictly left and far below the conic so that

\[
       Y\subset\operatorname{int}\operatorname{conv}
                         \{\ell_0,a,b\},                            \tag{10}
\]

while `ell_0 union {a,b} union X` is convex.  Choose the lower arc so that,
in its left-to-right order,

\[
 \chi(\ell_0,y_i,y_j)<0<\chi(y_i,y_j,y_k)
 \quad(i<j<k).                                            \tag{10a}
\]

This follows, for example, by taking a compact strictly convex graph arc
and putting `ell_0` below it so that every secant slope from `ell_0`
exceeds the arc's tangent slopes.  These are strict rational orientation
inequalities.  Hence one may replace
`ell_0` by an arbitrary rational general-position cluster `L` in a small
neighbourhood.  Put a rational cluster `R` strictly to the right of the
conic.

Force five initial lower-arc labels `y_0,...,y_4` into every interval face.
The first bad four-subset is then

\[
                         \{\ell,a,y_0,y_1\},                       \tag{11}
\]

for every `ell in L`; its fixed trace is
`A={a,y_0,y_1}` with left endpoint role.  The three forced labels
`y_2,y_3,y_4` remain in `W-A`, so complement reattachment is still
nonconvex.

Let the optional clouds `X` and `Y-{y_0,...,y_4}` each have size `3s`,
and let `X_0` and `Y_0` range over their rank-`s` layers.  Define

\[
 W(X_0,Y_0)=\{a,b,y_0,\ldots,y_4\}\cup X_0\cup Y_0.                \tag{12}
\]

Every such `W` is an ordinary face of one common rank.  Equations
(9)--(10) give exactly

\[
 \begin{split}
 V_\ell(W)&=\{\ell,a,b\}\cup X_0,\\
 Z_\ell(W)&=\{y_0,\ldots,y_4\}\cup Y_0.                           \tag{13}
 \end{split}
\]

Thus visible and hidden choices are independent.  Adding any member of the
second line to the complete first line is nonconvex by (10).

## 3. Exact literal projection loads

Write

\[
 A=\binom{3s}{s},\qquad l=|L|,\quad r=|R|.             \tag{14}
\]

The number of records is

\[
                         M=l r A^2.                                 \tag{15}
\]

At canonical depth zero, `q_(0,e)=p_e` for every endpoint cell, so

\[
                              h_{0,e}=1.                            \tag{16}
\]

All target faces in (12) have one rank, hence their half-Gibbs capacities
are equal.  After scaling by that common positive constant, the literal
record weights are exactly uniform.

The four projection banks have the following exact sizes and per-output
loads:

\[
\begin{array}{c|c|c}
\text{output}&\text{number of outputs}&\text{load}\\
\hline
V_\ell(W)&lA&Ar\\
Z_\ell(W)&A&Alr\\
W&A^2&lr\\
e&lr&A^2.
\end{array}                                                       \tag{17}
\]

The entries follow by fixing the displayed coordinates and freely choosing
the erased ones.  They multiply back to `M` in every row.

The relevant Hall calculation must use half-Gibbs capacities, rather than
unit capacities.  Every record has literal depth-zero demand

\[
 {2^{-|W|}\over4F}={2^{-(2s+9)}\over F},                         \tag{18}
\]

because `q_(0,e)=p_e` and `Z_e=4G_e`.  The four tagged output banks have
total half-Gibbs capacity

\[
 {1\over F}\left(
 lA2^{-(s+3)}+A2^{-(s+5)}+A^2 2^{-(2s+7)}+{lr\over4}
 \right).                                                        \tag{19}
\]

Tagging the banks can only increase the available capacity.  Therefore,
even for arbitrary fractional routing, the maximum normalized output load
`T` obeys the exact lower bound

\[
 \boxed{
 T\ge
 {lrA^2 2^{-(2s+9)}\over
 lA2^{-(s+3)}+A2^{-(s+5)}+A^2 2^{-(2s+7)}+lr/4}.}                 \tag{20}
\]

Put `B=A2^{-s}`.  Stirling gives

\[
 B=\Theta\left({(27/8)^s\over\sqrt s}\right).                    \tag{21}
\]

For `l=r=2^s`, the denominator of (20) is asymptotic to `B^2/128`,
whereas its numerator is `lrB^2/512`.  Consequently

\[
                              T=\Theta(2^{2s}).                     \tag{22}
\]

The ambient number of points is `n=2^(s+1)+O(s)`, proving (4).  The loss
is present for the actual activity weighting, not merely for raw record
counts.  The unweighted projection table happens to give the same
fixed-power conclusion, but (18)--(22) are the load-bearing KL audit.

## 4. Every subset-valued one-face decoder is congested

The obstruction is not confined to the four projections.  Suppose a
decoder may output any ordinary face `O subset e union W` from its record.
By (10a), if `ell in O`, then `O` contains at most two labels of the entire
lower cloud: any three of them together with `ell` already form a
nonconvex four-set.

We can therefore upper-bound the half-Gibbs capacity of **all** possible
outputs, including many sets which do not actually occur.  Put

\[
 P_s=\sum_{i=0}^2\binom{3s+5}{i}2^{-i}=O(s^2).           \tag{23}
\]

Outputs omitting `ell` have total capacity at most

\[
 {1\over F}\left(1+{r\over2}\right)
                  \left({3\over2}\right)^{6s+7}.       \tag{24}
\]

Here we have allowed every subset of all conic labels, even though a
record contains only `s` optional labels from each arc.  For outputs
containing `ell`, sum first over its `l` possible labels, then over an
optional right endpoint, the two anchors, every upper-cloud subset, and at
most two lower-cloud labels.  Their total capacity is at most

\[
 {1\over F}{l\over2}\left(1+{r\over2}\right){9\over4}
        \left({3\over2}\right)^{3s}P_s.                \tag{25}
\]

Consequently arbitrary fractional routing to arbitrary record subfaces
has maximum normalized load at least

\[
 \boxed{
 {lrA^2 2^{-(2s+9)}\over
 (1+r/2)\left[(3/2)^{6s+7}
 +(l/2)(9/4)(3/2)^{3s}P_s\right]}.}                    \tag{26}
\]

For `l=r=2^s`, Stirling and the exact identity
`(27/8)^(2s)=(3/2)^(6s)` show that the numerator is

\[
 \Theta\left({lr(3/2)^{6s}\over s}\right).             \tag{27}
\]

The first term in the denominator of (26) is
`Theta(r(3/2)^(6s))`.  The second is smaller by
`O(s^2(16/27)^s)`.  Thus

\[
                 T=\Omega(2^s/s)=\Omega(n/\log n).      \tag{28}
\]

This proves the claimed subset-decoder barrier.  An escape must use a
label outside the record, or extra state whose global capacity is charged
separately; merely choosing a cleverer mixed subface cannot work.

The statement is robust to a small external repair alphabet.  If every
output is contained in `e union W union C` for one fixed external alphabet
`C` of size `c`, allowing all subsets of `C` multiplies the capacity upper
bound by at most `(3/2)^c`.  Adding labels cannot repair the already
nonconvex four-subset `ell union {y_i,y_j,y_k}`, so the at-most-two lower
trace restriction remains valid.  If the decoder also uses `J` tagged
states, tagging multiplies capacity by at most `J`.  Thus (28) strengthens
to

\[
 T=\Omega\left({n\over J(3/2)^c\log n}\right).           \tag{29}
\]

In particular, `J=n^{o(1)}` and `c=o(log n)` still force fixed-power
congestion.  Any external-alphabet escape must expose `Omega(log n)`
globally chargeable repair labels (or an equivalent fixed-power state
alphabet); a subpower decoder description does not suffice.

## 5. Parabola and universality stress tests

In the parabola regression from the preceding report, an external endpoint
sees only the two extreme labels of every retained interval subset.  The
hidden pocket is the remaining middle set.  Repeating the visible reset
therefore outputs successive endpoint pairs.  A central layer has
exponentially many subsets but only quadratically many possible pair
outputs at every level.  The complete path of pairs encodes the subset;
no individual ordinary pair does.  This is the linear-chain specialization
of (17)--(20).

At the opposite extreme, singleton-reset projective universality says that
the discarded tips of a strict full-pocket reset chain can have any
prescribed rational planar order type, with exactly the same detached face
complex.  Its rooted polynomial is only `1+Ls`, so no nonempty child face
coexists with the roots and current visible tip.  Hence repeated use of
(2) cannot assume Booleanity, convex-chain structure, or an independent
parent-child product after the first reset.

The two examples bracket the identity sharply: the conic/parabola family
already saturates projection congestion when the child is Boolean, while
projective universality makes the child arbitrary when one tries to
recurse.  A positive continuation must introduce a new mixed ordinary face
or exploit source chronology/marks beyond the visible-hidden Kraft data.
