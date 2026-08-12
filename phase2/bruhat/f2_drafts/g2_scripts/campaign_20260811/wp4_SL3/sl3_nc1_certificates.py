# NC-SL3-1: certificates for wp4_sl_SL3.md (Lemmas SL3.A/SL3.C, named
# constants, Theorem SL3.2 table). mpmath dps=40; every printed comparison is
# an explicit inequality with its margin. Safe-direction roundings asserted.
from mpmath import mp, mpf, exp, sqrt, pi, log, atan, asinh, sinh, asin

mp.dps = 40
ok = True
def chk(name, cond, detail=""):
    global ok
    ok = ok and bool(cond)
    print(f"[{'PASS' if cond else 'FAIL'}] {name}  {detail}")

# ---- named constants ----
x1 = mpf("3.9269"); x2 = mpf("2.9251")
chk("x1 <= pi/0.8", x1 <= pi/mpf("0.8"), f"pi/0.8 = {pi/mpf('0.8')}")
chk("x2 <= pi/1.074", x2 <= pi/mpf("1.074"), f"pi/1.074 = {pi/mpf('1.074')}")
c1 = (2/pi**2)*(1 - mpf("0.35")); c2 = (2/pi**2)*(1 - mpf("0.57"))
chk("c1 = (2/pi^2)(0.65) >= 1/8", c1 >= mpf(1)/8, f"c1 = {c1}")
chk("c2 = (2/pi^2)(0.43) >= 1/11.5", c2 >= mpf(1)/mpf("11.5"), f"c2 = {c2}")
chk("8/sqrt(2pi) <= 3.192", 8/sqrt(2*pi) <= mpf("3.192"), f"= {8/sqrt(2*pi)}")
chk("11.5/(1.6 sqrt(2pi)) <= 2.87", mpf("11.5")/(mpf("1.6")*sqrt(2*pi)) <= mpf("2.87"),
    f"= {mpf('11.5')/(mpf('1.6')*sqrt(2*pi))}")
chk("0.64/11.5 >= 0.0556", mpf("0.64")/mpf("11.5") >= mpf("0.0556"),
    f"= {mpf('0.64')/mpf('11.5')}")
chk("sqrt(pi/2)/4 <= 0.3134", sqrt(pi/2)/4 <= mpf("0.3134"), f"= {sqrt(pi/2)/4}")

# q(2,1) from wp1-c W.3 closed form: I(M,r), q = I/(2M)
def qWr(M, r):
    M = mpf(M); r = mpf(r)
    I = M*log((1+r)*M**2/(r*M**2+1)) - (2/sqrt(r))*(atan(sqrt(r)*M) - atan(sqrt(r)))
    return I/(2*M)
chk("q(2,1) >= 0.0741", qWr(2, 1) >= mpf("0.0741"), f"q(2,1) = {qWr(2,1)}")

# SL3.C: t0(0.89)/0.89 <= 1.074 ; sinh(0.445) <= 1 ; t0(0.89) < pi
t0_089 = 2*asin(sinh(mpf("0.89")/2))
chk("t0(0.89)/0.89 <= 1.074", t0_089/mpf("0.89") <= mpf("1.074"),
    f"ratio = {t0_089/mpf('0.89')}, margin = {mpf('1.074')-t0_089/mpf('0.89')}")
chk("sinh(0.445) <= 1", sinh(mpf("0.445")) <= 1, f"= {sinh(mpf('0.445'))}")
chk("t0(0.89) < pi", t0_089 < pi, f"t0(0.89) = {t0_089}")

# ---- Lemma SL3.A: interval certificate on (0, 0.89], step 0.001 ----
def phi1(lam):      # (1-e^-lam)/lam, phi1(0):=1, decreasing
    lam = mpf(lam)
    return mpf(1) if lam == 0 else (1 - exp(-lam))/lam
def Eps_piece(a_lo, a_hi, x0):   # upper bound of Eps(lam,x0) on (a_lo,a_hi]
    qhi = exp(-mpf(a_hi))
    p = phi1(a_lo)
    return exp(-x0)*(x0**2*p**2/(qhi*(1+qhi)) + 2*x0*p/(1+qhi) + 1)
N = 890  # step 0.001 over (0, 0.89]
m1 = mpf(0); m2 = mpf(0); arg1 = arg2 = None
for i in range(N):
    a_lo = mpf(i)/1000; a_hi = mpf(i+1)/1000
    e1 = Eps_piece(a_lo, a_hi, x1); e2 = Eps_piece(a_lo, a_hi, x2)
    if e1 > m1: m1, arg1 = e1, (a_lo, a_hi)
    if e2 > m2: m2, arg2 = e2, (a_lo, a_hi)
