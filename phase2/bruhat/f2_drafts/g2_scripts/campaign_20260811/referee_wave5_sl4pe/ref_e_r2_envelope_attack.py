#!/usr/bin/env python3
# ref_e_r2_envelope_attack.py -- REFEREE (numerics, wave-5 sl4pe): end-to-end
# falsification attack on Theorem E / Lemma E.2.  For hypothesis-consistent
# tuples (m, lam, s2, k3, k4) -- corners engineered to sit ON the (E1)/(E2)/
# (E3) boundaries at the A-floor, plus random draws -- compute eta from the
# closed forms (independent qhat implementation, dps 60) and test:
#   (a) the envelope  |eta/u - (lam^2/2 + r42/2 - r31^2)| <= REM*(W) (exact);
#   (b) the pricing   |eta| <= [R42*/2 + 0.3 R31*^2 + lam^2/2] u ;
#   (c) Lemma E.1(i)&(iii): direct-qhat eta == algebraic-form eta (agreement).
# A single violation of (a) or (b) at a consistent tuple REFUTES the theorem.
import mpmath as mp
from fractions import Fraction as Fr
import random
mp.mp.dps = 60
random.seed(561)

BANDS = {'W1': (Fr(28,100), Fr(1),     Fr(4,5),  (4, 5)),
         'W2': (Fr(35,100), Fr(6,5),   Fr(7,5),  (5, 6)),
         'W3': (Fr(42,100), Fr(3,2),   Fr(13,5), (6, 8)),
         'W4': (Fr(52,100), Fr(17,10), Fr(7,2),  (8, 10)),
         'W5': (Fr(3,5),    Fr(2),     Fr(26,5), (10, 20)),
         'W6b':(Fr(7,10),   Fr(21,10), Fr(6),    (20, 40)),
         'W7': (Fr(4,5),    Fr(11,5),  Fr(33,5), (40, None))}
S0 = Fr(1122800, 7921)

# exact REM* recomputed by ref_e_r1 (verified == archived J0 fractions)
def certs(W):
    cA, R31, R42, _ = BANDS[W]
    E0 = Fr(1)/S0; M0 = 561
    A0 = cA*M0
    wmax = {'W1':Fr(5),'W2':Fr(6),'W3':Fr(8),'W4':Fr(10),'W5':Fr(20),'W6b':Fr(40)}.get(W)
    Lam = wmax/M0 if wmax is not None else Fr(89,100)
    Jst = R42/2 + Fr(3,10)*R31**2
    R42d = max(R42, 2*Jst)
    bb = R42d/(24*A0); aa = R31**2/(36*A0)
    xb = 3*bb + 15*(aa/2); sb = 6*bb + 30*(aa/2)
    db = 2*xb + xb*xb + 9*E0*aa
    ph = (E0/(1-E0) + db)/(1-db)
    e_b = max(6*(2+sb)/24 - Fr(1,2), Fr(1,2) - (6-E0)*(2-sb)/24)
    e_a = max(abs(9-(45-15*E0)*(1-sb/2)+36), abs(9-6*E0-45*(1+sb/2)+36))/36
    REM2 = (1+ph)*(e_b*R42d + e_a*R31**2) + ph*max(R42/2, Jst)
    d1 = Lam**2*E0/(6*(1-E0/4))
    REMs = REM2 + d1
    return Jst, Jst - REMs, REMs

def He(n, x):
    return {3: x**3-3*x, 4: x**4-6*x*x+3, 6: x**6-15*x**4+45*x*x-15}[n]

def eta_direct(s2, k3, k4):
    a = k3/(6*s2**mp.mpf('1.5')); b4 = k4/(24*s2**2); c6 = k3**2/(72*s2**3)
    def qh(d):
        z = d/mp.sqrt(s2)
        return (mp.e**(-d*d/(2*s2))/mp.sqrt(2*mp.pi*s2)) * \
               (1 + a*He(3,z) + b4*He(4,z) + c6*He(6,z))
    q0, qm, qp = qh(0), qh(-1), qh(1)
    assert qm > 0 and qp > 0, "qhat positivity violated"
    return s2*((q0*q0 - qm*qp)/(qm*qp)) - 1

def eta_algebraic(s2, k3, k4):
    eps2 = 1/s2
    a2 = k3**2/(36*s2**3); b4 = k4/(24*s2**2); c6 = a2/2
    h4 = 3 - 6*eps2 + eps2**2
    h6 = eps2**3 - 15*eps2**2 + 45*eps2 - 15
    h3sq = eps2*(3-eps2)**2
    N = 1 + 3*b4 - 15*c6
    D = (1 + b4*h4 + c6*h6)**2 - a2*h3sq
    return s2*(mp.e**eps2 * N*N/D - 1) - 1

