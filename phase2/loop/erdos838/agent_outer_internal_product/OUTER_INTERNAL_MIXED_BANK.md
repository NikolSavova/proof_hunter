# Erdős 838: a global outer--internal mixed bank

**Date:** 2026-08-14.  All logarithms are base two.

## Verdict

There is an exact way to remove the overload

\[
                         C D^3/H                              \tag{1}
\]

from the released-reservoir theorem.  It is genuinely global: attach the
outer context to an internal reservoir face and use the union as one
ordinary-face codeword.  If a context has merely `D^3/2` compatible
internal faces, its entire `D^2` record cell is paid, independently of the
number `C` of contexts and independently of how often the untagged internal
faces are reused.

The theorem below also identifies the exact geometric obstruction.  Under
the one-point insertion hypothesis, every failed outer--internal union has
a planar four-circuit of type `2+2` or `1+3`; there is no `3+1` type.  A
weighted four-circuit shadow gives a rigorous sufficient criterion for the
mixed bank to close fixed-power EIC'.

This does **not** close the general case.  The circuit criterion can fail
maximally.  There are rational planar examples with

\[
 C={2^r\choose r-4}=2^{(1-o(1))r^2}                         \tag{2}
\]

distinct outer contexts and one common internal reservoir for which every
context is compatible with only the empty set and the singletons.  In that
example every incompatibility is witnessed by the same outer guard pair.
The example is not a counterexample to EIC': its complete outer shield is
in convex position and has `2^(2^r)` ordinary faces.  Thus the unconditional
residual is now the sharp dichotomy

\[
 \boxed{\text{enough context-tagged mixed unions, or a released shield
 complex forced by concentrated planar four-circuits}.}       \tag{3}
\]

The first branch is proved here.  Deriving the shield complex in the second
branch for an arbitrary quadratic-entropy outer family remains open.

## 1. The exact mixed-bank telescope

Let `P=O disjoint_union X` be a labelled planar general-position set.  The
partition is only a decoder convention; no separation by a line is
assumed.  There are `C` contextual cells.  In cell `c` assume:

* there are exactly `D` distinct source faces and exactly `D` selected
  exterior repairs over each source, so the record set `G_c` has size
  `D^2`;
* a fixed actual source occurs in at most `Sigma` contextual cells;
* `A_c` is an ordinary-face bank with `|A_c|>=2D`, and a fixed ordinary
  face belongs to at most `Lambda` of the banks `A_c`;
* `R_c subseteq O` is an ordinary outer carrier.  A fixed mixed ordinary
  face introduced below belongs to at most `Omega` contextual mixed banks.
  In the main application the carriers are pairwise distinct, which forces
  `Omega=1`.

Let `H subseteq F(P)` be a common internal reservoir whose members are
subsets of `X`.  Define

\[
 \begin{split}
 M_c&=\{R_c\cup F:F\in H,\ R_c\cup F\in F(P)\},\\
 q_c&=|M_c|,\qquad b={D^3\over2},\\
 \delta_c&=1-\min\{1,\sqrt{q_c/b}\},\qquad
 \bar\delta={1\over C}\sum_c\delta_c .             \tag{4}
 \end{split}
\]

Use `ceil(D^3/2)` instead of `b` when `D` is odd.  The present application
has `D` a power of two.

> **Theorem 1 (global outer--internal mixed-bank theorem).**  Under the
> preceding assumptions,
> \[
>       \boxed{|G|\le
>       \bigl(\sqrt{\Lambda\Omega}+\Sigma D\bar\delta
>                     +\Sigma D^{-1}\bigr)V(P).}            \tag{5}
> \]
> Consequently, if `Lambda,Omega,Sigma=n^o(1)` and for some absolute
> `epsilon>0`
> \[
>                    \bar\delta\le n^{o(1)}D^{-\epsilon},   \tag{6}
> \]
> then
> \[
>                    |G|\le n^{o(1)}D^{1-\epsilon}V(P),     \tag{7}
> \]
> after decreasing `epsilon` harmlessly.  In particular, if every context
> has `q_c>=D^3/2`, then the whole family has the stronger bound
> `|G|<=(sqrt(Lambda Omega)+Sigma D^-1)V(P)`.

**Proof.**  When the carriers are distinct, the mixed banks are globally
disjoint.  Indeed a member `U` of `M_c` determines

\[
                         R_c=U\cap O,\qquad F=U\cap X.       \tag{8}
\]

Thus no ordinary face lies in two `M_c`.  In the general stated form their
overlap is `Omega` by hypothesis.
For each cell retain an arbitrary subfamily of

