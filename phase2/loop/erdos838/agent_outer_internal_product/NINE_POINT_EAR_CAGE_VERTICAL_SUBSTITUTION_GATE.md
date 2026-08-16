# Nine-point ear cage: vertical substitution gate

## Verdict

The exact nine-point three-ear minimizer cage does **not** produce a
minimizer-safe scalable obstruction by homogeneous vertical substitution.
Two separate effects are exact.

1. The literal lifted ear alphabet has only polynomial entropy. At depth
   \(d\), with \(n=9^d\), all marked individual ear contexts over all scales
   number \(n^{4+o(1)}\), and even the generously counted same-label triples
   number \(n^{10+o(1)}\).
2. The same substitution exposes much larger ordinary cap--cup profile banks.
   Its face count satisfies

   \[
   \log _2 V(P_d)=\left({4\over\log _2 9}+o(1)\right)(\log _2 n)^2,
   \qquad {4\over\log _2 9}=1.261859507\ldots .                 \tag{1}
   \]

   The maximum face rank is \(8d-3=O(\log n)\), so low rank does not rescue
   the construction.

More decisively, already at depth two every physical label violates the
necessary one-point minimizer inequality. This remains true for all
\(37^2=1369\) independent choices of macro and micro projection chambers.
In the original chart, every one-, two-, and three-point deletion violates
the corresponding order-\(1,2,3\) minimizer comparison.

Thus this route gives neither a near-half construction nor a
minimizer-safe scalar barrier. It instead identifies the extra hypothesis
that a live use of the finite cage must retain: a **recoverable continuation
alphabet of live weighted mass**. Bare ear geometry, even repeated at every
scale, is only polynomial metadata and is erased by the live normalization.

This is a local gate, not a proof of the half-coefficient theorem.

## 1. The seed and every projection chamber

Let \(S\) be the exact rational nine-point configuration in
`agent_lex_minimizer_search/exact_realizable_n9.json`. In its stored affine
chart it has

\[
\begin{array}{c|rrrrr|r}
 &1&2&3&4&5&\text{total}\\ \hline
\text{caps}&9&36&52&17&1&115\\
\text{cups}&9&36&32&12&1&90\\
\text{ordinary faces}&9&36&84&36&3&168.
\end{array}                                                     \tag{2}
\]

The three-ear cage from
`THREE_EAR_MINIMIZER_BARRIER_AND_ORDER_THREE_GATE.md` uses one hidden label
and the three source triangles

\[
 \{0,1,6\},\qquad \{0,1,7\},\qquad \{1,3,8\}                   \tag{3}
\]

in the original labelling. Each pair of open ear chambers intersects, their
triple intersection is empty, and the exact Farkas certificate is checked by
the earlier verifier.

There are 37 generic shear-projection chambers in one half-turn. Exact
enumeration gives, in **every** chamber,

\[
               a(S)=5,\qquad b(S)=5,                           \tag{4}
\]

although the total cap and cup counts vary. Consequently no rechart of this
seed lowers the stationary rank exponent used below.

## 2. Exact vertical recurrence and the forced mixed bank

Let \(P_0\) be a singleton and let

\[
                         P_d=S[P_{d-1}]                         \tag{5}
\]

be the strict vertical lexicographic substitution. Write
\(N=|P_{d-1}|=9^{d-1}\), and let \(C_d,U_d,V_d\) count nonempty
caps, cups, and ordinary faces. The exact substitution formula gives

\[
\begin{aligned}
C_d={}&C_{d-1}(N^4+17N^3+52N^2+36N+9),\\
U_d={}&U_{d-1}(N^4+12N^3+32N^2+36N+9),\\
V_d={}&9V_{d-1}\\
 &+C_{d-1}U_{d-1}(3N^3+36N^2+84N+36).
                                                               \tag{6}
\end{aligned}
\]

The last line exhibits the ordinary bank absent from the isolated finite
cage. Each of the three macro five-faces permits an arbitrary cap in its
first occupied child, an arbitrary cup in its last occupied child, and one
arbitrary point in each of three intermediate children. Hence it contributes

