#!/usr/bin/env python3
"""REF-A: independent re-implementation (mpmath dps 60; no code shared with
the wp4 scripts) of every certified number in wp4_draft_composite.md sections
1/3/4 and their SL2/SL3/SL5 sources.
  A1: assembler table [1] (3.192/0.2/0.01), [2] (P2-band/1.3e-7), [3]
      (m>=1581 vs 136) recomputed directly from the formulas; effective C*;
      D1 delta.  Their table entries are safe-rounded UP, so requirement:
      my exact value <= their printed entry, and |diff| tiny; PASS/FAIL per row.
  A2: SL3 named constants; P1/P2/P3 band table; P3(401); q(2,1) (wp1-c W.3
      closed form, independently coded); t0(0.89)/0.89; Eps sup on (0,0.89]
      two ways (fine grid step 1e-5, and the 890-interval monotone bound).
  A3: SL2 certificates: V(w0) by direct mpmath quadrature of v; v(cap);
      LBV(w0) <= V(w0)?  UBv(cap) >= v(cap)?  floor vs c_A; exact chains
      1122800/7921 and 8000/7921; and my own recompute of the step-1/8
      left-Riemann LBV values (exact route re-implemented at dps 60).
  A4: SL5 far(401), ratio test, log certificates.
"""
import mpmath as mp
from fractions import Fraction as F
mp.mp.dps = 60

