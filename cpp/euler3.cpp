#include <iostream>

using namespace std;

long long int highestPrimeFactor(long long int n)
{
  int i = 2;

  while (i * i < n)
  {
    if (n % i == 0)
      n /= i;
    i++;
  }
  return n;
}

int main()
{
  cout << highestPrimeFactor(600851475143) << endl;
  return 0;
}