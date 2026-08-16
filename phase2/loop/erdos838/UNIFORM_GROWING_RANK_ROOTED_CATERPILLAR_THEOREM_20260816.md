# A uniform growing-rank rooted-caterpillar theorem

**Date:** 2026-08-16. All logarithms are base two.

## Verdict

Let $T$ be an arbitrary rooted full binary tree with $n$ leaves, and let
$R_k(T)$ be the number of $k$-leaf subsets whose suppressed induced
rooted tree is the binary caterpillar $F_k^2$. Put

\[
 b_2={1\over2},\qquad
 b_k={b_{k-1}\over 2^{k-1}-1}\qquad(k\geq3).
                                                               \tag{1}
\]

Then the following finite inequality holds simultaneously for every $n$
and $k\geq2$:

\[
 \boxed{
 R_k(T)\geq b_k\bigl(n-2^{k-2}\bigr)_+^k.}
                                                               \tag{2}
\]

This replaces the nonuniform additive error in the fixed-$k$
caterpillar-density theorem by an exact shift of only $2^{k-2}$ leaves.
In particular, at the canonical growing-rank scale $n=4^k$,

\[
 \log R_k(T)\geq {3\over2}k^2+O(k).             \tag{3}
\]

Thus the finite-size obstruction in
`FIXED_RANK_STRONG_TREE_CATERPILLAR_AUDIT_20260815.md` is completely
removed. The plane-orientation obstruction is not: $R_k$ counts every
left/right itinerary of an endpoint-rooted caterpillar, whereas an ordinary
face in an ordered strong tree is assembled from a monotone cap arm and a
monotone cup arm. Consequently (2) is a strict construction-class theorem,
not a fixed-size supersaturation theorem for convex faces.

## 1. The split inequality

The only analytic input is

\[
 x^k+y^k+(2^{k-1}-1)
       \bigl(xy^{k-1}+yx^{k-1}\bigr)
 \geq (x+y)^k                                      \tag{4}
\]

for $x,y\geq0$ and $k\geq3$.

To prove it, put $A=xy^{k-1}$ and $B=x^{k-1}y$. For
$1\leq j\leq k-1$, weighted AM--GM gives

\[
 x^j y^{k-j}
 =A^{(k-1-j)/(k-2)}B^{(j-1)/(k-2)}
 \leq {k-1-j\over k-2}A+{j-1\over k-2}B.          \tag{5}
\]

After multiplying by $\binom kj$ and summing, symmetry makes the
coefficient of each of $A,B$ equal to

\[
 {1\over2}\sum_{j=1}^{k-1}\binom kj=2^{k-1}-1.   \tag{6}
\]

Equations (5)--(6) majorize all the middle terms in the binomial expansion
of $(x+y)^k$, proving (4). Equality holds at $x=y$, explaining the
constant in (1).

## 2. Shifted induction

Write

\[
                         s_k=2^{k-2}.             \tag{7}
\]

For a root split $T=A\wedge B$, with $a=|A|$ and $b=|B|$, the exact
rooted-caterpillar recurrence is

\[
 R_k(T)=R_k(A)+R_k(B)+aR_{k-1}(B)+bR_{k-1}(A).   \tag{8}
\]

The base $k=2$ follows from

\[
 R_2(T)=\binom n2\geq {1\over2}(n-1)^2.          \tag{9}
\]

Assume (2) at rank $k$ for smaller trees and at rank $k-1$. There are
two cases.

### Both children cross the preceding shift

Suppose $a,b\geq s_{k-1}$, and set

\[
                 x=a-s_{k-1},\qquad y=b-s_{k-1}. \tag{10}
\]

Since $s_k=2s_{k-1}$, we have $x+y=n-s_k$. Also $a\geq x$ and
$b\geq y$. Applying the induction hypotheses in (8), then using
$b_{k-1}/b_k=2^{k-1}-1$, gives

\[
\begin{aligned}
 R_k(T)
 &\geq b_k(x^k+y^k)
   +b_{k-1}(xy^{k-1}+yx^{k-1})\\
 &\geq b_k(x+y)^k
  =b_k(n-s_k)^k,                                  \tag{11}
\end{aligned}
\]

where the second line is (4).

### One child lies below the preceding shift

By symmetry suppose $a<s_{k-1}$. Put $X=(n-s_k)_+$. The inherited
$B$-term and the crossing term in (8) give

\[
 R_k(T)\geq b_k(X-a)_+^k+a b_{k-1}X^{k-1}.       \tag{12}
\]

Indeed $b-s_k=X-a$ whenever $X>0$, and
$b-s_{k-1}\geq X$. The elementary mean-value estimate

\[
 X^k-(X-a)_+^k\leq kaX^{k-1}                    \tag{13}
\]

and $b_{k-1}/b_k=2^{k-1}-1\geq k$ show that (12) is at least
$b_kX^k$. This proves (2).

## 3. Canonical exponent

From (1),

