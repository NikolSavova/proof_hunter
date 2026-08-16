# Fixed-gap ambient faces: the exact linear profile potential

**Date:** 2026-08-15. All logarithms are base two. This attacks the
ambient multi-label escape left by
CENTRAL_NESTED_CHILD_TWO_SIDED_PRODUCT_BARRIER.md.

## Verdict

For a genuine **linear strong-glue** composition there is an exact
fixed-gap potential which recovers the whole \(O(L\log L)\) induction
deficit from a very small directional-profile fluctuation.

Let \(q\) equal-size role children \(X_0,\ldots,X_{q-1}\), each of size
\(D=2^d\), be composed in the standard first-cap/last-cup chart. Write
\(C_i,U_i,H_i\) for their nonempty cap, cup, and ordinary-face counts in
that chart. Suppose

\[
                         \log H_i\ge \Phi(d)                       \tag{1}
\]

for every role, where \(\Phi\) is the inductive target exponent. Put

\[
 A_i=\log_D C_i,\qquad y_i=A_i-i,\qquad \ell=\log q.               \tag{2}
\]

Every child face splits injectively into an upper cap and lower cup, so
\(C_iU_i\ge H_i\). The exact linear composition has the ordinary bank

\[
 C_iU_j(1+D)^{j-i-1}\qquad(i<j).                                  \tag{3}
\]

Consequently, if

\[
 \boxed{
 y_i-y_j\ge
 T_\Phi(d,q):=1+\frac{\Phi(d+\ell)-\Phi(d)}{d}}                    \tag{4}
\]

for some \(i<j\), then the single bank (3) already contains at least

\[
                           2^{\Phi(\log(qD))}                      \tag{5}
\]

ordinary faces. Its decoder load is one: the first and last occupied
roles and every local trace are recovered from the face.

For a coefficient-\(c\) target

\[
                   \Phi(L)=cL^2-O(L\log L),                       \tag{6}
\]

one has

\[
                  T_\Phi(d,q)=(2c+o(1))\log q+1.                  \tag{7}
\]

At the live fixed gap \(q=\Theta(\log n)\), this is only
\(O(\log\log n)\). Thus any downward fluctuation of that size in the
cap-potential closes the full ambient scale loss. The exact remaining
state is sharply constrained:

\[
              y_j\ge y_i-T_\Phi(d,q)\qquad\text{for every }i<j.   \tag{8}
\]

It is an \(O(\log\log n)\)-coherent slope-one cap/cup ramp across
\(\Theta(\log n)\) physical children, not an arbitrary profile family.

This conclusion is best possible from induction and upper/lower-hull
factorization alone. For \(c=1/2\), \(q=d/4\), and \(8\mid d\), the exact
integer menu

\[
 \begin{aligned}
 C_i&=D^{d/8+i},\\
 U_i&=D^{3d/8-i},\\
 H_i&=C_iU_i=D^{d/2}
 \end{aligned}
 \qquad(0\le i<q)                                                  \tag{9}
\]

has \(y_i=d/8\) identically. It satisfies every scalar constraint

\[
 D\le C_i,U_i\le H_i,\qquad H_i=C_iU_i,                           \tag{10}
\]

yet the complete linear recurrence is only

\[
                 Hq\le W_{\rm lin}\le2Hq,                        \tag{11}
\]

while the half target at \(n=qD\) exceeds it by

\[
 \frac{2^{(d+\ell)^2/2}}{2q\,2^{d^2/2}}
     =2^{d\ell+\ell^2/2-\ell-1}
     =n^{(1-o(1))\log\log n}.                                    \tag{12}
\]

Thus no theorem using only \(H_i\le C_iU_i\), child induction, and the
exact first/last recurrence can recover the fixed-gap multiplier. One
must rule out the coherent ramp by a genuinely planar profile-alignment
theorem, or charge extra faces inside a child.

