#!/usr/bin/env python3
"""wave6b numerics referee, sol_s2_20260812.md — recipe check 6 PLUS the
adversarial band scan the recipe omits.

The draft's VERIFICATION RECIPE names the seven sup obligations but samples NO
actual (m, lam, t) points on any band. This script measures the (S2) truth
surface Q(m, lam, t) = lam^3 |R5(t)| / (s2 t^5):

  [Q1] full x = t/lam grid (0 (SOL.5.2 value), 0.02..0.50 step 0.02, + local
       refinement around the argmax) at m = 561 over all seven bands,
       including off-grid open edges (w = 4+1e-9, 5+1e-9, ..., 40+1e-9),
       exact band right edges, and the deep-tilt corner lam = 0.89.
  [Q2] m-direction: m = 1581 and m = 5000 at band edges (is the m = 561 value
       an understatement of the sup?).
  [Q3] the lam -> 0 limit surface Qbar(w, x) computed INDEPENDENTLY (per-factor
       closed form S(u, T) + quadrature), giving the m -> infinity truth at the
       W1-W6b edges; unit-tested against the finite-m engine.
  [C]  the crude-majorant constant C_abs (SOL.4.3) over the same grid: which
       C5* constants would SOL.4 alone discharge?

Verdict data: per-band max Q vs C5* = 0.05/0.06/0.08/0.10/0.15/0.25/0.80
(ledger) and vs the wave-6 scout adjustment C5*(W7) = 0.50.
"""
import time
from mpmath import mp, mpf, mpc, fabs

T0 = time.time()
def clk(): return f"[{time.time()-T0:7.1f}s]"

def A0(x): return 1/mp.expm1(x)
def A1(x): q = mp.exp(-x); return q/(1-q)**2
def A2(x): q = mp.exp(-x); return q*(1+q)/(1-q)**3
def A3(x): q = mp.exp(-x); return q*(1+4*q+q*q)/(1-q)**4
def A4(x): q = mp.exp(-x); return q*(1+11*q+11*q*q+q**3)/(1-q)**5

def core(m, lam):
    s2  = m*A1(lam) - mp.fsum(mpf(j)**2*A1(j*lam) for j in range(1, m+1))
    k3  = m*A2(lam) - mp.fsum(mpf(j)**3*A2(j*lam) for j in range(1, m+1))
    k4  = m*A3(lam) - mp.fsum(mpf(j)**4*A3(j*lam) for j in range(1, m+1))
    Lp  = -(m*A0(lam) - mp.fsum(mpf(j)*A0(j*lam) for j in range(1, m+1)))
    L5  = mp.fsum(mpf(j)**5*A4(j*lam) for j in range(1, m+1)) - m*A4(lam)
    MAJ = m*A4(lam) + mp.fsum(mpf(j)**5*A4(j*lam) for j in range(1, m+1))
    Llam = mp.fsum(mp.log(-mp.expm1(-j*lam)) for j in range(1, m+1)) \
           - m*mp.log(-mp.expm1(-lam))
    return s2, k3, k4, Lp, L5, MAJ, Llam

def Qval(m, lam, x, s2, k3, k4, Lp, L5, Llam):
    """Q(m, lam, x*lam); x = 0 -> SOL.5.2 value."""
    if x == 0:
        return lam**3*fabs(L5)/(120*s2)
    t = lam*x
    z = lam - 1j*t
    Lz = mp.fsum(mp.log(-mp.expm1(-j*z)) for j in range(1, m+1)) \
         - m*mp.log(-mp.expm1(-z))
    logphi = Lz - Llam + 1j*t*Lp
    r5 = logphi + s2*t*t/2 + 1j*k3*t**3/6 - k4*t**4/24
    return lam**3*fabs(r5)/(s2*t**5)

BANDS = [("W1", 4, 5, mpf('0.05')), ("W2", 5, 6, mpf('0.06')),
         ("W3", 6, 8, mpf('0.08')), ("W4", 8, 10, mpf('0.10')),
         ("W5", 10, 20, mpf('0.15')), ("W6b", 20, 40, mpf('0.25')),
         ("W7", 40, None, mpf('0.80'))]
