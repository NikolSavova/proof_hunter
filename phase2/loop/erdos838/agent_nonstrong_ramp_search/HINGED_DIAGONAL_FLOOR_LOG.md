# Universal hinged diagonal: an exact Kraft theorem

**Date:** 2026-08-15. All logarithms are base two.

## Verdict

Let \(P=(p_1,\ldots,p_n)\) be any generic point set in increasing
\(x\)-order. Define

\[
\begin{aligned}
 \alpha(i)&=\max\{|A|-1:A\text{ is a cap and }\min_x A=p_i\},\\
 \beta(i)&=\max\{|B|-1:B\text{ is a cup and }\max_x B=p_i\}.
\end{aligned}                                                \tag{1}
\]

There is a prefix-free binary code with codeword \(w_i\) of length
\(\alpha(i)+\beta(i)\) for every point. Consequently,

\[
 \boxed{\sum_{i=1}^n2^{-\alpha(i)-\beta(i)}\le 1},\qquad
 \boxed{\max_i\{\alpha(i)+\beta(i)\}\ge\lceil\log n\rceil}.    \tag{2}
\]

The result is stronger than a point-set theorem. It holds for every
assignment of distinct real labels to the edges of the ordered complete
graph: cups are increasing-label paths and caps are decreasing-label paths.
For point sets with parallel disjoint edges, an arbitrarily small
orientation-preserving perturbation makes all slopes distinct without
changing any cap or cup.

The proof uses exactly the endpoint conventions required by the
substitution recurrence: cap support with macro minimum \(i\), and cup
support with macro maximum \(i\). It therefore repairs the endpoint mismatch
in the proposed Baek--Balko route; no split-polygon theorem is used.

For every finite transition grammar, including variable arities and parallel
child transitions, let \(M\) be its transition-count matrix. On every
strongly connected component,

\[
                         \boxed{\rho_C+\rho_U\ge\log\rho(M)}. \tag{3}
\]

Here \(\rho_C,\rho_U\) are the cap and cup maximum cycle means. Since
\(\rho(M)\) is also the exponential size-growth factor, every finite grammar
has recursive convex-face coefficient at least \(1/2\), irrespective of
variable child counts, child order types, projection charts, state count, or
parallel child-state menus. In particular, arbitrary nonstrong children
cannot realize a genuinely sub-half perfect-reset ramp inside this finite
grammar model.

Exact verifier:

~~~text
python3 phase2/loop/erdos838/agent_nonstrong_ramp_search/verify_hinged_diagonal_floor_log.py
~~~

It constructs and checks the prefix code for every tested order, exhausts
all 720 arbitrary edge orders at \(n=4\), exhausts all reflection-order
commutation classes through \(n=7\), and verifies a sharp stretchable
eight-point equality certificate.

## 1. Threshold profiles

Write \(\lambda(i,j)\) for the label of edge \(ij\), where \(i<j\). For
\(1\le r\le\beta(i)\), define

\[
 u_i(r)=\min\{\lambda(v_{r-1},i):
 v_0<\cdots<v_{r-1}<i
 \text{ is an }r\text{-edge increasing path ending at }i\}. \tag{4}
\]

Thus \(u_i(r)\) is the least possible last label of an \(r\)-edge cup
ending at \(i\). For \(1\le s\le\alpha(i)\), define

\[
 d_i(s)=\min\{\lambda(i,v_1):
 i<v_1<\cdots<v_s
 \text{ is an }s\text{-edge decreasing path starting at }i\}. \tag{5}
\]

Thus \(d_i(s)\) is the least possible first label of an \(s\)-edge cap
starting at \(i\). Taking a suffix in (4), or a prefix in (5), shows that
each profile is nondecreasing:

\[
 u_i(1)\le\cdots\le u_i(\beta(i)),\qquad
 d_i(1)\le\cdots\le d_i(\alpha(i)).                         \tag{6}
\]

For convenient sentinels, put

\[
 u_i(0)=d_i(0)=-\infty,\qquad
 u_i(\beta(i)+1)=d_i(\alpha(i)+1)=+\infty.                 \tag{7}
\]

## 2. The binary profile word

Merge the two sorted lists

