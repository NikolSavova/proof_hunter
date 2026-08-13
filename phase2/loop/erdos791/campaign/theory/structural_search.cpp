// Coordinated block search for the generalized-Mrose tile placement problem.
//
// Unlike coordinate-wise local search, one proposal moves/resizes a whole AP or
// interval block.  This preserves the geometry of Kohonen's ten coverage seams
// often enough to explore genuinely different block layouts.

#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <random>
#include <set>
#include <string>
#include <vector>

using V = std::vector<int>;

struct P {
  // I={0,x} U AP(is,id,ic); J=AP(js,jd,jc);
  // K=[0,k0-1] U [k1,k1+c1-1] U [k2,k2+c2-1].
  int x=5,is=112,id=5,ic=6,js=10,jd=6,jc=17,k0=5,k1=224,c1=6,k2=367,c2=6;
};

static V ap(int s,int d,int c) { V z; for(int i=0;i<c;i++) z.push_back(s+d*i); return z; }
static V interval(int s,int c) { return ap(s,1,c); }
static bool unique_nonnegative(const V& z) {
  if (std::any_of(z.begin(),z.end(),[](int x){return x<0;})) return false;
  return std::set<int>(z.begin(),z.end()).size()==z.size();
}
static std::array<V,3> expand(const P& p) {
  V I{0,p.x}; auto hi=ap(p.is,p.id,p.ic); I.insert(I.end(),hi.begin(),hi.end());
  V J=ap(p.js,p.jd,p.jc);
  V K=interval(0,p.k0), a=interval(p.k1,p.c1), b=interval(p.k2,p.c2);
  K.insert(K.end(),a.begin(),a.end()); K.insert(K.end(),b.begin(),b.end());
  for(auto* z:{&I,&J,&K}) {std::sort(z->begin(),z->end()); z->erase(std::unique(z->begin(),z->end()),z->end());}
  return {I,J,K};
}
struct Eval { int prefix=0,count=0,weighted=0; long long score=0; };
static Eval eval(const P& p,int target=511,int horizon=560) {
  auto z=expand(p); if(!unique_nonnegative(z[0])||!unique_nonnegative(z[1])||!unique_nonnegative(z[2])) return {};
  if((int)(z[0].size()+z[1].size()+z[2].size())!=42) return {};
  std::vector<uint8_t> ij(horizon+1),ik(horizon+1),jk(horizon+1),cov(horizon+1);
  auto sums=[&](const V&a,const V&b,std::vector<uint8_t>&out){for(int x:a)for(int y:b)if(x+y<=horizon)out[x+y]=1;};
  sums(z[0],z[1],ij); sums(z[0],z[2],ik); sums(z[1],z[2],jk);
  Eval e;
  for(int q=0;q<=horizon;q++) {
    cov[q]=ij[q]||ik[q]||(q>0&&jk[q-1]&&jk[q]);
    if(q<target&&cov[q]) {e.count++; e.weighted += target-q;}
  }
  while(e.prefix<=horizon&&cov[e.prefix])e.prefix++;
  e.score=1000000000LL*e.count + 100000LL*e.weighted + e.prefix;
  return e;
}
static void print(const P&p,const Eval&e,int seed,long long iter) {
  auto z=expand(p);
  std::cout<<"FOUND_OR_BEST seed="<<seed<<" iter="<<iter<<" prefix="<<e.prefix<<" count="<<e.count<<"\n";
  const char* names="IJK";
  for(int k=0;k<3;k++){std::cout<<names[k]<<"=";for(int x:z[k])std::cout<<x<<",";std::cout<<"\n";}
  std::cout<<"params "<<p.x<<" "<<p.is<<" "<<p.id<<" "<<p.ic<<" "<<p.js<<" "<<p.jd<<" "<<p.jc<<" "<<p.k0<<" "<<p.k1<<" "<<p.c1<<" "<<p.k2<<" "<<p.c2<<"\n";
}

int main(int argc,char**argv){
  long long steps=argc>1?std::stoll(argv[1]):20000000;
  int runs=argc>2?std::stoi(argv[2]):32;
  int baseseed=argc>3?std::stoi(argv[3]):791;
  P global; Eval ge=eval(global); print(global,ge,baseseed,0);
  for(int run=0;run<runs;run++){
    int seed=baseseed+1000003*run; std::mt19937_64 rng(seed); P cur; Eval ce=eval(cur);
    // Every fourth run begins with a coherent random displacement, while the
    // others exploit the known placement before slowly heating away from it.
    if(run%4==3){cur.is+=int(rng()%31)-15;cur.js+=int(rng()%15)-7;cur.k1+=int(rng()%41)-20;cur.k2+=int(rng()%41)-20;ce=eval(cur);}
    long long each=(steps+runs-1)/runs;
    for(long long it=1;it<=each;it++){
      P q=cur; int which=rng()%12; int d=(rng()%2?1:-1)*(rng()%10<8?1:2+int(rng()%10));
      int* vars[]={&q.x,&q.is,&q.id,&q.ic,&q.js,&q.jd,&q.jc,&q.k0,&q.k1,&q.c1,&q.k2,&q.c2};
      *vars[which]+=d;
      // Maintain 42 elements under count changes by compensating within the
      // same structural side (I/J/K); reject if any block becomes empty.
      if(which==3) q.jc-=d; else if(which==6) q.c2-=d; else if(which==7)q.c2-=d; else if(which==9)q.c2-=d;
      if(q.x<1||q.id<1||q.jd<1||q.ic<1||q.jc<1||q.k0<1||q.c1<1||q.c2<1)continue;
      Eval qe=eval(q); double frac=double((it-1)%200000)/199999.0;
      double temp=3e8*std::pow(2e5/3e8,frac); long long delta=qe.score-ce.score;
      if(delta>=0||std::uniform_real_distribution<double>(0,1)(rng)<std::exp(double(delta)/temp)){cur=q;ce=qe;}
      if(qe.score>ge.score){global=q;ge=qe;print(global,ge,seed,it);}
      if(qe.prefix>=511){print(q,qe,seed,it);return 0;}
    }
  }
  std::cout<<"NO_TARGET_FOUND\n"; print(global,ge,baseseed,steps); return 1;
}