viol = 0; ncase = 0; worst_env = mp.mpf(0); worst_pr = mp.mpf(0); worst_id = mp.mpf(0)
def case(W, m, w, s2, r31s, r42, tag):
    global viol, ncase, worst_env, worst_pr, worst_id
    ncase += 1
    _, R31, R42, _ = BANDS[W]
    Jst, J0, REMs = CERT[W]
    lam = mp.mpf(w)/m
    s2 = mp.mpf(s2)
    k3 = mp.sqrt(mp.mpf(r31s))*s2/lam          # sign irrelevant (a^2 only)
    k4 = mp.mpf(r42)*s2/lam**2
    A = lam*lam*s2; u = 1/A
    # hypothesis self-check
    assert s2 >= float(S0) - 1e-12 and A >= float(BANDS[W][0]*m) - 1e-9, (tag, "A2")
    assert mp.mpf(r31s) <= float(R31**2) + 1e-15 and mp.mpf(r42) <= float(R42) + 1e-15, (tag, "E1/E2")
    assert mp.mpf(r31s) - mp.mpf(r42)/2 <= float(J0) + 1e-12, (tag, "E3")
    e1v = eta_direct(s2, k3, k4)
    e2v = eta_algebraic(s2, k3, k4)
    idg = abs(e1v - e2v)/max(abs(e1v), mp.mpf(1))
    worst_id = max(worst_id, idg)
    env = abs(e1v/u - (lam*lam/2 + mp.mpf(r42)/2 - mp.mpf(r31s)))
    price = mp.mpf(float(R42))/2 + mp.mpf('0.3')*mp.mpf(float(R31))**2 + lam*lam/2
    fr_env = env/mp.mpf(float(REMs)); fr_pr = abs(e1v)/u/price
    worst_env = max(worst_env, fr_env); worst_pr = max(worst_pr, fr_pr)
    bad = fr_env > 1 or fr_pr > 1
    if bad:
        viol += 1
        print(f"  ** VIOLATION ** {tag} {W} m={m} w={w}: env/REM*={float(fr_env):.4f} "
              f"ratio={float(fr_pr):.4f}")
    return fr_env, fr_pr

CERT = {W: certs(W) for W in BANDS}
print("== referee r2: envelope + pricing attack at hypothesis-boundary corners ==")
for W, (cA, R31, R42, (wlo, whi)) in BANDS.items():
    Jst, J0, REMs = CERT[W]
    for m in (561, 562, 600, 5000):
        whi_m = whi if whi is not None else 0.89*m
        for w in (wlo + 1e-9 if wlo == 4 else wlo + 1e-6, (wlo + float(whi_m))/2, float(whi_m)):
            if w/m > 0.89 + 1e-15: continue
            lam = w/m
            for Afac in (1, 10, 10**4):
                s2 = float(cA*m)*Afac/lam**2
                if s2 < float(S0): continue
                # corner C1: (E3) tight from r31 side
                case(W, m, w, s2, float(R31**2), float(2*(R31**2 - J0)), 'C1')
                # corner C2: (E3) tight, most-negative r42
                case(W, m, w, s2, 0.0, float(-2*J0), 'C2')
                # corner C3: (E2) tight, r31 = 0
                case(W, m, w, s2, 0.0, float(R42), 'C3')
                # corner C4: (E1)+(E2) tight jointly
                case(W, m, w, s2, float(R31**2), float(R42), 'C4')
                # random interior draws
                for _ in range(3):
                    r31s = random.random()*float(R31**2)
                    lo = float(2*(r31s - float(J0)))
                    r42 = lo + random.random()*(float(R42) - lo)
                    case(W, m, w, s2, r31s, r42, 'RND')
print(f"  cases run: {ncase};  VIOLATIONS: {viol}")
print(f"  worst envelope fraction |eta/u - main|/REM* = {float(worst_env):.6f}")
print(f"  worst pricing ratio |eta|/(price u)         = {float(worst_pr):.6f}")
print(f"  worst E.1(i)-vs-direct eta relative gap     = {float(worst_id):.3e}")

print()
print("== Prop E.3 point, independent recomputation (dps 60) ==")
m = 561; w = mp.mpf('4.5'); lam = w/m
A0 = mp.mpf('0.28')*m
s2x = A0/lam**2
k3x = s2x/lam; k4x = mp.mpf(0)
e_d = eta_direct(s2x, k3x, k4x); e_a2 = eta_algebraic(s2x, k3x, k4x)
u = 1/(lam*lam*s2x)
price = mp.mpf('0.4') + mp.mpf('0.3') + lam*lam/2
print(f"  eta/u (direct)    = {mp.nstr(e_d/u, 12)}")
print(f"  eta/u (algebraic) = {mp.nstr(e_a2/u, 12)}")
print(f"  price = {mp.nstr(price, 9)};  |eta|/(price*u) = {mp.nstr(abs(e_d)/u/price, 8)}")
print(f"  hypothesis check: s2 >= S0: {s2x >= float(S0)}; A = {mp.nstr(lam*lam*s2x, 8)} "
      f">= 0.28*561 = 157.08: True; r31 = 1.0 = R31*(W1); r42 = 0; k4 >= 0")
