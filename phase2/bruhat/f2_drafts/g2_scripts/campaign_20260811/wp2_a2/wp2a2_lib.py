"""wp2a2_lib: shared machinery for wp2-a2 (Delta_ker bucket + T.9 merge), 2026-08-11.

Imports the REPAIRED wp2-b library (wp2b_lib_fixed.py, repairs_20260811 B1,
referee-verified byte-level) for cumulant closed forms, the model polynomial
P(y), Hermite evaluation, and exact Mahonian rows.  New content here:

  * Coefficient boxes A3..A7 for the tilted 6-term model exponent on |t| <= t1
    (unscaled; from wp2-b Lemma W.3 + T2 Lemma T.9''(b)):
      |alpha| = |kappa_3|/6   <= A3 := (K/m)(S_4+m)/720
      |beta|  = |kappa_4|/24  <= A4 := (S_4+m)/2880
      |delta| = |kappa_5|/120 <= A5 := C5UP (S_5+m)/120
      |gamma| = |kappa_6|/720 <= A6 := C6UP (S_6+m)/720
      |R_7(t)|                <= A7 |t|^7,  A7 := (m+1)^8 / 2.8e6
  * eps_K(m): the Gaussian-domination weakening
      eps := [A4 t1^4 + A6 t1^6 + A7 t1^7] / (s2min t1^2 / 2),
    giving (Lemma A.1a)  |phi_lam^c(t)| <= exp(-(1-eps) s2min t^2/2) on |t|<=t1.
  * W_A monomial list (Lemma A.1b majorant), V_Q monomial list (|hatQ - 1|).
  * Closed-form Gaussian moments J(n, a) = Gamma((n+1)/2) / a^{(n+1)/2}
    ( = int_R |t|^n e^{-a t^2} dt ), upper tail bounds tail(n, t0, c)
    ( >= int_{t0}^inf t^n e^{-c t^2} dt ), exact for odd n, safe for even n.
  * delta_ker_bound(K, m): the assembled explicit bound with every named
    intermediate returned (box / tail / out / pointwise / denominator pieces).

Status of inputs (flags carried into the draft):
  W.3 boxes, W.1(i) floors c_1 = 0.967, c_2 = 0.868: PROVED (wp2-b, both
  referees + repair B5).  c_4 = 0.60: grid-certified (repair B4 exhaustive
  m in [30,400] + sampled tail).  T.9''(b): PROVED (T2, both referees).
  wp1-c W.4(i) far constants c1K: PROVED (wp1-c, both referees, repairs A).
  All numeric constants rounded in the safe direction where they are inputs.
"""
import math
import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPAIRS = os.path.normpath(os.path.join(_HERE, "..", "repairs"))
sys.path.insert(0, _REPAIRS)
import wp2b_lib_fixed as lib            # noqa: E402  (repaired library, B1)
from wp2b_n0_resid_table import RESID   # noqa: E402  (sympy-generated, verified)

GAMMA_HALF = math.sqrt(math.pi)

# ---- certified constants (provenance in module docstring) ----
C5UP = 5.08266e-3          # >= 48 zeta(5)/(2pi)^5      (wp2-b NC-W2, PROVED)
C6UP = 3.96835e-3          # >= 240 zeta(6)/(2pi)^6     (wp2-b NC-W2, PROVED)
CK = {1: 0.967, 2: 0.868, 4: 0.60}   # variance floors s2 >= c_K lambda (W.1)
C1K = {1: 0.2259, 2: 0.1802, 4: 0.1019}  # wp1-c Cor W.4(i) far exponents
A7DEN = 2.8e6              # T.9''(b) denominator (chain gives 2.8549e6, safe)


def exact_sums(m):
    S4 = int(lib.S(4, m)); S5 = int(lib.S(5, m)); S6 = int(lib.S(6, m))
    return S4, S5, S6


def coef_boxes(K, m):
    """Unscaled coefficient boxes A3..A7, t1, s2min, lamv, eps for |w| <= K."""
    S4, S5, S6 = exact_sums(m)
    lamv = float(lib.lam_var(m))
    s2min = CK[K] * lamv
    A3 = (K / m) * (S4 + m) / 720.0
    A4 = (S4 + m) / 2880.0
    A5 = C5UP * (S5 + m) / 120.0
    A6 = C6UP * (S6 + m) / 720.0
    A7 = float(m + 1) ** 8 / A7DEN
    t1 = math.sqrt(2.0) * math.pi / m
    eps = (A4 * t1**4 + A6 * t1**6 + A7 * t1**7) / (s2min * t1**2 / 2.0)
    return dict(A3=A3, A4=A4, A5=A5, A6=A6, A7=A7, t1=t1, s2min=s2min,
                lamv=lamv, eps=eps)


# ---- polynomial-as-monomial-dict helpers: {power: coeff} ----
def pmul(p, q):
    out = {}
    for n1, c1 in p.items():
        for n2, c2 in q.items():
            out[n1 + n2] = out.get(n1 + n2, 0.0) + c1 * c2
    return out


