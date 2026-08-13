"""referee_sol_s2_checks.py — adversarial maths-referee verification for
sol_s2_20260812.md (gpt-5.6-sol's (S2) attempt).  Wave 6b cross-model
refereeing, F2 campaign, 2026-08-12.

Blocks:
 [A] SOL.2 scalar identities: A_1/A_4 closed forms vs direct sums (mp dps 60).
 [B] SOL.1/SOL.2 cumulant formulas vs brute-force discrete law (small case).
 [C] SOL.3 exact remainder: R5_direct (log-phi) vs R5_series (SOL.3.1)
     vs R5_integral (SOL.3.2), small case + a campaign-scale case.
 [D] SOL.4 majorant: |R5| <= B5 t^5, and the size of C_abs vs the C5* targets
     at the W1 corner (561, w=4.5) and the W7 deep corner (561, lam=0.89)
     -> quantifies "too crude" with numbers.
 [E] SOL.6 limit constant: exact a, b, 32*sqrt(a^2+b^2) at dps 60, against
     the draft's quoted digits; also Q_inf(x) formula cross-check; also
     finite-N convergence Q(N^2, 1/N, 1/(2N)) for N = 20..320.
 [F] Q at the two corners of [D] (measured (S2) truth corroboration vs the
     C5* tables old (0.80) and scout-adjusted (0.50) at W7).
"""
import mpmath as mp

mp.mp.dps = 60

def A_(p, x):
    """A_p(x) = sum_{r>=1} r^p e^{-rx}, direct sum with certified-small tail."""
    s = mp.mpf(0)
    r = 1
    while True:
        term = mp.mpf(r)**p * mp.e**(-r*x)
        s += term
        if term < mp.mpf(10)**(-70) and r > 10:
            break
        r += 1
        if r > 200000:
            break
    return s

def A1_closed(x):
    q = mp.e**(-x)
    return q/(1-q)**2

def A4_closed(x):
    q = mp.e**(-x)
    return q*(1+11*q+11*q**2+q**3)/(1-q)**5

print("[A] SOL.2 scalar identities")
for x in [mp.mpf('0.3'), mp.mpf('0.89'), mp.mpf('2.0')]:
    d1 = abs(A_(1, x) - A1_closed(x))/A1_closed(x)
    d4 = abs(A_(4, x) - A4_closed(x))/A4_closed(x)
    print(f"  x={float(x):5.2f}:  relerr A1 = {mp.nstr(d1,3)}   relerr A4 = {mp.nstr(d4,3)}")

# ---- model machinery (SOL.1/SOL.2) ----
def cumulants_bruteforce(m, lam):
    """mean, var, k3, k4 of X_m = sum U_j from the discrete tilted law directly."""
    tot_mu = mp.mpf(0); tot_v = mp.mpf(0); tot_k3 = mp.mpf(0); tot_k4 = mp.mpf(0)
    for j in range(1, m+1):
        ws = [mp.e**(-lam*a) for a in range(j)]
        Z = sum(ws)
        mu = sum(a*ws[a] for a in range(j))/Z
        m2 = sum((a-mu)**2*ws[a] for a in range(j))/Z
        m3 = sum((a-mu)**3*ws[a] for a in range(j))/Z
        m4 = sum((a-mu)**4*ws[a] for a in range(j))/Z
        tot_mu += mu; tot_v += m2; tot_k3 += m3; tot_k4 += m4 - 3*m2**2
    return tot_mu, tot_v, tot_k3, tot_k4

def Lnth(m, lam, n):
    """L_m^{(n)}(lam) per SOL.2: (-1)^n ( m A_{n-1}(lam) - sum_j j^n A_{n-1}(j lam) )."""
    s = m*A_(n-1, lam) - sum(mp.mpf(j)**n * A_(n-1, j*lam) for j in range(1, m+1))
    return (-1)**n * s