\[
                         3N^3C_{d-1}U_{d-1}                    \tag{7}
\]

ordinary faces, with no decoder loss inside one fixed composition.

Because all coefficients in (6) are positive,

\[
\begin{aligned}
\log _2 C_d&=2(\log _2 9)d^2+O(d),\\
\log _2 U_d&=2(\log _2 9)d^2+O(d),\\
\log _2 V_d&=4(\log _2 9)d^2+O(d).                \tag{8}
\end{aligned}
\]

Since \(\log _2|P_d|=d\log _2 9\), equation (1) follows.

The graded recurrence is equally exact:

\[
\begin{aligned}
C_d(z)&=C_{d-1}(z)F_C(9^{d-1}z),\\
U_d(z)&=U_{d-1}(z)F_U(9^{d-1}z),\\
V_d(z)&=9V_{d-1}(z)+C_{d-1}(z)U_{d-1}(z)
                         F_V(9^{d-1}z).                         \tag{9}
\end{aligned}
\]

Taking degrees yields

\[
 \deg C_d=\deg U_d=4d+1,\qquad \deg V_d=8d-3.                  \tag{10}
\]

Thus every ordinary face has rank at most
\((8/\log _2 9)\log _2 n-3\). The uniform mean face rank is also linear;
the exact values at depths \(1,2,3,10\) are

\[
 2.928571,\quad 7.481629,\quad 14.367079,\quad 70.136211.       \tag{11}
\]

For scale, the first terms are

\[
\begin{array}{c|r|r|r|c}
d&n&V_d&\max |F|&\log_2V_d/(\log_2n)^2\\ \hline
1&9&168&5&0.735669\\
2&81&61014762&13&0.643450\\
3&729&8148275465027020758&21&0.694650\\
4&6561&2^{123.358585\ldots}&29&0.767276\\
10&9^{10}&2^{1017.318010\ldots}&77&1.012415.
\end{array}                                                     \tag{12}
\]

The superficially attractive depth-two value \(0.64345\) is therefore a
finite-depth dip, not the asymptotic coefficient.

## 3. Exact literal cage loads

Consider one internal substitution node whose nine children each have
\(N\) points. The strict macro signs make every transversal copy of a source
triangle in (3) hide every chosen point from the hidden child. Because the
seed chamber intersections and its Farkas certificate are strict, choosing
the children sufficiently small preserves pairwise repairability and triple
infeasibility for all these finitely many transversals.

For each of the three ears there are \(N\) choices of hidden label and
\(N^3\) choices of source transversal. Thus the number of individual marked
ear contexts at that node is

\[
                              3N^4.                             \tag{13}
\]

If the three source transversals are allowed to choose their points
independently, the number of same-hidden-label cage triples is at most, and
in this generous raw model exactly,

\[
                         N(N^3)^3=N^{10}.                       \tag{14}
\]

This count deliberately imposes no coherence on source roles shared by two
macro triangles; imposing coherence only decreases it.

Summing over all nodes of \(P_d\) gives

\[
\begin{aligned}
M_d&=\sum_{\ell=0}^{d-1}9^\ell\cdot3
                    (9^{d-\ell-1})^4=n^{4+o(1)},\\
T_d&=\sum_{\ell=0}^{d-1}9^\ell
                    (9^{d-\ell-1})^{10}=n^{10+o(1)}.            \tag{15}
\end{aligned}
\]

For a fixed hidden physical label at a fixed node, the corresponding loads
are \(3N^3\) individual contexts and \(N^9\) triples. These are large
polynomial loads, but their logarithms are only \(O(\log n)\).

In contrast, equation (8) has quadratic logarithmic entropy. Indeed \(V_d\)
already exceeds both \(M_d\) and \(T_d\) from depth four onward, and

\[
     {M_d\over V_d}=2^{-\Theta((\log n)^2)},\qquad
     {T_d\over V_d}=2^{-\Theta((\log n)^2)}.                    \tag{16}
\]

