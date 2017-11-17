#include <iostream>
#include <string>
#include <vector>

/* Topics
 * Basic I/0, Namespaces 
 * vectors, string [stl]
 */


using namespace std;
int n;
vector<string> statements;

int main() {
	int X = 0;
	cin >> n;
	for(int i=0; i<n; i++) {
		string s; 
		cin >> s;	
		if (s.find("++") == string::npos) {
			X -= 1;
		} else {
			X += 1;
		}
	}
	cout << X;
}
