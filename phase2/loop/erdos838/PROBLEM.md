# Erdős problem 838 — frozen statement and target

## Correct statement

For a finite planar point set \(P\) in general position, let \(v(P)\) be the
number of subsets of \(P\) that are in convex position.  Define

\[
f(N)=\min\{v(P): |P|=N,\ P\subset\mathbb R^2\text{ in general position}\}.
\]

Equivalently, \(f(N)\) is the largest integer such that every \(N\)-point set
in general position determines at least \(f(N)\) convex subsets.  Erdős and
Hammer asked whether

\[
\frac{\log f(N)}{(\log N)^2}
\]

has a limit and, if so, what it is.

The old pipeline paraphrase in `problem-id/review/deeppass_remaining.md`
incorrectly says "the maximum, over \(N\)-point sets".  Taken literally that
version is trivial.  The extremal direction above is the one on the official
problem page and in Erdős's original formulation.

## Current public window (base-2 logarithms)

The April 2026 discussion on the Erdős Problems page records the elementary
window

\[
\frac14\leq
\liminf_{N\to\infty}\frac{\log_2 f(N)}{(\log_2 N)^2}
\leq
\limsup_{N\to\infty}\frac{\log_2 f(N)}{(\log_2 N)^2}
\leq 1.
\]

The lower constant uses Suk's \(ES(k)=2^{k+o(k)}\) theorem and a
double-counting argument.  The upper constant counts all subsets of size at
most \(\log_2 N+O(1)\) in the classical Erdős--Szekeres construction.

## Candidate new upper theorem

Prove the strict upper-window improvement

\[
\boxed{
\limsup_{N\to\infty}\frac{\log_2 f(N)}{(\log_2 N)^2}
\leq \frac12.
}
\]

The construction repeatedly replaces every point of a large balanced
cap--cup extremal template by a thin vertical copy of the preceding iterate.
The exact cap, cup, and convex-subset substitution formulas give coefficient
\((a+b-2)/(2\log_2 r)\) for a fixed \(r\)-point template whose largest cap
and cup have sizes \(a,b\). Balanced Pascal cells make this tend to \(1/2\).
The earlier central-cell construction gives the weaker audited coefficient
\(1-1/(4\ln2)=0.639326\ldots\).

## Verification / kill criteria

The candidate bound dies if any of the following fails.

1. The thin vertical composition does not realize the four asserted classes
   of orientation signs.
2. A spanning convex subset can use more than one point in an intermediate
   macro-block, or its occupied macro-blocks need not be convex.
3. The exact substitution formula in `proof_blowup_half.md` misses a class
   of caps, cups, or convex subsets.
4. Iterating the formula does not have coefficient
   \((a+b-2)/(2\log_2 r)\), or deletion to arbitrary \(N\) changes it.
5. A fresh literature sweep finds the same or a stronger count already in
   print or in public notes.

The new proof is in proof_blowup_half.md and its exact rational-coordinate
audit is lexicographic_blowup.py. The independently audited central-cell and
row calculations remain in proof_central.md and proof_draft.md as weaker
routes.

## Primary links

- Original 1978 paper:
  <https://users.renyi.hu/~p_erdos/1978-44.pdf>
- Official problem: <https://www.erdosproblems.com/838>
- Discussion thread: <https://www.erdosproblems.com/forum/thread/838>
- Morris--Soltan survey: <https://doi.org/10.1090/S0273-0979-00-00877-6>
- Eppstein's exposition of the Pascal-row construction:
  <https://11011110.github.io/blog/2017/07/01/pascals-triangle-points.html>
- Dated prior-art record: prior_art_20260812.md
