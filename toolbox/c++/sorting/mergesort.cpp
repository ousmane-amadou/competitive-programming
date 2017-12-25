#include <iostream>
#include <cmath>

// Merge sort
/**
  *
  */

using namespace std;

const int MAX_INT = 2^31 - 1;

void swap(int &a, int &b) {
	/* Swap's the values of a and b. */
	int temp = a;
	a = b;
	b = temp;
}

// [Precondition] A[start...mid], A[mid+1....end] sorted in non-decreasing order.
// [Postcondition] A[start...end] is sorted in non-decreasing order.
void merge(int A[], int start, int mid, int end) {
	/* */
	int leftSize = mid-start+1;
	int rightSize = end-mid;

	int leftArray[leftSize+1];
	int rightArray[rightSize+1];

	// Copies the subarray A[start...mid] into leftArrray[0...leftSize]
	for(int i = 0; i < leftSize; i++) {	leftArray[i] = A[start + i]; }

	// Copies the subarray A[mid+1...end] into leftArrray[0...rightSize]
	for(int j = 0; j < rightSize; j++) { rightArray[j] = A[mid + 1 + j]; }

	leftArray[leftSize+1] = MAX_INT;
	rightArray[rightSize+1] = MAX_INT;

	int i = 0; int j = 0;
	for(int k = start; k < end; k++){
		if (leftArray[i] <= rightArray[j]) {
				A[k] = leftArray[i]; i++;
		} else {
				A[k] = rightArray[j]; j++;
		}
	}

}

void mergeSort(int* A, int start, int end) {
	/* Sort the subarray A[start...end] using the merge Sort
	 * algorithm. */
	 if( (end - start) > 1 ) {
		 int mid = floor((start + end) / 2);	// Find midpoint
		 mergeSort(A, start, mid);
		 mergeSort(A, mid+1, end);
		 merge(A, start, mid, end);
	 }
}

int main() {
	int arrayInts[] = {4, 1, 2, 3, 5, 6};
	mergeSort(arrayInts, 0, 5);

	for(int i = 0; i < sizeof arrayInts / sizeof arrayInts[0]; i++) {
		cout << arrayInts[i] << ", ";
	}
}
