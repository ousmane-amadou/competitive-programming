#include <iostream>
#include <string>

using namespace std;

int main() {
  int d, m;
  cin >> m >> d;

  if (m == 2) {
    if (d == 18) {
      cout << "Special";
    } else if (d < 18 ){
      cout << "Before";
    } else {
      cout << "After";
    }
  } else if (m < 2) {
    cout << "Before";
  } else {
    cout << "After";
  }
}
