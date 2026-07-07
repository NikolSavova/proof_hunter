# Sections 2-5: N-corner bounds, W/V kernel constants, superpoly thresholds, C2 table.
import math, numpy as np
SQ2PI = math.sqrt(2*math.pi)
B1hi, B1lo = 0.0900, 0.0890
B2hi, B2lo = 0.03674, 0.03540
B3hi = 0.0431
H2M3 = 36.0

def lam(m): return m*(m-1)*(2*m+5)/72.0

# probabilists' Hermite
def He(n):
    c = np.zeros(n+1); c[0] = 1.0; prev = np.zeros(n+1)
    # He_0=1, He_1=y; He_{k+1} = y He_k - k He_{k-1}
    if n == 0: return np.poly1d([1.0])
    Hkm1, Hk = np.poly1d([1.0]), np.poly1d([1.0,0.0])
    for k in range(1, n):
        Hkm1, Hk = Hk, np.poly1d([1.0,0.0])*Hk - k*Hkm1
    return Hk
HeP = {n: He(n) for n in range(0,11)}

# N monomials from sympy (exact); dict (i,j) -> poly coefficients in y (descending, even powers)
Nmono = {
 (0,1): np.poly1d([-30,0,180,0,-90]),
 (0,2): np.poly1d([6,0,-90,0,540,0,-900,0,1350,0,1350]),
 (1,1): np.poly1d([-30,0,456,0,-1620,0,1800,0,90]),
 (1,2): np.poly1d([-12,0,372,0,-4140,0,20340,0,-46260,0,45900,0,-18900,0,2700]),
 (2,0): np.poly1d([240,0,-1008,0,384]),
 (2,1): np.poly1d([29,0,-666,0,5121,0,-16692,0,21195,0,-15930,0,-9945]),
 (3,0): np.poly1d([-22,0,510,0,-3588,0,8916,0,-7470,0,-522]),
 (3,1): np.poly1d([-12,0,528,0,-8616,0,66240,0,-253440,0,478800,0,-415800,0,151200,0,-18900]),
 (4,0): np.poly1d([14,0,-490,0,5946,0,-31830,0,79338,0,-83790,0,48510,0,18270]),
 (5,0): np.poly1d([-3,0,171,0,-3780,0,41412,0,-241290,0,750330,0,-1208340,0,926100,0,-297675,0,33075]),
}
# sanity: N(0) coefficient check
assert Nmono[(0,1)](0) == -90 and Nmono[(2,0)](0) == 384

def polymax(p, a, bnd):  # max |p| on [a,bnd] via critical points
    dp = p.deriv(); rts = [r.real for r in dp.r if abs(r.imag)<1e-9 and a <= r.real <= bnd]
    pts = [a,bnd]+rts
    return max(abs(p(t)) for t in pts)

# sup_y e^{-y^2/2}|He_n|  (for pointwise first-order corollary)
for n in (6,8):
    ys = np.linspace(0,12,240001); v = np.exp(-ys**2/2)*np.abs(HeP[n](ys))
    print(f"sup e^-y^2/2 |He{n}| = {v.max():.4f} at y={ys[v.argmax()]:.3f}")

# ---------------- W and V scaled-coefficient tables ----------------
# scaled units: b=B1/m, g=B2/m^2, c=B3/m^3 (upper values); powers n mean w_n*lam^-n
# W(t) = R8 + beta t^4(gamma t^6 + R8) + (gamma t^6+R8)^2/2 + U^3/6,  U = beta t^4+gamma t^6+c8 t^8
from collections import defaultdict
def mul(p1, p2):
    out = defaultdict(float)
    for n1,c1 in p1.items():
        for n2,c2 in p2.items(): out[n1+n2] += c1*c2
    return out
def add(p1, p2, s=1.0):
    out = defaultdict(float, p1)
    for n,c in p2.items(): out[n]+=s*c
    return out
def scale(p, s): return defaultdict(float, {n:c*s for n,c in p.items()})
def m_order(n):  # 1/m-order of scaled coeff at power n: b~m^-1(n=2), g~m^-2(n=3), c~m^-3(n=4)
    pass
U  = defaultdict(float, {2:B1hi, 3:B2hi, 4:B3hi})   # keyed by n (t^{2n}), value = lam^n w_n * m^{n-1}
# CAREFUL: units: entry (n, v) means w_n lam^{-n} <= v / m^{n-1}.  products: (n1,v1)(n2,v2) -> (n1+n2, v1v2) with m^{-(n1+n2-2)} -- consistent since m exponents add: (n1-1)+(n2-1) = n1+n2-2 != (n1+n2)-1. MISMATCH by m^{-1} per extra factor => quadratic terms carry extra 1/m. Handle by tracking (n, mpow, val).
# Redo with explicit m-power tracking: item ((n, q), val) means contribution val/m^q at t^{2n}
def D2(d): return defaultdict(float, d)
Ub = D2({(2,1):B1hi, (3,2):B2hi, (4,3):B3hi})
def mul2(p1,p2):
    out = defaultdict(float)
    for (n1,q1),v1 in p1.items():
        for (n2,q2),v2 in p2.items(): out[(n1+n2,q1+q2)] += v1*v2
    return out
