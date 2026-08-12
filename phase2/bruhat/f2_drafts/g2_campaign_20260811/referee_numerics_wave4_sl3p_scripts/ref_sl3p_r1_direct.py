# ref_sl3p_r1_direct.py — NUMERICS REFEREE, wave4_sl3p. Independent DIRECT
# verification of the final Theorem SL3' statement:
#   -2 log|phi_lam(t)| >= 2 gamma*(W) s2 t^2 ,  t = tau*lam, tau in (0, 0.8]
# via a THIRD computational path (closed-form |nu_j| product, NOT the E.1
# g/h-identity and NOT NC1's series summation):
#   log|phi| = sum_j [ log(1-q) - log(1-q^j)
#                      + 0.5 log((1-q^j)^2 + 4 q^j sin^2(j t/2))
#                      - 0.5 log((1-q)^2  + 4 q  sin^2(t/2)) ]
# and s2 independently from the truncated-geometric variance formula
#   Var(U_j) = q/(1-q)^2 - j^2 q^j/(1-q^j)^2   (NOT via h).
# Adversarial points: band edges (both sides, off-grid), the CL-max w~4.9,
# lam at/near the 0.30 regime split, lam = 0.89, off-grid taus incl. 0.8 exact,
# m = 401/402/1000/5000 (mpmath dps 30) and m = 200000 (numpy float64).
import numpy as np
from mpmath import mp, mpf, exp, log, sin, sqrt

mp.dps = 30

BANDS = [("W1", 4.0, 5.0, mpf("0.42")), ("W2", 5.0, 6.0, mpf("0.42")),
         ("W3", 6.0, 8.0, mpf("0.40")), ("W4", 8.0, 10.0, mpf("0.40")),
         ("W5", 10.0, 20.0, mpf("0.38")), ("W6b", 20.0, 40.0, mpf("0.34")),
         ("W7", 40.0, float("inf"), mpf("0.32"))]

def band_of(w):
    for nm, lo, hi, gs in BANDS:
        if lo < float(w) <= hi:
            return nm, gs
    raise ValueError(w)

def check_mp(m, w, tau):
    lam = mpf(w)/m; t = mpf(tau)*lam; q = exp(-lam)
    lq = log(1-q); base = mpf("0.5")*log((1-q)**2 + 4*q*sin(t/2)**2)
    qj = mpf(1); L = mpf(0); s2 = mpf(0); vq = q/(1-q)**2
    for j in range(1, m+1):
        qj *= q
        L += lq - log(1-qj) + mpf("0.5")*log((1-qj)**2 + 4*qj*sin(j*t/2)**2) - base
        s2 += vq - j*j*qj/(1-qj)**2
    lhs = -2*L
    nm, gs = band_of(w)
    rhs = 2*gs*t**2*s2
    return nm, gs, lhs, rhs, lhs - rhs, lhs/(2*t**2*s2)   # last = gamma_ach

print("== ref_sl3p_r1: direct SL3' statement check, independent path (dps=30) ==")
print("%-7s %-11s %-6s %-4s %5s | %-12s %-12s | ratio" %
      ("m", "w", "tau", "band", "g*", "slack", "gamma_ach"))
worst = None
PTS = []
W401 = ["4.000001", "4.0001", "4.05", "4.51", "4.9", "4.99999", "5.0",
        "5.00001", "6.0", "6.00001", "8.0", "8.00001", "10.0", "10.00001",
        "19.99999", "20.0", "20.00001", "40.0", "40.00001", "45.0",
        "120.0", "120.3", "120.35", "200.0", "356.89"]
TAUS = ["0.005", "0.1", "0.42", "0.55", "0.58", "0.65", "0.7275", "0.7975", "0.8"]
for w in W401:
    for tau in TAUS:
        PTS.append((401, w, tau))
for (m, w) in [(402, "4.9"), (402, "20.0"), (402, "357.78"), (1000, "20.0"),
               (1000, "890.0"), (5000, "20.0"), (5000, "4.05"), (5000, "4450.0")]:
    for tau in ["0.58", "0.8"]:
        PTS.append((m, w, tau))
nfail = 0
for (m, w, tau) in PTS:
    nm, gs, lhs, rhs, sl, gach = check_mp(m, w, tau)
    ratio = gach/gs
    if worst is None or ratio < worst[0]:
        worst = (ratio, m, w, tau, nm)
    if sl <= 0:
        nfail += 1
        print("FAIL   %-7d %-11s %-6s %-4s %s | slack=%s gamma_ach=%s" %
              (m, w, tau, nm, mp.nstr(gs, 3), mp.nstr(sl, 8), mp.nstr(gach, 8)))
print("points checked: %d   FAILs (slack<=0): %d" % (len(PTS), nfail))
print("worst gamma_ach/gamma* = %s at m=%d w=%s tau=%s (%s)" %
      (mp.nstr(worst[0], 6), worst[1], worst[2], worst[3], worst[4]))

# spot-print the headline points for cross-reference with NC1
for (m, w, tau) in [(401, "4.05", "0.8"), (401, "4.9", "0.8"), (401, "20.0", "0.8"),
                    (401, "356.89", "0.8"), (401, "120.3", "0.8")]:
    nm, gs, lhs, rhs, sl, gach = check_mp(m, w, tau)
    print("  m=%d w=%-8s tau=%s [%s]: -2log|phi| = %s  2 g* s2 t^2 = %s  "
          "slack = %s  gamma_ach = %s" %
          (m, w, tau, nm, mp.nstr(lhs, 12), mp.nstr(rhs, 8),
           mp.nstr(sl, 6), mp.nstr(gach, 6)))

# large-m float64 sweep (numpy, independent of mpmath path)
print()
print("== large-m float64 sweep (worst-band probes) ==")
def check_np(m, w, tau):
    lam = w/m; t = tau*lam
    j = np.arange(1, m+1, dtype=np.float64)
    q = np.exp(-lam); qj = np.exp(-j*lam)
    L = (np.log1p(-q) - np.log1p(-qj)
         + 0.5*np.log((1-qj)**2 + 4*qj*np.sin(j*t/2)**2)
         - 0.5*np.log((1-q)**2 + 4*q*np.sin(t/2)**2)).sum()
    s2 = (q/(1-q)**2 - j*j*qj/(1-qj)**2).sum()
    lhs = -2*L
    nm, gs = band_of(w)
    gach = lhs/(2*t*t*s2)
    return nm, float(gs), lhs - 2*float(gs)*t*t*s2, gach
for (m, w, tau) in [(200000, 20.0, 0.8), (200000, 20.0, 0.58),
                    (200000, 10.0, 0.8), (200000, 5.0, 0.8),
                    (200000, 178000.0, 0.8), (200000, 60000.0, 0.8),
                    (1000000, 20.0, 0.8)]:
    nm, gs, sl, gach = check_np(m, w, tau)
    print("  m=%d w=%-9g tau=%.2f [%s g*=%.2f]: slack=%+.4f  gamma_ach=%.6f  "
          "ratio=%.4f  %s" % (m, w, tau, nm, gs, sl, gach, gach/gs,
                              "PASS" if sl > 0 else "FAIL"))
print("== end r1 ==")
