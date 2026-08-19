#include <algorithm>
#include <array>
#include <cmath>
#include <iostream>
#include <numeric>
#include <random>
#include <set>
#include <string>
#include <unordered_set>
#include <utility>
#include <vector>

using Matching = std::vector<int>;
using Matchings = std::array<Matching, 4>;
using Coeff = std::pair<int, int>;
using Form = std::vector<Coeff>;

std::vector<int> components(const Matching& x, const Matching& y) {
  int n = x.size(), count = 0;
  std::vector<int> label(n, -1), stack;
  for (int root = 0; root < n; ++root) {
    if (label[root] >= 0) continue;
    label[root] = count;
    stack = {root};
    while (!stack.empty()) {
      int v = stack.back(); stack.pop_back();
      for (int w : {x[v], y[v]}) if (label[w] < 0) {
        label[w] = count; stack.push_back(w);
      }
    }
    ++count;
  }
  return label;
}

std::string serialize(const Form& form) {
  std::string out;
  out.reserve(2 * form.size());
  for (auto [a,b] : form) {
    out.push_back(static_cast<char>(a + 8));
    out.push_back(static_cast<char>(b + 8));
  }
  return out;
}

std::string unit_signature(Form value) {
  std::string best;
  bool first = true;
  for (int turn = 0; turn < 4; ++turn) {
    std::string candidate = serialize(value);
    if (first || candidate < best) { best = candidate; first = false; }
    for (auto& [a,b] : value) { int old = a; a = -b; b = old; }
  }
  return best;
}

std::tuple<int,int,int> score(const Matchings& matchings) {
  const auto a0 = components(matchings[0], matchings[1]);
  const auto a1 = components(matchings[2], matchings[3]);
  const auto b0 = components(matchings[0], matchings[2]);
  const auto b1 = components(matchings[1], matchings[3]);
  std::array<std::vector<int>,4> maps = {a0,a1,b0,b1};
  std::array<int,4> counts, offsets;
  int dimension = 0;
  for (int role=0; role<4; ++role) {
    counts[role] = 1 + *std::max_element(maps[role].begin(), maps[role].end());
    offsets[role] = dimension; dimension += counts[role];
  }
  const int p = dimension++;
  std::vector<Form> points;
  for (int j=0; j<dimension; ++j) {
    Form form(dimension, {0,0}); form[j] = {1,0}; points.push_back(form);
  }
  for (int record=0; record<(int)matchings[0].size(); ++record) {
    Form c(dimension, {0,0}); c[p] = {1,0};
    const int signs[4] = {1,-1,-1,1};
    for (int role=0; role<4; ++role)
      c[offsets[role]+maps[role][record]] = {0,signs[role]};
    points.push_back(c);
  }
  std::unordered_set<std::string> point_set;
  for (const auto& point : points) point_set.insert(serialize(point));
  int duplicates = points.size() - point_set.size();
  std::unordered_set<std::string> edges;
  int repeats = 0;
  for (int i=0; i<(int)points.size(); ++i) for (int j=i+1; j<(int)points.size(); ++j) {
    Form difference(dimension);
    for (int q=0; q<dimension; ++q)
      difference[q] = {points[i][q].first-points[j][q].first,
                       points[i][q].second-points[j][q].second};
    if (!edges.insert(unit_signature(std::move(difference))).second) ++repeats;
  }
  return {100000*duplicates+repeats, duplicates, repeats};
}

std::set<std::pair<int,int>> edges(const Matching& matching) {
  std::set<std::pair<int,int>> result;
  for (int i=0; i<(int)matching.size(); ++i) if (i<matching[i]) result.insert({i,matching[i]});
  return result;
}

Matching fresh_matching(int n, const std::set<std::pair<int,int>>& used, std::mt19937_64& rng) {
  while (true) {
    std::vector<int> vertices(n); std::iota(vertices.begin(), vertices.end(), 0);
    std::shuffle(vertices.begin(), vertices.end(), rng);
    Matching mate(n,-1); bool okay=true;
    while (!vertices.empty()) {
      int a=vertices.back(); vertices.pop_back();
      std::vector<int> choices;
      for (int b:vertices) if (!used.count(std::minmax(a,b))) choices.push_back(b);
      if (choices.empty()) { okay=false; break; }
      int b=choices[rng()%choices.size()];
      vertices.erase(std::find(vertices.begin(), vertices.end(), b));
      mate[a]=b; mate[b]=a;
    }
    if (okay) return mate;
  }
}

void print_matchings(const Matchings& matchings) {
  std::cout << "matchings\n";
  for (const auto& matching:matchings) {
    for (int x:matching) std::cout << x << ' ';
    std::cout << '\n';
  }
}

int main(int argc, char** argv) {
  int n = argc>1 ? std::stoi(argv[1]) : 14;
  long long steps = argc>2 ? std::stoll(argv[2]) : 2000000;
  unsigned long long seed = argc>3 ? std::stoull(argv[3]) : 1208;
  std::mt19937_64 rng(seed);
  Matchings matchings;
  matchings[0].resize(n);
  for (int i=0; i<n; ++i) matchings[0][i]=i^1;
  auto used=edges(matchings[0]);
  for (int colour=1; colour<4; ++colour) {
    matchings[colour]=fresh_matching(n,used,rng);
    auto next=edges(matchings[colour]); used.insert(next.begin(),next.end());
  }
  auto current=score(matchings), best=current; Matchings best_matchings=matchings;
  std::cout << "initial " << std::get<0>(current) << ' ' << std::get<1>(current) << ' ' << std::get<2>(current) << '\n';
  for (long long step=0; step<steps; ++step) {
    int colour=1+rng()%3;
    auto old=matchings[colour]; auto old_edges=edges(old);
    auto first=*std::next(old_edges.begin(),rng()%old_edges.size());
    auto second=*std::next(old_edges.begin(),rng()%old_edges.size());
    if (first==second) continue;
    int a=first.first,b=first.second,c=second.first,d=second.second;
    std::array<std::pair<int,int>,2> replacement;
    if (rng()%2) replacement={std::minmax(a,c),std::minmax(b,d)};
    else replacement={std::minmax(a,d),std::minmax(b,c)};
    std::set<std::pair<int,int>> other;
    for (int q=0;q<4;++q) if(q!=colour) { auto es=edges(matchings[q]); other.insert(es.begin(),es.end()); }
    if (other.count(replacement[0])||other.count(replacement[1])) continue;
    Matching candidate=old;
    for(auto [x,y]:replacement){candidate[x]=y;candidate[y]=x;}
    matchings[colour]=candidate;
    auto next_score=score(matchings);
    double temperature=std::max(0.05,5.0*(1.0-double(step)/steps));
    int delta=std::get<0>(next_score)-std::get<0>(current);
    if(delta<=0||std::generate_canonical<double,64>(rng)<std::exp(-delta/temperature)) current=next_score;
    else matchings[colour]=old;
    if(current<best){best=current;best_matchings=matchings;
      std::cout<<"best "<<step<<' '<<std::get<0>(best)<<' '<<std::get<1>(best)<<' '<<std::get<2>(best)<<'\n';
      if(std::get<0>(best)==0){print_matchings(best_matchings);return 0;}
    }
  }
  std::cout<<"complete "<<std::get<0>(best)<<' '<<std::get<1>(best)<<' '<<std::get<2>(best)<<'\n';
  print_matchings(best_matchings);
}
