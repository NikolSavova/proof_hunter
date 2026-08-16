// Exact-face / numerical-entropy probe for block deletion on the saved n=20
// planar record.  Convexity is tested directly with int64 orientations.  The
// subset zeta transform then obtains Z_Q(1) and 2^20 Z_Q(1/2) for every Q.

#include <array>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <vector>

struct Point { int64_t x, y; };

static int64_t cross(const Point &a, const Point &b, const Point &c) {
  return (b.x-a.x)*(c.y-a.y) - (b.y-a.y)*(c.x-a.x);
}

static bool convex_position(const std::vector<Point> &p) {
  const int k = int(p.size());
  if (k <= 2) return true;
  std::vector<Point> hull;
  hull.reserve(2*k);
  for (const auto &q : p) {
    while (hull.size() >= 2 && cross(hull[hull.size()-2], hull.back(), q) <= 0)
      hull.pop_back();
    hull.push_back(q);
  }
  const std::size_t lower = hull.size();
  for (int i=k-2; i>=0; --i) {
    const Point q=p[i];
    while (hull.size() > lower && cross(hull[hull.size()-2], hull.back(), q) <= 0)
      hull.pop_back();
    hull.push_back(q);
  }
  return int(hull.size())-1 == k;
}

int main() {
  constexpr int n=20;
  constexpr uint32_t N=(uint32_t(1)<<n);
  const std::array<int64_t,n> y={
    358329966,-198927971,-63719209,217376688,-90978114,
    -51535675,-10240197,35270977,81248315,1125190,
    13012406,-271597462,170081922,-21479979,270310124,
    -492940940,-549521438,-607603894,412455433,450382350
  };
  std::array<Point,n> points;
  for (int i=0;i<n;i++) points[i]={i,y[i]};
  for (int i=0;i<n;i++) for (int j=i+1;j<n;j++) for (int k=j+1;k<n;k++)
    if (cross(points[i],points[j],points[k])==0) return 2;

  // z1[Q]=Z_Q(1).  zhalf_scaled[Q]=2^20 Z_Q(1/2), so all arithmetic in
  // the transform is integral and exactly reproducible.
  std::vector<uint64_t> z1(N,0), zhalf_scaled(N,0);
  std::vector<uint64_t> m1(N,0), mhalf_scaled(N,0);
  std::vector<Point> subset;
  subset.reserve(n);
  for (uint32_t mask=0; mask<N; ++mask) {
    subset.clear();
    for (int i=0;i<n;i++) if ((mask>>i)&1U) subset.push_back(points[i]);
    if (convex_position(subset)) {
      z1[mask]=1;
      zhalf_scaled[mask]=uint64_t(1)<<(n-subset.size());
      m1[mask]=subset.size();
      mhalf_scaled[mask]=uint64_t(subset.size())<<(n-subset.size());
    }
  }
  for (int i=0;i<n;i++) for (uint32_t mask=0;mask<N;mask++)
    if ((mask>>i)&1U) {
      z1[mask]+=z1[mask^(uint32_t(1)<<i)];
      zhalf_scaled[mask]+=zhalf_scaled[mask^(uint32_t(1)<<i)];
      m1[mask]+=m1[mask^(uint32_t(1)<<i)];
      mhalf_scaled[mask]+=mhalf_scaled[mask^(uint32_t(1)<<i)];
    }

  // Dynamic program for the full q_{1/2}-deletion path.  rsum is the
  // accumulated integrated normalized-variance term, and klsum the
  // accumulated local deletion KL.  Their sum must be L exactly up to
  // floating roundoff.
  std::vector<long double> rsum(N,0), klsum(N,0), minsum(N,0), maxsum(N,0);
  for (uint32_t mask=1;mask<N;mask++) {
    const int m=__builtin_popcount(mask);
    const long double mu1=(long double)m1[mask]/z1[mask];
    const long double muh=(long double)mhalf_scaled[mask]/zhalf_scaled[mask];
    const long double r=std::log(((long double)m-muh)/((long double)m-mu1));
    long double child1=0,childh=0;
    for (int i=0;i<n;i++) if ((mask>>i)&1U) {
      const uint32_t child=mask^(uint32_t(1)<<i);
      child1+=(long double)z1[child];
      childh+=(long double)zhalf_scaled[child];
    }
    long double er=0,ek=0,d=0;
    long double child_min=1e100L, child_max=-1e100L;
    for (int i=0;i<n;i++) if ((mask>>i)&1U) {
      const uint32_t child=mask^(uint32_t(1)<<i);
      const long double q1=(long double)z1[child]/child1;
      const long double qh=(long double)zhalf_scaled[child]/childh;
      er+=qh*rsum[child];
      ek+=qh*klsum[child];
      d+=qh*std::log(qh/q1);
      child_min=std::min(child_min,minsum[child]);
      child_max=std::max(child_max,maxsum[child]);
    }
    rsum[mask]=r+er;
    klsum[mask]=d+ek;
    minsum[mask]=r+child_min;
    maxsum[mask]=r+child_max;
  }

  const long double scale=std::ldexp((long double)1.0,-n);
  const long double parent_L=std::log((long double)z1[N-1]/
                                     ((long double)zhalf_scaled[N-1]*scale));
  if (z1[N-1]!=4775 || zhalf_scaled[N-1]!=399687680ULL) return 3;
  if (std::abs(rsum[N-1]+klsum[N-1]-parent_L)>1e-12L) return 4;
  if (rsum[N-1]+1e-12L<std::log((long double)n/2)) return 5;
  std::cout << std::setprecision(18);
  std::cout << "parent_V=" << z1[N-1]
            << " parent_Zhalf_scaled=" << zhalf_scaled[N-1]
            << " parent_L=" << parent_L << "\n";
  std::cout << "path_integrated_variance=" << rsum[N-1]
            << " path_KL=" << klsum[N-1]
            << " path_sum_error=" << rsum[N-1]+klsum[N-1]-parent_L
            << " target_log_n_over_2=" << std::log((long double)n/2)
            << " path_min=" << minsum[N-1]
            << " path_max=" << maxsum[N-1] << "\n";
  std::cout << "m block_drift target_log_ratio normalized_drift KL mean_child_L\n";
  for (int m=1;m<n;m++) {
    long double s1=0,sh=0;
    for (uint32_t mask=0;mask<N;mask++) if (__builtin_popcount(mask)==m) {
      s1+=(long double)z1[mask];
      sh+=(long double)zhalf_scaled[mask];
    }
    long double meanL=0,D=0;
    for (uint32_t mask=0;mask<N;mask++) if (__builtin_popcount(mask)==m) {
      long double q1=(long double)z1[mask]/s1;
      long double qh=(long double)zhalf_scaled[mask]/sh;
      long double lq=std::log((long double)z1[mask]/
                              ((long double)zhalf_scaled[mask]*scale));
      meanL+=qh*lq;
      D+=qh*std::log(qh/q1);
    }
    long double drift=parent_L-meanL;
    long double target=std::log((long double)n/m);
    std::cout << m << ' ' << drift << ' ' << target << ' '
              << drift/target << ' ' << D << ' ' << meanL << '\n';
  }
}
