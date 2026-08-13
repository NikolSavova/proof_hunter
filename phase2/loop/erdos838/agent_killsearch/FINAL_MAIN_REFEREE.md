# Final adversarial referee pass on paper/main.tex

**Date:** 2026-08-13  
**Verdict:** **MATHEMATICALLY READY AFTER MINOR REVISION; NOT YET
SUBMISSION-READY OPERATIONALLY.**

I found no false theorem, missing branch, reversed inequality, or
coefficient-level gap in the integrated Section 5. It faithfully implements
the audited endpoint-reset proof. The source also compiles successfully with
Tectonic to a nine-page PDF, without TeX warnings.

Before public submission, make the precise wording and exposition changes
below, add the authors, and complete the already-planned external
MathSciNet/Zentralblatt and geometer check. The novelty language is mostly
appropriately restrained.

## 1. Section 5 mathematical audit

### Exact recurrences and endpoint identity: correct

Lines 426--509 correctly derive
\[
\begin{aligned}
C(A\prec B)&=C(B)+(b+1)C(A),\\
U(A\prec B)&=U(A)+(a+1)U(B),\\
W(A\prec B)&=W(A)+W(B)+C(A)U(B),
\end{aligned}
\]
and the exact max recurrences
\[
\begin{aligned}
X(A\prec B)&=\max\{(b+1)X(A),X(B)\},\\
Y(A\prec B)&=\max\{Y(A),(a+1)Y(B)\},\\
M(A\prec B)&=\max\{M(A),M(B),X(A)Y(B)\}.
\end{aligned}
\]
The crossing endpoint identities
\(c(p,q)=x_A(p)\), \(u(p,q)=y_B(q)\) justify the last recurrence.
The singleton convention in
\[
x(p)=1+\sum_{q>p}c(p,q)
\]
is handled correctly, so \(X,Y\le |S|M\).

The cap--cup product lemma is also correct. In line 457, “convexity of
\(x^d\)” means convexity of the function \(d\mapsto x^d\) on \([0,1]\);
the displayed chord inequality has the right direction. The identity
\[
\sum_i d_it_i=\frac{(\log s)^2+\sum_i d_i^2}{2}
\]
and all factors of two in passing from \(R=\sqrt{CU}\) to
\(\log C+\log U\) check out.

### Heavy-path dichotomy: correct

Lines 511--549 reproduce the audited constants:

- total scale loss before stopping is \(>4R\);
- each large level contributes at most one bit;
- each nonlarge level contributes at most \(2/L^2\);
- fewer than \(R\) large levels therefore force more than
  \(\tfrac32RL^2\) nonlarge levels;
- a majority color gives more than \(\tfrac34RL^2\) independent optional
  sibling leaves.

Lines 527--532 now include the needed upward cap/cup induction. The side
labels are correct: right siblings mean the path continues left and yield
caps; left siblings yield cups.

In the other branch, every selected node occurs before the \(4R\)-bit stop,
so its followed child and sibling have log-sizes at least
\[
L-4R-1,\qquad L-4R-2\log L.
\]
Thus the common window with
\(\Delta=4R+2\log L+1\) and the uniform radial threshold
\[
F=\frac12(L-\Delta)^2-3L
\]
are valid for all sufficiently large \(L\).

### Reset and nesting: correct

Lines 551--596 correctly use the global
\(\mu=\log M(P)\). Monotonicity gives \(M(S)\le M(P)\) for every subtree,
and \(X(S),Y(S)\le |S|M(S)\) gives the coordinate ceiling
\(\mu+L\). Hence every selected-child coordinate is at least
\(\ell=F-\mu-L\).

At the deepest selected cross,
\[
x_A+y_B\le\mu
\quad\Longrightarrow\quad
x_B,y_A\ge 2(F-\mu)-L.
\]
At every later selected attachment, a left path child forces an \(x\)-gain
of \(D=F-\mu\), while a right path child forces a \(y\)-gain of \(D\).
Both coordinates are monotone through intervening unselected nodes, so
alternating directions do not cancel gains.

The actual majority count \(q_*\) is used, and the final-occurrence
off-by-one is correct:
\[
\mu\ge h_0+(q_*-1)D+\ell=(q_*+2)D-2L.
\]
Solving for \(\mu\), with \(q_*=\Omega(\sqrt L)\), yields exactly the
claimed \(L^2/2-O(L^{3/2})\) bound.

## 2. Required fixes before submission

### A. Clarify what “sharp throughout the class” means

**Location:** abstract, lines 46--50.

Current wording:

> Thus the coefficient \(1/2\) is sharp throughout this nonstationary
> class.

This can be read as saying every sequence of strongly decomposable sets has
coefficient exactly \(1/2\), whereas many such sequences have much larger
counts. What is proved is that \(1/2\) is the optimal universal lower
coefficient and is attained by examples in the class.

**Replace with:**

> This lower bound is asymptotically attained within the class, so \(1/2\)
> is its optimal universal coefficient.

### B. Avoid the universal priority claim about graph transfers

**Location:** introduction, lines 110--112.

Current wording:

> ... but no transfer between the two settings is known.

The primary-source sweep found no transfer, but this is a broad negative
claim and unnecessary to the theorem.

**Replace with:**

> The same base-normalized coefficient occurs in Székely's
> graph-theoretic analogue \cite{Szekely1984}; its argument does not directly
> yield the geometric statement proved here.