The menu (9) is an exact numerical regression, not a claimed family of
planar order types. Realizing it by induction-minimal children is exactly
the unrestricted heterogeneous cap/cup anti-alignment problem. Known
stationary, periodic, finite-menu, and small-step homogeneous
constructions do not realize it and have coefficient at least one half,
but no theorem currently excludes independently chosen primitive
children with these profiles. This report therefore gives a rigorous
positive drop theorem and a sharp applicability barrier, not a sub-half
construction.

Crucially, no false CENTRAL_SHELL factorization is used. The only
geometric composition is the audited **linear** first-cap/last-cup bank
(3). We never assert that arbitrary child faces attach at a cyclic
omitted gap.

## 1. The exact linear bank

Use the standard vertical/lexicographic strong glue of the ordered role
children. Its orientation law says that a multi-role ordinary face has:

* a cap trace in its first occupied child;
* a cup trace in its last occupied child; and
* at most one label in every intermediate child.

Conversely every such choice is ordinary. Therefore the nonempty face
count contains, and in the pure linear model equals,

\[
 W_{\rm lin}=\sum_iH_i+
   \sum_{0\le i<j<q}C_iU_j
        \prod_{i<r<j}(1+|X_r|).                                  \tag{13}
\]

For equal child sizes this is (3). This is the usual heterogeneous
strong-glue recurrence; it follows directly from local orientation signs
with two labels only in the first or last block.

It is materially weaker than the retracted cyclic endpoint-profile
claim. There is no assertion that a full child face factors into two
profiles which can be attached on opposite sides of an arbitrary omitted
macro role. The only internal fact used below is the always-valid
injection

\[
 \{\text{ordinary child faces}\}
   \hookrightarrow
 \{\text{caps}\}\times\{\text{cups}\},\qquad
 F\mapsto(\operatorname{upper}F,\operatorname{lower}F),           \tag{14}
\]

which gives \(H_i\le C_iU_i\).

## 2. Proof of the fixed-gap potential theorem

Put

\[
                           h=\frac{\Phi(d)}{d}.                    \tag{15}
\]

Equation (14) and (1) imply

\[
                B_i:=\log_DU_i\ge h-A_i.                          \tag{16}
\]

There is also an exact strengthening which will matter below. Define

\[
 h_i=\log_DH_i,\qquad
 s_i=A_i+B_i-h_i=\log_D\frac{C_iU_i}{H_i}\ge0.                   \tag{16a}
\]

Then the base-\(D\) exponent of the \(i<j\) bank is exactly

\[
 A_i+B_j+j-i-1=h_j+s_j+y_i-y_j-1.                               \tag{16b}
\]

Thus the bank closes whenever \(s_j+y_i-y_j\ge T_\Phi(d,q)\).
The surplus telescope and its planar endpoint-module consequence are
proved in COHERENT_RAMP_ENDPOINT_MODULE_LOCALIZATION.md.

For \(i<j\), use only the \(D^{j-i-1}\) subfamily of (3) in which every
intermediate role is occupied. Its base-\(D\) logarithm is at least

\[
\begin{aligned}
 A_i+B_j+j-i-1
 &\ge h+A_i-A_j+j-i-1\\
 &=h+(A_i-i)-(A_j-j)-1\\
 &=h+y_i-y_j-1.                                                   \tag{17}
\end{aligned}
\]

If (4) holds, the last expression is at least

\[
 \frac{\Phi(d)}{d}+\frac{\Phi(d+\ell)-\Phi(d)}{d}
       =\frac{\Phi(d+\ell)}{d}.                                  \tag{18}
\]

Raising \(D=2^d\) to this power proves (5).

The contrapositive is exactly (8). No averaging, Hall routing, or output
summation is hidden in the argument; one actual pair of physical roles
produces the entire face bank.

For the pure quadratic target \(\Phi(L)=cL^2\), formula (4) becomes

\[
                  T_\Phi=1+2c\ell+c\frac{\ell^2}{d}.              \tag{19}
\]

If \(\Phi(L)=cL^2-\beta L\log L+O(L)\) and
\(\ell=O(\log d)\), direct expansion gives

\[
 \frac{\Phi(d+\ell)-\Phi(d)}{d}
       =2c\ell+o(\ell),                                           \tag{20}
\]

