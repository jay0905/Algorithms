#include <stdio.h>

int main(void) {
	while (1) {
		int n, i, j, cnt = 0;
		scanf("%d", &n);
		
		for (i = n * 2; i > n; i--) {
			for (j = i - 1; j > 1; j--) {
				if (i % j == 0) break;
			}
			if (j == 1) cnt++;
		}

		printf("%d\n", cnt);
	}
}

// 이렇게 풀었더니 시간 
