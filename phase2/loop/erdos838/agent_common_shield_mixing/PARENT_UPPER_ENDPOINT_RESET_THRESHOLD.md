# Parent upper bounds force an endpoint reset exactly at coefficient one half

**Date:** 2026-08-15.  All logarithms are base two and all face counts are
nonempty.

## Verdict

There is an exact quantitative use of the parent fixed-gap upper bound in
the canonical two-child all-delete state, but it produces **endpoint energy**,
not yet ordinary faces.

Let \(P=A\prec B\) be a vertical strong glue, put \(a=|A|,b=|B|\), and
write \(W,C,U\) for ordinary, cap, and cup counts in the glue chart.  Then

\[
 \boxed{
 C(P)U(P)\ge
 \left(\sqrt{(b+1)W(A)}+\sqrt{(a+1)W(B)}\right)^2 .}
                                                               \tag{1}
\]

In the balanced mirror state \(a=b=m\), \(W(A)=W(B)=H\), this is

\[
                       C(P)=U(P),\qquad C(P)U(P)\ge4(m+1)H.     \tag{2}
\]

For

\[
              \Phi_{\beta,K}(L)=\beta L^2-KL\log L            \tag{3}
\]

and \(2m=2^L\), the child lower bound
\(H\ge2^{\Phi_{\beta,K}(L-1)}\) gives

\[
\boxed{
 \log(C(P)U(P))-\Phi_{\beta,K}(L)
 \ge (1-2\beta)L+(1+\beta)
       +K\{L\log L-(L-1)\log(L-1)\}.}                         \tag{4}
\]

Thus the threshold is exactly one half:

* if \(\beta<1/2\), the endpoint surplus is \(n^{1-2\beta-o(1)}\);
* if \(\beta=1/2\), it is at least \(2^{3/2}L^K\); and
* for \(\beta>1/2\), the child lower bound alone no longer puts the parent
  endpoint product at the parent target.

Consequently a genuine fixed-gap counterexample in this normal form cannot
be a low-endpoint Pascal cell.  It must be a **high endpoint-energy terminal
reset**: the ordinary face count is below the target while the product of
its two directional profiles is above it by the factor in (4).

This does not yet close the proof.  A map from all cap--cup pairs to ordinary
faces with decoder load \(\Lambda\) would close whenever

\[
 \log\Lambda<(1-2\beta)L+(1+\beta)+K\Delta_L,
 \quad
 \Delta_L=L\log L-(L-1)\log(L-1),                             \tag{5}
\]

but the all-delete rectangle supplies no such map.  Its terminal output
load cancels the complete source factor exactly.

Both qualifications are sharp.

1.  An exact integral scalar family attains equality in (1), obeys every
    elementary endpoint constraint (including the rank-two baseline), has
    dense noncap \(\times\) noncup sides, satisfies the child lower bound and
    parent upper bound, and stores precisely the surplus (4).  A planar
    realization of that family below coefficient one half would itself be
    a major upper construction.
2.  There is an exact stretchable planar leading-coefficient calibration at
    \(\beta=1/2\): put two copies of the known balanced iterated cup--cap upper
    construction in one strong glue.  Almost every child face lies on each
    all-delete side, all ranks are \(O(\log n)\), and the canonical common
    triple has linear root degree.  The parent still has coefficient
    \(1/2+o(1)\).  Hence no leading-coefficient, density, rank, or canonical-
    root argument can exclude the phenotype; the fixed-gap polylogarithmic
    conversion in (5) is genuinely load-bearing.

The positive result is therefore an exact **parent-upper endpoint-reset
theorem**, not a completed ordinary-face bank.

## 1. Exact two-block endpoint reset

The strong-glue identities are

\[
\begin{aligned}
 W(P)&=W(A)+W(B)+C(A)U(B),\\
 C(P)&=C(B)+(b+1)C(A),\\
 U(P)&=U(A)+(a+1)U(B).                                \tag{6}
\end{aligned}
\]

Every ordinary face has a canonical upper-cap/lower-cup decomposition, so

\[
                    W(A)\le C(A)U(A),\qquad
                    W(B)\le C(B)U(B).                         \tag{7}
\]

Put \(x=C(A)\) and \(y=U(B)\).  Equations (6)--(7) imply

\[
\begin{aligned}
 C(P)U(P)
 &\ge \left({W(B)\over y}+(b+1)x\right)
         \left({W(A)\over x}+(a+1)y\right)\\
 &= {W(A)W(B)\over xy}+(a+1)W(B)+(b+1)W(A)
       +(a+1)(b+1)xy.                                  \tag{8}
\end{aligned}
\]

AM--GM on the first and last terms proves (1).

