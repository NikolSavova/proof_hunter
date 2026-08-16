// Scan the aligned Aichholzer--Aurenhammer--Krasser order-type and k-gon
// files.  For every record, compute the minimum cap count over all generic
// projection chambers of the displayed realization.  Parallel critical
// directions are handled by all orders of their disjoint simultaneous swaps.

#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <limits>
#include <map>
#include <numeric>
#include <set>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

using Point = std::pair<int,int>;

static int orient(const Point& a, const Point& b, const Point& c) {
  int64_t z = int64_t(b.first-a.first)*(c.second-a.second)
            - int64_t(b.second-a.second)*(c.first-a.first);
  if (!z) { std::cerr << "collinear database record\n"; std::exit(3); }
  return z > 0 ? 1 : -1;
}

struct Fraction {
  int64_t num, den; // den > 0
  bool operator<(const Fraction& o) const {
    return (__int128)num*o.den < (__int128)o.num*den;
  }
  bool operator==(const Fraction& o) const {
    return (__int128)num*o.den == (__int128)o.num*den;
  }
};

struct Event {
  Fraction at;
  int a,b;
};

static uint64_t cap_count(const std::vector<Point>& p,
                          const std::vector<int>& order) {
  const int n = p.size();
  uint64_t cap[12][12]{};
  uint64_t total = n;
  for (int i=0;i<n;i++) for (int j=i+1;j<n;j++) {
    uint64_t value=1;
    for (int h=0;h<i;h++)
      if (orient(p[order[h]],p[order[i]],p[order[j]]) < 0)
        value += cap[h][i];
    cap[i][j]=value;
    total += value;
  }
  return total;
}

static void audit_order(const std::vector<Point>& p,
                        const std::vector<int>& order,
                        uint64_t& answer) {
  answer = std::min(answer,cap_count(p,order));
  std::vector<int> reverse(order.rbegin(),order.rend());
  answer = std::min(answer,cap_count(p,reverse));
}

static uint64_t minimum_cap(const std::vector<Point>& p) {
  const int n=p.size();
  std::vector<Event> events;
  for (int i=0;i<n;i++) for (int j=i+1;j<n;j++) {
    int64_t dy=int64_t(p[j].second)-p[i].second;
    if (!dy) continue;
    int64_t num=-(int64_t(p[j].first)-p[i].first), den=dy;
    if (den<0) {num=-num;den=-den;}
    int64_t g=std::gcd(std::llabs(num),den);
    events.push_back({{num/g,den/g},i,j});
  }
  std::sort(events.begin(),events.end(),[](const Event& x,const Event& y){
    if (x.at<y.at) return true;
    if (y.at<x.at) return false;
    return std::tie(x.a,x.b)<std::tie(y.a,y.b);
  });

  // At s=-infinity, x+s*y is ordered by decreasing y, then increasing x.
  std::vector<int> order(n);
  std::iota(order.begin(),order.end(),0);
  std::sort(order.begin(),order.end(),[&](int i,int j){
    if (p[i].second!=p[j].second) return p[i].second>p[j].second;
    return p[i].first<p[j].first;
  });
  uint64_t answer=std::numeric_limits<uint64_t>::max();
  audit_order(p,order,answer);

  for (size_t first=0;first<events.size();) {
    size_t last=first+1;
    while(last<events.size() && events[last].at==events[first].at) last++;
    std::vector<std::pair<int,int>> group;
    for(size_t k=first;k<last;k++) group.push_back({events[k].a,events[k].b});

    // Equal-slope pairs are vertex-disjoint in general position.  Every
    // ordering is obtained by an arbitrarily small chirotope-preserving
    // perturbation, so audit every intermediate generic chamber.
    std::sort(group.begin(),group.end());
    do {
      auto trial=order;
      for(auto [a,b]:group) {
        int pa=-1,pb=-1;
        for(int i=0;i<n;i++) {if(trial[i]==a)pa=i;if(trial[i]==b)pb=i;}
        if (std::abs(pa-pb)!=1) {
          std::cerr << "nonadjacent simultaneous crossing\n"; std::exit(4);
        }
        std::swap(trial[pa],trial[pb]);
        audit_order(p,trial,answer);
      }
    } while(std::next_permutation(group.begin(),group.end()));

    // Any ordering of disjoint swaps gives the same post-event order.
    for(size_t k=first;k<last;k++) {
      int a=events[k].a,b=events[k].b,pa=-1,pb=-1;
      for(int i=0;i<n;i++) {if(order[i]==a)pa=i;if(order[i]==b)pb=i;}
      if(std::abs(pa-pb)!=1) {std::cerr<<"nonadjacent crossing\n";std::exit(4);}
      std::swap(order[pa],order[pb]);
    }
    first=last;
  }
  return answer;
}

static uint16_t get16(std::istream& f) {
  unsigned char a,b; f.read((char*)&a,1);f.read((char*)&b,1);
  return uint16_t(a)|(uint16_t(b)<<8);
}

int main(int argc,char**argv) {
  if(argc<6) {
    std::cerr<<"usage: scan_endpoint_envelope n b08|b16 otypes kgons maxV\n";
    return 2;
  }
  int n=std::atoi(argv[1]);
  bool wide=std::string(argv[2])=="b16";
  std::ifstream points(argv[3],std::ios::binary), kgons(argv[4],std::ios::binary);
  uint64_t maxV=std::strtoull(argv[5],nullptr,10);
  if(!points||!kgons){std::cerr<<"cannot open input\n";return 2;}
  std::map<uint64_t,std::pair<uint64_t,uint64_t>> byV; // V -> (min C,count)
  uint64_t records=0,audited=0;
  while(true) {
    std::vector<Point> p;
    for(int i=0;i<n;i++) {
      int x,y;
      if(wide){if(points.peek()==EOF)break;x=get16(points);y=get16(points);}
      else {unsigned char a,b;if(!points.read((char*)&a,1))break;points.read((char*)&b,1);x=a;y=b;}
      p.push_back({x,y});
    }
    if(p.empty())break;
    if((int)p.size()!=n){std::cerr<<"partial point record\n";return 3;}
    uint64_t V=n+uint64_t(n)*(n-1)/2;
    for(int k=3;k<=n;k++){unsigned char c;if(!kgons.read((char*)&c,1)){std::cerr<<"partial kgons\n";return 3;}V+=c;}
    if(V<=maxV) {
      uint64_t C=minimum_cap(p); audited++;
      auto it=byV.find(V);
      if(it==byV.end()) byV[V]={C,1};
      else if(C<it->second.first)it->second={C,1};
      else if(C==it->second.first)it->second.second++;
    }
    records++;
  }
  std::cout<<"{\"n\":"<<n<<",\"records\":"<<records
           <<",\"audited\":"<<audited<<",\"maxV\":"<<maxV<<",\"profiles\":[";
  bool first=true;
  for(auto [V,row]:byV){if(!first)std::cout<<",";first=false;std::cout<<"["<<V<<","<<row.first<<","<<row.second<<"]";}
  std::cout<<"]}\n";
}
