#!/usr/bin/env python3
# ref_msr_a_row_indep.py -- maths referee, wave4_sl4p_repaired: INDEPENDENT
# re-implementation of the W1 row from the DRAFT TEXTS' displayed closed forms
# (original wave4_sl4p SS2 Lemmas SL4'.3-.5 + SS1 pricing + wp1-c W.6), written
# from scratch (no import of sl4pr_common / sl4p_nc1_ledger).  Checks:
#  [A1] trapezoid boundary values: row(401, 4.095) PASS / row(401, 4.094) FAIL;
#       row(462, 4.00021) PASS / row(462, 4.00020) FAIL; row(46x, 4+1e-9)
#       first PASS at m = 463.
#  [A2] Fact R.G sentinels: row(561, 4+1e-9), row(699, 4+1e-9).
#  [A3] independent named-constant round checks.
import mpmath as mp
mp.mp.dps = 50
SQ2PI = mp.sqrt(2*mp.pi)
INFL = mp.mpf('1.10'); QUADF = mp.mpf('0.09')
C1T = mp.mpf('0.1317'); C2T = mp.mpf('0.0871'); FAREXP = mp.mpf('0.0741')

# --- W1 constants from the tables (original SS0/SS4): ---
R31 = mp.mpf('1.0'); R42 = mp.mpf('0.8'); CAD = mp.mpf('0.28')
C5 = mp.mpf('0.05'); GAM = mp.mpf('0.42')   # route (a): Theorem SL3' W1 value

def efac(C5v): return (mp.mpf('0.5')/(mp.mpf('0.5') - C5v/8))**4

def dec_entries(A, g, C5v):
    # R5 numerator + denominator (Lemma SL4'.3)
    r5n = 48*SQ2PI/mp.pi*C5v*efac(C5v)/mp.sqrt(A)
    r5d = 8*SQ2PI/mp.pi*C5v*efac(C5v)/mp.sqrt(A)
    # cube + cross (Lemma SL4'.5)
    cube = mp.mpf('2.37')*R31**3/mp.sqrt(A)
    cross = (mp.mpf('2.13')*R31*R42 + mp.mpf('0.56')*R42**2)/mp.sqrt(A)
    # mid numerator + denominator (Lemma SL4'.4(i)), Mills from a = lam/2
    midn = SQ2PI/mp.pi*A**mp.mpf('1.5')/(4*g)*mp.e**(-g*A/4)*(1 + 2/(g*A))
    midd = SQ2PI/mp.pi*mp.sqrt(A)/g*mp.e**(-g*A/4)
    return r5n + r5d + cube + cross + midn + midd

def w6x(w, tau, m):
    # wp1-c Clause W.6 exponent (per-m): x = ((M-1)/(2M))(log(1+s/S) - s/(SM))
    lam = w/m; t = tau*lam
    M = m*mp.sin(t/2); s = mp.sin(t/2)**2; S = mp.sinh(lam/2)**2
    if M <= 1: return mp.mpf(0)
    return max((M-1)/(2*M)*(mp.log(1+s/S) - s/(S*M)), mp.mpf(0))

def X_slot(w, m, A):
    # left-endpoint upper sums over 60 cells of [0.8, tau0/lam] (SL4'-X device),
    # t^2 at the right endpoint (safe for the increasing factor)
    lam = w/m; tau0 = 2*mp.asin(mp.sinh(lam/2))/lam
    n = 60; h = (tau0 - mp.mpf('0.8'))/n
    sn = sd = mp.mpf(0)
    for i in range(n):
        a = mp.mpf('0.8') + i*h
        E = m*w6x(w, a, m)
        sn += h*lam*((a+h)*lam)**2*mp.e**(-E)
        sd += h*lam*mp.e**(-E)
    s2 = A/lam**2
    Xn = A*SQ2PI/mp.pi*s2**mp.mpf('1.5')*sn
    Xd = A*SQ2PI/mp.pi*mp.sqrt(s2)*sd
    return Xn, Xd

def far_slot(m):
    # Lemma SL4'.4(iii) at A = m, band-left lam = 4/m
    lam = mp.mpf(4)/m; s2max = m/(4*mp.sinh(lam/2)**2)
    Fn = 2*SQ2PI*m*s2max**mp.mpf('1.5')*mp.e**(-FAREXP*m)
    Fd = m*mp.sqrt(2*mp.pi*s2max)*mp.e**(-FAREXP*m)
    return Fn, Fd

def w1row(m, w, g=GAM, C5v=C5):
    A0 = CAD*m
    lammax = mp.mpf(5)/m
    main = R42/2 + mp.mpf('0.3')*R31**2 + lammax**2/2
    dec = main + INFL*dec_entries(A0, g, C5v)
    Xn, Xd = X_slot(w, mp.mpf(m), mp.mpf(m))
    Fn, Fd = far_slot(m)
    share = dec/(20*CAD) + (INFL*(Xn+Xd) + INFL*(Fn+Fd))/20
    return share*(1+QUADF)

print("== [A1] trapezoid boundary (independent rebuild from draft closed forms) ==")
for m, wv in ((401, '4.095'), (401, '4.094'), (462, '4.00021'), (462, '4.00020'),
              (461, '4.002'), (461, '4.001')):
    t = w1row(m, mp.mpf(wv))
    print(f"  row({m}, {wv}) = {mp.nstr(t, 7)}  {'PASS' if t <= 1 else 'FAIL'}")
weps = mp.mpf(4) + mp.mpf('1e-9')
for m in (461, 462, 463, 464):
    t = w1row(m, weps)
    print(f"  row({m}, 4+1e-9) = {mp.nstr(t, 7)}  {'PASS' if t <= 1 else 'FAIL'}")

print("\n== [A2] Fact R.G sentinels (independent) ==")
for m in (561, 699):
    t = w1row(m, weps)
    print(f"  row({m}, 4+1e-9) = {mp.nstr(t, 7)}   [prover: 0.424939 / 0.261345]")

print("\n== [A3] named-constant roundings (exact) ==")
print(f"  48 sqrt(2pi)/pi = {mp.nstr(48*SQ2PI/mp.pi, 10)} <= 38.2985: {48*SQ2PI/mp.pi <= mp.mpf('38.2985')}")
print(f"  2.3641 cube exact = {mp.nstr(mp.mpf(3840)/1296*SQ2PI/mp.pi, 8)} <= 2.37: "
      f"{mp.mpf(3840)/1296*SQ2PI/mp.pi <= mp.mpf('2.37')}")
print(f"  2.1277 cross exact = {mp.nstr(mp.mpf(384)/144*SQ2PI/mp.pi, 8)} <= 2.13: "
      f"{mp.mpf(384)/144*SQ2PI/mp.pi <= mp.mpf('2.13')}")
print(f"  4(1-e^-1/4) = {mp.nstr(4*(1-mp.e**mp.mpf('-0.25')), 9)}  (F5 boundary)")
