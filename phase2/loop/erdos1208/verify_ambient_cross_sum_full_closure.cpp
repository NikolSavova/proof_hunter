#include <algorithm>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <regex>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

using Point = std::pair<int, int>;

static std::vector<Point> read_points(const std::string& path) {
    std::ifstream input(path);
    assert(input);
    std::ostringstream buffer;
    buffer << input.rdbuf();
    const std::string text = buffer.str();

    const std::string marker = "POINTS = [";
    const std::size_t start = text.find(marker);
    assert(start != std::string::npos);
    const std::size_t finish = text.find("\n]", start + marker.size());
    assert(finish != std::string::npos);
    const std::string block = text.substr(start + marker.size(), finish - start);

    const std::regex pair_pattern(R"(\((-?[0-9]+),\s*(-?[0-9]+)\))");
    std::vector<Point> points;
    for (std::sregex_iterator it(block.begin(), block.end(), pair_pattern), end;
         it != end; ++it) {
        points.emplace_back(std::stoi((*it)[1]), std::stoi((*it)[2]));
    }
    return points;
}

int main(int argc, char** argv) {
    const std::string path = argc == 2
        ? argv[1]
        : "phase2/loop/erdos1208/verify_transverse_closure_witness.py";
    const std::vector<Point> points = read_points(path);
    assert(points.size() == 120);

    std::vector<Point> cross_sum;
    cross_sum.reserve(points.size() * points.size());
    for (const auto& [x, y] : points) {
        for (const auto& [u, v] : points) {
            cross_sum.emplace_back(x - v, y + u);
        }
    }
    std::sort(cross_sum.begin(), cross_sum.end());
    assert(std::adjacent_find(cross_sum.begin(), cross_sum.end()) == cross_sum.end());
    assert(cross_sum.size() == 120 * 120);

    int min_x = std::numeric_limits<int>::max();
    int max_x = std::numeric_limits<int>::min();
    int min_y = std::numeric_limits<int>::max();
    int max_y = std::numeric_limits<int>::min();
    for (const auto& [x, y] : cross_sum) {
        min_x = std::min(min_x, x);
        max_x = std::max(max_x, x);
        min_y = std::min(min_y, y);
        max_y = std::max(max_y, y);
    }

    const int span_x = max_x - min_x;
    const int span_y = max_y - min_y;
    const int width = 2 * span_y + 1;
    const int height = 2 * span_x + 1;
    assert(width == 6001 && height == 6001);
    std::vector<std::uint32_t> counts(
        static_cast<std::size_t>(width) * static_cast<std::size_t>(height), 0);

    for (const auto& [x, y] : cross_sum) {
        for (const auto& [u, v] : cross_sum) {
            const int dx = x - u;
            const int dy = y - v;
            const std::size_t index =
                static_cast<std::size_t>(dx + span_x) * width + (dy + span_y);
            ++counts[index];
        }
    }

    std::uint64_t energy = 0;
    std::uint32_t maximum = 0;
    int max_dx = 0;
    int max_dy = 0;
    for (int ix = 0; ix < height; ++ix) {
        for (int iy = 0; iy < width; ++iy) {
            const std::uint32_t value =
                counts[static_cast<std::size_t>(ix) * width + iy];
            energy += static_cast<std::uint64_t>(value) * value;
            const int dx = ix - span_x;
            const int dy = iy - span_y;
            if ((dx != 0 || dy != 0) && value > maximum) {
                maximum = value;
                max_dx = dx;
                max_dy = dy;
            }
        }
    }

    assert(energy == 24'957'897'968ULL);
    assert(maximum == 1071);
    assert((max_dx == 0 && std::abs(max_dy) == 1)
        || (max_dy == 0 && std::abs(max_dx) == 1));

    const int point_min_x = std::min_element(
        points.begin(), points.end(), [](Point a, Point b) { return a.first < b.first; }
    )->first;
    const int point_max_x = std::max_element(
        points.begin(), points.end(), [](Point a, Point b) { return a.first < b.first; }
    )->first;
    const int point_min_y = std::min_element(
        points.begin(), points.end(), [](Point a, Point b) { return a.second < b.second; }
    )->second;
    const int point_max_y = std::max_element(
        points.begin(), points.end(), [](Point a, Point b) { return a.second < b.second; }
    )->second;
    const int m = std::max(point_max_x - point_min_x, point_max_y - point_min_y);
    assert(m == 1514);

    const long double k = 120.0L;
    const long double energy_scale =
        k * k * k * k * k + static_cast<long double>(m) * m * k * k;
    const long double pointwise_scale = k + static_cast<long double>(m) * m / (k * k);
    std::cout << "k 120\n";
    std::cout << "m " << m << "\n";
    std::cout << "energy " << energy << "\n";
    std::cout << "maximum " << maximum << " shift " << max_dx << " " << max_dy << "\n";
    std::cout << "energy_ratio " << static_cast<double>(energy / energy_scale) << "\n";
    std::cout << "pointwise_ratio " << static_cast<double>(maximum / pointwise_scale) << "\n";
    std::cout << "ambient full-closure stress: PASS\n";
}
