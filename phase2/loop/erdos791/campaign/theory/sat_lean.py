#!/usr/bin/env python3
"""Lean CP-SAT encoding for the smaller one-square-short family instances.

This deliberately disables CP-SAT's memory-hungry global presolve.  It is a
separate implementation of the tile predicate, with a supplied block-family
hint and an optional exact replacement radius around that hint.
"""
from __future__ import annotations
import argparse, json, sys, time
from pathlib import Path
from ortools.sat.python import cp_model

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parents[1]))
from verifier import prefix_length,tile_coverage  # noqa:E402
from campaign.theory.family_analysis import placement as family_placement  # noqa:E402

def solve(a):
 m=a.m; model=cp_model.CpModel(); names="IJK"
 x={z:[model.new_bool_var(f"{z}{p}") for p in range(m)] for z in names}
 for z,c in zip(names,a.counts): model.add(sum(x[z])==c)
 model.add(x['I'][0]==1);model.add(x['J'][0]==1)
 def conv(A,B,label):
  out=[]
  for q in range(m):
   ws=[]
   for p in range(q+1):
    w=model.new_bool_var(f"{label}{q}_{p}")
    # Exact conjunction in clauses.
    model.add_bool_or([w.Not(),A[p]])
    model.add_bool_or([w.Not(),B[q-p]])
    model.add_bool_or([A[p].Not(),B[q-p].Not(),w])
    ws.append(w)
   out.append(ws)
  return out
 ij=conv(x['I'],x['J'],'a');ik=conv(x['I'],x['K'],'b');jkw=conv(x['J'],x['K'],'c')
 jk=[]
 for q,ws in enumerate(jkw):
  z=model.new_bool_var(f"s{q}");jk.append(z)
  for w in ws:model.add_bool_or([w.Not(),z])
  model.add_bool_or([z.Not(),*ws])
 for q in range(m):
  alts=ij[q]+ik[q]
  if q:
   z=model.new_bool_var(f"d{q}")
   model.add_bool_or([z.Not(),jk[q-1]]);model.add_bool_or([z.Not(),jk[q]])
   model.add_bool_or([jk[q-1].Not(),jk[q].Not(),z]);alts.append(z)
  model.add_bool_or(alts)
 seed=family_placement(a.h,a.h+1,a.n,a.r)
 if [len(seed[z]) for z in names] != a.counts: raise ValueError('family/count mismatch')
 for z in names:
  S=set(seed[z])
  for p,v in enumerate(x[z]):model.add_hint(v,int(p in S))
 if a.radius is not None:
  diff=[]
  for z in names:
   S=set(seed[z]);diff += [v if p not in S else 1-v for p,v in enumerate(x[z])]
  model.add(sum(diff)<=2*a.radius)
 solver=cp_model.CpSolver();solver.parameters.max_time_in_seconds=a.seconds
 solver.parameters.num_search_workers=a.workers;solver.parameters.random_seed=a.seed
 solver.parameters.cp_model_presolve=False;solver.parameters.symmetry_level=0
 started=time.monotonic();status=solver.solve(model)
 out={'status':solver.status_name(status),'m':m,'counts':a.counts,'radius':a.radius,
      'seconds':time.monotonic()-started,'branches':solver.num_branches,'conflicts':solver.num_conflicts}
 if status in (cp_model.FEASIBLE,cp_model.OPTIMAL):
  P={z:[p for p,v in enumerate(x[z]) if solver.value(v)] for z in names}
  out['placement']=P;out['prefix']=prefix_length(tile_coverage(P['I'],P['J'],P['K']))
 return out

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--m',type=int,required=True);p.add_argument('--counts',type=int,nargs=3,required=True)
 p.add_argument('--h',type=int,required=True);p.add_argument('--n',type=int,required=True);p.add_argument('--r',type=int,required=True)
 p.add_argument('--radius',type=int);p.add_argument('--seconds',type=float,default=60);p.add_argument('--workers',type=int,default=1);p.add_argument('--seed',type=int,default=791);p.add_argument('--output',type=Path)
 a=p.parse_args();o=solve(a);s=json.dumps(o,indent=2)+'\n';print(s,end='');
 if a.output:a.output.write_text(s)
