"""wp2b_lib_fixed: REPAIRED copy of wp2b_lib.py (repairs_20260811, repair B1).

Fixes the two series-fallback coefficients found by both wp2-b referees
(maths F1 / numerics repair 3), original file untouched per the no-erasing rule:
  g4 small-u fallback last term:  -u**5/22176  ->  -u**5/15840
      (g(u) = 1/u - 1/(e^u-1) has +u^7/1209600 term, B_8 = -1/30;
       g'''' picks up 7*6*5*4/1209600 = 840/1209600 = 1/1440 at u^3 -- unchanged --
       and the NEXT term of g is -u^9/47900160 (B_10 = 5/66), giving
       9*8*7*6*5/47900160 = 15120/47900160 = 1/3168 at u^4 for g5 and
       9*8*7*6/47900160 ... -> for g4: 3024/47900160 = 1/15840 at u^5.)
  g5 small-u fallback last term:  -u**4/4435.2  ->  -u**4/3168
Both wrong coefficients were off by the factor 5/7; measured downstream impact
<= 2.7e-6 relative on any cumulant (referee), far below every quoted margin.

Original docstring follows.
---------------------------------------------------------------------------
wp2b_lib: shared helpers for the wp2-b scripts (Taylor bucket + C_R assembly).

Conventions (identical to g2_draft_t2 / t2i4_nc1_model.py):
  g0(u) = 1/u - 1/(e^u - 1);  g1..g5 its derivatives (Bernoulli small-u fallbacks).
  Tilted cumulants of X = sum_j U_j^lam (Lemma T.2 / (2.2)-(2.5) extended):
    mu    = sum_j [ j g0(lam j) - g0(lam) ]
    s2    = sum_j [ g1(lam) - j^2 g1(lam j) ]
    k3    = sum_j [ j^3 g2(lam j) - g2(lam) ]
    k4    = sum_j [ g3(lam) - j^4 g3(lam j) ]
    k5    = sum_j [ j^5 g4(lam j) - g4(lam) ]
    k6    = sum_j [ g5(lam) - j^6 g5(lam j) ]
  Model exponent (T.6iii sign note): log phi_lam^c(t) = -s2 t^2/2 - i alpha t^3
    - beta t^4 + i delta t^5 - gamma t^6 + R_7,  alpha=k3/6, beta=-k4/24,
    delta=k5/120, gamma=k6/720.
  Scaled coefficients: a = alpha/s2^{3/2}, b = beta/s2^2, d = delta/s2^{5/2},
    g = gamma/s2^3.
  Model polynomial (derived + verified in wp2b_nc1_model_poly.py):
    P(y) = 1 + a He3 - b He4 + d He5 + (g + a^2/2) He6 - a b He7
             + (b^2/2 + a d) He8.
"""
import math
from fractions import Fraction


# ---- per-factor g-derivatives (float; Bernoulli series fallback near 0) ----
def g0(u):
    if abs(u) < 1e-2:
        return 0.5 - u / 12 + u**3 / 720 - u**5 / 30240
    return 1 / u - 1 / (math.expm1(u))


def g1(u):
    if abs(u) < 1e-2:
        return -1 / 12 + u * u / 240 - u**4 / 6048
    e = math.exp(u)
    return -1 / (u * u) + e / math.expm1(u) ** 2


def g2(u):
    if abs(u) < 1e-2:
        return u / 120 - u**3 / 1512 + u**5 / 28800
    e = math.exp(u)
    return 2 / u**3 - e * (e + 1) / math.expm1(u) ** 3


def g3(u):
    if abs(u) < 5e-2:
        return 1 / 120 - u * u / 504 + u**4 / 5760
    e = math.exp(u)
    return -6 / u**4 + e * (e * e + 4 * e + 1) / math.expm1(u) ** 4


def g4(u):
    if abs(u) < 1e-1:
        return -u / 252 + u**3 / 1440 - u**5 / 15840  # FIXED (was /22176)
    e = math.exp(u)
    return 24 / u**5 - e * (e**3 + 11 * e**2 + 11 * e + 1) / math.expm1(u) ** 5


