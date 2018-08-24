#include <iostream>
#include <vector>

using namespace std;

int printCell(int (*field)[10], int row, int col);


int main() {
  vector<int> vec;    // declaring a vector
  cout << sizeof(vec) << " bytes" << endl;
  vec.push_back(0);  // adding an element
  vector<int> vec2(vec); // declare and initialize using elements of vec
  cout << sizeof(vec) << " bytes" << endl;
  
  
  // printCell(n, 9, 10);
  // for (int i = 0; i < 25; i++) {
  //   for (int j = 0; j < 25; j++) {
  //     cout << n[i][j] << " ";
  //   }
  //   cout << endl;
  // }
}

int printCell(int (*field)[10], int row, int col) {
  cout << (*field)[0];
  cout << (*++field)[0];
  return 1;
}