\[
 \log b_k=-1-\sum_{j=1}^{k-1}\log(2^j-1)
          =-{k(k-1)\over2}+O(1).                 \tag{14}
\]

At $n=4^k$, the shift ratio is

\[
 {2^{k-2}\over4^k}=2^{-k-2},                    \tag{15}
\]

so $k\log(1-2^{-k-2})=o(1)$. Therefore

\[
\begin{aligned}
 \log R_k(T)
 &\geq \log b_k+k\log(4^k-2^{k-2})\\
 &= -{k(k-1)\over2}+2k^2+O(1)
  ={3\over2}k^2+{k\over2}+O(1),                 \tag{16}
\end{aligned}
\]

which proves (3).

## 4. The exact plane-ordered endpoint formula

The orientation gap has a compact exact form. Order the leaves of an
ordered full binary tree from left to right. Fix two leaves $x<y$, let
$w$ be their least common ancestor, and let $A,B$ be the left and right
children of $w$.

On the path from $A$ to $x$, record the size of the right sibling every
time the path takes a left edge. On the path from $B$ to $y$, record the
size of the left sibling every time the path takes a right edge. Call the
resulting list

\[
                  \mathcal S(x,y)=(s_1,\ldots,s_q).       \tag{17}
\]

Then the ordinary faces whose leftmost and rightmost leaves are exactly
(x,y) have generating polynomial

\[
                   z^2\prod_{j=1}^q(1+s_jz).             \tag{18}
\]

Indeed the left trace must be a cap. Along its root-to-(x) path it may
take zero or one arbitrary leaf from exactly the recorded right siblings.
The right trace is the reflected cup statement. The two choices have
disjoint grounds and glue at (w), so they are independent. Conversely,
the strong-glue classification forces every face with extreme leaves
(x,y) to arise this way.

Consequently, if $e_t$ denotes the elementary symmetric polynomial,

\[
 \boxed{
 v_k(T)=\sum_{x<y}e_{k-2}\bigl(\mathcal S(x,y)\bigr)
 \qquad(k\geq2).}                                      \tag{19}
\]

Formula (19) is the orientation-sensitive endpoint of the present attack.
Unlike $R_k$, it counts genuine ordinary faces and retains all sibling
weights. Thus P1b is now reduced to a concrete weighted two-arm statement:
at $n=4^k$, prove that the sum in (19) is
$2^{(3/2-o(1))k^2}$. This is not declared a further theorem here; it is
the exact gate left after the finite-size issue has been removed.

## 5. Exact scope

The result is stronger than the fixed-(k) asymptotic estimate in precisely
the regime needed by P1b: its error remains negligible when
$k=(1/2)\log n$. It also shows that the dominating additive error in the
published estimate is a proof artifact rather than a genuine shortage of
unordered caterpillars.

It does **not** imply the desired ordinary-face count. Forgetting the plane
order is still a quadratic-scale issue: a rooted caterpillar accepts an
arbitrary attachment word, while the cap and cup recurrences accept only
the two monotone endpoint states. Any completion of P1b must use an
orientation-sensitive two-arm argument; merely improving the finite error
in unordered inducibility can no longer help.

## 6. A stronger plane analogue is false

The most natural attempted completion of (2) was

\[
 v_k(T)\stackrel{?}{\geq}
 b_k\bigl(n-2^{k-2}\bigr)_+^k.                         \tag{20}
\]

It passes every ordered full binary tree through thirteen leaves, with
substantial slack outside rank two, but it is false.  Take the 256-leaf
comb whose successive attachment sides alternate.  The exact graded
strong-tree recurrence gives

\[
 v_4(T)=86{,}709{,}504,
 \qquad
 b_4(256-4)^4=96{,}018{,}048.                           \tag{21}
\]

Thus the ratio in (20) is approximately $0.903054$.  This finite failure
does not threaten the desired exponent: it is less than one bit, whereas
P1b permits a factor $2^{o(k^2)}$.  It does rule out reusing the scalar
shifted induction without an orientation state.

At the canonical scales tested, the largest observed unordered-to-plane
ratio is instead the alternating comb value
$R_k(T)/v_k(T)=2^{k-3+o(1)}$.  A uniform proof of a
$2^{O(k\log k)}$ comparison after subtracting the near-threshold part would
complete P1b together with (2).  No such comparison is claimed here: close
to the Erdős--Szekeres threshold the ratio can be much larger, so the
statement must retain the shifted/excess mass rather than compare the two
raw pattern counts.

## 7. Verification

Run

~~~text
python3 phase2/loop/erdos838/verify_uniform_growing_rank_caterpillar.py
~~~

The verifier checks the exact recurrence and (2) on every ordered full
binary tree through eleven leaves, checks the coefficient identities behind
(4)--(6), verifies the one-small-child estimate on an exhaustive integer
grid, recomputes the canonical exponent ledger with exact rational
arithmetic, independently checks (18)--(19) on every ordered tree through
nine leaves, exhausts (20) through thirteen leaves, and verifies the exact
alternating-comb counterexample (21).
