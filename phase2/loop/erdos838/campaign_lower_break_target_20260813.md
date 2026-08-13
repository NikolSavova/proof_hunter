# Erdős 838 lower-bound campaign — break_target (gpt-5.6-sol, effort=max, 2026-08-13 14:43)

> Target: log C + log U >= (1/2 - o(1))(log N)^2 for ARBITRARY point sets.
> With Theorem 1.1 already proved, this resolves Erdős 838 outright.

I did not find a construction with coefficient strictly below \(1/2\). I did obtain two fairly broad obstructions, the exact nonuniform substitution identities, and a serious issue with the proposed cap–cup target.

## 1. The stated cap–cup target does not imply the desired bound on \(W\)

From the inequalities quoted in the question,
\[
C\le NX\le N^2M\le N^2W,\qquad
U\le NY\le N^2M\le N^2W.
\]
Consequently
\[
CU\le N^4W^2,
\qquad
\log W\ge \frac{\log C+\log U}{2}-2\log N.
\]
Thus
\[
\log C+\log U\ge \left(\frac12-o(1)\right)(\log N)^2
\]
only gives
\[
\log W\ge \left(\frac14-o(1)\right)(\log N)^2.
\]
Indeed, since every cap and cup is itself convex, the even simpler estimate
\[
W\ge\max(C,U)\ge\sqrt{CU}
\]
has the same factor-\(2\) loss.

This is not merely a weakness of the inequalities: cap and cup mass can be exponentially anti-correlated in their endpoints.

### Exact rational anti-correlation example

Let \(n\ge2\), \(M=2n+1\), and \(\varepsilon=(100n^4)^{-1}\). Define
\[
\ell_i=(\varepsilon^2i,\varepsilon i^2),\qquad
r_i=(1+\varepsilon^2i,\,1+\varepsilon(Mi-i^2)),
\quad 1\le i\le n.
\]
Let \(L=\{\ell_i\}\), \(R=\{r_i\}\), and \(P=L\cup R\).

Internally, \(L\) is an \(n\)-cup and \(R\) an \(n\)-cap. For mixed triples, putting \(f_k=Mk-k^2\), direct determinants give
\[
\det(\ell_j-\ell_i,r_k-\ell_i)
=\varepsilon(j-i)\!\left[
 \varepsilon-(i+j)
 +\varepsilon^2\bigl(f_k-i^2-(i+j)(k-i)\bigr)
\right]<0
\]
for \(i<j\), while
\[
\det(r_j-\ell_i,r_k-\ell_i)
=\varepsilon(k-j)\!\left[
 M-j-k-\varepsilon
 +\varepsilon^2\bigl(i^2-f_j-(M-j-k)(i-j)\bigr)
\right]>0
\]
for \(j<k\). The chosen \(\varepsilon\) makes the error terms much smaller than the main terms \(i+j\ge3\) and \(M-j-k\ge2\). Hence \(P=L\prec R\), in exact rational general position.

Put
\[
m=n+\binom n2=\frac{n(n+1)}2.
\]
Then
\[
C(L)=U(R)=m,\qquad U(L)=C(R)=2^n-1,
\]
and every nonempty subset internal to either block is convex. Therefore
\[
C(P)=U(P)=2^n-1+(n+1)m,
\]
whereas
\[
W(P)=2(2^n-1)+m^2.
\]
Hence
\[
\log C(P)+\log U(P)=2n+o(n),\qquad
\log W(P)=n+1+o(1).
\]
Thus no general estimate of the form
\[
W\ge \frac{CU}{N^{O(1)}}
\]
is possible. A lower-bound campaign needs an endpoint-correlation statement about
\[
\sum_{p<q}c(p,q)u(p,q),
\]
not only a bound on the uncorrelated totals \(C\) and \(U\).

This example is not an upper construction for Erdős 838—its \(W\) is exponentially large in \(N\)—but it shows that the asserted final implication is invalid.

---

## 2. Exact functional for level-dependent uniform templates

Let
\[
P_0=\{\ast\},\qquad P_i=S_i[P_{i-1}],
\]
where
\[
r_i=|S_i|,\qquad N_i=|P_i|=\prod_{j\le i}r_j,
\qquad
\ell_i=\log r_i,\qquad L_i=\log N_i.
\]
For \(S_i\), define
\[
A_i(z)=\sum_{j\ge1}c_j(S_i)z^{j-1},\quad
B_i(z)=\sum_{j\ge1}u_j(S_i)z^{j-1},\quad
D_i(z)=\sum_{j\ge2}v_j(S_i)z^{j-2}.
\]
Lemma 2.2 gives
\[
C(P_i)=C(P_{i-1})A_i(N_{i-1}),
\]
\[
U(P_i)=U(P_{i-1})B_i(N_{i-1}),
\]
and
\[
W(P_i)=r_iW(P_{i-1})
 +C(P_{i-1})U(P_{i-1})D_i(N_{i-1}).
\]
Unrolling gives the exact expression
\[
\boxed{
W(P_d)=N_d+
\sum_{s=1}^d
\frac{N_d}{N_s}\,
D_s(N_{s-1})
\prod_{i<s}A_i(N_{i-1})B_i(N_{i-1}).
}
\tag{1}
\]

