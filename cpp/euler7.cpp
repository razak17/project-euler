#include <iostream>
#include <vector>

using namespace std;

int main() {
  vector<unsigned int> primes;
  primes.reserve(10001);
  primes.push_back(2);
  for (unsigned int i = 3; primes.size() <= 10000; i += 2) {
    bool isPrime = true;
    for (auto p: primes) {
      if (i % p == 0) {
        isPrime = false;
        break;
      }
      if (p * p > i)
        break;
    }
    if (isPrime)
      primes.push_back(i);
  }

  unsigned int tests = 1;
  while (tests--) {
    unsigned int x = 10001;
    x--;

    if (x <primes.size())
      cout << primes[x] << endl;
    else
      cout << "ERROR" << endl;
  }
  return 0;
}