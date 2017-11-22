#include <iostream>
#include <cstdio>

using namespace std;

/* Practice: Working with Numbers */
// int | (-2^32, 2^32 -1) | 32 bit
// long long | (-2^64, 2^32 -1) | 64 bit

long long x, y;
int main() {
  while (cin >> x >> y) {
    cout << abs(x-y) << endl;
  }
  return 0;
}
