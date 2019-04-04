// 세 정수 A, B, C가 주어진다.이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오.

#include <stdio.h>

int main() {
	int a, b, c, i, j;
	int arr[3];

	scanf("%d %d %d", &a, &b, &c);

	arr[0] = a;
	arr[1] = b;
	arr[2] = c;

	for (i = 0; i < 3; i++) {
		int temp;
		for (j = i; j < 2; j++) {
			if (arr[i] < arr[j + 1]) {
				temp = arr[i];
				arr[i] = arr[j + 1];
				arr[j + 1] = temp;
			}
		}
	}
	printf("%d", arr[1]);
  
	return 0;
}
