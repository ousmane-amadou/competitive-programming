#include <iostream>

using namespace std;

/* === Preconditions ==
 * Suppose A is the array represented by the pointer a.
 *  - A[start...mid] is sorted in non decreasing order.
 *	- A[mid+1...end] is sorted in non descreasing order.
 * === Postcondition ===
 * - A[start...end] will be sorted in non decreasing order.
 */
void merge(int *a, int start, int end, int mid) {
	/* Merges two sorted subarray's A[start...mid] and A[mid...start] into
	 * a fully sorted array A[start...end] */

	int i, j, k, temp[end-start+1]; // Allocate memory needed for merge procedure
	
	i = start;	  // 1. Set current left array item to A[start]
	k = 0;		   	// 2. Set current temp array item to temp[0]
	j = mid + 1;  // 3. Set current right array item to A[mid+1]

	// Merge
	while (i <= mid && j <= end) {
		if (a[i] < a[j]) {
			temp[k] = a[i]; k++; i++;
		} else {
			temp[k] = a[j]; k++; j++;
		}
	}	// Loop Invariant(s): 
		// - temp[0..k] = sorted(A[start...start+k])
		// - k <= min(end-mid+1, mid-start)
		//   In other words, the index k of the last element assigned by this loop
		//   will be the index of the last element of the smaller partition.

	// Insert all the remaining values from i to mid into temp[].
	while (i <= mid) {
		temp[k] = a[i]; k++; i++;
	}
	// Insert all the remaining values from j to high into temp[].
	while (j <= end) {
		temp[k] = a[j]; k++; j++;
	}

	// Assign sorted data stored in temp[] to a[].
	for (i = start; i <= end; i++) {
		a[i] = temp[i-start];
	}
}

// A function to split array into two parts.
void mergeSort(int *a, int start, int end) {
	if (start < end) {
		int mid=(start+end)/2;
		// Split the data into two half.
		mergeSort(a, start, mid);
		mergeSort(a, mid+1, end);

		// Merge them to get sorted output.
		merge(a, start, end, mid);
	}
}

int main() {
	int arr[] = {9, 8, 2, 1, 3, 4, 5};

	mergeSort(arr, 0, 6);
	
	// Printing the sorted data.
	cout<<"\nSorted Data ";
	for (int i = 0; i < 6; i++)
        cout << arr[i] << ", ";

	return 0;
}
