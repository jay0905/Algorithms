/* 어떤 양의 정수 X의 자리수가 등차수열을 이룬다면, 그 수를 한수라고 한다.
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.*/

#include <stdio.h>

int IsItHansu(int num);

int main(void) {
	int N;
	int count = 0;

	scanf("%d", &N);
	
	for (int i = 1; i <= N; i++) {
		if (IsItHansu(i) == 1) count++;
	} 

	printf("%d", count);
}

int IsItHansu(int num) {
	if (num >= 1 && num < 100) {
		return 1;
	}
	else if (num >= 100 && num < 1000) {
		int first, second, third;
		first = num / 100;
		second = (num / 10 ) % 10;
		third = num % 10;

		if (second - first == third - second) return 1;
		else return 0;
	}
	else return 0;
}
