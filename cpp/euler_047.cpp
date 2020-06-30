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

void compute() {
  fio;
  int t;
  cin >> t;

  while(t--) {
    ui maxNum = 500000;
    ui consecutive = 4;
    cin >> maxNum >>consecutive;

    maxNum += consecutive - 1;

    vector<ui> primeFactors(maxNum + 1, 0);

    // Sieve
    for (ui i = 2; i <= maxNum; i++)
      if (primeFactors[i] == 0)
        for (ui j = i; j <= maxNum; j += i)
          primeFactors[j]++;

    ui cur = 0;
    for (ui i = 2; i <= maxNum; i++) {
      if (primeFactors[i] == consecutive) {
        cur++;

        if (cur >= consecutive)
          cout << (i - consecutive + 1) << endl;
      } else {
        cur = 0;
      }
    }
  }
}

int main() {
  compute();
  return 0;
}