print()
print("[B] SOL.1/SOL.2 cumulants vs brute force  (m=7, lam=0.37)")
m, lam = 7, mp.mpf('0.37')
mu_b, v_b, k3_b, k4_b = cumulants_bruteforce(m, lam)
s2_f  = m*A1_closed(lam) - sum(mp.mpf(j)**2*A1_closed(j*lam) for j in range(1, m+1))
k3_f  = -Lnth(m, lam, 3)
k4_f  = Lnth(m, lam, 4)
mu_f  = -Lnth(m, lam, 1)
print(f"  mu : brute {mp.nstr(mu_b,20)}  formula {mp.nstr(mu_f,20)}  diff {mp.nstr(abs(mu_b-mu_f),3)}")
print(f"  s2 : brute {mp.nstr(v_b,20)}  SOL.2.1 {mp.nstr(s2_f,20)}  diff {mp.nstr(abs(v_b-s2_f),3)}")
print(f"  k3 : brute {mp.nstr(k3_b,20)}  formula {mp.nstr(k3_f,20)}  diff {mp.nstr(abs(k3_b-k3_f),3)}")
print(f"  k4 : brute {mp.nstr(k4_b,20)}  formula {mp.nstr(k4_f,20)}  diff {mp.nstr(abs(k4_b-k4_f),3)}")

# ---- R5 three ways (SOL.3) ----
def Lm(m, lam, z):
    """L_m(z) = sum_j [log(1-e^{-jz}) - log(1-e^{-z})], principal branch (|e^{-jz}|<1)."""
    return sum(mp.log(1-mp.e**(-j*z)) - mp.log(1-mp.e**(-z)) for j in range(1, m+1))

def R5_direct(m, lam, t):
    s2 = m*A1_closed(lam) - sum(mp.mpf(j)**2*A1_closed(j*lam) for j in range(1, m+1))
    k3 = -Lnth(m, lam, 3)
    k4 =  Lnth(m, lam, 4)
    L1 = -Lnth(m, lam, 1)     # mu = -L'(lam), so L'(lam) = -mu
    z  = lam - 1j*t
    lp = Lm(m, lam, z) - Lm(m, lam, lam) + 1j*t*(-L1)   # L'(lam) = -mu = -L1... careful
    # NOTE: SOL.1: log phi = L(lam-it) - L(lam) + i t L'(lam); L'(lam) = -mu = -mu_f
    lp = Lm(m, lam, z) - Lm(m, lam, lam) + 1j*t*(Lnth(m, lam, 1))
    return lp + s2*t**2/2 + 1j*k3*t**3/6 - k4*t**4/24, s2, k3, k4

def E4(u):
    return mp.e**u - (1 + u + u**2/2 + u**3/6 + u**4/24)

def R5_series(m, lam, t, R=400):
    s = mp.mpc(0)
    for r in range(1, R+1):
        term = m*mp.e**(-r*lam)*E4(1j*r*t) - sum(mp.e**(-r*j*lam)*E4(1j*r*j*t) for j in range(1, m+1))
        s += term/r
    return s

def R5_integral(m, lam, t):
    def integrand(u):
        z = lam - 1j*u*t
        # L^{(5)}(z) = -( m A_4(z) - sum_j j^5 A_4(j z) )  [n=5 odd]
        L5 = -(m*A4_closed(z) - sum(mp.mpf(j)**5*A4_closed(j*z) for j in range(1, m+1)))
        return (1-u)**4 * L5
    I = mp.quad(integrand, [0, 1])
    return (-1j*t)**5/24 * I

print()
print("[C] SOL.3: R5 three ways")
for (mm, ll) in [(7, mp.mpf('0.37')), (60, mp.mpf('4.5')/60)]:
    tt = ll/2
    r5d, s2c, k3c, k4c = R5_direct(mm, ll, tt)
    r5s = R5_series(mm, ll, tt, R=600)
    r5i = R5_integral(mm, ll, tt)
    print(f"  (m,lam,t)=({mm},{mp.nstr(ll,8)},{mp.nstr(tt,8)}):")
    print(f"    R5_direct   = {mp.nstr(r5d, 20)}")
    print(f"    R5_series   = {mp.nstr(r5s, 20)}   |d-s| = {mp.nstr(abs(r5d-r5s),3)}")
    print(f"    R5_integral = {mp.nstr(r5i, 20)}   |d-i| = {mp.nstr(abs(r5d-r5i),3)}")

print()
print("[D] SOL.4 majorant + size of C_abs vs targets")
def B5(m, lam):
    return (m*A4_closed(lam) + sum(mp.mpf(j)**5*A4_closed(j*lam) for j in range(1, m+1)))/120

def s2_of(m, lam):
    return m*A1_closed(lam) - sum(mp.mpf(j)**2*A1_closed(j*lam) for j in range(1, m+1))

cases = [("W1 corner  (m=561, w=4.5)", 561, mp.mpf('4.5')/561, mp.mpf('0.05')),
         ("W1 rt edge (m=561, w=5.0)", 561, mp.mpf('5.0')/561, mp.mpf('0.05')),
         ("W7 deep    (m=561, lam=0.89)", 561, mp.mpf('0.89'), mp.mpf('0.80'))]
