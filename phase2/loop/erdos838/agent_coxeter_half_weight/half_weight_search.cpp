// Heuristic search for large half-weight ratios in type-A reflection orders.
//
// A state is an ordinary reduced word for w_0.  Adjacent commutations and
// long braids preserve reducedness.  We evaluate both the literal matrix
// trace Q(z)=<A(z),B(z)> and the convex-set normalization
// F(z)=1+nz+Q(z)-n at z=1/2,1.

#include <algorithm>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <random>
#include <string>
#include <tuple>
#include <vector>

using Word = std::vector<int>;

struct Score {
  long double q1 = 0, qh = 0, f1 = 0, fh = 0;
  long double m1 = 0, mh = 0, apa = 0;
  long double hq = 0, hf = 0, acp = 0;
};

Word bubble_word(int n) {
  Word w;
  for (int top = 1; top < n; ++top)
    for (int i = top - 1; i >= 0; --i) w.push_back(i);
  return w;
}

Word random_word(int n, std::mt19937_64& rng) {
  std::vector<int> p(n);
  std::iota(p.begin(), p.end(), 0);
  Word w;
  w.reserve(n * (n - 1) / 2);
  while ((int)w.size() < n * (n - 1) / 2) {
    std::vector<int> asc;
    for (int i = 0; i + 1 < n; ++i)
      if (p[i] < p[i + 1]) asc.push_back(i);
    int i = asc[rng() % asc.size()];
    w.push_back(i);
    std::swap(p[i], p[i + 1]);
  }
  return w;
}

Word word_from_coordinates(int n, const std::vector<long long>& y) {
  struct Slope { long long dy; int dx, i, j; };
  std::vector<Slope> slopes;
  for (int i=0;i<n;++i) for(int j=i+1;j<n;++j)
    slopes.push_back({y[j]-y[i],j-i,i,j});
  std::sort(slopes.begin(),slopes.end(),[](const Slope& a,const Slope& b){
    __int128 l=(__int128)a.dy*b.dx, r=(__int128)b.dy*a.dx;
    if(l!=r) return l<r;
    return std::tie(a.i,a.j)<std::tie(b.i,b.j);
  });
  std::vector<int> wires(n); std::iota(wires.begin(),wires.end(),0);
  Word w; w.reserve(slopes.size());
  for(auto s:slopes){
    int p=-1,q=-1;
    for(int k=0;k<n;++k){if(wires[k]==s.i)p=k;if(wires[k]==s.j)q=k;}
    if(std::abs(p-q)!=1){std::cerr<<"coordinate slopes not an allowable sequence\n";std::abort();}
    int k=std::min(p,q);
    if(wires[k]>wires[k+1]){std::cerr<<"coordinate order crosses backward\n";std::abort();}
    w.push_back(k); std::swap(wires[k],wires[k+1]);
  }
  return w;
}

std::vector<std::pair<int,int>> roots_from_word(int n, const Word& w) {
  std::vector<int> p(n);
  std::iota(p.begin(), p.end(), 0);
  std::vector<std::pair<int,int>> roots;
  roots.reserve(w.size());
  for (int s : w) {
    int a = p[s], b = p[s + 1];
    if (a > b) std::abort();
    roots.push_back({a,b});
    std::swap(p[s],p[s+1]);
  }
  return roots;
}

std::pair<long double,long double>
trace_at(int n, const std::vector<std::pair<int,int>>& roots,
         long double z) {
  std::vector<long double> b(n*n,0), a(n*n,0);
  std::vector<long double> db(n*n,0), da(n*n,0);
  for (int i=0;i<n;++i) b[i*n+i]=a[i*n+i]=1;
  for (auto [i,j] : roots) {
    for (int c=0;c<n;++c) {
      db[j*n+c] += z*(db[i*n+c]+b[i*n+c]);
      b[j*n+c] += z*b[i*n+c];
    }
  }
  for (auto it=roots.rbegin(); it!=roots.rend(); ++it) {
    auto [i,j]=*it;
    for (int c=0;c<n;++c) {
      da[j*n+c] += z*(da[i*n+c]+a[i*n+c]);
      a[j*n+c] += z*a[i*n+c];
    }
  }
  long double q=0,m=0;
  for (int k=0;k<n*n;++k) {
    q += a[k]*b[k];
    m += da[k]*b[k]+a[k]*db[k];
  }
  return {q,m};
}

Score evaluate(int n, const Word& w) {
  auto roots=roots_from_word(n,w);
  Score s;
  long double dq1,dqh;
  std::tie(s.q1,dq1)=trace_at(n,roots,1);
  std::tie(s.qh,dqh)=trace_at(n,roots,0.5L);
  s.f1=s.q1+1;
  s.fh=s.qh+1-n/2.0L;
  s.m1=n+dq1;
  s.mh=n/2.0L+dqh;
  s.apa=(n*s.fh+(n-1)*s.mh)/(2*s.m1);
  s.hq=n*s.qh/s.q1;
  s.hf=n*s.fh/s.f1;
  long double delta=s.m1/s.f1-s.mh/s.fh;
  s.acp=s.hf*std::max(0.0L,1-delta);
  return s;
}

