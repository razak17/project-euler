#include <iostream>

using namespace std;

int isPal(int n)
{
  int rev = 0;
  int start = n;

  while (start > 0)
  {
    rev = 10 * rev + start % 10;
    start /= 10;
  }
  return n == rev;
}

long long int largestPalindromeProduct(long long int n)
{
  int max = -1;
  int start = n / 10;
  for (int i = n; i >= start; i--)
  {
    for (int j = n; j >= i; j--)
    {
      int product = i * j;
      if (max < product && isPal(product))
      {
        max = product;
      }
    }
  }
  return max;
}

int main()
{
  cout << largestPalindromeProduct(999) << endl;
}