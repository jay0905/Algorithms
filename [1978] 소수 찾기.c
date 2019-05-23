// 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

#include <stdio.h>

int main(void) {
	int N, num, cnt = 0;
	scanf("%d", &N);

	while (N--) {
		scanf("%d", &num);

		if (num > 1) cnt++;
		for (int i = 2; i < num; i++) {
			if (num % i == 0) {
				cnt--;
				break;
			}
		}
	}
	printf("%d", cnt);
}
