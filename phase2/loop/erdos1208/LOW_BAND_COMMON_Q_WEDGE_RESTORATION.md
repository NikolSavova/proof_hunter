# Low band after restoring the exact common-translation weight

## 1. Outcome

The broad ambient wedge moment

\[
 J_L=\sum_rR_D(-18r)W_{r,L}                              \tag{1.1}
\]

should be retired as a proposed bridge.  On the stored closure prefixes its
normalization `J_L/(Nk^2)` grows from `0.96` at `k=20` to `9.71` at
`k=120`, and the rich-restricted normalization grows from `0.71` to `7.19`.
This growth is not present in the quantity actually arising from the clean
fibres.

For a chosen fibre collection `Q`, let

\[
 c_Q(s,s')=|\{q\in Q:s,s'\in H_q\}|                     \tag{1.2}
\]

and retain only `c_Q(s,s')<k`.  Define

\[
 C^Q_{<k}(r)=
 \sum_{\substack{s\ne s'\\
       \delta(s)-\delta(s')=-18r\\c_Q(s,s')<k}}
 c_Q(s,s').                                               \tag{1.3}
\]

The exact low-band wedge mass is

\[
 \boxed{Z^Q_{<k,L}=\sum_rC^Q_{<k}(r)W_{r,L}.}            \tag{1.4}
\]

It has three lossless expansions: over the actual common translation `q`,
over source determinant cells, and over physical target endpoint wedges.
All are proved in Section 2 and checked exhaustively by the companion
verifier.

On closure through `k=100`, every source codegree is below `k`.  Nevertheless
the rich part of (1.4) uses at most `2.74%` of the sufficient scale

\[
 N(H_Q+k^3),\qquad H_Q=\sum_{q\in Q}|H_q|.               \tag{1.5}
\]

The ambient polynomial rich-pencil counterexample is even more decisive:
its ambient fixed-wedge weight is 57 at `k=34`, but after restoring clean
translations its rich-restricted exact weight is zero.  Thus the new
perpendicular kill does **not** kill the actual low-codegree tail.

No proof of the required global bound is supplied.  The durable advance is
that the alarming closure growth has been localized entirely to the invalid
replacement `C^Q_(<k)(r) <= kR_D(-18r)`.  The exact common-`q` gate remains
plausible and has a clean sufficient pointwise form in Section 4.

## 2. Three exact expansions

Put

\[
 r(s,s')=-{\delta(s)-\delta(s')\over18},                 \tag{2.1}
\]

and interpret every summand as zero unless the quotient is a nonzero
integer.  Expanding the codegree in (1.3) proves the first identity

