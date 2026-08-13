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

## Candidate new target

Prove the strict upper-window improvement

\[
\boxed{
\limsup_{N\to\infty}\frac{\log_2 f(N)}{(\log_2 N)^2}
\leq 1-\frac{1}{4\ln 2}=0.6393262398\ldots .
}
\]

The construction uses the central cell
\(T_{m,\lfloor m/2\rfloor}\) of the standard Morris--Soltan /
Erdős--Szekeres Pascal construction. It has \(2^{m-o(m)}\) points. The new
ingredient is to count its caps and cups recursively, then use the fact that
every convex subset is determined by its upper cap and lower cup.

## Verification / kill criteria

The candidate bound dies if any of the following fails.

1. A cap in a recursively glued Pascal cell can use an unrestricted cap in
   one child and at most one point from the other child, giving the recurrence
   in `proof_draft.md`.
2. Convex subsets contained in one cell are bounded by the product of that
   cell's cap and cup counts.
3. The central cap rate is
   \(A(1/2)=1/2-1/(8\ln2)\).
4. The passage from \({m\choose\lfloor m/2\rfloor}\) points to arbitrary
   \(N\) changes the leading coefficient.
5. A fresh literature sweep finds the same or a stronger count already in
   print or in public notes.

The underlying separated-union construction is stated in Morris--Soltan,
*Bull. AMS* 37 (2000), Theorem 2.5 and its proof. The new proof is in
proof_central.md; the independently audited row calculation remains in
proof_draft.md as a weaker \(0.721347\ldots\) route.

## Primary links

- Original 1978 paper:
  <https://users.renyi.hu/~p_erdos/1978-44.pdf>
- Official problem: <https://www.erdosproblems.com/838>
- Discussion thread: <https://www.erdosproblems.com/forum/thread/838>
- Morris--Soltan survey: <https://doi.org/10.1090/S0273-0979-00-00877-6>
- Eppstein's exposition of the Pascal-row construction:
  <https://11011110.github.io/blog/2017/07/01/pascals-triangle-points.html>
- Dated prior-art record: prior_art_20260812.md