If \(B\) is a reflected copy of \(A\), then

\[
 C(B)=U(A),\qquad U(B)=C(A),                            \tag{9}
\]

and (6) gives

\[
 C(P)=U(P)=U(A)+(m+1)C(A).                              \tag{10}
\]

Equation (2) follows either from (1) or directly from
\(C(A)U(A)\ge H\).  Notice that the conclusion is chart-local and exact;
no unrestricted endpoint theorem is being invoked.

## 2. The coefficient threshold and the fixed-gap surplus

Let \(m=2^{L-1}\).  From (2) and the child lower bound,

\[
 \log(C(P)U(P))
 \ge2+\log(m+1)+\Phi_{\beta,K}(L-1)
 \ge L+1+\Phi_{\beta,K}(L-1).                         \tag{11}
\]

Subtracting (3) at \(L\) gives exactly the right side of (4).  Moreover

\[
 \Delta_L
 =\log L+(L-1)\log{L\over L-1}\ge\log L.             \tag{12}
\]

At \(\beta=1/2\), (4) is therefore at least
\(3/2+K\log L\).  If the parent is a fixed-gap counterexample,

\[
                         W(P)<2^{\Phi_{1/2,K}(L)},       \tag{13}
\]

then

\[
              {C(P)U(P)\over W(P)}>2^{3/2}L^K.          \tag{14}
\]

Suppose, as an additional geometric input, that every ordered
cap--cup pair of \(P\) can be assigned an ordinary face and that no face
has more than \(\Lambda\) preimages.  Then

\[
                         W(P)\ge {C(P)U(P)\over\Lambda}. \tag{15}
\]

Equations (4), (13), and (15) prove (5).  The phrase “every pair” is
essential.  The usual upper/lower hull union only works for matching
endpoints, and counting those compatible pairs gives back \(W(P)\), not
\(C(P)U(P)\).

This is the precise scale of the remaining operation.  A polynomial-load
endpoint-pair pigeonhole is too expensive at \(\beta=1/2\); one needs a
polylogarithmic-load conversion, an actual same-configuration profile
cycle, or an equivalent reset which retains the root/carrier history.

## 3. The dense all-delete rectangle is simultaneous but orthogonal

Let

\[
 \mathcal D=\mathcal F(A)\setminus\mathcal C(A),\qquad
 \mathcal H=\mathcal F(B)\setminus\mathcal U(B).        \tag{16}
\]

