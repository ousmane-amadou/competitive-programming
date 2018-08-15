/*
Programming Challenges; 1.6.1 The 3n+1 Problem
Problem Type: Ad hoc
*/

#include <iostream>
using namespace std;

int i = 0, j = 0, mc = 1;

int main() {
  scanf("%d %d", &i, &j);
  for (; i < j; i++) {
    int num = i, cycle = 1;
    while (num > 1) {
      if ((num % 2) == 0) {
        num = num / 2;
      } else {
        num = (num * 3) + 1;
      }
      cycle++;
    }
    mc = max(mc, cycle);
  }
  printf("%d %d %d", i, j, mc);
}
