# Erdős 838: the fitted cyclic IFS has a branching convex chain

## Verdict

The cyclic three-cluster IFS fitted to the unique nine-point lexicographic
minimizer is **rigorously unusable** as a quasipolynomial upper construction.
It contains a fixed binary subsystem whose entire level is in strict convex
position.

Let `F_0,F_1,F_2` be the exact rational affine maps in
`agent_lex_minimizer_search/triangular_ifs_certificate.json`, and set

\[
 T_0=F_0\circ F_0,\qquad T_1=F_0\circ F_1.                 \tag{1}
\]

If `q` is macro vertex zero, then for every `r>=1` the points

\[
 \mathcal C_r=
 \{T_{\epsilon _1}\circ\cdots\circ T_{\epsilon _r}(q):
       \epsilon_i\in\{0,1\}\}                             \tag{2}
\]

form one strict convex `x`-monotone chain, in lexicographic word order.  Let
`H_{2r+1}` denote the size of this explicit witness.  At IFS depth
`d=2r+1`,

\[
 H_{2r+1}=2^r,
 \qquad H_{d+2}=2H_d,
 \qquad h(P_d)\ge H_d,                                    \tag{3}
\]

for the explicit witnesses, where `h` is maximum convex-subset size.  Since
`|P_d|=3^d`, writing `N=3^{2r+1}` gives

\[
 h(P_{2r+1})\ge (N/3)^{\log_9 2}.                         \tag{4}
\]

Every subset of a convex-position set remains in convex position.  Hence,
including the empty set as in the official convention,

\[
 \boxed{V(P_{2r+1})\ge 2^{2^r}
       =2^{(N/3)^{\log_9 2}}.}                            \tag{5}
\]

This is stretched exponential in `N`, and therefore larger than
`2^{C(log N)^2}` for every fixed `C`.  The finite dip in normalized trace at
depths three and four cannot extend asymptotically.

All computations below are exact rational computations.  The source IFS file
is pinned in the certificate by SHA-256.

## 1. Exact cone certificate

Write `A_0,A_1` for the linear parts of `T_0,T_1`.  With positive scalar
denominators suppressed, they are

\[
A_0={1\over117587030741278944400}
\begin{pmatrix}
43841317051540908396&13309053758516261466\\
52820350536179839518&16318941012260210853
\end{pmatrix},                                            \tag{6}
\]

and

\[
A_1={1\over2351740614825578888}
\begin{pmatrix}
103022665546611636&-650294688144150\\
144407361732265458&51616671965280225
\end{pmatrix}.                                            \tag{7}
\]

Both determinants are positive.  For a vector with positive first
coordinate, identify its direction with its slope.  Put

\[
 C=(1,3),\qquad a={243\over200}=1.215,qquad
 b={13\over10}=1.3.                                      \tag{8}
\]

Direct exact endpoint checks, combined with positivity of the determinants,
give

\[
 A_0(C)\subset C,\qquad A_1(C)\subset C,                 \tag{9}
\]

and the stronger separated inclusions

\[
 \operatorname{slope}(A_0v)<a
 \quad(v\in C),
 \qquad
 \operatorname{slope}(A_1v)>b
 \quad(v\in C).                                         \tag{10}
\]

Here and below `v in C` also records that its first coordinate is positive.
The initial edge

\[
 e=T_1(q)-T_0(q)                                         \tag{11}
\]

lies in `C`.

The only depth-dependent object is the bridge between the two recursive
children.  For `k>=1`, define

\[
 B_k=T_1(T_0^kq)-T_0(T_1^kq).                            \tag{12}
\]

The exact certificate proves

\[
 B_k^{(x)}>0,qquad
 a<\operatorname{slope}(B_k)<b
 \quad\hbox{for every }k\ge1.                            \tag{13}
\]

For completeness, this is an all-depth estimate, not extrapolation from a
finite list.  Let `p_i` be the fixed point of `T_i`.  Then

