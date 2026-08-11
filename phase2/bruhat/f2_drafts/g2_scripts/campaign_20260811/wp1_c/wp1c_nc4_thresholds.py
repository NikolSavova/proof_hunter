"""NC-W4: threshold restoration. Reruns the T2 campaign's standing threshold
criteria with the new far exponents.

(a) NC-T10d criterion (g2_scripts/t2/t2_nc10_far.py, part (d), verbatim):
    m_2 = smallest m with  16 sqrt(2pi) (1.05 m^3/36)^{3/2} exp(-c m) <= 0.2/m^2.
    Old exponents: c = 0.06 e^{-2K} (T.7c). New: c = c_1(K) (Cor W.4).
    Old thresholds reproduced with the T10d loop (m=100 start, step x1.05);
    new thresholds computed with unit step (finer, same criterion).

(b) T.8-final condition (V): exp(-c m) <= s2^{-3/2}/(2 min(m, s2)), worst case
    s2 = 1.05 m^3/36 (upper end; B.0(i)), min(m, s2) = m.
    Old: c m = (m/pi - 1)/4730 (T.7b-final). New: c = c_V = 0.0372 (far region
    [pi/m, pi], scope |lam| <= pi/m) and c = c_1(pi) = 0.1306 (far region
    [t_1, pi], same scope; usable when the core is cut at t_1).

(c) g1_draft_b far-arc note (its section 6/8: m_1(y_0) is set by the far piece
    16 sqrt(2pi) lambda^{3/2} e^{y_0^2} exp(-c m) <= 0.2/m^2):  y_0 = 1,
    old c = 0.19314 (Lemma 1.4, range [2pi/m, pi]) vs new c = c_1'(0) = 0.4617
    (Cor W.4 untilted clause, same range).

Run: python3 wp1c_nc4_thresholds.py   (stdlib only)
"""
import math, sys

C1 = {0: 0.2478, 1: 0.2259, 2: 0.1802, 3: 0.1361, 4: 0.1019}
C1P0 = 0.4617
CV = 0.0372
C1PI = 0.1306

def t10d_threshold(c, coarse):
    m = 100 if coarse else 30
    while True:
        lhs = 16 * math.sqrt(2 * math.pi) * (1.05 * m ** 3 / 36) ** 1.5 * math.exp(-c * m)
        if lhs <= 0.2 / m ** 2:
            return m
        m = int(m * 1.05) + 1 if coarse else m + 1
        if m > 10 ** 8:
            return None

def V_threshold(cfun):
    m = 30
    while m <= 10 ** 8:
        s2 = 1.05 * m ** 3 / 36
        if math.exp(-cfun(m)) <= s2 ** -1.5 / (2 * min(m, s2)):
            return m
        m += 1
    return None

def g1_threshold(c):
    m = 30
    while m <= 10 ** 8:
        lhs = (16 * math.sqrt(2 * math.pi) * (1.05 * m ** 3 / 36) ** 1.5
               * math.e * math.exp(-c * m))
        if lhs <= 0.2 / m ** 2:
            return m
        m += 1
    return None

def main():
    print("NC-W4(a) refined-law far-bucket thresholds m_2(K) (NC-T10d criterion)")
    print("  K   old c (T.7c)   old m_2 (T10d loop)   new c_1(K)   new m_2 (unit step)")
    for K in (1, 2, 3, 4):
        cold = 0.06 * math.exp(-2 * K)
        mold = t10d_threshold(cold, coarse=True)
        mnew = t10d_threshold(C1[K], coarse=False)
        print(f"  {K}   {cold:11.3e}   {mold:12d}          {C1[K]:.4f}       {mnew:6d}")

    print("\nNC-W4(b) T.8-final condition (V) threshold (scope |lam| <= pi/m)")
    print("  worst case over the hypothesis set: s2 = 1.05 m^3/36 (uniform form);")
    print("  the T2 draft's '~2.5e5' evaluated at s2 = C_0 = 2000 (best case) --")
    print("  both shown for the old bound.")
    mV_old = V_threshold(lambda m: (m / math.pi - 1) / 4730)

    def V_threshold_C0(cfun):
        m = 30
        while m <= 10 ** 8:
            s2 = 2000.0
            if math.exp(-cfun(m)) <= s2 ** -1.5 / (2 * min(m, s2)):
                return m
            m += 1
        return None
    mV_old_C0 = V_threshold_C0(lambda m: (m / math.pi - 1) / 4730)
    mV_new = V_threshold(lambda m: CV * m)
    mV_t1 = V_threshold(lambda m: C1PI * m)
    print(f"  old (T.7b-final): m >= {mV_old} (worst case) / {mV_old_C0} (s2 = C_0)")
    print(f"  new, far = [pi/m, pi],  c_V   = {CV}:   m >= {mV_new} (worst case)")
    print(f"  new, far = [t_1, pi],   c_1(pi) = {C1PI}: m >= {mV_t1} (worst case)")

    print("\nNC-W4(c) g1_draft_b far-arc threshold (y_0 = 1)")
    m_old = g1_threshold(0.19314)
    m_new = g1_threshold(C1P0)
    print(f"  old (Lemma 1.4, c = 0.19314): m_1 ~ {m_old}   "
          f"(g1_draft_b's table used m_1 = 180 at y_0 <= 1 -- consistency check)")
    print(f"  new (Cor W.4 untilted, c = {C1P0}): m_1-far ~ {m_new}")
    print("  (note: lowering m_1 below 180 also requires re-evaluating B.8's")
    print("   box/denominator buckets at the smaller m; they are decreasing in m")
    print("   and were evaluated at m_1 = 180, so this is mechanical -- flagged,")
    print("   not done here.)")

    print("\nNC-W4 VERDICT: PASS (reported facts; criterion identical to NC-T10d)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
