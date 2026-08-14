// Numerical high-depth audit of the exact cyclic three-cluster IFS fitted in
// triangular_ifs_probe.py.  Root orders are obtained from long-double
// coordinates and checked as sorting networks.  Path counts are accumulated
// in log space; first logarithmic derivatives propagate the exact weighted-
// average degree recurrence, avoiding integer overflow.  Max degrees use the
// exact max-plus recurrence once the checked root order is fixed.

#include <algorithm>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <limits>
#include <numeric>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

using Real=long double;
struct Point{Real x,y;};
struct Edge{Real slope;int i,j;};

static constexpr Real neginf=-std::numeric_limits<Real>::infinity();

struct Map { Real a00,a01,a10,a11,b0,b1; };

static std::vector<Point> expand(const std::vector<Point>&p,const std::vector<Map>&maps){
  std::vector<Point>q;q.reserve(3*p.size());
  for(const auto&m:maps)for(const auto&z:p)
    q.push_back({m.a00*z.x+m.a01*z.y+m.b0,m.a10*z.x+m.a11*z.y+m.b1});
  return q;
}

static inline void add_term(Real oldLog,Real oldMean,Real termLog,Real termMean,
                            Real&newLog,Real&newMean){
  if(oldLog==neginf){newLog=termLog;newMean=termMean;return;}
  if(termLog==neginf){newLog=oldLog;newMean=oldMean;return;}
  Real hi=std::max(oldLog,termLog),lo=std::min(oldLog,termLog);
  newLog=hi+std::log1pl(std::expl(lo-hi));
  Real wo=std::expl(oldLog-newLog),wt=std::expl(termLog-newLog);
  newMean=wo*oldMean+wt*termMean;
}

struct Result{Real logV,mu;int maxSize;};

static Result evaluate(std::vector<Point> points){
  std::sort(points.begin(),points.end(),[](auto&a,auto&b){return a.x<b.x;});
  int n=points.size();std::vector<Edge>roots;roots.reserve(size_t(n)*(n-1)/2);
  for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)
    roots.push_back({(points[j].y-points[i].y)/(points[j].x-points[i].x),i,j});
  std::sort(roots.begin(),roots.end(),[](auto&a,auto&b){
    if(a.slope!=b.slope)return a.slope<b.slope;
    return std::tie(a.i,a.j)<std::tie(b.i,b.j);
  });
  // A wrong floating ordering of incident roots cannot pass this exact
  // sorting-network adjacency check.
  std::vector<int>wires(n),pos(n);std::iota(wires.begin(),wires.end(),0);
  std::iota(pos.begin(),pos.end(),0);
  for(auto&e:roots){
    int p=pos[e.i],q=pos[e.j];
    if(std::abs(p-q)!=1){std::cerr<<"non-adjacent slope crossing at n="<<n<<"\n";std::exit(3);}
    if(p>q)std::swap(p,q);
    std::swap(wires[p],wires[q]);pos[wires[p]]=p;pos[wires[q]]=q;
  }
  for(int i=0;i<n;i++)if(wires[i]!=n-1-i){std::cerr<<"not w0\n";std::exit(3);}

  size_t nn=size_t(n)*n;
  std::vector<Real> LA(nn,neginf),LB(nn,neginf),DA(nn,0),DB(nn,0);
  std::vector<int> MA(nn,-1000000),MB(nn,-1000000);
  for(int i=0;i<n;i++)LA[size_t(i)*n+i]=LB[size_t(i)*n+i]=0,MA[size_t(i)*n+i]=MB[size_t(i)*n+i]=0;
  auto step=[&](std::vector<Real>&L,std::vector<Real>&D,std::vector<int>&M,const Edge&e){
    int i=e.i,j=e.j;
    for(int c=0;c<=i;c++){
      size_t ii=size_t(i)*n+c,jj=size_t(j)*n+c;
      Real nl,nm;add_term(L[jj],D[jj],L[ii],1+D[ii],nl,nm);L[jj]=nl;D[jj]=nm;
      M[jj]=std::max(M[jj],1+M[ii]);
    }
  };
  for(const auto&e:roots)step(LA,DA,MA,e);
  for(auto it=roots.rbegin();it!=roots.rend();++it)step(LB,DB,MB,*it);

  Real totalLog=neginf,totalMean=0;int maxSize=1;
  for(int i=0;i<n;i++)for(int j=0;j<=i;j++){
    size_t z=size_t(i)*n+j;if(LA[z]==neginf||LB[z]==neginf)continue;
    Real lw=LA[z]+LB[z],degree=(i==j?1:DA[z]+DB[z]);
    Real nl,nm;add_term(totalLog,totalMean,lw,degree,nl,nm);totalLog=nl;totalMean=nm;
    if(i!=j)maxSize=std::max(maxSize,MA[z]+MB[z]);
  }
  return {totalLog,totalMean,maxSize};
}

int main(int argc,char**argv){
  int maxDepth=argc>1?std::atoi(argv[1]):6;
  // Exact rational constants from triangular_ifs_certificate.json, rendered
  // here as long-double quotients.  b=macro+translation because shrink=1.
  std::vector<Point> points={
    {33791.0L/3,14233.0L},{13734.0L,162353.0L/3},{42029.0L,23221.0L}};
  std::vector<Map> maps={
    {1444451988.0L/2710938845,811656951.0L/5421877690,
     3221266173.0L/5421877690,2420885931.0L/10843755380,
     33791.0L/3-53591676719203.0L/3253126614,
     14233.0L-43567068503741.0L/2168751076},
    {10617000.0L/542187769,-60470700.0L/542187769,
     120872295.0L/542187769,428459775.0L/1084375538,
     13734.0L+1608593554500.0L/542187769,
     162353.0L/3-55438109748775.0L/3253126614},
    {-739405023.0L/5421877690,8921368209.0L/10843755380,
     55730445.0L/1084375538,-1420776849.0L/2168751076,
     42029.0L-47854989855239.0L/2168751076,
     23221.0L+40877350701315.0L/2168751076}
  };
  std::cout<<"[\n";
  for(int d=1;d<=maxDepth;d++){
    if(d>1)points=expand(points,maps);
    auto r=evaluate(points);Real log2V=r.logV/std::log(2.0L),log2n=std::log2((Real)points.size());
    if(d>1)std::cout<<",\n";
    std::cout<<std::setprecision(18)<<"  {\"depth\":"<<d<<",\"n\":"<<points.size()
      <<",\"log2_trace\":"<<log2V<<",\"mean_size\":"<<r.mu
      <<",\"mean_minus_log2_n\":"<<r.mu-log2n
      <<",\"normalized_log_trace\":"<<log2V/(log2n*log2n)
      <<",\"maximum_convex_subset_size\":"<<r.maxSize<<"}";
  }
  std::cout<<"\n]\n";
}