def pscale(p, c):
    return {n: v * c for n, v in p.items()}


def padd(*ps):
    out = {}
    for p in ps:
        for n, v in p.items():
            out[n] = out.get(n, 0.0) + v
    return out


def wa_poly(K, m, boxes=None):
    """Monomial dict of the W_A majorant of Lemma A.1(b):
       W_A = V_z^3/6 + A7 t^7 (1 + V_E + A7 t^7/2) + V_r9 ."""
    B = boxes or coef_boxes(K, m)
    A3, A4, A5, A6, A7 = B["A3"], B["A4"], B["A5"], B["A6"], B["A7"]
    VE = {3: A3, 4: A4, 5: A5, 6: A6}
    Vz = padd(VE, {7: A7})
    Wz3 = pscale(pmul(pmul(Vz, Vz), Vz), 1.0 / 6.0)
    R7part = padd({7: A7}, pmul({7: A7}, VE), {14: A7 * A7 / 2.0})
    Vr9 = {9: A3 * A6 + A4 * A5, 10: A4 * A6 + A5 * A5 / 2.0,
           11: A5 * A6, 12: A6 * A6 / 2.0}
    return padd(Wz3, R7part, Vr9)


def vq_poly(K, m, boxes=None):
    """Monomial dict of V_Q = |hatQ - 1| majorant (triangle on hatQ)."""
    B = boxes or coef_boxes(K, m)
    A3, A4, A5, A6 = B["A3"], B["A4"], B["A5"], B["A6"]
    return {3: A3, 4: A4, 5: A5, 6: A6 + A3 * A3 / 2.0,
            7: A3 * A4, 8: A4 * A4 / 2.0 + A3 * A5}


def J(n, a):
    """int_R |t|^n e^{-a t^2} dt = Gamma((n+1)/2) / a^{(n+1)/2}."""
    return math.gamma((n + 1) / 2.0) / a ** ((n + 1) / 2.0)


def Jpoly(p, a, shift=0):
    return sum(c * J(n + shift, a) for n, c in p.items())


def tail(n, t0, c):
    """Upper bound for int_{t0}^inf t^n e^{-c t^2} dt.
       Odd n = 2k+1: exact  e^{-c t0^2} k! / (2 c^{k+1}) sum_{j<=k} (c t0^2)^j/j!.
       Even n: <= tail(n+1)/t0 (t^n <= t^{n+1}/t0 on t >= t0)."""
    if n % 2 == 1:
        k = (n - 1) // 2
        x = c * t0 * t0
        s = sum(x**j / math.factorial(j) for j in range(k + 1))
        return math.exp(-x) * math.factorial(k) / (2.0 * c ** (k + 1)) * s
    return tail(n + 1, t0, c) / t0


# ---- wp2-b scaled boxes / P_min / P0_min / Taylor bucket (ported verbatim
#      from wp2b_nc3_taylor.py + wp2b_nc4_assembly.py, both referee-verified;
#      re-implemented here so wp2_a2 is self-contained) ----
def scaled_boxes(K, m):
    S4, S5, S6 = exact_sums(m)
    lamv = float(lib.lam_var(m))
    s2min = CK[K] * lamv
    a = (K / m) * (S4 + m) / 120.0 / (6.0 * s2min**1.5)
    b = (S4 + m) / 120.0 / (24.0 * s2min**2)
    d = C5UP * (S5 + m) / (120.0 * s2min**2.5)
    g = C6UP * (S6 + m) / (720.0 * s2min**3)
    h = 1.0 / math.sqrt(s2min)
    return a, b, d, g, h, s2min


def P_min(K, m):
    a, b, d, g, h, s2min = scaled_boxes(K, m)
    ga = g + a * a / 2.0
    e8 = b * b / 2.0 + a * d
    return 1.0 - (3*a*h + 3*b + 15*d*h + 15*ga + 105*a*b*h + 105*e8)


def P0_min(K, m):
    a, b, d, g, h, s2min = scaled_boxes(K, m)
    return 1.0 - (3*b + 15*(g + a*a/2.0) + 105*(b*b/2.0 + a*d))


def taylor_bucket(K, m):
    """m^2 sup|L''''|/(12 s2min): wp2-b Lemma W.4's C_R entry (ported)."""
    a, b, d, g, h, s2min = scaled_boxes(K, m)
    ga = g + a * a / 2.0
    e8 = b * b / 2.0 + a * d
    p1 = 3*a + 12*b*h + 15*d + 90*ga*h + 105*a*b + 840*e8*h
    p2 = 6*a*h + 12*b + 60*d*h + 90*ga + 630*a*b*h + 840*e8
    p3 = 6*a + 24*b*h + 60*d + 360*ga*h + 630*a*b + 5040*e8*h
    p4 = 24*b + 120*d*h + 360*ga + 2520*a*b*h + 5040*e8
    Pm = 1 - (3*a*h + 3*b + 15*d*h + 15*ga + 105*a*b*h + 105*e8)
    supL4 = (p4/Pm + 4*p3*p1/Pm**2 + 3*p2**2/Pm**2 + 12*p2*p1**2/Pm**3
             + 6*p1**4/Pm**4)
    return m * m * supL4 / (12.0 * s2min)