def g5(u):
    if abs(u) < 1e-1:
        return -1 / 252 + u * u / 480 - u**4 / 3168  # FIXED (was /4435.2)
    e = math.exp(u)
    return -120 / u**6 + e * (e**4 + 26 * e**3 + 66 * e**2 + 26 * e + 1) / math.expm1(u) ** 6


def cumulants(m, lam):
    """(mu, s2, k3, k4, k5, k6) of the tilted Mahonian sum, closed forms."""
    mu = var = k3 = k4 = k5 = k6 = 0.0
    gl = (g0(lam), g1(lam), g2(lam), g3(lam), g4(lam), g5(lam))
    for j in range(1, m + 1):
        u = lam * j
        mu += j * g0(u) - gl[0]
        var += gl[1] - j * j * g1(u)
        k3 += j**3 * g2(u) - gl[2]
        k4 += gl[3] - j**4 * g3(u)
        k5 += j**5 * g4(u) - gl[4]
        k6 += gl[5] - j**6 * g5(u)
    return mu, var, k3, k4, k5, k6


def scaled_coeffs(m, lam):
    """(a, b, d, g, s2) true scaled model coefficients at (m, lam)."""
    _, s2, k3, k4, k5, k6 = cumulants(m, lam)
    return (k3 / 6 / s2**1.5, -k4 / 24 / s2**2, k5 / 120 / s2**2.5,
            k6 / 720 / s2**3, s2)


# ---- exact power sums and lambda ----
def S(r, m):
    return sum(Fraction(j) ** r for j in range(1, m + 1))


def lam_var(m):  # sigma^2 = lambda, exact Fraction
    return Fraction(m * (m - 1) * (2 * m + 5), 72)


# ---- Hermite (probabilists') ----
def He(n, y):
    a, b = 1.0, y
    if n == 0:
        return 1.0
    for k in range(1, n):
        a, b = b, y * b - k * a
    return b


# ---- model polynomial and its exact y-derivatives (verified in nc1) ----
def P_coeffs(a, b, d, g):
    """He-basis coefficients c[n] of P = sum_n c[n] He_n."""
    return {0: 1.0, 3: a, 4: -b, 5: d, 6: g + a * a / 2, 7: -a * b,
            8: b * b / 2 + a * d}


def P_eval(a, b, d, g, y, deriv=0):
    """P^(deriv)(y) via He_n' = n He_{n-1} (falling factorial)."""
    tot = 0.0
    for n, c in P_coeffs(a, b, d, g).items():
        if n < deriv:
            continue
        ff = 1.0
        for i in range(deriv):
            ff *= (n - i)
        tot += c * ff * He(n - deriv, y)
    return tot


# N_lam(0) split (hardcoded from the sympy derivation, wp2b_nc1_model_poly.py;
# nc1 asserts these agree with the symbolic result):
# N(y) := -P''P + P'^2 - 12 b He2(y) P^2 ;  N(0) = -36 a^2 + N0_RESID(a,b,d,g)
N0_RESID_MONOMIALS = None  # filled by nc1's generated file if present


def N0_and_P0(a, b, d, g):
    """Exact N(0), P(0) from the polynomial (numeric)."""
    P0 = P_eval(a, b, d, g, 0.0)
    P1 = P_eval(a, b, d, g, 0.0, 1)
    P2 = P_eval(a, b, d, g, 0.0, 2)
    N0 = -P2 * P0 + P1 * P1 - 12 * b * (-1.0) * P0 * P0  # He2(0) = -1
    return N0, P0


def N0_resid_and_P0(a, b, d, g):
    N0, P0 = N0_and_P0(a, b, d, g)
    return N0 + 36 * a * a, P0  # residual := N0 - (-36 a^2)


# ---- exact Mahonian rows (harness algorithm, restated) ----
def mahonian(m):
    poly = [1]
    for dd in range(1, m + 1):
        out = [0] * (len(poly) + dd - 1)
        run = 0
        for k in range(len(out)):
            if k < len(poly):
                run += poly[k]
            if k - dd >= 0:
                run -= poly[k - dd]
            out[k] = run
        poly = out
    return poly
