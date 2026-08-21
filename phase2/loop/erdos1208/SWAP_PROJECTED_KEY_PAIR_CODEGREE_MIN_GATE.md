# A three-channel codegree bound for projected completion keys

## 1. Outcome

The role-projected formulation is a bipartite incidence graph.  Its left
vertices are second-generation groups `g=(C,x,u,role)`, its right vertices
are projected completion keys, and its edges are reverse occurrences.  A
group contains at most one occurrence with a prescribed projected key.
Therefore the size-biased collision mass is a left-wedge count, and the
load of a fixed ordered pair of right keys is their common-group codegree.

This note gives three independent lossless inversions of that codegree.
Let

\[
 R(v)=R_D(v),\qquad
 R_{\mathcal P}(v)=|\mathcal P_K\cap(\mathcal P_K-v)|.          \tag{1.1}
\]

For the moving-`W` roles put

\[
 w=Js+Ld,\qquad j=J(s+d),                         \tag{1.2}
\]

and define

\[
\boxed{
 \Gamma_W(s,d)=R(d)\min\{R(s)R(w),R(s)R(j),R(w)R(j)\}.}       \tag{1.3}
\]

For the moving-`V` roles put

\[
 a=d-s,\qquad b=Js,\qquad e=Js+d,                \tag{1.4}
\]

and define

\[
\boxed{
 \Gamma_V(s,d)=R(Ld)\min\{R(a)R(b),R(a)R(e),R(b)R(e)\}.}      \tag{1.5}
\]

Let `mathcal G_2^same` denote the ordered cross-`t` pair mass for which the
two occurrences have the same one of the four oriented endpoint roles.
Then this diagonal-role part obeys the scalar reduction

\[
\boxed{
 \mathcal G_2^{\rm same}\le
 2k\!\sum_{\substack{s\in\mathcal P_K-\mathcal P_K\\
                      d\ne0,\ Ld\in D}}
 R_{\mathcal P}(s)\Gamma_W(s,d)
 +2k\!\sum_{\substack{s\in\mathcal P_K-\mathcal P_K\\
                       d\ne0,\ d\in D}}
 R_{\mathcal P}(s)\Gamma_V(s,d).}                \tag{1.6}
\]

All quantities on the right are global overlap functions; no centre,
physical endpoint, completion start, or metric-cell multiplicity remains.
Formula (1.6) is deliberately an upper gate rather than a claimed closure.
It is the first completely scalar target obtained for a full role block of
the endpoint-faithful completion program.  The mixed `W`--`V` role blocks
remain to be put into comparable scalar normal forms before (1.6) can be
used as a bound for the full `mathcal G_2`.

The minimum in (1.3)/(1.5) is load-bearing.  Each factor pair comes from a
different recovery triple; replacing the minimum by any one channel
reintroduces exactly the known resonant losses.

## 2. Moving-`W` codegree normal form

Fix two ordered projected keys

\[
 \eta_i=(r_i,B_i)\in\mathcal T_K^\perp,qquad i=1,2.            \tag{2.1}
\]

For them to occur in one group, their physical edges must contain the same
endpoint in the same oriented role, and

\[
 s=r_1-r_2,\qquad B_1-B_2=Ld                    \tag{2.2}
\]

for a nonzero integral `d=t_1-t_2`.  Use the second occurrence as base and
write `r=r_2`, `B=B_2`, `q=q_2`, `t=t_2`.  The common group has

\[
 q_1=q+s,\qquad t_1=t+d.                         \tag{2.3}
\]

With the six-vector notation of the four-norm inversion, put

\[
 X=c-q,\quad Y=B+Jq,\quad V=c+t,\quad
 E=B-Lt,\quad F=Y-t,\quad G=B+Jr-t.              \tag{2.4}
\]

The two occurrences require the following six translated pairs in `D`:

\[
\begin{array}{c|c}
\text{start}&\text{translation}\ \hline
X&-s\\
Y&Js+Ld=w\\
V&d\\
E&0\\
F&J(s+d)=j\\
G&J(s+d)=j.
\end{array}                                      \tag{2.5}
\]

They also retain the eight popular coordinates

\[
 r,r+s,q,q+s,r+t,r+t+s+d,q+t,q+t+s+d
 \in\mathcal P_K.                                \tag{2.6}
\]

There are three injective projections of a common group:

\[
 (X,Y,V),\qquad (X,F,V),\qquad (Y,F,V).          \tag{2.7}
\]

For the first, recover

\[
 q=-J(Y-B),\quad c=X+q,\quad t=V-c.              \tag{2.8}
\]

For the second, use

\[
 Lq=F-B-X+V,\quad c=X+q,\quad t=V-c.             \tag{2.9}
\]

For the third, use

\[
 t=Y-F,\quad c=V-t,\quad q=-J(Y-B).              \tag{2.10}
\]

In every case `u=q-r` and `ell=B-Lt` recover the group.  Counting the
available translated pairs in each projection proves (1.3).

## 3. Moving-`V` codegree normal form

Now fix

\[
 \eta_i=(r_i,A_i)\in\mathcal T_K^\parallel.       \tag{3.1}
\]

The physical directed edges are `c_i=A_i+r_i`; in one group they share the
fixed physical endpoint and

\[
 s=r_1-r_2,\qquad d=c_1-c_2=t_1-t_2\ne0.         \tag{3.2}
\]

The perpendicular completion start `B=ell` is fixed across the group.
Using the second occurrence, put

\[
 X=c-p,\quad Y=B+Jp,\quad C_0=c-t,\quad
 W=B+Lt,\quad F=Y+t,\quad G=B+Jr+t.              \tag{3.3}
\]

The six pair translations are

\[
 d-s,\quad Js,\quad0,\quad Ld,\quad Js+d,\quad Js+d.     \tag{3.4}
\]

The three injective recovery triples are

\[
 (X,Y,W),\qquad (X,F,W),\qquad (Y,F,W).          \tag{3.5}
\]

Indeed `(X,Y,W)` gives `p=c-X`, `B=Y-Jp`, and
`t=L^{-1}(W-B)`.  For `(X,F,W)`, first recover `p=c-X` and then solve

\[
 t=J(F-W-Jp),\qquad B=W-Lt.                      \tag{3.6}
\]

Finally `(Y,F,W)` gives `t=F-Y`, `B=W-Lt`, and
`p=-J(Y-B)`.  Then `u=p-r` and the original centre are recovered.  The
three translated-pair counts give (1.5).

## 4. From codegrees to the scalar aggregate

Fix `s,d`.  The ordered popular-key pair `(r_1,r_2)` has at most
`R_P(s)` choices.  For a fixed head-role pair of physical `W`
edges with `B_1-B_2=Ld`, directed-vector Sidonicity determines their two
nonshared endpoints.  The common physical endpoint has at most `k`
choices.  The tail role has the same bound.  Hence the two moving-`W`
roles contribute at most

\[
 2k R_{\mathcal P}(s)\Gamma_W(s,d).              \tag{4.1}
\]

The identical argument with the physical edges `c_i=A_i+r_i` gives (4.1)
with `Gamma_V` for the two moving-`V` roles.

Every same-role pair counted here consists of reverse occurrences in
different `t`-fibres of one group, so `d != 0`.  Summing (4.1) proves
(1.6).  Pairs whose two occurrences have different oriented roles are not
included; there are mixed `W`--`V` blocks as well as harmless head/tail
orientation constants.  Those mixed blocks are the exact next task.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_projected_key_pair_codegree_min.py
```

The verifier checks all six pair translations and all six recovery maps on
random integral data, exhausts the three-channel product bound on genuine
finite distance-Sidon difference sets, and verifies the factor-`k` physical
endpoint-pair count exactly.