The exact two-block face classification says that for nonempty
\(D'\subseteq D\in\mathcal D\) and \(F\in\mathcal H\),

\[
                         D'\cup F\notin\mathcal F(P),   \tag{17}
\]

while \(F\in\mathcal F(P)\).  Indeed a spanning face needs a cap in the
left block and a cup in the right block; \(F\) is not a cup.  Thus every
record \((D,F)\) has the unique deletion mask \(D\): the entire source is
erased.

For arbitrary nonnegative source weights \(w_D\), routing every record to
its released face \(F\) gives

\[
 \text{total incidence mass}
   =|\mathcal H|\sum_Dw_D,qquad
 \text{load at every }F=\sum_Dw_D.                    \tag{18}
\]

After division by the actual load, (18) yields exactly
\(|\mathcal H|\).  Density of \(\mathcal D\) does not improve it.

The canonical rooted-circuit state is also literal.  Every noncap face
\(D\) contains an increasing positive triple.  Choose the first such triple
\(T(D)\).  For every \(z\in B\), the four-set \(T(D)\cup\{z\}\) is bad by
the same two-block classification.  Hence \(T(D)\) has root degree \(b\),
and it is independent of the released singleton \(z\).

If the source ranks are at most \(R\), a fixed \((T,r)\) fibre retains at
least

\[
             {|\mathcal D|\over {a\choose3}(R+1)}       \tag{19}
\]

sources.  Unordered injective role colouring loses only
\(r!/r^r\ge e^{-r}\).  Thus for \(R=O(\log a)\), the common-root marked
slice has only polynomial loss.  Equations (17)--(18) show exactly why this
still does not convert the endpoint surplus (14).

## 4. Exact scalar equality family

Fix integers \(m\ge2\) and

\[
                         t\ge m+{m\choose2}.             \tag{20}
\]

Give the left and right abstract children the profiles

\[
\begin{array}{c|ccc}
 &W&C&U\\ \hline
 A&(m+1)t^2&t&(m+1)t\\
 B&(m+1)t^2&(m+1)t&t.
\end{array}                                             \tag{21}
\]

They obey

\[
 C,U\ge m+{m\choose2},\qquad C,U\le W,qquad CU=W.     \tag{22}
\]

The strong-glue recurrence gives

\[
\begin{aligned}
 W(P)&=(2m+3)t^2,\\
 C(P)&=U(P)=2(m+1)t,\\
 C(P)U(P)&=4(m+1)^2t^2=4(m+1)W(A).             \tag{23}
\end{aligned}
\]

Thus (1) is attained with equality.  Both all-delete sides have size
\((m+1)t^2-t\), asymptotic to the full child bank.

Take \(m=2^d\) and choose \(t\) so that
\((m+1)t^2=2^{\Phi_{\beta,K}(d)+O(1)}\).  For every fixed
\(\beta>0\), (20) holds for large \(d\).  The child is at the inductive
scale, the parent has only a constant multiple of that many formal faces
and is far below \(2^{\Phi_{\beta,K}(d+1)}\), while its endpoint product
attains the reset scale in (4).  This is an exact scalar obstruction to
strengthening (1) from the stated data.

It is not asserted that (21) is the profile of a planar child.  At
\(\beta<1/2\), realizing it recursively would already give a sub-half upper
construction.  At \(\beta=1/2\), realizing the sharp fixed-gap correction
would defeat the proposed fixed-gap theorem.  The scalar family is used
only to prove that parent upper, dense all-delete incidence, pair baselines,
and endpoint factorization have no stronger numerical consequence.

## 5. Stretchable planar calibration at the leading half coefficient

Let

\[
 S_k=T(2k-4,k-2),\qquad
 r_k={2k-4\choose k-2},\qquad a_k=b_k=k-1,              \tag{24}
\]

and let \(Q_{k,d}\) be the \(d\)-fold vertical substitution iterate of
\(S_k\).  The exact rational substitution theorem gives, with
\(N=r_k^d\),

\[
\begin{aligned}
 \log W(Q_{k,d})
   &=\rho_k(\log N)^2+O_k(\log N),\\
 \log C(Q_{k,d})=\log U(Q_{k,d})
   &={\rho_k\over2}(\log N)^2+O_k(\log N),              \tag{25}\\
 \rho_k&={k-2\over\log {2k-4\choose k-2}}\longrightarrow{1\over2}.
\end{aligned}
\]

Now strongly glue two identical copies:

\[
                         P_{k,d}=Q_{k,d}\prec Q_{k,d}.   \tag{26}
\]

Equations (6) give exactly

\[
\begin{aligned}
 W(P_{k,d})&=2W(Q_{k,d})+C(Q_{k,d})^2,\\
 C(P_{k,d})=U(P_{k,d})&=(N+2)C(Q_{k,d}).                \tag{27}
\end{aligned}

Hence

\[
 {\log W(P_{k,d})\over(\log(2N))^2}\longrightarrow\rho_k
 \quad(d\to\infty),qquad
 \lim_{k\to\infty}\rho_k={1\over2}.                  \tag{28}
\]

Moreover \(C(Q_{k,d})/W(Q_{k,d})\to0\), so both sides of
(16) have \((1-o(1))W(Q_{k,d})\) members.  The largest cap and cup ranks in
\(Q_{k,d}\) are \(1+d(k-2)\), and every ordinary face has rank at most

\[
                   r_k+2d(k-2)=O_k(d)=O_k(\log N).      \tag{29}
\]

Choosing \(d=d(k)\) much larger than \(r_k\) makes the last \(O(\log N)\)
uniform along a diagonal \(k\to\infty\).  Equations (19) and the colouring
bound then retain the canonical common-triple state at polynomial loss.
All sets are stretchable over the rationals by the exact substitution
construction.

This family does **not** satisfy the strict fixed-gap parent upper bound
(13); its subleading error is not a negative \(-K L\log L\) term.  It proves
the sharper applicability statement: every other ingredient of the
canonical Pascal/all-delete normal form survives at the leading half
coefficient.  Any successful exclusion must use the strict parent upper
bound to realize the polylogarithmic conversion (5), not merely record the
endpoint surplus.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_parent_upper_endpoint_reset_threshold.py
```

The checker uses exact rational geometry and integer arithmetic.  It

* exhausts small endpoint profiles and verifies (1);
* checks equality (21)--(23) and the rank-two baseline;
* verifies the exact threshold identity (4) across the three coefficient
  regimes;
* constructs the rational \(T(4,2)\prec T(4,2)\) twelve-point instance,
  enumerates its all-delete rectangle and common-triple witnesses;
* independently evaluates the 36-point iterate
  \(T(4,2)[T(4,2)]\), recovering
  \((C,U,W)=(14136,14136,441399)\); and
* evaluates its exact 72-point two-block parent, recovering (27), while
  checking the balanced-template coefficients \(\rho_k\downarrow1/2\).
