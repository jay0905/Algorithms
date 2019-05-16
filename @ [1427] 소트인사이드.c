#include <stdio.h>

int main(void) {
	int N, temp;
	int arr[10];
	scanf("%d", &N);

	for (int i = 0; N != 0; i++) {
		arr[i] = N % 10;
		N /= 10;
	}
	
	int size = sizeof(arr) / sizeof(int);
	/*
	for (int i = 0; i < size; i++) {
		for (int j = i + 1; j < size; j++) {
			if (arr[i] < arr[j]) {
				temp = arr[i];
				arr[j] = arr[i];
				arr[i] = temp;
			}
		}
	}
	*/
	for (int i = 0; i < size; i++) {
		printf("%d\n", arr[i]);
	}

}
