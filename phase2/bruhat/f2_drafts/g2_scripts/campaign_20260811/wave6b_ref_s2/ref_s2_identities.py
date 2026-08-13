#!/usr/bin/env python3
"""wave6b numerics referee, sol_s2_20260812.md — recipe checks 1-5 (identities).

Independently re-implements every formula of SOL.1-SOL.5 from scratch (no code
reuse from the draft, which shipped none) and checks:

  [1] A_1/A_4 closed forms vs direct r-sums with certified geometric tails
      (dps 80; recipe expects agreement < 1e-70).
  [2] s2 closed form (SOL.2.1) vs direct per-factor variances of the truncated
      geometrics; also kappa3/kappa4 closed forms vs direct central moments.
  [3] R5 direct-log form vs SOL.3.1 series form, with a CERTIFIED tail bound
      (|E4(iy)| <= 2 + |y| + y^2/2 + |y|^3/6 + y^4/24 and the geometric-tail
      closed bound sum_{r>R} r^k e^{-ar} <= (R+1)^k e^{-a(R+1)} / (1-e^{-a/2})
      valid for R+1 >= 2k/a, k <= 3).
  [4] majorant |R5| <= B5 = (t^5/120)(m A4(lam) + sum j^5 A4(j lam))  (SOL.4.1)
      and Q <= C_abs (SOL.4.2/4.3).
  [5] SOL.5.2 continuity: Q(t -> 0) -> lam^3 |L5|/(120 s2).

Adversarial points: band edges w = 4+1e-9 / 5 / 40+1e-9, the operative m = 561,
the deep corner lam = 0.89, and the open lam edge lam = (4/m)(1+1e-12).
"""
import time
from mpmath import mp, mpf, mpc, fabs, sqrt

T0 = time.time()

def clk():
    return f"[{time.time()-T0:7.1f}s]"

# ---------- closed-form A_p (Eulerian numerators), independent derivation ----
def A0(x):  # sum e^{-rx} = 1/(e^x - 1)
    return 1/mp.expm1(x)

def A1(x):
    q = mp.exp(-x); return q/(1-q)**2

def A2(x):
    q = mp.exp(-x); return q*(1+q)/(1-q)**3

def A3(x):
    q = mp.exp(-x); return q*(1+4*q+q*q)/(1-q)**4

def A4(x):
    q = mp.exp(-x); return q*(1+11*q+11*q*q+q**3)/(1-q)**5

# ---------- CHECK 1: A1/A4 closed forms vs direct sums, dps 80 --------------
print("== CHECK 1: A_1/A_4 closed forms vs direct r-sums (dps 80) ==")
mp.dps = 80
for x in [mpf('0.007130124'), mpf('0.05'), mpf('0.89'), mpf('2.67'), mpf('7')]:
    # direct sums truncated at R with certified tail (r^4 e^{-rx} tail bound)
    R = int(mp.ceil(200/x)) + 50
    s1d = mp.fsum(r*mp.exp(-r*x) for r in range(1, R+1))
    s4d = mp.fsum(mpf(r)**4*mp.exp(-r*x) for r in range(1, R+1))
    # tail bound: (R+1)^k e^{-x(R+1)} / (1 - e^{-x/2})  for k = 1, 4
    tb1 = (mpf(R+1))**1*mp.exp(-x*(R+1))/(1-mp.exp(-x/2))
    tb4 = (mpf(R+1))**4*mp.exp(-x*(R+1))/(1-mp.exp(-x/2))
    d1 = fabs(s1d - A1(x))/A1(x)
    d4 = fabs(s4d - A4(x))/A4(x)
    ok = d1 < mpf('1e-70') + tb1/A1(x) and d4 < mpf('1e-70') + tb4/A4(x)
    print(f"  x={float(x):12.9f}  relerr A1={mp.nstr(d1,3)}  A4={mp.nstr(d4,3)}"
          f"  tails=({mp.nstr(tb1,2)},{mp.nstr(tb4,2)})  PASS={ok}")

