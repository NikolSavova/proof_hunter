# s4ref_c_remainder.py -- adversarial check of Lemma SOL.2's load-bearing outputs:
#   (SOL.8):  |R(y)| <= 0.0021 y^4 for |y| <= 4   (R = log Phi + y^2/2 - i alpha y^3)
#   |alpha| = |kappa_3|/(6 sigma^3) <= 0.0298
#   (SOL.17): |Phi(y/sigma) - e^{-y^2/2}| <= e^{-y^2/2}(0.0298|y|^3 + e^{0.0021 y^4}-1)
#   plus the (SOL.1) truth check A/m in [0.28, 1] at every corner.
# log Phi computed EXACTLY as a sum of per-factor principal logs (factors are
# near the positive real axis for |t| <= 0.29, so no branch crossings; verified
# by continuity of the imaginary part along the y-grid).
import mpmath as mp
mp.mp.dps = 40

def csch(x): return 1/mp.sinh(x)
def v_j(lam, j):
    a = lam/2; b = j*lam/2
    return (csch(a)**2 - j*j*csch(b)**2)/4
def k3_j(lam, j):
    a = lam/2; b = j*lam/2
    return (csch(a)**2*mp.coth(a) - j**3*csch(b)**2*mp.coth(b))/4
def mean_j(lam, j):
    return 1/(mp.e**lam - 1) - j/(mp.e**(j*lam) - 1)

def model(m, lam):
    s2 = mp.mpf(0); k3 = mp.mpf(0); mu = mp.mpf(0)
    for j in range(1, m+1):
        if j >= 2:
            s2 += v_j(lam, j); k3 += k3_j(lam, j)
        mu += mean_j(lam, j)
    return mu, s2, k3

def logPhi(m, lam, mu, t):
    # log E e^{it(S-mu)} = -it*mu + sum_j [log(1-e^{(it-lam) j}) - log(1-e^{it-lam})
    #                                      - log(1-e^{-lam j}) + log(1-e^{-lam})]
    tot = -1j*t*mu
    z = mp.e**(1j*t - lam)
    q = mp.e**(-lam)
    zj = mp.mpf(1); qj = mp.mpf(1)
    for j in range(1, m+1):
        zj = zj*z; qj = qj*q
        tot += mp.log(1 - zj) - mp.log(1 - z) - mp.log(1 - qj) + mp.log(1 - q)
    return tot

corners = [(700, mp.mpf("4.001")/700, "W1 edge, A near floor"),
           (700, mp.mpf("4.3")/700,   "W1 mid"),
           (700, mp.mpf("5.001")/700, "W2 left edge"),
           (700, mp.mpf("10")/700,    "W4 right edge"),
           (700, mp.mpf("40.001")/700,"W7 left edge"),
           (700, mp.mpf("0.89"),      "W7 deep corner"),
           (1000, mp.mpf("4.001")/1000, "W1 edge, m=1000"),
           (1000, mp.mpf("0.89"),     "W7 deep, m=1000"),
           (561, mp.mpf("4.001")/561, "W1 edge, m=561 [informative]"),
           (561, mp.mpf("0.89"),      "W7 deep, m=561 [informative]")]

ys = [mp.mpf(x)/8 for x in range(2, 33)]   # y = 0.25 .. 4.0 step 0.125
print("== (SOL.8)/(SOL.17)/alpha/(SOL.1) at adversarial corners ==")
allpass = True
for m, lam, label in corners:
    mu, s2, k3 = model(m, lam)
    sig = mp.sqrt(s2); A = lam*lam*s2
    alpha_abs = abs(k3)/(6*sig**3)
    Aok = mp.mpf("0.28") <= A/m <= 1
    a_ok = alpha_abs <= mp.mpf("0.0298")
    maxratio = mp.mpf(0); cor_ok = True; im_prev = 0
    for y in ys:
        t = y/sig
        LP = logPhi(m, lam, mu, t)
        # branch-continuity guard: imaginary part moves continuously
        if abs(mp.im(LP) - im_prev) > 1:
            print(f"    BRANCH JUMP at y={float(y)}"); cor_ok = False
        im_prev = mp.im(LP)
        R = LP + y*y/2 + 1j*k3*t**3/6
        ratio = abs(R)/y**4
        if ratio > maxratio: maxratio = ratio
        # Corollary SOL.17 direct
        lhs = abs(mp.e**LP - mp.e**(-y*y/2))
        rhs = mp.e**(-y*y/2)*(mp.mpf("0.0298")*abs(y)**3 + mp.e**(mp.mpf("0.0021")*y**4) - 1)
        if lhs > rhs: cor_ok = False
    r_ok = maxratio <= mp.mpf("0.0021")
    tag = "PASS" if (Aok and a_ok and r_ok and cor_ok) else "FAIL"
    if m >= 700 and tag == "FAIL": allpass = False
    print(f"  [{tag}] m={m}, w={mp.nstr(lam*m,7)} ({label}):")
    print(f"      A/m = {mp.nstr(A/m, 6)} in [0.28, 1]: {Aok};  |alpha| = {mp.nstr(alpha_abs, 5)}"
          f" <= 0.0298: {a_ok}")
    print(f"      max |R(y)|/y^4 = {mp.nstr(maxratio, 5)} <= 0.0021: {r_ok};  (SOL.17) direct: {cor_ok}")
print(f"ALL m >= 700 corners PASS: {allpass}")