This remains true against a hypothetical near-half face scale
\(2^{(1/2-\delta)(\log n)^2}\): any fixed polynomial cage alphabet is
negligible.

## 4. Necessary minimizer inequalities fail immediately

For a globally face-minimal \(P\), deletion of a point \(x\) and relocation
to the two endpoint cells gives the necessary order-one inequality

\[
 V(P)-V(P-x)\le 1+\min\{C(P-x),U(P-x)\}.                        \tag{17}
\]

The corresponding exact order-two and order-three comparisons are the
three and four strong-glue branches proved in
`MINIMIZER_TWO_POINT_EXTENSION_INTERACTION_GATE.md` and
`THREE_EAR_MINIMIZER_BARRIER_AND_ORDER_THREE_GATE.md`.

For the original-chart composition \(S[S]\),

\[
 (n,C,U,V)=(81,2702385,1641060,61014762).                       \tag{18}
\]

For every deleted subset of the indicated order, the verifier computes
\"comparison bound minus actual deletion loss.\" Its complete ranges are

\[
\begin{array}{c|r|r}
|X|&\min\text{ gap}&\max\text{ gap}\\ \hline
1&-10768745&-1300427\\
2&-18727142&-1608620\\
3&-24342189&-1728073.
\end{array}                                                     \tag{19}
\]

Every gap is negative. Thus every one-, two-, and three-point deletion
rejects this depth-two candidate.

This is not an unfortunate chart. Choose the macro and micro charts
independently from all 37 generic projection chambers. Among all
\(37^2\cdot81\) singleton tests, the largest gap is still

\[
                              -584054.                          \tag{20}
\]

Every recharted composition fails (17) at every label.

There is also a nonvertical calibration. The exact fitted three-map rational
IFS from `triangular_ifs_probe.py` reproduces the nine-point seed at depth
two and has \(V=22862\) at depth three (\(n=27\)). Eight of its 27 labels
already fail (17); the gap range is \([-431,910]\). Hence the direct
self-affine continuation is not a minimizer-safe escape either.

## 5. The minimal marked-history distinction

The finite cage proves that the following data are insufficient:

* one physical repair label;
* three pairwise repairable, jointly incompatible ear chambers;
* order-\(\le3\) scalar minimizer inequalities at that one finite scale.

The vertical audit proves that merely repeating those data at
\(\Theta(\log n)\) nested scales is also insufficient. A literal rank-three
cage carries only the physical choices in (15), while vertical recurrence
automatically creates the profile bank (7).

The weakest live hypothesis that separates the current deletion-forest
branch from this finite obstruction is therefore a **continuation-bearing
cage**:

1. every marked ear occurrence retains a canonical continuation/source
   record \(H\) not determined by its at most ten physical cage labels;
2. the output decoder retains the depth/role tag and \(H\), with total loss
   at most \(2^{O((\log n)\log\log n)}\); and
3. after coalescing identical physical cage geometry, the effective marked
   mass remains

   \[
        W_{\rm cage}\ge V(P)\,2^{-O((\log n)\log\log n)}.        \tag{21}
   \]

The isolated nine-point cage has no such \(H\). Its literal vertical lifts
fail (21) by (16). The live \(\Theta(\log n)\)-role branch is intended to
supply (21) through its canonical source/completion history; verifying that
the same history survives into all three ears is the exact remaining
coexistence/decoder obligation.

No multiplication theorem for an arbitrary \(H\) is asserted here.
Anti-aligned child profiles remain a genuine obstruction if the history is
erased before the ear stage.

## 6. Verification

Run

```bash
python3 agent_outer_internal_product/verify_nine_point_ear_cage_vertical_substitution_gate.py
```

The verifier:

* rechecks the exact seed cage and its Farkas certificate;
* enumerates all 37 projection chambers and all \(37^2\) two-level rechart
  pairs;
* verifies the heterogeneous composition formulas and graded rank profiles;
* exhausts every one-, two-, and three-label deletion at \(n=81\);
* verifies the cage-load sums through depth ten; and
* independently checks the rational three-map IFS at \(n=27\).

It prints `PASS`.