def add2(*ps):
    out = defaultdict(float)
    for p in ps:
        for k,v in p.items(): out[k]+=v
    return out
R8b = D2({(4,3):B3hi})
gam6 = D2({(3,2):B2hi})
bet4 = D2({(2,1):B1hi})
gR = add2(gam6, R8b)
W = add2(R8b, mul2(bet4, gR), scale2:=None or {}, )
W = add2(R8b, mul2(bet4,gR))
W = add2(W, {k: v/2 for k,v in mul2(gR,gR).items()})
U3 = mul2(Ub, mul2(Ub,Ub))
W = add2(W, {k: v/6 for k,v in U3.items()})
V = D2({(2,1):B1hi, (3,2):B2hi, (4,3):B3hi})   # V = beta t^4 + gamma t^6 + beta^2 t^8/2; beta^2/2 lam^-4 = b^2/2 <= B1hi^2/2/m^2
V = D2({(2,1):B1hi, (3,2):B2hi, (4,2):B1hi**2/2})
def dfact(n):  # (n)!! double factorial for odd n
    r=1
    while n>1: r*=n; n-=2
    return r
# pointwise constant C1'' (coefficient of 1/(sigma m^3)): m^3 * sum w_n lam^-n (2n-1)!!/sqrt(2pi)
def C1pp(m1):
    return sum(v/m1**(q-3)*dfact(2*n-1) for (n,q),v in W.items())/SQ2PI
# kernel box constant KB (coefficient of 1/m^3 in lam*|w|_box before e^{y0^2}/P^2 factor)
def KB(m1):
    t1 = sum(v/m1**(q-3)*dfact(2*n-1)*(2*n+2) for (n,q),v in W.items())
    t2 = 0.0
    for (a,qa),va in V.items():
        for (bb,qb),vb in W.items():
            t2 += va*vb/m1**(qa+qb-3)*(dfact(2*a+1)*dfact(2*bb-1)+dfact(2*a-1)*dfact(2*bb+1))
    return t1+t2
print("\nW table ((n,q):coeff):", dict(W))
for m1 in (150,180,200,240,300):
    print(f"m1={m1}: C1''={C1pp(m1):.4f}  KB={KB(m1):.3f}")

# ---------------- N corner bound + P_min + l2, l4 ----------------
def bounds_at(y0, m1):
    hbar = 1/math.sqrt(lam(m1))
    yg = np.linspace(0, y0, 4001)                      # |y|<=y0 (N even in y)
    ygE = np.linspace(0, y0+hbar+1e-9, 4001)           # enlarged for P_min, L''''
    # corner max of m^2*(g*N01 + b^2*N20) + slop from higher monomials at m1
    N01, N20 = Nmono[(0,1)](yg), Nmono[(2,0)](yg)
    corners = []
    for gv in (B2lo, B2hi):
        for bv in (B1lo, B1hi):
            corners.append(np.abs(gv*N01 + bv*bv*N20))
    main = np.max(corners, axis=0)
    slop = np.zeros_like(yg)
    for (i,j),p in Nmono.items():
        if (i,j) in ((0,1),(2,0)): continue
        slop += np.abs(p(yg))*(B1hi**i)*(B2hi**j)/m1**(i+2*j-2)
    A2N = (main+slop).max()
    # P_min on enlarged interval at m1  (P = 1 - b He4 + g He6 + b^2/2 He8)
    He4v, He6v, He8v = HeP[4](ygE), HeP[6](ygE), HeP[8](ygE)
    Pm = 1e9
    for gv in (B2lo,B2hi):
        for bv in (B1lo,B1hi):
            Pm = min(Pm, np.min(1 - bv/m1*He4v + gv/m1**2*He6v + bv**2/2/m1**2*He8v))
    # l2 = sup|L''| , l4 = sup|L''''| on enlarged interval (crude, at m1)
    def pj(j):  # sup |P^(j)|
        s = (1.0 if j==0 else 0.0)
        fac = lambda n: math.factorial(n)//math.factorial(n-j) if n>=j else 0
        s += B1hi/m1*fac(4)*polymax(HeP[4-j] if 4>=j else np.poly1d([0]),0,ygE[-1]) if 4>=j else 0
        s += B2hi/m1**2*fac(6)*polymax(HeP[6-j],0,ygE[-1]) if 6>=j else 0
        s += B1hi**2/2/m1**2*fac(8)*polymax(HeP[8-j],0,ygE[-1]) if 8>=j else 0
        return s
    p0,p1,p2,p3,p4 = [pj(j) for j in range(5)]
    l2 = p2/Pm + (p1/Pm)**2
    l4 = p4/Pm + 4*p3*p1/Pm**2 + 3*p2**2/Pm**2 + 12*p2*p1**2/Pm**3 + 6*p1**4/Pm**4
    return A2N, Pm, l2, l4, hbar

