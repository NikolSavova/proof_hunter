# s4ref_f_gap561.py -- REFEREE'S OWN sizing (not the draft's) of the [561, 699]
# scope gap: re-run the draft's architecture at m in [561, 699] with the only
# necessary modification -- local range |y| <= y_max(m) = (2/7) sqrt(A_min(m)),
# A_min(m) = 0.28 m (so the (SOL.14) Taylor domain |t|/lam <= 2/7 is preserved),
# alpha cap 5/(12 sqrt(A_min)), remainder coeff (1/(24 A_min))(6.72 + 0.288),
# same cited inputs (SL3' 0.32 mid, R.1 floor 0.0176 [stated m >= 561],
# A3(ii) far floor 0.0741). Purpose: quantify whether the draft's WHAT-REMAINS
# item 2 ("run the same C^2 estimate at m = 561 with slightly enlarged
# derivative budgets") is actually workable, i.e. whether the gap is
# repairable-in-kind against the (S4) target 0.89.
import mpmath as mp
mp.mp.dps = 40

def gauss_int(j, x, a):
    # int_x^inf y^j e^{-a y^2} dy, j = 0, 1, 2
    if j == 0: return mp.sqrt(mp.pi/a)/2*mp.erfc(x*mp.sqrt(a))
    if j == 1: return mp.e**(-a*x*x)/(2*a)
    if j == 2: return x*mp.e**(-a*x*x)/(2*a) + gauss_int(0, x, a)/(2*a)

def moment(n):
    # int_R |y|^n e^{-y^2/2} dy
    return 2**((n+1)/mp.mpf(2))*mp.gamma((n+1)/mp.mpf(2))

def size_at(m):
    Amin = mp.mpf("0.28")*m
    ymax = mp.mpf(2)/7*mp.sqrt(Amin)
    s2min = Amin/mp.mpf("0.89")**2
    eps = 1/mp.sqrt(s2min)
    alpha = mp.mpf(5)/(12*mp.sqrt(Amin))
    cprime = (mp.mpf("6.72") + mp.mpf("0.288"))/(24*Amin)
    umax = cprime*ymax**4
    cdd = cprime*mp.e**umax          # (SOL.25)-style linearization
    Eloc = [(alpha*moment(j+3) + cdd*moment(j+4))/(2*mp.pi) for j in range(3)]
    Emid = [(gauss_int(j, ymax, mp.mpf("0.32")) + gauss_int(j, ymax, mp.mpf("0.5")))/mp.pi
            for j in range(3)]
    ec = mp.e**(-mp.mpf("0.0176")*m)
    Ecross = [mp.mpf("0.274")*mp.mpf("1.074")**j/mp.pi*mp.mpf(m)**((j+1)/mp.mpf(2))*ec
              for j in range(3)]
    ef = mp.e**(-mp.mpf("0.0741")*m)
    Efar = [mp.pi**j/(j+1)*(mp.mpf(m)**mp.mpf("1.5")/4)**(j+1)*ef for j in range(3)]
    E = [Eloc[j]+Emid[j]+Ecross[j]+Efar[j] for j in range(3)]
    g0 = 1/mp.sqrt(2*mp.pi)
    gz = mp.e**(-eps*eps/2)/mp.sqrt(2*mp.pi)
    f_lo = gz - E[0]; f_hi = g0 + E[0]
    fp = eps*gz + E[1]
    fpp_lo = (1-eps*eps)*gz - E[2]; fpp_hi = g0 + E[2]
    Hmin = fpp_lo/f_hi
    Hmax = fpp_hi/f_lo + (fp/f_lo)**2
    Xmax = Hmax*mp.e**(Hmax/s2min)
    bound = max(1 - Hmin, Xmax - 1)
    return ymax, E, Hmin, Hmax, bound

print("== referee gap sizing: draft architecture at m in [561, 699], y_max = (2/7) sqrt(0.28 m) ==")
print("   (uses only inputs the draft already cites; R.1 floor is stated for m >= 561)")
worst = -mp.mpf(1); worst_m = None
for m in [561, 575, 600, 625, 650, 675, 699]:
    ymax, E, Hmin, Hmax, bound = size_at(m)
    ok = bound < mp.mpf("0.89")
    if bound > worst: worst, worst_m = bound, m
    print(f"  m={m}: y_max={mp.nstr(ymax,5)}  E0={mp.nstr(E[0],4)} E1={mp.nstr(E[1],4)} E2={mp.nstr(E[2],4)}"
          f"  H=({mp.nstr(Hmin,5)}, {mp.nstr(Hmax,5)})  |s2(r-1)-1| < {mp.nstr(bound,5)}"
          f"  vs 0.89: {'CLOSES' if ok else 'FAILS'}")
print(f"  worst bound on the gap range: {mp.nstr(worst,6)} at m = {worst_m}"
      f"  ({'the gap is repairable-in-kind' if worst < mp.mpf('0.89') else 'NOT repairable this way'})")
print()
print("== same sizing at m = 700 (consistency with the draft's own numbers) ==")
ymax, E, Hmin, Hmax, bound = size_at(700)
print(f"  m=700: y_max={mp.nstr(ymax,5)}  E0={mp.nstr(E[0],4)} E1={mp.nstr(E[1],4)} E2={mp.nstr(E[2],4)}"
      f"  H=({mp.nstr(Hmin,5)}, {mp.nstr(Hmax,5)})  bound {mp.nstr(bound,5)}")
print("  (y_max = 4 exactly at m = 700; matches the draft's setup, modulo its rounded-up E budgets)")
