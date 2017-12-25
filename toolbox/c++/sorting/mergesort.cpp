#include <iostream>

using namespace std;

/*  == Preconditions ==
		Let A be the following array: int A[sizeof()] = *a;
		Postcondition:
 */
void merge(int *a, int start, int end, int mid)
{
	// We have low to mid and mid+1 to high already sorted
	int i, j, k, temp[start-end+1];
	i = start;
	k = 0;	// Current temp item being pointed to
	j = mid + 1;

	// Merge the two parts into temp[].
	while (i <= mid && j <= end) {
		if (a[i] < a[j]) {
			temp[k] = a[i]; k++; i++;
		} else {
			temp[k] = a[j]; k++; j++;
		}
	}	// In other words, the index k of the last element assigned by this loop
		// will be the index of the last element of the smaller partition.

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
void mergeSort(int *a, int low, int high) {
	if (low < high) {
		int mid=(low+high)/2;
		// Split the data into two half.
		mergeSort(a, low, mid);
		mergeSort(a, mid+1, high);

		// Merge them to get sorted output.
		merge(a, low, high, mid);
	}
}

int main()
{
	int n, i;
	cout<<"\nEnter the number of data element to be sorted: ";
	cin>>n;

	int arr[n];
	for(i = 0; i < n; i++)
	{
		cout<<"Enter element "<<i+1<<": ";
		cin>>arr[i];
	}

	mergeSort(arr, 0, n-1);

	// Printing the sorted data.
	cout<<"\nSorted Data ";
	for (i = 0; i < n; i++)
        cout<<"->"<<arr[i];

	return 0;
}
