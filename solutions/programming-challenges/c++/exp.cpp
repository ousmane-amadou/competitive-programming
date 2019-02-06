#include <iostream>
#include <set>

using namespace std;

int main() {
	set<int> mySet;

	mySet.insert(3);

	cout << mySet.count(3) << endl;
}
