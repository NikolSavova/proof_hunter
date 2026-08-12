# sl3p_s2a_constants.py — Stage-2 SL3': closed-form constants for E.4(a,b) and
# the analytic lemmas E.5.1/E.5.2/E.6a. Verifies every named constant on fine
# grids (numpy float64) with mpmath dps-30 spot checks at the extremes.
# Output: out_sl3p_s2a.txt (tee manually). 2026-08-12.
import numpy as np
import mpmath as mp
mp.mp.dps = 30

print("=== SL3' Stage 2, script A: closed-form constants ===")

def h(x):
    return np.where(x == 0.0, 1.0, (x/2.0)**2/np.sinh(np.where(x==0,1,x)/2.0)**2)
def psi(x, tau):
    return np.where(x == 0.0, tau**2, np.sin(tau*np.where(x==0,1,x)/2.0)**2/np.sinh(np.where(x==0,1,x)/2.0)**2)
def F(x, tau, gam):
    return np.log1p(psi(x, tau)) - 2*gam*tau**2*h(x)

# (a) envelope constant: 1/sinh^2(y/2) = 4 e^-y/(1-e^-y)^2 <= C_env e^-y, y >= 2pi
Cenv = 4.0/(1.0 - np.exp(-2*np.pi))**2
print(f"(a) C_env = 4/(1-e^-2pi)^2 = {Cenv:.6f}  (claimed <= 4.04: {Cenv <= 4.04})")
# monotone: (1-e^-y)^-2 decreasing in y, so worst at y = 2pi. exact statement.

# (b) psi <= tau^2 beyond the first arch: need 4.04 e^{-2pi/tau} <= tau^2, tau<=0.8
u = np.linspace(1.25, 40, 20000)   # u = 1/tau >= 1.25
ratio = np.exp(2*np.pi*u)/(4.04*u**2)
print(f"(b) min over u>=1.25 of e^(2pi u)/(4.04 u^2) = {ratio.min():.3f} (>=1: {ratio.min()>=1.0})")
print(f"    derivative 2pi - 2/u > 0 for u > 1/pi: monotone increasing, so u=1.25 is the min: at u=1.25: {np.exp(2*np.pi*1.25)/(4.04*1.25**2):.3f}")

# (c) series constants on lam <= 0.3 (v = lam/2 <= 0.15, u = tau*lam/2 <= 0.12)
v = np.linspace(1e-6, 0.15, 300000)
r1 = (np.sinh(v)**2 - v**2)/(v**4/3.0)
oneH = 1.0 - v**2/np.sinh(v)**2
r2 = oneH/(v**2/3.0)
print(f"(c1) (sinh^2 v - v^2)/(v^4/3) in [{r1.min():.6f},{r1.max():.6f}]  (claim <= 1.01: {r1.max()<=1.01})")
print(f"(c2) (1-H(v))/(v^2/3)     in [{r2.min():.6f},{r2.max():.6f}]  (claim in [0.99,1.01]: {r2.min()>=0.99 and r2.max()<=1.01})")
uu = np.linspace(1e-3, 0.12, 300000)   # float grid away from catastrophic cancellation
r3 = (1.0 - np.sin(uu)**2/uu**2)/(uu**2/3.0)
r3mp = max(float((1 - (mp.sin(um)/um)**2)/(um**2/3)) for um in [mp.mpf('1e-4'), mp.mpf('1e-3'), mp.mpf('0.05'), mp.mpf('0.12')])
print(f"(c3) (1-S(u))/(u^2/3)     max = {max(r3.max(), r3mp):.6f}  (claim <= 1, exact by alternating series sin^2 u >= u^2-u^4/3: {max(r3.max(), r3mp)<=1.0})")

# (d) K1'(gam) = (1.65 - 1.98 gam)/12; check F(0)-F(lam) <= K1' tau^2 lam^2
print("(d) K1' verification, lam in (0,0.3], tau in (0,0.8]:")
lam = np.linspace(1e-4, 0.3, 601)[:, None]
tau = np.linspace(1e-3, 0.8, 400)[None, :]
for gam in [0.32, 0.34, 0.38, 0.40, 0.42]:
    K1p = (1.65 - 1.98*gam)/12.0
    F0 = np.log1p(tau**2) - 2*gam*tau**2
    lhs = F0 - F(lam, tau, gam)
    bound = K1p*tau**2*lam**2
    worst = (lhs/bound).max()
    print(f"    gamma*={gam:.2f}: K1'={K1p:.5f}  max (F(0)-F(lam))/(K1' tau^2 lam^2) = {worst:.5f}  PASS={worst<=1.0}")

