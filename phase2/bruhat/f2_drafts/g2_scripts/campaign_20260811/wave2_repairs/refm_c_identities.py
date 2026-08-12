"""Maths-referee checks C: independent re-implementation of the structural identities.

(a) T.2 summed forms (2.2)-(2.5): kappa_r(lam) = (-1)^{r+1}[sum_j j^r g^{(r-1)}(lam j)
    - m g^{(r-1)}(lam)] vs cumulants computed from the EXACT pmf of X = sum U_j
    (direct convolution, mpmath dps 50) at (m, lam) = (8, 0.3), (12, 0.05).
    This is NOT the draft's script route (which used per-factor moment recursions).
(b) T.5 staircase decomposition: p_i = sum_{s>i} c_s/s with c_s = s(p_{s-1}-p_s):
    exact-Fraction verification on random nonincreasing weight vectors, plus (**).
(c) T.4 kernel: E(u) = sum_{n>=1} 2(3 v_n^2 + u^2)/(v_n^2 (v_n^2+u^2)^2) vs the
    direct (1/12 - q(u))/u^2; the lower bound (1/240)(1 - u^2/19.7); E decreasing.
"""
from mpmath import mp, mpf, exp, diff, pi
from fractions import Fraction as F
import random

mp.dps = 50

def g(u):
    return 1/u - 1/(exp(u) - 1)

print("== (a) (2.2)-(2.5) vs exact-pmf cumulants ==")
for (m, lam) in [(8, mpf('0.3')), (12, mpf('0.05'))]:
    # exact pmf of X = sum_j U_j^{lam} by convolution
    pmf = [mpf(1)]
    for j in range(1, m+1):
        w = [exp(-lam*i) for i in range(j)]
        Z = sum(w)
        w = [x/Z for x in w]
        new = [mpf(0)]*(len(pmf)+j-1)
        for a, pa in enumerate(pmf):
            for b, pb in enumerate(w):
                new[a+b] += pa*pb
        pmf = new
    mu = sum(i*p for i, p in enumerate(pmf))
    cm = [sum((i-mu)**r * p for i, p in enumerate(pmf)) for r in range(5)]
    k2, k3 = cm[2], cm[3]
    k4 = cm[4] - 3*cm[2]**2
    # closed forms
    mu_c = sum(j*g(lam*j) for j in range(1, m+1)) - m*g(lam)
    s2_c = -(sum(j*j*diff(g, lam*j) for j in range(1, m+1)) - m*diff(g, lam))
    k3_c = sum(j**3*diff(g, lam*j, 2) for j in range(1, m+1)) - m*diff(g, lam, 2)
    k4_c = -(sum(j**4*diff(g, lam*j, 3) for j in range(1, m+1)) - m*diff(g, lam, 3))
    for name, a, b in [("mu", mu, mu_c), ("k2", k2, s2_c), ("k3", k3, k3_c), ("k4", k4, k4_c)]:
        rel = abs(a-b)/max(abs(a), mpf(10)**-30)
        print("  m=%2d lam=%s %-3s: exact-pmf %.12g closed %.12g  rel dev %.1e" %
              (m, str(lam), name, float(a), float(b), float(rel)))

print("== (b) T.5 staircase + (**) on 500 random nonincreasing exact-Fraction vectors ==")
random.seed(7)
ok_dec, ok_star, worst = True, True, F(10**9)
for trial in range(500):
    j = random.randint(1, 12)
    raw = sorted([random.randint(0, 20) for _ in range(j)], reverse=True)
    if sum(raw) == 0:
        raw[0] = 1
    tot = sum(raw)
    p = [F(x, tot) for x in raw]
    # staircase: c_s = s(p_{s-1} - p_s), p_j = 0
    pp = p + [F(0)]
    c = [s*(pp[s-1]-pp[s]) for s in range(1, j+1)]
    if any(x < 0 for x in c) or sum(c) != 1:
        ok_dec = False
    for i in range(j):
        if sum(c[s-1]/s for s in range(i+1, j+1)) != p[i]:
            ok_dec = False
    EU = sum(F(i)*p[i] for i in range(j))
    EU2 = sum(F(i*i)*p[i] for i in range(j))
    Var = EU2 - EU*EU
    margin = Var - (EU*EU/3 + EU/3)
    worst = min(worst, margin)
    if margin < 0:
        ok_star = False
print("  decomposition exact on all vectors: %s ; (**) holds: %s ; min margin = %s" %
      (ok_dec, ok_star, float(worst)))

print("== (c) T.4 kernel E(u): partial-fraction sum vs direct; lower bound; monotone ==")
def E_direct(u):
    q = 1/u**2 - exp(u)/(exp(u)-1)**2
    return (mpf(1)/12 - q)/u**2
def E_pf(u, N=200000):
    s = mpf(0)
    for n in range(1, N+1):
        v2 = (2*pi*n)**2
        s += 2*(3*v2 + u*u)/(v2*(v2+u*u)**2)
    return s
dev = max(abs(E_direct(u)-E_pf(u))/E_direct(u) for u in [mpf('0.3'), mpf(1), mpf(2), mpf('3.14')])
print("  max rel dev direct vs partial-fraction (4 pts, N=2e5): %.1e" % float(dev))
lows = [(float(u), float(E_direct(u)*240), float(1-u*u/mpf('19.7'))) for u in [mpf('0.5'), mpf(1), mpf(2), mpf(3), mpf('3.14')]]
allok = all(a >= b for _, a, b in lows)
print("  240*E(u) vs 1-u^2/19.7:", [(u, round(a, 4), round(b, 4)) for u, a, b in lows], "lower bound holds:", allok)
vals = [E_direct(mpf(x)/10) for x in range(1, 32)]
print("  E decreasing on (0, 3.1]: %s ; E(pi)*240 = %.5f" %
      (all(vals[i] > vals[i+1] for i in range(len(vals)-1)), float(E_direct(pi)*240)))