uniformly for fixed \(\beta\). This proves (7): the usual
\(O(L\log L)\) correction changes only the lower-order part of the drop
threshold.

## 3. Balanced-role corollary

The potential theorem has a convenient nontechnical sufficient
condition. Suppose two roles \(i<j\) obey

\[
 \begin{aligned}
 \log_D C_i&\ge \frac h2-R,\\
 \log_D U_j&\ge \frac h2-R.
 \end{aligned}                                                    \tag{21}
\]

Then (3) has base-\(D\) logarithm at least

\[
                         h-2R+j-i-1.                              \tag{22}
\]

It closes the target whenever

\[
 j-i\ge1+2R+\frac{\Phi(d+\ell)-\Phi(d)}{d}.                       \tag{23}
\]

Thus a positive-density set of roles whose cap and cup counts are
balanced to \(O(\log q)\) automatically contains a far pair and closes
the fixed-gap branch. An unpaid family must order almost every cup-heavy
role before almost every cap-heavy role, with the calibrated slope in
(8).

This is the exact profile-alignment statement which survives the
arbitrary child counterexamples. It concerns scalar cap/cup counts in
their actual linear construction chart, not nonexistent universal
endpoint profiles.

## 4. Exact coherent-ramp regression

Take \(d\) divisible by eight, \(D=2^d\), \(q=d/4\), and define (9). Put
\(H=D^{d/2}\). For \(i<j\),

\[
 C_iU_jD^{j-i-1}
   =D^{d/8+i+3d/8-j+j-i-1}
   =\frac{H}{D}.                                                   \tag{24}
\]

Moreover

\[
 (1+D)^{j-i-1}\le
 D^{j-i-1}(1+1/D)^q<2D^{j-i-1}                                  \tag{25}
\]

for \(q\le D\). Hence every cross term in (13) is below \(2H/D\), and

\[
 Hq\le W_{\rm lin}\le Hq+\binom q2\frac{2H}{D}\le2Hq.             \tag{26}
\]

The potential is

\[
                        y_i=(d/8+i)-i=d/8,                        \tag{27}
\]

so the positive theorem has no drop to exploit. Equations (12) and (26)
quantify the exact missing scale.

The recurrence also contains the full singleton source product, but it
is smaller:

\[
                         D^q=D^{d/4}\ll H=D^{d/2}.                 \tag{28}
\]

Thus neither source entropy, child induction, nor ambient linear
multi-label faces pay the fixed-gap target in the scalar model.

## 5. What is proved and what remains

The following is unconditional once a physical branch has been promoted
to a recoverable linear strong-glue chart:

> Either one pair of roles supplies the complete fixed-gap target with
> load one, or the actual cap potential is an \(O(\log\log n)\)-coherent
> nondecreasing ramp after subtracting the role index.

This is substantially narrower than arbitrary one-sided anti-alignment.
It also gives an exact quantity for a future planar argument to control:

\[
                 \max_{i<j}\big[(\log_D C_i-i)
                                  -(\log_D C_j-j)\big].            \tag{29}
\]

What is not proved is that arbitrary induction-minimal planar children
cannot realize the constant-potential menu (9). The menu respects every
scalar inequality used here. Excluding it requires one of:

* a direction-spectrum theorem for induction-minimal order types;
* a local surplus theorem saying a strongly skew child already has more
  than \(2^{\Phi(d)}\) faces by the needed
  \(D^{\Omega(\log q)}\) factor; or
* a cross-role theorem using faces outside the linear first/last
  recurrence.

Known homogeneous recursive constructions satisfy stronger alignment
and do not realize (9), but importing that fact for arbitrary children
would be circular. The coherent ramp is therefore the exact remaining
fixed-gap atom.

## 6. Verification

Run

    python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_fixed_gap_linear_profile_potential.py

Expected output:

    PASS: drop theorem exhaustive, exact ramps d=16,64,256, and fixed-gap deficits verified; summaries=[(16, 4, 131, 31), (64, 16, 2053, 259), (256, 64, 32775, 1547)]
