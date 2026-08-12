#!/usr/bin/env python3
# e1_pricing_certificate.py -- wave-5 SL4'-E (eta pricing machinery), F2 campaign.
# EXACT-RATIONAL certificate of the remainder constants REM*(W) and the
# derived joint-bound thresholds J0(W) for Theorem E at the shifted CL
# threshold m >= 561.  Everything below is computed in Fractions; the only
# transcendental input is e^{eps2}, bounded by 1 <= e^{eps2} <= 1/(1-eps2)
# (valid for 0 < eps2 < 1), applied at eps2 = E0 := 1/S0.
#
# Frame (Lemma E.1 of wave5_sl4pe_20260812.md):
#   eta = s2 ( e^{eps2} N^2 / D - 1 ) - 1 ,  eps2 = 1/s2 ,
#   N = 1 + 3 b4 - 15 c6 ,   D = (1 + b4 h4 + c6 h6)^2 - a^2 h3^2 ,
#   a = k3/(6 s2^{3/2}), b4 = k4/(24 s2^2), c6 = k3^2/(72 s2^3) = a^2/2 ,
#   h3 = eps^3 - 3 eps, h4 = 3 - 6 eps2 + eps2^2,
#   h6 = eps2^3 - 15 eps2^2 + 45 eps2 - 15   (eps2 = eps^2 = 1/s2) .
# Exact identity (verified below at exact rational tuples):
#   N^2 - D = eps2 [ C_b b4 + C_a a^2 ] ,
#   C_b = (6 - eps2) Sig ,  C_a = (3-eps2)^2 - (45 - 15 eps2 + eps2^2) Sig/2 ,
#   Sig = 2 + b4 (3 + h4) + c6 (h6 - 15) .
# Hence, in u-units (u = 1/A, A = lam^2 s2, r42 = k4 lam^2/s2, r31s = (k3 lam/s2)^2):
#   eta/u = lam^2/2 + rho1*A + (e^{eps2}/D) [ (C_b/24) r42 + (C_a/36) r31s ] ,
#   0 <= rho1*A <= delta1max ,
# and the certificate below bounds the deviation of the bracket from
# (r42/2 - r31s) by REM2max, uniformly over the hypothesis ranges at m >= 561.
from fractions import Fraction as F

M0 = 561                      # shifted CL threshold (sliver CLOSED to 560)
S0 = F(1122800, 7921)         # [A2](iii) certified variance floor
E0 = 1 / S0                   # eps2 = 1/s2 <= E0

# band, c_A (A2), R31*, R42* (SL1'-w(i) scales), wmax (None = W7, lam <= 0.89)
BANDS = [
    ('W1',  F(28,100), F(1,1),   F(8,10),  F(5,1)),
    ('W2',  F(35,100), F(12,10), F(14,10), F(6,1)),
    ('W3',  F(42,100), F(15,10), F(26,10), F(8,1)),
    ('W4',  F(52,100), F(17,10), F(35,10), F(10,1)),
    ('W5',  F(60,100), F(2,1),   F(52,10), F(20,1)),
    ('W6b', F(70,100), F(21,10), F(6,1),   F(40,1)),
    ('W7',  F(80,100), F(22,10), F(66,10), None),
]

def fmt(x, nd=8):
    return f"{float(x):.{nd}g}"

print("== [0] exact identity check: N^2 - D == eps2 [C_b b4 + C_a a^2], c6 = a^2/2 ==")
import random
random.seed(20260812)
ok = True
for trial in range(6):
    t  = F(random.randint(1, 999), random.randint(1000, 99999))   # eps2
    b  = F(random.randint(-999, 999), random.randint(10**5, 10**6))  # b4
    a2 = F(random.randint(0, 999), random.randint(10**5, 10**6))     # a^2
    c  = a2 / 2
    h4 = 3 - 6*t + t*t
    h6 = t**3 - 15*t**2 + 45*t - 15
    h3sq = t * (3 - t)**2
    N  = 1 + 3*b - 15*c
    Dv = (1 + b*h4 + c*h6)**2 - a2*h3sq
    Sig = 2 + b*(3 + h4) + c*(h6 - 15)
    Cb = (6 - t)*Sig
    Ca = (3 - t)**2 - (45 - 15*t + t*t)*Sig/2
    lhs = N*N - Dv
    rhs = t*(Cb*b + Ca*a2)
    same = (lhs == rhs)
    ok = ok and same
    print(f"  tuple {trial}: exact equality: {same}")
