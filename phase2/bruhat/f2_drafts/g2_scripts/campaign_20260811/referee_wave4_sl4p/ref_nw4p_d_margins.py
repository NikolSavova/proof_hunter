#!/usr/bin/env python3
# ref_nw4p_d_margins.py -- adversarial numerics referee, wave4_sl4p.
# [D1] SS5 'binding entry' claim: decompose the W1 row at w = 4.05, m = 401
#      into share contributions (X vs far vs dec-bucket).
# [D2] the two thin-margin rows (W5 0.9891, W7 0.9808) re-certified at dps 100.
# [D3] far-entry m-decrease threshold: 5.5/0.0741 (draft: 'for m >= 75').
# [D4] efac(0.8) and the C5* <= 0.8464 acceptance-grid consistency.
import mpmath as mp
mp.mp.dps = 100
exec(open('/Users/sihaohuang/Desktop/Coding/proof_hunter/phase2/bruhat/f2_drafts/'
          'g2_scripts/campaign_20260811/referee_wave4_sl4p/ref_nw4p_b_sliver.py')
     .read().split("print(\"== [B1]")[0])   # reuse defs at dps 100

print("== [D1] W1 row decomposition at w = 4.05, m = 401 (SS5 claims X-share 0.68, far-share 0.11) ==")
b = BANDS[0]; m = 401; w = mp.mpf('4.05')
name,wlo,whi,R31,R42,cAd,C5,gam = b
R31=mp.mpf(R31); R42=mp.mpf(R42); cAd=mp.mpf(cAd); C5=mp.mpf(C5)
A0 = cAd*m; g = mp.mpf(gam)
main = R42/2 + mp.mpf('0.3')*R31**2 + (mp.mpf(whi)/m)**2/2
R5n = 48*SQ2PI/mp.pi*C5*efac(C5)/mp.sqrt(A0); R5d = R5n/6
cube = mp.mpf('2.37')*R31**3/mp.sqrt(A0)
cross = (mp.mpf('2.13')*R31*R42+mp.mpf('0.56')*R42**2)/mp.sqrt(A0)
midn = KMID*A0**mp.mpf('1.5')/(4*g)*mp.e**(-g*A0/4)*(1+2/(g*A0))
midd = KMID*mp.sqrt(A0)/g*mp.e**(-g*A0/4)
dec = main + INFL*(R5n+cube+cross+midn+R5d+midd)
Xn, Xd = X_w6(w, m, mp.mpf(m))
lamL = mp.mpf(wlo)/m; s2max = m/(4*mp.sinh(lamL/2)**2)
Fn = 2*SQ2PI*m*s2max**mp.mpf('1.5')*mp.e**(-FAR*m)
Fd = m*mp.sqrt(2*mp.pi*s2max)*mp.e**(-FAR*m)
sh_dec = dec/(20*cAd)*(1+QUADF)
sh_X   = INFL*(Xn+Xd)/20*(1+QUADF)
sh_far = INFL*(Fn+Fd)/20*(1+QUADF)
tot = sh_dec + sh_X + sh_far
print(f"  tot = {mp.nstr(tot,6)} (FAIL expected, w below w_dagger) | dec-share = {mp.nstr(sh_dec,4)}"
      f"  X-share = {mp.nstr(sh_X,4)}  far-share = {mp.nstr(sh_far,4)}")
print(f"  m*x(4.05, 0.8) = {mp.nstr(401*w6_x('4.05', mp.mpf('0.8'), 401),5)} (draft: 7.65)")

print("\n== [D2] thin-margin rows at dps 100 ==")
for bb, quoted in [(BANDS[4], '0.9891'), (BANDS[6], '0.9808'), (BANDS[1], '0.8601')]:
    tot = row(bb, 401)
    print(f"  {bb[0]:3s}: tot = {mp.nstr(tot,12)}  <= 1: {tot <= 1}  margin = {mp.nstr(1-tot,6)}  (quoted {quoted})")

print("\n== [D3] far-entry decrease threshold ==")
print(f"  5.5/0.0741 = {mp.nstr(mp.mpf('5.5')/FAR,6)}  (draft: 'grows faster ... for m >= 75'; "
      f"74.23 <= 75 so the claim is safe-direction)")

print("\n== [D4] efac values on the acceptance grid ==")
for c in ['0.05','0.06','0.08','0.10','0.15','0.25','0.4','0.8']:
    print(f"  efac({c}) = {mp.nstr(efac(c),6)}")
print(f"  20 * 0.9891 = {mp.nstr(20*mp.mpf('0.9891'),6)} (draft: 19.78 <= 20)")
print(f"  1/0.28 = {mp.nstr(1/mp.mpf('0.28'),6)} (draft SS6: 'up to 3.57x')")
