#!/usr/bin/env python3
"""Referee independent checks for wp3-a2 (part 1): exact algebra of P.2-P.4,
independent constant chain, E(u) rounding directions, R3 crossover."""
from fractions import Fraction
from math import comb
import mpmath as mp
mp.mp.dps = 50

def T(m, j): return comb(m - 1 + j, m - 1) if j >= 0 else 0

def xg(m, g, k):
    if g > k: return Fraction(0)
    num = den = 1
    for i in range(g):
        num *= (k - i); den *= (m + k - 1 - i)
    return Fraction(num, den)

print("== (1) x_g(k) = T(k-g)/T(k) product formula, exact ==")
bad = 0
for m in (5, 17, 30):
    for k in range(1, m + 1):
        for g in range(0, k + 1):
            if xg(m, g, k) != Fraction(T(m, k - g), T(m, k)):
                bad += 1
print("   mismatches:", bad)

print("== (2) Delta^2 x_1 and Delta^2 x_2 exact displays ==")
bad1 = bad2 = 0
for m in (7, 30, 101):
    for k in range(2, m):
        lhs1 = xg(m, 1, k + 1) + xg(m, 1, k - 1) - 2 * xg(m, 1, k)
        rhs1 = Fraction(-2 * (m - 1), (m + k) * (m + k - 1) * (m + k - 2))
        if lhs1 != rhs1: bad1 += 1
        lhs2 = xg(m, 2, k + 1) + xg(m, 2, k - 1) - 2 * xg(m, 2, k)
        rhs2 = Fraction(2 * (m - 1) * (m - 2 * k),
                        (m + k) * (m + k - 1) * (m + k - 2) * (m + k - 3))
        if lhs2 != rhs2: bad2 += 1
print("   Delta^2 x_1 mismatches:", bad1, " Delta^2 x_2 mismatches:", bad2)

print("== (3) Delta^2 x_g display for g >= 5, g <= (k+1)/2 (exact) ==")
bad3 = 0
for m in (30, 80):
    for k in range(2, m):
        for g in (5, 7, 12, 15):
            if g > (k + 1) // 2 or g > k - 1: continue
            lhs = xg(m, g, k + 1) + xg(m, g, k - 1) - 2 * xg(m, g, k)
            rhs = xg(m, g, k) * Fraction(g * (m - 1) * ((g - 1) * (m + k) - (g + 1) * k),
                                         (k + 1 - g) * k * (m + k) * (m + k - 1 - g))
            if lhs != rhs: bad3 += 1
print("   mismatches:", bad3)

print("== (4) independent constant chain (mpmath, 50 dps) ==")
def pent(limit=600):
    out, n = [], 1
    while True:
        g1 = n * (3 * n - 1) // 2; g2 = n * (3 * n + 1) // 2
        if g1 > limit: break
        out.append(g1)
        if g2 <= limit: out.append(g2)
        n += 1
    return sorted(out)
G = pent()
for cname, xc in (("1/4", mp.mpf(17) / 75), ("1/2", mp.mpf(16) / 45),
                  ("7/10", mp.mpf(22) / 51), ("1", mp.mpf(30) / 59)):
    s1p = sum(g * xc ** g for g in G)
    s2r = sum(g * g * xc ** (g - 2) for g in G if g >= 5)
    Phimin = 1 - xc - xc * xc
    Cd = s1p / xc
    CA = 4 + 6 * s2r
    CP = CA / Phimin + Cd ** 2 / Phimin ** 2
    c = {"1/4": 0.25, "1/2": 0.5, "7/10": 0.7, "1": 1.0}[cname]
    mp_thr = 3 * CP * c * (1 + c) + 1
    print(f"   c={cname}: Cd={mp.nstr(Cd,6)} CA={mp.nstr(CA,6)} CP={mp.nstr(CP,6)}"
          f" m_p=ceil({mp.nstr(mp_thr,7)})")

print("== (5) E(u) true values (closed form), rounding directions ==")
def Etrue(u):
    u = mp.mpf(u)
    q = 1 / u ** 2 - mp.e ** u / (mp.e ** u - 1) ** 2
    return (mp.mpf(1) / 12 - q) / u ** 2
for u, printed in ((1, "0.00400693"), (2, "0.00358719"), (3, "0.00304036"),
                   (4, "0.00248992"), (5, "0.00200652"), (6, "0.00161241")):
    ev = Etrue(u)
    ok = "SAFE(lower)" if mp.mpf(printed) <= ev else "UNSAFE (printed > true)"
    print(f"   E({u}) = {mp.nstr(ev, 12)}  printed {printed}  -> {ok}")

E4 = Etrue(4)
defl = mp.mpf("6.85") * 16 * mp.mpf("0.00248992")   # what the chain proves
print(f"   proved deficit floor 6.85*16*0.00248992 = {mp.nstr(defl, 8)}"
      f"  (draft claims >= 0.2729 -> {'OK' if defl >= mp.mpf('0.2729') else 'UNSAFE'})")
rho = 1 - defl
print(f"   proved rho(4) <= {mp.nstr(rho, 8)}  (draft claims <= 0.7271 ->"
      f" {'OK' if rho <= mp.mpf('0.7271') else 'UNSAFE'})")
d2 = mp.mpf("6.85") * 4 * mp.mpf("0.00358719")
print(f"   w0=2 floor = {mp.nstr(d2, 8)} (draft 0.0983 -> {'OK' if d2 >= mp.mpf('0.0983') else 'UNSAFE'})")
print(f"   R2 chain: (1-0.2516)/rho = {mp.nstr((1 - mp.mpf('0.2516')) / rho, 8)}  (draft: 1.0294)")

print("== (6) R3 bracket crossover: 6.85E4(1-17Bm-C/m^2) >= Bm ==")
def Bm(m):
    S4 = sum(j ** 4 for j in range(1, m + 1))
    lam = Fraction(m * (m - 1) * (2 * m + 5), 72)
    return Fraction(S4 - m, 240) / lam ** 2
a = mp.mpf("6.85") * mp.mpf("0.00248992"); C = mp.mpf("10.7")
def brk(m):
    b = mp.mpf(Bm(m).numerator) / mp.mpf(Bm(m).denominator)
    return a * (1 - 17 * b - C / m ** 2) - b
mstar = None
for m in range(30, 200):
    if brk(m) >= 0 and mstar is None: mstar = m
print(f"   smallest m with bracket >= 0: {mstar}  (draft note says '~68')")
print(f"   bracket at m=100: {mp.nstr(brk(100), 5)}; at m=401: {mp.nstr(brk(401), 5)}")
print(f"   at m=401: 6.85E4*(1-17Bm-C/m^2) = {mp.nstr(a*(1-17*(mp.mpf(Bm(401).numerator)/mp.mpf(Bm(401).denominator))-C/401**2), 7)} (draft claims >= 0.01628)")
