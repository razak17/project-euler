#include <iostream>

using namespace std;

int sumOfEvenFibonacciValues(int prev, int current, int limit)
{
  int total = 0;
  while (current <= limit)
  {
    if (current % 2 == 0)
    {
      total += current;
    }
    int temp = current;
    current = current + prev;
    prev = temp;
  }
  return total;
}

int main()
{
  cout << sumOfEvenFibonacciValues(1, 2, 4000000) << endl;
}