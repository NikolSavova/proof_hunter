#!/usr/bin/env python3
# wave6b_ref_s1 / ref3_band_certificate_iv.py
# Independent RIGOROUS re-certification of the draft's SOL.6 band table (V4+V5),
# using mpmath.iv outward-rounded interval arithmetic (prec 100 bits).
#
# For each band [A0,B0] with cells [wk, wk+d], d = 2^-8, lambda in [0, (wk+d)/561]
# (same lambda rule as the draft's V5), we form rigorous enclosures
#   L2 <= D2,  U3 >= D3,  U4 >= D4        (draft eqs (20)-(22), M-bounds (17))
# and check cell-by-cell:
#   (U3/L2).b <= c31(band),  (U4/L2).b <= c42(band),  L2.a >= floor(band) > 0.
# Monotone facts used for tight enclosures (all PROVED in the draft and verified
# analytically + in ref2): h2, h3 strictly decreasing; b(x)=h4/h2 increasing with
# b(0)=6; h2<=1; S_n(w) = sum e^{-nu w}E_n(nu w)/nu^2 decreasing in w (termwise,
# d/dx[e^{-x}E_n(x)] = -e^{-x}x^n/n!). h4(w-cell) is evaluated by direct interval
# arithmetic (no monotonicity assumed). Series tail: for w >= 4 the term ratio is
# <= e^{-4}*2^4 < 0.3, so once the float bound of the next term is < 1e-38 the
# whole tail is < 2e-38; we add [0, 1e-36] (100x headroom).
# Adaptive: failing cells are bisected down to 2^-14 before being declared FAILURES.
import math
from mpmath import iv, mp, mpf

iv.prec = 100
mp.prec = 100

zeta2 = iv.pi**2/6
ONE, TWO, SIX = iv.mpf(1), iv.mpf(2), iv.mpf(6)
FACT = {2: (1, 2), 3: (2, 6), 4: (6, 24)}  # (n-1)!, n!

def En_iv(n, xi):
    s = iv.mpf(1); t = iv.mpf(1)
    for k in range(1, n+1):
        t = t*xi/k; s = s + t
    return s

def En_f(n, x):
    s = 1.0; t = 1.0
    for k in range(1, n+1):
        t = t*x/k; s += t
    return s

def S_point(n, w_str):
    """Interval enclosure of S_n(w) = sum_{nu>=1} e^{-nu w}E_n(nu w)/nu^2 at point w."""
    wiv = iv.mpf(w_str); wf = float(mpf(w_str))
    s = iv.mpf(0); nu = 1
    while True:
        xi = nu*wiv
        s = s + iv.exp(-xi)*En_iv(n, xi)/(nu*nu)
        nu += 1
        x = nu*wf
        tb = math.exp(-x)*En_f(n, x)/(nu*nu) if x < 700 else 0.0
        if tb < 1e-38:
            return s + iv.mpf([0, mpf('1e-36')])
        if nu > 400:
            raise RuntimeError("series did not converge")

def iv_sinh(x):  # rigorous: interval combination of enclosed exponentials
    return (iv.exp(x) - iv.exp(-x))/2

def iv_cosh(x):
    return (iv.exp(x) + iv.exp(-x))/2

def h2_pt(x_iv): return (x_iv/(2*iv_sinh(x_iv/2)))**2
def h3_pt(x_iv): return x_iv**3*iv_cosh(x_iv/2)/(4*iv_sinh(x_iv/2)**3)
def h4_direct(x_iv): return x_iv**4*(iv_cosh(x_iv)+2)/(8*iv_sinh(x_iv/2)**4)

def hull(a, b):
    return iv.mpf([min(a.a, b.a), max(a.b, b.b)])

class SCache(dict):
    def get_s(self, n, w_str):
        if (n, w_str) not in self:
            self[(n, w_str)] = S_point(n, w_str)
        return self[(n, w_str)]