\[
              m_c=\min\{D^2,\lfloor\sqrt{|A_c|q_c}\rfloor\} \tag{9}
\]

records.  It satisfies `m_c^2<=|A_c||M_c|`.  The recoverable-cell Cauchy
telescope, with overlaps `Lambda` and `Omega`, gives

\[
                 \sum_c m_c\le\sqrt{\Lambda\Omega}V(P).    \tag{10}
\]

Because `|A_c|>=2D`, (4) and (9) give

\[
             D^2-m_c\le D^2\delta_c+1.                     \tag{11}
\]

There are at least `CD/Sigma` distinct actual sources, and they are
themselves ordinary faces, so `V(P)>=CD/Sigma`.  Summing (11) and using
this inequality gives

\[
 \sum_c(D^2-m_c)
       \le CD^2\bar\delta+C
       \le(\Sigma D\bar\delta+\Sigma D^{-1})V(P).           \tag{12}
\]

Equations (10)--(12) prove (5).  Equation (7) follows from (5)--(6).
QED.

The theorem is the exact multiplication missing from the cyclic allocation
in the base-retention report.  There, the same internal face used by every
context has overlap `C`.  Here `R_c union F` is a different labelled
ordinary face for each outer carrier, so the overlap is one.  Only
`D^3/2` compatible faces per context are needed; the full reservoir may be
much larger, and no density assumption of the form `q_c/H=Omega(1)` occurs.

The theorem is nonlocal in the required sense.  `R_c union F` need not
belong to a repair neighbourhood, retain the ancestor base, or retain the
two tangent guards.  It only has to be an ordinary convex subset of the
ambient point set and to recover the carrier by the fixed label partition.

## 2. Four-circuits are the complete defect certificate

Write

\[
 d_H(S)=|\{F\in H:S\subseteq F\}|.                          \tag{13}
\]

Assume in addition that every internal label which occurs in `H` is a
valid one-point extension of every outer carrier:

\[
                 R_c\cup\{x\}\in F(P)
       \quad(c\in[C],\ x\in\bigcup H).                      \tag{14}
\]

For `T subseteq R_c` and `S subseteq X`, call `(T,S)` a bad split circuit
when `|T|+|S|=4` and `T union S` is not in convex position.  Put

\[
 \Xi_c=
 \sum_{\substack{T\subseteq R_c,\ |T|=1,2}}
 \ \sum_{\substack{S\subseteq X,\ |S|=4-|T|\\
                    T\cup S\text{ nonconvex}}}
                         d_H(S).                            \tag{15}
\]

> **Theorem 2 (weighted four-circuit defect bound).**  Under (14),
> \[
>                         |H|-q_c\le\Xi_c.                  \tag{16}
> \]
> Every incompatible pair `(R_c,F)` has a witness of exactly one of the
> two types
> \[
>          |T|=2,|S|=2\qquad\hbox{or}\qquad |T|=1,|S|=3.    \tag{17}
> \]
> In particular, a sufficient condition for (6) is
> \[
> {1\over C}\sum_c
> \left[1-min\left\{1,
> \sqrt{{2(|H|-\Xi_c)_+\over D^3}}\right\}\right]
>                 \le n^{o(1)}D^{-\epsilon}.               \tag{18}
> \]

**Proof.**  If `R_c union F` is nonconvex, planar Caratheodory gives a
nonconvex four-subset `Q`.  The four points cannot all lie in `R_c` or all
lie in `F`, since both are ordinary faces.  Three points in `R_c` and one
point `x` in `F` are also impossible by (14).  Hence `Q=T union S` has one
of the two splits in (17).  Its internal trace `S` lies in `F`, so the term
`d_H(S)` in (15) counts this failed face.  Summing over all split circuits
can only overcount the failed faces, proving (16).  Substitute
`q_c>=(|H|-Xi_c)_+` into (4) and use Theorem 1 to obtain (18).  QED.

There is an exact non-overcounted version.  Fix a total order on labelled
four-sets and assign every failed pair `(c,F)` its first bad split circuit.
If `omega_c(T,S)` is the number of failed faces assigned to `(T,S)`, then

\[
 |H|-q_c=\sum_{T,S}\omega_c(T,S),\qquad
 0\le\omega_c(T,S)\le d_H(S).                              \tag{19}
\]

