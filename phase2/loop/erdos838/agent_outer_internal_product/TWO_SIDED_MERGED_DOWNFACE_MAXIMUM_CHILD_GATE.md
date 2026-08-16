# Two-sided merged downfaces on maximum-child tries

## Verdict

There is an exact positive operation, but its sharp guaranteed scale is two
logarithms, not three.

For a fixed strong-glue double-bad record, the merged downfaces are exactly a
Cartesian product of two rooted chain downsets. Their rank enumerator
factorizes. Over independent left and right maximum-child tries, the weighted
expanded mass factorizes as

\[
                         E_{\rm merge}
                 =M\,\mathfrak B_L\mathfrak B_R.                \tag{1}
\]

In the best possible full-cube case, a uniform binary run of length
\(\Theta(L)\) has \(\mathfrak B_L=\Theta(L)\); hence the two sides give only
\(\Theta(L^2)\). Requiring the last prefix role on each side makes the two
depths recoverable and gives a genuine load-one two-face bank, but retains
only \(\Theta(L^2)\) expanded mass. Thus it still misses a \(K=3\)
normalization by one logarithm.

This is sharp on a rational planar family. A single blocker makes the full
selected prefixes compatible with the anchors while keeping every complete
source double-bad. With \(L\) binary roles and \(L/4\) roles of size
\(D=2^L/L^6\) on each side, its double-bad record rectangle has

\[
 \log_2 M={1\over2}L^2-3L\log_2L+2L+O(1),                     \tag{2}
\]

rank \(O(L)\), support \(O(2^L/L^5)\), and merged maximum-child multiplier
only \(L^2+O(L)\).

This is a stretchable **record/interface barrier**, not a full low-face
\(2^L\)-point construction. If all role labels are put on the displayed
parabolic arcs, their ambient Boolean faces pay. Replacing the role clouds
by arbitrary low-face children preserves the selected records but returns
the unresolved cross-profile composition problem.

Consequently the two-sided operation is useful when one side already has
superlinear weighted branching or when its merged-face/history load is
smaller than the exact Hall threshold below. It does not unconditionally
supply the missing \(L^3\) factor. No half-coefficient closure is claimed.

## 1. Exact fixed-record classification

Let

\[
                             P=P_L\prec P_R                     \tag{3}
\]

be a genuine two-block strong glue. Fix a double-bad record

\[
                         r=(A,B,y,z)
\]

where \(A\) is a cap of \(P_L\), \(B\) is a cup of \(P_R\),
\(A+y\) is not a cap, and \(B+z\) is not a cup. Let
\(a=a_*(A,y)\) and \(b=b_*(B,z)\) be marked witnesses for which

\[
                         Y_r=\{a,y,z,b\}                        \tag{4}
\]

is the ordinary rank-four seam. Take

\[
                    K\subseteq A-\{a\},\qquad J\subseteq B-\{b\}.
\]

Define the two rooted downsets

\[
\begin{aligned}
\mathcal D^-_{a,y}(K)
  &=\{S\subseteq K:S\cup\{a,y\}\text{ is a cap of }P_L\},\\
\mathcal D^+_{z,b}(J)
  &=\{T\subseteq J:T\cup\{z,b\}\text{ is a cup of }P_R\}.
                                                               \tag{5}
\end{aligned}
\]

They are downsets by heredity. Put

\[
                         G_r(S,T)=Y_r\cup S\cup T.              \tag{6}
\]

> **Theorem 1 (merged-downface product).** For all \(S\subseteq K\) and
> \(T\subseteq J\),
> \[
> G_r(S,T)\in\mathcal F(P)
> \quad\Longleftrightarrow\quad
> S\in\mathcal D^-_{a,y}(K),\quad
> T\in\mathcal D^+_{z,b}(J).                                  \tag{7}
> \]
> Consequently, if
> \[
> C_{r,K}(t)=\sum_{S\in\mathcal D^-_{a,y}(K)}t^{|S|},\qquad
> U_{r,J}(t)=\sum_{T\in\mathcal D^+_{z,b}(J)}t^{|T|},
> \]
> then the merged-face rank enumerator is exactly
> \[
>                  t^4C_{r,K}(t)U_{r,J}(t).                    \tag{8}
> \]

