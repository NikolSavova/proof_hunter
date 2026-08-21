# Dyadic density gate for endpoint completion boxes

## 1. Outcome

This note gives an exact dyadic decomposition for the completion-square
model in `SWAP_ENDPOINT_REVERSE_STAR_INCIDENCE_GATE.md`.  It does not prove
the final endpoint estimate.  It removes all low-*group-load* records at
the target scale, gives a conditional low-corner-reuse charge, and gives an
independent quadratic-footprint charge for nonmatching endpoint stars.
The completion-vertex reservoir and the centred parallel-wedge mass are
kept distinct.

Let

\[
 \mathcal V_K=\{(r,A,B):r\in\mathcal P_K,
       A,A+r,B,B+Jr\in D\},
 \qquad W_\square=|\mathcal V_K|.                \tag{1.1}
\]

Let `W_parallel` retain its earlier meaning: the centred parallel-wedge
mass `sum_{C,t} binom(|Q_{C,t}|,2)`.  No comparison between `W_square` and
`W_parallel` is asserted.  Exact endpoint double counting gives

\[
 \sum_g\lambda_g\le8W_\parallel.                 \tag{1.1a}
\]

Write `mathscr R_g` for the reverse endpoint records in one group
`g=(C,x,u)`, and put

\[
 \lambda_g=|\mathscr R_g|,
 \qquad b_g=\lambda_g-\max_t a_{g,t}.             \tag{1.2}
\]

Choose one largest `t`-fibre and call all other records *residual*.  Then

\[
 \mathcal G_2=\sum_g\lambda_g b_g                 \tag{1.3}
\]

is literally the load-weighted number of residual records.

Every record `e` has the four distinct completion corners

\[
 \square(e)=\{v,\mathsf H_uv,\mathsf Vv,
                   \mathsf H_u\mathsf Vv\}\subset\mathcal V_K. \tag{1.4}
\]

Let `d(v)` be the number of all reverse endpoint records whose square
contains `v`.  For dyadic `L` and any real `R>=1`, let

\[
 \mathscr L_{L,R}=\{e:\ e\hbox{ is residual},\quad
       L\le\lambda_{g(e)}<2L,\quad
       \min_{v\in\square(e)}d(v)<R\}.             \tag{1.5}
\]

The low-reuse completion theorem is

\[
 \boxed{
 \sum_{e\in\mathscr L_{L,R}}\lambda_{g(e)}
       <2LRW_\square .}                           \tag{1.6}
\]

The target-scaled unconditional regularization is instead

\[
 \boxed{
 \sum_{g:\lambda_g<P}\lambda_gb_g
 \le8P W_\parallel.}                              \tag{1.6a}
\]

Thus only groups of super-subpolynomial load can obstruct the desired
bound.  In a dyadic band `L<=lambda_g<2L`, let `mathscr H_{L,R}` be the
residual records whose four corners all have reuse at least `R`.  The
exact combined inequality is

\[
 \boxed{
 \mathcal G_{2,L}
 \le2LRW_\square+2L|\mathscr H_{L,R}|,}           \tag{1.6b}
\]

and independently `mathcal G_{2,L}<=16L W_parallel`.  Formula (1.6b) is
useful when the active completion reservoir is economical; it does not by
itself prove that low reuse closes at the target scale.

There is a second exact charge.  Canonically assign every residual record
to one of its at most four physical endpoint roles.  For a fixed group,
fixed base start `X`, and fixed role, let `T_sigma` be the surviving
neighbour-displacement set and put `h_sigma=|T_sigma|`.  Its translated
quadratic footprint is

\[
 \Phi_\sigma=
 \{2H_C-2JX+Jt_1+Lt_2:t_1,t_2\in T_\sigma\}
 \subset D+D.                                     \tag{1.7}
\]

For a collection `mathfrak S` of such stars define its footprint depth

\[
 \Delta(\mathfrak S)=
 \max_{z\in D+D}|\{\sigma\in\mathfrak S:z\in\Phi_\sigma\}|. \tag{1.8}
\]

If every group in `mathfrak S` has load below `2L` and every star has
`H<=h_sigma<2H`, then its contribution to (1.3) is at most

\[
 \boxed{
 \sum_{\sigma\in\mathfrak S}\lambda_{g(\sigma)}h_\sigma
 \le {4L\Delta(\mathfrak S)|D+D|\over H}.}       \tag{1.9}
\]

Thus an excessive nonmatching star band forces one point of `D+D` to lie
in many translated `JT+LT` footprints.  The exact survivor is now:

1. high-load, matching-heavy stars (`H` small), possibly with almost
   disjoint completion vertices;
2. a high-depth common footprint; or
3. a dense high-reuse completion core.

The first branch is the immediate danger; Section 4.1 shows why the most
obvious sumset charge does not remove it.  The last two are the starting
points for a label-preserving dependent-random-choice or density-increment
argument.  Ordinary unlabelled box energy is still too coarse.

## 2. Proof of the completion-corner charge

Assign every record in `mathscr L_{L,R}` to one of its completion corners
having degree below `R`.  A vertex receives fewer than `R` records, so

\[
 |\mathscr L_{L,R}|<R|\mathcal V_K|.              \tag{2.1}
\]

The weight of every assigned record is `lambda_g<2L`.  Multiplying (2.1)
by `2L` proves (1.6).

