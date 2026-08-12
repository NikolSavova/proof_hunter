#!/usr/bin/env python3
# SL4 numeric certification script (wave 3, wp4).  All claims quoted in
# wp4_sl_SL4.md come from THIS file's printed output.
# Parts:
#  A. Hermite closed forms for qhat(d) and the exact eta formula: verified
#     against direct mpmath quadrature of the model G, at real tilted-sum
#     cumulants (m=401, several w).  Also: eta leading-form check.
#  B. REFUTATION numbers: honest numerator-transfer sizes of the three tail
#     buckets under SL3-as-stated (gamma=1/8, W.6, W.5(ii) floor), at m=401.
#  C. Corrected honest band ledger at m=401 under strengthened hypotheses
#     (banded C5*, gamma*), with minimal closing constants per band; far
#     sliver boundary w_dagger(m); thresholds M*(band) under STATED SL1-SL3.
import mpmath as mp
mp.mp.dps = 40

# ---------- tilted factor cumulants (exact model: U_j on {0..j-1}, P~e^{-lam i})
def factor_cums(j, lam):
    # returns (mu, k2, k3, k4) of U_j^lam by direct summation (mp)
    ws = [mp.e**(-lam*i) for i in range(j)]
    Z = mp.fsum(ws)
    m1 = mp.fsum(i*w for i, w in enumerate(ws))/Z
    c2 = mp.fsum((i-m1)**2*w for i, w in enumerate(ws))/Z
    c3 = mp.fsum((i-m1)**3*w for i, w in enumerate(ws))/Z
    c4 = mp.fsum((i-m1)**4*w for i, w in enumerate(ws))/Z - 3*c2**2
    return m1, c2, c3, c4

def sum_cums(m, lam):
    mu = k2 = k3 = k4 = mp.mpf(0)
    for j in range(1, m+1):
        a, b, c, d = factor_cums(j, lam)
        mu += a; k2 += b; k3 += c; k4 += d
    return mu, k2, k3, k4

# ---------- Part A: qhat(d) Hermite closed form vs quadrature; eta formula
def He(n, x):
    if n == 3: return x**3 - 3*x
    if n == 4: return x**4 - 6*x**2 + 3
    if n == 6: return x**6 - 15*x**4 + 45*x**2 - 15
def qhat_closed(d, s2, k3, k4):
    g = mp.e**(-d*d/(2*s2))/mp.sqrt(2*mp.pi*s2)
    z = d/mp.sqrt(s2)
    a = k3/(6*s2**mp.mpf('1.5')); b4 = k4/(24*s2**2); c6 = k3**2/(72*s2**3)
    return g*(1 + a*He(3, z) + b4*He(4, z) + c6*He(6, z))
def qhat_quad(d, s2, k3, k4):
    f = lambda t: mp.e**(-s2*t*t/2)*(1 - 1j*k3*t**3/6 + k4*t**4/24
                                     - k3**2*t**6/72)*mp.e**(-1j*t*d)
    T = 12/mp.sqrt(s2)
    return mp.re(mp.quad(f, [-T, 0, T]))/(2*mp.pi)
def eta_closed(s2, k3, k4):
    q0 = qhat_closed(0, s2, k3, k4); qm = qhat_closed(-1, s2, k3, k4)
    qp = qhat_closed(1, s2, k3, k4)
    return s2*((q0*q0 - qm*qp)/(qm*qp))   # s2*Dhat/(qm qp) - ... = 1+eta => eta:
def run_A():
    print("== PART A: Hermite closed forms + eta ==")
    m = 401
    for w in ['4.5', '7', '30', '200']:
        lam = mp.mpf(w)/m
        mu, s2, k3, k4 = sum_cums(m, lam)
        A = lam*lam*s2; u = 1/A
        errs = [abs(qhat_closed(d, s2, k3, k4)/qhat_quad(d, s2, k3, k4)-1)
                for d in (-1, 0, 1)]
        e = eta_closed(s2, k3, k4) - 1
        lead = (s2*(mp.e**(1/s2)-1)-1) + k4/(2*s2**2) - k3**2/s2**3
        print(f" w={w}: lam={float(lam):.6f} s2={float(s2):.6e} A={float(A):.3f}"
              f" R31={float(abs(k3)*lam/s2):.4f} R42={float(k4*lam*lam/s2):.4f}")
        print(f"   closed-vs-quad qhat rel err max = {float(max(errs)):.3e}")
        print(f"   eta = {float(e):.6e} = {float(e/u):.5f} u ;"
              f" leading-form resid = {float(abs(e-lead)):.3e}"
              f" (= {float(abs(e-lead)/u**2):.4f} u^2)")
        print(f"   |eta| <= (R42/2 + max(R31^2, lam^2/2)) u ?"
              f" bound={float((k4*lam*lam/s2/2 + max((abs(k3)*lam/s2)**2, lam*lam/2))):.4f}"
              f" vs |eta|/u={float(abs(e)/u):.4f}")

