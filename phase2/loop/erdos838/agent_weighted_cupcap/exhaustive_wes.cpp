// Exhaustive audit of the weighted endpoint-span inequality on B(n,2).
//
// For each commutation class of reflection orders in type A, form the
// increasing- and decreasing-order monotone-path partition functions at
// activity z=1/2.  For every root (i,j), report the minimum of
//
//   mu(U_ij)+mu(C_ij)-log_2(j-i+1).
//
// A path with e edges has weight z^e.  Thus the sum of the two activities is
// exactly the expected size of the convex polygon obtained from independent
// upper/lower chains with the common endpoints (the endpoints cancel the two
// extra vertices).

#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <limits>
#include <queue>
#include <sstream>
#include <string>
#include <unordered_set>
#include <utility>
#include <vector>

struct Triple { int ab, ac, bc; };
struct Dual { long double v=0, d=0; };

struct Model {
  int n, roots_n;
  std::vector<std::pair<int,int>> roots;
  std::vector<Triple> triples;
  std::vector<std::vector<int>> root_id;

  explicit Model(int n_) : n(n_), roots_n(n*(n-1)/2),
      root_id(n,std::vector<int>(n,-1)) {
    for(int i=0;i<n;i++) for(int j=i+1;j<n;j++) {
      root_id[i][j]=(int)roots.size(); roots.push_back({i,j});
    }
    for(int a=0;a<n;a++) for(int b=a+1;b<n;b++) for(int c=b+1;c<n;c++)
      triples.push_back({root_id[a][b],root_id[a][c],root_id[b][c]});
    if(roots_n>63 || triples.size()>63) std::exit(2);
  }

  std::vector<uint64_t> direct(uint64_t state) const {
    std::vector<uint64_t>d(roots_n,0);
    for(size_t k=0;k<triples.size();k++) {
      const auto&t=triples[k];
      if((state>>k)&1ULL) { d[t.bc]|=1ULL<<t.ac; d[t.ac]|=1ULL<<t.ab; }
      else { d[t.ab]|=1ULL<<t.ac; d[t.ac]|=1ULL<<t.bc; }
    }
    return d;
  }
  std::vector<uint64_t> closure(const std::vector<uint64_t>&d) const {
    auto s=d;
    for(int k=0;k<roots_n;k++) for(int i=0;i<roots_n;i++)
      if((s[i]>>k)&1ULL) s[i]|=s[k];
    return s;
  }
  std::vector<int> order(const std::vector<uint64_t>&d) const {
    std::vector<int>deg(roots_n),out;
    for(int i=0;i<roots_n;i++) for(int j=0;j<roots_n;j++) if((d[i]>>j)&1ULL)deg[j]++;
    std::priority_queue<int,std::vector<int>,std::greater<int>>q;
    for(int i=0;i<roots_n;i++)if(!deg[i])q.push(i);
    while(!q.empty()) { int i=q.top();q.pop();out.push_back(i); uint64_t m=d[i];
      while(m){int j=__builtin_ctzll(m);m&=m-1;if(!--deg[j])q.push(j);} }
    assert((int)out.size()==roots_n); return out;
  }
  uint64_t initial() const {
    std::vector<int>w(n),pos(roots_n,-1);for(int i=0;i<n;i++)w[i]=i;int at=0;
    for(int top=1;top<n;top++)for(int g=top-1;g>=0;g--){int a=w[g],b=w[g+1];
      if(a>b)std::swap(a,b);pos[root_id[a][b]]=at++;std::swap(w[g],w[g+1]);}
    uint64_t state=0;
    for(size_t k=0;k<triples.size();k++){auto t=triples[k];
      if(pos[t.bc]<pos[t.ac]&&pos[t.ac]<pos[t.ab])state|=1ULL<<k;}
    return state;
  }