Thus a failure of (18) is not an unspecified geometric pathology: it is a
large, explicitly certifiable weighted family of rooted planar `2+2` and
`1+3` circuits.  The still-missing shield theorem must turn concentration
of (19), together with quadratic outer-context entropy, into an ordinary
face complex.  Merely counting the at most `n^4` circuit labels loses a
fixed power at the capped scale and is not enough.

## 3. A scalable sparse cross-union family

The compatibility hypothesis in Theorem 1 is not automatic, even when
there are quadratically many genuine one-pocket contexts.

Fix `r>=5`, put `D=2^r`, and let

\[
 u=(-1,0),\quad v=(1,0).
\]

On the lower parabola `y=x^2-1`, choose a common vertex `w` and `D`
additional rational points `Q`; together with `u,v` they are in convex
position and `uv` is their upper edge.  For every `(r-4)`-subset `J` of
`Q`, let

\[
                         B_J=\{u,v,w\}\cup J.               \tag{20}
\]

Thus `|B_J|=r-1` and the number of outer contexts is (2).

Above `uv`, choose a rational strict insertion chain

\[
 x_i\in\operatorname{int}\operatorname{conv}\{u,v,x_j\}
                         \quad(i<j),                         \tag{21}
\]

of length `2D`.  For every `J` and `1<=i<=D`, the rank-`r` source

\[
                         A_{J,i}=B_J\cup\{x_i\}              \tag{22}
\]

has the `D` selected exterior repairs `x_j`, `D<j<=2D`, with repaired hull
`B_J union {x_j}`.  Add generic rational padding inside the common triangle
`uvw` until `n=2^(2r)`.  It changes none of these hull identities, and the
selected cap is exactly `n/2^r=D`.

Let `H=F(X)` be the complete internal face complex of the chain.  For every
context,

\[
 B_J\cup F\text{ is convex}\quad\Longleftrightarrow\quad |F|\le1,\qquad
                         q_J=2D+1.                           \tag{23}
\]

Indeed (21) makes the earlier of any two chain points nonextreme in the
presence of `u,v` and the later point.  Conversely, one chain point joins
the lower convex polygon.  Every failed face of size at least two has the
`2+2` witness

\[
                         \{u,v,x_i,x_j\}.                    \tag{24}
\]

The universal planar convex-subset bound gives

\[
       |H|\ge2^{(1/4-o(1))(\log(2D))^2}\gg D^3,             \tag{25}
\]

so (23) misses the mixed-bank threshold by a superpolynomial factor even
though (2) has quadratic entropy.

This is not an EIC' counterexample.  The lower set
`{u,v,w} union Q` is itself in convex position, and therefore

\[
                         V(P)\ge2^{D+3}.                     \tag{26}
\]

The selected record count is only
`C D^2=2^{O(r^2)}`, far below (26).  The outer shield bank pays with
double-exponential room.  The construction instead proves two useful
negative facts:

1. quadratic context entropy does not imply even a tiny density of
   cross-union edges; and
2. the four-circuit branch of (3) must be allowed to charge an unrestricted
   global shield complex rather than a base-retaining local bank.

Replacing the convex lower cloud in this example by a low-`V` family while
preserving (20)--(24), and keeping the shield bank small, would produce a
candidate counterexample to fixed-power EIC'.  No such realizable family is
known here.  Constructing it is essentially the surviving outer-shield
problem, not a consequence of insertion-chain universality alone.

## 4. Relation to the other banked reductions

Theorem 1 plugs directly into the cross-atom square lift.  Its first bank is
the rooted-atom/protected-window bank of size at least `2D`, whose contextual
overlap is polynomial.  The mixed bank replaces the repeated released
internal bank.  When `q_c>=D^3/2`, the local square inequality is

\[
                         D^4\le(2D)q_c,                      \tag{27}
\]

and the outer label makes the second-bank overlap one.  Hence the spread
among atoms, variation of bases, and the `C D^3/H` allocation loss all
disappear simultaneously.

Combined with the fixed-power gate, (18) would close the leading
coefficient `1/2` for Erdős 838.  What is conditional is precisely (18), or
an alternative shield theorem for its failure.  No claim that (18) holds
for every planar repair family is made.

## 5. Exact verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_outer_internal_mixed_bank.py
```

The checker performs four independent audits:

* exact integer stress tests of Theorem 1 and its floor loss;
* a dense rational cross-union model in which mixed faces recover the outer
  carrier with overlap one;
* a rational 20-point projective insertion chain combined with 56 distinct
  lower-parabola contexts, verifying (21)--(24) and every `2+2` witness;
* the weighted circuit inequality (16), using the exact internal convex-face
  rank profile (`H=4,775`) of the 20-point record.
