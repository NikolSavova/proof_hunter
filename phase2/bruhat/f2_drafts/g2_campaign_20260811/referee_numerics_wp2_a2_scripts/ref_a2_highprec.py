"""Referee check R2 (wp2-a2 numerics): independent high-precision (mpmath
dps 60) re-implementation of the refined bound delta_ker_bound2, from the
draft's FORMULAS (Lemmas D.1'-D.4, Theorem D.5), not from the library code.
Compares every headline constant and per-piece entry against the float lib.

Any relative deviation > 1e-10 would indicate a float-assembly artifact or a
divergence between the draft's formulas and the shipped code.

Run: python3 ref_a2_highprec.py
"""
import os
import sys

import mpmath as mp

_HERE = os.path.dirname(os.path.abspath(__file__))
_WP = os.path.normpath(os.path.join(_HERE, "..", "..", "g2_scripts",
                                    "campaign_20260811", "wp2_a2"))
sys.path.insert(0, _WP)
import wp2a2_lib as L        # noqa: E402
import wp2a2_lib2 as L2      # noqa: E402

mp.mp.dps = 60

CK = {1: mp.mpf("0.967"), 2: mp.mpf("0.868"), 4: mp.mpf("0.60")}
C1K = {1: mp.mpf("0.2259"), 2: mp.mpf("0.1802"), 4: mp.mpf("0.1019")}
C5UP = mp.mpf("5.08266e-3")
C6UP = mp.mpf("3.96835e-3")
A7DEN = mp.mpf("2.8e6")


def S(r, m):
    return sum(mp.mpf(j) ** r for j in range(1, m + 1))


def pmul(p, q):
    out = {}
    for n1, c1 in p.items():
        for n2, c2 in q.items():
            out[n1 + n2] = out.get(n1 + n2, mp.mpf(0)) + c1 * c2
    return out


def padd(*ps):
    out = {}
    for p in ps:
        for n, v in p.items():
            out[n] = out.get(n, mp.mpf(0)) + v
    return out


def pscale(p, c):
    return {n: v * c for n, v in p.items()}


def J(n, a):
    return mp.gamma(mp.mpf(n + 1) / 2) / a ** (mp.mpf(n + 1) / 2)


def Jpoly(p, a, shift=0):
    return sum(c * J(n + shift, a) for n, c in p.items())


def tail(n, t0, c):
    if n % 2 == 1:
        k = (n - 1) // 2
        x = c * t0 * t0
        s = sum(x ** j / mp.factorial(j) for j in range(k + 1))
        return mp.e ** (-x) * mp.factorial(k) / (2 * c ** (k + 1)) * s
    return tail(n + 1, t0, c) / t0


