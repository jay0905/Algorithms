/* 세 개의 자연수 A, B, C가 주어질 때 A×B×C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

예를 들어 A = 150, B = 266, C = 427 이라면 

A × B × C = 150 × 266 × 427 = 17037300 이 되고, 

계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다. */

// 미완성. 숫자를 거꾸로 배열에 넣는 것까지 성공했으나 끝에 0이 불필요하게 붙음.

#include <stdio.h>

int main(void) {
	int A, B, C, num, last;
	int i = 0;
	int arr[20] = { 0, };

	scanf("%d %d %d", &A, &B, &C);

	num = A * B * C;

	while (num) {
		last = num % 10;
		arr[i] = last;
		num /= 10;
		i++;
	}
	
	for (int i = 0; i < 10; i++) {
		printf("%d", arr[i]);
	}

}