Let \(a_i,b_i\) be the largest cap and cup sizes in \(S_i\), and put
\[
h_i=a_i+b_i-2.
\]
Since the leading coefficients of \(A_i,B_i\) are positive,
\[
A_i(z)B_i(z)\ge z^{h_i}.
\]
Also
\[
D_i(z)\ge v_2(S_i)=\binom{r_i}{2}.
\]
Finally, the cup–cap theorem gives
\[
h_i\ge\log r_i=\ell_i.
\]
Therefore (1) implies the universal lower functional
\[
\boxed{
\log W(P_d)\ge
\max_{1\le s\le d}
\left[
L_d-L_s+\log\binom{r_s}{2}
+\sum_{i<s}h_iL_{i-1}
\right].
}
\tag{2}
\]

Relaxing \(h_i\) to its smallest permitted value \(\ell_i\), the quadratic part is
\[
\sum_{i<s}\ell_iL_{i-1}
=
\frac12\left(
L_{s-1}^2-\sum_{i<s}\ell_i^2
\right).
\tag{3}
\]
This is the varying-schedule analogue of the fixed-template coefficient.

### Fine-mesh obstruction

Let
\[
L=L_d,\qquad \Delta=\max_{i\le d}\ell_i.
\]
Taking \(s=d\) in (2) and using (3),
\[
\log W(P_d)\ge
\frac12\left(
L_{d-1}^2-\sum_{i<d}\ell_i^2
\right)
+\log\binom{r_d}{2}.
\]
Since
\[
L_{d-1}=L-O(\Delta),\qquad
\sum_{i<d}\ell_i^2\le \Delta L,
\]
we obtain
\[
\boxed{
\log W(P_d)\ge \frac12L^2-O(\Delta L).
}
\tag{4}
\]

Consequently:

> **Theorem.** For every triangular family of level-dependent uniform directional blow-ups satisfying
> \[
> \max_i\log|S_i|=o(\log|P_d|),
> \]
> one has
> \[
> \log W(P_d)\ge
> \left(\frac12-o(1)\right)(\log|P_d|)^2.
> \]

Thus nonstationarity by itself gives no improvement. Any uniform varying-template construction beating \(1/2\) must contain a **macroscopic level**
\[
\log |S_i|=\Omega(\log |P_d|).
\]

In normalized variables \(x_i=\ell_i/L\), the quadratic energy is
\[
\sum_{i<s}x_i\sum_{j<i}x_j
=
\frac12\left[
\left(\sum_{i<s}x_i\right)^2-\sum_{i<s}x_i^2
\right].
\]
For an atomless schedule, \(\max x_i\to0\), this tends to \(1/2\). The only loss is the diagonal mass \(\frac12\sum x_i^2\). Hence a sub-\(1/2\) construction must exploit the detailed cap/cup/convex profiles of a bounded number of growing templates; the ordinary cup–cap bound cannot control those diagonal terms.

This obstruction is sharp at the level of available information: for \(d=1\), (1) reduces to \(W(P_1)=W(S_1)\), so controlling a single macroscopic template is precisely the original problem.

---

## 3. Exact identities for a nonuniform blow-up

Let \(S=(s_1,\dots,s_r)\), and replace \(s_i\) by an arbitrary block \(Q_i\), with
\[
n_i=|Q_i|,\qquad C_i=C(Q_i),\quad U_i=U(Q_i),\quad W_i=W(Q_i).
\]
After separately normalizing the \(Q_i\) to bounded boxes, the same rational small-\(\varepsilon\) realization gives the four orientation rules of Lemma 2.1.