**Proof.** A cross-block subset in a strong glue is ordinary exactly when
its left trace is a cap and its right trace is a cup. The two traces of (6)
are \(S+\{a,y\}\) and \(T+\{z,b\}\). This proves (7). The physical sides
are disjoint, so \((S,T)\mapsto G_r(S,T)\) is injective for fixed \(r\);
summing ranks proves (8). \(\square\)

Thus the two sides really do multiply. What is not automatic is that either
rooted downset has exponential size. The parabolic common-guard example in
`DOUBLE_BAD_PREFIX_HALL_THRESHOLD_AND_HALF_BARRIER.md` has both sizes one.

## 2. Exact weighted aggregate and Hall threshold

Let \(K_i\) and \(J_j\) be the retained prefixes on left and right
maximum-child paths. Let \(\Omega_{ij}\) be the weighted records surviving
both choices and write

\[
\begin{aligned}
c_r(i)&=|\mathcal D^-_{a_r,y_r}(K_i)|,\\
u_r(j)&=|\mathcal D^+_{z_r,b_r}(J_j)|.
\end{aligned}
\]

Expanding every surviving record by every good pair \((S,T)\) gives the
exact total mass

\[
 \boxed{\displaystyle
 E_{\rm merge}
   =\sum_{i,j}\sum_{r\in\Omega_{ij}}w_r\,c_r(i)u_r(j).}         \tag{9}
\]

There are two actual ordinary targets:

\[
                  X_r=A_r\cup B_r,\qquad G_r(S,T).             \tag{10}
\]

Let \(K_X,K_G\) be their aggregate marginal loads, let
\(\Delta_{XG}\) be the ordered-pair load, and put

\[
                 h={K_XK_G\over K_X+K_G}.                      \tag{11}
\]

The two-target fractional Hall theorem gives

\[
 \boxed{\displaystyle
 E_{\rm merge}\le
 \min\{K_XV(P),K_GV(P),2hV(P),\Delta_{XG}V(P)^2\}.}             \tag{12}
\]

After role coloring, \(X_r\) recovers \(A_r,B_r\), while \(G_r\) recovers
\(a_r,y_r,z_r,b_r,S,T\). The only intrinsic ambiguity of the pair is the
two prefix depths and any external history. Therefore

\[
                 \Delta_{XG}\le R_LR_R\Lambda_{\rm hist}.       \tag{13}
\]

If \(S\) is required to contain the last role of \(K_i\), and \(T\) the last
role of \(J_j\), then their occupancy masks recover \(i,j\). On this marked
subbank,

\[
                         \Delta_{XG}\le\Lambda_{\rm hist}.       \tag{14}
\]

Equations (9), (12), and (14) are the exact positive theorem. The price is
that last-role marking keeps at most half of a full prefix cube on each
nonzero side.

If the record family is a Cartesian product of independent one-sided
families, its weights factor, and the two tries are independent, define

\[
\begin{aligned}
\mathfrak B_L
  &={1\over W_L}\sum_i\sum_{\ell\in\Omega_i^L}w_\ell c_\ell(i),\\
\mathfrak B_R
  &={1\over W_R}\sum_j\sum_{\rho\in\Omega_j^R}w_\rho u_\rho(j).
                                                               \tag{15}
\end{aligned}
\]

Then \(M=W_LW_R\), and Fubini applied to (9) proves (1).

## 3. Maximum-child product: the exact two-log ceiling

Consider one uniform role product with role sizes

\[
                              d_0,\ldots,d_{q-1}.               \tag{16}
\]

At depth \(i\), the maximum-child path has relative mass

\[
                       \alpha_i={1\over\prod_{h<i}d_h}.         \tag{17}
\]

Suppose the rooted downset is the full cube \(2^{K_i}\). This is the most
favorable possible geometry. Its one-sided factor is

