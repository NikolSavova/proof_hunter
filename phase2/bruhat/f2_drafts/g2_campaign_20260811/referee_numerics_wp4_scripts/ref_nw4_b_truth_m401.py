#!/usr/bin/env python3
"""REF-B: exact ground truth of CL(79, 20, 0.89) at m = 401 (the spec's own
threshold — no wp4 file computed it; NC-PL3 stopped at m = 200) and at
m = 402 (corner sample).  Also per-k truth of the delivered inputs:
Theorem A2(ii) floor A >= c_A(W) m, Lemma C.1 cap A <= m, s2 > m,
s2 >= 141.7497, at the ACTUAL mean-matched (k, m) pairs.

Method: exact Mahonian coefficients P[k] (prefix-sum DP, Python ints);
r(k)-1 exact from big ints, converted at mpmath dps 50; lam(k) by float
bisection on mu(lam) = k refined by 4 mpmath-Newton steps (dps 30);
s2 by the closed form Var(U_j) = q/(1-q)^2 - j^2 q^j/(1-q^j)^2.
Adversarial k-selection: both band edges of every w-band, the w -> 4+
corner (last 45 interior k), the lam -> 0.89 deep corner (first 30 k),
plus a stride sweep.  eps := |s2 (r-1) - 1|;  CL truth: eps*min(m,s2) <= 20.
"""
import mpmath as mp
mp.mp.dps = 30

def mahonian(m):
    P = [1]
    for j in range(2, m + 1):
        Q = [0] * (len(P) + j - 1)
        run = 0
        for i in range(len(Q)):
            if i < len(P):
                run += P[i]
            if i - j >= 0:
                run -= P[i - j]
            Q[i] = run
        P = Q
    return P

def mu_s2(m, lam):
    el = mp.e ** (-lam)
    mu = mp.mpf(0); s2 = mp.mpf(0)
    g1 = el / (1 - el); g2 = el / (1 - el) ** 2
    for j in range(1, m + 1):
        elj = mp.e ** (-lam * j)
        mu += g1 - j * elj / (1 - elj)
        s2 += g2 - j * j * elj / (1 - elj) ** 2
    return mu, s2

import math
def mu_float(m, lam):
    el = math.exp(-lam)
    g1 = el / (1 - el)
    s = 0.0
    for j in range(1, m + 1):
        elj = math.exp(-lam * j)
        s += g1 - j * elj / (1 - elj)
    return s

def lam_of_k(m, k):
    lo, hi = 1e-9, 5.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if mu_float(m, mid) > k:
            lo = mid
        else:
            hi = mid
    lam = mp.mpf(0.5 * (lo + hi))
    for _ in range(4):  # Newton refine: d mu/d lam = -s2
        mu, s2 = mu_s2(m, lam)
        lam = lam + (mu - k) / s2
    return lam

C_A = [(4, 5, mp.mpf('0.28')), (5, 6, mp.mpf('0.35')), (6, 8, mp.mpf('0.42')),
       (8, 10, mp.mpf('0.52')), (10, 20, mp.mpf('0.60')), (20, 40, mp.mpf('0.70')),
       (40, mp.inf, mp.mpf('0.80'))]
def band_cA(w):
    for lo, hi, c in C_A:
        if lo < w <= hi:
            return c
    return None

def run(m, full=True):
    print(f"===== m = {m} =====")
    P = mahonian(m)
    N = m * (m - 1) // 2
    # k-range of the residual band
    mu089 = mu_float(m, 0.89)
    mu4m = mu_float(m, 4.0 / m)
    k_min = math.ceil(mu089)
    k_max = math.ceil(mu4m) - 1
    print(f"  N = {N}; band k-range: [{k_min}, {k_max}]  (mu(0.89) = {mu089:.2f}, mu(4/m) = {mu4m:.2f})")
    ks = set()
    ks.update(range(k_min, k_min + (30 if full else 10)))          # deep corner lam ~ 0.89
    ks.update(range(k_max - (45 if full else 12), k_max + 1))      # w -> 4+ corner
    for w0 in (5, 6, 8, 10, 20, 40, 4.5, 4.78, 4.84, 4.2, 4.05):  # band edges + NC-PL3 max locus
        kk = math.floor(mu_float(m, w0 / m))
        ks.update([kk - 1, kk, kk + 1, kk + 2])
    if full:
        ks.update(range(k_min, k_max, max(1, (k_max - k_min) // 140)))
    ks = sorted(k for k in ks if k_min <= k <= k_max and 2 <= k <= N // 2)
    print(f"  testing {len(ks)} adversarial k values")
    worst = (mp.mpf(0), None)
    viol = {"CL>20": 0, "A<cA*m": 0, "A>m": 0, "s2<=m": 0, "s2<141.7497": 0, "r<1": 0, "bandless": 0}
    minAm_margin = (mp.inf, None)   # min of A/m - c_A
    maxA_m = (mp.mpf(0), None)      # max of A/m
    mins2m = (mp.inf, None)         # min of s2/m
    with mp.workdps(50):
        for k in ks:
            lam = lam_of_k(m, k)
            w = m * lam
            if not (w > 4 and lam <= mp.mpf('0.89') + mp.mpf('1e-12')):
                continue
            mu, s2 = mu_s2(m, lam)
            A = lam * lam * s2
            num = P[k] * P[k] - P[k - 1] * P[k + 1]
            den = P[k - 1] * P[k + 1]
            rm1 = mp.mpf(num) / mp.mpf(den)
            if rm1 < 0:
                viol["r<1"] += 1
            eps = abs(s2 * rm1 - 1)
            val = eps * min(mp.mpf(m), s2)
            if val > worst[0]:
                worst = (val, (k, float(w), float(s2), float(A)))
            cA = band_cA(w)
            if cA is None:
                viol["bandless"] += 1; continue
            if val > 20: viol["CL>20"] += 1
            if A < cA * m: viol["A<cA*m"] += 1
            if A > m: viol["A>m"] += 1
            if s2 <= m: viol["s2<=m"] += 1
            if s2 < mp.mpf('141.7497'): viol["s2<141.7497"] += 1
            if A / m - cA < minAm_margin[0]: minAm_margin = (A / m - cA, (k, float(w)))
            if A / m > maxA_m[0]: maxA_m = (A / m, (k, float(w)))
            if s2 / m < mins2m[0]: mins2m = (s2 / m, (k, float(w)))
    print(f"  violations: {viol}")
    print(f"  max eps*min(m,s2) = {mp.nstr(worst[0], 6)} at k={worst[1][0]} "
          f"(w={worst[1][1]:.3f}, s2={worst[1][2]:.1f}, A={worst[1][3]:.2f})   [CL asks <= 20]")
    print(f"  min (A/m - c_A(band)) = {mp.nstr(minAm_margin[0], 5)} at k={minAm_margin[1][0]} (w={minAm_margin[1][1]:.3f})")
    print(f"  max A/m = {mp.nstr(maxA_m[0], 6)} at (w={maxA_m[1][1]:.3f});  min s2/m = {mp.nstr(mins2m[0], 6)} at (w={mins2m[1][1]:.3f})")

run(401, full=True)
run(402, full=False)