# ---------- shared honest-entry formulas (all in u-units: contribution = entry*u)
SQ2PI = mp.sqrt(2*mp.pi)
def entry_num_R5(C5, A):        # numerator R5, kernel t^2/2 weight, e^1 inflation
    return 48*SQ2PI/mp.pi*C5*mp.e/mp.sqrt(A)          # = 38.30*C5*e/sqrt(A)... incl e
def entry_den_R5(C5, A):
    return 8*SQ2PI/mp.pi*C5*mp.e/mp.sqrt(A)           # = 6.38*C5*e/sqrt(A)
def entry_num_cube(R31, A):     # |x|^3/6 cube term, kernel-weighted
    return mp.mpf('2.37')*R31**3/mp.sqrt(A)
def entry_num_cross(R31, R42, A):   # k3k4 t^7/144 + k4^2 t^8/1152, kernel-weighted
    return (mp.mpf('2.13')*R31*R42 + mp.mpf('0.56')*R42**2)/mp.sqrt(A)
def entry_num_mid(gam, A):      # numerator mid tail from lam/2, Mills, kernel t^2/2
    # s2*q0*(1/pi)*int_{lam/2}^{.8lam} t^2 |phi| dt / g0^2 * A ;  |phi|<=e^{-gam s2 t^2}
    # int t^2 e^{-gam s2 t^2} <= (lam/(4 gam s2)) e^{-gam A/4} (1+ 2/(gam A)) for gam A>=4
    return SQ2PI/mp.pi*A**mp.mpf('1.5')/(2*gam)*mp.e**(-gam*A/4)*(1+2/(gam*A))
def entry_den_mid(gam, A):
    return 2/SQ2PI*mp.sqrt(A)/gam*mp.e**(-gam*A/4)
def w6_x(w, tau, m):            # W.6 exponent / m at t = tau*lam, lam = w/m (exact)
    lam = mp.mpf(w)/m; t = tau*lam
    M = m*mp.sin(t/2); s = mp.sin(t/2)**2; S = mp.sinh(lam/2)**2
    if M <= 1: return mp.mpf(0)
    val = (M-1)/(2*M)*(mp.log(1+s/S) - s/(S*M))
    return max(val, mp.mpf(0))
def entry_num_X(w, m, A):       # crossover numerator: fine subdivision of [0.8,tau0]
    lam = mp.mpf(w)/m
    tau0 = 2*mp.asin(mp.sinh(lam/2))/lam
    n = 60; h = (tau0 - mp.mpf('0.8'))/n; tot = mp.mpf(0)
    for i in range(n):
        a = mp.mpf('0.8') + i*h
        # W.6 exponent increasing in tau on this range (checked below): use left pt
        E = m*w6_x(w, a, m)
        tot += h*lam*((a+h)*lam)**2*mp.e**(-E)
    # contribution = s2*sqrt(2pi s2)*(1/pi)*(1/2)*tot*2 ... = (1/pi)sqrt(2pi)s2^1.5*tot/...
    s2 = A/lam**2
    return A*SQ2PI/mp.pi*s2**mp.mpf('1.5')*tot/2
def entry_den_X(w, m, A):
    lam = mp.mpf(w)/m
    tau0 = 2*mp.asin(mp.sinh(lam/2))/lam
    n = 60; h = (tau0-mp.mpf('0.8'))/n; tot = mp.mpf(0)
    for i in range(n):
        a = mp.mpf('0.8')+i*h
        tot += h*lam*mp.e**(-m*w6_x(w, a, m))
    s2 = A/lam**2
    return A*mp.sqrt(2*s2/mp.pi)*tot
