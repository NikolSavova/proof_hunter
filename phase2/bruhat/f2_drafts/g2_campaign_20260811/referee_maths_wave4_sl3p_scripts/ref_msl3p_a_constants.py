# ref_msl3p_a_constants.py — MATHS referee, wave4_sl3p (Stage 2).
# Independent re-derivation (mpmath dps 30, quadrature-based, code shared with
# nothing under wave4_sl3p/) of: every named constant of wave4_sl3p_20260812.md
# §1; the E.5.3 budget/threshold table (b, q, tau_c', tau_start, analytic
# margin at tau_start); high-precision recomputation of every band's printed
# WORST CELL bound; true delta_norm at those cells (direction sanity);
# E.6.A worst cell; E.6.B worst (lam,tau)-cell full x-sweep; E.4b corner truth.
# Output: out_ref_msl3p_a.txt. 2026-08-12.
import mpmath as mp
mp.mp.dps = 30

pi = mp.pi
def h(x):
    x = mp.mpf(x)
    if x == 0: return mp.mpf(1)
    return (x/2)**2/mp.sinh(x/2)**2
def psi(x, tau):
    x = mp.mpf(x); tau = mp.mpf(tau)
    if x == 0: return tau**2
    return mp.sin(tau*x/2)**2/mp.sinh(x/2)**2
def F(x, tau, gam):
    return mp.log(1+psi(x, tau)) - 2*gam*tau**2*h(x)

print("=== referee maths wave4_sl3p, script A (dps 30) ===")

# --- named constants of §1 ---
Cenv = 4/(1-mp.e**(-2*pi))**2
print(f"[1] C_env true = {mp.nstr(Cenv,10)}  <= 4.04: {Cenv <= mp.mpf('4.04')}")
epshat_true = mp.mpf('1.03')*mp.e**(-2*pi/mp.mpf('0.8'))/mp.mpf('0.64')
print(f"[1] eps_env(0.8)/0.64 = {mp.nstr(epshat_true,10)}  <= 6.25e-4: {epshat_true <= mp.mpf('6.25e-4')}")
Ih = mp.quad(h, [0, pi/mp.mpf('0.8')])
print(f"[1] I_h true (quad) = {mp.nstr(Ih,12)}  >= 2.7: {Ih >= mp.mpf('2.7')}  (script right-sum said 2.784022)")
cB = (4/pi**2)*(1/mp.mpf('1.64'))*mp.mpf('2.7')*(2*pi)**2
print(f"[1] c_B = {mp.nstr(cB,8)} ; 4.04 (2pi)^3 e^-2pi = {mp.nstr(mp.mpf('4.04')*(2*pi)**3*mp.e**(-2*pi),8)} < c_B: {mp.mpf('4.04')*(2*pi)**3*mp.e**(-2*pi) < cB}")
eps_t = 1/mp.sinh(mp.mpf('3.925'))**2
print(f"[1] eps_t = {mp.nstr(eps_t,10)}  <= 1.57e-3: {eps_t <= mp.mpf('1.57e-3')} ; 7.85 < 2pi/0.8 = {mp.nstr(2*pi/mp.mpf('0.8'),10)}: {mp.mpf('7.85') < 2*pi/mp.mpf('0.8')}")
for g in ['0.32','0.34','0.38','0.40','0.42']:
    K1 = (mp.mpf('1.65') - mp.mpf('1.98')*mp.mpf(g))/12
    print(f"[1] K1'({g}) = {mp.nstr(K1,6)}")

# --- E.4b corner truth (lam=0.3, tau=0.8, worst gamma=0.32) ---
for g in ['0.32','0.42']:
    gam = mp.mpf(g); K1 = (mp.mpf('1.65') - mp.mpf('1.98')*gam)/12
    worst = mp.mpf(0)
    for lam in ['0.3','0.29','0.2','0.1','0.05']:
        for tau in ['0.8','0.79','0.6','0.4','0.2','0.05']:
            lam_, tau_ = mp.mpf(lam), mp.mpf(tau)
            F0 = mp.log(1+tau_**2) - 2*gam*tau_**2
            r = (F0 - F(lam_, tau_, gam))/(K1*tau_**2*lam_**2)
            worst = max(worst, r)
    print(f"[2] E.4b corner-spot max ratio (gamma={g}) = {mp.nstr(worst,6)}  <= 1: {worst <= 1}")

# --- avg_h and avg_g helpers (true integrals) ---
def avg_h(w):
    return mp.quad(h, [0, w])/w
