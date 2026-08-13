#!/usr/bin/env python3
# wave6b_ref_s1 / ref4_envelope_vs_Dn.py
# Direct falsification test of the middle link of the draft's chain: the envelope
# formulas (15)-(22) versus the ACTUAL finite-m quantities D_n = lam^{n+1} kappa_n.
#   check 1: L2(w,lam) <= D2,  D3 <= U3(w,lam),  D4 <= U4(w,lam)  pointwise
#            (lam = w/m a point, NOT an interval -- so this tests the formulas
#            themselves, not the certificate's interval slack), at an adversarial
#            (m, w) grid including off-grid w and the plan's worst corners.
#   check 2: the trapezoid identity (15): eps_n := D_n - [G_n + w(h_n(lam)-h_n(0))
#            - (lam/2)(h_n(w)-h_n(0))] satisfies |eps_n| <= w lam^2 M_n / 12 with
#            the draft's M_n = (1, 4, 20)  AND with ref2's measured sups
#            (0.1686, 0.1845, 0.5301) -- the latter is ~5x tighter, so passing it
#            confirms the error model, not just the inequality.
from mpmath import mp, mpf, exp, sinh, cosh, zeta, fabs

mp.dps = 50

def g2(x): q = exp(-x); return q/(1-q)**2
def g3(x): q = exp(-x); return q*(1+q)/(1-q)**3
def g4(x): q = exp(-x); return q*(1+4*q+q*q)/(1-q)**4
def h2(x): return (x/(2*sinh(x/2)))**2
def h3(x): return x**3*cosh(x/2)/(4*sinh(x/2)**3)
def h4(x): return x**4*(cosh(x)+2)/(8*sinh(x/2)**4)
H = {2: h2, 3: h3, 4: h4}
H0 = {2: mpf(1), 3: mpf(2), 4: mpf(6)}
Z2 = zeta(2)

def En(n, x):
    s = mpf(1); t = mpf(1)
    for k in range(1, n+1):
        t = t*x/k; s += t
    return s

def G(n, w):
    fac_nm1 = [None, 1, 1, 2, 6][n+0] if False else {2: 1, 3: 2, 4: 6}[n]
    fac_n = {2: 2, 3: 6, 4: 24}[n]
    s = mpf(0); nu = 1
    while True:
        x = nu*w
        t = exp(-x)*En(n, x)/nu**2
        s += t
        nu += 1
        if t < mpf('1e-45') and nu > 4:
            break
    return fac_nm1*w - fac_n*Z2 + fac_n*s

def Dn(m, lam, n):
    hf = H[n]
    w = m*lam
    return w*hf(lam) - lam*sum(hf(j*lam) for j in range(1, m+1))

M_draft = {2: mpf(1), 3: mpf(4), 4: mpf(20)}
M_meas = {2: mpf('0.1686'), 3: mpf('0.1845'), 4: mpf('0.5301')}

ms = [561, 562, 563, 600, 701, 1000, 2500, 10000]
ws = ["4.001", "4.5", "5", "5.7", "6", "7.3", "8", "9.9", "10", "15.5", "20", "33.7", "40"]
ok_env = True; ok_eps_draft = True; ok_eps_meas = True
worst_gap = (mpf('inf'), None)   # min over probes of (U3 - D3), etc. tracked coarsely
worst_eps_ratio = mpf(0); worst_eps_arg = None
for wsstr in ws:
    w = mpf(wsstr)
    for m in ms:
        lam = w/m
        row = {}
        for n in (2, 3, 4):
            D = Dn(m, lam, n)
            base = G(n, w) + w*(H[n](lam) - H0[n]) - (lam/2)*(H[n](w) - H0[n])
            eps = D - base
            cap_d = w*lam**2*M_draft[n]/12
            cap_m = w*lam**2*M_meas[n]/12
            if fabs(eps) > cap_d: ok_eps_draft = False; print(f"  ** eps_{n} EXCEEDS draft cap at (m={m}, w={wsstr})")
            if fabs(eps) > cap_m: ok_eps_meas = False; print(f"  ** eps_{n} exceeds measured-M cap at (m={m}, w={wsstr})")
            r = fabs(eps)/cap_d
            if r > worst_eps_ratio: worst_eps_ratio, worst_eps_arg = r, (m, wsstr, n)
            row[n] = (D, base, eps)
        L2v = row[2][1] - w*lam**2*M_draft[2]/12
        U3v = row[3][1] + w*lam**2*M_draft[3]/12
        U4v = row[4][1] + w*lam**2*M_draft[4]/12
        if not (L2v <= row[2][0] and row[3][0] <= U3v and row[4][0] <= U4v):
            ok_env = False
            print(f"  ** ENVELOPE VIOLATION at (m={m}, w={wsstr}): "
                  f"L2-D2={mp.nstr(L2v-row[2][0],6)} D3-U3={mp.nstr(row[3][0]-U3v,6)} D4-U4={mp.nstr(row[4][0]-U4v,6)}")
print(f"probes: {len(ws)*len(ms)} (m,w) pairs x 3 cumulant orders")
print(f"check 1 -- pointwise L2 <= D2, D3 <= U3, D4 <= U4 at ALL probes: {ok_env}")
print(f"check 2 -- |eps_n| <= w lam^2 M_n/12 with draft M=(1,4,20) at ALL probes: {ok_eps_draft}")
print(f"          with ref2 measured M=(0.1686,0.1845,0.5301) at ALL probes: {ok_eps_meas}")
print(f"worst |eps|/draft-cap ratio: {mp.nstr(worst_eps_ratio, 6)} at (m,w,n)={worst_eps_arg}")

# spot print at the two binding corners for the record
for (m, wsstr) in [(561, "5"), (561, "40")]:
    w = mpf(wsstr); lam = w/m
    D2, D3, D4 = Dn(m, lam, 2), Dn(m, lam, 3), Dn(m, lam, 4)
    print(f"\ncorner (m={m}, w={wsstr}):  D3/D2 = {mp.nstr(D3/D2, 8)},  D4/D2 = {mp.nstr(D4/D2, 8)}")
    print(f"  r31 sentinel agreement: D3/D2 vs lam*k3/k2 -- both are the same object per (6)")
