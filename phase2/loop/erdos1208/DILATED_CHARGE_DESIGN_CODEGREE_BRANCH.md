# A design-codegree branch for the dilated internal charge

## 1. Outcome

Let `A subset R^2` be distance-Sidon, `|A|=k`, put

\[
 \Sigma=A\mathbin{\oplus}A,
 \qquad N=|\Sigma|=\binom k2,
\]

and fix a realized difference `q` and its clean start set `H_q`.  Write
`h=|H_q|`, identify the plane with the complex line, and put

\[
 \lambda=3(1+i).
\]

The charge records are `(s,t) in H_q x Sigma`, with key `s+lambda t`.
Let `C_q` be the set of ordered pairs of distinct records with the same
key.  Then

\[
 \mathcal E_q=Nh+|C_q|.                         \tag{1.1}
\]

Every pair sum has a canonical unordered endpoint pair.  After fixing an
arbitrary order within each pair, a collision gives eight endpoint roles

\[
 (c,d,c',d',x,y,x',y')                         \tag{1.2}
\]

and the sparse relation

\[
 c+d-c'-d'+\lambda(x+y-x'-y')=0.               \tag{1.3}
\]

Stratify the rows by their equality pattern among the eight endpoint
labels.  Inside one pattern, merge equal roles and delete any resulting
zero coefficient.  For a pattern `P`, let `t_P` be the largest number of
its rows containing two prescribed role-label columns, and put

\[
 T_q=\max_P t_P.
\]

The design-matrix theorem gives the exact qualitative branch

\[
 \boxed{|C_q|\le C_8 k^2T_q}                   \tag{1.4}
\]

for an absolute constant `C_8` (one may take fewer than nine million).
Consequently

\[
 \boxed{T_q\le h k^{o(1)}
 \quad\Longrightarrow\quad
\mathcal E_q\le Nh k^{o(1)}.}                 \tag{1.5}
\]

For the global problem one may weaken the hypothesis further:

\[
 \boxed{T_q\le (|H_q|+k)k^{o(1)}
 \quad\hbox{for every }q}                       \tag{1.6}
\]

already resolves #1208.  Indeed, fibres with `|H_q|<=k` contribute at most
`O(k^3)` clean records in total and require no charge estimate.  On every
remaining fibre, (1.6) is the hypothesis of (1.5) up to a factor two.  The
charged fibres contribute `m^(2+o(1))`, so the exact centroid identity gives
third energy `k^(3+o(1))+m^(2+o(1))`.

Thus this branch proves the missing dilated resonance estimate.  Conversely,
any fixed-power failure of that estimate forces a single equality pattern,
two fixed endpoint roles, and two fixed labels of `A` to occur together in
more than `h k^epsilon` charge collisions.  The remaining obstruction is an
endpoint-rich core, not diffuse additive energy.

This is a reduction, not a complete solution of Erdős problem 1208.  The
finite-field parabola barrier shows that high two-role codegrees can occur
without radial uniqueness.  The next metric theorem must show that a
supercritical endpoint-rich core forces two distinct endpoint differences
to have equal Euclidean norm.

## 2. Equality-pattern matrices

Fix one equality pattern `P` among the eight roles in (1.2).  Its blocks
are the distinct point labels occurring in a row.  Add the coefficients in
(1.3) inside each block, and discard blocks whose coefficient becomes zero.
Suppose `r` active blocks remain, with fixed nonzero complex coefficients

\[
 \alpha_1,\ldots,\alpha_r,
 \qquad \sum_{j=1}^r\alpha_j=0.                 \tag{2.1}
\]

The labels in different blocks are distinct.  Make `r` disjoint role
copies of `A`.  Every collision of pattern `P` supplies a row with one
nonzero entry `alpha_j` in role `j`; equation (1.3) says that both the real
and imaginary coordinate vectors of `A` lie in the kernel.

Only the following simpler kernel is needed.  Assign a constant `z_j` to
every active column in role `j`.  This vector lies in the kernel whenever

\[
 \sum_{j=1}^r\alpha_jz_j=0.                    \tag{2.2}

Hence the matrix has corank at least `r-1`.  Patterns with `r<=2` supply no
rows: for `r=2`, (2.1) makes the relation a nonzero multiple of the
difference of two distinct labels.

## 3. Design-rank proof

Let `R` be the number of rows of one pattern, and assume `r>=3`.  Repeatedly
delete any active role-label column of degree less than

\[
 \tau={R\over2rk},                              \tag{3.1}
\]

together with its incident rows.  There are at most `rk` columns, so fewer
than `R/2` rows are deleted.  The remaining matrix has `m>=R/2` rows, every
active column has degree at least `tau`, and every two columns occur together
in at most `t_P` rows.  Every retained row uses every role, so all `r` roles
remain active and the corank is still at least `r-1`.

The Dvir--Saraf--Wigderson design-matrix theorem gives

\[
 \operatorname{corank}M
 \le {m t_P r(r-1)\over\tau^2}
 \le {4t_P r^3(r-1)k^2\over R}.                \tag{3.2}
\]

Comparing with the lower bound `r-1` yields

\[
 R\le4r^3t_Pk^2\le2048t_Pk^2.                 \tag{3.3}
\]

There are only `B_8=4140` equality partitions of eight roles.  Summing
(3.3) proves (1.4), with `C_8=2048 B_8<8.5*10^6`.

The design theorem used here is Theorem 1.3 of Dvir--Saraf--Wigderson,
*Improved rank bounds for design matrices and a new proof of Kelly's
theorem*, <https://arxiv.org/abs/1211.0330>.  As elsewhere in this project,
the large displayed constant is irrelevant; only its absoluteness matters.

## 4. Exact finite profiles

On the largest clean fibre of each stored family, the companion verifier
reports

\[
 (k,h,|C_q|,\#\text{patterns},T_q):
\]

\[
\begin{array}{c|rrrrr}
\text{family}&k&h&|C_q|&\#P&T_q\\ \hline
\text{closure }30&30&14&30&7&6\\
\text{closure }40&40&23&208&29&22\\
\text{Costas }22&22&34&72&25&11\\
\text{parabola image }43&43&171&2586&65&107
\end{array}                                      \tag{4.1}
\]

In every row `T_q<=h`.  The values are evidence only.  The theorem says
that a proof may discard all configurations with this behavior and focus on
a polynomial violation of `T_q<=h k^(o(1))`.

Run

```text
python3 phase2/loop/erdos1208/verify_dilated_charge_design_codegree_branch.py
```

The verifier constructs all collision rows, checks (1.3) with exact Gaussian
integer arithmetic, performs the equality-pattern mergers, and recomputes
all pattern-specific two-role codegrees.

## 5. Restart target

Classify the 28 pairs of original roles in (1.2), modulo the four pair
symmetries and swapping the two charge records.  For each surviving type,
prove a dichotomy:

1. its codegree is at most `(h+k) k^(o(1))`; or
2. its endpoint-rich rows create a fixed-power number of nontrivial equal
   norms among differences of `A`.

In view of (1.6), the sharp local target is the endpoint-codegree inequality

\[
 T_q\le (|H_q|+k)k^{o(1)}.                      \tag{5.1}
\]

Case 2 is impossible for a distance-Sidon set.  A proof must keep the clean
end-pair condition `s+q in Sigma`; the metric-free parabola shows that the
eight-role linear relation by itself does not control the high-codegree
branch.