print(f"  identity holds at all exact rational tuples: {ok}")

print()
print("== [1] per-band certified constants at m >= 561 (exact rationals; floats shown) ==")
print("  S0 = 1122800/7921 =", fmt(S0), "; E0 = 1/S0 =", fmt(E0))
rows = []
for (W, cA, R31, R42, wmax) in BANDS:
    A0  = cA * M0                       # A >= c_A(W) m >= c_A(W)*561
    Lam = (wmax / M0) if wmax is not None else F(89,100)   # lam <= Lam(W)
    Jstar = R42/2 + F(3,10)*R31**2      # J* = R42*/2 + 0.3 R31*^2 = price - lam^2/2
    R42d  = max(R42, 2*Jstar)           # |r42| cap: r42 <= R42* (E2); r42 >= -2 J0 >= -2 J* by (E1)+(E3)
    bbar  = R42d / (24*A0)              # |b4| <= bbar
    a2bar = R31**2 / (36*A0)            # a^2 <= a2bar
    cbar  = a2bar / 2                   # c6 <= cbar
    xbar  = 3*bbar + 15*cbar            # |b4 h4 + c6 h6| <= xbar   (|h4|<=3, |h6|<=15)
    sbar  = 6*bbar + 30*cbar            # |Sig - 2| <= sbar          (|3+h4|<=6, |h6-15|<=30)
    dbar  = 2*xbar + xbar**2 + 9*E0*a2bar   # |D - 1| <= dbar
    Dlo   = (1 - xbar)**2 - 9*E0*a2bar      # D >= Dlo
    ebar  = E0 / (1 - E0)               # e^{eps2} <= 1 + ebar
    phi   = (ebar + dbar) / (1 - dbar)  # |e^{eps2}/D - 1| <= phi
    Cb_hi = 6*(2 + sbar);  Cb_lo = (6 - E0)*(2 - sbar)
    e_b   = max(Cb_hi/24 - F(1,2), F(1,2) - Cb_lo/24)      # |C_b/24 - 1/2| <= e_b
    Ca_hi = 9 - (45 - 15*E0)*(1 - sbar/2)
    Ca_lo = 9 - 6*E0 - 45*(1 + sbar/2)
    e_a   = max(abs(Ca_hi + 36), abs(Ca_lo + 36)) / 36     # |C_a/36 + 1| <= e_a
    M0cap = max(R42/2, Jstar)           # |r42/2 - r31s| <= M0cap under (E1)-(E3)
    Mdev  = e_b*R42d + e_a*R31**2       # |M - (r42/2 - r31s)| <= Mdev
    REM2  = (1 + phi)*Mdev + phi*M0cap
    d1max = Lam**2 * E0 / (6*(1 - E0/4))     # 0 <= rho1*A <= d1max
    REMs  = REM2 + d1max                # REM*(W)
    J0    = Jstar - REMs                # J0(W): the (E3) threshold
    up_ok = (REMs <= F(3,10)*R31**2)    # upper-side slack check
    pos_ok = (Dlo > 0) and (1 - 3*bbar - 15*cbar > 0) and (1 - xbar - (a2bar + 9*E0)/2 > 0)
    rows.append((W, REMs, J0))
    print(f"  {W:3s}: A0={fmt(A0,6)} Lam={fmt(Lam,4)} J*={fmt(Jstar,6)} R42+={fmt(R42d,4)} "
          f"bbar={fmt(bbar,3)} a2bar={fmt(a2bar,3)} dbar={fmt(dbar,3)} phi={fmt(phi,3)} "
          f"e_b={fmt(e_b,3)} e_a={fmt(e_a,3)}")
    print(f"       REM2={fmt(REM2,6)} d1max={fmt(d1max,3)} REM*={fmt(REMs,6)} "
          f"J0={fmt(J0,6)}  upper-side REM* <= 0.3 R31*^2: {up_ok}  positivity(D,qhat): {pos_ok}")

print()
print("== [2] summary tables (float; exact fractions above are authoritative) ==")
print("  REM*(W):", " / ".join(fmt(r[1],5) for r in rows))
print("  J0(W)  :", " / ".join(fmt(r[2],6) for r in rows))
print("  exact J0:", " ; ".join(f"{r[0]}={r[2].numerator}/{r[2].denominator}" for r in rows))
