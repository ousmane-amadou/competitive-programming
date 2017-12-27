#include <iostream>

using namespace std;

void insertionSort(int* a, int n) {
	for(int i = 1; i < n; i++) {
		int key = a[i];
		int j = i-1; 
		
		// Insert a[i] into a[0..i-1]
		while(j > 0 && a[j] > key) {
			a[j+1] = a[j]; j--;
		}
		a[j+1] = key;
	}
}

int main() {
	int size = 4;
	int a[4] = {1, 9, 2, 4};
	insertionSort(a, size);
	
	for(int i = 0; i < size; i++)
		cout << a[i] << ", ";	
}