For a macro-subset \(I=\{i_1<\cdots<i_k\}\), use the empty-product convention. The exact identities are
\[
\boxed{
C\bigl(S[Q_1,\dots,Q_r]\bigr)
=
\sum_{\substack{I\subseteq S\\ I\text{ a cap}}}
C_{i_1}\prod_{t=2}^k n_{i_t},
}
\tag{5}
\]
\[
\boxed{
U\bigl(S[Q_1,\dots,Q_r]\bigr)
=
\sum_{\substack{I\subseteq S\\ I\text{ a cup}}}
\left(\prod_{t=1}^{k-1}n_{i_t}\right)U_{i_k},
}
\tag{6}
\]
and
\[
\boxed{
W\bigl(S[Q_1,\dots,Q_r]\bigr)
=
\sum_{i=1}^rW_i+
\sum_{\substack{J=\{j_1<\cdots<j_k\}\subseteq S\\
                 J\text{ convex},\ k\ge2}}
C_{j_1}U_{j_k}
\prod_{t=2}^{k-1}n_{j_t}.
}
\tag{7}
\]

The proof is exactly the proof of Lemma 2.2, except that the first and last occupied blocks now have different statistics. In particular, for every \(i<j\),
\[
W\bigl(S[Q_1,\dots,Q_r]\bigr)\ge C_iU_j,
\tag{8}
\]
because every macro-pair is convex. Likewise,
\[
C\ge C_i n_j,\qquad U\ge n_iU_j.
\tag{9}
\]

Equation (8) identifies the only possible nonuniform escape: the fibers must exhibit quadratic-scale endpoint anti-correlation,
\[
\log C_i+\log U_j
\]
small for every \(i<j\). Hence cup-rich fibers must lie systematically to the left and cap-rich fibers to the right. The explicit two-block example above shows that this reverse ordering is geometrically possible, so it cannot be excluded by an abstract rearrangement argument. A successful construction would have to maintain it at every scale while also controlling all larger terms in (7).

---

## 4. Nonuniform decomposable substitutions are still blocked

There is a closure fact slightly stronger than the uniform closure stated in the paper.

> **Lemma.** If the macro-set \(S\) is mirror-decomposable and every fiber \(Q_i\) is mirror-decomposable, then the nonuniform directional blow-up
> \[
> S[Q_1,\dots,Q_r]
> \]
> is mirror-decomposable.

**Proof.** Induct on the strong binary tree of \(S\). At its root write \(S=A\prec B\). Let \(P_A,P_B\) be the unions of fibers over leaves of \(A,B\). By induction they are mirror-decomposable. Moreover \(P_A\prec P_B\): triples using three microblocks inherit the macro sign; triples with two points in one microblock have signs \(-\) or \(+\) by orientation rules (3) and (4). Thus \(P=P_A\prec P_B\). At a macro-leaf the assertion is exactly the assumed decomposability of its fiber. \(\square\)

Consequently, assuming Theorem 5.1 of the supplied paper as stated:

* arbitrary level-dependent schedules of Pascal cup–cap templates cannot beat \(1/2\), even when the template size grows macroscopically;
* replacing different macro-points by different decomposable cup/cap-extremal fibers also cannot beat \(1/2\);
* any successful nonuniform construction must introduce genuinely nondecomposable order types at a macroscopic scale.

---

## 5. Horton sets

The directional identities above do not apply to the standard high/low Horton recursion because the two recursive halves interleave in \(x\). The tempting majority-class rule for mixed triples is false.

If \(a_1<a_2\) are in the low half and \(b\) is in the high half, then \(b\) lies above the line \(a_1a_2\). Consequently:

* if \(x_b\) lies between \(x_{a_1}\) and \(x_{a_2}\), then
  \(\chi(a_1,b,a_2)=-\);
* if \(x_b\) lies outside that interval, the two low points are adjacent in the increasing triple and its sign is \(+\).

Thus cap/cup compatibility depends on interval nesting, not just on which recursive half contributes two points. I did not obtain a rigorous all-convex-subset count for Horton sets, so I cannot claim either an improvement or a \(1/2\) obstruction there.

The same issue prevents importing bounds concerning empty convex polygons from Horton/Valtr-type constructions: emptiness gives no direct upper bound on the number of arbitrary convex subsets.

---

The live route is therefore quite narrow but real: a sub-\(1/2\) construction must use one or more macroscopic, genuinely nondecomposable order types and maintain reverse-ordered cap/cup profiles so that every endpoint product in (7), including products with many intermediate blocks, stays below \(2^{(1/2-\delta)(\log N)^2}\).

**VERDICT: PARTIAL — no sub-\(1/2\) family was constructed. Cleanest established statement: every level-dependent uniform directional blow-up with \(\max_i\log|S_i|=o(\log N)\) has \(\log v(P)\ge(1/2-o(1))(\log N)^2\); nonuniform blow-ups satisfy the exact identities (5)–(7), and any possible improvement must exploit macroscopic nondecomposable templates with persistent left–right cap/cup anti-correlation.**