// N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

#include <stdio.h>

int main(void) {
	int n, total = 0;
	char num[101];

	scanf("%d", &n);
	scanf("%s", &num);

	for (int i = 0; i < n; i++) {
		total += num[i] - '0';
	}
	printf("%d", total);
}

/*
틀렸던 이유:
1 <= n <= 100 인데 num 자료형을 long long 쓰면서 왜 안되냐고 답답해함. 
*/
