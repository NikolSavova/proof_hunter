# s4ref_a_recipe.py -- wave-6b numerics referee, sol_s4_20260812.md
# Scripts the draft's VERIFICATION RECIPE V1-V8 and EVERY displayed numeric
# constant of the m >= 700 pipeline (SOL.2/3/13/16/25/27/30/32/35/36/38-45,
# SOL.49-52), in exact rationals where possible, mpmath dps 60 elsewhere.
# Every check prints computed value vs the draft's claimed bound and PASS/FAIL.
from fractions import Fraction as F
import mpmath as mp
mp.mp.dps = 60

ok_all = True
def chk(name, cond, detail=""):
    global ok_all
    tag = "PASS" if cond else "FAIL"
    if not cond: ok_all = False
    print(f"  [{tag}] {name}  {detail}")

print("== [V1] basic scale (exact rationals) ==")
A0 = F(7,25)*700                      # 196
s20 = F(1960000, 7921)                # A0/0.89^2
eps0sq = 1/s20
chk("A0 = 196 exactly", A0 == 196, f"A0 = {A0}")
chk("s20 = 1960000/7921 > 247.44", s20 > F(24744,100), f"s20 = {float(s20):.6f}")
eps0 = mp.sqrt(mp.mpf(7921)/1960000)
chk("eps0 < 0.06358", eps0 < mp.mpf("0.06358"), f"eps0 = {mp.nstr(eps0, 10)}")
chk("4/sqrt(196) = 2/7 exactly (Taylor domain edge)", F(4,14) == F(2,7))
chk("mid range nonempty: 0.8*sqrt(196) = 11.2 > 4", F(8,10)*14 > 4)

print("== [SOL.13] alpha cap ==")
chk("5/168 < 0.0298", F(5,168) < F(298,10000), f"5/168 = {float(F(5,168)):.8f}")

print("== [SOL.15/16] remainder coefficient at A = 196, t/lam = 2/7 ==")
val = (F(672,100) + F(72,100)*F(2,7)/(1 - F(2,7))) / (24*196)
chk("(6.72 + 0.72*(2/7)/(5/7))/4704 = 876/588000 < 0.00149", val < F(149,100000),
    f"= {float(val):.8f} (exact {val})")
chk("0.00149 < 0.0021 (stated slack)", F(149,100000) < F(21,10000))

print("== [V2] local moments and E_loc ==")
M3, M5 = mp.mpf(4), mp.mpf(16)
M4 = 3*mp.sqrt(2*mp.pi); M6 = 15*mp.sqrt(2*mp.pi)
chk("M4 = 2^(5/2)Gamma(5/2)", abs(M4 - 2**mp.mpf(2.5)*mp.gamma(mp.mpf(2.5))) < mp.mpf(1e-50))
chk("M6 = 2^(7/2)Gamma(7/2)", abs(M6 - 2**mp.mpf(3.5)*mp.gamma(mp.mpf(3.5))) < mp.mpf(1e-49))
b = mp.mpf("0.0298")
u_max = mp.mpf("0.0021")*256
chk("0.0021*4^4 = 0.5376", abs(u_max - mp.mpf("0.5376")) < 1e-50)
# (SOL.25) validity: (e^u - 1)/u increasing => e^u - 1 <= [(e^U-1)/U] u <= e^U u
chk("(e^0.5376 - 1)/0.5376 <= e^0.5376  ((SOL.25) is valid, lossy)",
    (mp.e**u_max - 1)/u_max <= mp.e**u_max,
    f"sharp mult {mp.nstr((mp.e**u_max-1)/u_max, 8)} vs used {mp.nstr(mp.e**u_max, 8)}")
c = mp.mpf("0.0021")*mp.e**u_max
chk("c = 0.0021 e^0.5376 < 0.003596", c < mp.mpf("0.003596"), f"c = {mp.nstr(c, 8)}")
Eloc = [(b*M(3+j) + c*M(4+j))/(2*mp.pi) for j, M in
        [(0, lambda n: [None,None,None,M3,M4,M5,M6][n]),
         (1, lambda n: [None,None,None,M3,M4,M5,M6][n]),
         (2, lambda n: [None,None,None,M3,M4,M5,M6][n])]]
