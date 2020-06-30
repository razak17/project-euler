#include<iostream>
#include<cmath>

using namespace std;

#define ll long long
#define co(n) cout << n << endl
#define ull unsigned long long
#define ui unsigned int
#define all(x) x.begin(), x.end()

bool isPrime(int n) {
  for (int i = 2; i < n; i++) {
    if (n % i == 0) return 0;
  }
  return 1;
}

bool isSquare(int n) {
  int m = sqrt(n);
  return m * m == n;
}

void compute() {
  int oddc = 9, flag;
  while (1) {
    if (isPrime(oddc)) {
      oddc += 2;
      continue;
    }
    for (int p = 3; p < oddc; p++) {
      if (isPrime(p)) {
        if (isSquare((oddc - p) / 2)) {
          printf("oddc: %d, prime: %d\n", oddc, p);
          flag = 1;
          break;
        }
      }
    }
    if (!flag) break;
    oddc += 2;
    flag = 0;
  }
  printf("The Answer is %d .", oddc);
}

int main() {
  compute();
  return 0;
}