#include <iostream>

using namespace std;


int n[5][10] = {
  {0, 1, 2, 3, 4, 5, 6, 7, 8, 9},
  {10, 11, 12, 13, 14, 15, 16, 17, 18, 19},
  {20, 21, 22, 23, 24, 25, 26, 27, 28, 29},
  {30, 31, 32, 33, 34, 35, 36, 37, 38, 39},
  {40, 41, 42, 43, 44, 45, 46, 47, 48, 49},
};

int add_one(int *field, int row, int col) {
  int *curr = field;
  curr += row;
  cout << (*++field);
  return 1;
}
int main() {
  add_one((*n));
  // for (int i = 0; i < 25; i++) {
  //   for (int j = 0; j < 25; j++) {
  //     cout << n[i][j] << " ";
  //   }
  //   cout << endl;
  // }
}