\[
 \boxed{
 Z^Q_{<k,L}
 =\sum_{q\in Q}
   \sum_{\substack{s\ne s'\in H_q\\c_Q(s,s')<k}}
      W_{r(s,s'),L}.}                                    \tag{2.2}
\]

Thus no ambient source representation has been inserted and no common
translation has been replaced by a maximum.

Canonically orient source edges and define their signed doubled area

\[
 e(s,s')=2\det(u_s,u_{s'}).                              \tag{2.3}
\]

Set

\[
 C^Q_{<k}(r,e)=
 \sum_{\substack{s\ne s'\\r(s,s')=r\\e(s,s')=e\\
                   c_Q(s,s')<k}}c_Q(s,s').               \tag{2.4}
\]

Then

\[
 \boxed{
 Z^Q_{<k,L}=\sum_{r,e}C^Q_{<k}(r,e)W_{r,L}.}             \tag{2.5}
\]

This is the exact source determinant decomposition.  Gaussian
factorization gives, uniformly for `r!=0`,

\[
 \#\{(s,s'):(r(s,s'),e(s,s'))=(r,e)\}\le G(m)=m^{o(1)}.
                                                                    \tag{2.6}
\]

Consequently the low-codegree restriction proves the rigorous cell cap

\[
 \boxed{C^Q_{<k}(r,e)\le(k-1)G(m)=m^{o(1)}k.}            \tag{2.7}
\]

Finally let `w=(x;{x,a_1},{x,a_2})` be a physical first-edge wedge, with
first labels `A_1,A_2` and canonical vectors `v_1,v_2`.  Let
`P_L(w)` be the partner pairs `(f_1,f_2)` satisfying

\[
 \delta(f_1)-\delta(f_2)=A_1-A_2,qquad
 |2\det(v_i,u_{f_i})|>L\quad(i=1,2).                    \tag{2.8}
\]

Define the exact common-translation fixed-wedge weight

\[
 \boxed{
 F^Q_{<k,L}(w)=
 \sum_{(f_1,f_2)\in P_L(w)}
 C^Q_{<k}(A_1-\delta(f_1)).}                             \tag{2.9}
\]

The same bijection as in the ambient localization, now with the exact
weight left untouched, gives

\[
 \boxed{Z^Q_{<k,L}=\sum_wF^Q_{<k,L}(w).}                \tag{2.10}
\]

Equations (2.2), (2.5), and (2.10) are three expansions of precisely the
same mass.

## 3. Exact implication for the reciprocal tail

Let

\[
 S_T=\{r:U_L(r)\ge T\},\qquad T\ge k.                   \tag{3.1}
\]

The endpoint degree inequality gives

\[
 W_{r,L}\ge {T^2\over k}\qquad(r\in S_T).              \tag{3.2}
\]

Therefore the exact source tail obeys

\[
 \boxed{
 \sum_{r\in S_T}C^Q_{<k}(r)
 \le {k\over T^2}
 \sum_{r\in S_T}C^Q_{<k}(r)W_{r,L}.}                   \tag{3.3}
\]

In particular the uniform moment theorem

\[
 \boxed{Z^Q_{<k,L}\le m^{o(1)}N(H_Q+k^3)}              \tag{3.4}
\]

would imply

\[
 \sum_{r\in S_T}C^Q_{<k}(r)
 \le {m^{o(1)}N(H_Q+k^3)\over T},                       \tag{3.5}
\]

because `T>=k`.  This is the required low-band reciprocal tail, with no
factor `k` lost to the ambient gap population.

## 4. A sufficient exact local gate

There are exactly

\[
 k{k-1\choose2}=N(k-2)                                  \tag{4.1}
\]

physical endpoint wedges.  Consequently the pointwise estimate

\[
 \boxed{
 F^Q_{<k,L}(w)
 \le m^{o(1)}\left({H_Q\over k}+k^2\right)
 \quad\text{for every }w}                               \tag{4.2}
\]

would prove (3.4), since

\[
 N(k-2)\left({H_Q\over k}+k^2\right)
 \le N(H_Q+k^3).                                        \tag{4.3}
\]

The rich-restricted version of (4.2), retaining only partner shifts in
`S_T`, is also sufficient.

Unlike the false ambient conjecture `F_(L,T)(w)<=m^(o(1))k`, the scale in
(4.2) allows quadratic perpendicular pencils.  But such a pencil is costly
only when the opposite scalar gaps are populated by pairs sharing genuine
clean translations.  The current rich-pencil construction does not do so.

Equation (2.7) does not by itself prove (4.2): it controls one fixed source
determinant cell, whereas (2.9) sums over all source determinants, and the
target high-determinant conditions in (2.8) do not constrain them.  This is
the exact surviving determinant mismatch.

## 5. Closure audit

The verifier takes the full clean-fibre collection on each prefix and uses
the adaptive stress cutoff `L=floor(N/k)`.  The columns below are

* `H`: total clean-fibre mass;
* `c_max`: maximum source-pair codegree;
* `||C_<k||_1` and its restriction to `U_L(r)>=k`;
* `Z_rich`: the rich restriction of (1.4);
* `F_max`: the maximum rich exact fixed-wedge weight; and
* `Z_rich/[N(H+k^3)]`.

\[
\begin{array}{c|r|r|r|r|r|r|c}
k&H&c_{\max}&\|C_{<k}\|_1&C_{\rm rich}&Z_{\rm rich}&F_{\max}&
 Z_{\rm rich}/[N(H+k^3)]\\ \hline
20&648&4&80&38&2409&10&0.00147\\
30&3816&6&1306&548&67083&69&0.00500\\
40&12420&12&8654&3940&709530&312&0.01190\\
50&26532&14&25558&11524&2761895&662&0.01488\\
60&49734&15&63340&27878&8162939&1218&0.01736\\
80&136134&16&273162&108978&42576488&3220&0.02079
\end{array}                                               \tag{5.1}
\]

A separate exact run at `k=100` gives

\[
 (H,c_{\max},\|C_{<k}\|_1,C_{\rm rich},Z_{\rm rich})
 =(322812,21,975404,372476,178772716),                    \tag{5.2}
\]

and normalized wedge mass `0.02730`.  The maximum normalized reciprocal
tail

\[
 \max_{T\ge k}{T\sum_{U_L(r)\ge T}C^Q_{<k}(r)
                   \over N(H+k^3)}                      \tag{5.3}
\]

is only `0.00569` at `k=100`.

For comparison, the broad ambient `J_L/(Nk^2)` is already `8.41` there.
The invalid pointwise envelope would replace the exact rich wedge mass by
roughly `kJ_L`; at `k=100` that is over 230 times the exact value in
(5.2).

The verifier independently evaluates (1.4), (2.2), (2.5), and (2.10) and
requires exact equality.  It also checks the polynomial rich-pencil family:

\[
 (k,H,c_{\max},\|C_{<k}\|_1,Z_{<k,L},Z^{\rm rich}_{<k,L})
 =(34,4086,12,5640,1,0).                                 \tag{5.4}
\]

Thus its ambient rich fixed-wedge weight 57 was entirely spurious for the
common-translation low band.

Run

```text
PYTHONPATH=phase2/loop/erdos1208 \
python3 phase2/loop/erdos1208/verify_low_band_common_q_wedge_decomposition.py
```

## 6. Exact remaining barrier

The clean translation `q` lives only on the source side of (2.2); a target
wedge at the matching scalar gap has no automatic endpoint relation to that
`q`.  Ordinary target incidence therefore still cannot prove (3.4).
Conversely, replacing the source side by `kR_D(-18r)` destroys precisely the
sparsity seen in (5.1)--(5.4).

The viable alternatives are now sharply delimited:

1. prove the exact local estimate (4.2), perhaps after a source-codegree or
   source-determinant dyadic split;
2. prove (3.4) directly by averaging (2.2) over physical wedges; or
3. construct a polynomial-height family in which one perpendicular target
   pencil is also populated by enough genuinely common-`q` source pairs to
   make (4.2) fail by a power.

No such common-`q` counterexample is currently known.  The closure data and
the strongest ambient pencil both support, rather than refute, the restored
exact gate.
