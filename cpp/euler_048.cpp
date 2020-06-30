#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

#define ll long long
#define ui unsigned int
#define nl cout << endl
#define co(n) cout << n
#define cs(n) cout << n << " "
#define ull unsigned long long
#define cn(n) cout << n << endl
#define all(x) x.begin(), x.end()
#define fio ios_base::sync_with_stdio(false); cin.tie(0); cout.tie()

/* ======================= End of template ========================= */

ull selfPowerLSB(ull num, ull md){
  ull output = 1;
  for(ull k = 0; k < num; ++k){
    output = (output * num) % md;
  }
  return output;
}

void compute() {
  ull output;
    ull upperBound = 10e9;
    for(int k = 1; k <= 1000; ++k){
        // cout << selfPowerLSB(k, upperBound)<<endl;
        output += selfPowerLSB(k, upperBound);
    }
    output = output % upperBound;
    cout<<"The sum is: "<< output<<endl;

}

int main() {
  compute();
  return 0;
}