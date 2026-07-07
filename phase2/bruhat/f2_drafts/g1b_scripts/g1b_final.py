import math, sys, os
import numpy as np
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "g1b_const2.py")).read().split("# ---------------- assemble C2 table")[0])

# pointwise thresholds: sigma*Theta_pt*m^3 at candidate m
def theta_pt(m1):
    L = lam(m1); t1 = math.sqrt(2)*math.pi/m1; q1 = L*t1*t1/2
    far = 2*math.exp(-0.19314*m1)
    mid = math.exp(-q1)/(math.pi*L*t1)
    mtail = (math.exp(-q1)/math.pi)*( tailmom(0,t1,L) +
        sum(v/m1**q*L**n*tailmom(n,t1,L) for (n,q),v in V.items()) )
    return far+mid+mtail
def tailmom(n, a, L):
    val = 1.0/(L*a)
    for k in range(1, n+1): val = a**(2*k-1)/L + (2*k-1)/L*val
    return val
print("== pointwise superpoly: sigma*Theta_pt*m^3 ==")
for m1 in (100,105,110,120,150):
    print(f"  m={m1}: {math.sqrt(lam(m1))*theta_pt(m1)*m1**3:.4f}   C1''={C1pp(m1):.4f}")
c1first = (15*B2hi + 52.5*B1hi**2)/SQ2PI
print(f"first-order He6/He8 pulldown constant = {c1first:.4f};  C1 total at m=110: {c1first + (C1pp(110)+0.4)/110:.4f}")

def superpoly(y0, m1, Pm):
    L = lam(m1); t1 = math.sqrt(2)*math.pi/m1; q1 = L*t1*t1/2.0
    far = 2*math.exp(-0.19314*m1)
    intV_R  = math.sqrt(2*math.pi/L)*(1 + sum(v/m1**q*dfact(2*n-1) for (n,q),v in V.items()))
    intV_tail = math.exp(-q1)*( tailmom(0,t1,L) + sum(v/m1**q*L**n*tailmom(n,t1,L) for (n,q),v in V.items()) )
    DD_tail = (1/math.pi**2)*2*intV_tail*intV_R*2
    qout = 2*(math.exp(-q1)/(L*t1) + math.pi*far)
    qall = math.sqrt(2*math.pi/L) + qout
    DD_out = (1/math.pi**2)*qout*qall*2
    return theta_pt(m1), 2*math.pi*L*L*(DD_tail+DD_out)

print("\n== final C2 table ==")
print(f"{'y0':>4} {'m1':>5} {'A2N':>8} {'Pmin':>6} {'boxE':>8} {'deltE':>8} {'spE':>8} {'C2':>9} {'C2 rounded':>10}")
rows = ((0.1,180),(0.5,180),(1.0,180),(2.0,200),(3.0,230),(3.0,2000))
for y0, m1 in rows:
    A2N, Pm, l2, l4, hbar = bounds_at(y0, m1)
    Th_pt, SP = superpoly(y0, m1, Pm)
    ey = math.exp(y0*y0 + hbar*hbar)
    boxE  = ey/Pm**2 * KB(m1)/m1
    spE   = ey/Pm**2 * SP * m1*m1
    sig = math.sqrt(lam(m1))
    dbar = SQ2PI*math.exp((y0+hbar)**2/2)*(C1pp(m1)/m1**3 + sig*Th_pt)/Pm
    lamv = (1+l2)*(1+2/lam(m1))
    deltE = m1*m1*(2*dbar+dbar**2)*lamv/(1-min(2*dbar+dbar**2,0.5))
    taylE = 3*l4/m1
    C2 = (A2N/Pm**2 + (boxE+spE+deltE)*1.02 + taylE)
    print(f"{y0:>4} {m1:>5} {A2N:>8.3f} {Pm:>6.3f} {boxE:>8.3f} {deltE:>8.4f} {spE:>8.4f} {C2:>9.3f} {math.ceil(C2*10)/10:>10}")

# measured truth on smaller windows for honesty lines
sys.path.insert(0, "/Users/sihaohuang/Desktop/Coding/proof_hunter/phase2/bruhat")
from mahonian import mahonian
print("\n== measured max m^2|E1| per window (m=40,60) ==")
for m in (40,60):
    a = mahonian(m); N = m*(m-1)//2
    L = lam(m); sig = math.sqrt(L)
    S4 = sum(j**4 for j in range(1,m+1)); Bm = (S4-m)/240.0/L**2
    la = [math.log(x) for x in a]
    for y0 in (0.5,1.0,2.0,3.0):
        vals = [abs(L*(2*la[k]-la[k-1]-la[k+1]) - 1 - Bm*(((k-N/2)/sig)**2-1))
                for k in range(1,N) if abs((k-N/2)/sig) <= y0]
        print(f"  m={m} y0={y0}: measured {m*m*max(vals):.3f}")