def qW(w):                      # W.3d lower bound on q(M,1), M >= w/2
    M = mp.mpf(w)/2
    return (M-1)/(2*M)*(mp.log(2) - 1/M)
def entry_num_far(w, m, A, s2max):
    return A*SQ2PI*s2max**mp.mpf('1.5')*mp.e**(-m*qW(w))
def entry_den_far(w, m, A, s2max):
    return A*mp.sqrt(2*s2max/mp.pi)*mp.pi*mp.e**(-m*qW(w))

BANDS = [   # (name, wlo, whi, R31*, R42*, cA)
 ('W1', 4, 5, 1.0, 0.8, 0.28), ('W2', 5, 6, 1.2, 1.4, 0.35),
 ('W3', 6, 8, 1.5, 2.6, 0.42), ('W4', 8, 10, 1.7, 3.5, 0.52),
 ('W5', 10, 20, 2.0, 5.2, 0.60), ('W6b', 20, 40, 2.1, 6.0, 0.70),
 ('W7', 40, 400, 2.2, 6.6, 0.80)]

def s2cap(m):  # B.0(i) global cap
    return mp.mpf('1.05')*m**3/36

def band_total(bi, m, gam, C5, eps2=mp.mpf('0.10')):
    name, wlo, whi, R31, R42, cA = bi
    A = mp.mpf(cA)*m
    e_main = mp.mpf(R42)/2 + mp.mpf(R31)**2 + eps2
    e_R5n = entry_num_R5(mp.mpf(C5), A); e_R5d = entry_den_R5(mp.mpf(C5), A)
    e_cb = entry_num_cube(mp.mpf(R31), A)
    e_cr = entry_num_cross(mp.mpf(R31), mp.mpf(R42), A)
    e_mn = entry_num_mid(gam, A); e_md = entry_den_mid(gam, A)
    e_xn = entry_num_X(wlo+mp.mpf('0.05'), m, A)   # worst w = band left edge (+.05)
    e_xd = entry_den_X(wlo+mp.mpf('0.05'), m, A)
    e_fn = entry_num_far(wlo+mp.mpf('0.05'), m, A, s2cap(m))
    e_fd = entry_den_far(wlo+mp.mpf('0.05'), m, A, s2cap(m))
    den = e_R5d + e_md + e_xd + e_fd            # delta-entry (linear occurrence)
    # second-order: 2*s2*delta_box*Delta_tail-type handled: mixed quad term
    lam = mp.mpf(wlo)/m; s2 = A/lam**2
    quad = 3*(den/A)**2*mp.sqrt(s2)*A + 2*s2*(e_R5d/A)*( (e_md+e_xd)/A*0.8*lam \
            + 2*(e_fd/A))*A
    tot = e_main + e_R5n + e_cb + e_cr + e_mn + e_xn + e_fn + den + quad
    return tot, dict(main=e_main, R5n=e_R5n, cube=e_cb, cross=e_cr, midn=e_mn,
                     Xn=e_xn, farn=e_fn, den=den, quad=quad, budget=20*mp.mpf(cA))

def run_B():
    print("\n== PART B: refutation of the architected ledger normalization ==")
    m = 401
    for bi in BANDS[:3]:
        name, wlo, whi, R31, R42, cA = bi
        A = mp.mpf(cA)*m
        plan_mid = mp.mpf('3.19')*mp.sqrt(A)*mp.e**(-A/32)
        hon_mid = entry_num_mid(mp.mpf(1)/8, A)
        print(f" {name}: A={float(A):.1f}  plan mid entry={float(plan_mid):.3f}"
              f"  honest numerator mid entry (gamma=1/8)={float(hon_mid):.2f}"
              f"  ratio={float(hon_mid/plan_mid):.1f}")
    # far, W1 at m=401, with the TRUE W.5(ii) band exponent (W.3d at M=w/2):
    for w in ['4.05', '4.2', '4.5', '5.0']:
        e = entry_num_far(mp.mpf(w), m, mp.mpf('0.28')*m, s2cap(m))
        print(f" far numerator entry at w={w}, m=401 (u-units): {float(e):.4g}"
              f"   [m*qW = {float(m*qW(mp.mpf(w))):.2f}]")
    print(" (architected far entry 0.36*sqrt(A)*A*e^{-0.0373m} ="
          f" {float(mp.mpf('0.36')*mp.sqrt(112.3)*112.3*mp.e**(-mp.mpf('0.0373')*401)):.2e})")
    # W.6 exponent monotone-increase check on [0.8, tau0], w grid:
    bad = 0
    for w in ['4.05', '4.5', '5.5', '7', '9', '15', '30', '100', '356']:
        lam = mp.mpf(w)/m; tau0 = 2*mp.asin(mp.sinh(lam/2))/lam
        xs = [w6_x(mp.mpf(w), mp.mpf('0.8')+(tau0-mp.mpf('0.8'))*i/80, m)
              for i in range(81)]
        for i in range(80):
            if xs[i+1] < xs[i]: bad += 1
    print(f" W.6 exponent monotone-in-tau violations on [0.8,tau0] grid: {bad}")
    # W.6 x(w,tau) increasing in w check (fixed tau=0.8):
    ws = ['4.05','4.5','5','6','8','10','20','40','100','356']
    vals = [w6_x(mp.mpf(w), mp.mpf('0.8'), m) for w in ws]
    inc = all(vals[i+1] > vals[i] for i in range(len(vals)-1))
    print(f" W.6 x(w,0.8) increasing in w over grid: {inc};"
          f" x(4.05,.8)={float(vals[0]):.5f} -> E=m*x={float(m*vals[0]):.2f}")

