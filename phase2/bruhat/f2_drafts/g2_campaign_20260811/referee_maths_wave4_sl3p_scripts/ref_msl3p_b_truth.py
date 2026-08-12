# ref_msl3p_b_truth.py — MATHS referee, wave4_sl3p: adversarial TRUTH attack.
# Computes |phi_lam(t)| by DIRECT termwise summation of every factor's finite
# series (numpy complex128; O(m^2)) — no use of the E.1 g-identity — and s2 by
# direct probability-mass summation (no closed form). Attacks Theorem SL3'
# |phi| <= exp(-gamma*(W) s2 t^2) at band edges, off-grid tau (incl. the
# analytic/cell crossovers tau_start), the w->4+ and lam->0.89 corners, and
# m in {401, 402, 1000}. Also: direct check of Lemma E.4a's display at two
# operating points (quad for the integral), and mpmath dps-25 spot cross-check
# of -2log|phi| against route NC1's archived probe value at (401, 4.05, 0.8).
# Output: out_ref_msl3p_b.txt. 2026-08-12.
import numpy as np
import mpmath as mp

def phi_s2_direct(m, lam):
    """returns (list of factor moduli callables data, s2) via direct sums."""
    j = np.arange(1, m+1)
    s2 = 0.0
    for jj in j:
        i = np.arange(jj, dtype=float)
        wgt = np.exp(-lam*i); wgt /= wgt.sum()
        mu = (wgt*i).sum()
        s2 += (wgt*(i-mu)**2).sum()
    return s2

def absphi(m, lam, t):
    tot = 0.0
    for jj in range(1, m+1):
        i = np.arange(jj, dtype=float)
        wgt = np.exp(-lam*i); wgt /= wgt.sum()
        z = (wgt*np.exp(1j*t*i)).sum()
        tot += np.log(np.abs(z))
    return tot   # log|phi|

def band_of(w):
    for name, a, b, g in [("W1",4,5,0.42),("W2",5,6,0.42),("W3",6,8,0.40),
                          ("W4",8,10,0.40),("W5",10,20,0.38),("W6b",20,40,0.34)]:
        if a < w <= b: return name, g
    return "W7", 0.32

print("=== referee maths wave4_sl3p, script B: direct truth attack ===")
print("m      w         lam       band  g*    tau     -2log|phi|   2g*s2t^2    margin      ratio   OK")
worst = 9e9; wloc = None
CASES = []
for m, ws in [(401, [4.0001, 4.05, 4.9, 5.0, 5.0001, 6.0, 8.0, 10.0, 20.0,
                     40.0, 40.0001, 120.3, 200.0, 356.89]),
              (402, [4.0001, 4.85]),
              (1000, [20.0, 890.0])]:
    for w in ws:
        lam = w/m
        if lam > 0.89: continue
        s2 = phi_s2_direct(m, lam)
        name, g = band_of(w)
        for tau in [0.05, 0.2, 0.415, 0.4175, 0.5, 0.58, 0.7275, 0.7975, 0.8]:
            t = tau*lam
            L = -2*absphi(m, lam, t)
            R = 2*g*s2*t*t
            marg = L - R
            ratio = L/R
            ok = marg >= 0
            if ratio < worst: worst, wloc = ratio, (m, w, tau)
            if not ok or tau in (0.8, 0.415):
                print(f"{m:<6d} {w:<9.4f} {lam:<9.6f} {name:4s} {g:.2f}  {tau:<6.4f}  {L:<11.5f}  {R:<11.5f} {marg:<+11.5f} {ratio:6.4f}  {'PASS' if ok else 'FAIL'}")
            CASES.append(ok)
print(f"all {len(CASES)} (m,w,tau) checks PASS: {all(CASES)}")
print(f"worst ratio -2log|phi| / 2 gamma* s2 t^2 = {worst:.4f} at (m,w,tau)={wloc}")

# mpmath dps-25 spot: -2log|phi| at (401, 4.05, tau=0.8) vs NC1 probe 76.8524292638
mp.mp.dps = 25
m, w, tau = 401, mp.mpf('4.05'), mp.mpf('0.8')
lam = w/m; t = tau*lam
tot = mp.mpf(0)
for jj in range(1, m+1):
    z = mp.mpf(0)*1j
    s = mp.mpf(0)
    for i in range(jj):
        wt = mp.e**(-lam*i)
        z += wt*(mp.cos(t*i) + 1j*mp.sin(t*i))
        s += wt
    tot += mp.log(abs(z/s))
print(f"[mp] -2log|phi|(401, w=4.05, tau=0.8) = {mp.nstr(-2*tot, 12)}   (NC1 archived: 76.8524292638)")

# --- Lemma E.4a direct check at two operating points ---
mp.mp.dps = 20
pi = mp.pi
def h(x):
    x = mp.mpf(x)
    return (x/2)**2/mp.sinh(x/2)**2 if x != 0 else mp.mpf(1)
def psi(x, tau):
    x = mp.mpf(x); tau = mp.mpf(tau)
    return mp.sin(tau*x/2)**2/mp.sinh(x/2)**2 if x != 0 else tau**2
def F(x, tau, gam):
    return mp.log(1+psi(x, tau)) - 2*gam*tau**2*h(x)
for (m, lam_s, gam_s) in [(401, '0.3', '0.32'), (401, str(5/401), '0.42'), (500, '0.1', '0.38')]:
    lam = mp.mpf(lam_s); gam = mp.mpf(gam_s); tau = mp.mpf('0.8')
    w = m*lam
    S = sum(F(jj*lam, tau, gam) for jj in range(1, m+1))
    X = float(pi/tau); pts = [0]; z = 2*X
    while z < w: pts.append(z); z += 2*X
    pts.append(float(w))
    I = sum(mp.quad(lambda x: F(x, tau, gam), [a, b]) for a, b in zip(pts[:-1], pts[1:]))
    rhs = I/lam + 2*gam*tau**2 + m*mp.mpf('1.03')*mp.e**(-2*pi/tau)
    print(f"[E.4a] m={m} lam={lam_s} gam={gam_s}: sum F(j lam) = {mp.nstr(S,8)} <= (1/lam)IntF + 2g t^2 + m eps = {mp.nstr(rhs,8)}: {S <= rhs}")
print("=== end script B ===")