The complementary residual records are exactly `mathscr H_{L,R}`, proving
(1.6b).  For (1.6a), use `b_g<=lambda_g<P` and (1.1a).  Likewise, in one
dyadic band,

\[
 \mathcal G_{2,L}
 \le2L\sum_{g\text{ in band}}b_g
 \le2L\sum_g\lambda_g
 \le16L W_\parallel.                              \tag{2.2}
\]

There is still a genuine density consequence in the high-corner branch.
Every record has four corners, so

\[
 \sum_{v\in\mathcal V_K}d(v)=4\sum_g\lambda_g
 \le32W_\parallel.                                \tag{2.3}
\]

Hence the set of vertices of reuse at least `R` has size at most
`32W_parallel/R`.  Every square in `mathscr H_{L,R}` lies entirely inside
this smaller vertex set.  No independence or geometric estimate enters
this conclusion, but a further labelled incidence theorem is needed to
turn it into the target bound.

## 3. Proof of the footprint charge

For one star, the role set `T_sigma` is vector-Sidon.  The energy identity

\[
 Jt_1+Lt_2=Jt_3+Lt_4
 \quad\Longleftrightarrow\quad
 t_1-t_3=(I-J)(t_4-t_2)                            \tag{3.1}
\]

therefore gives

\[
 E_+(JT_\sigma,LT_\sigma)\le2h_\sigma^2-h_\sigma.
                                                               \tag{3.2}
\]

Cauchy--Schwarz yields

\[
 |\Phi_\sigma|
 \ge{h_\sigma^4\over2h_\sigma^2-h_\sigma}
 \ge {h_\sigma^2\over2}.                         \tag{3.3}
\]

Double-counting footprint incidences gives

\[
 {1\over2}\sum_{\sigma\in\mathfrak S}h_\sigma^2
 \le\sum_{\sigma\in\mathfrak S}|\Phi_\sigma|
 \le\Delta(\mathfrak S)|D+D|.                   \tag{3.4}
\]

Since `h_sigma>=H`,

\[
 \sum_{\sigma\in\mathfrak S}h_\sigma
 \le {1\over H}\sum_\sigma h_\sigma^2
 \le {2\Delta(\mathfrak S)|D+D|\over H}.        \tag{3.5}
\]

Finally `lambda_g<2L`; multiplying (3.5) by `2L` proves (1.9).

## 4. What remains

The high-corner branch must use the simultaneous richness of all four
corners.  Around a completion vertex `v=(p,X,ell)`, the horizontal choices
`u` and vertical choices `q` form the exact link matrix

\[
\begin{aligned}
 &(p-u,X+u,\ell)\in\mathcal V_K,\\
 &(q,X,\ell+L(p-q))\in\mathcal V_K,\\
 &(q-u,X+u,\ell+L(p-q))\in\mathcal V_K.          \tag{4.1}
\end{aligned}
\]

High corner reuse means that many cells of these labelled link matrices
are occupied.  The selected cells coming from one group lie on the affine
slice `q=c-X` and share the physical endpoint `x`.  A valid density
increment must keep both facts.

The immediate proof-or-kill target is therefore:

> In a high-load dyadic band with matching-heavy fixed-`X` stars, either
> pay the low-reuse matching population directly from its endpoint labels,
> or show that a large population of selected high-reuse cells in (4.1)
> contains a common labelled rectangle whose endpoint-Sidon footprint pays
> for it.

The known abstract matching rectangles are not enough: geometric
realizability, all four completion vertices, adaptive popularity, and the
physical endpoint colour must remain present.

### 4.1 A genuine matching cross-support shortcut is false

It is tempting to replace the fixed-`X` footprint by the cross-sum of all
`Y` and `Z` values in a matching-heavy group.  The hoped-for assertion
would be `|Y+Z|>>lambda_g^2`.  This is false even on a genuine small
distance-Sidon set.

For the genuine distance-Sidon transformed Costas-23 set, take

\[
 C=((14,-11),(50,33)),\qquad x=(-124,-80),\qquad u=(0,23). \tag{4.2}
\]

After deleting one largest `t`-fibre, one endpoint role contains the two
exact reverse rows

\[
\begin{array}{c|c|c|c}
X&t&Y&Z\\ \hline
(-9,-11)&(-69,23)&(27,-13)&(-42,10)\\
(37,-57)&(-23,23)&(-19,-13)&(-42,10).
\end{array}                                        \tag{4.3}
\]

The `X` and `t` coordinates are both injective, so this is a literal
two-edge matching.  All six translated difference conditions, all four
adaptive-popular corners, all four completion vertices, and the common
physical endpoint hold.  Nevertheless `Z` is constant and

\[
 |Y+Z|=2                                             \tag{4.4}
\]

rather than four.  Thus a proof cannot use an unqualified `Y+Z` support
bound, even in the matching branch.  It must exploit reuse of the complete
four-corner squares or introduce another coordinate before taking support.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_completion_box_dyadic_density.py
```

The verifier exhausts random finite grouped four-corner systems for (1.6),
(1.6a)--(1.6b), and (2.2)--(2.3), checks the exact residual identity, verifies the footprint
energy and depth inequalities on vector-Sidon endpoint-role sets, and
checks every assertion in the genuine Costas-23 barrier (4.2)--(4.4).
