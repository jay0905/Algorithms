// N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

#include <stdio.h>

int main(void) {
	int arr[10001] = { 0, }, n, input;

	scanf("%d", &n); // 수의 개수

	for (int i = 0; i < n; i++) {
		scanf("%d", &input);
		arr[input]++;
	}

	for (int i = 0; i < 10001; i++) {
		for (int j = 0; j < arr[i]; j++) {
			printf("%d\n", i);
		}
	}
}