# ---------- core quantities at working precision ----------------------------
def core(m, lam):
    """s2, kappa3, kappa4, L'(lam), L5 = L^{(5)}(lam), and majorant sum."""
    s2  = m*A1(lam) - mp.fsum(mpf(j)**2*A1(j*lam) for j in range(1, m+1))
    k3  = m*A2(lam) - mp.fsum(mpf(j)**3*A2(j*lam) for j in range(1, m+1))
    k4  = m*A3(lam) - mp.fsum(mpf(j)**4*A3(j*lam) for j in range(1, m+1))
    Lp  = -(m*A0(lam) - mp.fsum(mpf(j)*A0(j*lam) for j in range(1, m+1)))
    L5  = mp.fsum(mpf(j)**5*A4(j*lam) for j in range(1, m+1)) - m*A4(lam)
    MAJ = m*A4(lam) + mp.fsum(mpf(j)**5*A4(j*lam) for j in range(1, m+1))
    return s2, k3, k4, Lp, L5, MAJ

def Lfun(m, z):
    """L_m(z) = sum_j log(1-e^{-jz}) - m log(1-e^{-z}), analytic branch, Re z > 0."""
    tot = mpc(0)
    for j in range(1, m+1):
        tot += mp.log(-mp.expm1(-j*z))
    return tot - m*mp.log(-mp.expm1(-z))

def R5_direct(m, lam, t, s2, k3, k4, Lp):
    logphi = Lfun(m, lam - 1j*t) - Lfun(m, lam) + 1j*t*Lp
    return logphi + s2*t*t/2 + 1j*k3*t**3/6 - k4*t**4/24

def E4(u):
    return mp.exp(u) - (1 + u + u*u/2 + u**3/6 + u**4/24)

def S_series(a, T, cut):
    """sum_{r=1..R} (1/r) e^{-ra} E4(irT), R = ceil(cut/a); returns (val, tail).

    tail: |E4(iy)| <= 2 + |y| + y^2/2 + |y|^3/6 + y^4/24, y = rT, gives per-term
    e^{-ra}(2/r + T + r T^2/2 + r^2 T^3/6 + r^3 T^4/24); with
    sum_{r>R} r^k e^{-ar} <= (R+1)^k e^{-a(R+1)}/(1-e^{-a/2}) for R+1 >= 2k/a.
    """
    R = max(int(mp.ceil(cut/a)), int(mp.ceil(8/a)) + 1)
    val = mpc(0)
    for r in range(1, R+1):
        val += mp.exp(-r*a)*E4(1j*r*T)/r
    g = mp.exp(-a*(R+1))/(1-mp.exp(-a/2))
    tail = g*(2 + T*(R+1) + T*T*(R+1)**2/2 + T**3*(R+1)**3/6 + T**4*(R+1)**4/24)
    return val, tail

def R5_series(m, lam, t, cut=95):
    v0, tl0 = S_series(lam, t, cut)
    val = m*v0
    tail = m*tl0
    for j in range(1, m+1):
        vj, tlj = S_series(j*lam, j*t, cut)
        val -= vj
        tail += tlj
    return val, tail