C5_W7_ADJ = mpf('0.50')

def band_of(w):
    for (nm, lo, hi, c5) in BANDS:
        if hi is None:
            if w > lo: return nm, c5
        elif lo < w <= hi:
            return nm, c5
    return None, None

mp.dps = 50
XGRID = [mpf(0)] + [mpf(k)/50 for k in range(1, 26)]      # 0, 0.02..0.50

def scan_point(m, lam, xs=None):
    s2, k3, k4, Lp, L5, MAJ, Llam = core(m, lam)
    Cabs = lam**3*MAJ/(120*s2)
    xs = xs or XGRID
    vals = [(Qval(m, lam, x, s2, k3, k4, Lp, L5, Llam), x) for x in xs]
    qmax, xarg = max(vals, key=lambda p: p[0])
    # local refinement around the argmax (step 0.0025 over +-0.02)
    if xs is XGRID:
        lo = max(xarg - mpf('0.02'), mpf('0.0025'))
        hi = min(xarg + mpf('0.02'), mpf('0.5'))
        ref = []
        xx = lo
        while xx <= hi + mpf('1e-12'):
            ref.append(xx); xx += mpf('0.0025')
        vals2 = [(Qval(m, lam, x, s2, k3, k4, Lp, L5, Llam), x) for x in ref]
        q2, x2 = max(vals2, key=lambda p: p[0])
        if q2 > qmax: qmax, xarg = q2, x2
    return qmax, xarg, Cabs

# ---------------- [Q1] m = 561, all bands, dense w -------------------------
print("== [Q1] Q(m=561) band scan (x-grid 0..0.5 step 0.02 + refinement) ==")
m = 561
W_LIST = ['4.000000001', '4.2', '4.3', '4.5', '4.7', '4.9', '5',
          '5.000000001', '5.3', '5.6', '6',
          '6.000000001', '6.5', '7', '7.5', '8',
          '8.000000001', '8.5', '9', '9.5', '10',
          '10.000000001', '12', '14', '16', '18', '20',
          '20.000000001', '25', '30', '35', '40',
          '40.000000001', '45', '50', '60', '80', '100', '150', '200',
          '300', '400']
band_max = {}; band_cabs = {}
for wstr in W_LIST:
    w = mpf(wstr); lam = w/m
    nm, c5 = band_of(w)
    qmax, xarg, cabs = scan_point(m, lam)
    band_max.setdefault(nm, []).append((qmax, wstr, xarg))
    band_cabs.setdefault(nm, []).append((cabs, wstr))
    print(f"  {clk()} {nm:3s} w={wstr:13s}  maxQ={mp.nstr(qmax,6)} at x={mp.nstr(xarg,4)}   C_abs={mp.nstr(cabs,6)}")
for lamstr in ['0.3', '0.5', '0.7', '0.8', '0.85', '0.89']:
    lam = mpf(lamstr); w = m*lam
    nm, c5 = band_of(w)
    qmax, xarg, cabs = scan_point(m, lam)
    band_max.setdefault(nm, []).append((qmax, f"lam={lamstr}", xarg))
    band_cabs.setdefault(nm, []).append((cabs, f"lam={lamstr}"))
    print(f"  {clk()} {nm:3s} lam={lamstr:5s} (w={mp.nstr(w,6)})  maxQ={mp.nstr(qmax,6)} at x={mp.nstr(xarg,4)}   C_abs={mp.nstr(cabs,6)}")

print("== [Q1] per-band summary at m = 561 vs C5* ==")
for (nm, lo, hi, c5) in BANDS:
    qs = band_max.get(nm, [])
    if not qs: continue
    qb, wb, xb = max(qs, key=lambda p: p[0])
    cb, wcb = max(band_cabs[nm], key=lambda p: p[0])
    extra = f"  [scout-adjusted 0.50: {'PASS' if qb <= C5_W7_ADJ else 'FAIL'} margin {mp.nstr(C5_W7_ADJ/qb,4)}x]" if nm == "W7" else ""
    print(f"  {nm:3s}: max Q = {mp.nstr(qb,6)} at ({wb}, x={mp.nstr(xb,4)})  vs C5*={mp.nstr(c5,3)}"
          f"  -> {'PASS' if qb <= c5 else 'FAIL'} margin {mp.nstr(c5/qb,4)}x{extra}"
          f"  | max C_abs = {mp.nstr(cb,5)} at {wcb} ({'covers C5*' if cb <= c5 else 'crude bound does NOT cover'})")

