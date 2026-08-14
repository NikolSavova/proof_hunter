// Exhaustive commutation-class enumeration for reflection orders of type A.
//
// A commutation class is encoded by one orientation bit for every 3-subset
// {a<b<c}.  Its three roots occur either
//
//     ab < ac < bc              or              bc < ac < ab.
//
// These precedence constraints define the Coxeter heap on the positive roots.
// A packet can be flipped iff its three roots form a convex interval.  Thus a
// breadth-first walk from the bubble class enumerates the higher Bruhat order
// B(n,2), equivalently every commutation class of reduced words for w_0.
//
// The program evaluates the reverse-product trace V and first moment M using
// exact unsigned 64-bit arithmetic.  (The --selftest range n<=8 is far below
// overflow.)  A lexicographically least topological order supplies a canonical
// root sequence; disjoint roots commute, so V and M are class invariants.

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

struct Triple {
  int ab, ac, bc;
};

struct Eval {
  uint64_t V, M;
};

struct Model {
  int n, roots_n;
  std::vector<std::pair<int,int>> roots;
  std::vector<Triple> triples;
  std::vector<std::vector<int>> root_id;

  explicit Model(int n_) : n(n_), roots_n(n*(n-1)/2), root_id(n, std::vector<int>(n,-1)) {
    for (int i=0;i<n;i++) for (int j=i+1;j<n;j++) {
      root_id[i][j] = (int)roots.size();
      roots.push_back({i,j});
    }
    for (int a=0;a<n;a++) for (int b=a+1;b<n;b++) for (int c=b+1;c<n;c++)
      triples.push_back({root_id[a][b],root_id[a][c],root_id[b][c]});
    if (roots_n > 63 || triples.size() > 63) {
      std::cerr << "This compact implementation supports n<=8.\n";
      std::exit(2);
    }
  }

  // Direct successor masks for a state.
  std::vector<uint64_t> direct(uint64_t state) const {
    std::vector<uint64_t> d(roots_n,0);
    for (size_t k=0;k<triples.size();k++) {
      const auto &t=triples[k];
      if ((state>>k)&1ULL) {
        d[t.bc] |= 1ULL<<t.ac;
        d[t.ac] |= 1ULL<<t.ab;
      } else {
        d[t.ab] |= 1ULL<<t.ac;
        d[t.ac] |= 1ULL<<t.bc;
      }
    }
    return d;
  }

  // Transitive successor closure.  Valid higher-Bruhat states are acyclic.
  std::vector<uint64_t> closure(const std::vector<uint64_t>& d) const {
    std::vector<uint64_t> s=d;
    for (int k=0;k<roots_n;k++)
      for (int i=0;i<roots_n;i++) if ((s[i]>>k)&1ULL) s[i] |= s[k];
    return s;
  }

  std::vector<int> canonical_order(const std::vector<uint64_t>& d) const {
    std::vector<int> indeg(roots_n,0), out;
    for (int i=0;i<roots_n;i++) for (int j=0;j<roots_n;j++)
      if ((d[i]>>j)&1ULL) indeg[j]++;
    std::priority_queue<int,std::vector<int>,std::greater<int>> q;
    for (int i=0;i<roots_n;i++) if (!indeg[i]) q.push(i);
    while (!q.empty()) {
      int i=q.top(); q.pop(); out.push_back(i);
      uint64_t m=d[i];
      while(m) {
        int j=__builtin_ctzll(m); m&=m-1;
        if (!--indeg[j]) q.push(j);
      }
    }
    if ((int)out.size()!=roots_n) {
      std::cerr << "Cyclic state reached\n"; std::exit(3);
    }
    return out;
  }

  Eval evaluate(const std::vector<int>& order) const {
    using Row=std::array<uint64_t,8>;
    std::array<Row,8> A{},B{},DA{},DB{};
    for(int i=0;i<n;i++) A[i][i]=B[i][i]=1;
    auto step=[&](std::array<Row,8>& X,std::array<Row,8>& DX,int rid){
      auto [i,j]=roots[rid];
      Row old=X[j], dold=DX[j];
      for(int c=0;c<n;c++) {
        X[j][c]=old[c]+X[i][c];
        DX[j][c]=dold[c]+X[i][c]+DX[i][c];
      }
    };
    for(int rid:order) step(A,DA,rid);
    for(auto it=order.rbegin();it!=order.rend();++it) step(B,DB,*it);
    uint64_t V=0,M=n;
    for(int i=0;i<n;i++) for(int j=0;j<n;j++) {
      V += A[i][j]*B[i][j];
      M += DA[i][j]*B[i][j]+A[i][j]*DB[i][j];
    }
    return {V,M};
  }

