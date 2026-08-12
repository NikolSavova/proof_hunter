#!/usr/bin/env python3
# ref_mw5e_a_symbolic_exact.py -- MATHS REFEREE, wave5_sl4pe (SL4'-E machinery).
# [A] SYMBOLIC proof of Lemma E.1(ii) and E.1(iii) (sympy; strictly stronger
#     than the prover's 6-random-tuple Fraction check).
# [B] INDEPENDENT exact-rational re-derivation of the Lemma E.2 certificate
#     (formulas re-typed from the LEMMA TEXT, not copied from e1), compared
#     against the exact J0 fractions archived in out_e1_pricing_certificate.txt.
import sympy as sp
from fractions import Fraction as F

print("== [A] symbolic verification of Lemma E.1(ii)/(iii) ==")
t, b, a2, E, lam, s2 = sp.symbols('t b a2 E lam s2', positive=True)  # t = eps2
c  = a2/2
h4 = 3 - 6*t + t**2
h6 = t**3 - 15*t**2 + 45*t - 15
h3sq = t*(3 - t)**2
N   = 1 + 3*b - 15*c
D   = (1 + b*h4 + c*h6)**2 - a2*h3sq
Sig = 2 + b*(3 + h4) + c*(h6 - 15)
Cb  = (6 - t)*Sig
Ca  = (3 - t)**2 - (45 - 15*t + t**2)*Sig/2
lhs = sp.expand(N**2 - D)
rhs = sp.expand(t*(Cb*b + Ca*a2))
print("  (ii)  N^2 - D - eps2[C_b b4 + C_a a^2] == 0 symbolically:",
      sp.simplify(lhs - rhs) == 0)

# (iii): with eps2 = 1/s2, A = lam^2 s2, u = 1/A, r42 = 24 A b4, r31s = 36 A a2,
# rho1 = s2(E - 1) - 1 - eps2/2  (E stands for e^{eps2}),
# claim:  A*eta == lam^2/2 + rho1*A + (E/D)[(C_b/24) r42 + (C_a/36) r31s]
# where eta = s2 (E N^2/D - 1) - 1.
eps2s = 1/s2
A   = lam**2*s2
sub = {t: eps2s}
Ns, Ds, Cbs, Cas = (e.subs(sub) for e in (N, D, Cb, Ca))
eta  = s2*(E*Ns**2/Ds - 1) - 1
rho1 = s2*(E - 1) - 1 - eps2s/2
r42s = 24*A*b
r31s = 36*A*a2
rhs3 = lam**2/2 + rho1*A + (E/Ds)*(Cbs/24*r42s + Cas/36*r31s)
print("  (iii) A*eta - [lam^2/2 + rho1 A + (E/D)((C_b/24) r42 + (C_a/36) r31^2)] == 0:",
      sp.simplify(sp.together(A*eta - rhs3)) == 0)

print()
print("== [B] independent exact re-derivation of the E.2 certificate, m >= 561 ==")
M0 = 561
S0 = F(1122800, 7921); E0 = 1/S0
BANDS = [('W1', F(28,100), F(1,1),  F(8,10), F(5,1)),
         ('W2', F(35,100), F(12,10),F(14,10),F(6,1)),
         ('W3', F(42,100), F(15,10),F(26,10),F(8,1)),
         ('W4', F(52,100), F(17,10),F(35,10),F(10,1)),
         ('W5', F(60,100), F(2,1),  F(52,10),F(20,1)),
         ('W6b',F(70,100), F(21,10),F(6,1),  F(40,1)),
         ('W7', F(80,100), F(22,10),F(66,10),None)]
myJ0 = {}
allup = allpos = True
for (W, cA, R31, R42, wmax) in BANDS:
    A0 = cA*M0
    Lam = wmax/M0 if wmax is not None else F(89,100)
    Jst = R42/2 + F(3,10)*R31**2
    R42d = max(R42, 2*Jst)
    bb = R42d/(24*A0); aa = R31**2/(36*A0)
    xb = 3*bb + 15*(aa/2)                    # |x| <= xb, x = b4 h4 + c6 h6
    sb = 6*bb + 30*(aa/2)                    # |Sig - 2| <= sb
    db = 2*xb + xb**2 + 9*E0*aa              # |D - 1| <= db
    ph = (E0/(1-E0) + db)/(1 - db)           # |e^{eps2}/D - 1| <= ph
    e_b = max(6*(2+sb)/24 - F(1,2), F(1,2) - (6-E0)*(2-sb)/24)
    Ca_lo = 9 - 6*E0 - 45*(1 + sb/2)
    Ca_hi = 9 - (45 - 15*E0)*(1 - sb/2)
    e_a = max(abs(Ca_lo/36 + 1), abs(Ca_hi/36 + 1))
    M0cap = max(R42/2, Jst)
    REM2 = (1 + ph)*(e_b*R42d + e_a*R31**2) + ph*M0cap
    d1 = Lam**2*E0/(6*(1 - E0/4))
    REMs = REM2 + d1
    J0 = Jst - REMs
    myJ0[W] = J0
    up = REMs <= F(3,10)*R31**2
    Dlo = (1-xb)**2 - 9*E0*aa
    pos = (Dlo > 0) and (1 - 3*bb - 15*(aa/2) > 0) and (1 - xb - (aa + 9*E0)/2 > 0)
    allup &= up; allpos &= pos
    print(f"  {W:3s}: REM* = {float(REMs):.6f}  J0 = {float(J0):.6f}  "
          f"upper-slack {up}  positivity {pos}")
print(f"  all bands: upper-side REM* <= 0.3 R31*^2: {allup}; positivity: {allpos}")

# compare against the archived exact fractions in out_e1_pricing_certificate.txt
import re, pathlib
out = pathlib.Path(__file__).resolve().parents[2] / (
    'g2_scripts/campaign_20260811/wave5_sl4pe/out_e1_pricing_certificate.txt')
txt = out.read_text()
line = [l for l in txt.splitlines() if l.strip().startswith('exact J0:')][0]
arch = dict((m.group(1), F(int(m.group(2)), int(m.group(3))))
            for m in re.finditer(r'(W\d?b?\w*)=(\d+)/(\d+)', line))
same = all(arch[W] == myJ0[W] for W in myJ0)
print(f"  independent exact J0 fractions == archived e1 fractions (all 7 bands): {same}")