\[
                 \mathfrak B(d_0,\ldots,d_{q-1})
                    =\sum_{i=0}^{q-1}{2^i\over\prod_{h<i}d_h}. \tag{18}
\]

The depth-recovering last-role subbank has factor

\[
                \mathfrak B^\star={\mathfrak B-1\over2}.        \tag{19}
\]

For

\[
              d_0=\cdots=d_{a-1}=2,\qquad
              d_a=\cdots=d_{a+b-1}=D,
\]

\[
\begin{aligned}
\mathfrak B
  &=a+\sum_{k=0}^{b-1}(2/D)^k\le a+2,\\
\mathfrak B^\star&={\mathfrak B-1\over2}.                      \tag{20}
\end{aligned}
\]

Hence two independent sides have

\[
 \mathfrak B_L\mathfrak B_R\le(a+2)^2,\qquad
 \mathfrak B_L^\star\mathfrak B_R^\star\le{(a+1)^2\over4}.     \tag{21}
\]

When \(a=\Theta(L)\), both are \(\Theta(L^2)\), not \(L^3\).

There is also an exact decoder cancellation. In the unmarked full-cube bank,
the pair \((X,G)\) with \(S=T=\varnothing\) can occur at every pair of
depths, giving \(R_LR_R=\Theta(L^2)\) load. Thus the unmarked expansion and
the depth decoder have the same order. Last-role marking removes this load,
but also leaves only the \(\Theta(L^2)\) factor in (21).

For three binary roles on each side, the verifier finds

\[
\begin{array}{c|r}
\text{quantity}&\text{value}\\ \hline
M&64\\
E_{\rm merge}&576\\
\max_G d(G)&196\\
\max_{X,G}d(X,G)&9\\
E_{\rm marked}&64\\
\max_{X,G}d_{\rm marked}(X,G)&1.
\end{array}                                                     \tag{22}
\]

This is the finite equality pattern: the unmarked factor \(9\) is canceled
by depth-pair load \(9\), while the load-one marked factor is only \(1\) at
\(q=3\) and grows quadratically, not cubically, with \(q\).

## 4. Rational full-prefix-compatible double-bad regression

The full-cube hypothesis above is genuinely stretchable. On the left take

\[
 y=(-1,2),\qquad a=(0,0),\qquad c=(1,-1),                      \tag{23}
\]

and put every variable role label on the strict concave parabola

\[
                              p(x)=(x,-x^2),\qquad x>2.         \tag{24}
\]

For every word \(A=\{a,c\}\cup\{p_i\}\),

* \(A\) is a cap;
* \(A+y\) is not a cap, witnessed by the positive triple \(y,a,c\); and
* \(\{y,a\}\cup S\) is a cap for every subset \(S\) of all variable
  labels.

Reflect in the \(x\)-axis:

\[
 z=(-1,-2),\qquad b=(0,0),\qquad d=(1,1),\qquad
                              q(x)=(x,x^2).                     \tag{25}
\]

Then every right word \(B=\{b,d\}\cup\{q_i\}\) is a cup,
\(B+z\) is not a cup, and every \(\{z,b\}+T\) is a cup.

A positive shear makes both finite child lists increasing in both
coordinates without changing any determinant. A sufficiently small rational
strong glue then has, simultaneously,

\[
 A\cup B,\quad \{a,y,z,b\},\quad
 \{a,y,z,b\}\cup S\cup T\in\mathcal F(P)                       \tag{26}
\]

for every source word and every pair of variable downfaces. Thus (20)--(22)
are not abstract set-system artifacts.

The verifier uses three binary roles per side. It exhausts all 64 source
rectangles and all 4096 merged downfaces. Their exact rank distribution is

\[
 64t^4+384t^5+960t^6+1280t^7+960t^8+384t^9+64t^{10},
                                                                    \tag{27}
\]

which is exactly \(64t^4(1+t)^6\), as Theorem 1 predicts.

## 5. Fixed-gap \(K=3\) ledger

Let the ambient scale be \(n=2^L\). On each side choose

