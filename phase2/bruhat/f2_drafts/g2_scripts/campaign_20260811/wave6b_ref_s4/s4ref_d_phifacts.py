# s4ref_d_phifacts.py -- truth spot-checks of the three characteristic-function
# facts the draft consumes as "established", at adversarial (m, lam, t):
#   (SOL.4): |Phi(t)| <= e^{-0.32 s2 t^2}         on 0 < t <= 0.8 lam   [Thm SL3', min gamma* = 0.32]
#   (SOL.5): |Phi(t)| <= e^{-0.0176 m}            on 0.8 lam <= t <= t0 [R.1 (w in (4,5]) / tier-2+c_A (W2-W7)]
#   (SOL.6): |Phi(t)| <= e^{-0.0741 m}            on t0 <= t <= pi      [Thm A3(ii) P3 ingredient]
# plus the exact-arithmetic coverage table for (SOL.5) on W2-W7:
#   c2 * 0.64 * c_A(W) >= 0.0176  with c2 = (2/pi^2)(0.43) = 0.0871362...
# t0(lam) = 2 asin(sinh(lam/2)) (the s = S crossover scale; Cor X.2: t0 <= 1.074 lam).
import mpmath as mp
mp.mp.dps = 30

def log_absPhi(m, lam, t):
    z = mp.e**(1j*t - lam); q = mp.e**(-lam)
    tot = mp.mpf(0); zj = mp.mpf(1); qj = mp.mpf(1)
    for j in range(1, m+1):
        zj = zj*z; qj = qj*q
        tot += mp.log(abs(1 - zj)) - mp.log(abs(1 - z)) - mp.log(1 - qj) + mp.log(1 - q)
    return tot

def csch(x): return 1/mp.sinh(x)
def s2_of(m, lam):
    return sum((csch(lam/2)**2 - j*j*csch(j*lam/2)**2)/4 for j in range(2, m+1))

def t0_of(lam): return 2*mp.asin(mp.sinh(lam/2))

print("== [1] exact coverage chain for (SOL.5) on W2-W7: c2*0.64*c_A >= 0.0176 ==")
from fractions import Fraction as F
# c2 = (2/pi^2)(1 - 0.57) certified >= 1/11.5 (Thm SL3.1(i')); use the certified decimal 0.0871362 (floor)
c2 = mp.mpf("0.0871362")
cA = {"W2": F(35,100), "W3": F(42,100), "W4": F(52,100), "W5": F(60,100),
      "W6b": F(70,100), "W7": F(80,100)}
for Wn, ca in cA.items():
    val = c2*mp.mpf("0.64")*mp.mpf(float(ca))
    print(f"  {Wn}: c2*0.64*c_A = {mp.nstr(val, 6)} >= 0.0176: "
          f"{'PASS' if val >= mp.mpf('0.0176') else 'FAIL'}"
          f"  (margin {mp.nstr((val/mp.mpf('0.0176')-1)*100, 4)}%)")
print("  NOTE: W1 (w in (4,5]) is NOT covered by this chain (0.0871362*0.64*0.28 = "
      f"{mp.nstr(c2*mp.mpf('0.64')*mp.mpf('0.28'), 5)} < 0.0176) -- it needs Lemma R.1, as the draft cites.")

print("== [2] truth spot-checks ==")
cases = [(700, mp.mpf("0.89"),      "W7 deep"),
         (700, mp.mpf("4.0001")/700, "W1 open edge"),
         (700, mp.mpf("5.0001")/700, "W2 left edge"),
         (700, mp.mpf("40.0001")/700,"W7 left edge"),
         (561, mp.mpf("4.0001")/561, "W1 open edge, m=561"),
         (561, mp.mpf("0.89"),      "W7 deep, m=561")]
for m, lam, label in cases:
    s2 = s2_of(m, lam); t0 = t0_of(lam)
    # (SOL.4) grid on (0, 0.8 lam]
    bad4 = 0; worst4 = mp.mpf("inf")
    for i in range(1, 25):
        t = mp.mpf("0.8")*lam*i/24
        L = log_absPhi(m, lam, t)
        ratio = -L/(s2*t*t)
        if ratio < worst4: worst4 = ratio
        if ratio < mp.mpf("0.32"): bad4 += 1
    # (SOL.5) grid on [0.8 lam, t0]
    bad5 = 0; worst5 = mp.mpf("inf")
    for i in range(0, 25):
        t = mp.mpf("0.8")*lam + (t0 - mp.mpf("0.8")*lam)*i/24
        L = log_absPhi(m, lam, t)
        ratio = -L/m
        if ratio < worst5: worst5 = ratio
        if ratio < mp.mpf("0.0176"): bad5 += 1
    # (SOL.6) grid on [t0, pi]
    bad6 = 0; worst6 = mp.mpf("inf")
    for i in range(0, 41):
        t = t0 + (mp.pi - t0)*i/40
        L = log_absPhi(m, lam, t)
        ratio = -L/m
        if ratio < worst6: worst6 = ratio
        if ratio < mp.mpf("0.0741"): bad6 += 1
    print(f"  m={m}, w={mp.nstr(lam*m, 6)} ({label}): t0/lam = {mp.nstr(t0/lam, 6)}")
    print(f"    (SOL.4) min -log|Phi|/(s2 t^2) on (0, 0.8lam] = {mp.nstr(worst4, 6)}"
          f"  (>=0.32: {'PASS' if bad4 == 0 else 'FAIL ' + str(bad4)})")
    print(f"    (SOL.5) min -log|Phi|/m on [0.8lam, t0]     = {mp.nstr(worst5, 6)}"
          f"  (>=0.0176: {'PASS' if bad5 == 0 else 'FAIL ' + str(bad5)})")
    print(f"    (SOL.6) min -log|Phi|/m on [t0, pi]         = {mp.nstr(worst6, 6)}"
          f"  (>=0.0741: {'PASS' if bad6 == 0 else 'FAIL ' + str(bad6)})")
print("== [3] Cor X.2 cap sanity: t0(0.89)/0.89 ==")
print(f"  t0(0.89)/0.89 = {mp.nstr(t0_of(mp.mpf('0.89'))/mp.mpf('0.89'), 10)} <= 1.074: "
      f"{'PASS' if t0_of(mp.mpf('0.89'))/mp.mpf('0.89') <= mp.mpf('1.074') else 'FAIL'}")
