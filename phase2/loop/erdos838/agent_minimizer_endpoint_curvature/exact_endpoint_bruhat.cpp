// Exact endpoint Pareto scan over B(n,2), for n <= 8.
// A state is one packet-orientation bit for each 3-subset.  Breadth-first
// packet flips enumerate all reflection-order commutation classes.

#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <map>
#include <queue>
#include <tuple>
#include <unordered_set>
#include <utility>
#include <vector>

struct Triple { int ab,ac,bc; };
struct Eval { uint64_t V,C,U; };

struct Model {
  int n,rn;
  std::vector<std::pair<int,int>> roots;
  std::vector<Triple> triples;
  std::vector<std::vector<int>> id;

  explicit Model(int n_):n(n_),rn(n*(n-1)/2),id(n,std::vector<int>(n,-1)) {
    for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){
      id[i][j]=roots.size();roots.push_back({i,j});
    }
    for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)for(int c=b+1;c<n;c++)
      triples.push_back({id[a][b],id[a][c],id[b][c]});
    if(rn>63||triples.size()>63){std::cerr<<"n too large\n";std::exit(2);}
  }

  std::vector<uint64_t> direct(uint64_t state) const {
    std::vector<uint64_t>d(rn,0);
    for(size_t k=0;k<triples.size();k++){
      auto t=triples[k];
      if((state>>k)&1){d[t.bc]|=1ULL<<t.ac;d[t.ac]|=1ULL<<t.ab;}
      else {d[t.ab]|=1ULL<<t.ac;d[t.ac]|=1ULL<<t.bc;}
    }
    return d;
  }
  std::vector<uint64_t> closure(std::vector<uint64_t>s) const {
    for(int k=0;k<rn;k++)for(int i=0;i<rn;i++)if((s[i]>>k)&1)s[i]|=s[k];
    return s;
  }
  std::vector<int> order(const std::vector<uint64_t>&d) const {
    std::vector<int>deg(rn),out;
    for(int i=0;i<rn;i++)for(int j=0;j<rn;j++)if((d[i]>>j)&1)deg[j]++;
    std::priority_queue<int,std::vector<int>,std::greater<int>>q;
    for(int i=0;i<rn;i++)if(!deg[i])q.push(i);
    while(!q.empty()){
      int i=q.top();q.pop();out.push_back(i);uint64_t m=d[i];
      while(m){int j=__builtin_ctzll(m);m&=m-1;if(!--deg[j])q.push(j);}
    }
    if((int)out.size()!=rn){std::cerr<<"cycle\n";std::exit(3);}return out;
  }
  Eval eval(const std::vector<int>&o) const {
    using Row=std::array<uint64_t,8>;
    std::array<Row,8>A{},B{};
    for(int i=0;i<n;i++)A[i][i]=B[i][i]=1;
    auto step=[&](std::array<Row,8>&X,int rid){
      auto [i,j]=roots[rid];for(int c=0;c<n;c++)X[j][c]+=X[i][c];
    };
    for(int x:o)step(A,x);for(auto it=o.rbegin();it!=o.rend();++it)step(B,*it);
    uint64_t V=0,C=0,U=0;
    for(int i=0;i<n;i++)for(int j=0;j<n;j++){
      V+=A[i][j]*B[i][j];U+=A[i][j];C+=B[i][j];
    }
    return {V,C,U};
  }
  uint64_t initial() const {
    std::vector<int>w(n),pos(rn,-1);for(int i=0;i<n;i++)w[i]=i;int at=0;
    for(int top=1;top<n;top++)for(int g=top-1;g>=0;g--){
      int a=w[g],b=w[g+1];if(a>b)std::swap(a,b);pos[id[a][b]]=at++;std::swap(w[g],w[g+1]);
    }
    uint64_t s=0;
    for(size_t k=0;k<triples.size();k++){
      auto t=triples[k];if(pos[t.bc]<pos[t.ac]&&pos[t.ac]<pos[t.ab])s|=1ULL<<k;
      else assert(pos[t.ab]<pos[t.ac]&&pos[t.ac]<pos[t.bc]);
    }
    return s;
  }
};

int main(int argc,char**argv){
  int n=argc>1?std::atoi(argv[1]):8;Model m(n);uint64_t start=m.initial();
  std::unordered_set<uint64_t>seen;seen.reserve(n==8?1500000:40000);
  std::vector<uint64_t>queue;queue.reserve(n==8?1300000:30000);seen.insert(start);queue.push_back(start);
  std::map<uint64_t,std::pair<uint64_t,uint64_t>> byV;
  for(size_t cursor=0;cursor<queue.size();cursor++){
    uint64_t state=queue[cursor];auto d=m.direct(state),succ=m.closure(d);
    std::vector<uint64_t>pred(m.rn,0);
    for(int i=0;i<m.rn;i++)for(int j=0;j<m.rn;j++)if((succ[i]>>j)&1)pred[j]|=1ULL<<i;
    auto e=m.eval(m.order(d));uint64_t endpoint=std::min(e.C,e.U);
    auto it=byV.find(e.V);
    if(it==byV.end())byV[e.V]={endpoint,1};
    else if(endpoint<it->second.first)it->second={endpoint,1};
    else if(endpoint==it->second.first)it->second.second++;
    for(size_t k=0;k<m.triples.size();k++){
      auto t=m.triples[k];int first=((state>>k)&1)?t.bc:t.ab,last=((state>>k)&1)?t.ab:t.bc;
      uint64_t interval=(succ[first]&pred[last])|(1ULL<<first)|(1ULL<<last);
      uint64_t packet=(1ULL<<t.ab)|(1ULL<<t.ac)|(1ULL<<t.bc);
      if(interval==packet){uint64_t other=state^(1ULL<<k);if(seen.insert(other).second)queue.push_back(other);}
    }
  }
  std::cout<<"{\"n\":"<<n<<",\"classes\":"<<queue.size()<<",\"profiles\":[";bool first=true;
  for(auto [V,row]:byV){if(!first)std::cout<<",";first=false;std::cout<<"["<<V<<","<<row.first<<","<<row.second<<"]";}
  std::cout<<"]}\n";
}
