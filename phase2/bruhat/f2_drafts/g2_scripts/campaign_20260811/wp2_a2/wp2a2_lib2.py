"""wp2a2_lib2: the REFINED (real-part-split) Delta_ker bound, 2026-08-11.

Motivation (NC-A2 finding): the crude modulus route (wp2a2_lib.delta_ker_bound)
carries the bare odd-cube row  |z|^3/6 ~ alpha^3 t^9 / 6  of the exponential-
Taylor remainder, which enters the kernel bucket at order K^3 m^{-3/2} -- NOT
O(m^{-2}) -- making C_ker(K, m) non-monotone (growing ~ K^3 sqrt(m)) and
inflating K = 4 to ~6e4.  The TRUE Delta_ker is flat ~1.4-5.0/m^2 (wp2-b
NC-W4(6)): the alpha^3 term is PURELY IMAGINARY at leading order, and D,
p(k +- 1), phat are all REAL, so it cancels in every consumed quantity.  This
module makes that cancellation PROVABLE by tracking real and imaginary parts
of the model error separately (the tilted-frame analogue of the "odd-part
cancellation at the mean" of T2 Step 3 (b1), realized at the bucket level).

Construction (Lemma D.1 of the draft).  On |t| <= t1, with the exact
6th-order representation (T.9''):
    phi_lam^c(t) = e^{-s2 t^2/2} e^{-z(t)},   z = zR + i zI,
    zR = beta t^4 + gamma t^6 - Re R_7,  zI = alpha t^3 - delta t^5 - Im R_7,
and the model  phihat = e^{-s2 t^2/2} Q(t),  Q = 1 - U0 + U0^2/2 - D2
(the O(t^8) truncation of e^{-U0}, U0 = i alpha t^3 + beta t^4 - i delta t^5
+ gamma t^6; D2 = dropped degree 9..12 part of U0^2/2).  Write
    phi - phihat = e^{-s2 t^2/2} (DC(t) + i DS(t))        (both real).
With the coefficient boxes A3..A7 (wp2a2_lib), the majorant polynomials
    ZR = A4 t^4 + A6 t^6 + A7 t^7,   ZI = A3 t^3 + A5 t^5 + A7 t^7,
    UB = A3 t^3 + A4 t^4 + A5 t^5 + A6 t^6,
    R7X = A7 t^7 (1 + UB) + A7^2 t^14 / 2          [R_7 - U0 R_7 + R_7^2/2]
and EE(t) := e^{ZR(t)} <= e^{eps s2min t^2/2} (same eps as wp2a2_lib), the
exponential-Taylor remainder rem3 := e^{-z} - (1 - z + z^2/2) satisfies,
via  rem3 = -(z^3/2) int_0^1 (1-tau)^2 e^{-tau z} dtau,  |cos| <= 1,
|sin(tau zI)| <= tau |zI|, int (1-tau)^2 dtau = 1/3, int (1-tau)^2 tau = 1/12:
    |Re rem3| <= EE [ (ZR^3 + 3 ZR ZI^2)/6 + (3 ZR^2 ZI^2 + ZI^4)/24 ],
    |Im rem3| <= EE (ZR + ZI)^3 / 6 ,
whence   |DC| <= EE * WR,   |DS| <= EE * WI   with
    WR := (ZR^3 + 3 ZR ZI^2)/6 + (3 ZR^2 ZI^2 + ZI^4)/24 + R7X + ReD2b,
    WI := (ZR + ZI)^3/6 + R7X + ImD2b,
    ReD2b := (A4 A6 + A5^2/2) t^10 + (A6^2/2) t^12,
    ImD2b := (A3 A6 + A4 A5) t^9  + (A5 A6) t^11 .
Also |Re Q| <= 1 + VE, |Im Q| <= VO, |Re e^{-z}| <= EE, |Im e^{-z}| <= EE*ZI:
    VE := A4 t^4 + (A6 + A3^2/2) t^6 + (A4^2/2 + A3 A5) t^8,
    VO := A3 t^3 + A5 t^5 + A3 A4 t^7 .
Every polynomial here is EVEN in the odd-coefficient set {A3, A5, A7-odd
part} except WI, VO, ZI -- and those only ever meet another odd-family factor
inside the real-part kernel bucket, so no odd-degree monomial in (alpha,
delta) survives alone: the bare alpha^3 row is gone.

Everything else (out/tail/denominator assembly) as in wp2a2_lib, reused by
import.  All bounds conservative in the safe direction; provenance of inputs
identical to wp2a2_lib's docstring.
"""
import math
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
import wp2a2_lib as L