# (e) I_h := int_0^{pi/0.8} h dx, rigorous lower bound (right Riemann sum, h decreasing)
X = float(mp.pi/mp.mpf('0.8'))
n = 400000; d = X/n
xs = np.arange(1, n+1)*d
Ih_lo = float(np.sum(h(xs))*d)
Ih_hi = float(np.sum(h(np.arange(0, n)*d))*d)
print(f"(e) I_h = int_0^{{pi/0.8={X:.5f}}} h: right-sum lower {Ih_lo:.6f}, left-sum upper {Ih_hi:.6f}; certified I_h >= 2.7: {Ih_lo >= 2.7}")

# (f) E.5.1 Case B slack: need 4.04 e^-w < (4/pi^2)(1/1.64) I_h (2pi)^2 / w^3 for w >= 2pi
cB = (4/np.pi**2)*(1/1.64)*2.7*(2*np.pi)**2
w = np.linspace(2*np.pi, 60, 200000)
slack = cB/(4.04*np.exp(-w)*w**3)
print(f"(f) Case-B constant c_B = {cB:.4f}; min over w>=2pi of c_B/(4.04 w^3 e^-w) = {slack.min():.2f}  (>1: {slack.min()>1.0})")
print(f"    (w^3 e^-w decreasing for w>3; value at w=2pi: {4.04*np.exp(-2*np.pi)*(2*np.pi)**3:.5f} < c_B)")

# (g) E.5.2 spot-check: G(w,tau) >= 1/(2(1+tau^2)) on a grid
def G_of(wv, tv, nx=20000):
    xs = np.linspace(0, wv, nx+1); xs[0] = 1e-12
    gg = np.log1p(psi(xs, tv)); hh = h(xs)
    ag = np.trapz(gg, xs)/wv; ah = np.trapz(hh, xs)/wv
    return (np.log1p(tv**2) - ag)/(2*tv**2*(1-ah))
ok = True; worst = 9e9; wloc = None
for wv in [4.0, 5.0, 8.0, 10.0, 20.0, 40.0, 200.0]:
    for tv in [0.05, 0.2, 0.4, 0.6, 0.75, 0.8]:
        gap = G_of(wv, tv) - 1/(2*(1+tv**2))
        if gap < worst: worst, wloc = gap, (wv, tv)
        ok &= gap > -1e-9
print(f"(g) E.5.2 spot grid: min G - 1/(2(1+tau^2)) = {worst:.6f} at {wloc}  (>=0: {ok})")

# (h) eps_env pieces: 1/(1-e^-lam) <= 1/lam + 1 ; e^{-2pi/tau}/tau^2 increasing
lg = np.linspace(1e-5, 1.0, 200000)
d1 = (1/lg + 1) - 1/(1 - np.exp(-lg))
tg = np.linspace(0.01, 0.8, 100000)
f_env = np.exp(-2*np.pi/tg)/tg**2
print(f"(h) min[(1/lam+1) - 1/(1-e^-lam)] = {d1.min():.6e} (>=0: {d1.min()>=-1e-12})")
print(f"    e^(-2pi/tau)/tau^2 monotone increasing on (0,0.8]: {bool(np.all(np.diff(f_env)>0))}; value at 0.8 = {f_env[-1]:.6e}")
eps_hat = 1.03*np.exp(-2*np.pi/0.8)/0.64
print(f"    eps_hat := max eps_env(tau)/tau^2 = 1.03 e^(-2.5pi)/0.64 = {eps_hat:.6e}")

# (i) E.6a condition C spot-consistency: C(lam,tau) => F(lam) >= F(x) for x>=2lam
print("(i) E.6a spot check at tau0=0.58, gamma=0.32: condition C margins and direct F-domination")
gam = 0.32; t0 = 0.58
for lv in [0.30, 0.45, 0.60, 0.75, 0.89]:
    hl = float(h(np.array([lv]))[0]); h2l = float(h(np.array([2*lv]))[0])
    lhsC = (hl - h2l)*(1 - 2*gam - 2*gam*t0**2)
    rhsC = hl*t0**2*lv**2/12.0
    xs = np.linspace(2*lv, 60, 40000)
    dmin = 9e9
    for tv in np.linspace(0.01, t0, 60):
        dmin = min(dmin, float((F(np.array([lv]), tv, gam) - F(xs, tv, gam)).min()))
    print(f"    lam={lv:.2f}: C-margin = {lhsC/rhsC:.4f} (>1 needed); direct min F(lam)-F(x) over tau<=0.58 = {dmin:.6f}")

# (j) tail constant for E.6c: eps_t = 1/sinh^2(3.925); and 7.85 <= 2pi/0.8
eps_t = float(1/mp.sinh(mp.mpf('3.925'))**2)
print(f"(j) eps_t = 1/sinh^2(3.925) = {eps_t:.6e} (claim <= 1.57e-3: {eps_t <= 1.57e-3}); 2pi/0.8 - 7.85 = {2*np.pi/0.8 - 7.85:.6f} > 0")
print("=== end script A ===")