\[
        (u_i(1),\ldots,u_i(\beta(i)))\quad\text{and}\quad
        (d_i(1),\ldots,d_i(\alpha(i))).                    \tag{8}
\]

Record a \(0\) when the next entry comes from the \(u\)-list and a \(1\)
when it comes from the \(d\)-list. Call the resulting word \(w_i\). Its
length is exactly

\[
                         |w_i|=\alpha(i)+\beta(i).           \tag{9}
\]

Repeated values inside one profile cause no ambiguity because they emit
the same bit. With globally distinct edge labels, a \(u_i\)-value and a
\(d_i\)-value cannot tie: the former is an incoming edge at \(i\), while
the latter is an outgoing edge at \(i\).

This construction is a variable-length, mixed-endpoint adaptation of the
binary profile-word method of Norin and Yuditsky, *Erdos--Szekeres without
induction* (2015, arXiv:1509.03332). Their fixed-length encoding motivates
the merge; the proof below is included in full and no novelty claim about
the encoding technique is made.

## 3. Prefix separation

Fix \(i<j\) and let \(t=\lambda(i,j)\). Define

\[
 x=\min\{r\ge1:u_i(r)>t\},\qquad
 y=\min\{s\ge1:d_j(s)>t\},                                \tag{10}
\]

where the sentinels (7) guarantee existence.

By minimality, \(u_i(x-1)<t\). Append edge \(ij\) to an
\((x-1)\)-edge increasing path ending at \(i\). This gives an \(x\)-edge
increasing path ending at \(j\), so

\[
                         x\le\beta(j),\qquad u_j(x)\le t.    \tag{11}
\]

Similarly, \(d_j(y-1)<t\). Prepend edge \(ij\) to a
\((y-1)\)-edge decreasing path starting at \(j\). This gives a
\(y\)-edge decreasing path starting at \(i\), so

\[
                         y\le\alpha(i),\qquad d_i(y)\le t.   \tag{12}
\]

Set \(L=x+y-1\). The sentinel bounds and (11)--(12) give

\[
 L\le\alpha(i)+\beta(i),\qquad
 L\le\alpha(j)+\beta(j),                                  \tag{13}
\]

so both words have a prefix of length \(L\).

For point \(i\), (10) and (12) give

\[
                         d_i(y)\le t<u_i(x).                \tag{14}
\]

Therefore the first \(L\) bits of \(w_i\) contain at most \(x-1\) zeros
and at least \(y\) ones. For point \(j\), (10) and (11) give

\[
                         u_j(x)\le t<d_j(y).                \tag{15}
\]

Therefore the first \(L\) bits of \(w_j\) contain at least \(x\) zeros and
at most \(y-1\) ones. The two length-\(L\) prefixes differ. Since \(L\)
does not exceed either word length, neither \(w_i\) nor \(w_j\) is a prefix
of the other.

This holds for every pair \(i<j\). Hence \(\{w_1,\ldots,w_n\}\) is
prefix-free. Kraft's inequality and (9) prove the first assertion in (2).
If every length were smaller than \(\lceil\log n\rceil\), its Kraft sum
would exceed one, proving the second assertion.

## 4. One-pass verifier recurrence

Sweep the edges in increasing label order. At edge \(ij\), the endpoint
ranks obey

\[
 \alpha_i\leftarrow\max(\alpha_i,\alpha_j+1),\qquad
 \beta_j\leftarrow\max(\beta_j,\beta_i+1).                 \tag{16}
\]

At the same step, every newly reachable cup rank at \(j\) records the
current edge time as its first, hence minimum, value \(u_j(r)\). Every newly
reachable cap rank at \(i\) similarly records the current time as
\(d_i(s)\). This computes (4)--(5) without enumerating paths.

For every pair \(i<j\), the verifier reconstructs \(x,y,L\) from (10), checks
(11)--(15), checks that the two prefixes differ, and finally checks the
Kraft sum using exact rational arithmetic.

## 5. Finite variable-arity grammar

Consider any finite recursive grammar with state set \(\mathcal S\). State
\(s\) exports \(m_s\) macro positions. A position is a directed edge
\(e:s\to\tau(e)\), and parallel edges are retained.

