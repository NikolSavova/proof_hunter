#!/usr/bin/env python3
"""NC-PL2: core-model remainder + tail feasibility on the residual band.
(a) C5 := max |log phi_c + s2t^2/2 + i k3 t^3/6 - k4 t^4/24| / (s2|t|^5/lam^3)
    over |t| <= 0.45 lam  (SL1(c) target: C5 <= 3).
(b) min over [0.45lam, 0.7lam] of -log|phi| / (s2 t^2)  (SL3(i) target: >= 1/8).
(c) W.6 exponent at t = 0.7lam (target >= 4 at m=401) + bound-side tail integral
    over [0.45lam, pi] in u-units: bucket_u = integral * sqrt(s2/2pi) * A.
"""
import mpmath as mp
mp.mp.dps = 30

def factor_stats(j, lam):
    q = mp.e**(-lam)
    ws = [q**i for i in range(j)]
    Z = mp.fsum(ws)
    m1 = mp.fsum([i*w for i, w in enumerate(ws)])/Z
    c2 = mp.fsum([(i-m1)**2*w for i, w in enumerate(ws)])/Z
    c3 = mp.fsum([(i-m1)**3*w for i, w in enumerate(ws)])/Z
    c4 = mp.fsum([(i-m1)**4*w for i, w in enumerate(ws)])/Z - 3*c2**2
    return m1, c2, c3, c4

def phi_centered_log(m, lam, t, stats):
    # sum_j [log(nu_j(t) e^{-it mu_j})], principal branch per centered factor
    tot = mp.mpc(0)
    z = mp.mpc(0, t) - lam
    for j in range(1, m+1):
        mu = stats[j][0]
        if j == 1:
            continue
        num = (1 - mp.e**(z*j))/(1 - mp.e**z)
        q = mp.e**(-lam)
        Z = (1 - q**j)/(1 - q)
        tot += mp.log(num/Z * mp.e**(mp.mpc(0, -t*mu)))
    return tot

def w6_exponent(m, lam, t):
    M = m*mp.sin(t/2)
    s = mp.sin(t/2)**2
    S = mp.sinh(lam/2)**2
    if M <= 1:
        return mp.mpf(0)
    return m*((M-1)/(2*M))*(mp.log(1+s/S) - s/(S*M))

m = 401
print("m=401.  w | C5(0.45lam) | min -log|phi|/(s2 t^2) on [.45,.7]lam | W6@0.7lam | tail_u")
for w in ['4.2', '7', '20', '150', '356']:
    lam = mp.mpf(w)/m
    stats = {j: factor_stats(j, lam) for j in range(1, m+1)}
    s2 = mp.fsum([stats[j][1] for j in stats])
    k3 = mp.fsum([stats[j][2] for j in stats])
    k4 = mp.fsum([stats[j][3] for j in stats])
    A = lam**2*s2
    # (a) C5
    C5 = mp.mpf(0)
    for i in range(1, 13):
        t = mp.mpf('0.45')*lam*i/12
        L = phi_centered_log(m, lam, t, stats)
        resid = abs(L + s2*t**2/2 + mp.mpc(0, 1)*k3*t**3/6 - k4*t**4/24)
        C5 = max(C5, resid/(s2*t**5/lam**3))
    # (b) mid-range domination ratio
    ratio_min = mp.mpf(100)
    for i in range(7):
        t = lam*(mp.mpf('0.45') + mp.mpf('0.25')*i/6)
        L = phi_centered_log(m, lam, t, stats)
        ratio_min = min(ratio_min, -mp.re(L)/(s2*t**2))
    # (c) W6 exponent at 0.7lam and bound-side tail integral in u-units
    t0 = 2*mp.asin(mp.sinh(lam/2)) if mp.sinh(lam/2) <= 1 else mp.pi
    w6e = w6_exponent(m, lam, mp.mpf('0.7')*lam)
    # tail bound integral: [0.45,0.7]lam with exp(-s2 t^2/8);
    # [0.7lam, t0] with exp(-W6); [t0, pi] with pi*exp(-0.0373 m)
    I1 = mp.quad(lambda t: mp.e**(-s2*t**2/8), [mp.mpf('0.45')*lam, mp.mpf('0.7')*lam])
    I2 = mp.quad(lambda t: mp.e**(-w6_exponent(m, lam, t)), [mp.mpf('0.7')*lam, t0]) if t0 > mp.mpf('0.7')*lam else mp.mpf(0)
    I3 = (mp.pi - t0)*mp.e**(-mp.mpf('0.0373')*m)
    tail_u = (I1 + I2 + I3)*mp.sqrt(s2/(2*mp.pi))*A
    print(f"w={w:>5}: C5={float(C5):8.4f}  midmin={float(ratio_min):7.4f}  "
          f"W6(0.7lam)={float(w6e):8.3f}  tail_u={float(tail_u):9.5f} "
          f"(I1u={float(I1*mp.sqrt(s2/(2*mp.pi))*A):.4f}, I2u={float(I2*mp.sqrt(s2/(2*mp.pi))*A):.4f})")
print("note: tail_u is the tail bucket in u=1/A units; ledger target: total <= 20*c_A(w).")