chk("SL3.A(i): max piece bound Eps(.,x1) <= 0.35", m1 <= mpf("0.35"),
    f"max = {m1} on {arg1}")
chk("SL3.A(ii): max piece bound Eps(.,x2) <= 0.57", m2 <= mpf("0.57"),
    f"max = {m2} on {arg2}")
# continuum reference values (lam -> 0): e^{-x}(x^2+2x+2)/2
for x0, tag in [(x1, "x1"), (x2, "x2")]:
    print(f"      continuum Eps(0+,{tag}) = {exp(-x0)*(x0**2+2*x0+2)/2}")

# ---- Theorem SL3.2: monotonicity thresholds + table + P3 ----
chk("P1 decreasing for A >= 16 (16 < 112.28)", mpf(16) < mpf("112.28"))
chk("P2 decreasing for A >= 1/(2*0.0556)", 1/(2*mpf("0.0556")) < mpf("112.28"),
    f"threshold = {1/(2*mpf('0.0556'))}")
chk("P3 decreasing for m >= 2.5/0.0741", mpf("2.5")/mpf("0.0741") < 401,
    f"threshold = {mpf('2.5')/mpf('0.0741')}")
P3_401 = mpf("0.3134")*mpf(401)**mpf("2.5")*exp(-mpf("0.0741")*401)
chk("P3(401) <= 1.3e-7", P3_401 <= mpf("1.3e-7"), f"P3(401) = {P3_401}")
print("      band table (A0 = c_A*401; P1,P2 safe-rounded UP at 4 dp):")
import math
bands = [("(4,5]","0.28"),("(5,6]","0.35"),("(6,8]","0.42"),("(8,10]","0.52"),
         ("(10,20]","0.60"),("(20,40]","0.70"),("(40,inf)","0.80")]
def rup(v, d=4):
    f = mpf(10)**d
    return math.ceil(float(v*f))/float(f)
for name, ca in bands:
    A0 = mpf(ca)*401
    P1 = mpf("3.192")*sqrt(A0)*exp(-A0/32)
    P2 = mpf("2.87")*sqrt(A0)*exp(-mpf("0.0556")*A0)
    tot = P1 + P2 + P3_401
    print(f"      {name:9s} cA={ca}  A0={float(A0):7.2f}  P1<={rup(P1):.4f}  "
          f"P2<={rup(P2):.4f}  total<={rup(tot):.4f}")
# worst-band checks quoted in the draft
A0 = mpf("0.28")*401
chk("W1: P1 <= 1.0125", mpf("3.192")*sqrt(A0)*exp(-A0/32) <= mpf("1.0125"),
    f"= {mpf('3.192')*sqrt(A0)*exp(-A0/32)}")
chk("W1: P2 <= 0.0592", mpf("2.87")*sqrt(A0)*exp(-mpf('0.0556')*A0) <= mpf("0.0592"),
    f"= {mpf('2.87')*sqrt(A0)*exp(-mpf('0.0556')*A0)}")
chk("P2 <= 0.2 already at A = 90", mpf("2.87")*sqrt(mpf(90))*exp(-mpf("0.0556")*90) <= mpf("0.2"),
    f"= {mpf('2.87')*sqrt(mpf(90))*exp(-mpf('0.0556')*90)}")
chk("three-slot form: 1.0125+0.0592+1.3e-7 <= 1.072",
    mpf("1.0125")+mpf("0.0592")+mpf("1.3e-7") <= mpf("1.072"))
chk("architected budget: 1.072 <= 1.01+0.2+0.01", mpf("1.072") <= mpf("1.22"))

# D2 gap documentation (not a certificate of the draft, a certificate of the
# CLAIM that the architected W.6 route needs an A-upper bound): with only
# A <= m available, 0.1117*m^1.5*e^{-E} <= 0.2 at m=401 forces E >= 8.4:
import mpmath
E_need = log(mpf("0.1117")*mpf(401)**mpf("1.5")/mpf("0.2"))
print(f"      D2 note: exponent needed with A<=m only: E >= {E_need} (measured W6min = 7.645)")
# provable W.6 corner exponent at w->4+, m=401 (draft §7 D2 formula):
w = mpf(4); Ecorner = 401*(mpf(1)/2)*(1-mpf("2.656")/w)*(mpf("0.4491")-mpf("1.506")/w)
print(f"      D2 note: provable W.6 corner exponent at w=4, m=401: {Ecorner}")

print("ALL CERTIFICATES PASS" if ok else "SOME CERTIFICATE FAILED")