  struct Scores {
    long double wes, localized, localized2, mass_localized, mass2, mass3, left2, either2;
    int wes_root, localized_root, localized2_root, mass_root, mass2_root, mass3_root, left2_root, either2_root;
  };
  Scores eval(const std::vector<int>&ord) const {
    std::array<std::array<Dual,8>,8> A{},B{};
    std::array<std::array<uint64_t,8>,8> A1{},B1{};
    for(int i=0;i<n;i++) A[i][i].v=B[i][i].v=1;
    for(int i=0;i<n;i++) A1[i][i]=B1[i][i]=1;
    const long double z=.5L;
    auto step=[&](auto&X,int rid){auto [i,j]=roots[rid]; auto old=X[j];
      for(int c=0;c<n;c++){
        X[j][c].v=old[c].v+z*X[i][c].v;
        X[j][c].d=old[c].d+X[i][c].v+z*X[i][c].d;
      }};
    auto step1=[&](auto&X,int rid){auto [i,j]=roots[rid];
      for(int c=0;c<n;c++)X[j][c]+=X[i][c];};
    for(int rid:ord){step(A,rid);step1(A1,rid);}
    for(auto it=ord.rbegin();it!=ord.rend();++it){step(B,*it);step1(B1,*it);}
    long double best=std::numeric_limits<long double>::infinity();int best_root=-1;
    long double best_local=std::numeric_limits<long double>::infinity();int best_local_root=-1;
    long double best_local2=best_local;int best_local2_root=-1;
    long double best_mass=std::numeric_limits<long double>::infinity();int best_mass_root=-1;
    long double best_mass2=best_mass,best_mass3=best_mass,best_left2=best_mass,best_either2=best_mass;
    int best_mass2_root=-1,best_mass3_root=-1,best_left2_root=-1,best_either2_root=-1;
    for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){
      assert(A[j][i].v>0&&B[j][i].v>0);
      long double mu=z*A[j][i].d/A[j][i].v+z*B[j][i].d/B[j][i].v;
      long double deficit=mu-std::log2((long double)(j-i+1));
      if(deficit<best){best=deficit;best_root=root_id[i][j];}
      uint64_t zi=1+(j-i+1);
      for(int a=i;a<=j;a++)for(int b=a+1;b<=j;b++)zi+=A1[b][a]*B1[b][a];
      uint64_t endpoint=A1[j][i]*B1[j][i];
      long double localized=deficit+std::log2((long double)zi/endpoint);
      if(localized<best_local){best_local=localized;best_local_root=root_id[i][j];}
      long double localized2=localized-std::log2((long double)(j-i+1));
      if(localized2<best_local2){best_local2=localized2;best_local2_root=root_id[i][j];}
      long double fhalf=A[j][i].v*B[j][i].v;
      long double mass_localized=std::log2((long double)zi/fhalf)-std::log2((long double)(j-i+1));
      if(mass_localized<best_mass){best_mass=mass_localized;best_mass_root=root_id[i][j];}
      long double mass2=mass_localized-std::log2((long double)(j-i+1));
      long double mass3=mass2-std::log2((long double)(j-i+1));
      if(mass2<best_mass2){best_mass2=mass2;best_mass2_root=root_id[i][j];}
      if(mass3<best_mass3){best_mass3=mass3;best_mass3_root=root_id[i][j];}
      // Rooted compensation: all convex faces in I whose exact left endpoint
      // is i (and, symmetrically, faces retaining at least one marker).
      uint64_t left=1; // singleton {i}
      uint64_t right=1; // singleton {j}
      for(int b=i+1;b<=j;b++)left+=A1[b][i]*B1[b][i];
      for(int a=i;a<j;a++)right+=A1[j][a]*B1[j][a];
      uint64_t either=left+right-endpoint; // endpoint family counted twice
      long double left2=std::log2((long double)std::max(left,right)/fhalf)-2*std::log2((long double)(j-i+1));
      long double either2=std::log2((long double)either/fhalf)-2*std::log2((long double)(j-i+1));
      if(left2<best_left2){best_left2=left2;best_left2_root=root_id[i][j];}
      if(either2<best_either2){best_either2=either2;best_either2_root=root_id[i][j];}
    }
    return {best,best_local,best_local2,best_mass,best_mass2,best_mass3,best_left2,best_either2,
      best_root,best_local_root,best_local2_root,best_mass_root,best_mass2_root,best_mass3_root,best_left2_root,best_either2_root};
  }
};