Choose a reachable critical strongly connected component \(K\) of the
transition-count matrix. In every state \(s\in K\), retain only positions
whose child state also lies in \(K\), take their induced \(x\)-ordered
subchart, and recompute cap/cup endpoint ranks inside that subchart. Write
the resulting rewards as

\[
       c_e=\alpha_s(e),\qquad u_e=\beta_s(e),\qquad
       \ell_e=c_e+u_e.                                    \tag{17}
\]

This restriction is essential in a reducible variable-arity grammar:
every ordinary filler position used by a restricted cap or cup now has the
same exponential child growth. The restricted banks are genuine subbanks of
the full recurrence.

The profile words from Sections 1--3 are prefix-free within each restricted
state chart.
Therefore every row of the transition multigraph satisfies

\[
                         \sum_{e\text{ out of }s}2^{-\ell_e}\le1. \tag{18}
\]

Let \(M_{st}\) be the number of retained positions of state \(s\) whose
child has state \(t\), and write \(\Lambda=\rho(M)\). Let \(r_s>0\) be a
right Perron vector:

\[
                         \sum_tM_{st}r_t=\Lambda r_s.      \tag{19}
\]

Give every individual parallel edge \(e:s\to t\) probability

\[
                         p_e={r_t\over\Lambda r_s}.        \tag{20}
\]

These probabilities sum to one in each row. Choose the stationary vertex
law \(\pi\) for this Markov chain. Its entropy rate is exactly

\[
\begin{aligned}
 H
 &=\sum_s\pi_s\sum_{e\text{ out of }s}p_e\log{1\over p_e}\\
 &=\log\Lambda+
   \sum_s\pi_s\sum_{e:s\to t}p_e(\log r_s-\log r_t)
 =\log\Lambda,                                            \tag{21}
\end{aligned}
\]

because stationarity telescopes the Perron-potential term. This is the
Parry measure written explicitly, so no variational theorem is needed.

For a fixed row \(s\), put \(Q_s=\sum_e2^{-\ell_e}\le1\). Nonnegativity of
the relative entropy between \(p_e\) and \(2^{-\ell_e}/Q_s\) gives the
rowwise cross-entropy inequality

\[
             \sum_ep_e\log{1\over p_e}
             \le\sum_ep_e\ell_e+\log Q_s
             \le\sum_ep_e\ell_e.                          \tag{22}
\]

Average (22) with \(\pi\), and use (21):

\[
                         \log\Lambda\le\mathbb E_\pi\ell_e. \tag{23}
\]

The stationary edge law \(\pi_sp_e\) is a nonnegative circulation. Every
finite circulation decomposes into a convex combination of directed-cycle
flows. Hence some directed cycle \(\gamma\) satisfies

\[
 {1\over|\gamma|}\sum_{e\in\gamma}\ell_e
 \ge\mathbb E_\pi\ell_e\ge\log\Lambda.                    \tag{24}
\]

Let \(\rho_C,\rho_U\) be the maximum cycle means of \(c_e,u_e\) on this
component. The two rewards in (24) use the same edges, and therefore

\[
\begin{aligned}
 \rho_C+\rho_U
 &\ge {1\over|\gamma|}\sum_{e\in\gamma}c_e
      +{1\over|\gamma|}\sum_{e\in\gamma}u_e\\
 &= {1\over|\gamma|}\sum_{e\in\gamma}\ell_e
 \ge\log\Lambda.                                         \tag{25}
\end{aligned}
\]

This proves (3), including variable arities and transition multiplicities.
For a reducible grammar, the preliminary restriction to \(K\) supplies this
same proof. Components with \(\Lambda\le1\) have no exponential size growth
and are irrelevant to a quadratic-in-\(\log N\) coefficient.

The size vector obeys \(N(d)=MN(d-1)\), up to the fixed singleton
initialization, so on a critical component

\[
                         \log N_s(d)=d\log\Lambda+O(\log d). \tag{26}
\]

The retained positions recursively define an actual point subset of the
full construction. Any initial state that reaches \(K\) contains such a
subset after a bounded depth shift. The full construction has the same
leading \(d\log\Lambda\) logarithmic size; reducible critical chains can add
only the displayed \(O(\log d)\) term.

