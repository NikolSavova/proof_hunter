#!/usr/bin/env python3
"""Referee independent checks for wp3-a2 (part 2): P.5 truth with an
independently-coded Mahonian generator; the T.4-Step-2 identity feeding P.7;
Lemma P.8's mean bound; R1b margin formula."""
from fractions import Fraction
import mpmath as mp
mp.mp.dps = 40

def mahonian_row(m):
    """Independent algorithm: naive polynomial product with explicit factor
    lists (no running-sum trick)."""
    poly = [1]
    for j in range(2, m + 1):
        fac = [1] * j
        new = [0] * (len(poly) + j - 1)
        for i, a in enumerate(poly):
            if a:
                for t in range(j):
                    new[i + t] += a
        poly = new
    return poly

print("== (7) P.5 truth, independent generator, m in {50, 121}, all 2<=k<=m-1 ==")
for m in (50, 121):
    row = mahonian_row(m)
    viol = 0
    minratio = None
    for k in range(2, m):
        num = row[k] * row[k] - row[k - 1] * row[k + 1]
        lhs = num * 2 * k * (m + k)
        rhs = (m - 1) * row[k - 1] * row[k + 1]
        if lhs < rhs: viol += 1
        rat = Fraction(lhs, rhs)
        if minratio is None or rat < minratio: minratio = rat
    print(f"   m={m}: violations={viol}, min ratio={float(minratio):.4f}")

print("== (8) T.4 Step-2 identity: lambda - s2 = lam^2 sum_j [j^4 E(lam j) - E(lam)] ==")
def E(u):
    u = mp.mpf(u)
    if u == 0: return mp.mpf(1) / 240
    q = 1 / u ** 2 - mp.e ** u / (mp.e ** u - 1) ** 2
    return (mp.mpf(1) / 12 - q) / u ** 2
def var_exact(lam, j):
    # truncated geometric on {0..j-1}, weights e^{-lam i}: exact moments
    ws = [mp.e ** (-lam * i) for i in range(j)]
    Z = sum(ws)
    m1 = sum(i * w for i, w in enumerate(ws)) / Z
    m2 = sum(i * i * w for i, w in enumerate(ws)) / Z
    return m2 - m1 ** 2
for m, w in ((25, 1.0), (25, 4.0), (60, 4.0), (60, 6.0)):
    lam = mp.mpf(w) / m
    lamb = mp.mpf(m * (m - 1) * (2 * m + 5)) / 72
    s2 = sum(var_exact(lam, j) for j in range(1, m + 1))
    lhs = lamb - s2
    rhs = lam ** 2 * sum((j ** 4) * E(lam * j) - E(lam) for j in range(1, m + 1))
    print(f"   m={m} w={w}: rel dev = {mp.nstr(abs(lhs - rhs) / abs(lhs), 3)}")

print("== (9) P.7 floor vs exact deficit, incl. large w (statement scope probe) ==")
for m, w in ((30, 4), (30, 8), (30, 20), (30, 60), (100, 4), (100, 8)):
    lam = mp.mpf(w) / m
    lamb = mp.mpf(m * (m - 1) * (2 * m + 5)) / 72
    s2 = sum(var_exact(lam, j) for j in range(1, m + 1))
    d = 1 - s2 / lamb
    fl = mp.mpf("6.85") * w * w * E(w)
    print(f"   m={m} w={w}: true deficit {mp.nstr(d,5)}  claimed floor {mp.nstr(fl,5)}"
          f"  {'OK' if d >= fl else 'VIOLATED'}")

print("== (10) P.8: mu(lam) <= m/(e^lam - 1); cap check ==")
def g(u):
    u = mp.mpf(u)
    if abs(u) < mp.mpf('1e-8'): return mp.mpf(1)/2 - u / 12
    return 1 / u - 1 / (mp.e ** u - 1)
def mu(lam, m):
    return sum(j * g(lam * j) for j in range(1, m + 1)) - m * g(lam)
for m in (30, 300):
    for c in (mp.mpf(1)/2, mp.mpf(7)/10, mp.mpf(1)):
        lamc = mp.log(1 + 1 / c)
        print(f"   m={m} c={mp.nstr(c,3)}: mu(lam_c)={mp.nstr(mu(lamc, m),6)}"
              f" vs c*m={mp.nstr(c * m,6)} -> {'OK' if mu(lamc, m) <= c * m + mp.mpf('1e-12') else 'VIOL'}")

print("== (11) R1b margin formula at m=401, c=0.7 ==")
m = 401; c = mp.mpf(7) / 10
val = (m - 1) ** 2 * (2 * m + 5) / (144 * c * (1 + c) * m)
print(f"   (m-1)^2(2m+5)/(144 c(1+c) m) = {mp.nstr(val, 6)} (draft: 1879)")
lamb = mp.mpf(m * (m - 1) * (2 * m + 5)) / 72
print(f"   check vs lambda*(m-1)/(2 c(1+c) m^2) = {mp.nstr(lamb * (m-1) / (2*c*(1+c)*m**2), 6)}")