def pw_closed(K, m):
    """wp2-b closed-form pointwise bucket (all m >= 180), ported."""
    a, b, d, g, h, s2min = scaled_boxes(K, m)
    tot = Fraction(0)
    aF, bF, dF, gF = (Fraction(a), Fraction(b), Fraction(d), Fraction(g))
    for (ea, eb, ed, eg), co in RESID:
        tot += abs(Fraction(co)) * aF**ea * bF**eb * dF**ed * gF**eg
    return float(tot) * m * m / P0_min(K, m) ** 2


def lin_bucket(K, m):
    """wp2-b Lemma W.5 linearization bucket (m^2-scaled), ported."""
    s2min = CK[K] * float(lib.lam_var(m))
    return m * m * 1.125 * math.exp(1.5 / s2min) / s2min


# ---- the wp2-a2 deliverable ----
def delta_ker_bound(K, m):
    """Explicit bound: |Delta_ker(k)| <= Cker/m^2 for every interior k with
       0 < |lam(k)| <= K/m.  Returns every named intermediate."""
    B = coef_boxes(K, m)
    eps, t1, s2min, lamv = B["eps"], B["t1"], B["s2min"], B["lamv"]
    if eps >= 1.0:
        return None
    a_box = (1.0 - eps) * s2min / 2.0          # Gaussian rate inside the box
    WA = wa_poly(K, m, B)
    VQ = vq_poly(K, m, B)
    c1 = C1K[K]
    far = 2.0 * (math.pi - t1) * math.exp(-c1 * m)   # int_{strip} |phi| bound

    # -- kernel remainder pieces (Lemma A.3) --
    J0_WA = Jpoly(WA, a_box)
    J2_WA = Jpoly(WA, a_box, shift=2)
    J0_1VQ = J(0, a_box) + Jpoly(VQ, a_box)
    J2_1VQ = J(2, a_box) + Jpoly(VQ, a_box, shift=2)
    D_box = (J2_WA * J0_1VQ + J0_WA * J2_1VQ) / (4.0 * math.pi**2)

    cT = s2min / 2.0
    Ttail = tail(0, t1, cT) + sum(c * tail(n, t1, cT) for n, c in VQ.items())
    J0p_1VQ = J(0, cT) + Jpoly(VQ, cT)
    D_tail = 2.0 * Ttail * J0p_1VQ / math.pi**2

    int_phi = math.sqrt(math.pi / a_box) + far
    D_out = far * int_phi / math.pi**2

    DD = D_box + D_tail + D_out

    # -- pointwise error at x = +-1 and denominator bucket (Lemma A.4) --
    E_pt = J0_WA / (2.0 * math.pi) + far / (2.0 * math.pi) + Ttail / math.pi
    Pmin = P_min(K, m)
    P0min = P0_min(K, m)
    if Pmin <= 0 or P0min <= 0:
        return None
    dbar = math.sqrt(2.0 * math.pi * lamv) * math.exp(0.5 / s2min) * E_pt / Pmin
    delta_bar = 2.0 * dbar + dbar * dbar

    # -- numerator w_f and model size v (assembly, Theorem A.5) --
    s2wf = 2.0 * math.pi * lamv**2 * math.exp(1.0 / s2min) * DD / Pmin**2
    ah, bh, dh, gh, hh, _ = scaled_boxes(K, m)
    LF = (1.0 + 12.0 * bh + 36.0 * ah * ah / P0min**2
          + pw_closed(K, m) / m**2 + taylor_bucket(K, m) / m**2)
    vS2 = LF * math.exp(LF / s2min)
    if delta_bar >= 1.0:
        return None
    zbar = (s2wf / s2min + delta_bar * vS2 / s2min) / (1.0 - delta_bar)
    if zbar >= 1.0:
        return None
    Cker = m * m * (s2wf + delta_bar * vS2) / ((1.0 - delta_bar) * (1.0 - zbar))
    return dict(eps=eps, a_box=a_box, D_box=D_box, D_tail=D_tail, D_out=D_out,
                DD=DD, E_pt=E_pt, dbar=dbar, delta_bar=delta_bar, s2wf=s2wf,
                LF=LF, vS2=vS2, zbar=zbar, Cker=Cker, Pmin=Pmin, P0min=P0min,
                far=far, t1=t1, s2min=s2min,
                Cker_far_piece=m * m * (2.0 * math.pi * lamv**2
                                        * math.exp(1.0 / s2min) * D_out
                                        / Pmin**2))
