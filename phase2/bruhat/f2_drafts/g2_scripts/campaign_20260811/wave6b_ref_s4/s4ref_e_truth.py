# s4ref_e_truth.py -- end-to-end truth check of Theorem SOL.6's interval:
# exact-in-principle computation of r_m(k) = a_m(k)^2/(a_m(k-1) a_m(k+1)) via the
# tilted lattice DFT identity: the pmf of S under tilt lam is the inverse DFT of
# Phi_full(2 pi r/L), L >= N+1 (finite support => no aliasing; float64 rounding only,
# validated below against an exact big-integer computation at m = 30).
# For each case: k = mean-matched integer (k = ceil(mu(lam_target)), lam(k) solved
# by bisection so that mu(lam) = k, keeping lam in (4/m, 0.89]).
import numpy as np
from math import e, pi, sinh, cosh, asin
import mpmath as mp
mp.mp.dps = 30

def csch(x): return 1/mp.sinh(x)
def s2_of(m, lam): return sum((csch(lam/2)**2 - j*j*csch(j*lam/2)**2)/4 for j in range(2, m+1))
def mu_of(m, lam):  return sum(1/(mp.e**lam - 1) - j/(mp.e**(j*lam) - 1) for j in range(1, m+1))

def solve_lam(m, k):
    f = lambda x: mu_of(m, mp.mpf(x)) - k
    lo, hi = mp.mpf("1e-9"), mp.mpf("2.0")   # mu decreasing in lam
    for _ in range(200):
        mid = (lo+hi)/2
        if f(mid) > 0: lo = mid
        else: hi = mid
    return (lo+hi)/2

def pmf_neighborhood(m, lam, ks):
    N = m*(m-1)//2
    L = 1
    while L < N+1: L *= 2
    r = np.arange(L)
    t = 2*np.pi*r/L
    q = np.exp(-lam)
    z = q*np.exp(1j*t)
    P = np.ones(L, dtype=np.complex128)
    zj = np.ones(L, dtype=np.complex128); qj = 1.0
    one_minus_z = 1 - z
    for j in range(1, m+1):
        zj = zj*z; qj = qj*q
        P *= (1 - zj)/one_minus_z * ((1-q)/(1-qj))
    # Phi(t_r) = sum_h p_h e^{+2 pi i r h/L} = L * ifft(p)[r], hence p = fft(P)/L
    # (numpy fft is the e^{-2 pi i r h/L} transform).
    p = np.fft.fft(P).real/L
    return {k: p[k] for k in ks}

print("== [0] machinery validation at m = 30 vs exact integers ==")
m0 = 30
lam0 = 0.30
k0 = int(mp.ceil(mu_of(m0, mp.mpf(lam0))))
lam0x = float(solve_lam(m0, k0))
# exact a_m(n) by integer polynomial product
coeffs = [1]
for j in range(2, m0+1):
    new = [0]*(len(coeffs)+j-1)
    for i, c in enumerate(coeffs):
        for d in range(j):
            new[i+d] += c
    coeffs = new
import fractions
r_exact = fractions.Fraction(coeffs[k0]*coeffs[k0], coeffs[k0-1]*coeffs[k0+1])
p = pmf_neighborhood(m0, lam0x, [k0-1, k0, k0+1])
r_fft = p[k0]**2/(p[k0-1]*p[k0+1])
print(f"  m=30, k={k0}, lam={lam0x:.6f}: r_exact = {float(r_exact):.12f}, r_fft = {r_fft:.12f}, "
      f"rel err = {abs(r_fft-float(r_exact))/float(r_exact):.2e}  "
      f"{'PASS' if abs(r_fft-float(r_exact))/float(r_exact) < 1e-9 else 'FAIL'}")

print("== [1] truth of s2 (r-1) at mean-matched corners ==")
cases = [(700, 0.89, "W7 deep, m=700 (draft scope)"),
         (700, 4.05/700, "W1 edge, m=700 (draft scope)"),
         (700, 10/700, "W4 edge, m=700 (draft scope)"),
         (1000, 0.89, "W7 deep, m=1000 (draft scope)"),
         (699, 0.89, "W7 deep, m=699 [GAP RANGE]"),
         (650, 4.05/650, "W1 edge, m=650 [GAP RANGE]"),
         (561, 0.89, "W7 deep, m=561 [GAP RANGE]"),
         (561, 4.05/561, "W1 edge, m=561 [GAP RANGE]")]
for m, lam_t, label in cases:
    k = int(mp.ceil(mu_of(m, mp.mpf(lam_t))))
    lam = solve_lam(m, k)
    w = float(lam)*m
    if not (4.0/m < float(lam) <= 0.89):
        print(f"  m={m} ({label}): resolved lam={float(lam):.6f} OUT OF BAND -- skipped"); continue
    s2 = float(s2_of(m, lam))
    p = pmf_neighborhood(m, float(lam), [k-1, k, k+1])
    r = p[k]**2/(p[k-1]*p[k+1])
    val = s2*(r-1)
    in_int = 0.607 < val < 1.545
    in_seed = abs(val - 1) < 0.545
    print(f"  m={m}, k={k}, w={w:.4f} ({label}):")
    print(f"    s2 = {s2:.4f}, r-1 = {r-1:.6e}, s2(r-1) = {val:.6f}; "
          f"in (0.607, 1.545): {in_int}; |.-1| < 0.545: {in_seed}")