int main(int argc,char**argv){
  int n=argc>1?std::atoi(argv[1]):7; Model M(n);uint64_t start=M.initial();
  std::unordered_set<uint64_t>seen;seen.reserve(n==8?1600000:40000);
  std::vector<uint64_t>queue;queue.reserve(n==8?1300000:30000);
  seen.insert(start);queue.push_back(start);
  long double best=std::numeric_limits<long double>::infinity(),best_local=best,best_local2=best,best_mass=best,
    best_mass2=best,best_mass3=best,best_left2=best,best_either2=best;
  uint64_t best_state=0,best_local_state=0,best_local2_state=0,best_mass_state=0,best_mass2_state=0,best_mass3_state=0,
    best_left2_state=0,best_either2_state=0;
  int best_root=-1,best_local_root=-1,best_local2_root=-1,best_mass_root=-1,best_mass2_root=-1,best_mass3_root=-1,
    best_left2_root=-1,best_either2_root=-1;
  for(size_t cur=0;cur<queue.size();cur++){
    uint64_t s=queue[cur];auto d=M.direct(s),succ=M.closure(d);
    std::vector<uint64_t>pred(M.roots_n);for(int i=0;i<M.roots_n;i++)for(int j=0;j<M.roots_n;j++)
      if((succ[i]>>j)&1ULL)pred[j]|=1ULL<<i;
    auto scores=M.eval(M.order(d));if(scores.wes<best){best=scores.wes;best_state=s;best_root=scores.wes_root;}
    if(scores.localized<best_local){best_local=scores.localized;best_local_state=s;best_local_root=scores.localized_root;}
    if(scores.localized2<best_local2){best_local2=scores.localized2;best_local2_state=s;best_local2_root=scores.localized2_root;}
    if(scores.mass_localized<best_mass){best_mass=scores.mass_localized;best_mass_state=s;best_mass_root=scores.mass_root;}
    if(scores.mass2<best_mass2){best_mass2=scores.mass2;best_mass2_state=s;best_mass2_root=scores.mass2_root;}
    if(scores.mass3<best_mass3){best_mass3=scores.mass3;best_mass3_state=s;best_mass3_root=scores.mass3_root;}
    if(scores.left2<best_left2){best_left2=scores.left2;best_left2_state=s;best_left2_root=scores.left2_root;}
    if(scores.either2<best_either2){best_either2=scores.either2;best_either2_state=s;best_either2_root=scores.either2_root;}
    for(size_t k=0;k<M.triples.size();k++){auto t=M.triples[k];
      int first=((s>>k)&1ULL)?t.bc:t.ab,last=((s>>k)&1ULL)?t.ab:t.bc;
      uint64_t interval=(succ[first]&pred[last])|(1ULL<<first)|(1ULL<<last);
      uint64_t packet=(1ULL<<t.ab)|(1ULL<<t.ac)|(1ULL<<t.bc);
      if(interval==packet){uint64_t other=s^(1ULL<<k);if(seen.insert(other).second)queue.push_back(other);}
    }
  }
  auto [i,j]=M.roots[best_root];
  auto [li,lj]=M.roots[best_local_root];
  auto [l2wi,l2wj]=M.roots[best_local2_root];
  auto [mi,mj]=M.roots[best_mass_root];
  auto [m2i,m2j]=M.roots[best_mass2_root];
  auto [m3i,m3j]=M.roots[best_mass3_root];
  auto [l2i,l2j]=M.roots[best_left2_root];
  auto [e2i,e2j]=M.roots[best_either2_root];
  std::cout<<std::setprecision(18)<<"{\n  \"n\": "<<n<<",\n  \"classes\": "<<queue.size()
    <<",\n  \"minimum_mu_minus_log_span\": "<<(double)best
    <<",\n  \"endpoint\": ["<<i<<","<<j<<"],\n  \"span\": "<<(j-i+1)
    <<",\n  \"state_hex\": \""<<std::hex<<best_state<<std::dec<<"\""
    <<",\n  \"minimum_localized_score\": "<<(double)best_local
    <<",\n  \"localized_endpoint\": ["<<li<<","<<lj<<"]"
    <<",\n  \"localized_state_hex\": \""<<std::hex<<best_local_state<<std::dec<<"\""
    <<",\n  \"minimum_two_log_localized_score\": "<<(double)best_local2
    <<",\n  \"two_log_localized_endpoint\": ["<<l2wi<<","<<l2wj<<"]"
    <<",\n  \"two_log_localized_state_hex\": \""<<std::hex<<best_local2_state<<std::dec<<"\""
    <<",\n  \"minimum_mass_localized_score\": "<<(double)best_mass
    <<",\n  \"mass_localized_endpoint\": ["<<mi<<","<<mj<<"]"
    <<",\n  \"mass_localized_state_hex\": \""<<std::hex<<best_mass_state<<std::dec<<"\""
    <<",\n  \"minimum_span2_interval_score\": "<<(double)best_mass2
    <<",\n  \"span2_interval_endpoint\": ["<<m2i<<","<<m2j<<"]"
    <<",\n  \"span2_interval_state_hex\": \""<<std::hex<<best_mass2_state<<std::dec<<"\""
    <<",\n  \"minimum_span3_interval_score\": "<<(double)best_mass3
    <<",\n  \"span3_interval_endpoint\": ["<<m3i<<","<<m3j<<"]"
    <<",\n  \"span3_interval_state_hex\": \""<<std::hex<<best_mass3_state<<std::dec<<"\""
    <<",\n  \"minimum_span2_one_root_score\": "<<(double)best_left2
    <<",\n  \"span2_one_root_endpoint\": ["<<l2i<<","<<l2j<<"]"
    <<",\n  \"span2_one_root_state_hex\": \""<<std::hex<<best_left2_state<<std::dec<<"\""
    <<",\n  \"minimum_span2_either_marker_score\": "<<(double)best_either2
    <<",\n  \"span2_either_marker_endpoint\": ["<<e2i<<","<<e2j<<"]"
    <<",\n  \"span2_either_marker_state_hex\": \""<<std::hex<<best_either2_state<<std::dec<<"\"\n}\n";
}