for name, mm, ll, c5 in cases:
    tt = ll/2
    r5d, s2c, _, _ = R5_direct(mm, ll, tt)
    b5v = B5(mm, ll)
    cabs = ll**3 * b5v / s2c
    ok = abs(r5d) <= b5v*tt**5
    Q = ll**3*abs(r5d)/(s2c*tt**5)
    print(f"  {name}: |R5(lam/2)| = {mp.nstr(abs(r5d),6)}  <= B5 t^5 = {mp.nstr(b5v*tt**5,6)} : {ok}")
    print(f"      C_abs = {mp.nstr(cabs,6)}   vs C5* = {float(c5)}   (ratio {mp.nstr(cabs/c5,5)}x)")
    print(f"      measured Q(t=lam/2) = {mp.nstr(Q,6)}")

print()
print("[E] SOL.6 constant and convergence")
a = -mp.log(mp.mpf(5)/4)/2 + mp.mpf(1)/8 - mp.mpf(1)/64
b = mp.atan(mp.mpf(1)/2) - mp.mpf(1)/2 + mp.mpf(1)/24
Qhalf = 32*mp.sqrt(a**2+b**2)
print(f"  a = {mp.nstr(a, 20)}   (draft: -0.002196775657104877)")
print(f"  b = {mp.nstr(b, 20)}   (draft:  0.00531427566747278)")
print(f"  32 sqrt(a^2+b^2) = {mp.nstr(Qhalf, 15)}   (draft: 0.18401349...)")
x = mp.mpf(1)/2
Qform = abs(-mp.log(1-1j*x) - sum((1j*x)**n/n for n in range(1, 5)))/x**5
print(f"  Q_inf(1/2) via formula = {mp.nstr(Qform, 15)}   match: {abs(Qform-Qhalf) < mp.mpf(10)**-40}")
for N in [20, 50, 100, 200, 320]:
    mm = N*N; ll = mp.mpf(1)/N; tt = ll/2
    r5d, s2c, _, _ = R5_direct(mm, ll, tt)
    Q = ll**3*abs(r5d)/(s2c*tt**5)
    print(f"  N={N:4d}: (m,lam,t)=({mm},1/{N},1/{2*N})  w={N}  Q = {mp.nstr(Q, 10)}")

print()
print("[F] W7 C5 comparison: Q_inf(1/2) = 0.184013 vs old C5*(W7)=0.80, scout C5*(W7)=0.50")
print(f"  0.184013 <= 0.50: {Qhalf <= mp.mpf('0.50')}   0.184013 <= 0.80: {Qhalf <= mp.mpf('0.80')}")
print(f"  scout-quoted W7 corner truth 0.2104/0.21153: measured Q at (561, 0.89, lam/2) printed in [D]")

print()
print("[G] supplementary: C_abs over W7/W6b sample + SOL.5.2 Q(0) at the W7 corner")
def C_abs(m, lam):
    return lam**3*B5(m, lam)/s2_of(m, lam)
for (mm, w) in [(561, mp.mpf('40.001')), (561, mp.mpf('45')), (561, mp.mpf('100')),
                (2000, mp.mpf('41')), (10000, mp.mpf('41')), (100000, mp.mpf('41')),
                (2000, mp.mpf('0.89')*2000), (561, mp.mpf('0.89')*561)]:
    ll = w/mm
    print(f"  W7 sample (m={mm}, w={mp.nstr(w,7)}, lam={mp.nstr(ll,6)}): C_abs = {mp.nstr(C_abs(mm, ll),6)}")
for (mm, w) in [(561, mp.mpf('20.001')), (561, mp.mpf('40')), (100000, mp.mpf('20.001')), (100000, mp.mpf('40'))]:
    ll = w/mm
    print(f"  W6b sample (m={mm}, w={mp.nstr(w,7)}, lam={mp.nstr(ll,6)}): C_abs = {mp.nstr(C_abs(mm, ll),6)}  (target 0.25)")
# SOL.5.2 continuous extension at the W7 corner vs the scout's kappa_5 leading order 0.21153
mm, ll = 561, mp.mpf('0.89')
L5 = Lnth(mm, ll, 5)
Q0 = ll**3*abs(L5)/(120*s2_of(mm, ll))
print(f"  Q(561, 0.89, t=0) per SOL.5.2 = {mp.nstr(Q0, 8)}   (scout block [S2] leading order: 0.21153)")