def cell_check(sc, wA, wB, c31, c42):
    """wA, wB exact dyadic mpf. Returns (ok, r31_hi, r42_hi, L2_lo)."""
    sA, sB = str(wA), str(wB)
    w_iv = iv.mpf([wA, wB])
    # G_n via monotone S: S_n decreasing => S_n([wA,wB]) subset [S(wB).a, S(wA).b]
    G = {}
    for n in (2, 3, 4):
        Slo = sc.get_s(n, sB); Shi = sc.get_s(n, sA)
        S_iv = iv.mpf([Slo.a, Shi.b])
        G[n] = FACT[n][0]*w_iv - FACT[n][1]*zeta2 + FACT[n][1]*S_iv
    # h at w: h2, h3 decreasing -> endpoint hull; h4 direct interval
    h2A, h2B = h2_pt(iv.mpf(sA)), h2_pt(iv.mpf(sB))
    h3A, h3B = h3_pt(iv.mpf(sA)), h3_pt(iv.mpf(sB))
    h2w = iv.mpf([h2B.a, h2A.b]); h3w = iv.mpf([h3B.a, h3A.b])
    h4w = h4_direct(w_iv)
    # lambda range [0, wB/561]
    lamB = (iv.mpf(sB)/561).b
    lam_iv = iv.mpf([0, lamB])
    h2l = h2_pt(iv.mpf(lamB))
    h2lam_m1 = iv.mpf([(h2l - 1).a, 0])                    # h2(lam)-1 in [h2(lamB)-1, 0]
    h3l = h3_pt(iv.mpf(lamB))
    h3lam_m2 = iv.mpf([(h3l - 2).a, 0])                    # h3(lam)-2 in [h3(lamB)-2, 0]
    lb2 = iv.mpf(lamB)**2
    h4lam_m6 = iv.mpf([(6*h2l - 6).a, (lb2 + 6*h2l - 6).b])  # via h4 = b(x)h2(x)
    lam2 = lam_iv**2
    L2 = G[2] + w_iv*h2lam_m1 - (lam_iv/2)*(h2w - 1) - w_iv*lam2/12
    U3 = G[3] + w_iv*h3lam_m2 - (lam_iv/2)*(h3w - 2) + w_iv*lam2/3
    U4 = G[4] + w_iv*h4lam_m6 - (lam_iv/2)*(h4w - 6) + 5*w_iv*lam2/3
    if not (L2.a > 0):
        return (False, mpf('inf'), mpf('inf'), L2.a)
    R31 = (U3/L2).b; R42 = (U4/L2).b
    return (R31 <= c31 and R42 <= c42, R31, R42, L2.a)

BANDS = [  # (A0, B0, c31, c42, floor)  -- the draft's SOL.6 table
    (mpf(4), mpf(5), mpf('0.900'), mpf('0.680'), mpf('1.15')),
    (mpf(5), mpf(6), mpf('1.090'), mpf('1.250'), mpf('1.90')),
    (mpf(6), mpf(8), mpf('1.370'), mpf('2.400'), mpf('2.75')),
    (mpf(8), mpf(10), mpf('1.550'), mpf('3.260'), mpf('4.65')),
    (mpf(10), mpf(20), mpf('1.850'), mpf('4.980'), mpf('6.60')),
    (mpf(20), mpf(40), mpf('1.970'), mpf('5.650'), mpf('16.50')),
]
TARGETS31 = [mpf(x) for x in "1.19 1.44 1.82 2.04 2.38 2.56".split()]
TARGETS42 = [mpf(x) for x in "0.87 1.62 3.11 4.27 6.38 7.33".split()]

D0 = mpf(2)**-8
DMIN = mpf(2)**-14
sc = SCache()
grand_ok = True
print(f"iv precision: {iv.prec} bits; base cell width 2^-8; adaptive bisection to 2^-14")
print(f"lambda rule per cell [A,B]: lam in [0, B/561]  (the draft's V5 rule)\n")
for bi, (A0, B0, c31, c42, floor) in enumerate(BANDS):
    stack = []
    w = A0
    while w < B0:
        stack.append((w, w + D0))
        w += D0
    maxR31 = mpf(0); maxR42 = mpf(0); minL2 = mpf('inf')
    fails = []
    ncells = 0
    while stack:
        wA, wB = stack.pop()
        ok, r31, r42, l2lo = cell_check(sc, wA, wB, c31, c42)
        ncells += 1
        if not ok:
            if wB - wA > DMIN:
                mid = (wA + wB)/2
                stack.append((wA, mid)); stack.append((mid, wB))
                continue
            fails.append((wA, wB, r31, r42, l2lo))
            continue
        maxR31 = max(maxR31, r31); maxR42 = max(maxR42, r42); minL2 = min(minL2, l2lo)
    band_ok = (not fails) and minL2 >= floor
    grand_ok = grand_ok and band_ok
    print(f"band [{mp.nstr(A0,4)},{mp.nstr(B0,4)}]  cells evaluated: {ncells}")
    print(f"  certified sup U3/L2 <= {mp.nstr(maxR31, 8)}  (draft ceiling {mp.nstr(c31,4)};"
          f" <= ceiling: {maxR31 <= c31};  ceiling < target {mp.nstr(TARGETS31[bi],4)}: {c31 < TARGETS31[bi]})")
    print(f"  certified sup U4/L2 <= {mp.nstr(maxR42, 8)}  (draft ceiling {mp.nstr(c42,4)};"
          f" <= ceiling: {maxR42 <= c42};  ceiling < target {mp.nstr(TARGETS42[bi],4)}: {c42 < TARGETS42[bi]})")
    print(f"  certified inf L2 >= {mp.nstr(minL2, 8)}   (draft floor {mp.nstr(floor,5)};"
          f" >= floor: {minL2 >= floor};  positive: {minL2 > 0})")
    if fails:
        print(f"  ** {len(fails)} FAILING CELLS at width 2^-14, first: {fails[0]}")
    print(f"  BAND VERDICT: {'PASS' if band_ok else 'FAIL'}\n")