# ---------------- superpolynomial pieces at m1 ----------------
def tailmom(n, a, L):   # int_a^inf t^{2n} e^{-L t^2/2} dt <= e^{-La^2/2}*chain(n)
    # recursion: I_n = a^{2n-1}/L e^{-La^2/2} + (2n-1)/L I_{n-1};  I_0 <= e^{-La^2/2}/(L a)
    val = 1.0/(L*a)
    for k in range(1, n+1):
        val = a**(2*k-1)/L + (2*k-1)/L*val
    return val    # multiplies e^{-La^2/2}
def superpoly(y0, m1, Pm):
    L = lam(m1); t1 = math.sqrt(2)*math.pi/m1
    q1 = L*t1*t1/2.0
    far = 2*math.exp(-0.19314*m1)
    # pointwise superpoly Theta_pt (additive to p(k)):
    mid = math.exp(-q1)/(math.pi*L*t1)
    mtail = (math.exp(-q1)/math.pi)*( tailmom(0,t1,L) +
        sum(v/m1**q*L**n*tailmom(n,t1,L) for (n,q),v in V.items()) )  # w_n = Vscaled*lam^n... v/m^q = w_n lam^-n => w_n = v lam^n / m^q
    Th_pt = far + mid + mtail
    # kernel superpoly SP = 2 pi lam^2 (DD_tail + DD_out)
    intV_R  = math.sqrt(2*math.pi/L)*(1 + sum(v/m1**q*dfact(2*n-1) for (n,q),v in V.items()))
    intV_tail = math.exp(-q1)*( tailmom(0,t1,L) + sum(v/m1**q*L**n*tailmom(n,t1,L) for (n,q),v in V.items()) )
    DD_tail = (1/math.pi**2)*2*intV_tail*intV_R*2   # two symmetric strips x |K|<=2
    qout = 2*(math.exp(-q1)/(L*t1) + math.pi*far)
    qall = math.sqrt(2*math.pi/L) + qout
    DD_out = (1/math.pi**2)*qout*qall*2
    SP = 2*math.pi*L*L*(DD_tail+DD_out)
    return Th_pt, SP

# ---------------- assemble C2 table ----------------
print("\n== C2 table ==")
print(f"{'y0':>4} {'m1':>5} {'A2N':>8} {'Pmin':>6} {'boxE':>8} {'deltE':>8} {'spE':>9} {'taylE':>9} {'C2':>9}")
for y0, m1 in ((0.5,180),(1.0,180),(1.0,150),(2.0,200),(3.0,230),(3.0,300)):
    A2N, Pm, l2, l4, hbar = bounds_at(y0, m1)
    Th_pt, SP = superpoly(y0, m1, Pm)
    ey = math.exp(y0*y0 + hbar*hbar)
    boxE  = ey/Pm**2 * KB(m1)/m1           # m^2-scaled box transfer
    spE   = ey/Pm**2 * SP * m1*m1          # m^2-scaled kernel superpoly
    # delta transfer: m^2 * (2 dbar + dbar^2) * lam*v_up /(1-|delta|), lam*v <= (1+l2)(1+2h^2)
    sig = math.sqrt(lam(m1))
    dbar = SQ2PI*math.exp((y0+hbar)**2/2)*(C1pp(m1)/m1**3 + sig*Th_pt)/Pm
    lamv = (1+l2)*(1+2/lam(m1))
    deltE = m1*m1*(2*dbar+dbar**2)*lamv/(1-min(2*dbar+dbar**2,0.5))
    taylE = 3*l4/m1                        # m^2 * h^2 l4/12 <= 36 l4/(12 m) = 3 l4/m
    C2 = (A2N/Pm**2 + (boxE+spE+deltE)*1.02 + taylE)
    print(f"{y0:>4} {m1:>5} {A2N:>8.3f} {Pm:>6.3f} {boxE:>8.3f} {deltE:>8.4f} {spE:>9.4f} {taylE:>9.5f} {C2:>9.3f}")
