# Cross-core capped pairs: scale separation and the exact proper-downshadow gate

**Date:** 2026-08-14.  All logarithms are base two.

## Verdict

There are two different targets which must not be conflated.

* At the coefficient scale, where an ordered-pair decoder may have fibre
  `2^o(r^2)`, cross-core selected records are already trivial.  Sending the
  two records to their two actual source faces has fibre at most `d^2`;
  for `r=(alpha+o(1))log n` this is only `2^O(r)=2^o(r^2)`.
* At the global-EIC scale, the desired congestion is `2^o(r)=n^o(1)`.
  Source projection loses `d=n^(1-alpha+o(1))=2^Theta(r)` and is useless.
  Here proper source downfaces give an exact Hall theorem, but only when a
  codimension shadow has small global overlap.  Failure fixes a common
  proper prefix shared by too many different cores.

The exact downshadow theorem is proved below.  It also exposes a sharp
threshold: below `alpha=1/2`, even all Boolean proper downfaces of one
rank-`r` source have fewer code symbols than its cap, so core downfaces
alone cannot solve EIC.  At and above `1/2`, the only issue is cross-core
prefix multiplicity.

There is a scalable planar exterior-repair family on which every fixed
codimension proper-downshadow route has huge congestion.  It is not an EIC
counterexample because the released lower convex arc has an enormous full
face complex, and it is not in the low-addable hard class.  It rigorously
shows that a proof must credit the **full released core complex** (or mixed
forward targets), rather than only a chosen rank of proper source
downfaces.

## 1. The coefficient-scale cross-core theorem is automatic

Let `Omega` be a unit-weight selected family of repair records, with source
map

\[
                     \sigma:\Omega\longrightarrow\mathcal F_r(P),
\]

and assume the cap

\[
                 |\sigma^{-1}(A)|\le d\qquad(A\in\mathcal F_r(P)). \tag{1}
\]

> **Theorem 1 (source-pair code).**  The map
> \[
>            (e,f)\longmapsto(\sigma(e),\sigma(f))            \tag{2}
> \]
> from ordered record pairs to ordered ordinary-face pairs has fibre at
> most `d^2`.  The same statement holds for weights whose total over each
> source is at most `d`.

**Proof.**  Over a fixed ordered source pair `(A,B)`, the number of unit
record pairs is at most `d^2`.  In the weighted case their total weight is
at most

\[
 \left(\sum_{\sigma(e)=A}a_e\right)
 \left(\sum_{\sigma(f)=B}a_f\right)\le d^2.                  \tag{3}
\]

QED.

If `r=(alpha+o(1))L`, `L=log n`, and `d=2^(L-r+o(L))`, then

\[
 \log d^2=2(L-r)+o(L)
          =\left({2(1-\alpha)\over\alpha}+o(1)\right)r
          =o(r^2).                                           \tag{4}
\]

Thus no guard release is needed for a `2^o(r^2)` two-face theorem.  This
observation is **not useful for EIC**, which needs the much smaller
`2^o(r)` loss.

## 2. Exact proper-downshadow Hall theorem

For `0<=t<=r`, join a record `e` to every codimension-`t` downface of its
source:

\[
             N_t(e)=\{S:S\subseteq\sigma(e),\ |S|=r-t\}.     \tag{5}
\]

Every member of `N_t(e)` is an ordinary convex face by heredity.  Put

\[
 b_t={r\choose t},\qquad
 \Delta_t=\max_{|S|=r-t}
       |\{e\in\Omega:S\subseteq\sigma(e)\}|.                 \tag{6}
\]

> **Theorem 2 (global proper-downshadow routing).**  There is a map
> `phi_t:Omega->F(P)` with `phi_t(e) in N_t(e)` and maximum fibre
> \[
>                 K_t\le\left\lceil{\Delta_t\over b_t}\right\rceil. \tag{7}
> \]
> Consequently ordered pairs of records map coordinatewise to two
> ordinary faces with fibre at most `K_t^2`.

**Proof.**  In the bipartite graph (5), every left degree is `b_t` and
every right degree is at most `Delta_t`.  For every left set `U`, edge
counting gives

\[
                 b_t|U|\le\Delta_t|N(U)|.                    \tag{8}
\]

Replace every right vertex by `ceil(Delta_t/b_t)` copies and apply Hall's
theorem.  Taking the product of the two resulting maps proves the pair
statement.  QED.

For fractional weights the identical proof is obtained by rational
replication and a limit; equivalently it is the standard fractional
`b`-matching theorem.

Let `S` be the distinct source family and define its prefix multiplicity

\[
 \Lambda_t=\max_{|D|=r-t}|\{A\in S:D\subseteq A\}|.          \tag{9}
\]

The cap gives `Delta_t<=d Lambda_t`, so

\[
             \boxed{K_t\le
              \left\lceil{d\Lambda_t\over\binom rt}\right\rceil.} \tag{10}
\]

This is the precise proper-core gate.  It is a global-EIC theorem because
it uses arbitrary ordinary source downfaces.  It applies to a narrower
local RPH only if those downfaces are included in the record's permitted
local target neighbourhood.

## 3. The linear-codimension threshold

Write `t=(tau+o(1))r`.  Then