pmul, pscale, padd = L.pmul, L.pscale, L.padd
J, Jpoly, tail = L.J, L.Jpoly, L.tail


def pmul3(p, q, r):
    return pmul(pmul(p, q), r)


def split_polys(K, m, boxes=None):
    """Majorant monomial dicts for the real-part-split construction."""
    B = boxes or L.coef_boxes(K, m)
    A3, A4, A5, A6, A7 = B["A3"], B["A4"], B["A5"], B["A6"], B["A7"]
    ZR = {4: A4, 6: A6, 7: A7}
    ZI = {3: A3, 5: A5, 7: A7}
    UB = {3: A3, 4: A4, 5: A5, 6: A6}
    R7X = padd({7: A7}, pmul({7: A7}, UB), {14: A7 * A7 / 2.0})
    ReD2b = {10: A4 * A6 + A5 * A5 / 2.0, 12: A6 * A6 / 2.0}
    ImD2b = {9: A3 * A6 + A4 * A5, 11: A5 * A6}
    ZI2 = pmul(ZI, ZI)
    ZR2 = pmul(ZR, ZR)
    WR = padd(pscale(padd(pmul(ZR, ZR2), pscale(pmul(ZR, ZI2), 3.0)), 1 / 6.0),
              pscale(padd(pscale(pmul(ZR2, ZI2), 3.0), pmul(ZI2, ZI2)), 1 / 24.0),
              R7X, ReD2b)
    ZRI = padd(ZR, ZI)
    WI = padd(pscale(pmul3(ZRI, ZRI, ZRI), 1 / 6.0), R7X, ImD2b)
    VE = {4: A4, 6: A6 + A3 * A3 / 2.0, 8: A4 * A4 / 2.0 + A3 * A5}
    VO = {3: A3, 5: A5, 7: A3 * A4}
    return dict(B=B, ZR=ZR, ZI=ZI, WR=WR, WI=WI, VE=VE, VO=VO)