Alternatively say “we do not know a transfer,” which is appropriately
qualified.

### C. Make the strong-substitution upper example explicit

**Location:** proof of Theorem 5.1, lines 598--603.

Current wording:

> substitution of a strong tree at every leaf of a strong tree is again
> strong.

This is true, but it is the only bridge connecting the Section 2 directional
composition \(S[Q]\) to the recursively strong class. Add the reason:

> Indeed, at each macro internal node, triples meeting its two sides have
> the strong-separation signs by Lemma 2.1, including when two points lie in
> one substituted block. Hence replacing every leaf by the strong tree of
> \(Q\) produces the ordered tree obtained by tree substitution.

Then retain the induced-subset/unary-suppression sentence. This is an
expository omission, not a logical failure.

### D. Correct the Erdős bibliography label

**Location:** manual bibliography, line 634.

Change

    \bibitem[EH78]{Erdos1978}

to

    \bibitem[Erd78]{Erdos1978}

or use the label Er78. Hammer posed the problem with Erdős but is not an
author of the 1978 paper; EH78 visually suggests a nonexistent coauthorship.

### E. Support the coefficient-one “standard estimate”

**Location:** abstract lines 32--34 and introduction lines 67--90.

The novelty audit did not locate a peer-reviewed theorem stated in exactly
the normalized coefficient-one form. The claim is correct and elementary,
but should be supported rather than left as a historical assertion. Add a
one-sentence derivation in the introduction:

> The classical \(2^{k-2}\)-point construction has no convex \(k\)-subset,
> and therefore has at most
> \(\sum_{j<k}\binom{2^{k-2}}j\) convex subsets; its base-two logarithm is at
> most \((1+o(1))(k-2)^2\), and deletion handles intermediate \(N\).

This removes any “previous best published constant” ambiguity.

### F. Replace the imprecise interval sentence

**Location:** introduction, lines 87--88.

Current:

> this places the normalized quantity in the interval \([1/4,1/2]\).

The proved statements concern liminf and limsup.

**Replace with:**

> Together with Theorem 1.1, this bounds the liminf below by \(1/4\) and
> the limsup above by \(1/2\); in particular, every limit point lies in
> \([1/4,1/2]\).

### G. Finish submission metadata

**Location:** line 20 and README.

The author field is empty. This is an absolute operational blocker to
submission, though not a mathematical issue. Add author names, affiliations,
contact details as appropriate, and the AI-assistance/provenance disclosure
required by the target venue.

## 3. Recommended, nonblocking improvements

1. **Section 5, line 545:** write explicitly “for \(L\) sufficiently large,
   \(L-\Delta>3\), so \(u^2/2-3u\) is increasing.” The proof already begins
   by absorbing bounded \(N\), so this is only clarity.
2. **Section 5, lines 559 and 565:** refer to the “uniform bound
   \(x+y\ge F\) just established,” rather than to the raw radial equation,
   which has a child-size-dependent right side.
3. **Section 5, line 596:** the reset branch bounds \(\mu\) directly and then
   uses \(W\ge M\). In the pure-comb branch the proof bounds \(W\) directly.
   This is correct; one sentence noting the two different routes would make
   the structure easier to scan.
4. **Product lemma, line 457:** replace “convexity of \(x^d\)” with
   “convexity of \(d\mapsto x^d\).”
5. **Bibliography width:** use HOPTV22 rather than HKSS19 as the width
   argument to the bibliography environment, since the former is the widest
   displayed label.
6. **Persistent identifiers:** the handwritten bibliography omits the DOIs
   present in references.bib. Adding them is desirable, especially for
   Baek--Balko, Han et al., Huemer et al., and Székely.
7. **Base convention:** move “all logarithms are base two” to the first
   paragraph of the introduction, before the lower-bound calculation.

## 4. Novelty and priority verdict after adding Theorem 5.1

The integrated wording does **not** claim to introduce order-type blow-ups,
almost-vertical blow-ups, or exact convex-polygon enumeration in general. It
correctly cites:

- Han et al. for general and iterated order-type blow-ups;
- Baek--Balko for almost-vertical Erdős--Szekeres blow-ups;
- Huemer et al. for exact weighted polygon identities; and
- Székely for the same base-normalized graph coefficient.

The new strong-class theorem is presented as an additional theorem, not as a
“first” theorem. That is submission-safe. The defensible contribution is now
twofold:

1. the mixed-\(2+1\)-orientation substitution identities and geometric
   upper coefficient \(1/2\); and
2. the matching universal lower coefficient for arbitrary recursive strong
   decompositions.

The second result is substantially broader than fixed-template optimality,
but it remains a theorem about a special recursively decomposable class, not
about all planar order types. Lines 114--118 and the final sentence of the
abstract preserve this distinction. Do not change “inside the class” to a
claim about Erdős problem 838 itself.

## 5. Final submission gate

After fixes A--G:

- **mathematical correctness:** pass;
- **internal proof completeness:** pass;
- **LaTeX build:** pass under Tectonic;
- **novelty wording:** pass, subject to the qualified graph-transfer wording;
- **external novelty clearance:** still pending by design;
- **authorship/venue metadata:** pending.

I would circulate the corrected draft privately to a discrete geometer now.
I would not upload publicly until the author block and external similarity
check are complete.