\[
 \log {r\choose t}=(H_2(\tau)+o(1))r,
 \qquad
 \log d=\left({1-\alpha\over\alpha}+o(1)\right)r.            \tag{11}
\]

Therefore (10) has `K_t=2^o(r)` whenever

\[
 \log\Lambda_t\le
 \left(H_2(\tau)-{1-\alpha\over\alpha}\right)r+o(r).        \tag{12}
\]

This yields three regimes.

1. If `alpha>1/2`, choose `tau` with
   `H_2(tau)>(1-alpha)/alpha`.  Proper downfaces have enough local symbols;
   only the global prefix multiplicity in (12) remains.
2. If `alpha=1/2`, the largest binomial coefficient is
   `2^r/Theta(sqrt(r))`.  The unavoidable local loss is only
   `Theta(sqrt(r))=2^o(r)`, so subexponential `Lambda_t` is still harmless.
3. If `alpha<1/2`, even the complete Boolean reservoir has
   `2^r<d` symbols.  No map which assigns one proper source downface to each
   selected record can have `2^o(r)` load, already for one source attaining
   the cap.  A blocker/pocket face reservoir is mandatory.

Theorem 2 is also an exact recurse certificate.  If (12) fails, there is a
specific proper prefix `D` of size `r-t` contained in `Lambda_t` source
cores and carrying `Delta_t` selected records.  A valid heavy branch must
retain that prefix and descend on the `t` released labels; it cannot call
the collision an unstructured cross-core event.

## 4. A planar barrier to fixed-codimension downshadows

The prefix multiplicity in (10) cannot be bounded for arbitrary planar
exterior repairs.

Take

\[
 u=(-1,0),\quad v=(1,0),
\]

and put `m` points `Y={y_1,...,y_m}` on the strict lower parabola arc
`y=x^2-1`, with `-1<x<1`.  Every

\[
                 B_S=\{u,v\}\cup S,qquad S\in{Y\choose k}, \tag{13}
\]

is a convex core with upper hull edge `uv`.  Above `uv`, put a strict
insertion chain `x_0<x_1<...<x_N`.  Then every `B_S+x_i` is convex and

\[
 B_S+x_i\longrightarrow B_S+x_j\qquad(i<j)                  \tag{14}
\]

is a genuine exterior repair which hides `x_i` and retains `B_S`.

Fix the source tip `x_0`, and above every source `B_S+x_0` select the same
`d<=N` successors.  The selected family has

\[
                         |\Omega|=d{m\choose k}.              \tag{15}
\]

Its sources have rank `r=k+3`.  The union of all codimension-`t` source
downfaces has exactly

\[
 U_t=\sum_{\substack{0\le a\le\min(3,r-t)\\
                      0\le r-t-a\le k}}
             {3\choose a}{m\choose r-t-a}                    \tag{16}
\]

members: choose `a` of the three common labels `u,v,x_0` and the remaining
labels from `Y`.  Hence every map restricted to those proper downfaces has
maximum fibre at least

\[
             \boxed{{d\binom mk\over U_t}.}                  \tag{17}
\]

For `m` much larger than `r` and any `t>3`, the dominant term in (16) has
`r-t` lower-arc labels, while the sources have `k=r-3` such labels.  Thus
the ratio grows roughly as

\[
             d\left({m\over r}\right)^{t-3}                 \tag{18}

up to `2^O(r log r)` factors.  With `m=Theta(n)`,
`r=Theta(log n)`, and `t=Theta(r)`, this is
`2^Theta(r^2)`, far beyond EIC tolerance.  Deleting either tangent guard is
already included in (16), so merely saying “use proper downfaces” or
“release the guards” does not fix the collision.

This is a barrier to the **fixed-rank downshadow architecture**, not to
Erdos 838 or to global EIC.  The full lower-arc set `Y` is in convex
position and contributes all `2^m` ordinary faces, overwhelmingly more
than (15).  Moreover the sources have many addable omitted `Y` labels, so
they are outside the low-addable hard branch.  A correct global proof must
transfer the heavy prefix collision to that full released face complex;
restricting the target pool to (16) throws the paying capacity away.

## 5. Exact residual after proper guard release

At `2^o(r^2)` pair-fibre scale there is no residual: Theorem 1 closes all
cross-core pairs.

At the useful EIC scale, Theorem 2 closes the light-prefix branch.  What
remains is the following heavy-prefix alternative:

\[
 \boxed{\begin{array}{c}
 \text{a proper prefix }D\text{ is shared by too many cores;}\\
 \text{charge the complete convex-face complex on the released labels,}\\
 \text{or produce forward mixed core--pocket faces.}
 \end{array}}                                               \tag{19}
\]

The planar family above proves that the word “complete” is essential.  It
does not supply a hard low-addable counterexample.  Thus a scalable barrier
to (19) would have to combine quadratic core entropy, low addable degree,
and severe overlap of the *full* released complexes.  Constructing that
would be a genuinely new OAI barrier; it does not follow from retained
guards or from universal same-edge histories.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_linear_codim_capped/verify_cross_core_downshadow.py
```

The checker exhausts small source set-systems and verifies the duplicated-
Hall inequality, checks the exact shadow-union formula (16), constructs the
planar repair family with rational coordinates, and audits the linear-
codimension entropy thresholds.