\[
 B_k=B_\infty+A_1A_0^k(q-p_0)-A_0A_1^k(q-p_1),           \tag{14}
\]

where

\[
 B_\infty=T_1(p_0)-T_0(p_1).
\]

In the infinity norm, the following rational inequalities hold:

\[
 \|A_0\|_\infty<{3\over5},\quad
 \|A_1\|_\infty<{1\over10},\quad
 \|q-p_0\|_\infty<40000,\quad
 \|q-p_1\|_\infty<2000.                                \tag{15}
\]

Consequently

\[
 \|B_k-B_\infty\|_\infty
 <4000(3/5)^k+1200(1/10)^k.                              \tag{16}
\]

At `k=14` the right side is exactly bounded by

\[
 {783641640963\over250000000000}< {16\over5},            \tag{17}
\]

and decreases thereafter.  Exact evaluation of the limiting vector gives

\[
 B_\infty^{(x)}>12000,\quad
 B_\infty^{(y)}-aB_\infty^{(x)}>{15\over2},\quad
 bB_\infty^{(x)}-B_\infty^{(y)}>1000.                   \tag{18}
\]

Equations (16)--(18) imply (13) for `k>=14`; the thirteen remaining values
are checked exactly.  Notice that the narrow gap at the lower edge is still
strict: the worst possible tail loss is

\[
 (1+a){16\over5}=7.088 < 7.5.                            \tag{19}
\]

## 2. Proof that every binary level is a convex chain

Order the points of `C_r` lexicographically by their binary words.  We prove
simultaneously that

1. every consecutive edge has positive `x`-coordinate and slope in `C`;
2. consecutive edge slopes are strictly increasing.

For `r=1`, the only edge is (11), so the assertion holds.  At the next level,
the ordered list is

\[
 T_0(\mathcal C_{r-1})\quad\hbox{followed by}\quad
 T_1(\mathcal C_{r-1}).                                 \tag{20}
\]

Internal edges are transformed by `A_0` or `A_1`.  They remain in `C` by
(9), and all their internal turns retain their sign because both
determinants are positive.  The bridge in (20) is `B_{r-1}` and lies in
`(a,b)` by (13), so it also has positive `x`-coordinate.

It remains only to check the two turns touching the bridge.  The last edge
inside the left child is

\[
 A_0A_1^{r-2}e,
\]

whose slope is less than `a` by (9)--(10).  The first edge inside the right
child is

\[
 A_1A_0^{r-2}e,
\]

whose slope is greater than `b`.  Thus their slopes occur in the strict
order

\[
 \operatorname{slope}(A_0A_1^{r-2}e)
 <a<\operatorname{slope}(B_{r-1})<b
 <\operatorname{slope}(A_1A_0^{r-2}e).                  \tag{21}
\]

This closes the induction.  A strict `x`-monotone cup is a boundary chain of
its convex hull, so all `2^r` points are extreme.  Equations (3)--(5) follow.

## 3. Finite cone-state dichotomy for future cyclic substitutions

The example exposes a reusable kill test.  Here is a precise abstract form.

### Branching-state lemma

Suppose a fixed small-cluster substitution has a finite collection `S` of
certified boundary-chain states.  A production

\[
 s\longrightarrow(s_1,\ldots,s_m)                       \tag{22}
\]

means that chains in the listed child states can be concatenated, with at
most `K` shared or discarded endpoints, into a chain in state `s`.  Thus

\[
 H_s(d+1)\ge\sum_{j=1}^m H_{s_j}(d)-K.                  \tag{23}
\]

Assume `S` and `K` are fixed independently of depth.  If a recurrent strongly
connected component has a production with at least two children in that
same component, then there are constants `L,c>0` such that

\[
 H_s(d+L)\ge2H_s(d)-K',\qquad H_s(d)\ge c2^{d/L}.       \tag{24}
\]