  std::vector<int> word_from_order(const std::vector<int>& order) const {
    std::vector<int> wires(n), word;
    for(int i=0;i<n;i++) wires[i]=i;
    for(int rid:order) {
      auto [a,b]=roots[rid]; int p=-1,q=-1;
      for(int i=0;i<n;i++) { if(wires[i]==a)p=i; if(wires[i]==b)q=i; }
      if(std::abs(p-q)!=1) { std::cerr<<"Non-adjacent root in order\n"; std::exit(4); }
      int g=std::min(p,q);
      if(wires[g]>wires[g+1]) { std::cerr<<"Length-decreasing root\n"; std::exit(4); }
      word.push_back(g); std::swap(wires[g],wires[g+1]);
    }
    return word;
  }

  // The standard bubble word 0,1,0,2,1,0,..., converted to packet bits.
  uint64_t initial_state() const {
    std::vector<int>wires(n),pos(roots_n,-1); for(int i=0;i<n;i++)wires[i]=i;
    int at=0;
    for(int top=1;top<n;top++) for(int g=top-1;g>=0;g--) {
      int a=wires[g],b=wires[g+1]; if(a>b)std::swap(a,b);
      pos[root_id[a][b]]=at++; std::swap(wires[g],wires[g+1]);
    }
    uint64_t state=0;
    for(size_t k=0;k<triples.size();k++) {
      auto t=triples[k];
      if(pos[t.bc]<pos[t.ac] && pos[t.ac]<pos[t.ab]) state|=1ULL<<k;
      else assert(pos[t.ab]<pos[t.ac] && pos[t.ac]<pos[t.bc]);
    }
    return state;
  }
};

static std::string vec_json(const std::vector<int>& x) {
  std::ostringstream o; o<<"[";
  for(size_t i=0;i<x.size();i++){if(i)o<<",";o<<x[i];} o<<"]"; return o.str();
}

int main(int argc,char**argv) {
  int n=argc>1?std::atoi(argv[1]):7;
  Model model(n);
  uint64_t start=model.initial_state();
  std::unordered_set<uint64_t> seen; seen.reserve(n==8?1600000:40000);
  std::vector<uint64_t> queue; queue.reserve(n==8?1300000:30000);
  seen.insert(start); queue.push_back(start);
  uint64_t bestV=std::numeric_limits<uint64_t>::max(),bestM=std::numeric_limits<uint64_t>::max();
  uint64_t bestState=0,bestVCount=0,bestLexCount=0;
  for(size_t cursor=0;cursor<queue.size();cursor++) {
    uint64_t state=queue[cursor];
    auto d=model.direct(state); auto succ=model.closure(d);
    std::vector<uint64_t> pred(model.roots_n,0);
    for(int i=0;i<model.roots_n;i++) for(int j=0;j<model.roots_n;j++)
      if((succ[i]>>j)&1ULL) pred[j]|=1ULL<<i;
    auto order=model.canonical_order(d); auto e=model.evaluate(order);
    if(e.V<bestV) {bestV=e.V;bestM=e.M;bestState=state;bestVCount=bestLexCount=1;}
    else if(e.V==bestV) {
      bestVCount++;
      if(e.M<bestM){bestM=e.M;bestState=state;bestLexCount=1;}
      else if(e.M==bestM)bestLexCount++;
    }
    for(size_t k=0;k<model.triples.size();k++) {
      auto t=model.triples[k];
      int first=((state>>k)&1ULL)?t.bc:t.ab;
      int last =((state>>k)&1ULL)?t.ab:t.bc;
      uint64_t interval=(succ[first] & pred[last]) | (1ULL<<first) | (1ULL<<last);
      uint64_t packet=(1ULL<<t.ab)|(1ULL<<t.ac)|(1ULL<<t.bc);
      if(interval!=packet)continue;
      uint64_t other=state^(1ULL<<k);
      if(seen.insert(other).second)queue.push_back(other);
    }
    if(n==8 && cursor && cursor%100000==0)
      std::cerr<<"visited "<<cursor<<", frontier "<<(queue.size()-cursor)<<", best ("<<bestV<<","<<bestM<<")\n";
  }
  auto d=model.direct(bestState); auto order=model.canonical_order(d);
  auto word=model.word_from_order(order);
  std::cout<<"{\n"
           <<"  \"mode\": \"exhaustive_higher_bruhat_B_n_2\",\n"
           <<"  \"n\": "<<n<<",\n"
           <<"  \"class_count\": "<<queue.size()<<",\n"
           <<"  \"minimum_trace\": "<<bestV<<",\n"
           <<"  \"minimum_trace_class_count\": "<<bestVCount<<",\n"
           <<"  \"lex_minimum_first_moment\": "<<bestM<<",\n"
           <<"  \"lex_minimum_class_count\": "<<bestLexCount<<",\n"
           <<"  \"mean_size\": "<<std::setprecision(17)<<(double)bestM/bestV<<",\n"
           <<"  \"mean_minus_log2_n\": "<<std::setprecision(17)<<(double)bestM/bestV-std::log2(n)<<",\n"
           <<"  \"state_bits_hex\": \""<<std::hex<<bestState<<std::dec<<"\",\n"
           <<"  \"canonical_root_ids\": "<<vec_json(order)<<",\n"
           <<"  \"word_zero_based\": "<<vec_json(word)<<"\n"
           <<"}\n";
}
