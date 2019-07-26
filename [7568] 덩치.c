#include <stdio.h>

int main(void) {
	int n, i, j, a[50][2], b[50] = { 0, };
	scanf("%d", &n);

	for (i = 0; i < n; i++) {
		scanf("%d %d", &a[i][0], &a[i][1]);
	}

	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			if (a[i][0] < a[j][0] && a[i][1] < a[j][1]) b[i]++;
		}
	}

	for (i = 0; i < n; i++) printf("%d ", b[i] + 1);
}
