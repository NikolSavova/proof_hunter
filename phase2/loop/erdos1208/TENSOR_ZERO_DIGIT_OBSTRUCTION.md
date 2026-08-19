# The zero-digit obstruction to Cartesian tensor powers

## 1. Status

An earlier draft attempted to disprove the size-biased opposite-endpoint
estimate by tensoring the six-point sheared Welch--Costas set.  That argument
is invalid.  A Cartesian digit tensor of a nontrivial point set is never
vector-Sidon once it has at least two coordinates, regardless of how generic
the complex digit weights are.

The failure is elementary but load-bearing.  A zero coordinate difference
has many endpoint representations.  Generic weights can separate distinct
*digit-difference vectors*; they cannot separate two pairs that have exactly
the same digit-difference vector.

Consequently the proposed tensor family is not distance-Sidon, the claimed
power-law counterexample to charge near-injectivity does not exist, and the
size-biased opposite-endpoint estimate remains open.

This is also a regression catch, not a newly discovered phenomenon:
`CROSS_TRANSLATION_OVERLAP.md` and the August 17 research log had already
recorded the same cylinder-collision obstruction for an earlier tensor
proposal.  The later charge draft failed to carry that kill forward.

## 2. Universal obstruction

Let `B` contain distinct points `b,c,x,y`, let `r>=2`, and choose arbitrary
nonzero complex weights `lambda_1,...,lambda_r`.  The Cartesian digit image

\[
 A_r=\left\{\sum_{j=1}^r\lambda_j b_j:b_j\in B\right\}
 \tag{2.1}
\]

contains, already in the first two coordinates, the four points

\[
\begin{aligned}
 P &=\lambda_1b+\lambda_2x+z, &
 Q &=\lambda_1c+\lambda_2x+z,\\
 P'&=\lambda_1b+\lambda_2y+z, &
 Q'&=\lambda_1c+\lambda_2y+z,
\end{aligned}                                                   \tag{2.2}
\]

where the remaining digits have been fixed and absorbed into `z`.  Whenever
the digit map is injective these are two different unordered pairs, but

\[
 P-Q=\lambda_1(b-c)=P'-Q'.                         \tag{2.3}
\]

Thus the two pairs have exactly the same displacement and squared distance.
No algebraic-genericity choice can remove (2.3).

The flaw in the earlier polynomial argument occurred after the conclusion
`d=e` for two digit-difference vectors.  Directed-difference uniqueness of
the base determines the coordinate endpoints when `d_j` is nonzero.  When
`d_j=0`, however, every diagonal pair `(b_j,b_j)` represents that coordinate
difference.  Hence equality of all digit differences does not determine the
two global endpoints.

## 3. Immediate cardinality contradiction

For the six-point base used in the draft,

\[
 |B|=6,\qquad |B-B|=31.                              \tag{3.1}
\]

The draft claimed simultaneously that the two-fold tensor was
distance-Sidon and that its complete difference set had `31^2=961` elements.
But an injective two-fold digit image has `36` points, and every
distance-Sidon set of `36` points has

\[
 36\cdot35+1=1261                                  \tag{3.2}
\]

directed difference values including zero.  Equations (3.1)--(3.2) are
already incompatible.  The missing `300` values are precisely endpoint
multiplicities hidden in zero digit coordinates.

The accompanying verifier constructs an injective integral two-fold image,
exhibits (2.3), checks that it is not distance-Sidon, and checks the
`961<1261` contradiction.

## 4. Research consequence

The exact opposite-endpoint charge and its fibrewise injectivity remain
valid.  The following implication is again a live route:

\[
 \sum_{v,t}\nu(v,t)^2
 \le N^{o(1)}\sum_{v,t}\nu(v,t)
 \quad\Longrightarrow\quad
 \sum_{v,t}\nu(v,t)\le N^{1+o(1)}|D+D|.          \tag{4.1}
\]

Base-level charge collisions and their numerical growth are evidence to
stress-test (4.1), not an asymptotic counterexample.  Any valid amplification
would need a non-Cartesian construction whose full complete difference set
still has unique nonzero endpoint representations.  A Sidon code inside
`B^r` does not automatically preserve the coordinatewise rich-fibre counts,
so it cannot be inserted into the old argument without a new theorem.

This obstruction also prevents using naive Cartesian tensor powers to
"exactify" the orthogonal two-support conjecture or to disprove the rotated
triple-support conjecture.  Those questions remain unchanged.
