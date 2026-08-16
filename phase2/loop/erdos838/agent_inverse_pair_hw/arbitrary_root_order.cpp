// Search the broad class obtained by multiplying every type-A positive-root
// transvection exactly once, in an arbitrary order.  No reflection-order
// betweenness constraints are imposed.

#include <algorithm>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <random>
#include <string>
#include <utility>
#include <vector>

using Root = std::pair<int,int>;

struct Score { long double fhalf, fone, h; };

long double q_at(int n, const std::vector<Root>& roots, long double z) {
  std::vector<long double> b(n*n,0), a(n*n,0);
  for (int i=0;i<n;++i) b[i*n+i]=a[i*n+i]=1;
  for (auto [i,j]: roots)
    for (int c=0;c<n;++c) b[j*n+c]+=z*b[i*n+c];
  for (auto it=roots.rbegin();it!=roots.rend();++it) {
    auto [i,j]=*it;
    for (int c=0;c<n;++c) a[j*n+c]+=z*a[i*n+c];
  }
  long double q=0;
  for (int k=0;k<n*n;++k) q+=a[k]*b[k];
  return q;
}

Score score(int n, const std::vector<Root>& roots) {
  long double qh=q_at(n,roots,0.5L), q1=q_at(n,roots,1.0L);
  Score s{1-n/2.0L+qh,1+q1,0};
  s.h=n*s.fhalf/s.fone;
  return s;
}

void print(int n, const std::vector<Root>& roots, Score s,
           uint64_t visited, const std::string& mode) {
  std::cout<<"{\n  \"n\": "<<n<<",\n  \"mode\": \""<<mode
           <<"\",\n  \"visited\": "<<visited<<",\n  \"H\": "
           <<std::setprecision(20)<<(double)s.h<<",\n  \"F_half\": "
           <<(double)s.fhalf<<",\n  \"F_one\": "<<(double)s.fone
           <<",\n  \"roots\": [";
  for(size_t k=0;k<roots.size();++k){
    if(k)std::cout<<",";
    std::cout<<"["<<roots[k].first<<","<<roots[k].second<<"]";
  }
  std::cout<<"]\n}\n";
}

int main(int argc,char**argv){
  if(argc<3){
    std::cerr<<"usage: arbitrary_root_order n exhaustive | anneal steps restarts seed [stdin]\n";
    return 2;
  }
  int n=std::stoi(argv[1]);
  std::vector<Root> base;
  for(int i=0;i<n;++i)for(int j=i+1;j<n;++j)base.push_back({i,j});
  std::string mode=argv[2];
  Score best{-1,-1,-1}; std::vector<Root> bestroots; uint64_t visited=0;
  if(mode=="exhaustive"){
    do{
      Score s=score(n,base);++visited;
      if(s.h>best.h){best=s;bestroots=base;}
    }while(std::next_permutation(base.begin(),base.end()));
  }else if(mode=="anneal"){
    if(argc<6)return 2;
    long long steps=std::stoll(argv[3]);
    int restarts=std::stoi(argv[4]);
    uint64_t seed=std::stoull(argv[5]);
    if(argc>=7 && std::string(argv[6])=="stdin"){
      for(auto& [i,j]:base) if(!(std::cin>>i>>j)){
        std::cerr<<"not enough root pairs on stdin\n"; return 2;
      }
    }
    std::mt19937_64 rng(seed);
    std::uniform_real_distribution<long double> unif(0,1);
    for(int restart=0;restart<restarts;++restart){
      auto roots=base;
      if(restart)std::shuffle(roots.begin(),roots.end(),rng);
      Score cur=score(n,roots);++visited;
      if(cur.h>best.h){best=cur;bestroots=roots;}
      for(long long step=0;step<steps;++step){
        int x=rng()%roots.size(), y=rng()%roots.size();
        if(x==y)continue;
        std::swap(roots[x],roots[y]);
        Score cand=score(n,roots);++visited;
        long double phase=(step%std::max<long long>(1000,steps/10))/
                          (long double)std::max<long long>(999,steps/10-1);
        long double temp=.04L*(1-phase)+.00002L;
        if(cand.h>=cur.h || unif(rng)<std::exp((cand.h-cur.h)/temp))cur=cand;
        else std::swap(roots[x],roots[y]);
        if(cur.h>best.h){
          best=cur;bestroots=roots;
          std::cerr<<"best n="<<n<<" restart="<<restart<<" step="<<step
                   <<" H="<<std::setprecision(15)<<(double)best.h<<"\n";
        }
      }
    }
  }else return 2;
  print(n,bestroots,best,visited,mode);
}