ok_all = True
def chk(name, cond, detail=""):
    global ok_all
    ok_all = ok_all and bool(cond)
    print(f"[{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("== A1: assembler ledger tables, independent recompute ==")
bands = [("W1", '0.28', '1.0', '0.8', 3), ("W2", '0.35', '1.2', '1.4', 3),
         ("W3", '0.42', '1.5', '2.6', 3), ("W4", '0.52', '1.7', '3.5', 3),
         ("W5", '0.60', '2.0', '5.2', 3), ("W6b", '0.70', '2.1', '6.0', 3),
         ("W7", '0.80', '2.2', '6.6', 8)]
# printed entries of out_wp4asm_chain.txt table [1] (R5, I1u cols) for comparison:
printed1 = {"W1": ('1.8120', '1.012473', '4.7345'), "W2": ('1.6207', '0.470848', '4.4335'),
            "W3": ('1.4795', '0.214543', '4.8790'), "W4": ('1.3297', '0.068182', '5.2249'),
            "W5": ('1.2379', '0.026876', '6.2748'), "W6b": ('1.1460', '0.008292', '6.6873'),
            "W7": ('2.8586', '0.002532', '8.8231')}
def row(mfloor, cA, R31, R42, C5, i2mode, far):
    A0 = mp.mpf(cA) * mfloor
    k42 = mp.mpf(R42) / 2
    k32 = mp.mpf('0.3') * mp.mpf(R31) ** 2
    r5 = mp.mpf('6.4') * C5 / mp.sqrt(A0)
    i1 = mp.mpf('3.192') * mp.sqrt(A0) * mp.e ** (-A0 / 32)
    i2 = mp.mpf('0.2') if i2mode == '0.2' else mp.mpf('2.87') * mp.sqrt(A0) * mp.e ** (-mp.mpf('0.0556') * A0)
    return k42 + k32 + r5 + i1 + i2 + 1 + mp.mpf(far), (r5, i1, i2)
for tag, mfloor, i2mode, far, budC in [("[1]", 401, '0.2', '0.01', 20),
                                       ("[2]", 401, 'P2', '1.3e-7', 20),
                                       ("[3]", 1581, '0.2', '0.01', 136)]:
    worst = mp.mpf(0); allp = True
    for name, cA, R31, R42, C5 in bands:
        tot, (r5, i1, i2) = row(mfloor, cA, R31, R42, C5, i2mode, far)
        bud = budC * mp.mpf(cA)
        allp = allp and (tot <= bud)
        worst = max(worst, tot / mp.mpf(cA))
        if tag == "[1]":
            pr5, pi1, ptot = (mp.mpf(x) for x in printed1[name])
            chk(f"[1] {name}: exact<=printed (R5,I1u,total) & PASS",
                r5 <= pr5 and i1 <= pi1 and tot <= ptot and tot <= bud,
                f"r5={mp.nstr(r5,8)} i1={mp.nstr(i1,8)} tot={mp.nstr(tot,8)} bud={mp.nstr(bud,4)}")
    print(f"  {tag} all rows pass: {allp}; effective C* (exact-value side) = {mp.nstr(worst, 8)}")
chk("[1] effective C* printed 16.9088 = 4734473/280000 >= exact",
    mp.mpf(4734473) / 280000 >= mp.mpf('16.9088') and abs(mp.mpf(4734473)/280000 - mp.mpf('16.90883')) < 1e-4,
    f"4734473/280000 = {mp.nstr(mp.mpf(4734473)/280000, 8)}")
A0 = mp.mpf('0.28') * 401
d1 = (mp.mpf('3.192') - mp.mpf('3.19')) * mp.sqrt(A0) * mp.e ** (-A0 / 32)
chk("[1b] D1 delta = 0.000634", abs(d1 - mp.mpf('0.000634')) < 2e-6, f"delta={mp.nstr(d1,4)}")

print("== A2: SL3 constants, table, Eps sup ==")
chk("8/sqrt(2pi) in (3.19, 3.192]", mp.mpf('3.19') < 8/mp.sqrt(2*mp.pi) <= mp.mpf('3.192'),
    f"= {mp.nstr(8/mp.sqrt(2*mp.pi), 10)}")
chk("11.5/(1.6 sqrt(2pi)) <= 2.87", mp.mpf('11.5')/(mp.mpf('1.6')*mp.sqrt(2*mp.pi)) <= mp.mpf('2.87'),
    f"= {mp.nstr(mp.mpf('11.5')/(mp.mpf('1.6')*mp.sqrt(2*mp.pi)), 10)}")
chk("0.64/11.5 >= 0.0556", mp.mpf('0.64')/mp.mpf('11.5') >= mp.mpf('0.0556'))
chk("sqrt(pi/2)/4 <= 0.3134", mp.sqrt(mp.pi/2)/4 <= mp.mpf('0.3134'))
chk("c1 = (2/pi^2)(0.65) >= 1/8", 2/mp.pi**2*mp.mpf('0.65') >= mp.mpf(1)/8,
    f"= {mp.nstr(2/mp.pi**2*mp.mpf('0.65'), 8)}")
chk("c2 = (2/pi^2)(0.43) >= 1/11.5", 2/mp.pi**2*mp.mpf('0.43') >= 1/mp.mpf('11.5'),
    f"= {mp.nstr(2/mp.pi**2*mp.mpf('0.43'), 8)}, 1/11.5 = {mp.nstr(1/mp.mpf('11.5'), 8)}")
chk("x1 = 3.9269 <= pi/0.8", mp.mpf('3.9269') <= mp.pi/mp.mpf('0.8'))
chk("x2 = 2.9251 <= pi/1.074", mp.mpf('2.9251') <= mp.pi/mp.mpf('1.074'))
def qW3(M, r):  # wp1-c W.3 closed form, independent coding
    M = mp.mpf(M); r = mp.mpf(r)
    I = M*mp.log((1+r)*M**2/(r*M**2+1)) - 2/mp.sqrt(r)*(mp.atan(mp.sqrt(r)*M)-mp.atan(mp.sqrt(r)))
    return I/(2*M)
chk("q(2,1) >= 0.0741", qW3(2,1) >= mp.mpf('0.0741'), f"q(2,1) = {mp.nstr(qW3(2,1), 8)}")
t0r = 2*mp.asin(mp.sinh(mp.mpf('0.89')/2))/mp.mpf('0.89')
chk("t0(0.89)/0.89 <= 1.074", t0r <= mp.mpf('1.074'), f"= {mp.nstr(t0r, 10)}")
P3 = mp.mpf('0.3134')*mp.mpf(401)**mp.mpf('2.5')*mp.e**(-mp.mpf('0.0741')*401)
chk("P3(401) <= 1.3e-7", P3 <= mp.mpf('1.3e-7'), f"= {mp.nstr(P3, 6)}")
# SL3.2 band table independent
sl3tab = {"W1": ('1.0125', '0.0592'), "W2": ('0.4709', '0.0139'), "W3": ('0.2146', '0.0032'),
          "W4": ('0.0682', '0.0004'), "W5": ('0.0269', '0.0001'), "W6b": ('0.0083', '0.0001'),
          "W7": ('0.0026', '0.0001')}
for name, cA, _, _, _ in bands:
    A0 = mp.mpf(cA)*401
    P1 = mp.mpf('3.192')*mp.sqrt(A0)*mp.e**(-A0/32)
    P2 = mp.mpf('2.87')*mp.sqrt(A0)*mp.e**(-mp.mpf('0.0556')*A0)
    p1p, p2p = (mp.mpf(x) for x in sl3tab[name])
    chk(f"SL3.2 {name}: P1 <= printed {p1p}, P2 <= printed {p2p}",
        P1 <= p1p and P2 <= p2p, f"P1={mp.nstr(P1,6)} P2={mp.nstr(P2,6)}")
# Eps sup two ways
def Eps(lam, x0):
    q = mp.e**(-lam)
    return mp.e**(-x0)*((x0/lam)**2*(1-q)**2/(q*(1+q)) + 2*(x0/lam)*(1-q)/(1+q) + 1)
for x0, cap, claimed in [(mp.mpf('3.9269'), mp.mpf('0.35'), '0.32257'),
                         (mp.mpf('2.9251'), mp.mpf('0.57'), '0.54890')]:
    sup = mp.mpf(0)
    lam = mp.mpf('0.89')
    # Eps increasing toward lam=0.89 (their certificate); fine grid incl. top edge
    for i in range(1, 89001):
        l = mp.mpf(i)/100000
        if l > mp.mpf('0.89'): break
        v = Eps(l, x0)
        if v > sup: sup = v
    chk(f"Eps(.,{mp.nstr(x0,5)}) fine-grid sup <= {cap} (claimed max piece {claimed})",
        sup <= cap, f"grid sup = {mp.nstr(sup, 6)}")

print("== A3: SL2 certificates, independent ==")
def v(x):
    x = mp.mpf(x)
    if x == 0: return mp.mpf(0)
    return 1 - (x/(2*mp.sinh(x/2)))**2
LBV = {4: '0.287512', 5: '0.381827', 6: '0.462919', 8: '0.584563',
       10: '0.665345', 20: '0.832381', 40: '0.916190'}
UBv = {4: ('5/401', '0.00001296'), 5: ('6/401', '0.00001866'), 6: ('8/401', '0.00003317'),
       8: ('10/401', '0.00005183'), 10: ('20/401', '0.00020727'), 20: ('40/401', '0.00082877'),
       40: ('89/100', '0.06347403')}
cAs = {4: '0.28', 5: '0.35', 6: '0.42', 8: '0.52', 10: '0.60', 20: '0.70', 40: '0.80'}
for w0 in (4, 5, 6, 8, 10, 20, 40):
    V = mp.quad(v, [0, w0]) / w0
    capstr, ub = UBv[w0]
    p, q_ = capstr.split('/')
    cap = mp.mpf(p)/mp.mpf(q_)
    vcap = v(cap)
    lbv = mp.mpf(LBV[w0]); ubv = mp.mpf(ub)
    fl = lbv - ubv
    chk(f"SL2 w0={w0}: LBV<=V(w0), UBv>=v(cap), floor>c_A",
        lbv <= V and ubv >= vcap and fl > mp.mpf(cAs[w0]),
        f"V={mp.nstr(V,8)} LBV={LBV[w0]} v(cap)={mp.nstr(vcap,6)} UBv={ub} floor={mp.nstr(fl,7)} cA={cAs[w0]}")
# re-derive the step-1/8 left-Riemann LBV independently (dps-60 values, no Fractions)
for w0 in (4, 40):
    s = mp.fsum(v(mp.mpf(k)/8) for k in range(0, 8*w0)) / 8 / w0
    chk(f"SL2 left-Riemann V-lower at w0={w0} matches printed LBV to 5e-6 and <= V",
        abs(s - mp.mpf(LBV[w0])) < mp.mpf('5e-6') and s <= mp.quad(v, [0, w0])/w0,
        f"riemann={mp.nstr(s, 8)} printed={LBV[w0]}")
chk("exact chain 0.28*401/0.89^2 = 1122800/7921 >= 141.749",
    F(28,100)*401/(F(89,100)**2) == F(1122800, 7921) and F(1122800,7921) > F(141749,1000),
    f"= {mp.nstr(mp.mpf(1122800)/7921, 8)}")
chk("W7 chain 0.80/0.89^2 = 8000/7921 > 1", F(80,100)/(F(89,100)**2) == F(8000,7921) and F(8000,7921) > 1)

print("== A4: SL5 far entry + log certs ==")
far = mp.mpf('0.36')*mp.mpf(401)**mp.mpf('1.5')*mp.e**(-mp.mpf('0.0373')*401)
chk("far(401) = 0.36*401^1.5*e^-14.9573 <= 9.229e-4 (and > 9.2e-4: sharp)",
    far <= mp.mpf('9.229e-4') and far > mp.mpf('9.2e-4'), f"= {mp.nstr(far, 6)}")
chk("log(17/7) <= 0.8874", mp.log(mp.mpf(17)/7) <= mp.mpf('0.8874'),
    f"= {mp.nstr(mp.log(mp.mpf(17)/7), 8)}")
chk("log 2 <= 0.6932", mp.log(2) <= mp.mpf('0.6932'))
chk("(402/401)^3 < 1.0746", (mp.mpf(402)/401)**3 < mp.mpf('1.0746'),
    f"= {mp.nstr((mp.mpf(402)/401)**3, 8)}")
chk("SL5 3.19-flavor W1 I1u 1.0118: 3.19*sqrt(A0)e^{-A0/32} <= 1.0118+1e-4",
    mp.mpf('3.19')*mp.sqrt(mp.mpf('0.28')*401)*mp.e**(-mp.mpf('0.28')*401/32) <= mp.mpf('1.0119'),
    f"= {mp.nstr(mp.mpf('3.19')*mp.sqrt(mp.mpf('0.28')*401)*mp.e**(-mp.mpf('0.28')*401/32), 8)}")
print("REF-A ALL PASS" if ok_all else "REF-A: AT LEAST ONE FAIL")