claims_loc = ["0.02328", "0.04482", "0.09741"]
for j in range(3):
    chk(f"E_loc[{j}] < {claims_loc[j]}", Eloc[j] < mp.mpf(claims_loc[j]),
        f"computed {mp.nstr(Eloc[j], 9)}  (margin {mp.nstr(mp.mpf(claims_loc[j])-Eloc[j], 3)})")

print("== [V3] mid integrals (erfc, dps 60) ==")
def I0(a): return mp.sqrt(mp.pi/a)/2*mp.erfc(4*mp.sqrt(a))
def I1(a): return mp.e**(-16*a)/(2*a)
def I2(a): return 4*mp.e**(-16*a)/(2*a) + I0(a)/(2*a)
a1, a2 = mp.mpf("0.32"), mp.mpf("0.5")
Emid = [(I0(a1)+I0(a2))/mp.pi, (I1(a1)+I1(a2))/mp.pi, (I2(a1)+I2(a2))/mp.pi]
claims_mid = ["0.00071", "0.00308", "0.01342"]
for j in range(3):
    chk(f"E_mid[{j}] < {claims_mid[j]}", Emid[j] < mp.mpf(claims_mid[j]),
        f"computed {mp.nstr(Emid[j], 9)}  (margin {mp.nstr(mp.mpf(claims_mid[j])-Emid[j], 3)})")

print("== [V4] crossover at m = 700 ==")
e1232 = mp.e**mp.mpf("-12.32")
chk("e^-12.32 ~ 4.46e-6", mp.mpf("4.45e-6") < e1232 < mp.mpf("4.47e-6"), f"= {mp.nstr(e1232, 6)}")
Ecross = [mp.mpf("0.274")*mp.mpf("1.074")**j/mp.pi * mp.mpf(700)**(F(1,2)*(j+1)) * e1232
          for j in range(3)]
claims_cross = ["1.04e-5", "2.94e-4", "0.00832"]
for j in range(3):
    chk(f"E_cross[{j}] < {claims_cross[j]}", Ecross[j] < mp.mpf(claims_cross[j]),
        f"computed {mp.nstr(Ecross[j], 8)}")
chk("monotone decr in m (worst j=2): 3/(2*700) < 0.0176", F(3,1400) < F(176,10000),
    f"{float(F(3,1400)):.6f} < 0.0176")

print("== [V5] far at m = 700 ==")
Efar = [mp.pi**j/(j+1) * (mp.mpf(700)**mp.mpf(1.5)/4)**(j+1) * mp.e**(-mp.mpf("0.0741")*700)
        for j in range(3)]
chk("E_far[2] < 1.1e-11", Efar[2] < mp.mpf("1.1e-11"), f"computed {mp.nstr(Efar[2], 6)}")
chk("E_far[0], E_far[1] smaller than E_far[2]", Efar[0] < Efar[2] and Efar[1] < Efar[2],
    f"= {mp.nstr(Efar[0],4)}, {mp.nstr(Efar[1],4)}")
chk("far monotone decr: 4.5/700 < 0.0741", F(45,7000) < F(741,10000))

print("== [V6] totals ==")
Etot = [Eloc[j]+Emid[j]+Ecross[j]+Efar[j] for j in range(3)]
claims_tot = ["0.02401", "0.04820", "0.11916"]; budget = ["0.04", "0.06", "0.13"]
for j in range(3):
    chk(f"E{j} < {claims_tot[j]} < {budget[j]}",
        Etot[j] < mp.mpf(claims_tot[j]) and mp.mpf(claims_tot[j]) < mp.mpf(budget[j]),
        f"computed {mp.nstr(Etot[j], 9)}  (margin to displayed {mp.nstr(mp.mpf(claims_tot[j])-Etot[j], 3)})")

