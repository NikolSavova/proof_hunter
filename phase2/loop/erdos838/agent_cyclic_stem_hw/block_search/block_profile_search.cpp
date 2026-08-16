// Fixed-x stretchable search for weak block-doubling profiles.
//
// The ordinate vector is integral, so every slope comparison is exact in
// __int128.  A candidate with a tied slope is rejected.  The rank profile is
// evaluated by the endpoint-chain transvection identity, truncated at the
// largest rank relevant to the requested block.

#include <algorithm>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <numeric>
#include <random>
#include <string>
#include <tuple>
#include <vector>

using u128 = unsigned __int128;

struct Slope {
  int i, j;
  std::int64_t dy;
  int dx;
};

static long double as_ld(u128 x) {
  const u128 lo_mask = (u128(1) << 64) - 1;
  return static_cast<long double>(static_cast<std::uint64_t>(x >> 64))
             * 18446744073709551616.0L
         + static_cast<long double>(static_cast<std::uint64_t>(x & lo_mask));
}

static std::string decimal(u128 x) {
  if (!x) return "0";
  std::string out;
  while (x) {
    out.push_back(char('0' + x % 10));
    x /= 10;
  }
  std::reverse(out.begin(), out.end());
  return out;
}

static int ceil_log2(int n) {
  int ell = 0, value = 1;
  while (value < n) value <<= 1, ++ell;
  return ell;
}

// Return every positive root in exact increasing-slope order.  Empty means
// that the fixed-x configuration has a collinear triple.
static std::vector<std::pair<int, int>> slope_roots(
    const std::vector<std::int64_t>& y) {
  const int n = int(y.size());
  std::vector<Slope> slopes;
  slopes.reserve(n * (n - 1) / 2);
  for (int i = 0; i < n; ++i)
    for (int j = i + 1; j < n; ++j)
      slopes.push_back({i, j, y[j] - y[i], j - i});
  auto less = [](const Slope& a, const Slope& b) {
    __int128 lhs = __int128(a.dy) * b.dx;
    __int128 rhs = __int128(b.dy) * a.dx;
    if (lhs != rhs) return lhs < rhs;
    return std::tie(a.i, a.j) < std::tie(b.i, b.j);
  };
  std::sort(slopes.begin(), slopes.end(), less);
  for (std::size_t p = 1; p < slopes.size(); ++p) {
    __int128 lhs = __int128(slopes[p - 1].dy) * slopes[p].dx;
    __int128 rhs = __int128(slopes[p].dy) * slopes[p - 1].dx;
    if (lhs == rhs) return {};
  }
  std::vector<std::pair<int, int>> roots;
  roots.reserve(slopes.size());
  for (auto s : slopes) roots.push_back({s.i, s.j});
  return roots;
}

// Matrix entry (row,column) is a polynomial in z, stored coefficient-major.
static std::vector<u128> path_matrix(
    int n, int cutoff, const std::vector<std::pair<int, int>>& roots,
    bool reverse) {
  const std::size_t stride = cutoff + 1;
  std::vector<u128> matrix(std::size_t(n) * n * stride);
  auto at = [&](int row, int col, int degree) -> u128& {
    return matrix[(std::size_t(row) * n + col) * stride + degree];
  };
  for (int i = 0; i < n; ++i) at(i, i, 0) = 1;
  for (std::size_t step = 0; step < roots.size(); ++step) {
    std::size_t position = reverse ? roots.size() - 1 - step : step;
    auto [i, j] = roots[position];
    for (int col = 0; col < n; ++col)
      for (int degree = 1; degree <= cutoff; ++degree)
        at(j, col, degree) += at(i, col, degree - 1);
  }
  return matrix;
}

static std::vector<u128> profile(
    const std::vector<std::int64_t>& y, int cutoff) {
  const int n = int(y.size());
  auto roots = slope_roots(y);
  if (roots.empty()) return {};
  auto cups = path_matrix(n, cutoff, roots, false);
  auto caps = path_matrix(n, cutoff, roots, true);
  const std::size_t stride = cutoff + 1;
  std::vector<u128> answer(cutoff + 1);
  answer[0] = 1;
  answer[1] = n;
  for (int row = 0; row < n; ++row) {
    for (int col = 0; col < n; ++col) {
      std::size_t base = (std::size_t(row) * n + col) * stride;
      for (int a = 0; a <= cutoff; ++a) if (cups[base + a])
        for (int b = 0; a + b <= cutoff; ++b) if (caps[base + b])
          if (a + b >= 2)
            answer[a + b] += cups[base + a] * caps[base + b];
    }
  }
  return answer;
}

