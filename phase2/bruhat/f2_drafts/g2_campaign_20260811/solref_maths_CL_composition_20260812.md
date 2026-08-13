# maths referee (gpt-5.6-sol, effort=max) — CL_composition_20260812.md — 2026-08-12 19:06

> Cross-model referee report (Sol on the reviewed draft). Numeric checks are
> DERIVED, not executed — script them before trusting.

### Hand recomputation

The displayed arithmetic is internally consistent:

- \(560-4+1=557\) harness rows; the split \([401,560]\) and \(m\ge561\) has no integer gap.
- \(0.89^2/2=0.39605\).
- W7:
  \[
  6.6/2+0.3(2.2)^2=3.3+1.452=4.752,
  \]
  hence \(4.752+0.39605=5.14805\).
- \(20(0.911407)=18.22814\) and \(20(0.65297)=13.0594\).
- The W1 split \([561,699]\) and \(m\ge700\) is arithmetically contiguous, and \(462<561\).
- The quoted variance floor is
  \[
  \frac{1122800}{7921}=141.749779\ldots>79.
  \]

These checks do not repair the following quantifier and interface gaps.

VERDICT: MAJOR_ISSUES

1. **(§2 step 3; §3[C]; §5.3, “Fact R.G closes \(m\in[561,699]\) for all \(w>4\)”, finite probes do not prove the continuum claim).**  
   The 25,122 probes are a finite \(w\)-grid—indeed \(25{,}122=237\cdot106\)—and the additional 3,594 probes remain finite sampling. Theorem X.1 gives monotonicity in \(\tau\), not in \(w\), so it does not interpolate between the 106 sampled \(w\)-values. Nor does probing \(w=4+10^{-9}\) cover \(4<w<4+10^{-9}\). The note itself calls the one-crossing property “evidence,” not a proved interval enclosure. The proposed M3 replacement is merely asserted: no bound, cell formula, endpoint argument, or named landed lemma is reproduced, and it is not checked by `compose_chain.py`. The pending adoption of M3 into Corollary R.3 is also omitted from §5.2’s repair inventory. Thus the universal W1 rung is presently unsupported, and “exactly four hypotheses” silently omits a \(w\)-continuum certificate.

2. **(§2 step 1; §4(S4), “the seed and convexity close the INFL/QUADF bootstrap”, the stated facts are insufficient for the fixed-point conclusion).**  
   Put \(x=|s_2(r-1)-1|\) and \(a=20/m\). To deduce \(x\le a\), the proof must state and establish uniformly that
   \[
   x\le G_{m,W}(x),\qquad G_{m,W}(t)<t\quad(a<t\le0.89).
   \]
   Convexity/increase of \(G\) and \(G(a)<a\) alone do not imply the second inequality: a convex increasing function can cross the diagonal later. A chord proof additionally needs a rigorous bound \(G(0.89)<0.89\), plus the correct inequality direction and a reduction proving that the “two thinnest rows” dominate every band and every \(m\ge561\). The later decimal “seed basins” suggest the intended endpoint check but neither define the basin nor supply exact inequalities. Since \(0.89\) lies only about \(0.00412\) below the quoted worst basin, directed rounding matters. This load-bearing closure must be stated as a lemma with \(G\), its domain, endpoint signs, and uniformity; citation to an unlanded referee construction is not enough.

3. **(Theorem CL-C; §4(S1)–(S3), “statements verbatim” and “let \(W\) be the band”, the hypotheses are not mathematically defined in this note).**  
   No W1–W7 interval table or endpoint convention is given. Consequently the slash-separated constants cannot be assigned at band boundaries, and the use of the label “W6b” leaves the band partition especially ambiguous. This matters because constants and proof routes jump between bands and because \(w=4\) is an open target edge. The exact rational values of \(J_0(W)\) are also replaced by displayed decimals without saying whether those decimals are exact or directed bounds. The theorem must import the complete band table, including open/closed endpoints, and state the exact \(J_0\) fractions required by Theorem E.

4. **(I5; §2 step 1, “(S1)+(S3) and Theorem E imply the pricing bound”, missing interface identification).**  
   The inventory says Theorem E assumes `(E-A2)+(E1)+(E2)+(E3)`, whereas the proof simply substitutes (S1)+(S3). It never identifies E1 and E2, clause by clause, with the two inequalities in S1, nor identifies the exact proved input supplying E-A2. In particular, one must check whether E2 requires a signed or absolute fourth-cumulant bound and whether its band-edge conventions coincide with S1. Until those hypotheses are quoted and matched exactly, the invocation of Theorem E has a silently assumed interface.

5. **(§0 and §2 step 5, “\(\min(m,s_2)=m\) on the band”, not established by the displayed variance bound).**  
   The only explicit universal floor in this note is
   \[
   s_2\ge1122800/7921=141.749779\ldots,
   \]
   which is strictly less than every \(m\ge561\) and therefore does not imply \(s_2\ge m\). The reference to an “[A2](iii)-bonus” does not state the needed inequality or its dependence on \(c_A(W)\) and \(\lambda\). Since the share normalization and bootstrap use \(20/m\), the composition must quote the exact bandwise formula proving \(s_2/m\ge1\), and check its worst band edge, rather than cite the unrelated \(s_2>79\) floor.

6. **(I3 and the paragraph following the inventory, “every input I1–I7 is citable and two-referee”, inconsistent with the governing status and with the consumed threshold repair).**  
   I3 explicitly consumes the hygiene overlay’s repair \(M_H=560\), but that overlay has zero referees under the supplied campaign ledger and is expressly not yet citable. The new composition script is likewise not a substitute for the owed hygiene verifier. This does not by itself invalidate the theorem restricted to \(m\ge561\), but it invalidates the claims that the threshold/finite split is already a two-referee input and that every node in the combined Theorem A chain is presently citable.

7. **(§4(S3), “Prop. E.3 proves the joint hypothesis is unavoidable”, logical overstatement).**  
   The counterexample establishes that the old assumptions and the proposed sign-lemma route do not imply the desired pricing inequality. It does not prove that this particular bound \(J\le J_0(W)\) is logically unavoidable; a different joint estimate or a different pricing argument could suffice. Replace “unavoidable” by “required by the present Theorem E certificate / old route shown insufficient.”