#!/usr/bin/env python3
"""Independent referee verification for wave2_repairs_20260811.md.

Re-derives, by METHODS DIFFERENT from the session's scripts, the key numbers:
 (1) E(u) for u = 1..6 via mpmath dps=50 nsum (independent of the integer
     fixed-point route) -> check each lies inside w2r_rep1's certified
     bracket [lo, hi], and re-check safe/unsafe classification of the
     original E-decimal prints.
 (2) pi bracket digits used by w2r_rep1 (P_LO/Q < pi < P_HI/Q).
 (3) Monotonicity-in-p of the per-term function (the endpoint-evaluation
     validity gap in w2r_rep1's docstring): certify numerically that
     d/da log term < 0 reduces to 3/(3a+c) < 1/a, true identically; here
     just sanity-check term(P_LO) > term(P_HI) for a spread of (n, u).
 (4) B_m sanity: B_401 * 401 vs 27/25; deficits/rho reprints; the R2 chain
     (eps*, R2 value) with exact Fractions built from mpmath-independent
     E-values; the 'unsafe by' gap of the old rho(4) print 0.7271.
 (5) rep2 cross-checks: bracket crossover (first positive m), NC-13 m0
     table for C' in {1,5,20,42} (both flavors), the (1581,1) margin
     fraction 17363 + 14921/28458.
 (6) refm_a hand-checks: EX2(q)= q(1+q)/(1-q)^2 vs (1+1/lam)^2 at lam=0.1;
     Var = q/(1-q)^2; the M8 inequality failure root d* of
     (1-d)^{-2} = 1+2d+3.5d^2 (claimed 'fails from d ~ 0.107').
 (7) C2 arithmetic: 1 - 0.0330*3.7^2 >= 0.548.
"""
from fractions import Fraction as F
import mpmath as mp

mp.mp.dps = 50
ok = True

def chk(label, cond):
    global ok
    print(" %-68s %s" % (label, cond))
    ok &= bool(cond)

# (1) independent E(u)
print("(1) independent E(u), mpmath nsum dps=50:")
brackets = {
    1: (F("0.004006927541"), F("0.004006927542")),
    2: (F("0.003587187143"), F("0.003587187144")),
    3: (F("0.003040358636"), F("0.003040358637")),
    4: (F("0.002489924424"), F("0.002489924425")),
    5: (F("0.002006520248"), F("0.002006520249")),
    6: (F("0.001612406722"), F("0.001612406723")),
}
orig = {1: "0.00400693", 2: "0.00358719", 3: "0.00304036",
        4: "0.00248992", 5: "0.00200652", 6: "0.00161241"}
corr = {1: "0.00400692", 2: "0.00358718", 3: "0.00304035",
        4: "0.00248992", 5: "0.00200652", 6: "0.00161240"}
Eval = {}
for u in range(1, 7):
    f = lambda n: 2*(3*(2*mp.pi*n)**2 + u*u)/((2*mp.pi*n)**2*((2*mp.pi*n)**2 + u*u)**2)
    E = mp.nsum(f, [1, mp.inf])
    Eval[u] = E
    lo, hi = brackets[u]
    inside = mp.mpf(lo.numerator)/lo.denominator <= E <= mp.mpf(hi.numerator)/hi.denominator
    chk("E(%d) = %s inside rep1 bracket" % (u, mp.nstr(E, 14)), inside)
    chk("  corrected print %s <= E" % corr[u], mp.mpf(corr[u]) <= E)
    unsafe = mp.mpf(orig[u]) > E
    print("   original print %s > E (unsafe)? %s" % (orig[u], unsafe))

# (2) pi bracket
print("(2) pi bracket:")
P_LO, P_HI, Q = 314159265358979323846, 314159265358979323847, 10**20
chk("P_LO/Q < pi < P_HI/Q", mp.mpf(P_LO)/Q < mp.pi < mp.mpf(P_HI)/Q)

# (3) monotonicity spot check term(P_LO) > term(P_HI)
print("(3) per-term monotonicity in p (endpoint validity):")
mono = True
for u in (1, 8):
    for n in (1, 7, 50000):
        vals = []
        for p in (P_LO, P_HI):
            a = 4*n*n*p*p
            c = u*u*Q*Q
            vals.append(F(2*(3*a+c)*Q**4, a*(a+c)**2))
        mono &= vals[0] > vals[1]
chk("term strictly decreasing in p at all spot (u,n)", mono)
# identity: d/da log g = 3/(3a+c) - 1/a - 2/(a+c) < 0 since 3/(3a+c) < 1/a.

