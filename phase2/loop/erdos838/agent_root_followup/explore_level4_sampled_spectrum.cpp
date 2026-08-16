#include <algorithm>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <limits>
#include <numeric>
#include <tuple>
#include <utility>
#include <vector>

using u64 = std::uint64_t;
using u128 = unsigned __int128;

static std::string show(u128 x) {
    if (!x) return "0";
    std::string s;
    while (x) {
        s.push_back(char('0' + x % 10));
        x /= 10;
    }
    std::reverse(s.begin(), s.end());
    return s;
}

static std::pair<u64,u64> chain_counts(
    const std::vector<std::int8_t>& signs, const std::vector<int>& order) {
    int n = int(order.size());
    std::vector<u64> cap(n*n), cup(n*n);
    u64 C = n, U = n;
    for (int i=0;i<n;i++) for (int j=i+1;j<n;j++) {
        u64 a=1,b=1;
        for (int h=0;h<i;h++) {
            int s=signs[(order[h]*n+order[i])*n+order[j]];
            if (s<0) a += cap[h*n+i];
            else b += cup[h*n+i];
        }
        cap[i*n+j]=a; cup[i*n+j]=b; C+=a; U+=b;
    }
    return {C,U};
}

static u128 wrapper_value(
    const std::tuple<u64,u64>& a,
    const std::tuple<u64,u64>& b,
    const std::tuple<u64,u64>& c,
    u64 size, u64 faces) {
    std::vector<std::tuple<u64,u64,u64,u64>> z = {
        {1,1,1,1}, {size,std::get<0>(a),std::get<1>(a),faces},
        {size,std::get<0>(b),std::get<1>(b),faces},
        {size,std::get<0>(c),std::get<1>(c),faces}, {1,1,1,1}};
    u128 total=0;
    for (auto [n,C,U,W]:z) total += W;
    for (int i=0;i<5;i++) {
        u128 middle=1;
        for (int j=i+1;j<5;j++) {
            total += u128(std::get<1>(z[i]))*std::get<2>(z[j])*middle;
            middle *= 1+std::get<0>(z[j]);
        }
    }
    return total;
}

struct Line {
    u64 slope=0, intercept=0;
    int profile=-1;
};

static u128 eval(const Line& line, u64 x) {
    return u128(line.slope)*x + line.intercept;
}

struct DiscreteLiChao {
    const std::vector<u64>& xs;
    std::vector<Line> tree;
    std::vector<char> used;

    explicit DiscreteLiChao(const std::vector<u64>& coordinates)
        : xs(coordinates), tree(4*coordinates.size()), used(4*coordinates.size()) {}

    void add(Line line, int node, int left, int right) {
        if (!used[node]) {
            tree[node]=line; used[node]=1; return;
        }
        int middle=(left+right)/2;
        bool low_left=eval(line,xs[left])<eval(tree[node],xs[left]);
        bool low_middle=eval(line,xs[middle])<eval(tree[node],xs[middle]);
        if (low_middle) std::swap(line,tree[node]);
        if (left==right) return;
        if (low_left!=low_middle) add(line,2*node,left,middle);
        else add(line,2*node+1,middle+1,right);
    }

    void add(Line line) { add(line,1,0,int(xs.size())-1); }

    Line query(int index, int node, int left, int right) const {
        Line answer=tree[node];
        if (left==right) return answer;
        int middle=(left+right)/2;
        Line other=(index<=middle
            ? query(index,2*node,left,middle)
            : query(index,2*node+1,middle+1,right));
        if (other.profile>=0
            && (answer.profile<0 || eval(other,xs[index])<eval(answer,xs[index])))
            answer=other;
        return answer;
    }

    Line query(int index) const { return query(index,1,0,int(xs.size())-1); }
};

int main(int argc, char** argv) {
    int n; if (!(std::cin>>n)) return 2;
    std::vector<std::int8_t> signs(n*n*n);
    for (int i=0;i<n;i++) for (int j=i+1;j<n;j++) for (int k=j+1;k<n;k++) {
        int s; std::cin>>s;
        signs[(i*n+j)*n+k]=s; signs[(j*n+k)*n+i]=s; signs[(k*n+i)*n+j]=s;
        signs[(i*n+k)*n+j]=-s; signs[(k*n+j)*n+i]=-s; signs[(j*n+i)*n+k]=-s;
    }
    int order_count; std::cin>>order_count;
    std::vector<std::pair<u64,u64>> profiles;
    for (int q=0;q<order_count;q++) {
        std::vector<int> order(n);
        for (int& x:order) std::cin>>x;
        auto z=chain_counts(signs,order); profiles.push_back(z);
        std::reverse(order.begin(),order.end());
        profiles.push_back(chain_counts(signs,order));
    }
    std::sort(profiles.begin(),profiles.end());
    profiles.erase(std::unique(profiles.begin(),profiles.end()),profiles.end());
    auto low=*std::min_element(profiles.begin(),profiles.end(),[](auto a,auto b){
        return u128(a.first)*a.second < u128(b.first)*b.second;
    });
    u128 best=~u128(0); std::tuple<u64,u64> wa,wb,wc;
    const u64 W3=11358202734ULL;
    const u64 block=1+n;
    std::vector<u64> xs;
    xs.reserve(profiles.size()*profiles.size());
    for (auto b:profiles) for (auto c:profiles)
        xs.push_back(std::get<1>(b)+block*std::get<1>(c)+block*block);
    std::sort(xs.begin(),xs.end());
    xs.erase(std::unique(xs.begin(),xs.end()),xs.end());
    DiscreteLiChao hull(xs);
    for (int i=0;i<int(profiles.size());i++)
        hull.add({std::get<0>(profiles[i]),std::get<1>(profiles[i]),i});
    const u128 constant=u128(3)*W3+2+u128(block)*block*block;
    for (auto b:profiles) for (auto c:profiles) {
        u64 x=std::get<1>(b)+block*std::get<1>(c)+block*block;
        int xi=int(std::lower_bound(xs.begin(),xs.end(),x)-xs.begin());
        Line line=hull.query(xi);
        auto a=profiles[line.profile];
        u128 v=(constant+eval(line,x)+u128(block)*std::get<1>(b)
            +u128(std::get<0>(b))*std::get<1>(c)
            +u128(block)*std::get<0>(b)
            +u128(block)*block*std::get<1>(c)+std::get<0>(c));
        if (v<best) {best=v;wa=a;wb=b;wc=c;}
    }
    std::cout<<"sampled_profiles="<<profiles.size()
             <<" min_CU=("<<low.first<<","<<low.second<<")"
             <<" product="<<show(u128(low.first)*low.second)<<"\n";
    std::cout<<"W4_sample="<<show(best)<<" witnesses=("
             <<std::get<0>(wa)<<","<<std::get<1>(wa)<<") ("
             <<std::get<0>(wb)<<","<<std::get<1>(wb)<<") ("
             <<std::get<0>(wc)<<","<<std::get<1>(wc)<<")\n";
}
