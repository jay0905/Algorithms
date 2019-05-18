#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int T, M, N, x, y, valid = 0;
	scanf("%d", &T);

	for (int i = 0; i < T; i++) {
		scanf("%d %d %d %d", &M, &N, &x, &y);

		int *arr = malloc(sizeof(int) * M); // x에 따른 y 값을 넣어두는 배열
		arr[0] = x;
		for (int i = 1; i < M; i++) {
			arr[i] = arr[i - 1] + M - 1;
			if (arr[i] >= N) arr[i] -= N - 1;
			if (arr[i] == y) valid++;
		}

		if (y == x || valid > 0) {
			printf("%d\n", (x - 1) * N + y);
		}
		else printf("-1\n");

		free(arr);
	}
}
