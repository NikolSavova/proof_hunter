#!/usr/bin/env python3
# ref_e_r1_exact_recert.py -- REFEREE (numerics, wave-5 sl4pe): independent
# exact-rational recertification of Lemma E.2's constants REM*(W), J0(W),
# written FROM THE DRAFT TEXT (wave5_sl4pe_20260812.md Lemma E.2 Steps 0-5),
# not from e1_pricing_certificate.py.  Compares against the archived exact
# J0 fractions of out_e1_pricing_certificate.txt [2] and audits the rounding
# direction of the 6-sig-fig float copies carried by e2_truth_margins.py.
from fractions import Fraction as Fr

M0 = 561
S0 = Fr(1122800, 7921)
E0 = Fr(1) / S0

# (band, c_A, R31*, R42*, wmax) -- wmax None => W7, lam <= 89/100
BANDS = [('W1', Fr(28,100), Fr(1),      Fr(4,5),   Fr(5)),
         ('W2', Fr(35,100), Fr(6,5),    Fr(7,5),   Fr(6)),
         ('W3', Fr(42,100), Fr(3,2),    Fr(13,5),  Fr(8)),
         ('W4', Fr(52,100), Fr(17,10),  Fr(7,2),   Fr(10)),
         ('W5', Fr(3,5),    Fr(2),      Fr(26,5),  Fr(20)),
         ('W6b',Fr(7,10),   Fr(21,10),  Fr(6),     Fr(40)),
         ('W7', Fr(4,5),    Fr(11,5),   Fr(33,5),  None)]

# archived exact J0 fractions from out_e1_pricing_certificate.txt line [2]
ARCHIVED_J0 = {
 'W1': Fr(57118994397115584673581017925677, 83636677924642268545373517242925),
 'W2': Fr(8780262582038667260419032112399, 7962646693509388441518013303500),
 'W3': Fr(23226752114049600942786345918529, 12124924040534855811562282250412),
 'W4': Fr(51023670104731644648292691510971089029, 20116161940562749876981457575487758500),
 'W5': Fr(245090904838186778621087950886801, 66819881289258331982063507145735),
 'W6b': Fr(4920815274788484069344938110131077, 1177774992986013038502688349299500),
 'W7': Fr(14348506522021163951398568763173, 3121975792131000476837815995000)}

# 6-sig-fig float copies hard-coded in e2_truth_margins.py (REMSTAR dict)
E2_REMSTAR = {'W1': '0.0170581', 'W2': '0.0293186', 'W3': '0.0593796',
              'W4': '0.0805485', 'W5': '0.132066', 'W6b': '0.144939',
              'W7': '0.15603'}

print("== referee r1: independent exact recertification of Lemma E.2 ==")
print(f"  S0 = {S0} = {float(S0):.8f}, E0 = {float(E0):.10f}")
all_match = True
all_checks = True
for (W, cA, R31, R42, wmax) in BANDS:
    A0  = cA * M0
    Lam = wmax / M0 if wmax is not None else Fr(89, 100)
    Jst = R42/2 + Fr(3,10) * R31**2          # J* (draft (E3) display)
    # Step 0: |r42| <= R42+ = max(R42*, 2 J*)
    R42d = max(R42, 2*Jst)
    # Step 1
    bb = R42d / (24 * A0)
    aa = R31**2 / (36 * A0)
    # Step 2
    xb = 3*bb + 15*(aa/2)
    sb = 6*bb + 30*(aa/2)
    db = 2*xb + xb*xb + 9*E0*aa
    eb_exp = E0 / (1 - E0)                    # e^{eps2} - 1 <= E0/(1-E0)
    ph = (eb_exp + db) / (1 - db)
    Dlo = (1 - xb)**2 - 9*E0*aa
    pos = (Dlo > 0) and (1 - 3*bb - 15*(aa/2) > 0) and (1 - xb - (aa + 9*E0)/2 > 0)
    # Step 3 (draft text endpoints)
    Cb_hi, Cb_lo = 6*(2 + sb), (6 - E0)*(2 - sb)
    e_b = max(Cb_hi/24 - Fr(1,2), Fr(1,2) - Cb_lo/24)
    Ca_hi = 9 - (45 - 15*E0)*(1 - sb/2)
    Ca_lo = 9 - 6*E0 - 45*(1 + sb/2)
    e_a = max(abs(Ca_hi + 36), abs(Ca_lo + 36)) / 36
    # Step 4
    M0cap = max(R42/2, Jst)
    Mdev = e_b*R42d + e_a*R31**2
    # Step 5
    REM2 = (1 + ph)*Mdev + ph*M0cap
    d1 = Lam**2 * E0 / (6 * (1 - E0/4))
    REMs = REM2 + d1
    J0 = Jst - REMs
    up_ok = REMs <= Fr(3,10)*R31**2
    match = (J0 == ARCHIVED_J0[W])
    all_match = all_match and match
    all_checks = all_checks and up_ok and pos
    # rounding-direction audit of e2's float copy
    e2f = Fr(E2_REMSTAR[W])                   # the decimal literal, exactly
    dirn = ('BELOW exact (J-check side anti-conservative by %.2e; REMact side conservative)'
            % float(REMs - e2f)) if e2f < REMs else \
           ('ABOVE exact (REMact side anti-conservative by %.2e; J-check side conservative)'
            % float(e2f - REMs)) if e2f > REMs else 'EXACT'
    print(f"  {W:3s}: REM* = {float(REMs):.12f}  J0 = {float(J0):.12f}  "
          f"J0 == archived fraction: {match}  REM*<=0.3R31^2: {up_ok}  pos: {pos}")
    print(f"       e2 float copy {E2_REMSTAR[W]} is {dirn}")
print(f"  ALL J0 fractions match archived e1 output: {all_match}")
print(f"  ALL upper-side + positivity checks: {all_checks}")

# extra referee check: R42+ = 2 J* strictly > R42* on every band (draft Step 0
# note) and J0 > 0 on every band (needed for the internal r42 lower cap)
print("  R42+ = 2J* > R42* on every band:",
      all(2*(R42/2 + Fr(3,10)*R31**2) > R42 for (_, _, R31, R42, _) in BANDS))