def avg_g(w, tau, arch=True):
    # split at first arch end 2pi/tau if inside
    X = 2*pi/tau
    pts = [0, min(w, pi/tau)]
    z = pi/tau
    while z < w:
        pts.append(min(w, z+pi/tau)); z += pi/tau
    pts = sorted(set([float(p) for p in pts]))
    tot = mp.mpf(0)
    for a, b in zip(pts[:-1], pts[1:]):
        tot += mp.quad(lambda x: mp.log(1+psi(x, tau)), [a, b])
    return tot/w
def delta_norm(w, tau, gam):
    N = mp.log(1+tau**2) - avg_g(w, tau)
    return N/tau**2 - 2*gam*(1-avg_h(w))

# --- E.5.3 table: b, q, tau_c', tau_start, analytic margin, worst cells ---
print("[3] E.5.3 independent table  (q_true = 1-avg_h(w_bot) by quad; printed q must be <= q_true)")
BANDS = [("W1", '4.0', '5.0', '0.42', mp.mpf(5)/401, ('4.0','0.415','0.4175')),
         ("W2", '5.0', '6.0', '0.42', mp.mpf(6)/401, ('5.995','0.7975','0.8')),
         ("W3", '6.0', '8.0', '0.40', mp.mpf(8)/401, ('7.99','0.7975','0.8')),
         ("W4", '8.0', '10.0', '0.40', mp.mpf(10)/401, ('9.99','0.7975','0.8')),
         ("W5", '10.0', '20.0', '0.38', mp.mpf(20)/401, ('19.98','0.7975','0.8')),
         ("W6b", '20.0', '40.0', '0.34', mp.mpf(40)/401, ('39.96','0.7975','0.8')),
         ("W7", '40.0', None, '0.32', mp.mpf('0.30'), ('40.0','0.7275','0.73'))]
PRINTED = {"W1": ('0.002730','0.29825','0.4215','0.4150',0.036055),
           "W2": ('0.002735','0.39208','0.4251','0.4200',0.036214),
           "W3": ('0.002648','0.47231','0.4912','0.4850',0.041498),
           "W4": ('0.002664','0.59214','0.4930','0.4875',0.028654),
           "W5": ('0.002706','0.67152','0.5557','0.5500',0.032532),
           "W6b": ('0.003131','0.83548','0.6801','0.6750',0.094264),
           "W7": ('0.009844','0.91774','0.7326','0.7275',0.078395)}
for name, w1, w2, g, lmax, wc in BANDS:
    gam = mp.mpf(g); K1 = (mp.mpf('1.65') - mp.mpf('1.98')*gam)/12
    b = K1*lmax**2 + mp.mpf('6.25e-4') + 2*gam/401
    qtrue = 1 - avg_h(mp.mpf(w1))
    pb, pq, ptc, pts_, pdmin = PRINTED[name]
    ok_q = mp.mpf(pq) <= qtrue
    tauc = mp.sqrt(1/(2*gam + b/mp.mpf(pq)) - 1)
    ts = mp.mpf(pts_)
    ana = mp.mpf(pq)*(1/(1+ts**2) - 2*gam)
    print(f"  {name:3s}: b = {mp.nstr(b,7)} (printed {pb}); q_true = {mp.nstr(qtrue,7)} printed<=true: {ok_q}; "
          f"tau_c' = {mp.nstr(tauc,6)} (printed {ptc}); ana(tau_start)={mp.nstr(ana,6)} margin ana/b = {mp.nstr(ana/b,5)}x")

# worst-cell recomputation, independent construction (true integrals of the
# same majorant, so my value should sit AT OR ABOVE the script's Riemann-loss
# value, and BELOW true delta_norm):
print("[4] worst cells: independent bound value vs printed min delta_cert vs TRUE delta_norm")
def g_ub(x, t2):
    x = mp.mpf(x)
    if x <= pi/t2:
        return mp.log(1+psi(x, t2))
    return mp.log(1+min(t2**2*h(x), 1/mp.sinh(x/2)**2))