# ---------------- [Q2] m-direction at band edges ---------------------------
print("== [Q2] m-direction: same w, larger m ==")
XS_COARSE = [mpf(0), mpf('0.1'), mpf('0.2'), mpf('0.3'), mpf('0.4'), mpf('0.45'), mpf('0.5')]
for mm in (1581, 5000):
    for wstr in ['5', '6', '8', '10', '20', '40', '41']:
        w = mpf(wstr); lam = w/mm
        nm, c5 = band_of(w)
        qmax, xarg, cabs = scan_point(mm, lam, xs=XS_COARSE)
        print(f"  {clk()} m={mm} {nm:3s} w={wstr:4s}  maxQ(coarse)={mp.nstr(qmax,6)} at x={mp.nstr(xarg,4)}  C_abs={mp.nstr(cabs,6)}")
# deep corner geometric limit approach
for mm in (561, 1581, 5000, 20000):
    lam = mpf('0.89')
    s2, k3, k4, Lp, L5, MAJ, Llam = core(mm, lam)
    q0 = lam**3*fabs(L5)/(120*s2)
    print(f"  {clk()} m={mm:6d} lam=0.89: Q(t->0) = {mp.nstr(q0,8)}  (geometric-limit approach)")

# ---------------- [Q3] the lam -> 0 limit surface Qbar(w, x) ---------------
print("== [Q3] independent lam->0 limit Qbar(w, x) (closed-form S + quadrature) ==")
mp.dps = 40

def Rinf(x):
    return -mp.log(1 - 1j*x) - mp.fsum((1j*x)**n/n for n in range(1, 5))

def S_closed(u, T):
    """S(u,T) = sum_r (1/r) e^{-ru} E4(irT) in closed form."""
    return (-mp.log(-mp.expm1(-u + 1j*T)) + mp.log(-mp.expm1(-u))
            - 1j*T*A0(u) + T*T/2*A1(u) + 1j*T**3/6*A2(u) - T**4/24*A3(u))

# unit test S_closed vs direct r-sum
u0, T0u = mpf('0.9'), mpf('0.31')
direct = mp.fsum(mp.exp(-r*u0)*(mp.exp(1j*r*T0u) - mp.fsum((1j*r*T0u)**n/mp.factorial(n) for n in range(5)))/r
                 for r in range(1, 300))
print(f"  unit test S_closed: |closed - direct r-sum| = {mp.nstr(fabs(S_closed(u0, T0u) - direct), 3)}")

def Qbar(w, x):
    g2 = mp.quad(lambda u: 1 - u*u*A1(u), [mpf('1e-30'), w])
    if x == 0:
        h5 = mp.quad(lambda u: 24 - u**5*A4(u), [mpf('1e-30'), w])
        return fabs(h5)/(120*g2)
    N = w*Rinf(x) - mp.quad(lambda u: S_closed(u, u*x), [mpf('1e-30'), w])
    return fabs(N)/(g2*x**5)

for w in [5, 6, 8, 10, 20, 40]:
    row = []
    for x in [mpf(0), mpf('0.25'), mpf('0.5')]:
        row.append((x, Qbar(mpf(w), x)))
    nm, c5 = band_of(mpf(w))
    txt = "  ".join(f"x={mp.nstr(x,3)}: {mp.nstr(q,6)}" for x, q in row)
    print(f"  {clk()} Qbar(w={w:3d}) [{nm} right edge]:  {txt}   (C5* = {mp.nstr(c5,3)})")

print(f"{clk()} == QSCAN DONE ==")