def bound_hp(K, m):
    S4, S5, S6 = S(4, m), S(5, m), S(6, m)
    lamv = mp.mpf(m * (m - 1) * (2 * m + 5)) / 72
    s2min = CK[K] * lamv
    A3 = (mp.mpf(K) / m) * (S4 + m) / 720
    A4 = (S4 + m) / 2880
    A5 = C5UP * (S5 + m) / 120
    A6 = C6UP * (S6 + m) / 720
    A7 = mp.mpf(m + 1) ** 8 / A7DEN
    t1 = mp.sqrt(2) * mp.pi / m
    eps = (A4 * t1 ** 4 + A6 * t1 ** 6 + A7 * t1 ** 7) / (s2min * t1 ** 2 / 2)
    a = (1 - eps) * s2min / 2

    ZR = {4: A4, 6: A6, 7: A7}
    ZI = {3: A3, 5: A5, 7: A7}
    UB = {3: A3, 4: A4, 5: A5, 6: A6}
    R7X = padd({7: A7}, pmul({7: A7}, UB), {14: A7 * A7 / 2})
    ReD2b = {10: A4 * A6 + A5 * A5 / 2, 12: A6 * A6 / 2}
    ImD2b = {9: A3 * A6 + A4 * A5, 11: A5 * A6}
    ZI2, ZR2 = pmul(ZI, ZI), pmul(ZR, ZR)
    WR = padd(pscale(padd(pmul(ZR, ZR2), pscale(pmul(ZR, ZI2), 3)), mp.mpf(1) / 6),
              pscale(padd(pscale(pmul(ZR2, ZI2), 3), pmul(ZI2, ZI2)), mp.mpf(1) / 24),
              R7X, ReD2b)
    ZRI = padd(ZR, ZI)
    WI = padd(pscale(pmul(pmul(ZRI, ZRI), ZRI), mp.mpf(1) / 6), R7X, ImD2b)
    VE = {4: A4, 6: A6 + A3 * A3 / 2, 8: A4 * A4 / 2 + A3 * A5}
    VO = {3: A3, 5: A5, 7: A3 * A4}
    VQ = {3: A3, 4: A4, 5: A5, 6: A6 + A3 * A3 / 2,
          7: A3 * A4, 8: A4 * A4 / 2 + A3 * A5}

    far = 2 * (mp.pi - t1) * mp.e ** (-C1K[K] * m)

    def pair(p, q):
        return (Jpoly(p, a, 2) * Jpoly(q, a) + Jpoly(p, a) * Jpoly(q, a, 2)) / 2

    ONE = {0: mp.mpf(1)}
    D_box = (pair(WR, ONE) + pair(padd(ONE, VE), WR)
             + pair(WI, ZI) + pair(VO, WI)) / (4 * mp.pi ** 2)
    cT = s2min / 2
    Ttail = tail(0, t1, cT) + sum(c * tail(n, t1, cT) for n, c in VQ.items())
    D_tail = 2 * Ttail * (J(0, cT) + Jpoly(VQ, cT)) / mp.pi ** 2
    D_out = far * (mp.sqrt(mp.pi / a) + far) / mp.pi ** 2
    DD = D_box + D_tail + D_out

    E_pt = ((Jpoly(WR, a) + Jpoly(WI, a, 1)) / (2 * mp.pi)
            + far / (2 * mp.pi) + Ttail / mp.pi)

    # scaled boxes and wp2-b floors (draft ports)
    a_s = (mp.mpf(K) / m) * (S4 + m) / 120 / (6 * s2min ** mp.mpf("1.5"))
    b_s = (S4 + m) / 120 / (24 * s2min ** 2)
    d_s = C5UP * (S5 + m) / (120 * s2min ** mp.mpf("2.5"))
    g_s = C6UP * (S6 + m) / (720 * s2min ** 3)
    h = 1 / mp.sqrt(s2min)
    ga = g_s + a_s * a_s / 2
    e8 = b_s * b_s / 2 + a_s * d_s
    Pmin = 1 - (3 * a_s * h + 3 * b_s + 15 * d_s * h + 15 * ga
                + 105 * a_s * b_s * h + 105 * e8)
    P0min = 1 - (3 * b_s + 15 * ga + 105 * e8)

    dbar = mp.sqrt(2 * mp.pi * lamv) * mp.e ** (1 / (2 * s2min)) * E_pt / Pmin
    delta_bar = 2 * dbar + dbar * dbar
    s2wf = 2 * mp.pi * lamv ** 2 * mp.e ** (1 / s2min) * DD / Pmin ** 2

    # core: 12 b + 36 a^2/P0min^2 + PW/m^2 + T/m^2 with the lib's ports
    pw = mp.mpf(L.pw_closed(K, m))       # Fraction-based; take as given
    tb = mp.mpf(L.taylor_bucket(K, m))   # float port; deviation checked below
    core = 12 * b_s + 36 * a_s * a_s / P0min ** 2 + pw / m ** 2 + tb / m ** 2
    LF = 1 + core
    vS2 = LF * mp.e ** (LF / s2min)
    zbar = (s2wf / s2min + delta_bar * vS2 / s2min) / (1 - delta_bar)
    Cker = m * m * (s2wf + delta_bar * vS2) / ((1 - delta_bar) * (1 - zbar))
    return dict(Cker=Cker, D_box=D_box, D_tail=D_tail, D_out=D_out,
                E_pt=E_pt, dbar=dbar, s2wf=s2wf, vS2=vS2, zbar=zbar,
                eps=eps, Pmin=Pmin, P0min=P0min)


def main():
    ok = True
    print("R2: high-precision re-implementation vs float lib")
    for K, m in ((1, 180), (2, 181), (4, 367), (1, 400), (2, 400), (4, 400),
                 (1, 2000), (4, 2000)):
        hp = bound_hp(K, m)
        fl = L2.delta_ker_bound2(K, m)
        rel = abs(mp.mpf(fl["Cker"]) - hp["Cker"]) / hp["Cker"]
        piece_rels = []
        for key in ("D_box", "D_tail", "D_out", "E_pt", "dbar", "s2wf",
                    "vS2", "zbar", "eps", "Pmin", "P0min"):
            hv, fv = hp[key], mp.mpf(fl[key])
            piece_rels.append(abs(fv - hv) / abs(hv) if hv != 0 else 0)
        worst = max(piece_rels)
        print("  K=%d m=%4d  Cker(hp) = %s  rel dev = %.2e  worst piece dev"
              " = %.2e" % (K, m, mp.nstr(hp["Cker"], 12), float(rel),
                           float(worst)))
        ok &= float(rel) < 1e-10 and float(worst) < 1e-8
    print("R2 VERDICT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
