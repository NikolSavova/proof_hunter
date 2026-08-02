# Stdlib-decimal (60+ digit) reimplementation of g1b_lemA.py (mpmath unavailable).
# Checks Lemma B.1: |phi - phihat| <= e^{-lam t^2/2} W(t) on (0, t_1], t_1 = sqrt2*pi/m.
from decimal import Decimal, getcontext
from fractions import Fraction

getcontext().prec = 80

PI = Decimal("3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211707")

def dsin(x):
    # Taylor series; |x| <= ~2.3 here so plain series converges fast.
    term = x
    s = x
    n = 1
    x2 = x * x
    while True:
        term = -term * x2 / ((2 * n) * (2 * n + 1))
        s += term
        n += 1
        if abs(term) < Decimal(10) ** (-78):
            return s

def check(m, npts=400):
    lam = Decimal(m * (m - 1) * (2 * m + 5)) / 72
    S4 = sum(j**4 for j in range(1, m + 1)); S6 = sum(j**6 for j in range(1, m + 1))
    beta = Decimal(S4 - m) / 2880
    gam = Decimal(S6 - m) / 181440
    c8 = Decimal((m + 1) ** 9) / 43545600
    t1 = Decimal(2).sqrt() * PI / m
    worst = Decimal(0); wt = None
    for i in range(1, npts + 1):
        t = t1 * i / npts
        phi = Decimal(1)
        s_half = dsin(t / 2)
        for j in range(2, m + 1):
            phi *= dsin(j * t / 2) / (j * s_half)
        eh = (-lam * t * t / 2).exp()
        phihat = eh * (1 - beta * t**4 - gam * t**6 + beta**2 / 2 * t**8)
        U = beta * t**4 + gam * t**6 + c8 * t**8
        W = c8 * t**8 + beta * t**4 * (gam * t**6 + c8 * t**8) \
            + (gam * t**6 + c8 * t**8) ** 2 / 2 + U**3 / 6
        r = abs(phi - phihat) / (eh * W)
        if r > worst:
            worst, wt = r, t / t1
    print(f"  m={m}: max ratio = {float(worst):.6f} at t/t1={float(wt):.4f}  (must be <= 1)")

for m in (10, 20, 40, 60, 100):
    check(m)