# ---------- CHECK 2: variance/cumulants vs direct factor moments ------------
print("== CHECK 2: s2/kappa3/kappa4 closed forms vs direct factor moments ==")
mp.dps = 40
for (m, lam_expr, tag) in [(561, mpf(43)/mpf(10)/561, "w=4.3"),
                           (561, mpf('0.89'),          "lam=0.89")]:
    lam = mpf(lam_expr)
    s2, k3, k4, Lp, L5, MAJ = core(m, lam)
    S2d = mpf(0); K3d = mpf(0); K4d = mpf(0); MUd = mpf(0)
    for j in range(1, m+1):
        ws = [mp.exp(-lam*a) for a in range(j)]
        Z = mp.fsum(ws)
        mu1 = mp.fsum(a*ws[a] for a in range(j))/Z
        c2 = mp.fsum((a-mu1)**2*ws[a] for a in range(j))/Z
        c3 = mp.fsum((a-mu1)**3*ws[a] for a in range(j))/Z
        c4 = mp.fsum((a-mu1)**4*ws[a] for a in range(j))/Z - 3*c2*c2
        MUd += mu1; S2d += c2; K3d += c3; K4d += c4
    rel = lambda a, b: fabs(a-b)/max(fabs(b), mpf('1e-30'))
    print(f"  {clk()} (m={m}, {tag}):  relerr s2={mp.nstr(rel(S2d,s2),3)}"
          f"  kappa3={mp.nstr(rel(K3d,k3),3)}  kappa4={mp.nstr(rel(K4d,k4),3)}"
          f"  mu={mp.nstr(rel(MUd,-Lp),3)}")
    print(f"      s2={mp.nstr(s2,12)}  kappa3={mp.nstr(k3,10)}  kappa4={mp.nstr(k4,10)}  s2>0={s2>0}")

# ---------- CHECKS 3-5 at the adversarial battery ---------------------------
print("== CHECKS 3/4/5: R5 direct vs series, majorant, t->0 continuity ==")
mp.dps = 45
battery = []
for m in (561,):
    for w in ['4.000000001', '4.3', '5', '8', '40.000000001', None]:
        if w is None:
            battery.append((m, mpf('0.89'), 'lam=0.89'))
        else:
            battery.append((m, mpf(w)/m, f"w={w}"))
    battery.append((m, (mpf(4)/m)*(1+mpf('1e-12')), 'lam=(4/m)(1+1e-12)'))
battery.append((700, mpf('4.000000001')/700, 'w=4+1e-9'))
battery.append((1581, mpf(5)/1581, 'w=5'))
battery.append((1581, mpf('0.89'), 'lam=0.89'))

allpass = True
for (m, lam, tag) in battery:
    s2, k3, k4, Lp, L5, MAJ = core(m, lam)
    Q0 = lam**3*fabs(L5)/(120*s2)
    for xfrac in [mpf(1)/2, mpf(1)/5]:
        t = lam*xfrac
        r5d = R5_direct(m, lam, t, s2, k3, k4, Lp)
        r5s, tail = R5_series(m, lam, t)
        diff = fabs(r5d - r5s)
        budget = tail + mpf(10)**(-(mp.dps-12))*max(1, fabs(s2*t*t))
        ok3 = diff <= budget
        B5 = t**5/120*MAJ
        ok4 = fabs(r5d) <= B5
        Q = lam**3*fabs(r5d)/(s2*t**5)
        Cabs = lam**3*MAJ/(120*s2)
        ok4b = Q <= Cabs*(1+mpf('1e-30'))
        allpass &= ok3 and ok4 and ok4b
        print(f"  {clk()} m={m:5d} {tag:22s} t=lam*{mp.nstr(xfrac,3)}:"
              f" |R5d-R5s|={mp.nstr(diff,3)} (tail bound {mp.nstr(tail,3)}) PASS={ok3};"
              f" |R5|<=B5: {ok4} (|R5|={mp.nstr(fabs(r5d),4)}, B5={mp.nstr(B5,4)});"
              f" Q={mp.nstr(Q,6)} <= C_abs={mp.nstr(Cabs,6)}: {ok4b}")
    # CHECK 5: continuity at t -> 0
    t = lam*mpf('1e-4')
    r5d = R5_direct(m, lam, t, s2, k3, k4, Lp)
    Qs = lam**3*fabs(r5d)/(s2*t**5)
    relgap = fabs(Qs - Q0)/max(Q0, mpf('1e-30'))
    ok5 = relgap < mpf('1e-2')
    allpass &= ok5
    print(f"           t->0: Q(t=lam*1e-4)={mp.nstr(Qs,8)} vs SOL.5.2 Q0={mp.nstr(Q0,8)}"
          f"  relgap={mp.nstr(relgap,3)}  PASS={ok5}")

print(f"{clk()} == IDENTITIES OVERALL PASS: {allpass} ==")