In the heterogeneous vertical recurrence, every ordinary child block still
has logarithmic size \(d\log\Lambda+O(1)\). Standard positive max-plus
expansion therefore gives leading cap and cup exponents

\[
 {\rho_C\log\Lambda\over2}d^2,\qquad
 {\rho_U\log\Lambda\over2}d^2.                            \tag{27}
\]

A two-position macro support is convex, so the corresponding child cap and
cup banks give convex-face coefficient

\[
 {\,\rho_C+\rho_U\,\over2\log\Lambda}\ge {1\over2}.        \tag{28}
\]

This is the exact finite/menu inequality requested. A sub-half construction
must leave at least one hypothesis of this model: finitely many stationary
transition states, the exact vertical endpoint recurrences, or availability
of both endpoint child banks in the parent face count. Variable arity,
parallel transitions, nonstrong order types, and additional projection
charts do not evade (28).

## 6. Exact census

The verifier exhausts one representative of every commutation class of
reduced words for the longest permutation. Swapping disjoint roots does not
change (16), and long-braid connectivity makes this an exact census of all
reflection orders. It also constructs the code above in every class.

\[
\begin{array}{c|r|l|r}
n&\#\text{ classes}&\text{histogram of }h&
 \#\text{ Kraft equalities}\\ \hline
2&1&1:1&1\\
3&2&2:2&2\\
4&8&2:3,\ 3:5&7\\
5&62&3:46,\ 4:16&36\\
6&908&3:325,\ 4:517,\ 5:66&282\\
7&24698&3:2132,\ 4:16206,\ 5:6008,\ 6:352&3500.
\end{array}                                                \tag{29}
\]

All 25,679 reflection classes satisfy (2). The minimum hinged value is
\(\lceil\log n\rceil\) in every enumerated size. The verifier separately
checks all \(6!=720\) arbitrary total orders of the six edges at \(n=4\),
emphasizing that the proof is not reflection-specific.

## 7. Sharp stretchable equality at eight points

The ceiling-log theorem is sharp. Take

~~~text
p_i = (i,y_i),
y = (0,-6857,-15714,33429,-39429,9714,857,-6000).
~~~

The minimum absolute triple determinant is \(2000\). Exact slope sorting,
the recurrence (16), and direct enumeration of all 255 nonempty supports
independently give

\[
\begin{aligned}
 \alpha&=(3,2,2,1,2,1,1,0),\\
 \beta &=(0,1,1,2,1,2,2,3).
\end{aligned}                                             \tag{30}
\]

The profile construction produces all eight three-bit words, exactly once.
Consequently,

\[
 \alpha(i)+\beta(i)=3\quad(1\le i\le8),\qquad
 \sum_i2^{-\alpha(i)-\beta(i)}=1.                         \tag{31}
\]

One reduced-word certificate is

~~~text
(3,4,5,4,2,1,2,0,6,1,2,5,4,3,2,4,3,1,2,5,0,6,4,1,3,2,5,4).
~~~

The coordinate slope order differs from its displayed root sequence only
by commutations of disjoint crossings; the verifier checks the canonical
commutation class exactly.

## 8. Relation to the older Pascal-cell bound

For comparison, let

\[
 X_{p,q}=\{p_i:\alpha(i)=p,\ \beta(i)=q\}.                 \tag{32}
\]

The exact cups--caps theorem gives

\[
                         |X_{p,q}|\le {p+q\choose p}.       \tag{33}
\]

Indeed, \(X_{p,q}\) has no \((p+2)\)-cap and no \((q+2)\)-cup. Summing
(33) over \(p+q\le h\) yields only

\[
                         n\le2^{h+1}-1,                    \tag{34}
\]

and hence the weaker \(h\ge\lfloor\log n\rfloor\).

The extra state missing from that argument is now explicit: the ordered
threshold lists (4)--(5), or equivalently the chronology in the simultaneous
rank updates (16). Static Pascal-cell cardinalities forget where the common
edge label lies relative to the two endpoint profiles. The mixed profile
word retains exactly that comparison, couples all rank diagonals, and
recovers the lost Kraft bit.