def run_C():
    print("\n== PART C: corrected honest ledger ==")
    m = 401
    C5s = {'W1': '0.05', 'W2': '0.06', 'W3': '0.08', 'W4': '0.10',
           'W5': '0.15', 'W6b': '0.25', 'W7': '0.80'}
    gams = {'W1': '0.42', 'W2': '0.42', 'W3': '0.40', 'W4': '0.40',
            'W5': '0.38', 'W6b': '0.34', 'W7': '0.32'}
    print(" -- table at m=401, strengthened (C5*, gamma*) per band --")
    for bi in BANDS:
        name = bi[0]
        tot, d = band_total(bi, m, mp.mpf(gams[name]), mp.mpf(C5s[name]))
        ok = 'PASS' if tot <= d['budget'] else 'FAIL'
        print(f" {name}: C5*={C5s[name]} gam*={gams[name]} total={float(tot):.3f}"
              f" budget={float(d['budget']):.1f} {ok} | main={float(d['main']):.2f}"
              f" R5n={float(d['R5n']):.2f} cube={float(d['cube']):.2f}"
              f" cross={float(d['cross']):.2f} midn={float(d['midn']):.3f}"
              f" Xn={float(d['Xn']):.3f} farn={float(d['farn']):.3g}"
              f" den={float(d['den']):.3f} quad={float(d['quad']):.3f}")
    print(" -- far sliver boundary: smallest w with W1 row passing, vs m --")
    for m2 in [401, 420, 440, 460, 480, 500, 520, 540, 560]:
        wdag = None
        for i in range(0, 101):
            w = mp.mpf(4) + mp.mpf(i)/100
            bi = list(BANDS[0]); A = mp.mpf('0.28')*m2
            e_fn = entry_num_far(w, m2, A, s2cap(m2))
            e_xn = entry_num_X(w, m2, A)
            base_tot, d = band_total(BANDS[0], m2, mp.mpf('0.42'), mp.mpf('0.05'))
            # replace left-edge far+X entries by this w:
            tot = base_tot - d['farn'] - d['Xn'] + e_fn + e_xn
            if tot <= d['budget']:
                wdag = w; break
        print(f"  m={m2}: W1 row passes for w >= {float(wdag) if wdag else 'never'}")
    print(" -- thresholds M*(band) under STATED SL1-SL3 (C5=3 or 8, gamma=1/8) --")
    for bi in BANDS:
        name = bi[0]; C5 = mp.mpf(8 if name == 'W7' else 3)
        lo, hi = 401, 40000
        def ok(mm):
            tot, d = band_total(bi, mm, mp.mpf(1)/8, C5)
            return tot <= d['budget']
        if ok(lo):
            print(f"  {name}: closes already at m=401")
            continue
        if not ok(hi):
            print(f"  {name}: does not close by m=40000"); continue
        while hi-lo > 1:
            mid = (lo+hi)//2
            if ok(mid): hi = mid
            else: lo = mid
        print(f"  {name}: M* = {hi}  (stated SL1-SL3, honest assembly)")

if __name__ == '__main__':
    run_A(); run_B(); run_C()
