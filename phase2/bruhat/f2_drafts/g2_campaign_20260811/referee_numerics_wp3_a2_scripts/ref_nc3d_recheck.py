#!/usr/bin/env python3
"""Referee (numerics, wp3-a2): independent recomputation of NC-P3(c)/(d).

The draft's NC-P3 computes s2/mu via the g/q closed forms. Here the tilted
moments are computed by DIRECT weighted sums (prefix-sum pass over u, O(m)
per evaluation, no g/q, no series) — an independent implementation path.

Checks:
 (c') true deficit 1 - s2/lambda at lam = w0/m, m in {60, 120}, w0 in 2..6,
      vs the P.7 floor 6.85 w0^2 E(w0) with high-precision E (closed form,
      Decimal) — reproduces the draft's NC-P3(c) rows.
 (d') for m in {30, 60, 140}: eps(k) = |s2(lam(k)) (r(k)-1) - 1| over EVERY
      interior k in 2..N/2 (exact Mahonian rows; r-1 exact-int / correctly
      rounded float):
        - max eps over ALL interior k (the draft §6.1 claims 0.0385 at m=30
          covers "EVERY interior k");
        - max eps over the band [0.7m, w=4 edge] (draft: 0.0385/0.0194/0.0084);
        - whether eps <= 0.25 everywhere ("trueC0 = 0" claim);
        - cross-check of lam(k), s2 vs the draft script's closed forms at
          two spot points (agreement tolerance 1e-7 relative).
"""
from math import exp, log
from decimal import Decimal, getcontext
getcontext().prec = 40

def moments(lam, m):
    """(mu, s2) by direct prefix sums: U_j uniform{0..j-1} tilted by e^{-lam u}."""
    t = exp(-lam)
    A = B = C = 0.0   # sum p_u, sum u p_u, sum u^2 p_u for u < j (running)
    p = 1.0
    mu = s2 = 0.0
    for j in range(1, m + 1):
        u = j - 1
        # after this block, A,B,C cover u = 0..j-1
        A += p; B += u * p; C += u * u * p
        mean = B / A
        var = C / A - mean * mean
        mu += mean; s2 += var
        p *= t
    return mu, s2

def lam_of_k(k, m, iters=80):
    lo, hi = 1e-13, 40.0
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        if moments(mid, m)[0] > k: lo = mid
        else: hi = mid
    return 0.5 * (lo + hi)

def E_true(u):
    ud = Decimal(u); eu = ud.exp()
    q = 1 / (ud * ud) - eu / ((eu - 1) ** 2)
    return float((Decimal(1) / 12 - q) / (ud * ud))

def mahonian_row(m):
    poly = [1]
    for mm in range(1, m + 1):
        old = poly; new = [0] * (len(old) + mm - 1); run = 0
        for k in range(len(new)):
            if k < len(old): run += old[k]
            if 0 <= k - mm < len(old): run -= old[k - mm]
            new[k] = run
        poly = new
    return poly

print("(c') true deficit vs P.7 floor (independent moments):")
for m in (60, 120):
    lamb = m * (m - 1) * (2 * m + 5) / 72.0
    line = f"   m={m}:"
    for w0 in (2, 3, 4, 5, 6):
        _, s2 = moments(w0 / m, m)
        d_true = 1 - s2 / lamb
        fl = 6.85 * w0 * w0 * E_true(w0)
        line += f"  w0={w0}: {d_true:.4f}>={fl:.4f}{'ok' if d_true >= fl else ' VIOL'}"
    print(line)

print("(d') eps over ALL interior k (independent implementation):")
print("    m   max_eps(ALL k in [2,N/2])   max_eps(band)   band          any eps>0.25?")
for m in (30, 60, 140):
    row = mahonian_row(m)
    N = m * (m - 1) // 2
    k_edge = int(moments(4.0 / m, m)[0])
    k_lo = max(2, int(0.7 * m))
    mall = mband = 0.0
    aall = aband = None
    over25 = 0
    for k in range(2, N // 2 + 1):
        lam = lam_of_k(k, m)
        _, s2 = moments(lam, m)
        r1 = row[k] * row[k] / (row[k - 1] * row[k + 1]) - 1.0
        eps = abs(s2 * r1 - 1.0)
        if eps > mall: mall, aall = eps, k
        if k_lo <= k <= k_edge and eps > mband: mband, aband = eps, k
        if eps > 0.25: over25 += 1
    print(f"  {m:4d}   {mall:.4f} (k={aall})            {mband:.4f} (k={aband})"
          f"   [{k_lo},{k_edge}]      {'NO' if over25 == 0 else f'YES x{over25}'}")

# spot cross-check vs the draft's closed-form implementation
from math import expm1
def g_(u):
    if abs(u) < 1e-4: return 0.5 - u / 12 + u**3 / 720 - u**5 / 30240
    return 1.0 / u - 1.0 / expm1(u)
def q_(u):
    if abs(u) < 1e-3: return 1.0 / 12 - u * u / 240 + u**4 / 6048 - u**6 / 172800
    e = expm1(u)
    return 1.0 / (u * u) - (e + 1.0) / (e * e)
def s2f(lam, m): return sum(j * j * q_(lam * j) for j in range(1, m + 1)) - m * q_(lam)
def muf(lam, m): return sum(j * g_(lam * j) for j in range(1, m + 1)) - m * g_(lam)
print("spot cross-checks direct-sum vs closed-form (rel diff):")
for (m, lam) in ((30, 0.13), (60, 4.0 / 60), (140, 0.02), (30, 1.5)):
    mu1, s21 = moments(lam, m)
    mu2, s22 = muf(lam, m), s2f(lam, m)
    print(f"   m={m} lam={lam:.4f}: mu {mu1:.9f}/{mu2:.9f} (rd {abs(mu1-mu2)/mu2:.1e}), "
          f"s2 {s21:.9f}/{s22:.9f} (rd {abs(s21-s22)/s22:.1e})")
