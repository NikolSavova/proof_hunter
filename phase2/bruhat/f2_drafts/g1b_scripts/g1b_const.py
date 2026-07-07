# All explicit constants for g1_draft_b (GAP G1 closure). Sections 1-6.
import math, numpy as np
from fractions import Fraction

SQ2PI = math.sqrt(2*math.pi)

def lam_exact(m): return Fraction(m*(m-1)*(2*m+5), 72)
def S(r, m): return sum(j**r for j in range(1, m+1))
def b_exact(m):  return Fraction(S(4,m)-m, 2880) / lam_exact(m)**2
def g_exact(m):  return Fraction(S(6,m)-m, 181440) / lam_exact(m)**3
def c8s_exact(m):  # c8/lam^4 with c8 = (m+1)^9/43545600  (t1 = sqrt2*pi/m version)
    return Fraction((m+1)**9, 43545600) / lam_exact(m)**4

# ---------------- Section 1: uniform coefficient bounds ----------------
print("== S1: coefficient bounds ==")
bs  = [(m, float(b_exact(m))*m)      for m in list(range(11,200))+list(range(200,3001,50))+[10**4,10**5]]
gs  = [(m, float(g_exact(m))*m*m)    for m in list(range(30,200))+list(range(200,3001,50))+[10**4,10**5]]
c8s = [(m, float(c8s_exact(m))*m**3) for m in list(range(30,200))+list(range(200,3001,50))+[10**4,10**5]]
print("b*m   : max(m>=11) = %.6f  min(m>=30) = %.6f  (claim <=0.0900, >=0.0890 for m>=30)"
      % (max(v for _,v in bs), min(v for m,v in bs if m>=30)))
print("g*m^2 : max(m>=30) = %.6f  min(m>=30) = %.6f" % (max(v for _,v in gs), min(v for _,v in gs)))
print("c8s*m^3: max(m>=30) = %.6f (claim <= 0.0431)" % max(v for _,v in c8s))
print("h^2*m^3 = 72 m^2/((m-1)(2m+5)) <= 36 for m>=2: at m=30 :", 72*900/(29*65))
B1hi, B1lo = 0.0900, 0.0890     # b*m in [B1lo,B1hi], m>=30
B2hi, B2lo = 0.03674, 0.03540   # g*m^2  (check min above!)
B3hi = 0.0431                   # c8s*m^3
H2M3 = 36.0                     # h^2 <= 36/m^3

# polynomial-inequality certificates (referee-checkable): roots of RHS-LHS
import sympy as sp
mm = sp.symbols('m', positive=True)
S4 = mm*(mm+1)*(2*mm+1)*(3*mm**2+3*mm-1)/30
S6 = sp.expand(sp.Rational(1,42)*(6*mm**7+21*mm**6+21*mm**5-7*mm**3+mm))
lamP = mm*(mm-1)*(2*mm+5)/72
checks = {
 "b<=0.0900/m (m>=11)":  sp.expand( sp.Rational(9,100)/mm*2880*lamP**2 - (S4-mm) ),
 "b>=0.0890/m (m>=30)":  sp.expand( (S4-mm) - sp.Rational(89,1000)/mm*2880*lamP**2 ),
 "g<=0.03674/m^2 (m>=30)": sp.expand( sp.Rational(3674,100000)/mm**2*181440*lamP**3 - (S6-mm) ),
 "g>=0.03540/m^2 (m>=30)": sp.expand( (S6-mm) - sp.Rational(3540,100000)/mm**2*181440*lamP**3 ),
 "c8s<=0.0431/m^3 (m>=30)": sp.expand( sp.Rational(431,10000)/mm**3*43545600*lamP**4 - (mm+1)**9 ),
}
for name, expr in checks.items():
    num = sp.fraction(sp.together(expr))[0]
    rts = [sp.re(r) for r in sp.Poly(num, mm).nroots() if abs(sp.im(r)) < 1e-9]
    print(f"  {name}: largest real root = {max(rts):.3f}  (must be < threshold)")

# S6 formula sanity
assert S6.subs(mm,30) == S(6,30), "S6 formula check"
print("  S6 closed form OK")
