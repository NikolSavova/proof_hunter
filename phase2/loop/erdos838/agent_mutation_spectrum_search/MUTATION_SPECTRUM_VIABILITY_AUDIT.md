# Ordered-block mutation spectrum: viability audit

**Date:** 2026-08-17. Face counts are nonempty. All geometric checks use
exact rational arithmetic.

## Plain-language verdict

Pointwise mutations contain more information than their Gibbs average, but
they still do not give the missing 838 bridge. The exact eight-point
configuration which defeats every bipartition is improved by an ordered
three-block mutation, while the true eight- and nine-point minimizers are
not. That is a genuine finite viability witness. However, low-face induced
subsets of the exact cyclic 27-point construction are stable under all
ordered three-block mutations at sizes 10, 12, and 14. At size 20 one
singleton mutation improves the count, after which the resulting rational
configuration is stable under every three-block mutation moving at most
four labels. Thus pointwise ordered-block descent is a useful search
operation, not an asymptotic proof mechanism by itself.

## 1. Relation to the previous target

This audit concerns the pointwise counterpart of the averaged fixed-$q$
kernel in
`POLYLOG_CAP_CUP_CONVERTER_MUTATION_GATE.md`.

- **Predecessor classification:** incomparable new bet. The averaged kernel
  can fail to detect a decreasing colouring even when one exists; conversely
  a pointwise statement needs a selection theorem absent from the average.
- **Coefficient implication sought:** if every fixed-gap counterexample
  admitted a decreasing ordered colouring, or if stability forced a mixed
  reservoir with a fixed exponent gain, global minimality would contradict
  the counterexample.
- **Viability controls:** the true $n=8,9$ minimizers, the bipartition-stable
  nonminimal $n=8$ trap, and the unstable twelve-point Pascal wrapper.
- **Kill condition:** a coherent scalable low-face family which is stable
  under the proposed fixed-$q$ mutations without already paying the desired
  rank/profile bank.

The finite control passes, but the cyclic family triggers the kill
condition. Therefore no new lemma is promoted from this audit.

## 2. Exact mutation spectrum

For an ordered bipartition $P=R\sqcup S$, define

\[
 \Delta_2(R,S)=V(R)+V(S)+C(R)U(S)-V(P).             \tag{1}
\]

For an ordered three-colouring $P=P_0\sqcup P_1\sqcup P_2$, define

\[
\begin{aligned}
 \Delta_3={}&\sum_iV(P_i)+C(P_0)U(P_1)+C(P_1)U(P_2)\\
 &+C(P_0)U(P_2)(1+|P_1|)-V(P).                  \tag{2}
\end{aligned}
\]

The verifier exhausts every colouring in the following table.

| control | $n$ | $V$ | $\min\Delta_2$ | decreasing bipartitions | $\min\Delta_3$ | decreasing 3-colourings |
|---|---:|---:|---:|---:|---:|---:|
| true minimizer | 8 | 113 | 0 | 0 | 0 | 0 |
| true minimizer | 9 | 168 | 0 | 0 | 0 | 0 |
| bipartition-stable trap | 8 | 121 | 0 | 0 | $-1$ | 12 |
| Pascal wrapper | 12 | 1061 | $-373$ | 2249 | $-445$ | 305089 |

The twelve improving colourings of the trap all have block sizes
$(1,6,1)$. The Pascal minima have sizes $(1,8,3)$ or $(3,8,1)$. Thus the
extra colour is not merely a formal refinement: it carries a second
physical anchor and escapes the exact bipartition trap.

## 3. Scalable cyclic stress

Start with the best exact cyclic three-map IFS from
`triangular_ifs_probe.py`. Its depth-three configuration has 27 points and
$V=22862$. Repeatedly delete the label which lexicographically minimizes
$(V,C+U,\text{index})$. The resulting exact rational nested sequence has

\[
\begin{array}{c|rrrrrrrrrrrrrrrrrr}
n&27&26&25&24&23&22&21&20&19&18&17&16&15&14&13&12&11&10\\ \hline
V&22862&18336&14831&11924&9566&7526&5976&4732&3688&2852&
2211&1676&1260&947&695&504&358&248.
\end{array}                                                \tag{3}
\]

Complete ordered-three-colour exhaustion gives

