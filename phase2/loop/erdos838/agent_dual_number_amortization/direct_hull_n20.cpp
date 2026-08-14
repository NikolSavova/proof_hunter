// Independent direct-hull verifier for the rational n=20 half-weight record.
// It does not use reflection orders or matrix products.  Every one of the
// 2^20 subsets is tested by an exact-int64 monotone-chain convex hull.

#include <array>
#include <cstdint>
#include <cstdlib>
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
  // The starting point is repeated at the end.
  return int(hull.size())-1 == k;
}

int main() {
  constexpr int n=20;
  const std::array<int64_t,n> y={
    358329966,-198927971,-63719209,217376688,-90978114,
    -51535675,-10240197,35270977,81248315,1125190,
    13012406,-271597462,170081922,-21479979,270310124,
    -492940940,-549521438,-607603894,412455433,450382350
  };
  std::array<Point,n> points;
  for (int i=0;i<n;i++) points[i]={i,y[i]};
  for (int i=0;i<n;i++) for (int j=i+1;j<n;j++) for (int k=j+1;k<n;k++)
    if (cross(points[i],points[j],points[k])==0) {
      std::cerr << "collinear triple\n"; return 2;
    }

  std::array<uint64_t,n+1> profile{};
  std::vector<Point> subset;
  subset.reserve(n);
  for (uint32_t mask=0; mask<(uint32_t(1)<<n); ++mask) {
    subset.clear();
    for (int i=0;i<n;i++) if ((mask>>i)&1U) subset.push_back(points[i]);
    if (convex_position(subset)) profile[subset.size()]++;
  }
  const std::array<uint64_t,n+1> expected={
    1,20,190,1140,2415,866,135,8,0,0,0,0,0,0,0,0,0,0,0,0,0
  };
  if (profile != expected) {
    std::cerr << "profile mismatch\n";
    for (auto x:profile) std::cerr << x << ' ';
    std::cerr << '\n'; return 3;
  }
  uint64_t V=0,M=0;
  for (int k=0;k<=n;k++) { V+=profile[k]; M+=uint64_t(k)*profile[k]; }
  if (V!=4775 || M!=18676) return 4;
  std::cout << "general_position=true\nprofile=";
  for (int k=0;k<=n;k++) { if (k) std::cout << ','; std::cout << profile[k]; }
  std::cout << "\nV=" << V << "\nM=" << M << '\n';
}