int main(int argc,char**argv) {
  if (argc<6) {
    std::cerr << "usage: half_weight_search n steps restarts seed q|f|a|c [output] [coords]\n"
                 "If coords is present, read n integer y-coordinates from stdin; "
                 "if word is present, read n(n-1)/2 generators.\n";
    return 2;
  }
  int n=std::stoi(argv[1]);
  long long steps=std::stoll(argv[2]);
  int restarts=std::stoi(argv[3]);
  uint64_t seed=std::stoull(argv[4]);
  std::string objective=argv[5];
  bool use_q=objective=="q", use_apa=objective=="a", use_acp=objective=="c";
  Word supplied;
  if(argc>=8 && std::string(argv[7])=="coords"){
    std::vector<long long> y(n);
    for(auto& v:y) if(!(std::cin>>v)){std::cerr<<"not enough coordinates\n";return 2;}
    supplied=word_from_coordinates(n,y);
  } else if(argc>=8 && std::string(argv[7])=="word") {
    supplied.resize(n*(n-1)/2);
    for(auto& v:supplied) if(!(std::cin>>v)){std::cerr<<"not enough generators\n";return 2;}
  }
  std::mt19937_64 rng(seed);
  std::uniform_real_distribution<long double> unif(0,1);
  Word global_word;
  Score global_score;
  long double global=-1;
  long long evaluated=0, accepted=0, commuted=0;
  for (int restart=0;restart<restarts;++restart) {
    Word w = restart==0 ? (supplied.empty()?bubble_word(n):supplied) : random_word(n,rng);
    Score cur=evaluate(n,w);
    long double cv=use_acp?cur.acp:(use_apa?cur.apa:(use_q?cur.hq:cur.hf));
    if(cv>global){global=cv;global_word=w;global_score=cur;}
    for(long long step=0;step<steps;++step){
      std::vector<int> cs,bs;
      for(int i=0;i+1<(int)w.size();++i)
        if(std::abs(w[i]-w[i+1])>1) cs.push_back(i);
      for(int i=0;i+2<(int)w.size();++i)
        if(w[i]==w[i+2] && std::abs(w[i]-w[i+1])==1) bs.push_back(i);
      // Spend about half the transitions on free commutations, which expose
      // different long braids without an objective evaluation.
      if(!cs.empty() && (bs.empty() || (rng()&1))){
        int k=cs[rng()%cs.size()]; std::swap(w[k],w[k+1]); ++commuted; continue;
      }
      if(bs.empty()) continue;
      int k=bs[rng()%bs.size()];
      int x=w[k],y=w[k+1]; w[k]=y;w[k+1]=x;w[k+2]=y;
      Score cand=evaluate(n,w); ++evaluated;
      long double nv=use_acp?cand.acp:(use_apa?cand.apa:(use_q?cand.hq:cand.hf));
      long double phase=(step%std::max<long long>(1000,steps/8)) /
                        (long double)std::max<long long>(999,steps/8-1);
      long double temp=(use_acp?.001L:.04L)*(1-phase)
                       +(use_acp?.00000001L:.00005L);
      bool take=nv>=cv || unif(rng)<std::exp((nv-cv)/temp);
      if(take){cur=cand;cv=nv;++accepted;}
      else { w[k]=x;w[k+1]=y;w[k+2]=x; }
      if(cv>global){
        global=cv;global_word=w;global_score=cur;
        std::cerr<<"best n="<<n<<" r="<<restart<<" step="<<step
                 <<" Hq="<<std::setprecision(12)<<(double)cur.hq
                 <<" Hf="<<(double)cur.hf<<" APA="<<(double)cur.apa
                 <<" ACP="<<(double)cur.acp
                 <<" q1="<<(double)cur.q1<<"\n";
      }
    }
  }
  std::ostream* out=&std::cout;
  std::ofstream file;
  if(argc>=7){file.open(argv[6]);out=&file;}
  *out<<"{\n  \"n\": "<<n<<",\n  \"steps_per_restart\": "<<steps
      <<",\n  \"restarts\": "<<restarts<<",\n  \"seed\": "<<seed
      <<",\n  \"objective\": \""<<(use_acp?"activity_compensated_peak":(use_apa?"apa":(use_q?"matrix_trace":"convex_partition")))<<"\",\n"
      <<"  \"H_trace\": "<<std::setprecision(18)<<(double)global_score.hq<<",\n"
      <<"  \"H_full\": "<<(double)global_score.hf<<",\n"
      <<"  \"APA_ratio\": "<<(double)global_score.apa<<",\n"
      <<"  \"ACP_value\": "<<(double)global_score.acp<<",\n"
      <<"  \"Q_1\": "<<(double)global_score.q1<<",\n"
      <<"  \"Q_half\": "<<(double)global_score.qh<<",\n"
      <<"  \"evaluated_braids\": "<<evaluated<<",\n"
      <<"  \"accepted_braids\": "<<accepted<<",\n"
      <<"  \"commutations\": "<<commuted<<",\n"
      <<"  \"word_zero_based\": [";
  for(size_t i=0;i<global_word.size();++i){if(i)*out<<",";*out<<global_word[i];}
  *out<<"]\n}\n";
}
