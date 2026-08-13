#!/usr/bin/env python3
"""Exact rational audit of the finite cases in the block-family bound proof."""
from fractions import Fraction
import json, math

record=Fraction(85,294)
exception_limits={2:3,3:9,4:12,5:5,6:2}
rows=[]
equality=[]
for s,amax in exception_limits.items():
 best=(Fraction(-1),None)
 for a in range(2,amax+1):
  c=s*s-s+2
  full_B=c*a*a-2*a+s+2
  lower=(s+1)*a
  star=Fraction(2*full_B,s*a)
  candidates={lower,max(lower,star.numerator//star.denominator),max(lower,math.ceil(star))}
  for L in candidates:
   m=s*a*L-c*a*a+2*a-s-2
   ratio=Fraction(m,L*L)
   if ratio>best[0]:best=(ratio,(a,L,m))
   if ratio==record:equality.append({'s':s,'a':a,'L':L,'m':m})
 rows.append({'s':s,'a_max_checked':amax,'maximum':str(best[0]),
              'at':{'a':best[1][0],'L':best[1][1],'m':best[1][2]}})
assert all(Fraction(row['maximum'])<=record for row in rows)
assert equality==[{'s':4,'a':6,'L':42,'m':510}]
print(json.dumps({'record':str(record),'exception_rows':rows,
                  'equality_cases':equality,
                  'large_parameter_bound':'Equation (2) in THEORY_NOTES.md'},indent=2))