static long double block_score(const std::vector<u128>& v, int n, int block) {
  int ell = ceil_log2(n);
  long double worst = std::numeric_limits<long double>::infinity();
  for (int k = 0; k <= ell - 2 * block; ++k)
    worst = std::min(worst, as_ld(v[k + block]) / (2 * as_ld(v[k])));
  return worst;
}

static int minimal_block(const std::vector<u128>& v, int n) {
  int ell = ceil_log2(n);
  for (int b = 1; b <= ell; ++b) {
    bool good = true;
    for (int k = 0; k <= ell - 2 * b; ++k)
      if (v[k + b] < 2 * v[k]) good = false;
    if (good) return b;
  }
  return ell;
}

int main(int argc, char** argv) {
  if (argc < 6) {
    std::cerr << "usage: block_profile_search n block steps restarts seed [output]\n";
    return 2;
  }
  const int n = std::stoi(argv[1]);
  const int block = std::stoi(argv[2]);
  const long long steps = std::stoll(argv[3]);
  const int restarts = std::stoi(argv[4]);
  const std::uint64_t seed = std::stoull(argv[5]);
  const int ell = ceil_log2(n);
  // Retain through ell so the reported minimal block is audited as well as
  // the requested target block.
  const int cutoff = ell;
  if (ell - 2 * block < 0) {
    std::cerr << "vacuous requested block\n";
    return 2;
  }
  std::mt19937_64 rng(seed);
  std::uniform_real_distribution<long double> uniform(0, 1);
  std::vector<std::int64_t> global_y;
  std::vector<u128> global_profile;
  long double global_score = std::numeric_limits<long double>::infinity();
  long long evaluated = 0, accepted = 0;
  for (int restart = 0; restart < restarts; ++restart) {
    std::vector<std::int64_t> y(n);
    for (auto& value : y)
      value = std::int64_t(rng() % 2000000001ULL) - 1000000000LL;
    auto current_profile = profile(y, cutoff);
    if (current_profile.empty()) { --restart; continue; }
    long double current = block_score(current_profile, n, block);
    if (current < global_score) {
      global_score = current; global_y = y; global_profile = current_profile;
    }
    for (long long step = 0; step < steps; ++step) {
      auto candidate = y;
      int point = int(rng() % n);
      // Large chamber jumps alternate with local ordinate adjustments.
      if ((rng() & 3) == 0)
        candidate[point] = std::int64_t(rng() % 2000000001ULL) - 1000000000LL;
      else {
        int scale_power = int(rng() % 9);
        std::int64_t scale = 1;
        for (int p = 0; p < scale_power; ++p) scale *= 10;
        candidate[point] += std::int64_t(rng() % (2 * scale + 1)) - scale;
      }
      auto candidate_profile = profile(candidate, cutoff);
      if (candidate_profile.empty()) continue;
      ++evaluated;
      long double value = block_score(candidate_profile, n, block);
      long double phase = (step % std::max<long long>(100, steps / 8)) /
                          (long double)std::max<long long>(99, steps / 8 - 1);
      long double temperature = 0.06L * (1 - phase) + 0.00001L;
      bool take = value <= current ||
                  uniform(rng) < std::exp((current - value) / temperature);
      if (take) {
        y.swap(candidate); current_profile.swap(candidate_profile);
        current = value; ++accepted;
      }
      if (current < global_score) {
        global_score = current; global_y = y; global_profile = current_profile;
        std::cerr << "best restart=" << restart << " step=" << step
                  << " score=" << std::setprecision(12)
                  << double(global_score) << " minimal_b="
                  << minimal_block(global_profile, n) << "\n";
      }
    }
  }
  std::ostream* out = &std::cout;
  std::ofstream file;
  if (argc >= 7) { file.open(argv[6]); out = &file; }
  *out << "{\n  \"n\": " << n << ",\n  \"ell\": " << ell
       << ",\n  \"target_block\": " << block
       << ",\n  \"target_block_min_ratio_to_doubling\": "
       << std::setprecision(18) << double(global_score)
       << ",\n  \"minimal_doubling_block\": "
       << minimal_block(global_profile, n)
       << ",\n  \"steps_per_restart\": " << steps
       << ",\n  \"restarts\": " << restarts
       << ",\n  \"seed\": " << seed
       << ",\n  \"evaluated\": " << evaluated
       << ",\n  \"accepted\": " << accepted
       << ",\n  \"y_coordinates\": [";
  for (int i = 0; i < n; ++i) {
    if (i) *out << ',';
    *out << global_y[i];
  }
  *out << "],\n  \"profile_through_cutoff\": [";
  for (std::size_t k = 0; k < global_profile.size(); ++k) {
    if (k) *out << ',';
    *out << decimal(global_profile[k]);
  }
  *out << "]\n}\n";
}