print("== [V7] normal bounds on |z| <= eps0 = 0.06358 and f-interval ==")
z = mp.mpf("0.06358")
g0 = 1/mp.sqrt(2*mp.pi)
gz = mp.e**(-z*z/2)/mp.sqrt(2*mp.pi)
# monotonicity: g decr on [0, z]; z*g(z) incr on [0,1]; (1-z^2)g(z) decr on [0,1]
chk("g_min = g(0.06358) > 0.39813", gz > mp.mpf("0.39813"), f"= {mp.nstr(gz, 9)}")
chk("g_max = g(0) < 0.39895", g0 < mp.mpf("0.39895"), f"= {mp.nstr(g0, 9)}")
gp = z*gz
chk("|g'| max = z g(z) < 0.02532", gp < mp.mpf("0.02532"), f"= {mp.nstr(gp, 9)}")
gpp_min = (1-z*z)*gz; gpp_max = g0
chk("-g'' in (0.39652, 0.39895)", gpp_min > mp.mpf("0.39652") and gpp_max < mp.mpf("0.39895"),
    f"min = {mp.nstr(gpp_min, 9)}, max = {mp.nstr(gpp_max, 9)}")
E0c, E1c, E2c = mp.mpf("0.04"), mp.mpf("0.06"), mp.mpf("0.13")
f_lo = mp.mpf("0.39813") - E0c; f_hi = mp.mpf("0.39895") + E0c
chk("f in (0.35813, 0.43895)", abs(f_lo-mp.mpf("0.35813"))<1e-40 and abs(f_hi-mp.mpf("0.43895"))<1e-40,
    f"({mp.nstr(f_lo,7)}, {mp.nstr(f_hi,7)})")
fp_hi = mp.mpf("0.02532") + E1c
chk("|f'| < 0.08532", abs(fp_hi-mp.mpf("0.08532"))<1e-40, f"= {mp.nstr(fp_hi,7)}")
fpp_lo = mp.mpf("0.39652") - E2c; fpp_hi = mp.mpf("0.39895") + E2c
chk("-f'' in (0.26652, 0.52895)", abs(fpp_lo-mp.mpf("0.26652"))<1e-40 and abs(fpp_hi-mp.mpf("0.52895"))<1e-40,
    f"({mp.nstr(fpp_lo,7)}, {mp.nstr(fpp_hi,7)})")
Hmin = mp.mpf("0.26652")/mp.mpf("0.43895")
Hmax = mp.mpf("0.52895")/mp.mpf("0.35813") + (mp.mpf("0.08532")/mp.mpf("0.35813"))**2
chk("H_min > 0.607", Hmin > mp.mpf("0.607"), f"= {mp.nstr(Hmin, 9)}")
chk("H_max < 1.535", Hmax < mp.mpf("1.535"), f"= {mp.nstr(Hmax, 9)}")

print("== [V8] final conversion ==")
Xmax = mp.mpf("1.535")*mp.e**(mp.mpf("1.535")/mp.mpf("247.44"))
chk("X_max = 1.535 e^(1.535/247.44) < 1.545", Xmax < mp.mpf("1.545"), f"= {mp.nstr(Xmax, 9)}")
final = max(1 - mp.mpf("0.607"), Xmax - 1)
chk("max(1-0.607, X_max-1) < 0.545 < 0.89", final < mp.mpf("0.545"), f"= {mp.nstr(final, 9)}")
# symmetric-difference identity kernel: 2*int_0^eps (eps-t) dt = eps^2 (exact)
chk("2 int_0^eps (eps - t) dt = eps^2 (exact, Fraction check at eps=1)",
    2*(F(1,1) - F(1,2)) == 1)

print()
print("== margin ledger (distance of computed value to the draft's displayed cap) ==")
for j in range(3):
    print(f"  E_loc[{j}]: {mp.nstr(mp.mpf(claims_loc[j])-Eloc[j], 3)}   "
          f"E_mid[{j}]: {mp.nstr(mp.mpf(claims_mid[j])-Emid[j], 3)}   "
          f"E_cross[{j}]: {mp.nstr(mp.mpf(claims_cross[j])-Ecross[j], 3)}")
print(f"  S4 recipe arithmetic: {'ALL PASS' if ok_all else 'FAILURES PRESENT'}")
