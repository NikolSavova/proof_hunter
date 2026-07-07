# Section 6: ground-truth checks against exact Mahonian numbers.
import math, sys
import numpy as np
from fractions import Fraction
sys.path.insert(0, "/Users/sihaohuang/Desktop/Coding/proof_hunter/phase2/bruhat")
from mahonian import mahonian

def He(n, y):
    a, b = 1.0, y
    if n == 0: return 1.0
    for k in range(1, n): a, b = b, y*b - k*a
    return b

def params(m):
    lam = m*(m-1)*(2*m+5)/72.0
    S4 = sum(j**4 for j in range(1,m+1)); S6 = sum(j**6 for j in range(1,m+1))
    b = (S4-m)/2880.0/lam**2; g = (S6-m)/181440.0/lam**3
    return lam, b, g

def P(y, b, g): return 1 - b*He(4,y) + g*He(6,y) + b*b/2*He(8,y)

# N(y) via the exact monomial table
Nm = {
 (0,1): [-30,0,180,0,-90],
 (0,2): [6,0,-90,0,540,0,-900,0,1350,0,1350],
 (1,1): [-30,0,456,0,-1620,0,1800,0,90],
 (1,2): [-12,0,372,0,-4140,0,20340,0,-46260,0,45900,0,-18900,0,2700],
 (2,0): [240,0,-1008,0,384],
 (2,1): [29,0,-666,0,5121,0,-16692,0,21195,0,-15930,0,-9945],
 (3,0): [-22,0,510,0,-3588,0,8916,0,-7470,0,-522],
 (3,1): [-12,0,528,0,-8616,0,66240,0,-253440,0,478800,0,-415800,0,151200,0,-18900],
 (4,0): [14,0,-490,0,5946,0,-31830,0,79338,0,-83790,0,48510,0,18270],
 (5,0): [-3,0,171,0,-3780,0,41412,0,-241290,0,750330,0,-1208340,0,926100,0,-297675,0,33075],
}
def Nval(y, b, g):
    tot = 0.0
    for (i,j), cs in Nm.items(): tot += (b**i)*(g**j)*np.polyval(cs, y)
    return tot

print("== E1 end-to-end vs N/P^2 (exact Mahonian) ==")
print(f"{'m':>3} {'max m2|E1| y<=1':>16} {'max m2|E1| y<=3':>16} {'m2 E1(kc)':>10} {'m2 N/P2(y_c)':>12}")
for m in (20,30,40,50,60):
    a = mahonian(m); N = m*(m-1)//2
    lam, b, g = params(m); sig = math.sqrt(lam); Bm = 12*b
    la = [math.log(x) for x in a]  # I(k) fits float for m<=60? m=60: max ~ 60!/... ~1e81 fine
    e1s, ys = [], []
    for k in range(1, N):
        y = (k - N/2)/sig
        if abs(y) > 3.02: continue
        E1 = lam*(2*la[k]-la[k-1]-la[k+1]) - 1 - Bm*(y*y-1)
        e1s.append(E1); ys.append(y)
    e1s, ys = np.array(e1s), np.array(ys)
    kc = N//2; yc = (kc - N/2)/sig
    E1c = lam*(2*la[kc]-la[kc-1]-la[kc+1]) - 1 - Bm*(yc*yc-1)
    pred = Nval(yc,b,g)/P(yc,b,g)**2
    print(f"{m:>3} {m*m*np.abs(e1s[np.abs(ys)<=1]).max():>16.4f} {m*m*np.abs(e1s).max():>16.4f}"
          f" {m*m*E1c:>10.4f} {m*m*pred:>12.4f}")

print("\n== pointwise second-order check: sigma m^3 |p - Z P| over all k ==")
for m in (20,30,40,60):
    a = mahonian(m); N = m*(m-1)//2; fN = float(math.factorial(m))
    lam,b,g = params(m); sig = math.sqrt(lam)
    worst = 0.0
    for k in range(N+1):
        y = (k-N/2)/sig
        p = float(Fraction(a[k], math.factorial(m)))
        Zp = math.exp(-y*y/2)/math.sqrt(2*math.pi*lam)*P(y,b,g)
        worst = max(worst, abs(p-Zp)*sig*m**3)
    print(f"  m={m}: sigma m^3 max|E2| = {worst:.4f}   (claim <= C1''+0.4 = 4.2)")

print("\n== Lemma A: |phi - phihat| <= e^{-lam t^2/2} W(t) on (0, sqrt2 pi/m] ==")
for m in (20,40,60):
    lam,b,g = params(m)
    beta = b*lam**2; gam = g*lam**3; c8 = (m+1)**9/43545600.0
    ts = np.linspace(1e-9, math.sqrt(2)*math.pi/m, 20001)
    phi = np.ones_like(ts)
    for j in range(2, m+1): phi *= np.sin(j*ts/2)/(j*np.sin(ts/2))
    ehalf = np.exp(-lam*ts**2/2)
    phihat = ehalf*(1 - beta*ts**4 - gam*ts**6 + beta**2/2*ts**8)
    U = beta*ts**4 + gam*ts**6 + c8*ts**8
    W = c8*ts**8 + beta*ts**4*(gam*ts**6 + c8*ts**8) + (gam*ts**6+c8*ts**8)**2/2 + U**3/6
    ratio = np.abs(phi-phihat)/(ehalf*W)
    print(f"  m={m}: max |phi-phihat|/(e^..W) = {ratio.max():.4f}  (must be <= 1)")

print("\n== factorization identity D_model = phat^2 - phat_- phat_+ (quadrature, m=10) ==")
m = 10; lam,b,g = params(m)
beta = b*lam**2; gam = g*lam**3
def phihat(t): return math.exp(-lam*t*t/2)*(1 - beta*t**4 - gam*t**6 + beta**2/2*t**8)
def phat(x):
    from scipy.integrate import quad
    return quad(lambda t: phihat(t)*math.cos(t*x), 0, np.inf, limit=400)[0]/math.pi
try:
    from scipy.integrate import dblquad, quad
    x = 3.3
    Dq = dblquad(lambda t,s: phihat(s)*phihat(t)*math.cos((s+t)*x)*(1-math.cos(s-t)),
                 -np.inf, np.inf, -np.inf, np.inf, epsabs=1e-14)[0]/(4*math.pi**2)
    Did = phat(x)**2 - phat(x-1)*phat(x+1)
    print(f"  dblquad D = {Dq:.10e}   phat^2-phat-phat+ = {Did:.10e}   ratio-1 = {Dq/Did-1:.2e}")
except ImportError:
    print("  scipy missing; skipped (identity is 4-line algebra)")
