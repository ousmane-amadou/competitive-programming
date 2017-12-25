#include <iostream>

using namespace std;

int main() {
  int A[9] = {0, 1, 2, 3, 4, 5, 6, 7, 8};
	int* a = A;
	int sizeOfArray = sizeof(A);
	int sizeOfPointer = sizeof(a);
	int sizeOfValueOfPointer = sizeof(*a);

	cout << "Size of Array: " << sizeOfArray << endl;
	cout << "Size of Pointer: " << sizeOfPointer << endl;
	cout << "Size of value of Pointer: " << sizeOfValueOfPointer << endl;
}
