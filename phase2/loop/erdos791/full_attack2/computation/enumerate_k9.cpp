// Exhaustive bitset census of nine-element interval bases at ranges 32 and 33.
#include <array>
#include <cstdint>
#include <iostream>

bool covers(const std::array<int, 9>& a, int n) {
  uint64_t sums = 0;
  for (int x : a)
    for (int y : a)
      if (x + y <= n) sums |= uint64_t{1} << (x + y);
  const uint64_t target = (uint64_t{1} << (n + 1)) - 1;
  return (sums & target) == target;
}

int main() {
  for (int n : {33, 32}) {
    uint64_t tested = 0, found = 0;
    std::array<int, 9> a{0, 1};
    for (a[2] = 2; a[2] <= n - 6; ++a[2])
      for (a[3] = a[2] + 1; a[3] <= n - 5; ++a[3])
        for (a[4] = a[3] + 1; a[4] <= n - 4; ++a[4])
          for (a[5] = a[4] + 1; a[5] <= n - 3; ++a[5])
            for (a[6] = a[5] + 1; a[6] <= n - 2; ++a[6])
              for (a[7] = a[6] + 1; a[7] <= n - 1; ++a[7])
                for (a[8] = a[7] + 1; a[8] <= n; ++a[8]) {
                  ++tested;
                  if (!covers(a, n)) continue;
                  ++found;
                  std::cout << "basis n=" << n << ':';
                  for (int x : a) std::cout << ' ' << x;
                  std::cout << '\n';
                }
    std::cout << "summary n=" << n << " tested=" << tested
              << " found=" << found << '\n';
  }
}