for name, w1, w2, g, lmax, wc in BANDS:
    gam = mp.mpf(g)
    w1c, t1, t2 = (mp.mpf(v) for v in wc)
    Ag = mp.quad(lambda x: g_ub(x, t2), [0, min(w1c, pi/t2)] + ([w1c] if w1c > pi/t2 else []))/w1c
    num = mp.log(1+t1**2) - Ag
    if w2 is None:
        sub = 2*gam
        w2c = w1c   # true delta at w1c
    else:
        dwmap = {"W1":'0.005', "W2":'0.005', "W3":'0.01', "W4":'0.01', "W5":'0.02', "W6b":'0.04'}
        w2c = w1c + mp.mpf(dwmap[name])
        sub = 2*gam*(1-avg_h(w2c))
    dc_true_integrals = num/t2**2 - sub
    dtrue = delta_norm(w1c if w2 is not None else mp.mpf('40'), t1, gam)
    pdmin = PRINTED[name][4]
    print(f"  {name:3s}: cell({mp.nstr(w1c,6)},{mp.nstr(t1,4)},{mp.nstr(t2,4)}): my cell bound (true-integral) = {mp.nstr(dc_true_integrals,6)}; "
          f"printed = {pdmin}; printed <= mine+2e-4: {mp.mpf(pdmin) <= dc_true_integrals + mp.mpf('2e-4')}; "
          f"TRUE delta_norm at (w1c,t1) = {mp.nstr(dtrue,6)}; printed <= true: {mp.mpf(pdmin) <= dtrue}")

# --- E.6.A worst cell, dps 30 ---
gam = mp.mpf('0.32'); t0 = mp.mpf('0.58')
l1, l2 = mp.mpf('0.8875'), mp.mpf('0.89')
lhs = (h(l2)-h(2*l1))*(1 - 2*gam - 2*gam*t0**2)
rhs = h(l1)*t0**2*l2**2/12
print(f"[5] E.6.A worst cell [0.8875,0.89]: lhs/rhs = {mp.nstr(lhs/rhs,6)}  (printed 1.1294)  >=1: {lhs >= rhs}")
# and the true pointwise C at lam=0.89:
lam = mp.mpf('0.89')
Cm = (h(lam)-h(2*lam))*(1-2*gam-2*gam*t0**2)/(h(lam)*t0**2*lam**2/12)
print(f"    pointwise C-margin at lam=0.89: {mp.nstr(Cm,6)} (script A(i) said 1.1374)")

# --- E.6.B worst (lam,tau) cell: full x sweep, dps 30 ---
la, lb = mp.mpf('0.30'), mp.mpf('0.3002')
t1, t2 = mp.mpf('0.58'), mp.mpf('0.5805')
Flb = mp.log(1+mp.sin(t1*la/2)**2/mp.sinh(lb/2)**2) - 2*gam*t2**2*h(la)
# x-cells as in the script
xs = []
z = 2*la
while z < 2*la+mp.mpf('0.4') - mp.mpf('1e-15'):
    xs.append(z); z += mp.mpf('0.005')
z = 2*la+mp.mpf('0.4')
while z < 4 - mp.mpf('1e-15'):
    xs.append(z); z += mp.mpf('0.01')
z = mp.mpf('4.0')
while z < mp.mpf('7.85') - mp.mpf('1e-15'):
    xs.append(z); z += mp.mpf('0.02')
xs.append(mp.mpf('7.85'))
worstF = mp.mpf('-1e9'); wx = None
for i in range(len(xs)-1):
    x1, x2 = xs[i], xs[i+1]
    a, b = t1*x1/2, t2*x1/2
    k = mp.ceil((a - pi/2)/pi)
    if pi/2 + k*pi <= b: s2m = mp.mpf(1)
    else: s2m = max(mp.sin(a)**2, mp.sin(b)**2)
    pub = min(s2m/mp.sinh(x1/2)**2, t2**2*h(x1))
    Fub = mp.log(1+pub) - 2*gam*t1**2*h(x2)
    if Fub > worstF: worstF, wx = Fub, x1
print(f"[6] E.6.B corner cell (0.30,0.58): F_lb = {mp.nstr(Flb,8)}, max_x F_ub = {mp.nstr(worstF,8)} at x1={mp.nstr(wx,6)}")
print(f"    slack = {mp.nstr(Flb-worstF,6)}  (printed 0.001448); >0: {Flb > worstF}")
# true corner slack (pointwise, lam=0.30, tau=0.58):
lam_, tau_ = mp.mpf('0.30'), mp.mpf('0.58')
tslack = min(F(lam_, tau_, gam) - F(x, tau_, gam) for x in [mp.mpf('0.6')+mp.mpf(k)/100 for k in range(0, 200)])
print(f"    true pointwise min_x [F(0.30)-F(x)] at tau=0.58 (x in [0.6,2.6) grid .01) = {mp.nstr(tslack,6)}")

print("=== end script A ===")
