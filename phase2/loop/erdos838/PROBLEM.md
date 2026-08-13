# Erdős problem 838 — frozen statement and target

## Correct statement

For a finite planar point set (P) in general position, let (v(P)) be the
number of subsets of (P) that are in convex position.  Define

\[
f(N)=\min\{v(P): |P|=N,\ P\subset\mathbb R^2\text{ in general position}\}.
\]

Equivalently, (f(N)) is the largest integer such that every (N)-point set
in general position determines at least (f(N)) convex subsets.  Erdős and
Hammer asked whether

\[
\frac{\log f(N)}{(\log N)^2}
\]

has a limit and, if so, what it is.

The old pipeline paraphrase in `problem-id/review/deeppass_remaining.md`
incorrectly says "the maximum, over (N)-point sets".  Taken literally that
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

The lower constant uses Suk's (ES(k)=2^{k+o(k)}) theorem and a
double-counting argument.  The upper constant counts all subsets of size at
most (log_2 N+O(1)) in the classical Erdős--Szekeres construction.

## Candidate new target

Prove the strict upper-window improvement

\[
\boxed{
\limsup_{N\to\infty}\frac{\log_2 f(N)}{(\log_2 N)^2}
\leq \frac{1}{2\ln 2}=0.7213475204\ldots .
}
\]

The construction is the standard (2^m)-point Morris--Soltan / Erdős--Szekeres
row construction.  The new ingredient is to count its convex subsets using
the cap/cup recursion instead of bounding them by all subsets of size at most
(m+1).

## Verification / kill criteria

The candidate bound dies if any of the following fails.

1. A cap in a recursively glued Pascal cell can use an unrestricted cap in
   one child and at most one point from the other child, giving the recurrence
   in `proof_draft.md`.
2. A convex subset spanning row blocks decomposes into a cap in its first
   occupied block, a cup in its last occupied block, and at most one point in
   each intermediate block.
3. Convex subsets contained in one block are bounded by the product of that
   block's cap and cup counts.
4. The maximum exponential rate of the resulting row sum is at most
   \(\int_0^1 H_2(t)\,dt=1/(2\ln2)\).
5. A fresh literature sweep finds the same or a stronger count already in
   print or in public notes.

Items 2 and the underlying construction are stated in Morris--Soltan,
*Bull. AMS* 37 (2000), Theorem 2.6 and its proof.  Item 4 has a short
pointwise proof.  Items 1 and 3 still need line-by-line geometric refereeing.

## Primary links

- Official problem: <https://www.erdosproblems.com/838>
- Discussion thread: <https://www.erdosproblems.com/forum/thread/838>
- Morris--Soltan survey: <https://doi.org/10.1090/S0273-0979-00-00877-6>
- Eppstein's exposition of the Pascal-row construction:
  <https://11011110.github.io/blog/2017/07/01/pascals-triangle-points.html>

