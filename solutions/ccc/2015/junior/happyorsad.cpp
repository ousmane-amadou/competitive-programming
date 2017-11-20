#include <iostream>
#include <string>

using namespace std;

string HAPPY = ":-)";
string SAD = ":-(";

int num_occur(string s, string substr) {
  int n = 0;
  int i = s.find(substr);

  while (i != -1) {
    n++;
    i = s.find(substr, i+1);
  }

  return n;
}

int main() {
  string s;
  getline(cin, s);

  int happy = num_occur(s, HAPPY);
  int sad = num_occur(s, SAD);

  if ( (happy == 0) && (sad == 0) ) {
    cout << "none";
  } else if (happy == sad) {
    cout << "unsure";
  } else if (happy > sad) {
    cout << "happy";
  } else {
    cout << "sad";
  }
}