def delta_ker_bound2(K, m):
    """Refined explicit bound |Delta_ker| <= Cker2/m^2 (Theorem D.5).
    Same out/tail/denominator/assembly scheme as wp2a2_lib.delta_ker_bound;
    only the BOX pieces (kernel and pointwise) use the real-part split."""
    S = split_polys(K, m)
    B = S["B"]
    eps, t1, s2min, lamv = B["eps"], B["t1"], B["s2min"], B["lamv"]
    if eps >= 1.0:
        return None
    a = (1.0 - eps) * s2min / 2.0
    WR, WI, VE, VO, ZI = S["WR"], S["WI"], S["VE"], S["VO"], S["ZI"]
    c1 = L.C1K[K]
    far = 2.0 * (math.pi - t1) * math.exp(-c1 * m)

    # -- refined kernel box (Lemma D.3'): |Re[phi phi - phat phat]| route --
    #    pointwise bound e^{-a(s^2+t^2)} [ WR(s)*1 + (1+VE(s)) WR(t)
    #                                      + WI(s) ZI(t) + VO(s) WI(t) ],
    #    kernel (1-cos(s-t)) <= (s-t)^2/2, odd cross terms integrate to 0.
    def pair(p, q):     # int int p(s) q(t) (s^2+t^2)/2 e^{-a(s^2+t^2)}
        return 0.5 * (Jpoly(p, a, shift=2) * Jpoly(q, a)
                      + Jpoly(p, a) * Jpoly(q, a, shift=2))
    ONE = {0: 1.0}
    D_box = (pair(WR, ONE) + pair(padd(ONE, VE), WR)
             + pair(WI, ZI) + pair(VO, WI)) / (4.0 * math.pi ** 2)

    # -- out / tail: same as the crude route (they are far-exponent-driven) --
    VQ = L.vq_poly(K, m, B)
    cT = s2min / 2.0
    Ttail = tail(0, t1, cT) + sum(c * tail(n, t1, cT) for n, c in VQ.items())
    J0p_1VQ = J(0, cT) + Jpoly(VQ, cT)
    D_tail = 2.0 * Ttail * J0p_1VQ / math.pi ** 2
    int_phi = math.sqrt(math.pi / a) + far
    D_out = far * int_phi / math.pi ** 2
    DD = D_box + D_tail + D_out

    # -- refined pointwise error at x = +-1 (Lemma D.4'):
    #    E_pt = |Re int (phi - phat) e^{-itj}| <= int e^{-a t^2}(WR + |t| WI)
    #    (|sin(tj)| <= |t| for j = +-1) + far + model tail --
    E_pt = ((Jpoly(WR, a) + Jpoly(WI, a, shift=1)) / (2.0 * math.pi)
            + far / (2.0 * math.pi) + Ttail / math.pi)
    Pmin = L.P_min(K, m)
    P0min = L.P0_min(K, m)
    if Pmin <= 0 or P0min <= 0:
        return None
    dbar = math.sqrt(2.0 * math.pi * lamv) * math.exp(0.5 / s2min) * E_pt / Pmin
    delta_bar = 2.0 * dbar + dbar * dbar

    # -- v > 0 certificate (Lemma D.4', clause (iii)):
    #    s2 log F(0) >= LFlow := 1 - 12 b - 36 a^2/P0min^2 - PW/m^2 - T/m^2 --
    ah, bh, dh, gh, hh, _ = L.scaled_boxes(K, m)
    pw = L.pw_closed(K, m)
    tb = L.taylor_bucket(K, m)
    core = 12.0 * bh + 36.0 * ah * ah / P0min ** 2 + pw / m ** 2 + tb / m ** 2
    LFlow = 1.0 - core
    LF = 1.0 + core
    vS2 = LF * math.exp(LF / s2min)
    if LFlow <= 0 or delta_bar >= 1.0:
        return None
    s2wf = 2.0 * math.pi * lamv ** 2 * math.exp(1.0 / s2min) * DD / Pmin ** 2
    zbar = (s2wf / s2min + delta_bar * vS2 / s2min) / (1.0 - delta_bar)
    if zbar >= 1.0:
        return None
    Cker = m * m * (s2wf + delta_bar * vS2) / ((1.0 - delta_bar) * (1.0 - zbar))
    return dict(eps=eps, a=a, D_box=D_box, D_tail=D_tail, D_out=D_out, DD=DD,
                E_pt=E_pt, dbar=dbar, delta_bar=delta_bar, s2wf=s2wf,
                LFlow=LFlow, LF=LF, vS2=vS2, zbar=zbar, Cker=Cker,
                Pmin=Pmin, P0min=P0min, far=far, t1=t1, s2min=s2min,
                box_piece=m * m * 2.0 * math.pi * lamv ** 2
                * math.exp(1.0 / s2min) * D_box / Pmin ** 2,
                far_piece=m * m * 2.0 * math.pi * lamv ** 2
                * math.exp(1.0 / s2min) * D_out / Pmin ** 2,
                tail_piece=m * m * 2.0 * math.pi * lamv ** 2
                * math.exp(1.0 / s2min) * D_tail / Pmin ** 2,
                den_piece=m * m * delta_bar * vS2 / (1.0 - delta_bar))