\[
 a=L,\qquad b=\lfloor L/4\rfloor,\qquad
 D=\left\lfloor{n\over L^6}\right\rfloor.                      \tag{28}
\]

Use \(a\) binary variable roles followed by \(b\) roles of size \(D\) in
the rational blocker construction. The number of sources on one side is
\(H=2^aD^b\), so the double-bad rectangle has

\[
\begin{aligned}
\log_2M
 &=2a+2b\log_2D\\
 &={1\over2}L^2-3L\log_2L+2L+O(L).              \tag{29}
\end{aligned}
\]

Its two source ranks are at most \(a+b+2<2L\). The complete support used by
both pockets is

\[
                 2(2a+bD+3)=O(n/L^5).                         \tag{30}
\]

Thus the record family has the exact \(K=3\) entropy and live logarithmic
rank while fitting inside two \(n/\operatorname{polylog}n\) pockets.
Nevertheless (20) gives

\[
             \mathfrak B_L\mathfrak B_R=L^2+O(L),\qquad
             \mathfrak B_L^\star\mathfrak B_R^\star
                         ={1\over4}L^2+O(L).                    \tag{31}
\]

This explains both relevant ledgers. At the parent endpoint-reset scale,
the half surplus gives a double-bad demand of order \(L^3V(P)\). The
regression does not turn its \(L^2\) choices into a low-load **one-face**
converter: \(S=T=\varnothing\) gives one common seam with load comparable
to the whole surviving record mass, and every depth-marked merged face still
erases all unexposed tail words. The load-one object is the ordered pair
\((X,G)\), whose ambient capacity is \(V(P)^2\), not \(V(P)\).

At a downstream two-face normalization, if the live entrance is only

\[
                             M\ge {V(P)^2\over L^3},             \tag{32}
\]

then even the optimistic load-one marked pair bank gives only

\[
                    E_{\rm marked}=\Theta(ML^2)
                                      \ge\Theta(V(P)^2/L),       \tag{33}
\]

which is fully compatible with the \(V(P)^2\) pair capacity. The unmarked
bank fares no better because its \(\Theta(L^2)\) depth-pair load cancels
its \(\Theta(L^2)\) expansion.

equations (32)--(33) show the same missing logarithm explicitly. More
generally, (12) says the exact two-face criterion is

\[
                 {M\over V(P)^2}\,
                 {\mathfrak B_L\mathfrak B_R\over\Delta_{XG}}>1.
                                                                    \tag{34}
\]

The maximum-child hypotheses alone do not force (34).

## 6. Scope and remaining positive branch

The regression is deliberately strongest for the operation being tested:
both rooted downsets are complete, the two sides are independent, and a
load-one depth-marked subbank exists. It still supplies only \(L^2\).

It is not a global counterexample to the half theorem. Putting every label
of a role cloud on one parabola makes the whole cloud convex and exposes a
large ambient Boolean bank. Tiny projective role clouds of arbitrary order
type preserve all selected transversal signs in (23)--(26), but then the
full ambient face recurrence depends on their cap/cup profiles. Proving that
this recurrence pays is precisely the coherent-profile child gate, not a
consequence of the merged-downface operation.

The exact positive residue is therefore narrower:

* \(\mathfrak B_L\mathfrak B_R\) must exceed the true \(L^3\)-scale loss;
* or one marked merged target must have unexpectedly small marginal load;
* or the external history must be decoded with another independent ordinary
  target; or
* the internal role-cloud face complexes must pay.

No third logarithm arises merely by multiplying the two maximum-child tries.

## 7. Verification

Run

```bash
python3 agent_outer_internal_product/verify_two_sided_merged_downface_maximum_child_gate.py
```

The verifier:

1. constructs the rational blocker gadgets and their rational strong glue;
2. exhausts the fixed-record product theorem and its graded rank enumerator;
3. checks the exact weighted trie factors, merged marginal loads, and
   depth-pair decoder loads;
4. verifies the load-one last-role marked subbank; and
5. checks the \(K=3\) entropy, support, rank, and \(O(L^2)\) aggregate ledger
   for \(32\le L\le128\).

It prints `PASS`.
