// Scan Aichholzer--Aurenhammer--Krasser coordinate order-type files and
// compute the exact convex-subset rank polynomial by endpoint factorization.
//
// File format: n pairs of unsigned coordinates per record, one byte for b08
// and little-endian two bytes for b16.  The database itself is not vendored.

#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <string>
#include <utility>
#include <vector>

using Point=std::pair<int,int>;

static int orient(const Point&a,const Point&b,const Point&c) {
  int64_t z=int64_t(b.first-a.first)*(c.second-a.second)
           -int64_t(b.second-a.second)*(c.first-a.first);
  if(!z){std::cerr<<"collinear database record\n";std::exit(3);}
  return z>0?1:-1;
}

// profile[k] = number of nonempty convex k-subsets.
static std::vector<uint64_t> profile(std::vector<Point> p) {
  std::sort(p.begin(),p.end()); int n=p.size();
  std::vector<uint64_t> ans(n+1); ans[1]=n;
  // chain[previous][end][length]
  for(int s=0;s<n;s++) {
    uint64_t cap[12][12][13]{},cup[12][12][13]{};
    for(int e=s+1;e<n;e++)cap[s][e][2]=cup[s][e][2]=1;
    for(int mid=s+1;mid<n;mid++)for(int e=mid+1;e<n;e++)
      for(int prev=s;prev<mid;prev++)for(int k=2;k<=n;k++) {
        if(orient(p[prev],p[mid],p[e])<0)cap[mid][e][k+1]+=cap[prev][mid][k];
        else cup[mid][e][k+1]+=cup[prev][mid][k];
      }
    for(int e=s+1;e<n;e++) {
      uint64_t C[13]{},U[13]{};
      for(int prev=s;prev<e;prev++)for(int k=2;k<=n;k++) {
        C[k]+=cap[prev][e][k]; U[k]+=cup[prev][e][k];
      }
      for(int k=2;k<=n;k++)for(int l=2;l<=n;l++)
        if(C[k]&&U[l])ans[k+l-2]+=C[k]*U[l];
    }
  }
  return ans;
}

static uint16_t get16(std::istream&f) {
  unsigned char a,b; f.read((char*)&a,1);f.read((char*)&b,1);
  return uint16_t(a)|(uint16_t(b)<<8);
}

int main(int argc,char**argv) {
  if(argc<4){std::cerr<<"usage: scan_order_types n b08|b16 file\n";return 2;}
  int n=std::atoi(argv[1]); bool wide=std::string(argv[2])=="b16";
  std::ifstream f(argv[3],std::ios::binary);if(!f){std::cerr<<"cannot open file\n";return 2;}
  uint64_t records=0,bestV=std::numeric_limits<uint64_t>::max(),bestM=0,bestCount=0,bestTraceCount=0,bestIndex=0;
  std::map<std::string,uint64_t> minimumProfiles;
  std::vector<Point> bestPoints;std::vector<uint64_t>bestProfile;
  while(true) {
    std::vector<Point> p;
    for(int i=0;i<n;i++) {
      int x,y;
      if(wide) { if(f.peek()==EOF)break;x=get16(f);y=get16(f); }
      else { unsigned char a,b;if(!f.read((char*)&a,1))break;f.read((char*)&b,1);x=a;y=b; }
      p.push_back({x,y});
    }
    if(p.empty())break;if((int)p.size()!=n){std::cerr<<"partial record\n";return 3;}
    auto q=profile(p);uint64_t V=0,M=0;
    for(int k=1;k<=n;k++){V+=q[k];M+=k*q[k];}
    std::string profileKey;
    for(int k=1;k<=n;k++)if(q[k])profileKey+=(profileKey.empty()?"":",")+std::to_string(q[k]);
    if(V<bestV) {
      bestV=V;bestM=M;bestCount=bestTraceCount=1;bestPoints=p;bestProfile=q;bestIndex=records;
      minimumProfiles.clear();minimumProfiles[profileKey]=1;
    } else if(V==bestV) {
      bestTraceCount++;minimumProfiles[profileKey]++;
      if(M<bestM){bestM=M;bestCount=1;bestPoints=p;bestProfile=q;bestIndex=records;}
      else if(M==bestM)bestCount++;
    }
    records++;
  }
  uint64_t raw2=0;for(int k=1;k<=n;k++)raw2+=uint64_t(k)*k*bestProfile[k];
  std::cout<<"{\n  \"mode\": \"exhaustive_realizable_order_type_database\",\n"
    <<"  \"n\": "<<n<<",\n  \"record_count\": "<<records<<",\n"
    <<"  \"minimum_trace\": "<<bestV<<",\n  \"minimum_trace_count_in_database\": "<<bestTraceCount<<",\n  \"lex_minimum_first_moment\": "<<bestM<<",\n"
    <<"  \"lex_minimum_count_in_database\": "<<bestCount<<",\n"
    <<"  \"lex_minimum_record_index_zero_based\": "<<bestIndex<<",\n"
    <<"  \"second_raw_moment_numerator\": "<<raw2<<",\n  \"profile\": [";
  for(int k=0;k<=n;k++){if(k)std::cout<<",";std::cout<<bestProfile[k];}
  std::cout<<"],\n  \"minimum_trace_profile_histogram\": {";
  {bool first=true;for(auto&kv:minimumProfiles){if(!first)std::cout<<",";first=false;std::cout<<"\""<<kv.first<<"\":"<<kv.second;}}
  std::cout<<"},\n  \"coordinates_as_stored\": [";
  for(size_t i=0;i<bestPoints.size();i++){if(i)std::cout<<",";std::cout<<"["<<bestPoints[i].first<<","<<bestPoints[i].second<<"]";}
  std::cout<<"]\n}\n";
}
