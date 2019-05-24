// 왜 안돼...

#include <stdio.h>

int main(void) {
	int m, n, i, j; 
	int total = 0, min = 0;
	scanf("%d %d", &m, &n);
	
	for (i = m; i <= n; i++) {
		for (j = 2; j < m; j++) {
			if (m % j == 0) break;
		}
		if (m == j) {
			total += j;
			if (j < min) min = j;
		}
	}
	if (total == 0) printf("-1 ");
	else printf("%d\n%d", total, min);

}
