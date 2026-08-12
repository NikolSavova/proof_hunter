#!/usr/bin/env python3
"""NC-PL3: exact-integer truth check of the CL form on the deep-tilt band.
I_m(k) exact (DP over truncated-uniform convolutions, Python ints);
lam(k) by bisection on mu(lam)=k (mpmath); s2 = sigma_lam^2 exact formula.
Reports max over sampled band k (w=m*lam(k)>4, k<=N/2) of
  eps*min(m,s2), eps := |s2*(r(k)-1) - 1|   (CL asks <= C* = 20).
"""
import mpmath as mp
mp.mp.dps = 30

def mahonian(m):
    P = [1]
    for j in range(2, m+1):
        # multiply by (1 + x + ... + x^{j-1}) via prefix sums
        Q = [0]*(len(P) + j - 1)
        run = 0
        for i in range(len(Q)):
            run += P[i] if i < len(P) else 0
            if i - j >= 0:
                run -= P[i - j]
            Q[i] = run
        P = Q
    return P

def mu_s2(m, lam):
    mu = mp.mpf(0); s2 = mp.mpf(0)
    for j in range(1, m+1):
        x = lam*j
        # mean/var of truncated geometric via closed forms
        el = mp.e**(-lam); elj = mp.e**(-x)
        mu_j = el/(1-el) - j*elj/(1-elj)
        v_j = el/(1-el)**2 - j**2*elj/(1-elj)**2
        mu += mu_j; s2 += v_j
    return mu, s2

def lam_of_k(m, k):
    lo, hi = mp.mpf('1e-9'), mp.mpf('5')
    for _ in range(80):
        mid = (lo+hi)/2
        if mu_s2(m, mid)[0] > k:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2

for m in [120, 200]:
    P = mahonian(m)
    N = m*(m-1)//2
    worst = (0, None)
    ks = sorted(set(list(range(2, N//2, max(1, N//80))) + [N//2 - 1]))
    for k in ks:
        lam = lam_of_k(m, k)
        w = m*lam
        if w <= 4 or lam > mp.mpf('0.89'):
            continue
        r = mp.mpf(P[k])**2/(mp.mpf(P[k-1])*mp.mpf(P[k+1]))
        _, s2 = mu_s2(m, lam)
        eps = abs(s2*(r-1) - 1)
        val = eps*min(mp.mpf(m), s2)
        if val > worst[0]:
            worst = (val, (k, float(w), float(s2)))
    print(f"m={m}: max over band of eps*min(m,s2) = {float(worst[0]):.4f} "
          f"at k={worst[1][0]} (w={worst[1][1]:.2f}, s2={worst[1][2]:.1f})  [CL asks <= 20]")
