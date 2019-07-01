// 배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

// 카운팅 정렬을 사용해서 풀이함.

#include <stdio.h>

int main(void) {
	int n, arr[11] = { 0, };
	scanf("%d", &n);
	
	for (int i = 0; n != 0; i++) {
		arr[n % 10]++;
		n /= 10;
	} 

	for (int i = 10; i >= 0; i--) {
		for (int j = 0; j < 10; j++) {
			if (j < arr[i]) printf("%d", i);
		}
	}
}