| $n$ | $V$ | $\min\Delta_3$ | minimum with all blocks nonempty |
|---:|---:|---:|---:|
| 10 | 248 | 0 | 18 |
| 12 | 504 | 0 | 43 |
| 14 | 947 | 0 | 98 |

At $n=16,18$, exhaustive search over every three-colouring moving at most
four labels also finds no decrease. At $n=20$, it finds a singleton versus
19-label mutation of value 4681, improving 4732 by 51. A rational horizontal
strong-glue realization, with the 19-label child reflected so that its cup
profile faces the singleton, has exactly

\[
                         (C,U,V)=(1765,2142,4681).       \tag{4}
\]

After this exact mutation, every ordered three-colouring moving at most four
labels has value at least 4681.

This is not a proof that the mutated configuration is globally minimal, or
even stable under every possible geometric mutation. It proves the narrower
point needed here: fixed-$q$ ordered-block descent can terminate at a strong
local wall inside a coherent stretchable family.

## 4. Consequence for strategy

The data reject the rule

> nonminimality should be visible as a decreasing bipartition or fixed-$q$
> ordered-block mutation.

The finite three-block success was real, but it does not scale across the
first serious control family. Accordingly the next 838 attack should not be
another uniform ordered-block selector. It must either

1. use a genuinely nonlinear/multi-chart minimizer mutation which the local
   strong-glue wall does not model; or
2. return to the fixed-rank positive-interval route, where a gain has a
   direct coefficient implication.

Under the campaign stop rule, this audit chooses option 2.

## 5. Coordinate-annealing follow-up

To check that the cyclic stress was not an artifact of one recursive family,
we ran a separate fixed-$x$ coordinate anneal at sizes
$10,12,14,16,18,20$.  The search itself was heuristic; the saved integral
coordinates and every count quoted here are checked independently with exact
rational arithmetic by `verify_annealed_coordinate_candidates.py`.

The resulting profiles $(C,U,V)$ are

\[
\begin{array}{c|rrrrrr}
n&10&12&14&16&18&20\\ \hline
(C,U,V)&(125,157,249)&(306,203,500)&(434,497,963)&
(951,645,1743)&(1087,1435,2965)&(1469,1636,4895).
\end{array}                                               \tag{5}
\]

The twelve-point candidate improves the cyclic deletion candidate from
$504$ to $500$.  Every candidate through $n=18$ is stable under every
ordered bipartition.  The $n=10,12$ candidates are stable under every
ordered three-colouring, and the $n=14,16,18$ candidates are stable under
every three-colouring which moves at most four labels away from one block.

The raw twenty-point candidate has one ten-face improvement, of block sizes
$(0,19,1)$.  Realizing that mutation by an exact rational strong glue gives

\[
                         (C,U,V)=(1441,2191,4885),        \tag{6}
\]

after which no ordered three-colouring moving at most four labels decreases
the count.  This is the same phenotype as the cyclic family: a short descent
ends at a fixed-block wall.

This follow-up strengthens the empirical negative conclusion but does not
strengthen the asymptotic kill condition.  All saved candidates are above
the coefficient-one-half scale at these sizes.  They therefore refute an
unconditioned fixed-$q$ descent theorem, not the sharper possibility that a
*strict fixed-gap sub-half* state must admit a decreasing mutation.  That
conditional version remains logically open, but it currently has no
sub-half viability witness and is not promoted to an active target.

## 6. Verification

Run

```text
python3 phase2/loop/erdos838/agent_mutation_spectrum_search/verify_mutation_spectrum_controls.py
python3 phase2/loop/erdos838/agent_mutation_spectrum_search/verify_greedy_ifs_mutation_spectrum.py
python3 phase2/loop/erdos838/agent_mutation_spectrum_search/verify_annealed_coordinate_candidates.py
```

The first verifier exhausts all ordered two- and three-colourings of the
four controls. The second reconstructs the rational cyclic IFS, certifies
the greedy deletion sequence, exhausts the displayed $n=10,12,14$
three-colourings, performs the sparse $n=16,18,20$ audit, constructs (4),
and reruns the sparse audit after mutation.
The third certifies the saved annealed coordinates, their two- and
three-block spectra in the stated ranges, and the exact repair (6).
