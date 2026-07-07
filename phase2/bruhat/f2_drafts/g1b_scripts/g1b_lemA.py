# Lemma A check in exact-ish arithmetic (mpmath, 60 digits)
import mpmath as mp
mp.mp.dps = 60

def check(m, npts=400):
    lam = mp.mpf(m*(m-1)*(2*m+5))/72
    S4 = sum(j**4 for j in range(1,m+1)); S6 = sum(j**6 for j in range(1,m+1))
    beta = mp.mpf(S4-m)/2880; gam = mp.mpf(S6-m)/181440
    c8 = mp.mpf((m+1)**9)/43545600
    t1 = mp.sqrt(2)*mp.pi/m
    worst = mp.mpf(0); wt = None
    for i in range(1, npts+1):
        t = t1*i/npts
        phi = mp.mpf(1)
        for j in range(2, m+1): phi *= mp.sin(j*t/2)/(j*mp.sin(t/2))
        eh = mp.e**(-lam*t*t/2)
        phihat = eh*(1 - beta*t**4 - gam*t**6 + beta**2/2*t**8)
        U = beta*t**4 + gam*t**6 + c8*t**8
        W = c8*t**8 + beta*t**4*(gam*t**6+c8*t**8) + (gam*t**6+c8*t**8)**2/2 + U**3/6
        r = abs(phi-phihat)/(eh*W)
        if r > worst: worst, wt = r, t/t1
    print(f"  m={m}: max ratio = {mp.nstr(worst,6)} at t/t1={mp.nstr(wt,4)}  (must be <= 1)")

for m in (10, 20, 40, 60, 100):
    check(m)