print(f"ALL SIX BANDS RIGOROUSLY CERTIFIED (table (V5)+(V4) TRUE): {grand_ok}")

# --- the draft's exact-resolution sentinel cells (width 2^-12, right edge of band) ---
print("\ndraft-resolution sentinel cells (width 2^-12 at each band's right edge):")
for bi, (A0, B0, c31, c42, floor) in enumerate(BANDS):
    wA = B0 - mpf(2)**-12
    ok, r31, r42, l2lo = cell_check(sc, wA, B0, c31, c42)
    print(f"  [{mp.nstr(wA, 12)}, {mp.nstr(B0,4)}]: U3/L2 <= {mp.nstr(r31, 8)} (c31 {mp.nstr(c31,4)}),"
          f" U4/L2 <= {mp.nstr(r42, 8)} (c42 {mp.nstr(c42,4)}), L2 >= {mp.nstr(l2lo, 8)} -> pass {ok}")

# --- consumption checks: draft constants == plan constants; chain arithmetic ---
print("\nconstants consumption:")
draft_R31 = "1.19 1.44 1.82 2.04 2.38 2.56 2.71".split()
draft_R42 = "0.87 1.62 3.11 4.27 6.38 7.33 8.17".split()
plan_R31 = "1.19 1.44 1.82 2.04 2.38 2.56 2.71".split()   # wave6_s1_plan §2 NEW column
plan_R42 = "0.87 1.62 3.11 4.27 6.38 7.33 8.17".split()
print(f"  draft R31* == plan R31*: {draft_R31 == plan_R31}")
print(f"  draft R42* == plan R42*: {draft_R42 == plan_R42}")
worst_row = mpf('0.978293')   # plan block [C], W6b @ 561
print(f"  20 * worst row 0.978293 = {mp.nstr(20*worst_row, 8)}  (plan quotes C* = 19.5659; "
      f"|diff| < 5e-5: {abs(20*worst_row - mpf('19.5659')) < mpf('5e-5')})  <= 20: {20*worst_row <= 20}")
worst_row_1581 = mpf('0.75839')
print(f"  20 * worst row(1581) 0.75839 = {mp.nstr(20*worst_row_1581, 8)}  (plan quotes 15.1678; "
      f"match: {abs(20*worst_row_1581 - mpf('15.1678')) < mpf('5e-5')})  <= 136: {20*worst_row_1581 <= 136}")
# W7 rigorous: a(0.89), b(0.89) in iv
lam89 = iv.mpf('0.89')
a89 = lam89*iv_cosh(lam89/2)/iv_sinh(lam89/2)
b89 = lam89**2*(1 + 3/(2*iv_sinh(lam89/2)**2))
print(f"  iv a(0.89) = [{mp.nstr(a89.a, 12)}, {mp.nstr(a89.b, 12)}]  < 2.71: {a89.b < mpf('2.71')}"
      f"  in draft enclosure (2.1302, 2.1304): {mpf('2.1302') < a89.a and a89.b < mpf('2.1304')}")
print(f"  iv b(0.89) = [{mp.nstr(b89.a, 12)}, {mp.nstr(b89.b, 12)}]  < 8.17: {b89.b < mpf('8.17')}"
      f"  in draft enclosure (6.4111, 6.4114): {mpf('6.4111') < b89.a and b89.b < mpf('6.4114')}")