Indeed, strong connectivity routes the parent state to the branching
production and routes both recurrent child states back to the parent in
bounded (not necessarily equal) numbers of unary productions.  This gives a
bounded-delay generalized Fibonacci inequality
`H_s(d)>=H_s(d-l_1)+H_s(d-l_2)-K'`.  Its positive characteristic root is
larger than one, giving the second part of (24); on a fixed arithmetic
subsequence it also gives the displayed doubling form after changing `L,c`
by constants.  Equivalently, the unfolded multitype production matrix has
Perron root greater than one.

If every local template has at most `R` children, then `N_d<=R^d`.  From a
branching rate `lambda>1`,

\[
 H_s(d)\ge c\lambda^d\ge cN_d^{\log_R\lambda},
 \qquad V(P_d)\ge2^{H_s(d)}.                             \tag{25}
\]

Thus **any recurrent branching cone state is fatal to a quasipolynomial
upper construction**.  The fitted IFS realizes (24) with `L=2`, `K'=0`, and
the single cup state certified by (8)--(21).

### Nonbranching normal form

Conversely, if `V(P_d)=2^{O(d^2)}`, (25) forbids every recurrent branching
state in any complete finite cone-state classifier.  Inside every reachable
sink component, each directional boundary chain can therefore have
unbounded occupancy in at most one child; all other child contributions are
bounded local decorations.  The bounded transient path into a sink does not
affect asymptotic coefficients.  This is the **one-multi-occupancy normal
form**.

This observation does not by itself prove the `1/2` barrier for every
conceivable affine substitution.  It reduces that claim to two checkable
properties of the local classifier:

1. complementary upper/lower chain states satisfy the ordinary cup--cap
   capacity inequality;
2. a left upper-chain choice and a right lower-chain choice glue
   independently to a convex subset (possibly with bounded endpoint loss).

When these hold, the standard finite-state max-plus proof applies verbatim.
If `rho_C,rho_U` are the recurrent cap and cup cycle means and the macro
growth is `R^d`, Erdős--Szekeres gives

\[
 \rho_C+\rho_U\ge\log_2R.                               \tag{26}
\]

One-multi-occupancy makes the cap and cup counting recurrences triangular:

\[
 \log C(d)={\rho_C\log_2R\over2}d^2+O(d),\qquad
 \log U(d)={\rho_U\log_2R\over2}d^2+O(d).              \tag{27}
\]

The independent two-endpoint gluing term `CU` then gives

\[
 \liminf {\log_2V(P_d)\over(\log_2|P_d|)^2}\ge{1\over2}.
                                                                    \tag{28}
\]

Therefore a finite-state cyclic/triangular proposal has a sharp audit:

* a recurrent branching cone transition implies stretched-exponential
  `V` and kills the construction immediately;
* without branching, it collapses to one-multi-occupancy, and any classifier
  with complementary-chain capacity plus endpoint gluing faces the existing
  `1/2` barrier.

An alleged finite-state escape must explicitly exhibit a failure of endpoint
gluing or an incomplete/infinite directional-state space.  Merely rotating
three ordinary small-cluster rules cannot evade this dichotomy.

## 4. Verification

From the repository root, run

```bash
python3 phase2/loop/erdos838/agent_cyclic_ifs_kill/verify_cyclic_ifs_kill.py
```

Expected output:

```text
PASS: exact all-depth certificate
tail bound at k=14: 783641640963/250000000000 = 3.134566563852
bridge separation: 243/200 < slope(b_k) < 13/10
binary convex-chain levels enumerated through r=8
```

The verifier checks all rational inequalities in (8)--(19), writes
`cyclic_ifs_kill_certificate.json`, and directly enumerates binary levels
through `r=8` as an indexing sanity check.  The enumeration is not used to
infer the all-depth result; that result follows from the cone induction and
the finite-prefix-plus-tail bridge proof.

`search_repeatable_embedding.py` records the discovery search that found the
two blocks `00,01`; it is not part of the proof.
