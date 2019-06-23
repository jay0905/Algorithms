#include <stdio.h>
#include <stdlib.h>

void merge(int *a, int low, int mid, int high) {
	int b[1000000];
	int i = low, j = mid + 1, k = 0;

	while (i <= mid && j <= high) {
		if (a[i] <= a[j]) {
			b[k] = a[i];
			k++;
			i++;
		}
		else {
			b[k] = a[j];
			k++;
			j++;
		}
	}

	// 왼쪽이 살아있다면
	while (i <= mid) {
		b[k] = a[i];
		k++;
		i++;
	}

	// 오른쪽이 살아있다면
	while (j <= high) {
		b[k] = a[j];
		k++;
		j++;
	}

	k--; // k가 빈 곳을 가리키므로

	// 문서작성
	while (k >= 0) {
		a[low + k] = b[k];
		k--;
	}
}

void mergesort(int *a, int low, int high) {
	if (low < high) {
		int m = (low + high) / 2;

		//left
		mergesort(a, low, m);

		//right
		mergesort(a, m + 1, high);

		merge(a, low, m, high);
	}
	else {
		return;
	}
}

int main() {
	int n, i;
	scanf("%d", &n);

	int *a = (int*)malloc(sizeof(int) * n);

	for (i = 0; i < n; i++) {
		scanf("%d", &a[i]);
	}

	mergesort(a, 0, n - 1);

	for (i = 0; i < n; i++) {
		printf("%d\n", a[i]);
	}

	free(a);

	return 0;
}

// 병합정렬 구현 연습
// 포인터 사용시 헷갈리는 부분 잡아야 할 