# (4) B_m, deficits, R2 chain
print("(4) B_m / deficit / rho / R2 chain:")
def S4(m): return m*(m+1)*(2*m+1)*(3*m*m+3*m-1)//30
def lam_var(m): return F(m*(m-1)*(2*m+5), 72)
def B(m): return F(S4(m)-m, 240)/lam_var(m)**2
print("   B_401*401 = %.6f (expect ~27/25 = 1.08)" % float(B(401)*401))
chk("B_401*401 in (1.06, 1.09)", F(106,100) < B(401)*401 < F(109,100))
d4 = F(685, 100)*16*brackets[4][1]  # deficit(4) using E_hi -> rho lower end
d4lo = F(685, 100)*16*brackets[4][0]
rho4_hi = 1 - d4lo
chk("rho(4) certified <= 0.72711", rho4_hi <= F(72711, 10**5))
gap = rho4_hi - F(7271, 10**4)
print("   old print 0.7271 unsafe by %.3e (doc claims 4.8e-6)" % float(gap))
chk("gap in (4e-6, 5e-6)", F(4,10**6) < gap < F(5,10**6))
eps = 1 - F(102,100)*rho4_hi
chk("eps* >= 20/79.5", eps >= F(40, 159))
val = (1 - F(40,159))/rho4_hi
print("   R2 value = %.6f (doc: 1.029326)" % float(val))
chk("R2 value >= 1.0292", val >= F(10292, 10**4))
d2lo = F(685,100)*4*brackets[2][0]
chk("deficit(2) >= 0.0982 and old 0.0983 unsafe",
    d2lo >= F(982,10**4) and F(685,100)*4*brackets[2][1] < F(983,10**4))

# (5) rep2 cross-checks
print("(5) rep2 cross-checks:")
E4LO = F(248992, 10**8)
CC = F(1071, 100)
CO = F(685, 100)
def br(m): return CO*E4LO*(1 - 17*B(m) - CC/m**2) - B(m)
firsts = [m for m in range(30, 200) if br(m) > 0]
chk("bracket first positive at m = 82", firsts[0] == 82)
chk("bracket negative at m = 81 and 68", br(81) <= 0 and br(68) <= 0)
CS = F(187, 216)
tab = {}
for Cp in (1, 5, 20, 42):
    m_disp = next(m for m in range(4, 3000) if 1 - F(27,25*m) - F(Cp,m*m) >= CS)
    m_ex = next(m for m in range(4, 3000) if 1 - B(m) - F(Cp,m*m) >= CS)
    tab[Cp] = (m_disp, m_ex)
print("   m0 table:", tab)
chk("m0 = 9/12/17/23 (disp) and same exact",
    all(tab[c] == (v, v) for c, v in ((1,9),(5,12),(20,17),(42,23))))
marg = F(1580**2*3167, 144*2*1581)
chk("margin = 17363 + 14921/28458", marg == 17363 + F(14921, 28458))
chk("17363 <= margin < 17364", 17363 <= marg < 17364)

# (6) refm_a hand checks
print("(6) refm_a hand checks:")
lam = mp.mpf("0.1")
q = mp.e**(-lam)
EX2 = q*(1+q)/(1-q)**2
Var = q/(1-q)**2
print("   EX2(lam=0.1) = %.4f (out: 190.3251), Var = %.4f (out: 99.9167)"
      % (EX2, Var))
chk("EX2 approx 190.3251", abs(EX2 - mp.mpf("190.3251")) < 1e-3)
chk("Var approx 99.9167 and <= 121", abs(Var - mp.mpf("99.9167")) < 1e-3 and Var <= 121)
# failure root of (1-d)^-2 = 1+2d+3.5d^2  ->  3.5d^2 - 5d + 0.5 = 0
r = (5 - mp.sqrt(25 - 7))/7
print("   M8 inequality failure root d* = %.6f (doc: 'fails from d ~ 0.107')" % r)
chk("d* in (0.107, 0.11)", mp.mpf("0.107") < r < mp.mpf("0.11"))

# (7) C2 arithmetic
print("(7) C2: 1 - 0.0330*3.7^2 = %.5f >= 0.548" % (1 - 0.0330*3.7**2))
chk("s2/lambda floor at w=3.7", F(1) - F(330,10**4)*F(37,10)**2 >= F(548,10**3))

print("VERDICT:", "PASS" if ok else "FAIL")
